const fs = require('fs');
const path = require('path');
const root = '.ai_paper_validation/review_1_6/';
const handoff = fs.readFileSync(root+'handoffs/report_004.md','utf8');
const ledger = fs.readFileSync(root+'candidate_ledger.md','utf8');
const blocks = handoff.split(/(?=^## C\d{3} — )/m).filter(x=>/^## C/.test(x));
const classLabels = ['Category','Relationship type','All relationships','Compared document roles','Review domain','Evidence state','Suggested review disposition'];
const required = ['Candidate statement',...classLabels,'Classification rationale','Classification ambiguity','Exact source locations','Source evidence','Reported-versus-comparator','Reasoning procedure','Calculation','Alternative source-grounded interpretations','Mechanical evidence recheck','Quality-control relevance','Potential downstream evidence impact','Human verification steps','Human adjudication fields'];
const out=[];
for(const b of blocks){
 const id=b.match(/^## (C\d{3})/)[1], n=Number(id.slice(1));
 const fields={};
 const matches=[...b.matchAll(/^\*\*([^\n]+?):\*\*\s*/gm)];
 for(let i=0;i<matches.length;i++) fields[matches[i][1]]=b.slice(matches[i].index+matches[i][0].length,i+1<matches.length?matches[i+1].index:b.length).split('\n### Mechanical')[0].trim();
 const get=k=>fields[k]||'';
 const row=ledger.split('\n').find(x=>x.startsWith('| '+id+' |')).split('|').slice(1,-1).map(x=>x.trim());
 const recheck=b.match(/- Determining fact\/state: ([\s\S]*?)\n- Missing definition and human question: ([\s\S]*?)(?=\n\n\*\*Audited reporting guidance)/);
 if(!recheck)throw Error('Missing recheck '+id);
 let title=b.split('\n')[0], statement=get('Candidate statement');
 const c={};
 classLabels.forEach((label,i)=>c[label]=row[i+1]);
 c['Classification rationale']=get('Classification rationale');
 c['Classification ambiguity']=get('Classification ambiguity');
 c['Exact source locations']=get('Compared locations and document roles');
 c['Source evidence']=get('Printed inputs')||get('Printed evidence');
 c['Reported-versus-comparator']=c['Source evidence']+' '+(get('Registered comparison scope')||'');
 c['Reasoning procedure']=(get('Direct observation versus inference')||get('Direct observation versus diagnostic'))+' '+recheck[2];
 c['Calculation']=(get('Reproducible rule and calculation')||get('Rule and calculation'))+' '+(get('Tolerance')?'Display tolerance: '+get('Tolerance'):'Logical signs, labels and printed inequalities are compared without digitizing exact graphical coordinates.');
 c['Alternative source-grounded interpretations']=get('Alternatives and missing definition')||get('Alternatives')||get('Alternative source-grounded interpretations');
 c['Mechanical evidence recheck']=recheck[1]+' Necessary missing inputs: '+recheck[2]+` The classification codes above agree with the source-confirmed recheck. The suggested review disposition (${c['Suggested review disposition']}) is a mechanical pre-fill for human review and is not an adjudication.`;
 c['Quality-control relevance']=get('Quality-control relevance');
 c['Human verification steps']='Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: '+(get('Exact human question')||get('Named uncertainty and human question')||recheck[2])+' Record the human assessment in the five blank fields below.';
 c['Potential downstream evidence impact']='If this question is confirmed as a reporting defect, an evidence extractor could copy the '+(n===82?'thoracic VAS SD into a quantitative synthesis':n===83?'count-burden summary with the wrong statistic or population':n<=87?'follow-up duration or time-dependent risk denominator into an endpoint summary':n<=98?'modeled sensitivity estimate as a crude arm risk ratio':n===99?'retained enrollment target into a plan summary':n===103?'effect-measure label into an extraction of the original plan':'stopping-boundary sign or region into a monitoring-plan summary')+'. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.';
 if(n===82){statement='Conditional on zero-origin 0–10 cm scores on the same postoperative VAS, the low-PEEP Day 2 thoracic mean/SD tuple exceeds the bounded-support moment limit even after rounding. A 10 cm line length alone does not establish those endpoints or the postoperative scale identity.';}
 if(n===83){statement='The high-arm count summary 0.35 differs from the nearest-rounded mean 353/989 = 0.36 only if the unlabeled first statistic is the mean of the same twelve component indicators in the displayed population. The summary statistic, aggregation and realized denominator are not supplied; randomized denominators provide a coherent alternative.';c['Exact source locations']+=' Corroborative PLAN count-definition context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity-analysis paragraph.';}
 if(n>=84&&n<=87){
  const pg=n-46, fig=n-76, endpoint=['PPC','severe PPC','extrapulmonary complications','mortality'][n-84], hi=[785,785,828,985][n-84],lo=[756,756,845,986][n-84],sum=hi+lo;
  c['Exact source locations']=`[joi190055supp4_prod_16092.pdf — physical PDF p. ${pg}](../../../joi190055supp4_prod_16092.pdf#page=${pg}), eFigure ${fig} ${endpoint}, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.`;
  c['Source evidence']=`The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are ${hi}/${lo} (total ${sum}).`;
  c['Reported-versus-comparator']=`The day-5 risk total ${sum} is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.`;
  c['Reasoning procedure']='The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.';
  c['Calculation']=`1976 / 2 = 988; ${hi} + ${lo} = ${sum}; ${sum} − 988 = ${sum-988}. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.`;
  c['Alternative source-grounded interpretations']='Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.';
  c['Human verification steps']=`Open eFigure ${fig} on physical PDF p. ${pg}; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.`;
 }
 if(n>=88&&n<=98){
  c['Exact source locations']+=' Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.';
  c['Source evidence']+=' The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.';
  c['Reported-versus-comparator']='Original registered comparison, retained as history: '+get('Printed inputs')+' The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.';
  c['Reasoning procedure']='The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.';
  c['Calculation']='Historical conditional crude diagnostic: '+get('Reproducible rule and calculation').replace('Under the displayed arm-specific risk definition','Under an explicitly crude arm-risk definition')+' '+get('Tolerance')+' Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.';
  c['Alternative source-grounded interpretations']='A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.';
  c['Quality-control relevance']='This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.';
  c['Human verification steps']='Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask '+recheck[2].replace(/^.*?Human question: /,'')+' Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.';
 }
 if(n===99){
  title='## C099 — Revised PLAN target versus retained procedural total';
  statement='The same protocol version explicitly revises the total to 2013 but retains a future-tense procedure statement of 748. The initial 748 is historical in section 6.4; whether section 7.2 intentionally retains historical wording requires human confirmation.';
  c['Exact source locations']='PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 10, printed p. 9](../../../joi190055supp1_prod_16092.pdf#page=10), current recruitment target; [physical PDF p. 11, printed p. 10](../../../joi190055supp1_prod_16092.pdf#page=11), version 2.6 section 6.4; [physical PDF p. 12, printed p. 11](../../../joi190055supp1_prod_16092.pdf#page=12), section 7.2. Corroborative PLAN [joi190055supp2_prod_16092.pdf — physical PDF p. 2](../../../joi190055supp2_prod_16092.pdf#page=2), revised sample target.';
  c['Source evidence']='The current recruitment statement gives 2013. Section 6.4 explicitly distinguishes initial 748 from revised total 2013. Section 7.2 states, “In total,748 patients will be included.” The amendment corroborates the revised total.';
  c['Reported-versus-comparator']='Section 7.2 future-tense total 748 versus the same version’s explicitly revised total 2013; the historical 748 in section 6.4 is not itself conflicting.';
  c['Reasoning procedure']='Directly compare the same-version current-total statements and their historical qualifiers. The rule is identity of the intended current planned enrollment total, conditional on section 7.2 remaining an operative procedure. No REPORT conflict or actual enrollment error is inferred.';
  c['Calculation']='2013 − 748 = 1265 participants. Both printed totals are exact integers; no rounding tolerance applies. The subtraction quantifies the displayed difference and does not establish the historical intent of section 7.2.';
  c['Alternative source-grounded interpretations']='Section 7.2 may be an unupdated procedural paragraph or an intentionally retained historical passage without an explicit historical label. The intended status of that future-tense paragraph is missing. The amendment supplies the revision; this record does not accuse an unlogged amendment.';
  c['Quality-control relevance']='A plan summary requires a distinguishable current sample target and historical procedure wording.';
  c['Human verification steps']='Read version 2.6 sections 6.4 and 7.2 alongside the current recruitment statement and amendment. Ask whether section 7.2 was intended to prescribe 748 or retain a historical paragraph, and which current target was intended. Record the answer below; do not change an actual enrolled total based on this wording comparison.';
 }
 if(n>=100&&n!==103){
  const look=n<=102?n-99:n-103, N=[956,1434,1912][look-1],isF=n<=102,bound=isF?[.225,.929,2.012][look-1]:[2.75,2.432,2.012][look-1];
  title=`## ${id} — Conditional ${isF?'futility-region':'efficacy-sign'} comparison at look ${look}`;
  statement=`Under a common signed-Z definition, the look-${look} table ${isF?'inequality Z < '+bound+' differs from the central graphical futility set':'inequality Z ≥ '+bound+' has the opposite orientation to the negative graphical Efficacy region'}. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.`;
  c['Reported-versus-comparator']=`Look ${look}, N = ${N}: printed table ${isF?'futility Z < '+bound:'efficacy Z ≥ '+bound}, versus ${isF?'a central pink graphical Futility region between negative and positive inner boundaries':'a graphical Efficacy region below zero, with Harm above zero'}. The plot does not independently print exact boundary coordinates.`;
  c['Reasoning procedure']=get('Direct observation versus diagnostic')+' Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.';
  c['Calculation']=isF?`Witness Z = −4 satisfies −4 < ${bound}, but is outside the central pink graphical region at N = ${N}. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.`:`The table inequality Z ≥ +${bound} points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.`;
 }
 if(n===103){c['Exact source locations']+=' Planning probabilities for the illustration: PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 11, printed p. 10](../../../joi190055supp1_prod_16092.pdf#page=11), sample-size assumptions.';c['Calculation']=get('Rule and calculation')+' The probabilities are supplied planning assumptions, not observed trial rates. Arithmetic is exact at the supplied two-decimal inputs; 0.642857 is a rounded diagnostic. Logistic regression alone does not determine whether a postprocessed estimate is an OR or RR.';}
 c['Candidate statement']=statement;
 c['Human adjudication fields']='\n\n- **Validity:** __\n- **Importance:** __\n- **Action:** __\n- **Initials:** __\n- **Notes:** __';
 for(const label of required)if(!c[label]||!c[label].trim())throw Error(id+' missing '+label);
 const sourceNames={'DOC-001':'jama_bluth_2019_oi_190055_16092.pdf','DOC-002':'joi190055supp1_prod_16092.pdf','DOC-003':'joi190055supp2_prod_16092.pdf','DOC-004':'joi190055supp3_prod_16092.pdf','DOC-005':'joi190055supp4_prod_16092.pdf'};
 c['Exact source locations']=c['Exact source locations'].replace(/\[(DOC-00[1-5])([^\]]*)\]/g,(_,doc,rest)=>'['+sourceNames[doc]+rest+']');
 out.push(title+'\n\nPending Human Adjudication.\n\n'+required.map(label=>'**'+label+':**'+(c[label].startsWith('- ')?'\n\n':' ')+c[label]).join('\n\n'));
}
 const result=out.join('\n\n')+'\n';
fs.writeFileSync(root+'report_parts/cards_004.md',result);
if(out.length!==25)throw Error('Wrong count');
for(const b of result.split(/(?=^## C)/m).filter(x=>/^## C/.test(x))){
 const id=b.match(/^## (C\d{3})/)[1];
 for(const label of required)if(b.split('**'+label+':**').length!==2)throw Error(id+' label '+label);
 for(const label of ['Validity','Importance','Action','Initials','Notes'])if(!b.includes('- **'+label+':** __'))throw Error(id+' blank '+label);
 for(const match of b.matchAll(/\]\(([^)]+)\)/g)){const link=match[1].replace(/^<|>$/g,'');if(!fs.existsSync(path.resolve(root+'report_parts',link.split('#')[0])))throw Error(id+' link '+link);if(link.includes('.pdf')&&!/#page=\d+$/.test(link))throw Error(id+' pdf page');}
}
console.log('PASS: 25 cards; 21 required labels/card; 5 exact blanks/card; source links resolve.');
