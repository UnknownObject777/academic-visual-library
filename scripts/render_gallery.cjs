const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const root = process.argv[2];
if (!root) throw new Error('Pass plugin root');
const assets = path.join(root,'assets');
const gallery = path.join(assets,'gallery'); fs.mkdirSync(gallery,{recursive:true});
const catalogue = JSON.parse(fs.readFileSync(path.join(assets,'catalog.json'),'utf8'));
const esc = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
(async () => {
 for(let page=0; page<2; page++) {
  const models=catalogue.models.slice(page*20,(page+1)*20); const layers=[];
  for(let i=0;i<models.length;i++) {
   const m=models[i], x=(i%4)*400, y=Math.floor(i/4)*300;
   const img=await sharp(path.join(root,m.preview)).resize(360,235,{fit:'inside',background:'white'}).png().toBuffer();
   const meta=await sharp(img).metadata();
   layers.push({input:img,left:x+Math.round((400-meta.width)/2),top:y+50});
   const label=Buffer.from(`<svg width="400" height="42"><rect width="400" height="42" fill="#F1F5F9"/><text x="10" y="26" font-family="Arial" font-size="17" fill="#24323D">${page*20+i+1}. ${esc(m.name)}</text></svg>`);
   layers.push({input:label,left:x,top:y});
  }
  await sharp({create:{width:1600,height:Math.ceil(models.length/4)*300,channels:4,background:'white'}}).composite(layers).png().toFile(path.join(gallery,`models-${page+1}.png`));
 }
 await sharp(path.join(assets,'previews/modules.svg')).resize(1600).png().toFile(path.join(gallery,'modules.png'));
 const icons=catalogue.icons; const layers=[];
 for(let i=0;i<icons.length;i++) {
  const x=(i%5)*200,y=Math.floor(i/5)*180;
  const txt=fs.readFileSync(path.join(assets,'icons',icons[i]+'.svg'),'utf8').replaceAll('currentColor','#334155');
  layers.push({input:await sharp(Buffer.from(txt)).resize(75,75).png().toBuffer(),left:x+60,top:y+25});
  layers.push({input:Buffer.from(`<svg width="200" height="35"><text x="100" y="25" text-anchor="middle" font-family="Arial" font-size="15">${icons[i]}</text></svg>`),left:x,top:y+110});
 }
 await sharp({create:{width:1000,height:360,channels:4,background:'white'}}).composite(layers).png().toFile(path.join(gallery,'icons.png'));
 console.log('Rendered four visual browsing sheets');
})().catch(e=>{console.error(e.message);process.exitCode=1});
