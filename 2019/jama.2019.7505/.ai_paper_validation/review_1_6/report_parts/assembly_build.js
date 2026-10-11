const fs=require('fs');
const path=require('path');
const root=process.cwd();
const dir='.ai_paper_validation/review_1_6/';
const parts=['cards_001.md','cards_002.md','cards_003.md','cards_004.md'];
const labels=['Candidate statement','Category','Relationship type','All relationships','Compared document roles','Review domain','Evidence state','Suggested review disposition','Classification rationale','Classification ambiguity','Exact source locations','Source evidence','Reported-versus-comparator','Reasoning procedure','Calculation','Alternative source-grounded interpretations','Mechanical evidence recheck','Quality-control relevance','Potential downstream evidence impact','Human verification steps','Human adjudication fields'];
const ledger=fs.readFileSync(dir+'candidate_ledger.md','utf8');
const rows=ledger.split('\n').filter(x=>/^\| C\d{3} \|/.test(x)).map(x=>x.split('|').slice(1,-1).map(x=>x.trim()));
if(rows.length!==106)throw Error('Expected 106 unique classification rows; got '+rows.length);
const classes=new Map(rows.map(x=>[x[0],x]));
const cards=[];
for(const name of parts){
 const text=fs.readFileSync(dir+'report_parts/'+name,'utf8');
 const chunks=[...text.matchAll(/^## (C\d{3}) — (.+)\n([\s\S]*?)(?=^## C\d{3} — |$(?![\s\S]))/gm)];
 for(const m of chunks) cards.push({id:m[1],title:m[2],text:m[0].trimEnd()});
}
cards.sort((a,b)=>a.id.localeCompare(b.id));
if(cards.length!==106||new Set(cards.map(c=>c.id)).size!==106)throw Error('Card set incomplete or duplicated');
const fields=['Category','Relationship type','All relationships','Compared document roles','Review domain','Evidence state','Suggested review disposition'];
const errors=[];
for(const c of cards){
 const cl=classes.get(c.id);if(!cl){errors.push(c.id+' absent from ledger');continue;}
 for(const label of labels)if(!c.text.includes('**'+label+':**'))errors.push(c.id+' missing '+label);
 fields.forEach((field,i)=>{const found=c.text.split('\n').find(x=>x.startsWith('**'+field+':**'));const value=found?.slice(('**'+field+':**').length).trim();if(value!==cl[i+1])errors.push(c.id+' class '+field+': '+value+' !== '+cl[i+1]);});
 for(const field of ['Validity','Importance','Action','Initials','Notes'])if(!c.text.includes('- **'+field+':** __'))errors.push(c.id+' blank '+field);
 if(!c.text.includes('Pending Human Adjudication'))errors.push(c.id+' pending notice');
}
if(errors.length)throw Error(errors.join('\n'));
let index='| ID | Candidate | Category | Relationship type | Review domain | Evidence state |\n|---|---|---|---|---|---|\n';
for(const c of cards){const r=classes.get(c.id);index+='| '+[c.id,c.title.replace(/\|/g,'\\|'),r[1],r[2],r[5],r[6]].join(' | ')+' |\n';}
const manifest=fs.readFileSync(dir+'agent_execution_manifest.md','utf8');
const agentTable=manifest.split('\n').filter(x=>x.startsWith('|')).join('\n');
const run=fs.readFileSync(dir+'run_state.md','utf8');
const performance=run.split('\n').filter(x=>/^- \*\*(Target basis|Total source units|Fresh-source units|Target elapsed minutes|Started UTC|Finished UTC|Observed elapsed minutes|Target status|Exceedance causes):\*\*/.test(x)).join('\n');
if(performance.split('\n').length!==9)throw Error('Missing performance fields');
const ending=fs.readFileSync(dir+'report_parts/assembly_end.md','utf8').replace('{{AGENT_TABLE}}',agentTable).replace('{{PERFORMANCE_FIELDS}}',performance);
const mergedCards=cards.map(c=>c.text.replace(/(?<=[(<])\.\.\/\.\.\/\.\.\/(?=[^\s)>]+\.pdf#page=\d+)/g,'../')).join('\n\n');
const output=fs.readFileSync(dir+'report_parts/assembly_front.md','utf8')+index+'\n## Candidate Evidence Cards\n\n'+mergedCards+'\n\n'+ending;
const links=[...output.matchAll(/\]\((?:<([^>]+)>|([^\s)]+))\)/g)].map(m=>m[1]||m[2]);
const missing=links.filter(x=>!x.startsWith('#')&&!fs.existsSync(path.resolve(root,'.ai_paper_validation',x.split('#')[0])));
fs.writeFileSync('.ai_paper_validation/final_report_1_6.md',output);
const checks={candidate_count:cards.length,part_counts:parts.map(p=>({part:p,count:(fs.readFileSync(dir+'report_parts/'+p,'utf8').match(/^## C\d{3} — /gm)||[]).length})),classification_matches:106,required_fields_per_card:21,human_blank_fields:530,agent_count:agentTable.split('\n').length-2,bytes:Buffer.byteLength(output),pending_coordinator_files:[...new Set(missing)],parts_losslessly_merged:'All card content preserved; PDF links rebased to final report location only'};
fs.writeFileSync(dir+'report_parts/assembly_checks.json',JSON.stringify(checks,null,2)+'\n');
console.log(JSON.stringify(checks));
