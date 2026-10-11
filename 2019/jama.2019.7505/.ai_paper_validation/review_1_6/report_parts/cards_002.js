const fs = require('fs');
const path = require('path');
const base = '.ai_paper_validation/review_1_6';
const handoff = fs.readFileSync(`${base}/handoffs/report_002.md`, 'utf8');
const ledger = fs.readFileSync(`${base}/candidate_ledger.md`, 'utf8');
const classes = JSON.parse(fs.readFileSync(`${base}/verification/recheck_classification.json`, 'utf8'));
const fields = [['Category','category'],['Relationship type','type'],['All relationships','all'],['Compared document roles','roles'],['Review domain','domain'],['Evidence state','state'],['Suggested review disposition','suggestion'],['Classification rationale','rationale'],['Classification ambiguity','ambiguity']];
const required = ['Candidate statement', ...fields.map(x=>x[0]), 'Exact source locations','Source evidence','Reported-versus-comparator','Reasoning procedure','Calculation','Alternative source-grounded interpretations','Mechanical evidence recheck','Quality-control relevance','Potential downstream evidence impact','Human verification steps','Human adjudication fields'];
const pdf = 'jama_bluth_2019_oi_190055_16092.pdf';
const link = p => `[${pdf} — PDF p. ${p}](<../../../${pdf}#page=${p}>)`;
const fmt = n=>n.toFixed(9);
const round2 = n=>(Math.round(n*100)/100).toFixed(2);
const trunc2 = n=>(Math.trunc(n*100)/100).toFixed(2);
const blocks = handoff.split(/(?=^## C\d{3} — )/m).filter(x=>/^## C\d{3}/.test(x));
const output = [];
for (const block of blocks) {
  const [ , id, title ] = block.match(/^## (C\d{3}) — (.+)$/m);
  const cl = classes.find(x=>x.id===id);
  const table = ledger.split('\n').find(x=>x.startsWith(`| ${id} |`)).split('|').slice(1,-1).map(x=>x.trim());
  for (const [i,key] of ['category','type','all','roles','domain','state','suggestion'].entries()) if (table[i+1]!==cl[key]) throw new Error(`${id} classification ${key}`);
  const printed = block.match(/^- \*\*Printed inputs:\*\* (.+)$/m)[1];
  const provenance = block.match(/^\*\*Checker provenance:\*\* (.+)$/m)[1];
  const relationship = block.match(/^- \*\*Numeric relationships:\*\* (.+)$/m)[1] + (id==='C028'?' Additional matched narrative relationship: N022.':'');
  const sourceTuple = printed.split('Complete source-row components: ')[1];
  const outcome = title.split(':')[0];
  let statement, comparator, rule, calc, alternatives, recheck, steps, target;
  let locations = `REPORT ${link(9)}, Table 3, ${outcome} row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT ${link(10)}, Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT ${link(4)}, completed-analysis Statistical Analysis description.`;
  let evidence = `Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: ${sourceTuple} Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: ${provenance}. Numeric relationship: ${relationship}`;
  if (id==='C029'||id==='C033') {
    locations += ` REPORT ${link(8)}, Primary Outcome narrative, additionally matched ${outcome.toLowerCase()} counts and reported effect.`;
    evidence += ' The direct-source recheck additionally confirmed the matched Primary Outcome narrative on PDF p. 8.';
  }
  if (id==='C028') {
    statement = 'For mild respiratory failure, the printed −1.9 percentage-point difference differs slightly from the nearest one-decimal display of the exact High-minus-Low count-defined difference. The observation depends on the computation and display convention: subtracting the displayed percentages or truncating the exact difference reproduces −1.9.';
    locations = `REPORT ${link(8)}, Primary Outcome narrative, mild respiratory failure counts/percentages and signed difference; REPORT ${link(9)}, Table 3 Mild respiratory failure row and High PEEP 989/Low PEEP 987 headers; REPORT ${link(10)}, Table 3 footnote a on reference patients.`;
    comparator = 'Reported −1.9 percentage points (95% CI −5.1 to 1.2), repeated in the narrative, versus the derived count-defined High-minus-Low risk difference −1.952685211 percentage points, whose nearest one-decimal display is −2.0. The separate displayed-percentage comparator, 13.7−15.6, equals −1.9.';
    rule = 'Use the exact printed integers and reference populations to compute 100×(135/989−154/987). Under nearest one-decimal display, the absolute tolerance is 0.05 percentage point. This rule is conditional on a raw count-defined difference and nearest rounding; neither the exact difference estimator nor the display convention is fully specified. The 0.15-percentage-point allowance when comparing already rounded summaries does not change the exact integer calculation.';
    calc = '100×(135/989−154/987)=−1.952685211 percentage points; printed-minus-derived=+0.052685211 percentage point. The gap exceeds 0.05 by only 0.002685211. Nearest rounding gives −2.0; truncation toward zero gives −1.9; 13.7−15.6=−1.9.';
    alternatives = 'Displayed-percentage subtraction and truncation toward zero both reconcile the printed −1.9. A specifically defined fitted or adjusted difference or different analysis denominator could also differ from the crude calculation, but the package does not give a row-specific point formula/display rule. These are alternatives for human reconciliation, not identified production mechanisms or proposed corrections.';
    recheck = 'The direct-source recheck found the narrative and Table 3 cells, matched 135 (13.7%), 154 (15.6%), −1.9 (−5.1 to 1.2), and the reference populations, and reproduced the tiny conditional nearest-rounding gap. The named missing inputs are the raw-versus-model difference formula and rounding/truncation convention. State recorded_candidate records that comparison pending the definition; it does not establish an arithmetic error. The suggested retain disposition is a mechanical pre-fill for human review. Document roles and S_W classification were confirmed.';
    steps = `1. Open ${link(8)}, ${link(9)} and ${link(10)} and confirm the matched row, narrative and reference-patient rule.\n2. Recompute the exact count-defined difference, displayed-percentage subtraction and truncation alternatives.\n3. Determine whether −1.9 was obtained from exact risks, rounded summaries or a fitted estimand, and identify its actual display convention.\n4. Decide which calculation and value an extractor should use; record the human decision in the fields below.`;
    target = 'the mild respiratory failure difference −1.9 percentage points and its interpretation as an exact count-defined effect';
  } else if (id==='C049'||id==='C050') {
    const failure = id==='C049';
    const n = failure?7:2;
    const label = failure?'Failure':'Loss';
    const display = failure?22.5:6.4;
    const exact = 100*n/31;
    statement = `For the nested kidney ${label.toLowerCase()} category, the High PEEP cell ${n}/31 (${display}%) does not match nearest one-decimal rounding of its explicit quotient. Truncation reproduces the printed percentage, so this is a conditional display-rule question.`;
    locations = `REPORT ${link(9)}, Table 3 Acute kidney failure subcategory ${label}, explicit High PEEP ${n}/31 (${display}%) cell compared with its own numerator/denominator; REPORT ${link(10)}, footnotes f/g defining No./total No. and kidney stage categories.`;
    evidence = `Direct printed nested row: ${label}; High PEEP ${n}/31 (${display}%); Low PEEP ${failure?'5/32 (15.6%)':'2/32 (6.2%)'}. No separate risk ratio or absolute difference is printed for this subcategory; the class comparison P .97 is shared by the kidney-stage block. The denominator here is explicitly 31 for High PEEP and 32 for Low PEEP, not the randomized reference population. Current checker provenance: ${provenance}. Numeric relationship: ${relationship}`;
    comparator = `Reported High PEEP ${display}% versus 100×${n}/31=${fmt(exact)}%, nearest one-decimal ${(Math.round(exact*10)/10).toFixed(1)}%. The signed printed-minus-exact gap is ${fmt(display-exact)} percentage point.`;
    rule = `Divide the explicit nested numerator ${n} by its explicit denominator 31 and multiply by 100. Nearest one-decimal rounding permits 0.05 percentage point at a tie; the observed non-tie gap exceeds that bound. Applicability is conditional on nearest rounding. No requirement that rounded subcategory percentages sum exactly to 100 is imposed.`;
    calc = `100×${n}/31=${fmt(exact)}%; nearest ${(Math.round(exact*10)/10).toFixed(1)}%; truncation ${(Math.trunc(exact*10)/10).toFixed(1)}%; printed ${display}%; absolute gap ${fmt(exact-display)} percentage point, exceeding 0.05 by ${fmt(exact-display-0.05)}. ${failure?'The nearest-rounding interval for 22.5% is [22.45%,22.55%), excluding the exact quotient.':'The nearest-rounding interval for 6.4% is [6.35%,6.45%), excluding the exact quotient by only 0.001612903 percentage point. The Low PEEP 2/32=6.25% permits tie conventions displaying 6.2%; it is not an additional contradiction.'}`;
    alternatives = `Truncation of the explicit ${n}/31 quotient gives the printed ${display}% and coherently reconciles the display. A differently defined denominator or a transcribed cell would require supporting information; the supplied row already specifies 31 and gives no replacement denominator. The actual display rule is missing, so no percentage correction is assigned.`;
    recheck = `The direct-source recheck matched the ${label} cell, explicit ${n}/31 fraction, printed ${display}% and location, and reproduced the registered nearest-rounding comparison. The quotient inputs are available; the missing input is the calculation/display convention. State recorded_candidate retains that conditional question, with suggested retain disposition as a mechanical pre-fill for human review. The roles are REPORT/REPORT within Table 3; classification S_W was confirmed.`;
    steps = `1. Open ${link(9)} and ${link(10)} and confirm the ${label} row and its explicit nested denominator 31.\n2. Calculate 100×${n}/31 and compare nearest rounding with truncation.\n3. Establish whether ${display}% was deliberately truncated or arose from a different documented denominator/display procedure.\n4. Choose the documented interpretation for extraction and complete the human adjudication fields.`;
    target = `the kidney ${label.toLowerCase()} category percentage ${display}% or the explicit ${n}/31 denominator`;
  } else {
    const inp = printed.match(/^H (\d+)\/989; L (\d+)\/987; printed RR([\d.]+)\((.+)\)\./);
    if (!inp) throw new Error(`Inputs ${id}`);
    const h = +inp[1], l = +inp[2], displayed = inp[3], point = +displayed;
    const rr = l ? (h/989)/(l/987) : null;
    const q = (h/(h+l))/((989-h)/(1976-h-l));
    const conditional = ['C037','C052','C053'].includes(id);
    statement = l===0 ? `For ${outcome.toLowerCase()}, Table 3 prints a finite risk ratio ${displayed} although the printed Low PEEP event risk is zero. The crude High/Low event-risk quotient has no finite value; interpreting the reported estimate requires its point formula, outcome/reference orientation and zero-cell or fitted-estimator rule.` : conditional ? `For ${outcome.toLowerCase()}, the printed risk ratio ${displayed} differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces ${displayed}. This remains a conditional display/definition question.` : `For ${outcome.toLowerCase()}, the printed risk ratio ${displayed} does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention.`;
    comparator = l===0 ? `Reported risk ratio ${displayed} (95% CI ${inp[4]}) versus (1/989)/(0/987), which has no finite crude event-risk value because its denominator risk is zero. A finite fitted or corrected estimate requires an additional stated procedure.` : `Reported risk ratio ${displayed} (95% CI ${inp[4]}) versus the derived clinical event-risk ratio (${h}/989)/(${l}/987)=${fmt(rr)}, nearest display ${round2(rr)}. Printed-minus-derived=${fmt(point-rr)}; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.`;
    rule = `Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.`;
    calc = l===0 ? `High event risk=1/989; Low event risk=0/987=0; their quotient is undefined as a finite number (unbounded in an extended ratio interpretation). No rounding tolerance can turn this crude quotient into 2.00. Diagnostic q=[1/(1+0)]/[(989−1)/(1976−1−0)]=${fmt(q)}, nearest ${round2(q)}, truncation ${trunc2(q)}.` : `(${h}/989)/(${l}/987)=${fmt(rr)}; nearest ${round2(rr)}; printed ${displayed}; signed gap ${fmt(point-rr)}. Reverse-conditioning diagnostic q=[${h}/(${h}+${l})]/[(${989-h})/(${1976-h-l})]=${fmt(q)}; nearest ${round2(q)}, truncation ${trunc2(q)}.${conditional?' Truncating the clinical ratio 0.997977755 itself gives 0.99.':''}`;
    alternatives = `${conditional?'Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. ':''}The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. ${id==='C040'?'Here q=0.498987854 nearest-rounds to 0.50 and truncates to 0.49. ':id==='C054'?'Here q=1.998987854 nearest-rounds to 2.00 and truncates to 1.99. ':''}A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. ${l===0?'A continuity or fitted zero-cell procedure could provide a finite estimate but its exact rule and variance method are not supplied. ':''}The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.`;
    recheck = `The direct-source recheck found this Table 3 row, matched High PEEP ${h}, Low PEEP ${l}, reference patients 989/987, risk ratio ${displayed} (${inp[4]}) and the method/footnote locations. It reproduced the registered ${l===0?'nonfinite crude quotient versus finite reported-point':'conditional nearest-rounding point-identity'} comparison. ${conditional?'It also confirmed that clinical-ratio truncation reconciles the printed point. ':''}Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions${l===0?', together with the zero-cell and variance procedures':''}. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.`;
    steps = `1. Open ${link(9)}, ${link(10)} and ${link(4)}; confirm the named ${outcome} row, reference-patient rule and RR/CI versus χ² procedures.\n2. Recalculate (${h}/989)/(${l}/987)${l===0?' and identify the zero-denominator issue':', applying the stated 0.005 nearest-rounding tolerance'}; compare the diagnostic q only as a different conditioning.\n3. Ask which exact event/reference orientation, population denominator, point formula${l===0?', zero-cell rule, variance method':''}, fitted adjustment and display convention produced ${displayed}. ${conditional?'Check specifically whether the clinical ratio was truncated to 0.99. ':''}Resolve those definitions before interpreting either derived comparator as a correction.\n4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.`;
    target = `the ${outcome.toLowerCase()} risk ratio ${displayed}, its interval and its treatment-versus-event interpretation`;
  }
  const labels = [];
  const put = (label,value)=>labels.push(`**${label}:**${label==='Human verification steps'?'\n\n':' '}${value}`);
  put('Candidate statement',statement+' Status: Pending Human Adjudication.');
  for (const [label,key] of fields) put(label,cl[key]);
  put('Exact source locations',locations);
  put('Source evidence',evidence);
  put('Reported-versus-comparator',comparator);
  put('Reasoning procedure',rule);
  put('Calculation',calc);
  put('Alternative source-grounded interpretations',alternatives);
  put('Mechanical evidence recheck',recheck);
  put('Quality-control relevance',`Clarifying ${target} supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.`);
  put('Potential downstream evidence impact',`A systematic-review or meta-analysis extractor could copy ${target}. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.`);
  put('Human verification steps',steps);
  labels.push('**Human adjudication fields:**\n\n- **Validity:** __\n- **Importance:** __\n- **Action:** __\n- **Initials:** __\n- **Notes:** __');
  output.push(`## ${id} — ${title}\n\n${labels.join('\n\n')}\n`);
}
const result = output.join('\n');
const dest = `${base}/report_parts/cards_002.md`;
fs.writeFileSync(dest,result);
const cards = result.split(/(?=^## C\d{3} — )/m).filter(x=>/^## C\d{3}/.test(x));
if (cards.length!==27) throw new Error('card count');
for (const [i,c] of cards.entries()) {
  const id = 'C'+String(i+28).padStart(3,'0');
  if (!c.startsWith(`## ${id} —`)) throw new Error('ID order');
  for (const label of required) if (c.split(`**${label}:**`).length!==2) throw new Error(`${id} label ${label}`);
  for (const label of ['Validity','Importance','Action','Initials','Notes']) if (!c.includes(`- **${label}:** __\n`)) throw new Error(`${id} blank ${label}`);
  if (!c.includes('**Human adjudication fields:**\n\n- ')) throw new Error('list separation');
  const cl = classes.find(x=>x.id===id);
  for (const [label,key] of fields) if (!c.includes(`**${label}:** ${cl[key]}\n`)) throw new Error(`${id} class equality ${label}`);
}
for (const m of result.matchAll(/\]\(<([^>]+)>\)/g)) {
  if (!m[1].match(/\.pdf#page=\d+$/)) throw new Error(`page fragment ${m[1]}`);
  if (!fs.existsSync(path.resolve(path.dirname(dest),m[1].split('#')[0]))) throw new Error(`broken link ${m[1]}`);
}
console.log(JSON.stringify({cards:cards.length,first:'C028',last:'C054',requiredLabels:required.length,humanBlanks:135,classification:'MATCH',links:'RESOLVE',output:dest,bytes:Buffer.byteLength(result),issues:[]}));
