import json,collections,pathlib
D=pathlib.Path('meta_report/consistency_reclassification_2026-09-04')
inputs=json.loads((D/'input_2018.json').read_text())
# These assignments are manual, after reading all 119 complete cards and targeted current-run records.
classes={
'jama.2017.21906':['S_W','S_W','S_W','P_R','S_C','P_R'],
'jama.2018.0156':['S_W']*5+['S_C','P_R','P_R'],
'jama.2018.0948':['P_R','P_P','P_P','P_P','P_B','P_P','P_B'],
'jama.2018.14280':['S_W']*21+['S_C','P_R'],
'jama.2018.14282':['S_W']*21+['S_C','S_W','S_W','S_W','P_P','P_P','P_P'],
'jama.2018.17075':['S_W','S_W','S_C','S_C','S_W','S_W','S_W','S_W'],
'jama.2018.18020':['S_W']*14,
'jama.2018.6496':['S_W','S_W','P_R','P_R'],
'jama.2018.8802':['S_W','P_R','S_W','S_W','S_W','S_W','S_C','S_W'],
'jama.2018.9128':['S_C']*8+['P_P','P_P','P_R','P_R','S_C'],
}
# Documents containing the focal within-document discrepancy, manually determined by content.
sw_supp={
'jama.2017.21906':{3},'jama.2018.0156':set(),'jama.2018.0948':set(),
'jama.2018.14280':{1,7,8,9,10},'jama.2018.14282':{19,20,21},
'jama.2018.17075':{5,6,7},'jama.2018.18020':{4,5,6,7},
'jama.2018.6496':set(),'jama.2018.8802':{3,4,5,6},'jama.2018.9128':set()}
subtypes={
'jama.2017.21906':['repeated_ci_endpoint','repeated_effect_estimate','comparator_label','subgroup_cutpoint_prespecification','composite_component_definition','subgroup_prespecification'],
'jama.2018.0156':['noninferiority_direction_word','count_vs_duration_unit','risk_difference_arithmetic','ci_scale_precision','proportion_and_contrast_direction','centre_count_unit','outcome_definition_amendment','composite_vs_reported_endpoint'],
'jama.2018.0948':['outcome_threshold_boundary','planning_unit_conversion','resuscitation_category_definition','preventability_threshold','planning_reference_period','planning_product_arithmetic','planning_reference_rates'],
'jama.2018.14280':['iqr_order']+['undisclosed_denominator']*9+['effect_measure_methods_vs_table']+['rr_vs_displayed_risks']*10+['iqr_vs_ci_label','enrollment_end_date'],
'jama.2018.14282':['count_percentage_rounding']*16+['repeated_ci_endpoint','denominator_communication']+['count_percentage_rounding']*3+['test_label','hr_orientation','hr_orientation','sample_size_sum','noninferiority_margin_sign','planned_intervention_label','planned_endpoint_horizon'],
'jama.2018.17075':['median_iqr_order','repeated_effect_sign','bleeding_effect_and_p_attachment','bleeding_effect_and_p_attachment','count_percentage_order','count_percentage_order','malformed_ci_string','sex_count_and_percentage'],
'jama.2018.18020':['sex_count_vs_percentage','score_scale_bound','contrast_direction','adverse_event_denominator','parameter_treatment_label','parameter_genotype_label','variance_treatment_label','genotype_symbol_typo','ci_p_compatibility','ci_p_compatibility','estimate_ci_p_compatibility','ci_p_compatibility','interval_order_and_containment','estimate_interval_containment'],
'jama.2018.6496':['ci_endpoint_order','linked_outcome_denominators','outcome_surveillance_window','duration_endpoint_definition'],
'jama.2018.8802':['count_percentage_arithmetic','eligibility_threshold','count_percentage_rounding','count_percentage_rounding','count_percentage_rounding','count_percentage_rounding','sampling_count_vs_total','ci_p_compatibility'],
'jama.2018.9128':['repeated_bmi_observation_count']*8+['planned_schedule_list_count','planned_schedule_list_count','planned_vs_reported_outcome_scale','planned_vs_reported_control_exposure','repeated_bmi_observation_count'],
}
# Exact deeper records consulted for each candidate; inventory establishes supplement document roles.
deep={
'jama.2017.21906':{1,2,3,4,5},'jama.2018.0156':{3,4,7,8},
'jama.2018.0948':{4},'jama.2018.14280':{11,23},
'jama.2018.14282':{18,25,26,27,28},'jama.2018.17075':{3,4},
'jama.2018.18020':{4,5,6,7,8},'jama.2018.6496':{1,2,3,4},
'jama.2018.8802':{2,7},'jama.2018.9128':{9,10,11,12},
}
ledger={ 'jama.2018.0948':set(range(1,8)), 'jama.2018.14282':set(range(17,29)) }
rows=[]
for r in inputs:
 p,n=r['package'],r['number']; c=classes[p][n-1]
 pref=f'2018/{p}/.ai_paper_validation/review_1_5_2/'
 paths=[pref+'source_inventory.md']
 if n in deep[p]:paths.append(pref+'verification/evidence_recheck.md')
 if n in ledger.get(p,set()):paths.append(pref+'candidate_ledger.md')
 role={'S_W':'The focal mismatch is within '+('one non-plan results supplement' if n in sw_supp[p] else 'the main article')+'.',
       'S_C':'The focal comparison is the main article versus a non-plan results supplement.',
       'P_R':'The reported article/results definition is compared substantively with the supplied protocol or SAP.',
       'P_P':'The focal discrepancy is internal to the protocol/SAP material, including plan-version passages in a bound bundle.',
       'P_B':'The focal discrepancy concerns historical/background quantitative evidence reproduced within the protocol, not the current trial reported result.'}[c]
 rows.append(dict(key=r['key'],primary=c,relations=[c],rationale=r['statement']+' '+role,evidence_paths=paths,ambiguity='',duplicate_of='',subtype=subtypes[p][n-1],evidence_state='recorded_candidate'))
by={r['key']:r for r in rows}
def edit(p,n,rationale=None,relations=None,ambiguity=None):
 r=by[f'2018::{p}::C{n:03}']
 if rationale:r['rationale']=rationale
 if relations:r['relations']=relations
 if ambiguity:r['ambiguity']=ambiguity
# Explicit relationship judgments for overlapping source cards.
edit('jama.2017.21906',2, 'Table 2 and Results narrative in the same main PDF report discharge beta-blocker RD 6.69 versus 6.63 and OR 1.48 versus 1.47 with identical intervals. Despite its original cross-document category, both discrepant occurrences are within the main article.')
edit('jama.2017.21906',4, 'The main article calls age strata <50, 50-69, and >=70 prespecified, whereas the supplied SAP specifies two groups split at 65; this is a reported-versus-prespecified subgroup definition discrepancy.',ambiguity='A later or separate prespecification could authorize the published cutpoints; no such dated record is supplied. The SAP age-65 gap is contextual, not a separate counted relationship.')
edit('jama.2017.21906',5, 'The main article and results-supplement eTable 5 define the medication composite using anticoagulant; eTable 6 in the same results supplement says heparin. The cross-file component mismatch and the eTable 5/eTable 6 within-file mismatch are both substantive.',relations=['S_C','S_W'],ambiguity='Mixed cross-file and within-supplement relationship. Heparin may exhaust the operative anticoagulant class; operational equivalence is unknown.')
edit('jama.2017.21906',6, 'Hospital type (government/nonprofit/private) is presented as prespecified in the main Figure 3 but absent from the supplied SAP site-level subgroup list. This compares reported prespecification with the plan, not main versus ordinary supplementary results.',ambiguity='An amended or separate plan may account for hospital type; the record establishes differing lists rather than intentional substitution.')
edit('jama.2018.0156',3, 'The main Table 2 PP-survival difference 0.1 does not round from its displayed 54/995 and 51/943 inputs, which yield 0.0189 percentage points. The SAP rounding sentence is a supporting convention, not a separate reported-versus-plan discrepancy.',ambiguity='The SAP explicitly rounds categorical percentages, not separately differences; an unreported estimator/denominator may explain the displayed 0.1.')
edit('jama.2018.0156',4, 'The main Table 2 interval -10 to 9.7 has unresolved scale/precision relative to the same row counts, effect scale, and P=.99. SAP CI wording corroborates the general method and does not itself conflict with reported analysis.',ambiguity='The diagnostic Wald interval is not an authoritative replacement; exact source CI construction is absent. Distinct from C003 point-estimate arithmetic although the same row is involved.')
edit('jama.2018.0156',6,ambiguity='Twenty EMS centres versus 21 investigator-centre rows may reflect different counting units; no centre-to-investigator crosswalk is supplied.')
edit('jama.2018.0156',7, 'The main article defines favorable outcome as CPC 1 or 2, while a supplied amended protocol also qualifies baseline-disabled survivors whose disability is unchanged. The potential outcome-definition difference is directly report versus amended plan.',ambiguity='An abbreviated article definition or no affected participants could reconcile the result; aggregate counts cannot establish actual coding or count changes.')
edit('jama.2018.0156',8, 'A supplied amended protocol defines technique failure as a composite including mortality/regurgitation/procedural failure, while the main Table 3 ETI failure row reports 21/996 without that composite definition. This is a conditional report-versus-plan endpoint/population mismatch.',ambiguity='The failure row may intentionally be procedural-only and uses actual-treatment safety data. The 27-versus-21 aggregate bound assumes participant-set alignment; recheck expressly says that assumption is not mechanically established. Additional source-derivative check: the final card and recheck call 54/1022 ETI deaths, but main native text explicitly labels 54/1022 day-28 survival. Thus the recorded 27-versus-21 mortality bound uses a mislabeled input and is not source-confirmed; the document-role endpoint-definition comparison is retained.')
edit('jama.2018.0948',1, 'The main article uses fluid >=60 mL/kg, while protocol Table 5 and the non-plan results-supplement eTable use >60 for the same SCD component. The article is discrepant with both the plan and ordinary results supplement.',relations=['P_R','S_C'],ambiguity='Mixed reported-versus-plan and submitted cross-file definition discrepancy; operative rule and any exact-boundary cases are unknown.')
edit('jama.2018.0948',2, 'The protocol appendix gives 0.9% for an approximately 18% reduction from 5.1 deaths/1000, whereas other passages in the same protocol give 0.9/1000 or 0.09%. The article repeats the coherent planning value and corroborates the internal plan unit-conversion defect; it is not counted as a separate plan-versus-report change.',ambiguity='Boundary decision: P_P only. Counting every transitive numerical disagreement would also involve the article, but the recorded issue is the internal planning percent/unit typo.')
edit('jama.2018.0948',4, 'Protocol p11 says >4 and immediately lists ratings 4, 5, 6; its own Table 7 says >=4. The main article and results supplement corroborate the inclusive list. The focal operator/list contradiction is internal to the protocol.',ambiguity='Boundary decision: P_P only; final reporting corroborates the internally stated >=4 rule. The actual rating-4 event classification is unknown.')
edit('jama.2018.14280',11, 'Main Methods broadly assigns mortality Cox HRs while main Table 2 labels ICU/hospital mortality RR. The SAP agrees with Table 2 and is corroboration of a Methods-versus-results wording discrepancy inside the main article.',ambiguity='The Methods sentence may intend only time-indexed 28/90-day mortality. No independent report-versus-plan departure is counted merely because SAP wording supports the table.')
for n in range(12,22):
 edit('jama.2018.14280',n,ambiguity='Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error.')
edit('jama.2018.14280',23, 'The main article gives August 20, 2017 as enrollment end, whereas the supplied SAP/update gives August 22, 2017. This is a main-report versus SAP factual date discrepancy, rather than an ordinary results-supplement discrepancy.',ambiguity='The SAP is an update after enrollment; clinical last-patient date versus administrative completion could explain the two days. P_R denotes document roles, not a proven prospective-plan violation.')
edit('jama.2018.14282',17, 'The abstract and Results of the same main PDF report upper CI endpoints -0.2 and -0.3/min for the matched six-hour respiratory-rate result. The original cross-document category is a within-main repetition discrepancy.')
edit('jama.2018.14282',18, 'The main paragraph explicitly begins In the overall population; 153/776=19.7% and 31/776=4.0% are correct, but the arm-attributed wording could be misread as within-arm risks. The retained candidate is within-main denominator communication, not an established numerical contradiction.',ambiguity='Communication-only candidate: arithmetic reproduces under the printed overall-population context. It is not an explicit failed evidence recheck, so evidence_state remains recorded_candidate; do not describe it as a confirmed inconsistency.')
edit('jama.2018.14282',20,ambiguity='Complementary to C021 and may share a forced-total percentage-production rule; separate printed count/percentage cell, so not marked an identical duplicate.')
edit('jama.2018.14282',21,ambiguity='Complementary to C020 and may share a forced-total percentage-production rule; separate printed count/percentage cell, so not marked an identical duplicate.')
for n in [23,24]:edit('jama.2018.14282',n,ambiguity='Figure reference group is not defined. Recheck rejects exact reciprocal agreement from all rounded values, while preserving near-reciprocal orientation compatible with hidden precision; this is not a wholly non-reproduced candidate.')
edit('jama.2018.14282',25, 'The main article states 779 patients with 389 in each of two arms, internally contradicting 389+389=778. The protocol/SAP 778 total corroborates that arithmetic; it is not counted as a separate implemented-versus-planned sample-size departure.',ambiguity='Boundary decision: S_W only; the plan comparison supports the internal total error. An unreported earlier unequal target remains possible.')
for n in [3,4]:edit('jama.2018.17075',n,relations=['S_C','S_W'],ambiguity='Mixed main-versus-results-supplement P-value mismatch and within-main RR/count incompatibility. Adjacent intra-/extracranial bleeding rows may have swapped effect tokens, but they are distinct outcomes and are not merged as duplicate IDs.')
edit('jama.2018.18020',4, 'Results-supplement eTable 4 prints placebo Any 2 (6%) against neighboring count-2 values of 7% and other pairs implying 30 participants. The main 21/30 statement supports that apparent denominator; the focal discrepancy is an internal eTable denominator/display issue, not a conflicting matched main result.',ambiguity='Conditional denominator: 31 treatment-set exposures, mentioned in the main article, could produce 6%; the table supplies neither analysis unit nor denominator.')
edit('jama.2018.18020',8, 'The main narrative attaches CLNC1 to the n=16 subgroup, while the same page gene definition and main figures use CLCN1. The results-supplement footnote corroborates the gene name, so the focal typo is within the main article.',ambiguity='Boundary decision: S_W only; the supplementary gene definition is corroborating context rather than a separate mismatched reported result.')
edit('jama.2018.6496',1, 'The main Table 3 CI is printed 4 to -1, a reversed order inside one table. The supplement explicitly recalculates inference for physician clustering and therefore is distinct-model context, not a same-analysis cross-file mismatch.',ambiguity='The clustered -1 to 4 interval cannot establish the intended unclustered endpoints.')
edit('jama.2018.6496',2, 'Main Tables 3 and 5 use ETT+stylet denominators 366 and 364 for linked composite/hypoxemia outcomes. Protocol definitions explain the relationship and even support outcome-specific missingness; there is no independent inconsistency with the protocol.',ambiguity='Known first-attempt failures may be classifiable as composite failures without a valid hypoxemia waveform, allowing different denominators. The discrepancy remains conditional and within the main article.')
for n in [3,4]:edit('jama.2018.6496',n,ambiguity='The planned cuff-inflation and reported blade-removal events may have been harmonized or intentionally changed, but no amendment/equivalence rule is supplied. The data form corroborates the reported operational event; it is not a separately counted protocol-versus-manual discrepancy.')
edit('jama.2018.8802',2, 'Main Table 2 and the sensitivity-results eTable use LDL >100; the protocol formal definition and results-supplement eTable 1 use >=100. The target is eligibility as formally defined versus attached to reported results, giving P_R; the main-versus-results-definition and within-supplement definition/label differences also substantively occur.',relations=['P_R','S_C','S_W'],ambiguity='Mixed planned/reported and submission-internal definition relationships. Labels may be abbreviations while the inclusive definition governed the denominators; participant-level LDL-at-100 data are absent.')
edit('jama.2018.8802',7, 'Main Table 1 reports 801 baseline-survey patients in 40 hospitals, while the ordinary results-supplement eAppendix says 20 patients per cluster were included, implying 800. Protocol 40-cluster statements corroborate the cluster count; the discrepant total versus per-cluster inclusion claim is main versus non-plan supplement.',ambiguity='Twenty may be a target, with one cluster enrolling 21; the printed retrospective inclusion claim lacks that qualification. No additional plan discrepancy is counted.')
for n in list(range(1,9))+[13]:
 edit('jama.2018.9128',n,relations=['S_C','S_W'],ambiguity='Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate.')
edit('jama.2018.9128',9, 'The final SAP says six timepoints but enumerates only five. The protocol schedule and article/eTable corroborate 24 months as the likely missing item; the focal contradiction is the SAP total versus its own list.',ambiguity='P_P only; printed 24-month results do not establish that the primary model used that occasion.')
edit('jama.2018.9128',10, 'The revised protocol says six points/T1-T6 but enumerates seven including 48 months, and elsewhere on the page says seven. The article/eTable 36-month horizon is contextual; no missing published 48-month outcome is counted as a report-versus-plan discrepancy.',ambiguity='A separately approved 48-month extension outside the six core visits could reconcile the wording; amendment chronology is absent.')
edit('jama.2018.9128',11, 'Original protocol BMI Percentile/BMI% wording differs from the final SAP and article/results raw BMI kg/m2 measure, and the original protocol itself supplies the raw-BMI formula. This is explicitly a planned-versus-reported outcome-scale comparison plus an internal/across-version plan-label inconsistency.',relations=['P_R','P_P'],ambiguity='Mixed plan/report and plan-internal relationships. The original label may have been shorthand/typo or the scale may have changed; the amendment summary mentions model changes but does not explain this label transition.')
edit('jama.2018.9128',12, 'Control exposure is 12x60 minutes in the original protocol, 7x45 in the revised protocol, and 6x30 in the article. The card expressly compares both plan versions and their relation to the reported intervention, so P_R and P_P apply.',relations=['P_R','P_P'],ambiguity='Mixed between-plan-version and report-versus-plan relationships. Successive amendments, ancillary components, baseline/48-month visits, and actual delivery could explain the differences; no mapping or delivery logs are supplied.')
edit('jama.2018.0948',5, 'The same historical Ontario four-hospital 1052 urgent ICU/PICU admissions count is called annual in protocol power-assumption text and two-year in the historical reference-data appendix. The conflicting quantity is a prior-data observation period reused as a planning input, so P_B distinguishes it from the current trial plan or report.',ambiguity='Historical evidence inside protocol. The p14 planning context uses this historical count, but the candidate does not independently challenge a prospective power calculation. Year-stratified data are absent.')
edit('jama.2018.0948',7, 'The protocol Sample Size Appendix reproduces Ontario 2007-8 historical data attributed to the Kotsakis 2009 collaborative report: 1052 admissions, denominators 7300/55963, and rates 14.5%/18 per 1000. The rates do not round from those historical integers. This is P_B background data inside the protocol, not current trial reported-versus-planned results.',ambiguity='Historical reference-table data can be planning inputs, but this candidate targets the pre-existing counts/rates themselves. The original external report was not obtained for new adjudication.')
for r in rows:
 if 'P_P' in r['relations']:r['plan_topology']='within_file'
 if r['primary']=='P_B':
  r['plan_topology']='within_file'
  r['evidence_paths'].append('2018/jama.2018.0948/.ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180015supp1_prod.txt')
by['2018::jama.2018.0156::C008']['evidence_paths'].append('2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_jabre_2018_oi_180004.txt')
by['2018::jama.2018.0156::C008']['validation_record_issue']='survival_count_mislabeled_as_deaths'
by['2018::jama.2018.0156::C008']['evidence_state']='record_input_error'
by['2018::jama.2018.0156::C008']['ambiguity'] += ' Exact main-abstract derivative wording: global survival at day 28 (55/1018 [5.4%] in the BMV group vs 54/1022 [5.3%] in the ETI group).'
assert len(rows)==119 and set(by)=={r['key'] for r in inputs}
for r in rows:
 assert all(pathlib.Path(p).exists() for p in r['evidence_paths'])
 assert r['primary']==r['relations'][0]
(D/'coded_2018.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(collections.Counter(r['primary'] for r in rows))
print('relations',collections.Counter(v for r in rows for v in r['relations']))
for p in classes:print(p,dict(collections.Counter(r['primary'] for r in rows if f'::{p}::' in r['key'])))
