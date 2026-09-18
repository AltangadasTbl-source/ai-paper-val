import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';import {build,fillExample} from './build.mjs';
for(const year of [2018,2024,2025]){
 const b=await build(year);await fillExample(b,true);
 for(const s of Object.values(b.sheets))for(let r=2;r<=s.getUsedRange().values.length;r++){s.getRange(`N${r}`).values=[['agree']];s.getRange(`F${r}`).values=[['checker_done']];}
 b.w.recalculate();assert.equal(b.checks.getRange('B7').values[0][0],'FINAL READY');
 const counts=b.w.worksheets.getItem('Paper_counts').getUsedRange().values.slice(1);assert(counts.every(r=>r[5]==='yes'));assert.equal(counts.reduce((sum,r)=>sum+r[2],0),b.total);
 const bad=b.decisions.getUsedRange().values.slice(1).filter(r=>r[6]!=='FINAL READY'||!r[7]);assert.equal(bad.length,0);
 console.log('PASS complete primary/freeze/checker/outcomes/counts',year,b.total);
}
