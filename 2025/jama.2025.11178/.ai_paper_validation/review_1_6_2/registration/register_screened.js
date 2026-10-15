const fs = require('fs');
const dir = '.ai_paper_validation/review_1_6_2/';
const screenPath = dir + 'screening/inclusion_screen.md';
let screen = fs.readFileSync(screenPath, 'utf8');
const groups = [
 ['IG01','protocol_report','P_R','P_R',['F-XS-002'],'Route B'],
 ['IG02','statistical_results','S_W','S_W',['F-NUM-001'],'Route A, category 3'],
 ['IG03','statistical_results','S_W','S_W',['F-NUM-004','F-ST1-004'],'Route A, category 4'],
 ['IG04','statistical_results','S_W','S_W',['F-NUM-005'],'Route A, category 4'],
 ['IG05','protocol_report','P_R','P_R, S_C, S_W',['F-XS-003'],'Route A, category 5'],
 ['IG06','protocol_report','P_R','P_R',['F-XS-004'],'Route B'],
 ['IG07','protocol_report','P_R','P_R, P_P',['F-XS-005'],'Route A, category 5'],
 ['IG08','statistical_results','S_W','S_W',['F-ST1-006'],'Route B'],
 ['IG09','statistical_results','S_W','S_W',['F-ST1-001'],'Route A, category 1'],
 ['IG10','statistical_results','S_W','S_W',['F-ST1-002'],'Route A, category 1'],
 ['IG12','statistical_results','S_W','S_W',['F-ST1-205'],'Route B'],
 ['IG13','statistical_results','S_W','S_W',['F-XS-007'],'Route B'],
 ['IG14','statistical_results','S_W','S_W',['F-XS-006'],'Route B'],
 ['IG15','statistical_results','S_W','S_W',['F-ST1-201','F-ST1-202'],'Route A, category 1'],
 ['IG16','statistical_results','S_W','S_W',['F-NUM-003'],'Route A, category 3'],
 ['IG11','statistical_results','S_W','S_W',['F-XS-008'],'Route B'],
 ['IG17','statistical_results','S_W','S_W',['F-NUM-002'],'Route A, category 3']
];
const roles = {
 IG01:'REPORT main/TIDieR intervention duration vs PLAN protocol intervention duration',
 IG02:'REPORT main adherence paragraph vs REPORT main Figure1 counts',
 IG03:'REPORT main SMD definition vs REPORT main Table3 contrasts',
 IG04:'REPORT main NNT method/Table2 internally; REPORT results supplement eTable8 internally',
 IG05:'REPORT main/results/workbook adjustment sets vs PLAN protocol/SAP primary adjustment sets',
 IG06:'REPORT main secondary adjustment vs PLAN protocol/SAP secondary adjustment',
 IG07:'REPORT main/results primary and sensitivity roles vs PLAN SAP roles; PLAN SAP amendment vs PLAN SAP retained methods',
 IG08:'REPORT main Table2 RR intervals vs REPORT main Table2 NNT intervals',
 IG09:'REPORT main Table2 NNT point vs REPORT main Table2 NNT interval',
 IG10:'REPORT main Table3 SMD points vs REPORT main Table3 SMD intervals',
 IG12:'REPORT results supplement full primary adjustment vs REPORT results supplement restricted primary adjustment',
 IG13:'REPORT results supplement weight predictor list vs REPORT results supplement fitted weight-model coefficients',
 IG14:'REPORT results supplement binary education specification vs REPORT results supplement education coefficients',
 IG15:'REPORT results supplement coefficient intervals vs REPORT results supplement coefficient P values',
 IG16:'REPORT results supplement eTable8 any-follow-up total vs REPORT results supplement eTable8 three-month arm counts',
 IG11:'REPORT results supplement mean-summary narrative vs REPORT results supplement median/quartile table labels and values',
 IG17:'REPORT workbook eTable3 count/percentage vs REPORT workbook denominator/missing count/footnote'
};
const duplicates = {'F-ST1-005':'IG04','F-ST1-206':'IG04','F-ST1-203':'IG13','F-ST1-204':'IG14','F-ST1-601':'IG11'};
const findings = {};
for (const file of ['checkers/numeric_consistency.md','checkers/cross_source_consistency.md','checkers/statistical_pass_1.md']) {
 const s = fs.readFileSync(dir+file,'utf8'); const headings = [...s.matchAll(/^###\s+(F-(?:NUM|XS|ST1)-\d+)\b[^\n]*$/gm)];
 for (const m of headings) {const tail=s.slice(m.index+m[0].length); const next=tail.search(/^#{1,3}\s+/m); findings[m[1]]={file,body:(m[0]+tail.slice(0,next<0?tail.length:next)).trim()};}
}
const idByGroup={}, idByFinding={};
groups.forEach((g,i)=>{const id='C'+String(i+1).padStart(3,'0');idByGroup[g[0]]=id;for(const f of g[4])idByFinding[f]=id;});
for(const [f,g] of Object.entries(duplicates))idByFinding[f]=idByGroup[g];
screen=screen.split('\n').map(line=>{if(!line.startsWith('| F-'))return line;const cells=line.split('|');const id=idByFinding[cells[1].trim()];if(id)cells[6]=' '+id+' ';return cells.join('|');}).join('\n');
screen=screen.replace(/Candidate IDs are deliberately[^\n]+/,'The coordinator assigned stable candidate IDs after these independent decisions, in substantive source order. Issue-group labels remain provenance labels; corroborating-only source definitions do not move an issue ahead of its conflicting report locations.');
fs.writeFileSync(screenPath,screen);
let ledger='# Candidate ledger — Workflow 1.6.2\n\nAll candidates are Pending Human Adjudication. Registration follows the complete independent initial screen:19 included findings consolidated into17 stable candidates. Source order uses earliest substantive conflicting source ID and physical page/cell, with screen-group order for ties; corroborating-only definitions do not move a candidate. Classification is provisional until the mechanical recheck and inclusion audit. Assigned IDs will never be deleted.\n\n| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |\n|---|---|---|---|---|---|---|---|\n';
for(const g of groups){ledger+='| '+[idByGroup[g[0]],g[1],g[2],g[3],roles[g[0]],'reproduced','PENDING',g[4].join(', ')].join(' | ')+' |\n';}
for(const g of groups){
 const marker=new RegExp('^### '+g[0]+' — (.+)$','m'); const m=screen.match(marker);if(!m)throw Error('Missing group '+g[0]); const start=screen.indexOf(m[0]);const remaining=screen.slice(start+m[0].length);const end=remaining.search(/^### IG\d+|^## Source confirmation/m);const groupBody=remaining.slice(0,end<0?remaining.length:end).trim();
 const id=idByGroup[g[0]];const title=m[1];
 ledger+='\n\n## '+id+' — '+title+'\n\n**Candidate statement:** '+title+'.\n\n**Status:** Pending Human Adjudication\n\n**Review domain:** '+g[1]+'\n\n**Relationship type:** '+g[2]+'\n\n**All relationships:** '+g[3]+'\n\n**Compared document roles:** '+roles[g[0]]+'\n\n**Evidence state:** reproduced\n\n**Inclusion audit:** PENDING\n\n**Finding IDs:** '+g[4].join(', ')+'\n\n**Qualifying route:** '+g[5]+'\n\n**Classification rationale:** '+(g[2]==='P_R'?'A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.':'The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.')+'\n\n**Classification ambiguity:** '+(g[0]==='IG11'?'The screener proposed S_C using the main PGIC scale definition; the coordinator provisionally records S_W because that definition corroborates the numerical premise, while the actual mean-versus-median conflict is inside the results supplement. Mechanical recheck will confirm this distinction.':g[0]==='IG07'?'The SAP IPW amendment may clarify the intended primary analysis. Recheck must distinguish a report/plan conflict from plan-internal retained wording and corroboration.':'None')+'\n\n### Independent screen and complete affected locations\n\n'+groupBody.replaceAll('../../../','../../')+'\n\n### Included finding evidence and checker provenance\n';
 for(const f of g[4]){const card=findings[f];if(!card)throw Error('Missing finding '+f);let body=card.body.replaceAll('../../../','../../').replace(/^### /gm,'#### ');body=body.replace(/\]\((<?)([^)>]+)(>?)\)/g,(all,left,path,right)=>{const tight=path.replace(/\s+/g,'');return /\.(pdf|xlsx)(?:#|$)/i.test(tight)?']('+left+tight+right+')':all;});ledger+='\nSource checker: '+card.file+'; finding '+f+'.\n\n'+body+'\n';}
 const dup=Object.keys(duplicates).filter(f=>duplicates[f]===g[0]);if(dup.length)ledger+='\nRelated screened duplicate findings (not included Finding IDs): '+dup.join(', ')+'. Their full affected locations are retained in the consolidated screen group and checker outputs.\n';
}
fs.writeFileSync(dir+'candidate_ledger.md',ledger);
fs.writeFileSync(dir+'registration/source_order_mapping.json',JSON.stringify(groups.map(g=>({id:idByGroup[g[0]],group:g[0],findings:g[4],domain:g[1],relationship:g[2],all_relationships:g[3]})),null,2)+'\n');
console.log(JSON.stringify({candidates:groups.length,include_findings:groups.reduce((n,g)=>n+g[4].length,0),ids:Object.values(idByGroup)}));
