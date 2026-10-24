"""Mechanical PPT figure checks; visual/scientific review is always separate."""
import argparse,json,math,posixpath,sys,xml.etree.ElementTree as E
from pathlib import Path
from zipfile import ZipFile

NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
EMU_MM=36000
def canonical(el):return E.canonicalize(E.tostring(el,encoding='unicode'))
def native_name(el):
    c=el.find('.//p:cNvPr',NS)
    return c.get('name','') if c is not None else ''
def size(z):
    s=E.fromstring(z.read('ppt/presentation.xml')).find('p:sldSz',NS)
    return int(s.get('cx')),int(s.get('cy'))
def parts(z):
    rel=E.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
    ids={r.get('Id'):posixpath.normpath(posixpath.join('ppt',r.get('Target'))) if not r.get('Target').startswith('/') else r.get('Target').lstrip('/') for r in rel}
    p=E.fromstring(z.read('ppt/presentation.xml'))
    return [ids[s.get('{'+NS['r']+'}id')] for s in p.findall('p:sldIdLst/p:sldId',NS)]
def shape_map(root):
    tree=root.find('p:cSld/p:spTree',NS);out={}
    for el in tree:
        n=native_name(el)
        if not n:continue
        if n in out:raise ValueError('Duplicate shape name: '+n)
        out[n]=el
    return out
def box(el):
    x=el.find('p:spPr/a:xfrm',NS)
    if x is None:x=el.find('p:grpSpPr/a:xfrm',NS)
    if x is None:raise ValueError('No supported native transform: '+native_name(el))
    o=x.find('a:off',NS);s=x.find('a:ext',NS)
    return tuple(int(o.get(k)) for k in ('x','y'))+tuple(int(s.get(k)) for k in ('cx','cy'))
def matches(name,prefixes,names):return name in names or any(name.startswith(p) for p in prefixes)

def audit(path,min_font_pt=None,target_width_mm=None,font=None,text_color=None,require_native=False,baseline=None,allow_prefix=(),allow_name=(),allow_part=()):
    errors=[];slides=[]
    with ZipFile(path) as z:
        if len(z.namelist())!=len(set(z.namelist())):errors.append('Duplicate ZIP members')
        bad=z.testzip()
        if bad:errors.append('Corrupt ZIP member: '+bad)
        sx,sy=size(z);width=sx/EMU_MM;factor=(target_width_mm/width if target_width_mm else 1)
        roots={p:E.fromstring(z.read(p)) for p in parts(z)}
        for i,(part,r) in enumerate(roots.items(),1):
            sizes=[];families=set();colors=set();unknown=0;texts=0;native=0
            try:shape_map(r)
            except ValueError as e:errors.append(str(e))
            for sh in r.findall('.//p:sp',NS):
                # Visible structural objects, rather than invisible textbox rectangles.
                props=sh.find('p:spPr',NS)
                if props is not None and (props.find('a:solidFill',NS) is not None or props.find('a:ln/a:solidFill',NS) is not None):native+=1
                body=sh.find('p:txBody',NS)
                if body is None:continue
                for paragraph in body.findall('a:p',NS):
                    default=paragraph.find('a:pPr/a:defRPr',NS)
                    for run in list(paragraph):
                        t=run.find('a:t',NS)
                        if t is None or not t.text:continue
                        texts+=1;pr=run.find('a:rPr',NS)
                        if pr is None:pr=default
                        def prop(attr):
                            return (pr.get(attr) if pr is not None else None) or (default.get(attr) if default is not None else None)
                        fs=prop('sz')
                        if fs:sizes.append(int(fs)/100*factor)
                        else:unknown+=1
                        for tag,target,attr in [('a:latin',families,'typeface'),('a:solidFill/a:srgbClr',colors,'val')]:
                            node=pr.find(tag,NS) if pr is not None else None
                            if node is None and default is not None:node=default.find(tag,NS)
                            target.add(node.get(attr) if node is not None else '<inherited/unresolved>')
            pics=r.findall('.//p:pic',NS);full=0
            for pic in pics:
                try:
                    x,y,w,h=box(pic)
                    if w*h/(sx*sy)>.9:full+=1
                except ValueError:pass
            if min_font_pt is not None and (unknown or not sizes or min(sizes)+.005<min_font_pt):errors.append(f'Slide {i}: final-size type below {min_font_pt}pt or unresolved')
            if font and families!={font}:errors.append(f'Slide {i}: font policy mismatch: {sorted(families)}')
            if text_color and colors!={text_color.upper().lstrip("#")}:errors.append(f'Slide {i}: text color policy mismatch: {sorted(colors)}')
            if require_native and (native==0 or texts==0 or (full and native<3)):errors.append(f'Slide {i}: native mechanism editability not demonstrated')
            slides.append({'slide':i,'part':part,'native_visual_shapes':native,'text_runs':texts,'photos_or_rasters':len(pics),'full_canvas_rasters':full,'font_pt_min_at_insertion':min(sizes) if sizes else None,'unresolved_font_runs':unknown,'font_families':sorted(families),'text_colors':sorted(colors)})
        if baseline:
            with ZipFile(baseline) as old:
                if size(old)!=(sx,sy):errors.append('Baseline canvas size changed')
                oldparts=parts(old)
                for p in set(old.namelist())|set(z.namelist()):
                    if p in allow_part:continue
                    if p in roots and p in oldparts:
                        before=E.fromstring(old.read(p));a=shape_map(before);b=shape_map(roots[p])
                        for n in set(a)|set(b):
                            if matches(n,allow_prefix,allow_name):continue
                            if n not in a or n not in b or canonical(a[n])!=canonical(b[n]):errors.append(f'Untouched native object changed: {p}/{n}')
                        # Also preserve slide properties, background and other non-shape content.
                        tree=before.find('p:cSld/p:spTree',NS)
                        for el in list(tree):
                            if native_name(el):tree.remove(el)
                        after=E.fromstring(z.read(p));tree=after.find('p:cSld/p:spTree',NS)
                        for el in list(tree):
                            if native_name(el):tree.remove(el)
                        if canonical(before)!=canonical(after):errors.append('Non-shape slide content changed: '+p)
                    elif p not in old.namelist() or p not in z.namelist() or old.read(p)!=z.read(p):errors.append('Unpermitted package part changed: '+p)
        return {'file':str(Path(path).resolve()),'width_mm':width,'height_mm':sy/EMU_MM,'target_width_mm':target_width_mm or width,'slides':slides,'errors':errors,'mechanical_pass':not errors,'visual_review_required':True}

def alignment(path,groups,axis):
    values=[]
    with ZipFile(path) as z:
        maps={i:shape_map(E.fromstring(z.read(p))) for i,p in enumerate(parts(z),1)}
        for token in groups:
            slide,expr=token.split('/',1);names=expr.split('@');m=maps[int(slide)];v=box(m[names[0]])
            if axis in (0,1):
                if len(names)!=2:raise ValueError('Relative alignment needs slide/object@frame')
                v=v[axis]-box(m[names[1]])[axis]
            else:v=v[2]
            values.append(v)
    return max(values)-min(values)<=.02*EMU_MM,values

def arrow_style(path,groups):
    values=[]
    with ZipFile(path) as z:
        maps={i:shape_map(E.fromstring(z.read(p))) for i,p in enumerate(parts(z),1)}
        for token in groups:
            slide,name=token.split('/',1);m=maps[int(slide)]
            line=m[name].find('p:spPr/a:ln',NS)
            if line is None:raise ValueError('Arrow has no native shaft: '+token)
            head=m.get(name+'-head')
            if head is None:raise ValueError('Custom head not found; inspect native end styles visually: '+token)
            p=head.find('p:spPr/a:custGeom/a:pathLst/a:path',NS)
            if p is None:raise ValueError('Unsupported head geometry: '+token)
            _,_,w,h=box(head);pw=float(p.get('w'));ph=float(p.get('h'))
            points=[(float(pt.get('x'))*w/pw,float(pt.get('y'))*h/ph) for pt in p.findall('.//a:pt',NS)]
            if len(points)!=3:raise ValueError('Expected a native triangular head: '+token)
            lengths=sorted(math.dist(points[i],points[(i+1)%3]) for i in range(3))
            values.append([int(line.get('w','0')),*lengths])
    return all(max(row[i] for row in values)-min(row[i] for row in values)<=.02*EMU_MM for i in range(4)),values

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pptx',type=Path)
    p.add_argument('--min-font-pt',type=float);p.add_argument('--target-width-mm',type=float);p.add_argument('--font');p.add_argument('--text-color');p.add_argument('--require-native',action='store_true')
    p.add_argument('--baseline',type=Path);p.add_argument('--allow-prefix',action='append',default=[]);p.add_argument('--allow-name',action='append',default=[]);p.add_argument('--allow-part',action='append',default=[])
    for opt in ('same-relative-x','same-relative-y','same-width'):p.add_argument('--'+opt,nargs='+',action='append',default=[],help='Native selectors: slide/object@frame (width needs slide/object)')
    p.add_argument('--same-arrow-style',nargs='+',action='append',default=[],help='Compare shaft weight and triangular head geometry using slide/shaft; semantic colors may differ')
    p.add_argument('--report',type=Path);a=p.parse_args()
    if a.target_width_mm is not None and a.target_width_mm<=0:p.error('Target width must be positive')
    try:
        report=audit(a.pptx,a.min_font_pt,a.target_width_mm,a.font,a.text_color,a.require_native,a.baseline,a.allow_prefix,a.allow_name,a.allow_part)
        for field,axis in [('same_relative_x',0),('same_relative_y',1),('same_width',2)]:
            for group in getattr(a,field):
                passed,values=alignment(a.pptx,group,axis)
                if not passed:report['errors'].append(f'{field}: {group}: EMU values {values}')
        for group in a.same_arrow_style:
            passed,values=arrow_style(a.pptx,group)
            if not passed:report['errors'].append(f'Arrow style differs: {group}: EMU values {values}')
        report['mechanical_pass']=not report['errors']
    except (ValueError,KeyError,E.ParseError,OSError) as e:report={'mechanical_pass':False,'errors':[str(e)],'visual_review_required':True}
    result=json.dumps(report,ensure_ascii=False,indent=2)
    if a.report:a.report.write_text(result,encoding='utf-8')
    print(result);return 0 if report['mechanical_pass'] else 1
if __name__=='__main__':sys.exit(main())
