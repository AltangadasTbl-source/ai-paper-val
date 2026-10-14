const fs=require('fs'),path=require('path');
const root=path.resolve('.ai_paper_validation/review_1_6_2');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const lines=p=>read(p).split('\n').filter(l=>l.startsWith('|')).map(l=>l.split('|').slice(1,-1).map(s=>s.trim())).filter(r=>r[0]&&!/^[-]+$/.test(r[0]));
const cfiles=['candidate_ledger.md','verification/evidence_recheck.md'];
for(const p of cfiles) console.log('C headings',p,(read(p).match(/^## C\d{3}\b/gm)||[]).join(','));
const findingPaths=['checkers/numeric_consistency.md','checkers/cross_source_consistency.md','checkers/statistical_pass_1.md','checkers/statistical_pass_2.md'];
const findings=findingPaths.flatMap(p=>Array.from(read(p).matchAll(/^### (F-[A-Z0-9]+-\d{3})\b/gm),m=>m[1]));
const screen=lines('screening/inclusion_screen.md').filter(r=>/^F-/.test(r[0]));
console.log('Checker finding set',findings.length,findings.join(', '));
console.log('Screen rows',screen.length,'missing',findings.filter(id=>screen.filter(r=>r[0]===id).length!==1),'unknown',screen.filter(r=>!findings.includes(r[0])).map(r=>r[0]));
console.log('Screen INCLUDE',screen.filter(r=>r[3]==='INCLUDE').length,'SCREENED_OUT',screen.filter(r=>r[3]==='SCREENED_OUT').length);
const sources=lines('source_coverage.md').filter(r=>/^DOC-/.test(r[0]));
for(const r of sources)console.log('Source closure',r[0],Number(r[4])+Number(r[5])===Number(r[3])&&r[6]===r[3]&&r[7]==='COMPLETE',r.slice(3).join('/'));
const cm=lines('coverage_manifest.md').filter(r=>r[0]!=='Stage');
const bad=cm.filter(r=>r.length!==5||!/^(?:\.\.\/)?[A-Za-z0-9_./-]+$/.test(r[3])||(r[4]==='COMPLETE'&&!fs.existsSync(path.resolve(root,r[3]))));
console.log('Coverage rows',cm.length,'artifact schema/exists failures',JSON.stringify(bad));
console.log('Coverage pending',cm.filter(r=>r[4]!=='COMPLETE').map(r=>r[1]).join(', '));
const mf=lines('agent_execution_manifest.md').filter(r=>r[0]!=='Stage');
console.log('Manifest agents',mf.length,'unique',new Set(mf.map(r=>r[1])).size,'model deviations',JSON.stringify(mf.filter(r=>r[2]!=='gpt-6.1-sol')));
for(const stage of ['statistics_pass_1','statistics_pass_2','inclusion_screener','evidence_rechecker','quality_control_auditor'])console.log('Mandatory routing',stage,JSON.stringify(mf.filter(r=>r[0]===stage)));
const n=Array.from(read('relationships/numeric_relationship_inventory.md').matchAll(/^\| (N\d{3})\b/gm),m=>m[1]);
const s=Array.from(read('statistics/relationship_inventory.md').matchAll(/^\| (S\d{3})\b/gm),m=>m[1]);
console.log('N IDs',n.length,'unique',new Set(n).size,'S IDs',s.length,'unique',new Set(s).size);
console.log('S pass statuses',read('statistics/relationship_inventory.md').split('\n').filter(l=>/^\| S\d{3}\b/.test(l)).every(l=>l.includes('PASS_1_COMPLETE')&&l.includes('PASS_2_COMPLETE')));
const limits={'jama_combes_2025_oi_250087_1766516490.94011.pdf':10,'joi250087supp1_prod_1766516490.96011.pdf':153,'joi250087supp2_prod_1766516490.96511.pdf':9,'joi250087supp3_prod_1766516490.97011.pdf':18,'joi250087supp4_prod_1766516490.97511.pdf':3,'joi250087supp5_prod_1766516490.97511.pdf':1};
for(const p of [...cfiles,'screening/inclusion_screen.md','quality/audit_handoff.md','checkers/parts/cross_source_remaining.md']){
let links=0,fail=[];
for(const m of read(p).matchAll(/\]\(<?([^\s)>]+)>?\)/g)){
const link=m[1];if(/^[a-z]+:\/\//i.test(link))continue;
const [loc,anchor]=link.split('#'),full=path.resolve(root,path.dirname(p),loc);links++;
if(!fs.existsSync(full))fail.push(link);
if(loc.endsWith('.pdf')&&(!/^page=\d+$/.test(anchor||'')||Number(anchor.slice(5))<1||Number(anchor.slice(5))>limits[path.basename(loc)]))fail.push('PAGE '+link);
}
console.log('Links',p,links,'failures',JSON.stringify(fail));
}
const scan=p=>{for(const entry of fs.readdirSync(p,{withFileTypes:true})){const q=path.join(p,entry.name);if(entry.isDirectory()){if(!['tooling','preprocessing'].includes(entry.name))scan(q);}else if(entry.name.endsWith('.md')){const content=fs.readFileSync(q,'utf8');for(const [i,l] of content.split('\n').entries())if(/\b(error|mistake|defect|erroneous|wrong|incorrect)\b/i.test(l)&&!/(?:standard|type I|type II|measurement|sampling|medication|refractive) error|error bars?|septal defect/i.test(l))console.log('Vocabulary review',path.relative(root,q),i+1,l.slice(0,180));}}};scan(root);
