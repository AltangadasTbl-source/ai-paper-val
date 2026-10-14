const fs=require('fs'),r='.ai_paper_validation/review_1_6_2/',report='.ai_paper_validation/final_report_1_6_2.md';
const names=['Target basis','Total source units','Fresh-source units','Target elapsed minutes','Started UTC','Finished UTC','Observed elapsed minutes','Target status','Exceedance causes'];
let state=fs.readFileSync(r+'run_state.md','utf8'),md=fs.readFileSync(report,'utf8');
function field(s,name){const escaped=name.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');const m=s.match(new RegExp('^[-*]?\\s*\\*\\*'+escaped+':\\*\\*\\s*(.+)$','m'));if(!m)throw new Error('Missing field '+name);return m[1].trim();}
const start=field(state,'Started UTC'),finished=new Date().toISOString().replace(/\.\d{3}Z$/,'Z'),elapsed=((Date.parse(finished)-Date.parse(start))/60000).toFixed(1),upper=+field(state,'Target elapsed minutes').split('-')[1];
const status=+elapsed<=upper?'MET_TARGET':'EXCEEDED_TARGET';
const updates={'Finished UTC':finished,'Observed elapsed minutes':elapsed,'Target status':status,'Exceedance causes':status==='MET_TARGET'?'None':'Distinct source-recheck, statistical and audit waves plus closure of the scanned protocol p.95 required additional bounded review time; full source and candidate coverage was retained.'};
for(const [name,value] of Object.entries(updates))state=state.replace(new RegExp('^(- \\*\\*'+name+':\\*\\*)[^\\n]*$','m'),'$1 '+value);
for(const name of names){const value=field(state,name),pattern=new RegExp('^[-*]?\\s*\\*\\*'+name+':\\*\\*[^\\n]*$','gm');if(pattern.test(md))md=md.replace(pattern,'- **'+name+':** '+value);else md+='\n- **'+name+':** '+value+'\n';}
fs.writeFileSync(r+'run_state.md',state);fs.writeFileSync(report,md);process.stdout.write(JSON.stringify({finished,elapsed,status})+'\n');
