"""Behavioral tests against real PPT packages, including refusal/failure cases."""
import copy,sys,unittest,tempfile,xml.etree.ElementTree as E,struct,zlib
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
scripts=Path(__file__).resolve().parents[1]/'scripts';sys.path.insert(0,str(scripts))
from audit_pptx import audit,NS,parts,shape_map,box,alignment,arrow_style
from patch_native_shapes import patch
from png_dpi import stamp_png

SOURCE=None
def modified(source,dest,part,edit):
    with ZipFile(source) as z,ZipFile(dest,'w',ZIP_DEFLATED) as out:
        for info in z.infolist():
            raw=z.read(info.filename)
            if info.filename==part:
                root=E.fromstring(raw);edit(root);raw=E.tostring(root,encoding='UTF-8',xml_declaration=True)
            out.writestr(info,raw)

class Packages(unittest.TestCase):
    def test_native_and_final_size_font_failure(self):
        self.assertTrue(audit(SOURCE,require_native=True,min_font_pt=9)['mechanical_pass'])
        self.assertFalse(audit(SOURCE,min_font_pt=9,target_width_mm=45)['mechanical_pass'])
    def test_wrong_font_fails(self):self.assertFalse(audit(SOURCE,font='A nonexistent font')['mechanical_pass'])
    def test_selected_patch_preserves_everything_else(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            with ZipFile(SOURCE) as z:p=parts(z)[0];names=list(shape_map(E.fromstring(z.read(p))))
            selected=next(n for n in names if 'label' in n)
            def move(root):shape_map(root)[selected].find('p:spPr/a:xfrm/a:off',NS).set('x','360000')
            rep=d/'replacement.pptx';modified(SOURCE,rep,p,move)
            out=d/'patched.pptx';patch(SOURCE,rep,out,[1],names=[selected])
            self.assertTrue(audit(out,baseline=SOURCE,allow_name=[selected])['mechanical_pass'])
            self.assertFalse(audit(out,baseline=SOURCE)['mechanical_pass'])
            with self.assertRaises(ValueError):patch(SOURCE,rep,out,[1],names=[selected])
    def test_mismatched_canvas_rejected_without_output(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d);rep=d/'wrong.pptx';out=d/'should-not-exist.pptx'
            def resize(root):root.find('p:sldSz',NS).set('cx','360000')
            modified(SOURCE,rep,'ppt/presentation.xml',resize)
            with self.assertRaises(ValueError):patch(SOURCE,rep,out,[1],prefixes=['title'])
            self.assertFalse(out.exists())
    def test_new_selected_shape_has_unique_id(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def add(root):
                el=copy.deepcopy(shape_map(root)['pool-label']);pr=el.find('p:nvSpPr/p:cNvPr',NS)
                pr.set('name','pool-label-extra');pr.set('id','99999');root.find('p:cSld/p:spTree',NS).append(el)
            rep=d/'extra.pptx';modified(SOURCE,rep,p,add);out=d/'patched.pptx'
            patch(SOURCE,rep,out,[1],prefixes=['pool-label'])
            with ZipFile(out) as z:
                root=E.fromstring(z.read(p));ids=[el.get('id') for el in root.findall('.//p:cNvPr',NS)]
                self.assertEqual(len(ids),len(set(ids)));self.assertIn('pool-label-extra',shape_map(root))
            self.assertTrue(audit(out,baseline=SOURCE,allow_prefix=['pool-label'])['mechanical_pass'])
    def test_relationship_bearing_replacement_is_refused(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def add_ref(root):shape_map(root)['pool-label'].set('{'+NS['r']+'}id','rId999')
            rep=d/'reference.pptx';modified(SOURCE,rep,p,add_ref);out=d/'should-not-exist.pptx'
            with self.assertRaises(ValueError):patch(SOURCE,rep,out,[1],names=['pool-label'])
            self.assertFalse(out.exists())
    def test_intentional_removal_is_explicit(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def remove(root):root.find('p:cSld/p:spTree',NS).remove(shape_map(root)['pool-label'])
            rep=d/'removed.pptx';modified(SOURCE,rep,p,remove);out=d/'removed-output.pptx'
            with self.assertRaises(ValueError):patch(SOURCE,rep,out,[1],prefixes=['pool'])
            patch(SOURCE,rep,out,[1],prefixes=['pool'],allow_remove=True)
            self.assertTrue(audit(out,baseline=SOURCE,allow_prefix=['pool'])['mechanical_pass'])
    def test_relative_alignment_detects_shift(self):
        tokens=['1/pool-label@pool','1/surrogate-label@surrogate']
        self.assertTrue(alignment(SOURCE,tokens,0)[0])
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def shift(root):shape_map(root)['pool-label'].find('p:spPr/a:xfrm/a:off',NS).set('x','999999')
            out=Path(d)/'misaligned.pptx';modified(SOURCE,out,p,shift)
            self.assertFalse(alignment(out,tokens,0)[0])
    def test_uniform_arrow_style_detects_weight_change(self):
        tokens=['1/pool-to-surrogate','1/surrogate-to-acquisition','1/measurement-update']
        self.assertTrue(arrow_style(SOURCE,tokens)[0])
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def thicken(root):shape_map(root)['pool-to-surrogate'].find('p:spPr/a:ln',NS).set('w','36000')
            out=Path(d)/'thick-arrow.pptx';modified(SOURCE,out,p,thicken)
            self.assertFalse(arrow_style(out,tokens)[0])
    def test_oversized_raster_preview_does_not_pass_native(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d)
            with ZipFile(SOURCE) as z:p=parts(z)[0]
            def flatten(root):
                tree=root.find('p:cSld/p:spTree',NS)
                for el in list(tree):
                    if el.tag=='{'+NS['p']+'}sp':tree.remove(el)
            out=d/'no-native.pptx';modified(SOURCE,out,p,flatten)
            self.assertFalse(audit(out,require_native=True)['mechanical_pass'])
    def test_png_pixels_are_preserved(self):
        def chunk(t,d):return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
        data=zlib.compress(b'\x00\xff\x00\x00')
        raw=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',1,1,8,2,0,0,0))+chunk(b'IDAT',data)+chunk(b'IEND',b'')
        stamped=stamp_png(raw,600)
        self.assertIn(chunk(b'IDAT',data),stamped)
        self.assertEqual(stamped.count(b'pHYs'),1)
        self.assertEqual(stamp_png(stamped,600),stamped)
        with self.assertRaises(ValueError):stamp_png(b'not png',600)

if __name__=='__main__':
    if len(sys.argv)<2:raise SystemExit('Usage: python test_pptx_tools.py native-fixture.pptx')
    SOURCE=Path(sys.argv.pop(1)).resolve();unittest.main()
