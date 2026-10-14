const fs=require('fs'),r='.ai_paper_validation/review_1_6_2/';
let out='# Complete current-run checker exclusion audit bundle\n\nMechanical lossless excerpts; canonical checker files remain authority. All44 rows retained: numeric6+7, cross13+3, statistical15.\n\n';
for(const name of ['numeric_consistency','cross_source_consistency','statistical_pass_1']){
 const s=fs.readFileSync(r+'checkers/'+name+'.md','utf8');
 out+='## '+name+'\n\n';
 const lines=s.split('\n');let collecting=false;
 for(const line of lines){if(/^## Excluded observations/.test(line)) collecting=true;else if(collecting && /^## /.test(line)) collecting=false;if(collecting)out+=line+'\n';}
}
fs.writeFileSync(r+'checkers/excluded_observations_bundle.md',out);
let cross=fs.readFileSync(r+'checkers/cross_source_consistency.md','utf8');
fs.writeFileSync(r+'checkers/cross_findings_excerpt.md','# Complete current cross-source finding and excluded-observation excerpt\n\n'+cross.slice(cross.indexOf('## Findings')));
