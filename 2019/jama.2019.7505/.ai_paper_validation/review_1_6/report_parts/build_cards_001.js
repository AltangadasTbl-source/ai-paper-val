const fs = require('fs');
const path = require('path');
const root = process.cwd();
const base = '.ai_paper_validation/review_1_6/';
const handoff = fs.readFileSync(base+'handoffs/report_001.md','utf8');
const classifications = JSON.parse(fs.readFileSync(base+'verification/recheck_classification.json','utf8'));
const ledger = fs.readFileSync(base+'candidate_ledger.md','utf8');
const statements = [
'The abstract labels group sizes 989 and 987 as randomized, whereas Figure 1 reports allocation sizes 1011 and 1002; the smaller sizes match the analyzed population.',
'The abstract and Table 3 give opposite signs for the upper confidence limit of the same hypoxemia difference: +6.1% versus −6.1%.',
'The H-arm abdominal and nonabdominal rows use denominators 986 and 987 although their counts sum to 986. A discrepancy depends on the rows being one complementary classification.',
'The L-arm abdominal and nonabdominal rows use denominators 987 and 986 although their counts sum to 986. A discrepancy depends on the rows being one complementary classification.',
'The H-arm reflux percentage 33.6% does not follow nearest one-decimal rounding of the explicit fraction 332/986; truncation reproduces the display.',
'The H-arm diabetes percentage 29.7% does not follow nearest one-decimal rounding of 294/988; truncation reproduces the display.',
'The H-arm oral-medication percentage 71.0% does not follow nearest one-decimal rounding of 209/294; truncation reproduces the display.',
'The registered comparison contains a record_input_error: it treated header n=987 as the exact observed denominator for 264 (26.8%) low-group obstructive-sleep-apnea cases. The source permits missing characteristics and does not supply that row denominator; a percentage contradiction is not established.',
'The H-arm never-tobacco cell 549/987 (55.5%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.',
'The L-arm never-tobacco percentage 53.2% does not follow nearest one-decimal rounding of 525/985; truncation reproduces the display.',
'The H-arm previous-tobacco percentage 27.6% does not follow nearest one-decimal rounding of 273/987; truncation reproduces the display.',
'The L-arm current-tobacco percentage 18.8% does not follow nearest one-decimal rounding of 186/985; truncation reproduces the display.',
'The H-arm antibiotic-prophylaxis cell 938/987 (94.8%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.',
'The L-arm antibiotic-prophylaxis cell 949/985 (96.1%) does not reconcile under nearest one-decimal rounding or simple truncation of its explicit fraction.',
'The monitoring percentages 64.9% and 67.7% subtract to −2.8 percentage points, whereas the reported difference is −1.8. Their population and estimand alignment requires clarification; the explicit fractions instead reproduce −1.8.',
'The reversal percentages 74.3% and 75.2% subtract to −0.9 percentage points, whereas the reported difference is +0.2. Their population and estimand alignment requires clarification. The exact slash fractions produce +0.251478, nearest +0.3; +0.2 is compatible with truncation.',
'Recruitment difference 97.1 does not follow nearest one-decimal rounding of the count/header calculation, conditional on headers 989/987 being the row denominators and the effect being a raw risk difference. Truncation reconciles that calculation.',
'The Table 2 heading “Heat rate” accompanies beats/min measurements, while the article defines bradycardia using “heart rate” in the same unit; the intended measure heading requires confirmation.',
'The noninvasive-ventilation low cell prints 264 (26.8%), without a slash denominator. A nearest-rounding gap occurs only if header n=987 is the row denominator; the row-specific denominator and display rule are unreported.',
'The noninvasive-ventilation difference 0.9 differs from nearest rounding of a count/header calculation, conditional on the headers being row denominators and the effect being a raw risk difference. Printed-percentage subtraction and truncation both reconcile 0.9.',
'The monitoring H cell 632/982 (64.9%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 974 reproduces the percentage diagnostically.',
'The monitoring L cell 651/984 (67.7%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 961 reproduces the percentage diagnostically.',
'The reversal H cell 724/982 (74.3%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 974 reproduces the percentage diagnostically.',
'The reversal L cell 723/984 (75.2%) has an attached percentage differing from division of its explicit fraction; division by the neighboring blockade count 961 reproduces the percentage diagnostically.',
'The reversal difference +0.2 differs from nearest rounding of the exact slash-fraction difference +0.251477820 by a small amount: nearest rounding gives +0.3, whereas truncation gives +0.2. This comparator is distinct from C016’s subtraction of printed percentages.',
'The registered comparison contains a record_input_error: it assumed the generic total-fluids Absolute Difference +0.02 L must subtract the displayed medians 1.5 and 1.6 L. The source does not define it as a difference of medians; a confirmed effect inconsistency is not established.',
'The primary PPC risk ratio 0.93 differs from the H/L event-risk ratio 0.903748096 computed from 211/989 and 233/987. The point-estimate formula, conditioning, adjustment and display convention require clarification; a distinct reverse-conditioning diagnostic can reproduce the printed point.'
];
const impacts = [
'randomized allocation sizes 989/987 instead of 1011/1002, thereby conflating allocated and analyzed denominators by 37 patients',
'an upper confidence limit of +6.1% instead of −6.1%, changing the extracted interval’s null-crossing description',
'H surgical-approach denominators 986 and 987 without knowing whether the two categories share one observed population',
'L surgical-approach denominators 987 and 986 without knowing whether the two categories share one observed population',
'the H reflux percentage 33.6% together with a fraction that gives 33.671399594%',
'the H diabetes percentage 29.7% with the explicit fraction 294/988',
'the nested H oral-medication percentage 71.0% with the explicit fraction 209/294',
'an unsupported obstructive-sleep-apnea denominator 987 reconstructed from the group header',
'the H never-tobacco percentage 55.5% with the explicit fraction 549/987',
'the L never-tobacco percentage 53.2% with the explicit fraction 525/985',
'the H previous-tobacco percentage 27.6% with the explicit fraction 273/987',
'the L current-tobacco percentage 18.8% with the explicit fraction 186/985',
'the H antibiotic-prophylaxis percentage 94.8% with the explicit fraction 938/987',
'the L antibiotic-prophylaxis percentage 96.1% with the explicit fraction 949/985',
'monitoring percentages 64.9%/67.7% and difference −1.8 as though all three summarize the same population',
'reversal percentages 74.3%/75.2% and positive difference +0.2 without documenting their different possible denominator mappings',
'recruitment difference 97.1 with assumed row denominators 989/987 and an assumed nearest-rounding rule',
'“Heat rate” as a variable label for the three beats/min rows',
'26.8% and a reconstructed denominator 987 for the low-group noninvasive-ventilation row',
'difference 0.9 as a raw count/header risk difference without preserving its unresolved denominator and display convention',
'monitoring H numerator 632, denominator 982 and percentage 64.9% as one population summary',
'monitoring L numerator 651, denominator 984 and percentage 67.7% as one population summary',
'reversal H numerator 724, denominator 982 and percentage 74.3% as one population summary',
'reversal L numerator 723, denominator 984 and percentage 75.2% as one population summary',
'reversal difference +0.2 with an assumed nearest-rounding convention rather than preserving the coherent truncation alternative',
'+0.02 L as an unsupported difference of medians instead of retaining an unspecified location-effect estimand',
'RR 0.93 and its interval as the H/L patient event-risk contrast without resolving the exact point-estimate definition'
];
const fieldMap = {'Category':'category','Relationship type':'type','All relationships':'all','Compared document roles':'roles','Review domain':'domain','Evidence state':'state','Suggested review disposition':'suggestion','Classification rationale':'rationale','Classification ambiguity':'ambiguity'};
const required = ['Candidate statement',...Object.keys(fieldMap),'Exact source locations','Source evidence','Reported-versus-comparator','Reasoning procedure','Calculation','Alternative source-grounded interpretations','Mechanical evidence recheck','Quality-control relevance','Potential downstream evidence impact','Human verification steps','Human adjudication fields'];
let cards=[];
for (const block of handoff.split(/(?=^## C\d{3} — )/m).filter(x=>/^## C/.test(x))) {
  const id=block.match(/^## (C\d{3})/)[1], n=+id.slice(1);
  const c=classifications.find(x=>x.id===id);
  const facts=block.split('### Mechanical evidence recheck update')[1];
  const value=label=>{const m=facts.match(new RegExp('^- '+label+': (.*)$','m'));if(!m)throw Error(id+' missing '+label);return m[1]};
  let title=block.split('\n')[0];
  if(n===8)title='## C008 — Obstructive-sleep-apnea header-denominator input error';
  if(n===26)title='## C026 — Unsupported total-fluids median/effect alignment';
  let tolerance;
  if([1,3,4].includes(n))tolerance='Exact integer counts and population labels have zero arithmetic tolerance; the applicability of a shared population is considered separately.';
  else if(n===2)tolerance='Matched signed endpoints have zero identity tolerance; ±0.05 percentage point endpoint rounding cannot reconcile a 12.2-point gap.';
  else if([15,16].includes(n))tolerance='Joint tolerance is 0.15 percentage point when two percentages and their difference are each displayed to one decimal under nearest rounding.';
  else if(n===18)tolerance='This is an exact label/unit comparison, with no numeric rounding tolerance and no re-estimation.';
  else if(n===26)tolerance='Conditional nearest-rounding bins are ±0.05 L for each median and ±0.005 L for the effect; the prerequisite median-difference estimand is unsupported.';
  else if(n===27)tolerance='The point-display tolerance under nearest two-decimal rounding is ±0.005. It does not license substituting a different conditioning or adjusted estimand.';
  else tolerance='Nearest one-decimal display tolerance is ±0.05 percentage point; applicability depends on the stated fraction/population and display rule. Truncation is evaluated separately.';
  let alt=value('Alternative and direct-versus-inferred boundary');
  if([9,13,14].includes(n))alt=alt.replace('The actual display might truncate rather than round, or the percentage might use a different population.','Simple one-decimal truncation does not reproduce this cell, as shown above. A different percentage population or another display procedure would need to be identified.');
  let calculation=value('Reproduced calculation');
  if(n===16)calculation+=' Truncation toward zero of +0.251477820 gives +0.2, a conditional alternative documented separately in C025.';
  if(n===27)alt+=' All four 2×2 cells are positive: 211, 778, 233 and 754. Generic zero-cell corrections are therefore not an explanation. Truncating the stated event-risk ratio itself gives 0.90, not 0.93; only the separately defined reverse-conditioning diagnostic described above reproduces 0.93 with truncation.';
  const relevance=n===8||n===26 ? 'The quality-control issue is the unsupported input alignment in the registered comparison. Retaining the stable ID and its record_input_error state prevents a conditional diagnostic from being presented as a confirmed source contradiction.' : 'This candidate identifies a reproducible numeric, denominator, display or measure-label comparison within the supplied REPORT. Small preventable reporting defects can matter for downstream evidence extraction; the named population, estimand or display questions bound this observation.';
  let steps='1. Open the linked physical PDF page(s) and inspect the named row, heading, reference population and applicable footnotes.\n2. Transcribe the printed inputs exactly, retaining signs, units, slash denominators and header-versus-row distinctions.\n3. Reproduce the comparison and calculation above under its stated rule and tolerance; then test the source-grounded alternatives without assigning an unstated denominator or estimator.\n4. Resolve the specific question: '+value('Missing definition and human question')+'\n5. Record the human decision in the blank fields below; the suggested review disposition is a mechanical pre-fill, not an adjudication.';
  cards.push(title+'\n\nPending Human Adjudication.\n\n**Candidate statement:** '+statements[n-1]+'\n\n'+Object.entries(fieldMap).map(([label,key])=>'**'+label+':** '+c[key]).join('\n\n')+'\n\n**Exact source locations:** '+value('Locations')+'\n\n**Source evidence:** '+value('Printed inputs')+'\n\n**Reported-versus-comparator:** '+value('Registered comparator/rule')+'\n\n**Reasoning procedure:** Read the printed components at the linked source locations, distinguish observed values from conditional calculations, and apply the comparison rule above. '+tolerance+'\n\n**Calculation:** '+calculation+'\n\n**Alternative source-grounded interpretations:** '+alt+'\n\n**Mechanical evidence recheck:** '+value('Determining fact/state')+' This field reports the completed source recheck; it is not human adjudication.\n\n**Quality-control relevance:** '+relevance+'\n\n**Potential downstream evidence impact:** An extractor preparing a systematic review or meta-analysis could copy '+impacts[n-1]+'. If human review confirms a reporting defect, documenting its definition or correction could improve extraction consistency. No actual propagation, conclusion change or serious harm is established.\n\n**Human verification steps:**\n\n'+steps+'\n\n**Human adjudication fields:**\n\n- **Validity:** __\n- **Importance:** __\n- **Action:** __\n- **Initials:** __\n- **Notes:** __\n');
}
if(cards.length!==27)throw Error('Card count '+cards.length);
const output=cards.join('\n');
const parsed=output.split(/(?=^## C\d{3} — )/m).filter(x=>/^## C/.test(x));
const ids=new Set();let links=0;
for(const block of parsed){
 const id=block.match(/^## (C\d{3})/)[1];if(ids.has(id))throw Error('Duplicate '+id);ids.add(id);
 for(const label of required){if(block.split('**'+label+':**').length!==2)throw Error(id+' label '+label);}
 for(const label of ['Validity','Importance','Action','Initials','Notes'])if(!block.includes('- **'+label+':** __\n'))throw Error(id+' blank '+label);
 const c=classifications.find(x=>x.id===id);
 for(const [label,key]of Object.entries(fieldMap)){const actual=block.match(new RegExp('^\\*\\*'+label+':\\*\\* (.*)$','m'))[1];if(actual!==c[key])throw Error(id+' classification '+label);}
 const row=ledger.split('\n').find(x=>x.startsWith('| '+id+' |'));const cells=row.split('|').slice(1,-1).map(x=>x.trim());
 for(const [i,key]of ['id','category','type','all','roles','domain','state','suggestion'].entries())if(cells[i]!==c[key])throw Error(id+' ledger '+key);
 for(const m of block.matchAll(/\]\(<([^>]+)>\)/g)){const target=m[1], file=target.split('#')[0];if(!/#page=\d+$/.test(target))throw Error(id+' PDF anchor');if(!fs.existsSync(path.resolve(base+'report_parts',file)))throw Error(id+' link '+target);links++;}
}
fs.writeFileSync(base+'report_parts/cards_001.md',output);
console.log(JSON.stringify({cards:cards.length,uniqueIDs:ids.size,requiredLabels:required.length,classificationEquality:'PASS',humanPlaceholders:'PASS',resolvingPDFLinks:links,output:base+'report_parts/cards_001.md'}));
