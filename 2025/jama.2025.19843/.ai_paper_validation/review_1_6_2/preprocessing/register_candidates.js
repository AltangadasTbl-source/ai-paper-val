const fs=require('fs');
const root='.ai_paper_validation/review_1_6_2/';
let screen=fs.readFileSync(root+'screening/inclusion_screen.md','utf8');
const groups=[
['C001','PRIMARY_ADJUSTMENT','Primary adjustment covariate descriptions do not reconcile','statistical_results','S_W','S_W','REPORT main Randomization/Statistical Analysis vs REPORT Table 2 footnote c; PLAN SAP corroborates only','F-XS-001, F-ST1-001','Route B'],
['C002','ORGAN_THRESHOLD','Organ-failure threshold differs between SAP and report','protocol_report','P_R','P_R','PLAN SAP vs REPORT main Outcomes/results eTable 3','F-XS-003, F-ST1-004','Route B'],
['C003','D60_FREE_DAYS','Planned day-60 free-day results are absent from supplied reports','protocol_report','P_R','P_R','PLAN protocol/SAP vs REPORT main/results supplement','F-XS-005, F-ST1-008','Route A, category 5'],
['C004','LV_COMPOSITE','Planned hierarchical LV-function composite differs from reported LVEF contrast','protocol_report','P_R','P_R','PLAN SAP vs REPORT main Outcomes/results eTable 3','F-XS-004, F-ST1-002','Route A, category 5'],
['C005','MACE_COMPONENTS','Dialysis membership differs across MACE definitions','protocol_report','P_R','P_R, P_P, S_C','PLAN protocol vs PLAN SAP vs REPORT main/results supplement','F-XS-002, F-ST1-003','Route A, category 5'],
['C006','ETIOLOGY_SUBGROUP','Planned post-arrest subgroup differs from reported predefined other-etiology subgroup','protocol_report','P_R','P_R','PLAN protocol/SAP vs REPORT main Figure 3/results eTable 6/eFigure 9','F-XS-007, F-ST1-005','Route A, category 5'],
['C007','ADJUSTED_SECONDARY_OUTPUTS','Planned adjusted key-secondary analyses lack supplied outputs','protocol_report','P_R','P_R','PLAN protocol/SAP vs REPORT main/results supplement','F-XS-006, F-ST1-006','Route A, category 5']
];
for(const g of groups) for(const id of g[7].split(', ')) screen=screen.replace(new RegExp('(\\| '+id+' \\|[^\\n]*\\| )PENDING( \\|)'),'$1'+g[0]+'$2');
screen=screen.replace('Candidate IDs are `PENDING` until the coordinator registers the seven consolidated issue groups below.','Candidate IDs were assigned by the coordinator after this independent screen to the seven consolidated issue groups below.');
screen=screen.replace('All included rows await coordinator Candidate IDs.','All included rows now name stable coordinator-assigned Candidate IDs.');
fs.writeFileSync(root+'screening/inclusion_screen.md',screen);
const reb=s=>s.replaceAll('../../../','../../');
const cat=screen.slice(screen.indexOf('## Exact source-location catalogue'),screen.indexOf('## Consolidated issues'));
let out='# Stable candidate ledger — Workflow 1.6.2\n\nPending Human Adjudication. Registration follows independent inclusion screening, without a count target. All assigned IDs are retained.\n\nStable source order follows the first substantive compared location in DOC-001 reading order: Randomization/primary adjustment; organ failure, D60 free days, LV function and MACE in Outcomes; subgroup analysis; then secondary statistical methods continuing on p.4. Abstract corroboration establishes key-secondary status and is retained without changing this substantive-location order.\n\nClassification is provisional pending direct-source recheck and independent quality audit. No human disposition is assigned.\n\n| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |\n|---|---|---|---|---|---|---|---|\n';
for(const g of groups) out+=`| ${g[0]} | ${g[3]} | ${g[4]} | ${g[5]} | ${g[6]} | PENDING | PENDING | ${g[7]} |\n`;
out+='\n'+reb(cat)+'\n';
for(const g of groups){
 const start=screen.indexOf('### '+g[1]+' —'); let end=screen.indexOf('\n### ',start+1); if(end<0) end=screen.indexOf('\n## Screened-out',start);
 const facts=screen.slice(screen.indexOf('\n',start)+1,end).trim();
 out+=`## ${g[0]} — ${g[2]}\n\n**Candidate statement:** ${g[2]}.\n\n**Review domain:** ${g[3]}\n\n**Relationship type:** ${g[4]}\n\n**All relationships:** ${g[5]}\n\n**Compared document roles:** ${g[6]}\n\n**Finding IDs:** ${g[7]}\n\n**Checker provenance:** cross_source_consistency_reviewer and statistics_pass_1, independently screened by root/inclusion_initial.\n\n**Qualifying route:** ${g[8]}\n\n**Classification rationale:** ${g[4]==='S_W'?'Conflicting compared descriptions are within the REPORT main article; the PLAN corroborates one side only, so S_W applies.':g[0]==='C005'?'Conflicting definitions span PLAN/REPORT, PLAN/PLAN and REPORT/REPORT, giving P_R, P_P and S_C; P_R takes precedence.':'The conflicting or absent supplied result is compared with an explicit PLAN analysis or outcome specification; P_R applies.'}\n\n**Classification ambiguity:** None at registration; exact content roles and evidence state await independent recheck.\n\n${reb(facts)}\n\n**Mechanical evidence recheck:** PENDING; assigned ID will remain even if any evidence fact changes.\n\n`;
}
fs.writeFileSync(root+'candidate_ledger.md',out);
fs.writeFileSync(root+'preprocessing/registration_groups.json',JSON.stringify(groups,null,2)+'\n');
