import xml from 'xml-js';
// CT_Xf requires alignment, then protection, then extLst. extLst must remain last.
export function normalizeUnlockedStyles(text){
 const doc=xml.xml2js(text,{compact:false});
 function walk(node){
  if(node.type==='element'&&node.name.split(':').pop()==='xf'){
   const prefix=node.name.includes(':')?node.name.split(':')[0]+':':'';
   node.attributes={...node.attributes,applyProtection:'1'};
   node.elements=(node.elements||[]).filter(e=>e.name?.split(':').pop()!=='protection');
   node.elements.push({type:'element',name:prefix+'protection',attributes:{locked:'0',hidden:'0'}});
   const rank={alignment:0,protection:1,extLst:2};
   node.elements.sort((a,b)=>(rank[a.name?.split(':').pop()]??-1)-(rank[b.name?.split(':').pop()]??-1));
  }
  for(const child of node.elements||[])walk(child);
 }walk(doc);return xml.js2xml(doc,{compact:false});
}
