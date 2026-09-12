import json
from pathlib import Path
from collections import Counter,defaultdict
root=Path('meta_report/consistency_reclassification_2026-09-04')
inputs=json.loads((root/'input_2024.json').read_text())
codes={}
def add(pkg, lines):
 for line in lines.strip().split('\n'):
  n,rel,sub,why,*amb=line.split('|')
  codes[f'2024::jama.2024.{pkg}::C{int(n):03d}']={'relations':rel.split(','),'subtype':sub,'rationale':why,'ambiguity':amb[0] if amb else ''}
add('0318','''
1|S_W|flow_total|The 305 parent and 193+122=315 child allocation boxes disagree inside main Figure 1.|Population identity of the branch counts is conditional; no plan comparator.
2|S_W|timepoint_label|Year-12 headings and year-7 footnote definitions conflict within results-supplement eTable 2. The main article pointer corroborates the heading rather than supplying an additional targeted discrepancy.|The table may intentionally mix visits without adequate labels; classified by its internal heading/footnote relationship.
3|S_C|p_value_repeat|Main abstract/Results give P=.002 but matched results-supplement eTable 2 gives P<.001 for the same displayed HbA1c estimate and interval.|Timepoint ambiguity in C002 leaves exact analysis identity conditional; this is a separate P-value comparison.
4|S_W|threshold_operator|Main narrative says HbA1c<=6.5%, whereas its cited Table 2 says <6.5%. Supplementary GEE methods do not state the operator and are context only.
5|S_W|count_percentage|Main abstract gives four deaths as2.2%, whereas its own enrolled denominators and Table3 imply4/262=1.5%.|An unreported abstract risk set remains possible.
6|S_C|threshold_operator|Main reports BMI>=35 for its higher subgroup, but the linked non-plan eFigure6 repeatedly prints BMI>35.|Actual membership impact depends on boundary values and coding.
''')
add('0572','''
1|S_C|distribution_threshold_counts|Main Figure2 ITT mRS distributions reconstruct different threshold counts from results-supplement eTable2 despite matched168-per-arm labels.|Requires ordinary nearest-whole rounding and identical outcome derivation.
2|S_W|effect_measure_label|Main narrative and tables expand aRR as absolute risk reduction while their own interpretation explicitly says rate ratio and uses null1, alongside separate additive aRD. SAP relative-risk methods and supplementary aRR/aRD rows corroborate this internal scale mismatch.|SAP citation is supporting model context, not a demonstrated report-versus-plan analytical discrepancy.
''')
add('11057','''
1|P_R,S_C|intervention_duration|Main describes6 pre-quit message weeks, whereas both the study protocol and distinct results supplement describe1 week for the same intervention/subgroup.|Mixed report-plan and main-results-supplement relationships; protocol context dated2021 and article2024 permit an unproven program-version change.
2|S_W|summary_statistic_label|Results-supplement eTable4 labels cells median(IQR) but gives single dispersion values unlike its own endpoint-pair convention. Main Table1 supports the format convention but concerns different groupings.|Scalar IQR widths remain possible; main comparator is corroborative, not a matched-result numerical disagreement.
3|S_W|method_abbreviation|Within the results supplement, the defined IPRW method and matching eTable5 result are called IPWR once in eAppendixC. Main methods corroborate the standard abbreviation.|The substantive mismatch is the undefined transposition against the same supplement's definition and repeated result.
''')
add('12829','''
1|S_W|count_percentage|Main Table1 gives77 females of249 as30.1% instead of the count-derived30.9%.
2|S_W|rounding|Main Table1 and results-supplement TableS1 identically repeat215/249 as86.4%; their agreement is not a cross-file inconsistency. Each is an internal rounding candidate.|86.3% follows ordinary nearest rounding; an unspecified display convention may explain the difference.
3|S_W|denominator_header|Results-supplement TableS4 header249 differs from footnoted procedure-applicable241, which reproduces the percentages.|The explicit241 footnote may fully resolve the header context; retained candidate is not established bad arithmetic.
4|S_W|count_percentage|Results-supplement TableS6 gives9(3.9) under249;9/249 rounds3.6%. This percentage/header issue is separate from C016's9-versus11 event-count comparison.|Unlabelled PPS denominator233 could explain3.9%; it is diagnostic only.
5|S_W|denominator_population|Within results-supplement TableS7, headers233/238 total471 while site totals sum501 and cell percentages imply other denominators. Main Figure1 provides contextual population totals.|Main flow context is corroborative; no specific contradictory main result is the target.
6|S_W|denominator_population|Results-supplement TableS8 is labelled PPS but headers249/252 conflict with its percentages and same-supplement TableS10 PPS totals233/238. Main Figure1 corroborates those PPS totals.|Per-protocol denotes an analysis set, not a protocol document; main population totals corroborate the internal supplement mismatch.
7|S_W|denominator_population|ATS TableS9 headers249/252 conflict with percentages reproduced by same-supplement TableS10 ATS totals247/254.|Separate from C014's cell percentage, which fails even under the ATS denominator.
8|S_W|eligibility_distribution|Main eligibility text specifies70%-99% stenosis while its Table1 includes four participants in60%-69% or100% categories.|Measurement time/reader identity is unresolved; mention of possible protocol deviations does not make this a protocol-document comparison.
9|P_R,S_C|visit_window|Non-plan study-design graphic says30±3days, whereas main schedule and supplied protocol schedule say30±7days for the matched visit.|Mixed results-supplement versus plan and main-versus-supplement discrepancy; a tighter operational contact window is possible but undefined.
10|P_P|eligibility_window|Within ProtocolV2.0, synopsis says ischemic stroke21-90days and body criterion says14-90days.|Same-version discrepancy; possible stale synopsis or unmarked amendment, not report-versus-plan.
11|S_W|rounding|Results-supplement TableS3 gives234/249 as93.9% while ordinary nearest rounding gives94.0%.|Truncation could explain the display; evaluated denominator is not supplied.
12|S_W|timeline_ordinal|Non-plan FigureS1 repeats2nd meeting for three distinct dates within its own chronology.|A repeated review-cycle convention is possible but unstated.
13|P_P|visit_sequence|The same protocol bundle repeats visit9 and11 in a six-token sentence in bothV2.0 andV2.3, against its four-visit8-11 schedule.|The sentence may specify face-to-face subset9/11 rather than six successive visits; two versioned repetitions remain one retained candidate.
14|S_W|rounding|Results-supplement TableS9 gives8(3.3), but both displayed249 and same-supplement ATS247 denominators produce3.2%.|Distinct from C007: changing the ATS header alone does not resolve this cell.
15|S_W|flow_reason_category|Main narrative attributes all11 exclusions to consent withdrawal; its Figure1 assigns10 to withdrawal and1 to erroneous randomization.|Original cross-document category actually describes two locations in one article; dual reason coding remains possible.
16|S_C|event_count_repeat|Main primary endpoint narrative/Table2 giveBA11 events, whereas matched non-plan TableS6 prints9 under the same249 header and endpoint wording.|Different from C004's arithmetic defect; unknown endpoint/population mapping could explain the count difference.
17|S_W|point_interval_containment|Main Table2 incidence difference-0.4 lies outside its printed95%CI[-2.4,-1.7].|The interval construction or a mismatched estimand is not supplied.
''')
add('19585','''
1|S_W|flow_hierarchy|The retained candidate concerns nested counts within main Figure1; recheck explicitly finds7+4+2=13 and top-level sum58, reconciling the displayed total.|NOT REPRODUCED: prior71-versus58 sum double-counted the13 parent; stable ID retained only for production-layout confirmation.
2|S_C|aggregate_percentage|Main rejected-statement percentage6.4% conflicts with142/1350=10.5% from the supplied non-plan eTable3 site counts.|A different unreported rejection population/definition remains possible.
3|S_W|effect_measure_label|Within one results supplement, eTable10 labels modeled effects Difference while eMethods expressly defines the relevant analyses as logistic odds ratios.|Difference might be an undefined generic heading; numerical odds-ratio error is not established.
''')
add('2302','''
1|P_R,P_P,S_C|endpoint_threshold|Main Table2 and SAP define>=1 SAE, while matched results eTable2 and protocol use>1. This explicitly spans report-plan, protocol-SAP, and main-results-supplement definitions.|Mixed relations; identical44/159 and27/149 counts do not establish which threshold was implemented.
2|P_P|planning_medians|Protocol planning medians18/15 conflict with its own8/5 medians and the SAP's8/5; all compared numbers are planning assumptions.|SAP explicitly calls18/15 incorrect and identifies8/5 as intended. This is disclosed plan correction, not observed-result disagreement or an undisclosed deviation.
3|P_R|prior_specification|Main common categorical/count intervention prior range0.33-3.0 differs from SAP categorical0.2-4 and count0.33-3.3 descriptions.|Final outcome-specific code/amendment is missing; SAP's approximate log-scale quantiles are contextual, not a separate coded plan-internal candidate.
4|P_R,P_P|subgroup_threshold|Actual Figure3 upperGA group>=28 differs from SAP subgroup/stratification>28 wording; the SAP itself also uses>=28 for its covariate.|Mixed report-plan and internal-SAP boundary wording; covariate context supports possible shorthand but final coding is unknown.
5|P_R,P_P|outcome_time_origin|Article/SAP use randomization as primarySAE timezero whereas protocol definitions use enrollment; verifier also records both terms inside protocol.|Mixed report-plan and internal/between-plan terminology; enrollment and randomization may be operationally simultaneous but are not defined as equal.
''')
add('23898','''
1|P_R|outcome_time_origin|Main primaryGI-3 labels72hours after surgery/operation, whereas SAP explicitly says72hours after start of operation.|This is ambiguity of timezero, not proven differing derivation; article wording may be shorthand.
2|P_R|outcome_window|Main reports cumulative opioid consumption through24hours; protocol and SAP define the matched outcome through72hours.|A distinct final endpoint or amendment remains possible but no supplied final record resolves it.
3|P_R,S_W|outcome_window|Main Table3 reports readmissions within90days, whereas main Methods and protocol/SAP definitions including dummy-table heading specify30days.|Mixed report-plan and internal-article discrepancy; actual31/34 counts may be30-day counts under a90-day label or reflect a changed window.
4|P_R|subgroup_cutpoints|Reported eFigure lowERAS<5/10 places40% in low, unlike the protocol's example30%-60% middle band.|Protocol explicitly says e.g.; eFigure says definitions were not predefined. This is a candidate plan/report difference with disclosed exploratory categorization, not proof of protocol violation.
5|S_W|confidence_level_label|One results eFigure labels subgroup intervals99% in its legend and95% in its caption; SAP99% convention supports the legend only.|Do not count plan involvement merely because SAP corroborates one side of the internal figure-label mismatch.
6|S_W|narrative_inference|Main day5EQ-5D row givesP=.04 and95%CI excluding0 while its Results says no statistically significantEQ-5D difference. SAP confirms the nominal framework.|SAP is framework support, not a separately targeted plan/report deviation; overall versus timepoint narrative rule is absent.
7|P_R,S_C|subgroup_levels|Main Methods callsERAS high versus low, but SAP and reported eFigure identify high/moderate/low for the displayed interaction.|Mixed report-plan and main-results-supplement labels; article could use shorthand or describe an extreme-level contrast. Distinct from C004's numerical cutpoints.
''')
add('25786','''
1|S_W|count_percentage|Results-supplement eTable2 pairs4/743 with5.3%, whereas the printed fraction gives0.5%.
2|S_W|count_percentage|Results-supplement eTable2 pairs0/747 with1.1%, inconsistent with its own count/total format.
3|S_W|interval_repeat|Matched eTables4 and7 within the same results supplement print upper95% limits1.41 and1.39 forOR0.98. Main methods only provide model context.|Original cross-document category is within one non-plan PDF; precise model identity remains conditional.
4|S_C,S_W|percentage_repeat|Main Figure4 gives48/473(10.1) while results eTable7 gives48/473(9.2), also inconsistent with its own fraction.|Mixed cross-file repeated percentage and within-table arithmetic relationship.
5|S_C,S_W|rounding_repeat|Main Figure4 gives14/69(20.3) while results eTable7 gives14/69(20.2); the latter differs from ordinary nearest rounding.|Mixed cross-file and internal arithmetic; unspecified truncation could explain20.2.
6|S_C,S_W|flow_total|Results eTable10 gives55+67=122 against its ownN130, while main Figure1 gives59+71=130.|Mixed cross-file counts and within-table total; four Swiss-law consent omissions per arm offer a plausible but unlabelled restriction.
7|S_W|denominator_estimand|Results eTable10 pairs174/750 and165/758 with51%/49%, which instead partition339 cross-arm exclusions. Main Figure1 agrees with the counts.|Main is corroborative; the two unassigned cases are already explained by a footnote, so that two-person gap is not another discrepancy.
8|S_W|count_notation|Results eTable11 prints135//750 with a doubled separator despite its own single-slash count convention; numerical18.0% reconciles.|Notation defect remains observed even though arithmetic reconciles; not a negated candidate.
''')
add('4183','''
1|S_W|denominator_population|Main abstract phase2 allocations combine percentages based on191/157 and151/122, summing114%/115%; Figure2 supplies nonattender context.
2|S_W|count_total|Main baseline table gives105+145=250 within each n245 arm, and male145 does not yield57.1%.
3|S_W|flow_total|Main initial randomized491 parent does not equal245+245=490 branches; later exclusion pertains to analysis total.
4|S_W|flow_population_label|Main Results calls the same40+35 continuation-assigned patients attendees, whereas abstract/Figure2 call them nonattendees.
5|S_C,S_W|credible_interval_repeat|Conditional abstract interval6%-11% for increasedCNRT differs from2%-11% explicitly printed in main Results and results eTable4.|Mixed cross-file/internal repetitions if abstract parenthetical applies to both rescue strategies; it may apply only to switch. Related to C006 but a distinct contrast.
6|S_C,S_W|credible_interval_repeat|CNRT-switch interval is6%-11% in main abstract,2%-11% in main Results, and2%-10% in results eTable4.|Mixed cross-file and internal repetitions; separate switch contrast from C005.
7|S_C,S_W|contrast_sign_direction|Main switch-versus-continuationRD-3% differs from+3% in results eTable4, while main text calls continuation worse despite own0% switch versus3% stay values.|Mixed cross-file sign/reference mismatch and main internal narrative direction mismatch.
8|S_C|credible_interval_repeat|Main increased-vareniclineRD18% interval13%-24% differs from results eTable4 interval13%-23%.
9|S_C|credible_interval_repeat|Main phase1-abstainerRD6% interval-5%-16% differs from results eTable4 interval-4%-16%.
10|P_P|prior_parameter_identity|Within protocolFigure2,Beta(785,869) yields mean0.4746 and diagnostic95%quantiles0.4506-0.4987 rather than paired0.50(0.40-0.60).|Whether paired interval describes that beta distribution is not explicit; no reported-result comparator.
11|P_P|power_monotonicity|ProtocolTable3 power rises0.948 to0.980 as posterior threshold tightens0.80 to0.85, conflicting with nested detection on one simulation set.|Common simulation realizations are unconfirmed; independent MonteCarlo sets could explain the rise.
12|P_P|contrast_label|ProtocolTable3 repeatsVARvsNPL for third effect0.195 even though its own contrast definitions and0.399-0.204 matchVARvsNPL+.
13|S_W|count_percent_order|Results eTable3 raceOther cell4.9(2) reverses its n(%) order, with2/41=4.9%.
14|S_W|estimate_interval_repeat|Within results supplement,EOT+30CNRT-switch narrative1.0%(7.0%-1.3%) disagrees with eFigure2's5/51,10%(7%-13%), and has reversed/noncontaining bounds.
15|S_W|credible_interval_repeat|Within results supplement,EOT+30increasedCNRT narrative8%(5%-1.1%) disagrees with eFigure2's8%(5%-11%).
16|S_W|credible_interval_repeat|Within results supplement,CNRT-switchARD6%(3%-1.0%) narrative disagrees with eTable9's6%(3%-10%).|Different estimand from C014's arm-specific response cell, so not a duplicate.
17|S_W|credible_interval_repeat|Within results supplement,increased-varenicline narrative repeats8%(5%-1.1%) for its cell and twoARDs, while matched eFigure/eTables give8%(5%-11%).|Multiple repeated affected outputs intentionally preserved as one source candidate; distinct arm from C015.
18|S_W|estimate_repeat|Within results supplement,abstainerARD1.1% narrative differs from11% in eTable11 and its67%-56% displayed cell difference.
19|S_W|cross_reference|Results-supplement sixmonthCNRT-switch narrative cites compliance eTable7 rather than matched outcome eTable9 in the same PDF.
20|S_W|interval_direction_repeat|Within results supplement,sixmonthabstainer narrative+1%(-1.3%,-1.1%),probability55%,direction text conflict with eTable11+1%(-11%,12%),56% and paired figure values.|Several result fields bundled in one retained candidate; no cross-file source or plan relationship.
21|S_W|cross_reference|Results-supplement phase1-abstainer summary cites nonabstainer eTable10 rather than its matched eTable11 in the same PDF.
22|S_W|cross_reference|Results-supplement VARplus-versus-switch clause cites continuation-reference eTable9 rather than direct-switch-reference eTable10 in the same PDF.
23|S_W|count_percent_order|Results eTable3 employment heading n(%) disagrees with all16 cells displaying percentage(count).|Separate employment row block from C013's race cell.
24|S_W|category_total|Results eTable3 employed/unemployed counts sum49/50 and38/39 with no missingness category.|Distinct from C023: reordering values does not supply the missing participant per column.
''')
add('6063','''
1|S_W|flow_count_repeat|Main Figure1 gives21placebo discontinuations/111completers but Results gives23withdrawals/losses and implied109completers.|Disposition-category identity is conditional.
2|S_W|denominator_footnote|Results eTable2 row n167 and percentage-supported83+84 conflict with its footnote n165.|A narrower footnote population is possible; separate from C016's main95% discrepancy.
3|S_W|count_percentage|Results eTable5 krill smaller1unit10/107 is printed12%, versus ordinary9%.
4|S_W|count_percentage|Results eTable5 krill nochange80/107 is printed72%, versus ordinary75%.
5|S_W|count_percentage|Results eTable5 krill larger1unit12/107 is printed12%, versus ordinary11%.
6|S_W|rounding|Results eTable5 placebo smaller2units2/109 is printed1.9%, versus ordinary1.8%.
7|S_W|count_percentage|Results eTable5 placebo smaller1unit16/109 is printed12%, versus ordinary15%.
8|S_W|count_percentage|Results eTable5 placebo nochange75/109 is printed72%, versus ordinary69%.
9|S_W|duplicated_output|Within results eTable4,week4weight-bearingpain repeats both function-arm change estimates/intervals despite separate outcome labels.|Descriptive subtraction is diagnostic, not adjusted-model reconstruction; coincidence/production cause is unproven.
10|S_W|duplicated_output|Within results eTable4,week12legstrength repeats the complete week4backpain changes,effect,interval,andP=.53.|Distinct pair of rows from C009/C011; model-versus-descriptive differences alone are not proof.
11|S_W|duplicated_output|Within results eTable4,week12fastingglucose repeats hsCRP's between-group0.07(-1.19,1.33),P=.92.|Separate paired measures from C009/C010; identical outputs are a candidate, not proof of copying.
12|S_C,S_W|sign_repeat|Main KeyPoints gives+0.30 but its own abstract/table/Results give-0.3 and results eTable1 gives-0.27 for otherwise matched primary fields.|Mixed internal-main and cross-file sign discrepancy; common signed operand order is undefined.
13|S_C,S_W|adverse_event_count|Main Table3 placeboextremitypain count6 differs from5 in its abstract/narrative and results eTable7.|Mixed internal-main/cross-file counts; coding-category equivalence remains conditional.
14|S_C|cross_reference|Main Table3 adverse-event footnote cites eTable4 but supplied results supplement eTable4 is secondary endpoints and eTable7 contains the stated adverse-event detail.|Cross-file destination/content mismatch; main narrative corroborates intended eTable7.
15|S_C|cross_reference|Main Table3 serious-event footnote cites eTables5/6 but results supplement uses those forWORMS/analgesics and places serious events in eTable8.|Cross-file destination/content mismatch; separate regular-versus-serious-event footnotes from C014.
16|S_C|aggregate_percentage|Main95%adherence statement disagrees with163/167=97.6% from its cited results eTable2.|Main numerator/denominator unknown; C002 separately records the eTable167versus165 discrepancy, so not a duplicate and no added internal relation here.
''')
assert set(codes)=={r['key'] for r in inputs},set(codes)^{r['key'] for r in inputs}
# Every inventory was read. Beyond it, list only deeper files actually inspected for that row.
deep={'0318':{'verification/evidence_recheck.md':[2,4]},'0572':{'verification/evidence_recheck.md':[1,2]},'11057':{'verification/evidence_recheck.md':[1,2],'verification/evidence_recheck_C003.md':[3]},'12829':{'verification/evidence_recheck.md':[6,9,10,13]},'19585':{'verification/evidence_recheck.md':[1]},'2302':{'verification/evidence_recheck.md':[1,2,3,4,5]},'23898':{'checkers/cross_source_consistency.md':[1,2,3,4],'checkers/statistical_pass_2.md':[1,2,3,4,5,6,7]},'25786':{'verification/evidence_recheck.md':[3,4,5,6,7]},'4183':{'verification/evidence_recheck.md':[5,6,7,10,11,12,23,24]},'6063':{'verification/evidence_recheck.md':[12,13,14,15,16]}}
rows=[]
for r in inputs:
 c=codes[r['key']]; pkg=r['package'].split('.')[-1]; n=int(r['id'][1:]); base=f"2024/{r['package']}/.ai_paper_validation/review_1_5_3/"
 paths=[base+'source_inventory.md']+[base+p for p,ns in deep.get(pkg,{}).items() if n in ns]
 row={'key':r['key'],'primary':c['relations'][0],**c,'evidence_paths':paths,'duplicate_of':'','evidence_state':'not_reproduced' if pkg=='19585' and n==1 else 'recorded_candidate'}
 rows.append(row)
(root/'coded_2024.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Primary',Counter(r['primary'] for r in rows))
print('Relations',Counter(v for r in rows for v in r['relations']))
for p in dict.fromkeys(r['package'] for r in inputs):
 rr=[r for r in rows if f'::{p}::' in r['key']];print(p,len(rr),dict(Counter(r['primary'] for r in rr)))
