import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {build,fillExample,save} from './build.mjs';
const b=await build(2019),{w,sheets,snap,total,checks,decisions,candidates}=b;
const s=sheets[candidates[0].package],setup=w.worksheets.getItem('Setup');
const set=(sh,a,v)=>{sh.getRange(a).values=[[v]];};
const get=(sh,a)=>sh.getRange(a).values[0][0];
const check=(actual,expected,label)=>{assert.equal(actual,expected,label);console.log('PASS',label);};
check(get(s,'M2'),'','Primary assessment initially blank');
check(get(checks,'B7'),'ACTION NEEDED','Empty template not complete');
await fillExample(b);
check(get(checks,'B7'),'PRIMARY READY','All completed primary rows accepted');
check(get(s,'M2'),'','Primary summary remains blank after primary completion');
set(setup,'B4','TEST_CHECKER');set(setup,'B6','checker');
assert.notEqual(get(s,'G2'),'FINAL READY');check(get(checks,'B7'),'ACTION NEEDED','Unfrozen handoff rejected');
set(setup,'B6','primary');set(setup,'B4','');
const primaryValues=snap.getRange(`A1:L${total+1}`).values;
snap.getRange(`A1:L${total+1}`).copyFrom(snap.getRange(`A1:L${total+1}`),'values');
set(setup,'B6','checker');set(setup,'B4','TEST_CHECKER');
check(get(s,'G2'),'CHECKER RESULT NEEDED','Primary completion never implies checker completion');
assert.match(get(s,'M2'),/Disposition: retain/); console.log('PASS frozen summary visible');
for(const sheet of Object.values(sheets)){
 const n=sheet.getUsedRange().values.length;
 for(let r=2;r<=n;r++){set(sheet,`N${r}`,'agree');set(sheet,`F${r}`,'checker_done');}
}
check(get(checks,'B7'),'FINAL READY','Unchanged checker agreement complete');
check(get(s,'G2'),'FINAL READY','Correct frozen row valid');
check(get(decisions,'H2'),'secondary_temporal','Substantive S_W internal outcome');
set(s,'K2','non_inconsistency');check(get(s,'G2'),'AGREE BUT CHANGED','Agree with changes rejected');
set(s,'N2','agree_clarification');check(get(s,'G2'),'COMMENT NEEDED','Clarification needs comment');
set(s,'O2','TEST clarification');check(get(s,'G2'),'FINAL READY','Clarified direct edit accepted');
check(get(decisions,'H2'),'not_eligible','Updated final classification used');
check(snap.getRange(`A1:L${total+1}`).values[1][6],primaryValues[1][6],'Snapshot remains unchanged after edits');
set(s,'N2','disagree');check(get(s,'G2'),'DISCUSS','Disagreement blocked until discussion');
set(s,'P2','resolved');check(get(s,'G2'),'RESOLUTION NOTE NEEDED','Resolution note required');
set(s,'Q2','TEST_PRIMARY and TEST_CHECKER agreed no inconsistency.');check(get(s,'G2'),'FINAL READY','Resolved disagreement complete');
set(s,'D2','discuss');set(s,'K2','');check(get(s,'G2'),'DISCUSS','Disposition discuss cannot be final');
set(s,'D2','retain');check(get(s,'G2'),'CHECK FIELDS','Required judgment cannot be cleared');
set(s,'K2','wording_only');check(get(s,'G2'),'CHECK FIELDS','Pasted obsolete option rejected');
set(s,'E2','statistical_results');set(s,'H2','confirmed_issue');set(s,'I2','substantive');check(get(s,'G2'),'CLEAR INACTIVE VALUES','Stale inactive answer rejected');
set(s,'K2','');set(s,'J2','');check(get(s,'G2'),'FINAL READY','Direct blank optional answer accepted');
check(get(decisions,'H2'),'primary_temporal','Statistical substantive outcome');
set(s,'H2','not_issue');check(get(decisions,'H2'),'not_eligible','Not-issue outcome excluded');
set(s,'J2','<clear>');check(get(s,'G2'),'CHECK FIELDS','Old clear sentinel rejected');set(s,'J2','');
set(setup,'B4','test_primary');check(get(s,'G2'),'CHECK REVIEWER IDs','Case-insensitive same reviewer rejected');set(setup,'B4','TEST_CHECKER');
const key=get(s,'A2');set(s,'A2',get(s,'A3'));check(get(s,'G2'),'CHECK KEY','Duplicate candidate key rejected');set(s,'A2',key);
const row2=s.getRange('A2:R2').values,row3=s.getRange('A3:R3').values;
// Sort-like move of input fields only, retaining row-relative calculated columns.
for(const col of ['A','B','C','D','E','F','H','I','J','K','L','N','O','P','Q','R']){let i=col.charCodeAt(0)-65;set(s,`${col}2`,row3[0][i]);set(s,`${col}3`,row2[0][i]);}
assert.match(get(s,'M3'),/substantive_inconsistency/);console.log('PASS key-based snapshot lookup after reordering');
check(get(checks,'B7'),'FINAL READY','Row reordering preserves final completion');
const issue=candidates.find(c=>c.primary==='P_R'),drow=candidates.indexOf(issue)+2;
check(get(decisions,`H${drow}`),'protocol_descriptive','P_R remains descriptive');
const pp=candidates.find(c=>c.primary==='P_P');check(get(decisions,`H${candidates.indexOf(pp)+2}`),'plan_descriptive','P_P remains descriptive');
await save(w,'/tmp/adjudication-excel-only/scenario-final.xlsx');
const preview=await w.render({sheetName:'Checks',range:'A1:B9',scale:1.3,format:'png'});await fs.writeFile('/tmp/adjudication-excel-only/checks.png',new Uint8Array(await preview.arrayBuffer()));
console.log('ALL SCENARIOS PASSED');
