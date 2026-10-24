// Native scientific diagrams: millimeters for geometry, points for typography.
// Supply the current artifact-tool module; this file embeds no runtime paths.
const PX_PER_MM=96/25.4, PX_PER_PT=96/72;
const positive=(v,n)=>{if(!Number.isFinite(v)||v<=0)throw new Error(`${n} must be positive`);return v;};
const finite=(v,n)=>{if(!Number.isFinite(v))throw new Error(`${n} must be finite`);return v;};
export function gridCells({x,y,width,height,rows,cols,gapX=0,gapY=gapX}){
  if(!Number.isInteger(rows)||!Number.isInteger(cols)||rows<1||cols<1)throw new Error('Positive integer rows and cols required');
  const w=(width-gapX*(cols-1))/cols,h=(height-gapY*(rows-1))/rows;
  positive(w,'cell width');positive(h,'cell height');
  return Array.from({length:rows*cols},(_,i)=>({x:x+(i%cols)*(w+gapX),y:y+Math.floor(i/cols)*(h+gapY),width:w,height:h}));
}
export function viewport(bounds,box){
  const [x0,y0,x1,y1]=bounds;
  positive(x1-x0,'data width');positive(y1-y0,'data height');
  positive(box.width,'viewport width');positive(box.height,'viewport height');
  const scale=Math.min(box.width/(x1-x0),box.height/(y1-y0));
  const ox=box.x+(box.width-scale*(x1-x0))/2,oy=box.y+(box.height-scale*(y1-y0))/2;
  return {scale,point:([x,y])=>[ox+(x-x0)*scale,oy+(y-y0)*scale],x:v=>ox+(v-x0)*scale,y:v=>oy+(v-y0)*scale};
}
export function createFigure({widthMm,heightMm,style},artifact){
  positive(widthMm,'widthMm');positive(heightMm,'heightMm');
  if(!style?.font)throw new Error('Select a concrete style.font before authoring');
  const st={fontPt:9.5,ink:'#000000',outline:'#8A8A8A',canvas:'#FFFFFF',lineMm:.22,arrowMm:.28,headMm:1.15,headRatio:.44,...style};
  for(const k of ['fontPt','lineMm','arrowMm','headMm','headRatio'])positive(st[k],k);
  if(!artifact?.Presentation||!artifact?.PresentationFile)throw new Error('Pass the current artifact-tool module');
  const presentation=artifact.Presentation.create({slideSize:{width:widthMm*PX_PER_MM,height:heightMm*PX_PER_MM}});
  function addCanvas({background=st.canvas}={}){
    const slide=presentation.slides.add();slide.background.fill=background;
    const names=new Set();
    const take=n=>{if(!n||names.has(n))throw new Error(`Missing or duplicate native object name: ${n}`);names.add(n);};
    const pos=(x,y,w,h)=>({left:finite(x,'x')*PX_PER_MM,top:finite(y,'y')*PX_PER_MM,width:positive(w,'width')*PX_PER_MM,height:positive(h,'height')*PX_PER_MM});
    function shape(name,geometry,x,y,w,h,o={}){
      take(name);return slide.shapes.add({name,geometry,position:pos(x,y,w,h),fill:o.fill??'none',line:{fill:o.stroke??st.outline,width:(o.lineMm??st.lineMm)*PX_PER_MM,style:o.dashed?'dashed':'solid'}});
    }
    function path(name,points,o={}){
      if(points.length<2||points.some(p=>p.length!==2||p.some(v=>!Number.isFinite(v))))throw new Error('A path needs finite points');
      take(name);
      const x=Math.min(...points.map(p=>p[0])),y=Math.min(...points.map(p=>p[1]));
      const w=Math.max(.001,Math.max(...points.map(p=>p[0]))-x),h=Math.max(.001,Math.max(...points.map(p=>p[1]))-y);
      const commands=points.map((p,i)=>({[i?'lineTo':'moveTo']:{x:(p[0]-x)*PX_PER_MM,y:(p[1]-y)*PX_PER_MM}}));
      if(o.closed)commands.push({close:{}});
      return slide.shapes.add({name,geometry:'custom',position:pos(x,y,w,h),fill:o.fill??'none',line:{fill:o.stroke??st.ink,width:(o.lineMm??st.lineMm)*PX_PER_MM},customPaths:[{width:w*PX_PER_MM,height:h*PX_PER_MM,commands}]});
    }
    function head(name,from,to,o={}){
      const length=Math.hypot(to[0]-from[0],to[1]-from[1]);
      if(length<1e-9)throw new Error('Arrow tangent must be nonzero');
      const u=(to[0]-from[0])/length,v=(to[1]-from[1])/length,k=o.headMm??st.headMm,r=o.headRatio??st.headRatio;
      return path(name,[to,[to[0]-k*u+k*r*v,to[1]-k*v-k*r*u],[to[0]-k*u-k*r*v,to[1]-k*v+k*r*u]],{closed:true,fill:o.stroke??st.ink,stroke:'none',lineMm:0});
    }
    function arrow(name,points,o={}){
      if(points.length<2||Math.hypot(points.at(-1)[0]-points.at(-2)[0],points.at(-1)[1]-points.at(-2)[1])<(o.headMm??st.headMm))throw new Error('Final arrow segment must accommodate its head');
      const shaft=path(name,points,{...o,lineMm:o.lineMm??st.arrowMm});
      head(name+'-head',points.at(-2),points.at(-1),o);return shaft;
    }
    function bezier(name,points,o={}){
      if(points.length!==4)throw new Error('Cubic Bezier needs four control points');
      const [a,b,c,d]=points;
      // Match shaft and head to the exact endpoint tangent, in the same arrow family.
      if(Math.hypot(d[0]-c[0],d[1]-c[1])<1e-9)throw new Error('Bezier endpoint tangent must be nonzero');
      const sampled=Array.from({length:65},(_,i)=>{const t=i/64,u=1-t;return [0,1].map(j=>u**3*a[j]+3*u*u*t*b[j]+3*u*t*t*c[j]+t**3*d[j]);});
      const shaft=path(name,sampled,{...o,lineMm:o.lineMm??st.arrowMm});
      head(name+'-head',c,d,o);return shaft;
    }
    function text(name,value,x,y,w,h,o={}){
      const fontPt=o.fontPt??st.fontPt;
      positive(fontPt,'fontPt');
      const minimumHeight=(fontPt*25.4/72)*1.2*String(value).split('\n').length+.3;
      const height=Math.max(h,minimumHeight),top=y-(height-h)/2;
      const z=shape(name,'textbox',x,top,w,height,{fill:'none',stroke:'none',lineMm:0});
      z.text=String(value);z.text.style={typeface:o.font??st.font,fontSize:fontPt*PX_PER_PT,color:o.color??st.ink,bold:o.bold??false,italic:o.italic??false,alignment:o.align??'center',verticalAlignment:'middle',wrap:o.wrap?'square':'none',autoFit:'none',insets:{top:0,right:0,bottom:0,left:0}};
      return z;
    }
    return {slide,style:st,text,path,arrow,bezier,shape,
      rect:(n,x,y,w,h,o={})=>shape(n,o.rounded?'roundRect':'rect',x,y,w,h,o),
      ellipse:(n,x,y,w,h,o={})=>shape(n,'ellipse',x,y,w,h,o),
      notes:value=>slide.speakerNotes.textFrame.setText(value)};
  }
  return {presentation,style:st,widthMm,heightMm,addCanvas,
    saveDraft:async file=>(await artifact.PresentationFile.exportPptx(presentation)).save(file)};
}
