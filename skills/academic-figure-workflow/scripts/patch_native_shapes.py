"""Merge selected standalone native shapes; preserve the rest of the baseline package."""
import argparse,copy,json,sys,xml.etree.ElementTree as E
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from audit_pptx import NS,size,parts,shape_map,native_name,matches,canonical

def patch(baseline,replacement,output,slides,prefixes=(),names=(),allow_remove=False):
    output=Path(output)
    if output.exists():raise ValueError('Use a new output path; output already exists')
    if not prefixes and not names:raise ValueError('Select a narrow --prefix or exact --name')
    changed={};report=[]
    with ZipFile(baseline) as src,ZipFile(replacement) as rep:
        if size(src)!=size(rep):raise ValueError('Baseline and replacement physical canvas sizes differ')
        bp=parts(src);rp=parts(rep)
        if not slides or len(slides)!=len(set(slides)):raise ValueError('Select unique 1-based slide numbers')
        for i in slides:
            if i<1 or i>min(len(bp),len(rp)):raise ValueError('Slide out of range')
            root=E.fromstring(src.read(bp[i-1]));newroot=E.fromstring(rep.read(rp[i-1]));tree=root.find('p:cSld/p:spTree',NS)
            old=shape_map(root);new=shape_map(newroot)
            selected={n:el for n,el in new.items() if matches(n,prefixes,names)}
            originals={n:el for n,el in old.items() if matches(n,prefixes,names)}
            if not selected:raise ValueError(f'Slide {i}: no selected replacements')
            if not originals:raise ValueError(f'Slide {i}: no baseline anchor; creation belongs to normal authoring')
            if not allow_remove and set(originals)-set(selected):raise ValueError('Selected originals absent from replacement; use --allow-remove for intentional deletion')
            for n,el in {**originals,**selected}.items():
                if el.tag!='{'+NS['p']+'}sp':raise ValueError('Only standalone shapes/text supported: '+n)
                if any(k.startswith('{'+NS['r']+'}') for e in el.iter() for k in e.attrib):raise ValueError('Replacement needs relationship mapping: '+n)
            untouched=[(el,canonical(el)) for el in tree if native_name(el) not in originals]
            maxid=max(int(e.get('id')) for e in root.findall('.//p:cNvPr',NS));inserted={};updated=[];removed=[]
            for n,el in originals.items():
                at=list(tree).index(el)
                if n in selected:
                    item=copy.deepcopy(selected[n]);item.find('p:nvSpPr/p:cNvPr',NS).set('id',el.find('p:nvSpPr/p:cNvPr',NS).get('id'))
                    tree.remove(el);tree.insert(at,item);inserted[n]=item;updated.append(n)
                else:tree.remove(el);removed.append(n)
            ordered=list(selected);added=[]
            for ix,n in enumerate(ordered):
                if n in inserted:continue
                before=[inserted[x] for x in ordered[:ix] if x in inserted]
                after=[inserted[x] for x in ordered[ix+1:] if x in inserted]
                if before:at=list(tree).index(before[-1])+1
                elif after:at=list(tree).index(after[0])
                else:raise ValueError('No retained insertion anchor')
                item=copy.deepcopy(selected[n]);maxid+=1;item.find('p:nvSpPr/p:cNvPr',NS).set('id',str(maxid))
                tree.insert(at,item);inserted[n]=item;added.append(n)
            for el,before in untouched:
                if canonical(el)!=before:raise ValueError('Untouched object changed')
            changed[bp[i-1]]=E.tostring(root,encoding='UTF-8',xml_declaration=True)
            report.append({'slide':i,'updated':updated,'added':added,'removed':removed,'preserved_objects':len(untouched)})
        # Complete validation before creating output; no half-written output on selection failure.
        with ZipFile(output,'w',ZIP_DEFLATED) as dst:
            for info in src.infolist():dst.writestr(info,changed.get(info.filename,src.read(info.filename)))
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('baseline','replacement','output'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--slide',type=int,action='append',required=True);p.add_argument('--prefix',action='append',default=[]);p.add_argument('--name',action='append',default=[]);p.add_argument('--allow-remove',action='store_true')
    a=p.parse_args()
    try:print(json.dumps(patch(a.baseline,a.replacement,a.output,a.slide,a.prefix,a.name,a.allow_remove),indent=2))
    except (ValueError,KeyError,E.ParseError,OSError) as e:print(str(e),file=sys.stderr);sys.exit(1)
