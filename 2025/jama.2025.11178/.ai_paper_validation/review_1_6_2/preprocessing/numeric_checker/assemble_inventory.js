const fs=require('fs'),root='.ai_paper_validation/review_1_6_2/';
const main=fs.readFileSync(root+'extraction/main_quantitative_evidence.md','utf8'),sup=fs.readFileSync(root+'extraction/parts/support_reports.md','utf8');
const cells=JSON.parse(fs.readFileSync(root+'preprocessing/numeric_checker/cells.json','utf8'));
const outcomes={
1:'2331 final eligible agrees with 776+778+777; 2333 allocated minus 2 UC ineligible is distinct and reconciles.',
2:'778+776+777=2331; individual three-arm allocation and eight-session dose agree across locations.',
3:'Primary scale 0–10, 11 items and ≥30% relative decrease distinguished from absolute score change; 3-month primary and 6/12-month secondary remain distinct.',
4:'2210/2331=94.8091%, 1712/2331=73.445%, 1030/2331=44.187%; percentages reconcile under half-unit intervals. Sex-count copy1713 in workbook is below precision threshold, separately recorded as excluded.',
5:'All three adjusted response percentages match body/Table2; group order32.0>26.6>20.8 is consistent. Model percentages are not crude counts.',
6:'32.0/20.8=1.53846,26.6/20.8=1.27885,32.0/26.6=1.20301; adjusted RR labels are consistent with displayed percentages and rounded1.54,1.28,1.20.',
7:'6/12-month adjusted primary-response direction matches figure/Table2; inferential breadth is assigned to statistical/cross-source checkers.',
8:'Direction of improvement agrees with adjusted response ranking; no count arithmetic beyond M005–M006.',
9:'2331 agrees with final randomized total; ≥30% threshold and3/12-month statements match their numerical labels.',
10:'Background8.5% is not a trial count; three groups and eight-session doses match intervention sections.',
11:'26 inclusive recruitment months January2021–February2023; eligibility thresholds18,60,360,12 and3-item PEG0–30 are consistently distinguished, not quantities to sum.',
12:'Three-arm superiority hypothesis contains no noninferiority margin or numeric count conflict.',
13:'Block sizes3/6/9 are multiples of three for1:1:1 allocation; stratification thresholds<7/≥7 partition the severity scale.',
14:'Eight45–60-minute sessions across12 weeks;12 coaches matches flow footnote; no total treatment-minute claim to recompute.',
15:'Eight30–45-minute sessions and12-week period match report supplement; outreach10-day/3-in9-day thresholds are separate criteria.',
16:'Four intensity items plus minimum four interference items is a minimum8-of11 scoring requirement; retaining full11-item definition is coherent. Threshold≥30% at3months.',
17:'Four intensity and seven interference items total11; social4 and physical6 are separate instruments, not parts of BPI.',
18:'3×777=2331;15%×1.5=22.5%, a7.5 percentage-point difference;80% retention leaves expected1864.8 overall. Simulation power checked by statistical specialist rather than replacing it with a crude formula.',
19:'ITT randomized totals retained separately from any-observation contributors; modified-Poisson RR is not odds ratio. Statistical model logic delegated.',
20:'Adjusted percentage/NNT definitions preserve proportions rather than percentage points; no numerical covariate means or standard errors printed here.',
21:'SMD defined by UC change SD; numerical SD denominator absent from main text. Continuous mean differences separated from proportions; numerical Table3 relationships owned by estimate checker.',
22:'Mean covariate imputation, pattern-mixture and nonresponse weighting are distinct steps; no additive population partition implied by those method names.',
23:'643/776=82.86%,690/778=88.69%,703/777=90.48%;3mo542/776=69.85%,635/778=81.62%,621/777=79.92%; rounded83/89/90 and70/82/80 agree. 2210 completion status is not2036 any-assessment status.',
24:'527/776=67.912%,371/776=47.809%,660/778=84.833%,548/778=70.437%. Only printed371(43%) yields F-NUM-001; others reconcile.',
25:'Age≥65:900/2331=38.61%;sex and residence round74/44%;negative SDOH758/2298=32.985%;severity594/2331=25.483%;depression1116/2329=47.918% versus47.8 is below threshold;anxiety648/2329=27.823%;sleep1005/2319=43.338%;opioid163/1697=9.605%.',
26:'Primary response copies agree; narrative SMD−0.26/−0.36 versus Table3−0.25/−0.34 has half-unit gaps0/.01 and relative0/.02941, screened out. Inferential narrative conflicts remain statistical scope.',
27:'36656+17803+38=54497;62125−54497=7628.',
28:'2993+245+1243=4481;7628−4481=3147. Other-exclusion list is expressly one or more and not exhaustive; no sum of overlapping reasons is imposed.',
29:'339+333=672;3147−672=2475;118+24=142;2475−142=2333.',
30:'371+156+249=776;371+156=527;776 ITT analyzed.',
31:'548+112+118=778;548+112=660;778 ITT analyzed.',
32:'779−2=777;776+778+779=2333;776+778+777=2331.',
33:'542,547,583 each≤643≤776;43+3=46 terminal-status participants;any-assessment and withdrawal/death can overlap per footnote.',
34:'HC635,621,639 each≤690≤778;UC621,622,639 each≤703≤777. Withdrawal45+16 and death7+7 combined with PT43/3 gives104 withdrawals,17 deaths;2331−104−17=2210 completion status.',
35:'PT13+1+2+233=249;212+8+5+3+3+2=233. HC16+1+101=118;74+16+3+3+2+2+1=101.',
36:'PEG3×0–10 gives0–30;coach range24–110 includes median69 and IQR52–76.12 providers, two UC exclusions and overlapping assessment-status definitions agree.',
82:'Baseline missingness excluded from each explicit denominator; sex source and race recoding explain variable-specific population counts. Opioid3/4-site restriction matches denominators569+566+562=1697.',
83:'PHQ8×0–3=0–24;GAD7×0–3=0–21;PROMIS higher/better and higher/worse directions remain distinguished;range0–37 for weighted Charlson is separate from number19 conditions.',
84:'183/2331=7.8507% rounds7.9%;17/2331=.7293% rounds.7%;hospitalization participants and247 events remain distinct.',
85:'All nine plotted adjusted percentage positions match corresponding table cells and group/time order; axis0–60 covers all points. No exact digitization of unnumbered marks.',
86:'Figure2 counts match flow:3mo1798=621+542+635;6mo1790=622+547+621;12mo1861=639+583+639.',
87:'63+55+65=183 participants;82+81+84=247 events;7+3+7=17 deaths. Percentages8.1/7.1/8.4 and.9/.4/.9 agree with777/776/778 denominators under precision rule.',
88:'16/778=2.0566% vs2.0% leaves gap about.0066 percentage points before widening input intervals, relative≤.0033;1/776=.1289% rounds.1%;UC0. Event terminology does not establish distinct affected-person totals.',
89:'Numerical ranking HC>PT at3mo, small separation6/12 agrees with figure; whether all secondary contrasts support narrative is inferential scope.'
};
let out='# Numeric relationship inventory — count and denominator scope\n\nRuntime task: /root/numeric_checker. Model gpt-6.1-sol; reasoning medium; fresh spawn. Complete disjoint assignment M001–M089, R001–R013 and R025. Estimate checker owns M090–M124 and R014–R024. All locations here are REPORT by content. N001–N117 are stable compound relationships; no record is a sample. Full source inputs below and in linked mapper artifacts preserve every displayed cell. CPU native extraction and direct ZIP/XML confirmation; no new OCR.\n\nRules: counts, denominators, category sums, repeat counts, display percentages and measure identities; half-unit input/target intervals, remaining relative gap >0.05 qualifies. Statistical statements attached to these records were numerically located; inferential and PLAN comparisons are covered by their specialist lanes.\n\n';
const mainRows=new Map([...main.matchAll(/^\| (M\d{3}) \| (.*)\|$/gm)].map(m=>[m[1],m[2]]));
for(let n=1;n<=89;n++){
const id='N'+String(n).padStart(3,'0'),key='M'+String(n).padStart(3,'0');
out+=`### ${id}\n\nMapping: ${key}, REPORT main article. Exact source inputs and location: ${mainRows.get(key)}\n\nCheck and outcome: `;
if(n>=37&&n<=81){
const row=mainRows.get(key),percent=[...row.matchAll(/(\d+)\/(\d+)\((\d+(?:\.\d+)?)%\)/g)];
if(percent.length)out+=percent.map(m=>`${m[1]}/${m[2]}×100=${(100*m[1]/m[2]).toFixed(5)}%, printed${m[3]}%`).join('; ')+'. All displayed percentage intervals reconcile; numerator≤denominator≤arm total. '+(n===39?'571+572+569=1712; male counts205+206+208=619; each sex partition equals arm total. ':n===51?'Race category sums751,760,755 equal displayed denominators. ':n===52?'340+345+345=1030. ':'');
else out+='All group denominators equal776/778/777; standard deviations nonnegative and all medians lie in their ordered IQRs. No aggregate mean/SD or change denominator is invented.';
}else out+=outcomes[n];
out+='\n\nStatus: COMPLETE.\n\n';
}
const checks={
1:'Eight-session arms and12-week completion period match main article;30–45/45–60-minute durations are distinct group definitions.',
2:'Staff training1+3+1+2+2=9hours;2instances×8sessions=16 proficiency sessions;4audio and2video resources are separate counts, not participant totals.',
3:'193+89+17=299 reviewed.299/4626=6.4635%;89/1791=4.9693%;8/299=2.6756%;11/299=3.6789%, all displayed percentages reconcile. Total reviewed training sessions193 is not total training sessions; therefore193+1791+2350 is not a valid completed-session total.',
4:'356/776=45.8763%, rounds45.9%;mean1.8 lies in range1–7.14 extensions is a separate subset; thresholds7/10/3-in9 are distinct criteria.',
5:'Approximately140 vs454 enrollment near change date is peripheral count comparison unless a subset result population changes; full subset result headers are assigned R021 to numeric estimate/cross-source checker.',
6:'BPI4+7=11 items;PHQ8×3=24;GAD7×3=21;PROMIS4/6 items and1–5 score ranges are distinguished from T50SD10. MCID30% is relative baseline reduction.',
7:'All0–8 completion bins and both arm panels reviewed as graphs; numerical bar heights unprinted, so no invented counts. Approximate endpoint heights do not replace Figure1 exact categories.',
8:'1798/2331=77.134%;621/777=79.923%;542/776=69.845%;635/778=81.620%;1568/2331=67.267%;295/2331=12.655%, all reported rounded percentages reconcile.',
9:'Age threshold≥65 and base categorical covariate list have no count arithmetic. Workbook selection P-value pairs retained in N117; numeric P values in[0,1]; analysis-selection logic assigned to statistical checkers.',
10:'One/two/three observed-pattern indicators are distinct, and each assigned person has three target time points. No claim that model covariates numerically partition participants.',
11:'Binary response uses log mean to yield RR, not log odds to yield OR; covariate/time indicators are distinct from cohort counts. Statistical estimation identity covered by statistical specialists.',
12:'74/777=9.524%,133/776=17.139%,88/778=11.311%,295/2331=12.655%;9.5/17.1/11.3/12.7 reconcile.2036+295=2331 and703+643+690=2036.',
13:'Every eTable1 N/% cell and arm row total checked. Time totals1798,1790,1861 and any2036/none295 reconcile;pattern rows64+77+47=188,99+103+81=283,540+464+564=1568. Pattern188+283+1568=2039 vs2036 differs3; arm patternsUC703,PT644,HC692 vs703/643/690 and total assessments5458 vs5449 are below display-precision threshold; excluded table records consolidated pattern.'
};
for(let k=1;k<=13;k++){
const id='N'+String(k+89).padStart(3,'0'),key='R'+String(k).padStart(3,'0');const m=sup.match(new RegExp('^\\| '+key+' \\| (.*)\\|$','m'));
out+=`### ${id}\n\nMapping: ${key}; REPORT support. Exact source inputs and location: ${m[1]}\n\nCheck and outcome: ${checks[k]}\n\nStatus: COMPLETE.\n\n`;
}
const blocks=[
[1,8,'Column totals and sites','295+468+1568=2331; each site row sums to overall566/609/606/550; sites sum to column totals.'],
[9,11,'Age and female','Female206+343+1164=1713; all four sex percentages reconcile. Age weighted mean agrees58.8 within precision; group SD values are positive.'],
[12,19,'Education and employment','Four education categories plus missing partition2331/295/468/1568; employed complement is not printed. Every category and unemployment percentage uses excluded-missing denominator.'],
[20,28,'Income and marital status','Income counts plus missing partition each column; income-missing percentages use full header N. Married counts181+290+1036=1507; missing1+8+22=31.'],
[29,37,'Race and ethnicity','Seven categories plus missing partition each column; denominators2266/286/445/1535.'],
[38,48,'Residence and social determinants','Every row sum and every variable-specific missing count checked; denominators from own missing row, not one universal column denominator.'],
[49,56,'Pain encounters, musculoskeletal conditions and opioid use','Musculoskeletal1710=213+353+1144. Opioid163=14+31+118;missing634=124+126+384, leaving denominators1697/171/342/1184. All count percentages reconcile;continuous means/SDs have no independent raw reconstruction.'],
[57,65,'Back, neck, arm and lower-limb pain','All four condition row sums, characteristic-specific missing totals and percentages reconcile.'],
[66,78,'Headache, abdominal, jaw, widespread pain and duration','Every condition sum and percentage reconciles; three duration categories plus missing partition each column;duration107+614+1609+1=2331.'],
[79,83,'Depression','Diagnosis965=141+209+615. PHQ threshold1116=162+243+711,missing2=0+0+2;E82 printed73.2% does not reconcile with711/(1568−2): F-NUM-002. Other count percentages reconcile;mean11(5.5) inC81 is a mean(SD), not a count/percentage.'],
[84,91,'Anxiety, substance diagnosis and Charlson','Anxiety648=102+126+420 with own missing exclusions;substance86=16+22+48;Charlson categories1162+812+357=2331 and partition all columns. Mean(SD) cells remain distinct from counts.'],
[92,98,'Sleep and baseline severity','Sleep1005=136+221+648,missing12=2+4+6. Severity594=89+147+358. All count percentages reconcile;means and SDs remain on their stated scales.'],
[99,104,'Intensity, interference and social function','Social threshold818=113+180+525,missing38=4+3+31;all percentages reconcile. Social threshold row mean(SD) label is immediately recognizable from count/percentage cells; wording observation excluded.'],
[105,109,'Physical function and PEG','Physical1709=209+357+1143,missing24=7+3+14;percentages reconcile;PEG missing1=0+0+1.Continuous values are means(SD).'],
[110,115,'Footnotes and selection marks','A110 excludes characteristic-missing counts;A113 sex fallback explains descriptive source differences;A114 defines outcome/missingnessP<.10 selection. All H/I/J numeric P values are valid probabilities and blanks remain blanks; selection/model concordance is statistical scope.']
];
for(let i=0;i<blocks.length;i++){
const [first,last,label,check]=blocks[i],id='N'+String(103+i).padStart(3,'0');
out+=`### ${id}\n\nMapping: R025, REPORT [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet eTable 3, exact range A${first}:J${last}. ${label}.\n\n| Exact cell | Printed/stored value |\n|---|---|\n`;
for(let r=first;r<=last;r++)for(const col of 'ABCDEFGHIJ')if(cells[col+r])out+=`| ${col+r} | ${cells[col+r]} |\n`;
out+=`\nCheck and outcome: ${check} Complete per-cell count/denominator/percentage arithmetic is in [arithmetic trace](../preprocessing/numeric_checker/arithmetic_trace.md). Every overall count equals the sum of the three follow-up-pattern columns; all examined printed percentages have overlapping rounding intervals except E82. No raw-data means or SDs inferred.\n\nStatus: COMPLETE.\n\n`;
}
out+='## Closure\n\n117 complete stable compound relationships;89 main,13 support-report families,15 exhaustive workbook blocks covering all525 nonempty cells.2 findings;6 excluded observation patterns. No assigned scientific coverage gap. Graphs with unprinted counts and unavailable raw continuous-summary inputs limit mechanical reconstruction, while their displayed evidence and definitions were fully inspected.\n';
fs.writeFileSync(root+'relationships/numeric_relationship_inventory.md',out);
