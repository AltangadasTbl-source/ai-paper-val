const fs=require('fs');
const root='.ai_paper_validation/review_1_6_2/';
const main=fs.readFileSync(root+'extraction/main_quantitative_evidence.md','utf8');
const sup=fs.readFileSync(root+'extraction/parts/support_reports.md','utf8');
const cells={};
for(const m of sup.matchAll(/^\| eTable 3!([A-J]\d+) \| (.*?) \| None \|$/gm))cells[m[1]]=m[2];
const totals={B:2331,C:295,D:468,E:1568};
const missing={13:17,14:17,15:17,16:17,18:19,21:26,22:26,23:26,24:26,25:26,27:28,30:37,31:37,32:37,33:37,34:37,35:37,36:37,39:40,41:42,43:44,45:46,47:48,55:56,58:59,60:61,62:63,64:65,66:67,68:69,70:71,72:73,75:78,76:78,77:78,82:83,85:86,93:94,103:104,106:107};
let trace='# Auxiliary arithmetic trace\n\nPure calculator output; interpretation and inclusion decisions are agent-authored. Percent intervals use displayed inputs ± half a unit. Count intervals are conservatively widened although counts are integers.\n\n| Cell | Printed | Denominator | Recomputed % | Recomputed interval | Interval gap / printed % |\n|---|---|---:|---:|---|---:|\n';
const countRows=[5,6,7,8,11,13,14,15,16,18,21,22,23,24,25,26,27,30,31,32,33,34,35,36,38,39,41,43,45,47,54,55,58,60,62,64,66,68,70,72,75,76,77,80,82,85,87,89,90,91,93,98,103,106];
for(const col of ['B','C','D','E'])for(const row of countRows){
const value=cells[col+row];if(!value)continue;
const m=value.match(/^(\d+) \((\d+(?:\.\d+)?)\)$/);if(!m)continue;
const n=+m[1],p=+m[2];let miss=0;if(missing[row])miss=+(cells[col+missing[row]]||'0').split(' ')[0];
const den=totals[col]-miss,lo=100*(n-.5)/(den+(missing[row]?1:.5)),hi=100*(n+.5)/(den-(missing[row]?1:.5));
const h=m[2].includes('.')?.05:.5;const gap=Math.max(0,lo-p-h,p-h-hi);
trace+=`| ${col+row} | ${value} | ${den} | ${(100*n/den).toFixed(5)} | [${lo.toFixed(5)}, ${hi.toFixed(5)}] | ${(p?gap/p:gap).toFixed(8)} |\n`;
}
trace+='\n## Main baseline count percentage calculations\n\n';
for(const line of main.split('\n').filter(x=>/^\| M0(?:3[7-9]|[4-7]\d|8[01]) \|/.test(x))){
trace+=line+'\n';
for(const m of line.matchAll(/(\d+)\/(\d+)\((\d+(?:\.\d+)?)%\)/g))trace+=`${m[1]}/${m[2]} = ${(100*(+m[1])/(+m[2])).toFixed(5)}%; printed ${m[3]}%.\n`;
}
fs.writeFileSync(root+'preprocessing/numeric_checker/arithmetic_trace.md',trace);
fs.writeFileSync(root+'preprocessing/numeric_checker/cells.json',JSON.stringify(cells,null,2));
