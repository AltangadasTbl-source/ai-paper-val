import {normalizeUnlockedStyles} from './xlsx-compat.mjs';
import {fileURLToPath} from 'node:url';
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {FileBlob, SpreadsheetFile, Workbook} from '@oai/artifact-tool';
import JSZip from 'jszip';

const ROOT=process.env.ADJ_ROOT || fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
const INPUT=process.env.ADJ_INPUT || ROOT;
const OUT=process.env.ADJ_OUTPUT || '/tmp/adjudication-excel-only-rebuild';
const cols=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'];
const fields=['disposition','domain','statisticalIssueStatus','substantiveStatus','downstreamImpact','internalStatus','protocolInterpretation','notes'];
const acols=['D','E','H','I','J','K','L','R'];
const labels=['Disposition','Review domain','Statistcal_or_numerical issue','Substantiveness','Downstream impact','Report-internal or planning-material inconsistency','Protocol interpretation','Notes (optional)'];
const headers=['Candidate key','Candidate title','Source location','Disposition','Review domain','Complete','Validation hint',...labels.slice(2,7),'Primary assessment','Checker result','Checker comment','Discussion resolution','Resolution note','Notes (optional)'];
const opts={disposition:['retain','exclude','discuss'],domain:['statistical_results','report_internal_inconsistency','plan_material','protocol_report'],statisticalIssueStatus:['confirmed_issue','probable_issue','not_issue','indeterminate'],substantiveStatus:['substantive','minor_presentation','indeterminate'],downstreamImpact:['direct','possible','unlikely','unknown'],internalStatus:['substantive_inconsistency','minor_presentation','non_inconsistency','indeterminate'],protocolInterpretation:['substantive_difference','minor_presentation','version_timing','non_inconsistency','indeterminate'],reviewComplete:['no','primary_done','checker_done'],checkStatus:['agree','agree_clarification','disagree','unable'],resolutionStatus:['pending','resolved']};
const stage='Setup!$B$6';
const q=s=>`'${s.replaceAll("'","''")}'`;
const quote=s=>`"${String(s).replaceAll('"','""')}"`;
const val=(s,a,v)=>s.getRange(a).values=[[v]];
const formula=(s,a,f)=>s.getRange(a).formulas=[[f]];
const lookup=(sheet,col,key,n)=>n===1?`IF(${key}=${q(sheet)}!$A$2,${q(sheet)}!$${col}$2,NA())`:`INDEX(${q(sheet)}!$${col}$2:$${col}$${n+1},MATCH(${key},${q(sheet)}!$A$2:$A$${n+1},0))`;
const preserve=e=>`IF(${e}="","",${e})`;
const valid=(e,list)=>`OR(${list.map(v=>`${e}=${quote(v)}`).join(',')})`;
const active=(i,d,e)=>`AND(${d}="retain",${i<5?`${e}="statistical_results"`:i===5?`OR(${e}="report_internal_inconsistency",${e}="plan_material")`:`${e}="protocol_report"`})`;
function table(w,name,rows,widths=[],height=48){
 const s=w.worksheets.add(name), n=rows.length,m=rows[0].length;
 s.getRangeByIndexes(0,0,n,m).values=rows;
 s.getRangeByIndexes(0,0,n,m).format={font:{name:'Calibri',size:11,color:'#173F57'},wrapText:true,verticalAlignment:'center',rowHeight:height};
 s.getRangeByIndexes(0,0,1,m).format={fill:'#173F57',font:{bold:true,color:'#FFFFFF'},rowHeight:42};
 for(let i=0;i<m;i++)s.getRangeByIndexes(0,i,n,1).format.columnWidth=widths[i]||26;
 for(let r=1;r<n;r+=2)s.getRangeByIndexes(r,0,1,m).format.fill='#F4F8FA';
 s.freezePanes.freezeRows(1);s.freezePanes.freezeColumns(1);s.showGridLines=false;
 return s;
}
export async function unlock(bytes){
 const z=await JSZip.loadAsync(bytes);
 for(const name of Object.keys(z.files)){
  if(!name.endsWith('.xml'))continue;
  let xml=await z.file(name).async('string');
  if(name==='xl/styles.xml') xml=normalizeUnlockedStyles(xml);
  xml=xml.replace(/<(?:\w+:)?sheetProtection\b[^>]*\/>/g,'').replace(/<(?:\w+:)?workbookProtection\b[^>]*\/>/g,'');
  if(name==='xl/workbook.xml'){
   const prefix=xml.includes('<x:workbook')?'x:':'';
   xml=xml.replace(/<(?:\w+:)?calcPr\b[^>]*\/>/g,'').replace(/<\/(?:x:)?workbook>/,`<${prefix}calcPr calcId="191029" fullCalcOnLoad="1" forceFullCalc="1" calcMode="auto"/></${prefix}workbook>`);
  }
  // Standard English font names in any imported theme.
  xml=xml.replaceAll('宋体','SimSun').replaceAll('新細明體','PMingLiU');
  z.file(name,xml);
 }
 return z.generateAsync({type:'nodebuffer',compression:'DEFLATE'});
}
async function save(w,file){
 w.recalculate();
 const blob=await SpreadsheetFile.exportXlsx(w);
 const temp='/tmp/adjudication-excel-only/export.xlsx';await fs.mkdir(path.dirname(temp),{recursive:true});await blob.save(temp);
 const bytes=await unlock(await fs.readFile(temp));
 await fs.mkdir(path.dirname(file),{recursive:true});await fs.writeFile(file,bytes);
}
function hints(s,r,n,total){
 const a=`A${r}`,d=`D${r}`,e=`E${r}`,f=`F${r}`;
 const pcol=c=>lookup('Primary_snapshot',c,a,total);
 const errors=[`NOT(${valid(d,opts.disposition)})`,`NOT(${valid(e,opts.domain)})`];
 const stale=[];
 for(let i=2;i<7;i++){
  const cell=`${acols[i]}${r}`,act=active(i,d,e), required=[2,3,5].includes(i);
  errors.push(`AND(${act},${required?'':`${cell}<>"",`}NOT(${valid(cell,opts[fields[i]])}))`);
  stale.push(`AND(NOT(${act}),${cell}<>"",${cell}<>"not_applicable")`);
 }
 const equal=acols.map((c,i)=>{const v=`${c}${r}`,effective=i>=2&&i<7?`IF(${active(i,d,e)},${preserve(v)},"not_applicable")`:preserve(v);return `${effective}=${preserve(pcol(cols[i+1]))}`;}).join(',');
 const snapshotBad=`OR(COUNTIF(Primary_snapshot!$A$2:$A$${total+1},${a})<>1,${pcol('J')}<>"primary_done",${pcol('K')}<>Setup!$B$2,${cols.slice(1,12).map(c=>`${pcol(c)}="NOT FROZEN"`).join(',')})`;
 const identity=`OR(LEN(TRIM(Setup!$B$2))=0,Setup!$B$2<>TRIM(Setup!$B$2),AND(${stage}="checker",OR(LEN(TRIM(Setup!$B$4))=0,Setup!$B$4<>TRIM(Setup!$B$4),LOWER(TRIM(Setup!$B$4))=LOWER(TRIM(Setup!$B$2)))))`;
 const needsDiscussion=`OR(${d}="discuss",${pcol('B')}="discuss",N${r}="disagree",N${r}="unable")`;
 let checker=`IF(${snapshotBad},"FREEZE SNAPSHOT",IF(NOT(${valid(`N${r}`,opts.checkStatus)}),"CHECKER RESULT NEEDED",IF(AND(N${r}<>"agree",LEN(TRIM(O${r}))=0),"COMMENT NEEDED",IF(AND(N${r}="agree",NOT(AND(${equal}))),"AGREE BUT CHANGED",IF(AND(P${r}<>"",NOT(${valid(`P${r}`,opts.resolutionStatus)})),"CHECK RESOLUTION",IF(OR(AND(${needsDiscussion},P${r}<>"resolved"),${d}="discuss"),"DISCUSS",IF(AND(P${r}="resolved",LEN(TRIM(Q${r}))=0),"RESOLUTION NOTE NEEDED",IF(${f}<>"checker_done","CHECKER DRAFT","FINAL READY"))))))))`;
 let primary=`IF(OR(N${r}<>"",O${r}<>"",P${r}<>"",Q${r}<>""),"CLEAR CHECKER FIELDS",IF(OR(Setup!$B$4<>"",Setup!$B$5<>""),"CLEAR CHECKER ID",IF(${f}<>"primary_done","PRIMARY DRAFT","PRIMARY READY")))`;
 formula(s,`G${r}`,`=IFERROR(IF(NOT(${valid(stage,['primary','checker'])}),"CHECK STAGE",IF(${identity},"CHECK REVIEWER IDs",IF(OR(COUNTIF($A$2:$A$${n+1},${a})<>1,COUNTIF(Decisions!$C$2:$C$${total+1},${a})<>1),"CHECK KEY",IF(OR(${stale.join(',')}),"CLEAR INACTIVE VALUES",IF(OR(${errors.join(',')}),"CHECK FIELDS",IF(${stage}="primary",${primary},${checker})))))),"CHECK KEY / SNAPSHOT")`);
}
function startRows(year,total){return [
 ['Step','Instructions'],['Release',`v.2.1.5.4 | ${year} | Excel-only review | ${total} candidates | No locks, macros or scripts`],
 ['1. Begin','Save As a working copy. Setup: enter primaryReviewerId (B2); stage (B6) stays primary. The primary and checker must be different people. Keep checker ID/name blank during primary review.'],
 ['2. Read one candidate','Papers lists each C_<paper> sheet. Read A-C, then filter Candidates and Evidence by Candidate key. Consult original documents in the shared year/paper folders. AI flags and suggested domains are not confirmed human findings.'],
 ['3. Make the assessment','Choose Disposition (D) and confirm Review domain (E). Fill the applicable H-L judgments. English inputs. Yellow = common/required; blue = optional; gray = inactive. Read Codebook for meanings. Primary assessment (M) is blank during primary review.'],
 ['4. Complete primary review','Set F to primary_done only after reviewing the row. Leave N-Q blank. G must say PRIMARY READY. Checks summarizes all rows. Use no while drafting; recheck after every later edit.'],
 ['5. Save the backup','When Checks says PRIMARY READY, save and close the primary file. Keep this backup. Open it and Save As a new checker working copy before continuing. Never reuse the primary backup for checker edits.'],
 ['6. Freeze the snapshot',`In the checker copy, while Setup B6 still says primary: open Primary_snapshot. Select A1:L${total+1} using the Name Box. Copy; Home > Paste > Paste Special > Values onto the SAME selected cells. Do this once. Save.`],
 ['7. Start checking','Now set Setup B6 to checker and enter checkerId in B4. Primary_snapshot must be saved as values BEFORE this switch. M now shows the original assessment. The existing answers remain in D/E/H-L/R; edit them directly. A blank is blank; there is no inheritance. F=primary_done does not finish checking.'],
 ['8. Check or discuss','If unchanged: N=agree. Otherwise choose the appropriate result and explain in O. For disagree, unable, or a primary discuss: discuss together; P=resolved; Q lists participants and conclusion; update the final answers and do not leave D=discuss. Then set F=checker_done.'],
 ['9. Finish and hand off','Every G must say FINAL READY and Checks must say FINAL READY. Save the annual workbook as *_final.xlsx. Decisions, Paper_counts and Protocol_plan_table are built in; no separate export command. Give the manager the final file and unchanged primary backup, preserving access to shared source folders.'],
 ['Changes / pause','Changing a domain may leave old literal answers. Clear inactive answers or choose not_applicable; answer newly applicable fields. Optional blanks are allowed. Set F=no after editing a completed row, then review and mark the correct stage done. Save; note the file, sheet and Candidate key to resume.'],
 ['No unlock step','Every cell and sheet is editable, including reference and formula cells. No passwords. Edit review inputs and Setup; preserve keys, sources and calculation cells. If a formula/reference is damaged, undo or recover from your saved copy.'],
 ['Meaning of results','Checks tests entries and completion, not scientific accuracy or tamper-proof provenance. Outcomes remain blank until FINAL READY per row. Paper counts stay blank until all candidates in that paper are final. Protocol and plan findings are descriptive; visible-answer checking is not blinded reliability.'],
 ['Help / PDF','Use the Chinese step-by-step PDF in this same folder. No terminal, package installation, handoff script, validation script, or export script is part of this workflow.']
 ];}

export async function build(year){
 const original=await SpreadsheetFile.importXlsx(await FileBlob.load(`${INPUT}/resources/source_catalog_v_2_1_5_4.xlsx`));
 const source=Object.fromEntries(['Candidates','Evidence','Links','Relations'].map(name=>[name,original.worksheets.getItem(name).getUsedRange().values]));
 for(const name of Object.keys(source)){const [h,...rows]=source[name];const ki=h.indexOf('key');source[name]=[h,...rows.filter(r=>String(r[ki]).startsWith(`${year}::`))];}
 const [ch,...cr]=source.Candidates; const candidates=cr.map(r=>Object.fromEntries(ch.map((k,i)=>[k,r[i]])));
 const total=candidates.length,papers=[...new Set(candidates.map(c=>c.package))];
 const w=Workbook.create();
 table(w,'Start',startRows(year,total),[30,112],68);
 const setup=table(w,'Setup',[['Field','Value'],['primaryReviewerId',''],['primaryReviewerName',''],['checkerId',''],['checkerName',''],['stage','primary']],[32,65],40);
 setup.getRange('B2:B6').format.fill='#FFF2CC';setup.getRange('B6').dataValidation={rule:{type:'list',values:['primary','checker']}};
 const checks=table(w,'Checks',[['Check','Result'],['Stage',''],['Candidates',total],['Primary ready rows',''],['Final ready rows',''],['Other / unfinished rows',''],['Workflow status',''],['Next action',''],['Scope','Entry checks only. Verify the evidence and preserve the primary backup. No passwords; reference cells remain editable.']],[34,104],44);
 const ps=table(w,'Papers',[['Paper','Review worksheet','Candidates'],...papers.map(p=>[p,`C_${p}`,candidates.filter(c=>c.package===p).length])],[32,34,18],36);
 const sheets={}; for(const p of papers){const cc=candidates.filter(c=>c.package===p);sheets[p]=table(w,`C_${p}`,[headers,...cc.map(c=>[c.key,c.title,c.locations,'',c.ai_domain,'no','',...Array(11).fill('')])],[22,28,22,18,24,17,25,28,20,20,34,26,58,23,32,22,32,32],92);}
 const snap=table(w,'Primary_snapshot',[['key',...fields,'reviewComplete','primaryReviewerId','summary'],...candidates.map(c=>Array(12).fill(''))],[44,20,26,26,24,24,26,26,40,22,26,75],70);
 const decisionHeaders=['year','package','key','relationship','primaryReviewerId','checkerId','status','outcome','aiDisposition','aiDomain',...fields.map(f=>'primary_'+f),...fields.map(f=>'final_'+f),'checkStatus','checkerComment','resolutionStatus','resolutionNote'];
 const decisions=table(w,'Decisions',[decisionHeaders,...candidates.map(c=>Array(decisionHeaders.length).fill(''))],[12,26,44,18,24,24,26,26],65);
 const counts=table(w,'Paper_counts',[['year','paper','candidates','pending','unresolved','paper_complete','primary_temporal','secondary_temporal','protocol_descriptive','plan_descriptive'],...papers.map(p=>[year,p,candidates.filter(c=>c.package===p).length,...Array(7).fill('')])],[12,30,18,18,18,22,24,26,26,26],42);
 const planCandidates=candidates.filter(c=>['P_R','P_P'].includes(c.primary));
 const plans=table(w,'Protocol_plan_table',[['year','paper','key','relationship','title','statement','status','disposition','interpretation','internalStatus','notes'],...planCandidates.map(c=>[year,c.package,c.key,c.primary,c.title,c.statement,...Array(5).fill('')])],[12,27,44,18,60,90,24,20,28,30,60],90);
 for(const [name,rows] of Object.entries(source))table(w,name,rows,rows[0].map(k=>({key:44,title:65,statement:90,locations:75,text:115,rationale:80,href:90}[k]||26)),name==='Evidence'?180:90);
 const oldCode=JSON.parse(await fs.readFile(new URL('./codebook.json',import.meta.url),'utf8'));
 const codeRows=[oldCode[0]];
 // Keep methodological option definitions; replace the workflow guides below.
 for(const r of oldCode.slice(1))if(r[1] && !['FIELD','GUIDE'].includes(r[1]) && r[2]==='Option' && !['yes','<clear>'].includes(r[1])){
   const row=[...r];if(row[1]==='agree')row[3]='Accept the unchanged primary assessment. Keep the existing answers; select agree and checker_done. No comment is required.';
   if(row[1]==='agree_clarification')row[3]='Accept the main assessment with clarification. Edit relevant answers directly and explain in Checker comment.';
   codeRows.push(row);
 } else if(r[1]==='FIELD') codeRows.push([r[0],'FIELD',r[2],r[3].replace(/Checker blanks inherit the primary answer\./g,'Checker edits the existing answer directly.').replace(/In Checker, blank inherits; <clear> removes the inherited text\./g,'In both stages, clearing removes the answer.').replace(/Mark yes only after human review\./g,'Mark primary_done or checker_done only after human review in that stage.').replace(/then review again\./g,'then review again and mark the correct stage done.').replace(/select agree and Complete=yes only\./g,'keep the answers, select agree and Complete=checker_done.').replace(/Blank applicable judgment cells then inherit the matching snapshot\./g,'The existing judgment cells remain filled and editable; blanks do not inherit.'),r[4]]);
 else if(!r[1] && r[0])codeRows.push(r);
 // Completion options are explicit to avoid stale initial completion in checking.
 codeRows.push(['Complete','primary_done','Primary only','Human reviewed; initial stage complete. This never counts as checker completion.','reviewComplete'],['Complete','checker_done','Checker only','Second person reviewed; checker stage complete. Required discussion must also be resolved.','reviewComplete']);
 codeRows.splice(1,0,['Working method','GUIDE','Both stages','No inherited blanks or control words. Keep the existing answers; edit directly. Blank = no answer; indeterminate/unknown = uncertain; not_applicable = inactive. Clear obsolete answers after changing a branch.',''],['Required judgments','GUIDE','Retain only','statistical_results: issue + substantiveness; report_internal_inconsistency or plan_material: internalStatus. protocol_report: no extra required judgment; interpretation is optional.','']);
 const overrides={primarySummary:'Blank during primary review. In checker stage, shows the saved initial assessment matched by Candidate key. Current answers remain in the editable fields; blanks do not inherit.',readiness:'Calculated entry checks for the current stage. PRIMARY READY allows handoff; FINAL READY allows final delivery. Other messages identify missing inputs or unresolved discussion. Checks does not establish scientific accuracy or prevent edits to source/formula cells.',reviewComplete:'Use no while drafting, primary_done after primary review, checker_done after checking. Reset to no after editing a completed row; then review again. Initial completion never implies checker completion.',checkStatus:'Required in checker stage. Keep answers unchanged for agree. Every other result needs a comment; disagreements or uncertainty also require resolved discussion before final delivery.',notes:'Optional English context. Clearing removes the text; no inheritance and no control words.',resolutionStatus:'For disagree, unable, or any primary discuss, discuss together and select resolved. Record participants and the conclusion in Resolution note; update the final assessment.'};
 for(const r of codeRows)if(r[1]==='FIELD'&&overrides[r[4]])r[3]=overrides[r[4]];
 table(w,'Codebook',codeRows,[34,28,38,92,26],86);
 table(w,'Manifest',[['field','value'],['version','v.2.1.5.4'],['schema','xlsx-adjudication-excel-9'],['workflow','Excel-only; Setup stage is authoritative'],['year',year],['provenance','Frozen source catalog; candidate content unchanged. Primary backup plus value snapshot preserve original review.'],['protection','None: all sheets, cells and workbook structure are unprotected.']],[30,100],44);
 for(const p of papers){
  const s=sheets[p],cc=candidates.filter(c=>c.package===p),n=cc.length;
  for(const col of ['D','E','F','H','I','K','N','O','P','Q'])s.getRange(`${col}2:${col}${n+1}`).format.fill='#FFF2CC';
  for(const col of ['J','L','R'])s.getRange(`${col}2:${col}${n+1}`).format.fill='#EAF3FC';
  for(const [col,field] of [['D','disposition'],['E','domain'],['F','reviewComplete'],['H','statisticalIssueStatus'],['I','substantiveStatus'],['J','downstreamImpact'],['K','internalStatus'],['L','protocolInterpretation'],['N','checkStatus'],['P','resolutionStatus']])s.getRange(`${col}2:${col}${n+1}`).dataValidation={rule:{type:'list',values:opts[field].concat('HIJKL'.includes(col)?['not_applicable']:[])}};
  for(let j=0;j<n;j++){
   const r=j+2;
   for(let i=2;i<7;i++)formula(s,`${acols[i]}${r}`,`=IF(${active(i,`D${r}`,`E${r}`).replace(`D${r}="retain"`,`OR(D${r}="retain",D${r}="")`)},"","not_applicable")`);
   formula(s,`M${r}`,`=IF(${stage}="primary","",IFERROR(${preserve(lookup('Primary_snapshot','L',`A${r}`,total))},"SNAPSHOT MISSING"))`);
   hints(s,r,n,total);
  }
  s.getRange(`G2:G${n+1}`).conditionalFormats.addCustom('AND(G2<>"PRIMARY READY",G2<>"FINAL READY")',{fill:'#FFF2CC',font:{color:'#9C0006'}});
  s.getRange(`N2:Q${n+1}`).conditionalFormats.addCustom(`${stage}="primary"`,{fill:'#EDF2F5',font:{color:'#687783'}});
  for(let i=2;i<7;i++){
   const condition=active(i,'$D2','$E2').replace('$D2="retain"','OR($D2="retain",$D2="")');
   s.getRange(`${acols[i]}2:${acols[i]}${n+1}`).conditionalFormats.addCustom(`NOT(${condition})`,{fill:'#EDF2F5',font:{color:'#687783'}});
  }
 }
 for(let i=0;i<total;i++){
  const c=candidates[i],r=i+2,n=candidates.filter(x=>x.package===c.package).length,name=`C_${c.package}`;
  const sourceLookup=col=>lookup(name,col,quote(c.key),n);
  const snapExpr=[quote(c.key),...acols.map((col,j)=>j>=2&&j<7?`IF(${active(j,sourceLookup('D'),sourceLookup('E'))},${preserve(sourceLookup(col))},"not_applicable")`:preserve(sourceLookup(col))),sourceLookup('F'),'Setup!$B$2'];
  snapExpr.forEach((e,j)=>formula(snap,`${cols[j]}${r}`,`=IF(${stage}="primary",${e},"NOT FROZEN")`));
  const summary=labels.map((label,j)=>`IF(OR(${cols[j+1]}${r}="",${cols[j+1]}${r}="not_applicable"),"",${quote(label+': ')}&${cols[j+1]}${r}&CHAR(10))`).join('&');
  formula(snap,`L${r}`,`=IF(${stage}="primary",${summary},"NOT FROZEN")`);
  decisions.getRange(`A${r}:D${r}`).values=[[year,c.package,c.key,c.primary]];
  formula(decisions,`E${r}`,'=Setup!$B$2');formula(decisions,`F${r}`,`=${preserve('Setup!$B$4')}`);
  formula(decisions,`G${r}`,`=IFERROR(${sourceLookup('G')},"CHECK KEY")`);
  formula(decisions,`H${r}`,`=IF(G${r}<>"FINAL READY","",IF(S${r}<>"retain","not_eligible",IF(D${r}="P_R","protocol_descriptive",IF(D${r}="P_P","plan_descriptive",IF(AND(T${r}="statistical_results",OR(U${r}="confirmed_issue",U${r}="probable_issue"),V${r}="substantive"),"primary_temporal",IF(AND(T${r}="report_internal_inconsistency",X${r}="substantive_inconsistency"),"secondary_temporal","not_eligible"))))))`);
  decisions.getRange(`I${r}:J${r}`).values=[[c.ai_disposition,c.ai_domain]];
  const colName=index=>{let o='';for(let v=index+1;v;v=Math.floor((v-1)/26))o=String.fromCharCode(65+(v-1)%26)+o;return o;};
  for(let j=0;j<8;j++){
   formula(decisions,`${colName(10+j)}${r}`,`=IF(${stage}="primary","",IFERROR(${preserve(lookup('Primary_snapshot',cols[j+1],`C${r}`,total))},"SNAPSHOT MISSING"))`);
   const e=sourceLookup(acols[j]);formula(decisions,`${colName(18+j)}${r}`,`=${j>=2&&j<7?`IF(${active(j,sourceLookup('D'),sourceLookup('E'))},${preserve(e)},"not_applicable")`:preserve(e)}`);
  }
  ['N','O','P','Q'].forEach((col,j)=>formula(decisions,`${colName(26+j)}${r}`,`=${preserve(sourceLookup(col))}`));
 }
 formula(checks,'B2',`=${stage}`);
 formula(checks,'B4',`=COUNTIF(Decisions!G2:G${total+1},"PRIMARY READY")`);
 formula(checks,'B5',`=COUNTIF(Decisions!G2:G${total+1},"FINAL READY")`);
 formula(checks,'B6','=B3-B4-B5');
 formula(checks,'B7',`=IF(AND(B2="primary",B4=B3),"PRIMARY READY",IF(AND(B2="checker",B5=B3),"FINAL READY","ACTION NEEDED"))`);
 formula(checks,'B8','=IF(B7="PRIMARY READY","Save primary backup, then follow Start steps 5-7.",IF(B7="FINAL READY","Save the final workbook. Built-in result sheets are ready.","Open Decisions; filter status for rows needing action. Return to the matching C_ sheet."))');
 for(let i=0;i<papers.length;i++){
  const r=i+2,p=papers[i],match=`Decisions!$B$2:$B$${total+1},B${r}`;
  formula(counts,`D${r}`,`=C${r}-COUNTIFS(${match},Decisions!$G$2:$G$${total+1},"FINAL READY")-E${r}`);
  formula(counts,`E${r}`,`=COUNTIFS(${match},Decisions!$G$2:$G$${total+1},"DISCUSS")`);
  formula(counts,`F${r}`,`=IF(D${r}+E${r}=0,"yes","no")`);
  ['primary_temporal','secondary_temporal','protocol_descriptive','plan_descriptive'].forEach((o,j)=>formula(counts,`${cols[6+j]}${r}`,`=IF(F${r}<>"yes","",COUNTIFS(${match},Decisions!$H$2:$H$${total+1},"${o}"))`));
 }
 for(let i=0;i<planCandidates.length;i++){const r=i+2;['G','S','Y','X','Z'].forEach((col,j)=>formula(plans,`${cols[6+j]}${r}`,`=${preserve(lookup('Decisions',col,`C${r}`,total).replace(/\$A\$/g,'$C$'))}`));}
 // Review sheets are filterable tables; snapshot is deliberately plain for one Paste Values action.
 let ti=0;for(const name of ['Decisions','Candidates','Evidence',...papers.map(p=>`C_${p}`)]){const s=w.worksheets.getItem(name);s.tables.add(name==='Decisions'?`A1:AD${total+1}`:name.startsWith('C_')?`A1:R${candidates.filter(c=>`C_${c.package}`===name).length+1}`:name==='Candidates'?`A1:AB${total+1}`:`A1:D${source.Evidence.length}`,true,`ReviewTable${++ti}`);}
 w.recalculate();
 return {w,candidates,papers,total,sheets,snap,checks,decisions};
}

export async function fillExample(b,checker=false){
 const {w,sheets,candidates,snap,total}=b;
 val(w.worksheets.getItem('Setup'),'B2','TEST_PRIMARY');
 for(const c of candidates){const cc=candidates.filter(x=>x.package===c.package),r=cc.indexOf(c)+2,s=sheets[c.package];val(s,`D${r}`,'retain');val(s,`F${r}`,'primary_done');const domain=c.ai_domain;if(domain==='statistical_results'){val(s,`H${r}`,'confirmed_issue');val(s,`I${r}`,'substantive');}else if(['plan_material','report_internal_inconsistency'].includes(domain))val(s,`K${r}`,'substantive_inconsistency');}
 w.recalculate();if(b.checks.getRange('B7').values[0][0]!=='PRIMARY READY')console.log('DEBUG',b.decisions.getRange(`C2:G${total+1}`).values);assert.equal(b.checks.getRange('B7').values[0][0],'PRIMARY READY');
 if(checker){snap.getRange(`A1:L${total+1}`).copyFrom(snap.getRange(`A1:L${total+1}`),'values');val(w.worksheets.getItem('Setup'),'B6','checker');val(w.worksheets.getItem('Setup'),'B4','TEST_CHECKER');}
 val(w.worksheets.getItem('Start'),'B2',`TEST ONLY - SYNTHETIC ANSWERS | 2019 | v.2.1.5.4 | ${checker?'checker':'primary'} | Never include in research results`);
}
if(process.argv[1] && await fs.realpath(process.argv[1])===fileURLToPath(import.meta.url)){
 try { await fs.access(OUT); throw new Error("Output directory already exists. Choose a new ADJ_OUTPUT; do not overwrite review files."); } catch (error) { if(error.code!=="ENOENT") throw error; }
 await fs.mkdir(OUT,{recursive:true});
 for(const year of [2018,2019,2024,2025]){
  const b=await build(year);console.log(year,b.total,b.checks.getRange('A2:B8').values);
  await save(b.w,`${OUT}/human_adjudication_v_2_1_5_4_${year}.xlsx`);
  if(year===2019){
   const preview=await b.w.render({sheetName:'Start',range:'A1:B8',scale:1.1,format:'png'});await fs.writeFile('/tmp/adjudication-excel-only/start.png',new Uint8Array(await preview.arrayBuffer()));
   await fillExample(b);await save(b.w,`${OUT}/examples/human_adjudication_v_2_1_5_4_2019_TEST_primary_complete.xlsx`);
   b.snap.getRange(`A1:L${b.total+1}`).copyFrom(b.snap.getRange(`A1:L${b.total+1}`),'values');val(b.w.worksheets.getItem('Setup'),'B6','checker');val(b.w.worksheets.getItem('Setup'),'B4','TEST_CHECKER');val(b.w.worksheets.getItem('Start'),'B2','TEST ONLY - SYNTHETIC ANSWERS | 2019 | v.2.1.5.4 | Checker ready | Never include in research results');
   await save(b.w,`${OUT}/examples/human_adjudication_v_2_1_5_4_2019_TEST_checker_ready.xlsx`);
  }
 }
}
export {save,ROOT,OUT,headers,opts};
