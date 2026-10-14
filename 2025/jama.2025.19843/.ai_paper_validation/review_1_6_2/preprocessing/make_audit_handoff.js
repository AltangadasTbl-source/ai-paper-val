const fs=require('fs'),path=require('path'),r='.ai_paper_validation/review_1_6_2/';
const parts={coverage_main_protocol:['Complete individual source-unit closure','Complete individual numeric-relationship closure'],coverage_support:[],cross_source_audit:['Complete relationship audit ledger'],statistical_audit:[]};
function links(s,from,to){return s.replace(/\]\((<?)([^)\n]+?)(>?)\)/g,(m,l,u,r)=>{if(/^(?:https?:|#|mailto:)/.test(u))return m;const i=u.indexOf('#'),file=i<0?u:u.slice(0,i),anchor=i<0?'':u.slice(i);return ']('+l+path.relative(to,path.resolve(from,file)).split(path.sep).join('/')+anchor+r+')';});}
let out='# Bounded scientific audit handoff\n\nThis mechanical excerpt retains all scientific conclusions, exclusions, source facts, repairs and limitations from four complete fresh audit parts. It omits routine individually enumerated closure ledgers whose complete independent audit is documented in the linked parts, preserved unchanged in each linked full artifact and losslessly merged into the final canonical audit. The mandatory auditor separately checks the complete coverage manifest/source-coverage rows and stable candidates. No candidate selection or classification is performed by this helper.\n\n';
for(const [name,omitted] of Object.entries(parts)){
 const f=r+'quality/parts/'+name+'.md',s=fs.readFileSync(f,'utf8');let keep=true,excerpt='';
 for(const line of s.split('\n')){if(/^## /.test(line))keep=!omitted.includes(line.slice(3));if(keep)excerpt+=line+'\n';}
 out+='## Full audit part: '+name+'\n\n[Full durable artifact](parts/'+name+'.md). Omitted completion-only sections: '+omitted.join('; ')+'.\n\n'+links(excerpt,path.dirname(path.resolve(f)),path.resolve(r+'quality'))+'\n';
}
fs.writeFileSync(r+'quality/audit_handoff.md',out);
