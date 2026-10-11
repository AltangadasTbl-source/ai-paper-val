# Workflow 1.6.2 Independent Mechanical Evidence Recheck

Runtime agent: 01a129cf-84b6-7100-8632-d270ac1d0646. Role: fresh evidence_rechecker; run model gpt-6.1-sol; reasoning effort high. Assigned and completed stable IDs: C001, C002, C003, C004, C005, C006, C007, C008. Every ID remains Pending Human Adjudication. Evidence states describe source-reading and reproduction facts only.

AGENTS.md, QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6_2/review_contract.md, workflow_1_6_2/report_spec.md, workflow_1_6_2/settings.toml and the current tooling record were read. Inputs were the current ledger, current initial inclusion screen, supplied sources and current-run source-linked locators. No prior scientific decision, external literature, web, custom Python extraction, or source modification was used.

Direct source authority was the supplied PDF at the physical page specified in each link. Source-native text was reread with direct Poppler 25.03.0 `pdftotext -layout -f N -l N source.pdf -`. Source-matched current-run Poppler CPU renderings in preprocessing/cross/ were independently viewed for main pp3,4,6; plan pp71,110,121,122,124,130,131,133; and results supplement p3. Their source-page mapping and direct pdftoppm provenance are recorded in checkers/cross_source_consistency.md. The statistics_1/calculation_record.md was a locator; all numerical calculations below were independently rebuilt from the visually confirmed inputs with JavaScript Number arithmetic. No new rendering or OCR was needed, and no derivative was written. Compute device: CPU.

Main pp1–9 and results-supplement pp1–3 were read directly, including the complete supplied reporting scope needed for C003. Other cited native plan locations were reread directly: pp9–10,15–16,36–37,64–65,90–92,121–124. The signed SAP image, rather than OCR, determined the sign on p130. All cited conflicting and corroborating locations were found. Page numbers below are physical PDF pages, not printed page labels.

| ID | Review domain | Relationship type | All relationships | Evidence state | Classification result |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | reproduced | Confirmed from endpoint content |
| C002 | protocol_report | P_R | P_R, P_P | reproduced | Confirmed; P_R precedes P_P |
| C003 | protocol_report | P_R | P_R | reproduced | Confirmed from explicit analysis specifications |
| C004 | statistical_results | S_W | S_W | reproduced | Confirmed; corroborating plans add no relationship |
| C005 | statistical_results | S_W | S_W | reproduced | Confirmed within main Table 2 |
| C006 | statistical_results | S_W | S_W | reproduced | Confirmed within main Table 2 |
| C007 | plan_material | P_P | P_P | reproduced | Confirmed within one bound plan bundle |
| C008 | statistical_results | S_W | S_W | reproduced | Confirmed within results-supplement eTable 2 |

No registered transcription or location required adjustment. All eight states are reproduced; the other allowed states are assigned to no ID. Source-reading gaps: none. Missing definitions and unavailable analytic inputs are specified separately below.

## C001 — Primary favorable-survival definition

**Location found and source/comparator matched:** Yes, for every listed location. PLAN final protocol [joi180004supp1_prod.pdf, p71 §4.1.1](../../../joi180004supp1_prod.pdf#page=71) defines favorable day-28 survival as CPC≤2 and additionally treats survival with the same degree of pre-randomization neurological disability as favorable. PLAN [p110 amendment comparison, primary-endpoint row](../../../joi180004supp1_prod.pdf#page=110) explicitly records the addition. REPORT [jama_jabre_2018_oi_180004.pdf, p1 Main Outcomes and Measures and Results](../../../jama_jabre_2018_oi_180004.pdf#page=1) states CPC1 or2; REPORT [p3 Outcomes](../../../jama_jabre_2018_oi_180004.pdf#page=3) states CPC≤2; REPORT [p4 Primary Outcome](../../../jama_jabre_2018_oi_180004.pdf#page=4) identifies CPC1–2 and gives44/1018 and43/1022; REPORT [p6 Table2 footnote b and ITT CPC rows](../../../jama_jabre_2018_oi_180004.pdf#page=6) explicitly counts CPC1 and2 as success and gives35+9 and37+6. Corroborating PLAN [p15 §4.1.1](../../../joi180004supp1_prod.pdf#page=15), [p122 §6.1](../../../joi180004supp1_prod.pdf#page=122), and [signed p131 §6.1](../../../joi180004supp1_prod.pdf#page=131) contain the absolute CPC≤2 rule without the added exception. The native and signed SAP readings match.

**Consistency rule and reproduced logical comparison:** Focus D, Route B. The amended rule can include a survivor with unchanged baseline CPC>2, whereas the report's explicit success coding counts CPC1–2. These are different success predicates. The report's44=35+9 and43=37+6 reproduce exactly; this checks which displayed CPC categories account for the printed numerators, but does not demonstrate that a participant was classified differently.

**Display-precision interval check:** Rounding does not reconcile categorical endpoint predicates. The count check has zero residual: allowing35±0.5 and9±0.5 gives their sum[43,45], overlapping44±0.5=[43.5,44.5];37±0.5 plus6±0.5 gives[42,44], overlapping43±0.5=[42.5,43.5]. Relative discrepancy for these count identities is zero. CPC categories are codes, not measured quantities to blur with a half-unit interval.

**Necessary inputs available / exact missing inputs:** Both endpoint specifications, the amendment disclosure, the success-coding footnote, denominators and CPC distributions are available. Missing are participant-linked baseline CPC, day-28 CPC, the number of survivors eligible for the unchanged-disability exception, and the coding instruction used to form the primary indicator. The baseline table has neurological-condition and activity-limitation summaries; it does not supply the CPC crosswalk needed to apply this exception.

**Alternative source-grounded interpretation:** No survivor may have qualified for the exception, the exception may have been applied without changing the displayed CPC1–2 totals, or the analysis may have used the older absolute rule. The amendment explicitly discloses the chronological change, so the older PLAN wording is contextual evidence, not an additional unexplained P_P comparison.

**Direct observation versus inferred explanation:** Direct observation is the difference between the amended predicate and the report's coding statement, and the exact reconciliation of displayed CPC1–2 counts to44 and43. An actual numerator change, participant reclassification, or production mechanism is not observed.

**Classification:** Review domain protocol_report; relationship type P_R; all relationships P_R. All protocol, SAP and amendment locations are PLAN because they specify prospective definitions; all article locations are REPORT because they describe the completed trial. The conflicting comparison is amended PLAN versus REPORT. Older plan wording only corroborates the absolute-rule side and its chronology is disclosed. Classification confirmed; no change. Classification ambiguity: the chronology and exception application do not identify the analysis predicate actually used.

**Evidence state:** reproduced. Determining fact: direct-source reading reproduces the amended unchanged-disability exception alongside the report's explicit CPC1–2 success rule; the definition discrepancy remains, without claiming a numeric effect.

**Exact remaining human question:** Which success rule generated44/1018 and43/1022, and how was the amended unchanged-baseline-disability exception applied to those primary indicators?

## C002 — Airway endpoint status across protocol, SAP and report

**Location found and source/comparator matched:** Yes, for every listed location and each repeated endpoint family. PLAN original [p9 Summary, secondary-endpoint list](../../../joi180004supp1_prod.pdf#page=9), [p10 continuation](../../../joi180004supp1_prod.pdf#page=10), and [p16 §4.1.2](../../../joi180004supp1_prod.pdf#page=16), and PLAN final [p64 Summary](../../../joi180004supp1_prod.pdf#page=64), [p65 continuation](../../../joi180004supp1_prod.pdf#page=65), and [p71 §4.1.2](../../../joi180004supp1_prod.pdf#page=71) put airway difficulty and complication measures under secondary endpoints. PLAN [p122 §§6.1–6.2](../../../joi180004supp1_prod.pdf#page=122) and [signed p131 §§6.1–6.2](../../../joi180004supp1_prod.pdf#page=131) instead assign the matched measures to Safety Endpoints, separately from secondary efficacy admission survival, day28 survival, ROSC and IDS. REPORT [p1 Main Outcomes and Measures](../../../jama_jabre_2018_oi_180004.pdf#page=1) calls difficulty/failure secondary; REPORT [p3 Outcomes](../../../jama_jabre_2018_oi_180004.pdf#page=3) likewise lists BMV difficulty and airway failure as secondary and separately describes complications. REPORT [p4 Adverse Events Analysis](../../../jama_jabre_2018_oi_180004.pdf#page=4) and [p6 Table3 Safety Population](../../../jama_jabre_2018_oi_180004.pdf#page=6) present airway safety results. PLAN [p37 §11.5](../../../joi180004supp1_prod.pdf#page=37) and [p92 §11.5](../../../joi180004supp1_prod.pdf#page=92) also describe safety analyses.

**Repeated-pattern coverage:** VAS and Han mask-ventilation difficulty occur under protocol secondary lists (VAS on pp10,16,65,71; Han on pp10,65,71) and SAP safety lists pp122,131. Tracheal failure, esophageal/mainstem intubation, vomiting, pulmonary aspiration and dental trauma occur under original/final protocol secondary lists pp9,16,64–65,71 and SAP safety lists pp122,131; extubation appears on pp16,65,71 and SAP pp122,131. BMV gastric regurgitation is secondary on pp10,16,65,71 and safety on pp122,131; the SAP safety lists also contain BMV procedural failure and gastric inflation. Those latter entries are retained as SAP family context, without inventing a protocol entry for gastric inflation. Table3 provides VAS, IDS, airway difficulty/failure, regurgitation, mainstem/esophageal intubation, dental injury and extubation; it does not provide a result for every named SAP complication. IDS remains secondary efficacy in the SAP and is not a shifted-status measure. The abstract-reported difficulty, failure and regurgitation results are the affected named results.

**Consistency rule and reproduced logical comparison:** Focus D, Route A category5. Read the explicit endpoint-family assignments, not merely a stylistic heading. The SAP separates efficacy and safety endpoint lists; the report/protocol use secondary designations for matched airway measures. Native and signed SAP copies reproduce the same assignment. The status difference is observed even though a concurrent secondary/safety designation is a source-grounded possibility.

**Display-precision interval check:** Not applicable to categorical endpoint-family membership; no numerical discrepancy qualifies this ID. Counts and intervals in the airway table are not being challenged here. Rounding cannot turn Safety Endpoints into Secondary Efficacy Endpoints.

**Necessary inputs available / exact missing inputs:** All compared lists and report-family labels are supplied, including the protocols' separate safety-analysis sections. Missing is an explicit hierarchy or crosswalk stating whether secondary and safety designations are concurrent, superseding or mutually exclusive, and which prespecified efficacy/safety population specification governs each published measure. No undisclosed amendment is inferred.

**Alternative source-grounded interpretation:** The original and final protocols already have safety-analysis sections, and the report simultaneously describes secondary airway outcomes and adverse-event results. Safety might be an umbrella designation that can coexist with secondary status. The SAP's separate efficacy/safety lists and differing population specifications do not explicitly define that equivalence.

**Direct observation versus inferred explanation:** Direct observation is the endpoint allocation under distinct headings and the report's concurrent designations. A substantive change in formal hierarchy, an altered analysis, or any numerical result effect is inferred rather than established and is not claimed.

**Classification:** Review domain protocol_report; relationship type P_R; all relationships P_R, P_P. Original/final protocol and both SAP copies are PLAN by their prescriptive content; article abstract, outcome methods, adverse-event results and tables are REPORT. Report versus SAP gives P_R; protocol versus SAP gives P_P within the bound plan material. P_R takes precedence. The report's concurrent labels alone do not establish an independent S_W discrepancy, so S_W is not added. Classification confirmed; no change. Classification ambiguity: concurrent designations could explain the formal-status interpretation.

**Evidence state:** reproduced. Determining fact: all source endpoint lists and report designations match the registered reading, leaving the explicit SAP-family versus protocol/report-family allocation unresolved; the alternative is retained rather than treated as an established hierarchy change.

**Exact remaining human question:** Were the matched airway outcomes secondary efficacy, safety, or concurrently both, and which prespecified endpoint family and analysis-population rules governed each published result?

## C003 — Specified analysis populations and interval presentations

**Location found and source/comparator matched:** Yes. PLAN [p121 §5.3](../../../joi180004supp1_prod.pdf#page=121) and [signed p130 §5.3](../../../joi180004supp1_prod.pdf#page=130) define AT as randomized adult cardiac-arrest patients grouped by ventilation really received. PLAN [p124 §§8.2.1,8.2.3,8.2.4](../../../joi180004supp1_prod.pdf#page=124) and [signed p133 same sections](../../../joi180004supp1_prod.pdf#page=133) explicitly specify primary CI/NI analyses for ITT/PP/AT, secondary analyses also in PP/AT, safety in ITT/AT, secondary OR/difference interval presentation, and safety OR interval presentation. PLAN [p37 §§11.4.2–11.5](../../../joi180004supp1_prod.pdf#page=37), [p91 §11.4.2](../../../joi180004supp1_prod.pdf#page=91), and [p92 §11.5](../../../joi180004supp1_prod.pdf#page=92) also specify OR interval presentation.

**Every affected report location:** REPORT [p1 abstract](../../../jama_jabre_2018_oi_180004.pdf#page=1), [p3 Statistical Analysis](../../../jama_jabre_2018_oi_180004.pdf#page=3), [p4 Figure/Primary Outcome/Secondary Outcomes/Adverse Events/Post-Hoc Analyses](../../../jama_jabre_2018_oi_180004.pdf#page=4), and [p6 Tables2–3/post-hoc continuation](../../../jama_jabre_2018_oi_180004.pdf#page=6) show primary ITT/PP NI, secondary ITT/PP and actual-treatment safety. REPORT [joi180004supp2_prod.pdf, p3 eTable2](../../../joi180004supp2_prod.pdf#page=3) shows post-hoc exclusion43/971 versus39/978 and one-way BMV→ETI reclassification41/863 versus45/1174, both under an intention-to-treat heading. Its reclassification result has difference0.9, two-sided95% CI[−0.9,2.7] and P=.31, with no identified NI test. The full report was searched by direct reading: main pp1–9 and results supplement pp1–3. Supplement p1 is its contents and p2 is center contributions; the remaining main pages contain baseline characteristics, discussion, article information and references, not the missing trial displays.

**Consistency rule and reproduced logical comparison:** Focus D, Route A category5. An explicit planned primary/key-secondary population analysis or interval presentation has no matching result in the supplied reporting scope. Primary NI appears in ITT/PP, not an explicitly identified full AT analysis; survival to admission/day28 and ROSC appear in ITT/PP, not an identified AT population; difficulty/failure/regurgitation appear for actual-treatment safety, not additionally randomized ITT. The planned trial OR intervals are not presented. Article p3 says secondary OR intervals were calculated, which does not supply their printed estimates/intervals. Observational-study ORs in the sample-size background are not matching trial results.

**Display-precision interval check:** Not applicable to absence/presence, population labels, or promised interval presentation. The reclassification counts and printed95% interval are confirmed as source content, not challenged numerically by this ID. No rounding rule can supply an absent NI test or an absent population crosswalk.

**Necessary inputs available / exact missing inputs:** Explicit plan specifications, AT definition, reported population definitions, all report pages and all displays are available. Missing are the full AT treatment-assignment crosswalk (including bidirectional/no-attempt cases and eligibility), AT primary NI result and decision, AT key-secondary results, randomized ITT airway safety results, and planned trial OR interval displays or an amendment explaining their replacement. Participant data are unavailable to reconstruct those results. The safety mapping in p3 expressly attributes unsuccessful ETI attempts to ETI and therefore cannot be assumed identical to every definition of actual treatment.

**Alternative source-grounded interpretation:** eTable2's one-way reclassification may have been intended to supply an AT primary sensitivity counterpart, or report safety may supply the intended AT safety counterpart; its ITT heading, lack of full mapping and lack of NI test do not identify the complete planned AT analysis. Additional analyses may exist outside this supplied package. An amendment may explain replaced displays, but none is identified in the compared content. Mixed prospective and retrospective language in the SAP bounds chronology interpretation.

**Direct observation versus inferred explanation:** Direct observation is what the SAP expressly requires and what the complete supplied report presents. The assertion is limited to no matching result being supplied; it does not assert that an analysis was never conducted. An effect on the trial conclusion or any result obtainable from unsupplied data is not inferred.

**Classification:** Review domain protocol_report; relationship type P_R; all relationships P_R. Protocol/SAP sections are PLAN because they prescribe analyses; article and numerical eTables are REPORT because they describe completed analyses. The inconsistency is plan specification versus report presentation. The report documents are not mutually conflicting here, so their presence does not add S_C; earlier protocols corroborate presentation specifications without adding P_P. Classification confirmed; no change. Classification ambiguity: possible amendment or AT/post-hoc mapping, not documented in the supplied comparison.

**Evidence state:** reproduced. Determining fact: direct rereading finds the explicit ITT/PP/AT and OR-presentation specifications, while the complete supplied report has no matching identified results for the additional registered specifications.

**Exact remaining human question:** Where are the specified additional population and OR results, or which supplied amendment and population/result crosswalk identifies their replacement by the published displays?

## C004 — Numerical ordering of the noninferiority confidence bound

**Location found and source/comparator matched:** Yes. REPORT [p3 Statistical Analysis](../../../jama_jabre_2018_oi_180004.pdf#page=3) accepts NI if the lower CI bound is higher than−1%. REPORT [p4 Primary Outcome](../../../jama_jabre_2018_oi_180004.pdf#page=4) prints the ITT lower bound−1.64%, then says it was greater than the NI threshold, while concluding NI was not demonstrated. Corroborating REPORT [p1 abstract](../../../jama_jabre_2018_oi_180004.pdf#page=1), [p2 Key Points](../../../jama_jabre_2018_oi_180004.pdf#page=2), [p7 Discussion](../../../jama_jabre_2018_oi_180004.pdf#page=7), and [p8 Conclusions](../../../jama_jabre_2018_oi_180004.pdf#page=8) give the inconclusive/no-NI reading. The p4 bounds−1.70% and−1.74% are additional hierarchical/PP results, not copies of the ITT bound.

**Consistency rule and calculation reproduced:** Focus B, Route A category2. The printed ordering is reversed:−1.64<−1. The literal separation is0.64 percentage points. Under the article's rule a bound below−1 does not establish NI, agreeing with the stated conclusion but conflicting with the greater-than phrase. This is the registered numerical-order statement, not a claim of a CI/P conflict.

**Display-precision interval check:** Lower-bound interval[−1.645,−1.635]% is below the exact declared design margin−1%. Even allowing the margin the broader display interval[−1.5,−0.5]% leaves gap0.135 percentage points and relative gap0.135/1=0.135>0.05. No allowable rounding reverses the order. Against an exact design margin the minimum separation is0.635 points.

**Necessary inputs available / exact missing inputs:** The lower bound, contrast direction, decision rule and margin are available; no numeric input is missing for ordering. The intended wording of the bound/threshold comparison is not specified beyond the conflicting sentence. No CI algorithm is needed to compare the already printed bound with the declared margin.

**Alternative source-grounded interpretation:** The printed greater-than phrase may refer to a different intended ordering. Immediate no-NI wording and other report copies support the numerical bound's below-margin reading. No alternate actual NI result is supplied.

**Direct observation versus inferred explanation:** Direct observation is the incompatible greater-than statement and printed numbers. A substituted word, mechanism or intended final wording is inferred and not assigned. No paper-level conclusion change is asserted.

**Classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. Both conflicting locations are REPORT in the same article. Other article conclusions and matching plan rules only corroborate one side; they do not add a plan-report relationship. Classification confirmed; no change. Classification ambiguity: None.

**Evidence state:** reproduced. Determining fact: the directly printed−1.64% bound remains wholly below−1% under even the broad margin rounding allowance while p4 states greater than.

**Exact remaining human question:** Which bound-versus-threshold ordering is intended by the greater-than statement in the primary-outcome paragraph?

## C005 — Table 2 per-protocol confidence intervals

**Location found and source/comparator matched:** Yes, including both affected rows and all same-display comparators. REPORT [p6 Table2 PP Survival at28d](../../../jama_jabre_2018_oi_180004.pdf#page=6) prints54/995 versus51/943, difference0.1, CI−10 to9.7 and P=.99. The PP hospital-admission row prints289/995 versus312/943, difference−4.0, CI−7.6 to0.6 and P=.055. Same-table ITT survival has55/1018 versus54/1022, CI−1.8 to2.1; ITT admission294/1018 versus333/1022, CI−7.7 to0.3; ITT ROSC348/1018 versus397/1022, CI−8.8 to−0.5; PP ROSC342/995 versus377/943, CI−9.9 to−1.3. Table footnote a attributes P values to chi-square or Fisher exact tests; it does not identify a CI algorithm. REPORT [p3 Statistical Analysis](../../../jama_jabre_2018_oi_180004.pdf#page=3) says secondary difference and OR95% CIs were calculated without row-specific CI algorithms.

**Consistency rule and calculation reproduced:** Focus B/C, Route A category4. With p=a/n,q=b/m,d=100(p−q),s=100√[p(1−p)/n+q(1−q)/m], and z=1.959963984540054, calculate d±zs. This independent-proportion calculation reproduces the four other binary Table2 intervals: ITT survival[−1.83285255,2.07083886]; ITT admission[−7.70393417,0.29790800]; ITT ROSC[−8.83435860,−0.48709207]; PP ROSC[−9.90623480,−1.30762879]. Their full input-rounding endpoint ranges overlap their respective printed endpoint ranges. The affected PP survival calculation gives d=0.01886420,s=1.02875615,CI[−1.99746080,2.03518921]; PP admission gives d=−4.04066995,s=2.10213883,CI[−8.16078633,0.07944644].

**Display-precision interval check:** Each displayed count and denominator is allowed±0.5: survival a[53.5,54.5],n[994.5,995.5],b[50.5,51.5],m[942.5,943.5]; admission a[288.5,289.5],n[994.5,995.5],b[311.5,312.5],m[942.5,943.5]. Form p_min=a_min/n_max,p_max=a_max/n_min and analogous q bounds; combine difference and variance extrema separately to obtain conservative ranges. All risks are below0.5, so p(1−p) increases over each risk interval. For the variance minimum use p_min(1−p_min)/n_max; for maximum use p_max(1−p_max)/n_min, and likewise q. These enlarged ranges include every allowable calculation, so remaining gaps cannot be closed by a tighter joint calculation.

| Affected limit | Recomputed endpoint range | Printed endpoint range | Interval gap | Relative gap |
|---|---|---|---:|---:|
| PP survival lower−10 | [−2.11638896,−1.87849692] | [−10.5,−9.5] | 7.38361104 | 0.73836110 |
| PP survival upper9.7 | [1.91621931,2.15411135] | [9.65,9.75] | 7.49588865 | 0.77277203 |
| PP admission upper0.6 | [−0.05949222,0.21836974] | [0.55,0.65] | 0.33163026 | 0.55271710 |

The admission lower endpoint alone has range[−8.29971929,−8.02185733] versus[−7.65,−7.55], gap0.37185733/7.6=0.04892860, which is within the contract's0.05 allowance and is not an independent reproduced discrepancy. Survival difference range[−0.09000715,0.12772954] overlaps printed0.1±0.05; its gap is zero. All affected printed CIs contain zero and their P values are nonsignificant; there is no interval-versus-P threshold conflict.

**Necessary inputs available / exact missing inputs:** Counts, row populations, contrast orientation, printed limits and95% confidence level are available for the reproducing calculation. Missing is the actual CI algorithm, row-specific method switch, source calculation output, and any different input population used for either affected interval. The reproducing calculation is not evidence that the authors selected this particular method.

**Alternative source-grounded interpretation:** A distinct unprinted row-specific method or population could generate a different interval; an alternative intended limit reading could also explain the display. The same-table comparators support the reproducing-method check, while the methods text does not uniquely specify the actual algorithm.

**Direct observation versus inferred explanation:** Direct observation is the pair of printed intervals and the method's ability to reproduce the other rows but not the affected limits beyond rounding. The production mechanism or intended replacement interval is not observed. The two PP rows remain one same-display pattern; no common cause with eTable2 is inferred.

**Classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. Every conflicting result, input and same-display comparator is REPORT within the article. No PLAN or second REPORT has a conflicting copy. Classification confirmed; no change. Classification ambiguity: None; actual CI-method uncertainty is an analytic limitation, not document-role ambiguity.

**Evidence state:** reproduced. Determining fact: independent recomputation from confirmed counts reproduces the other Table2 rows, while both PP survival limits and the PP admission upper limit retain relative interval gaps>0.05 under full half-unit inputs.

**Exact remaining human question:** Which CI method and input population generated the two affected PP Table2 intervals?

## C006 — Per-protocol ROSC count and percentage

**Location found and source/comparator matched:** Yes. REPORT [p6 Table2 PP Return of spontaneous circulation](../../../jama_jabre_2018_oi_180004.pdf#page=6) visibly prints BMV342(34.4%) under n995 and ETI377(30.0%) under n943, difference−5.6 with95% CI−9.9 to−1.3 and P=.01. REPORT [p4 Figure and baseline-population paragraph](../../../jama_jabre_2018_oi_180004.pdf#page=4) independently gives the same PP denominators995 and943. No alternative denominator appears in that row.

**Consistency rule and calculation reproduced:** Focus A/B, Route A category3, with a direction reading also under category2. The ETI count percentage is100×377/943=39.9787911%, while the row prints30.0%. BMV100×342/995=34.3718593%. The count-derived BMV−ETI difference is−5.60693180 points, matching−5.6; the printed percentage contrast is34.4−30.0=+4.4 points, reversing the count/difference direction.

**Display-precision interval check:** ETI count[376.5,377.5] and denominator[942.5,943.5] give100×[376.5/943.5,377.5/942.5]=[39.90461049,40.05305040]%. Printed30.0% permits[29.95,30.05]%; gap9.85461049 points, relative gap9.85461049/30=0.32848702>0.05. BMV permitted count percentage[34.30436966,34.43941679]% overlaps printed34.4±0.05=[34.35,34.45]. Count-derived difference range[−5.74868073,−5.46519370] overlaps−5.6±0.05=[−5.65,−5.55]. Printed-percentage difference range[4.30,4.50] remains positive, so rounding cannot reconcile its direction with the negative count-based difference.

**Necessary inputs available / exact missing inputs:** Printed numerator, group denominator, percentage and contrast are all available; no input is missing for arithmetic. Missing is any alternative intended count, denominator, or population that would account for30.0% and a source calculation showing which field represents the PP result.

**Alternative source-grounded interpretation:** The percentage could belong to another intended population or a substituted printed reading. The supplied count, denominator and negative difference consistently support the count-based direction, but do not establish an intended final replacement value.

**Direct observation versus inferred explanation:** Direct observation is that377,943 and30.0% do not reconcile in one display, and that the printed percentages reverse the other row quantities' direction. A production mechanism or intended corrected percentage is inferred and not assigned.

**Classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. The row and corroborating population paragraph/figure are REPORT in the same article. There is no conflicting plan or report-supplement value. Classification confirmed; no change. Classification ambiguity: None.

**Evidence state:** reproduced. Determining fact: the directly read377/943 versus30.0% mismatch retains relative gap0.32848702 under all allowed input/display rounding.

**Exact remaining human question:** Which ETI PP ROSC numerator, denominator and percentage belong to the result shown in this row?

## C007 — Alternative boundary in native and signed SAP copies

**Location found and source/comparator matched:** Yes. PLAN [p121 §4.1 native SAP](../../../joi180004supp1_prod.pdf#page=121) prints H1: BMV−TI≥−0.01. Direct visual reading of PLAN [p130 §4.1 signed SAP](../../../joi180004supp1_prod.pdf#page=130) prints H1: BMV−TI≥0.01, with no minus sign before0.01. Both H0 lines use≤−0.01, and both pages carry the18.FEB.2015 SAP date. PLAN [p124 §8.2.1](../../../joi180004supp1_prod.pdf#page=124) and [signed p133 §8.2.1](../../../joi180004supp1_prod.pdf#page=133) require a lower bound higher than−0.01; PLAN [p36 §11.2 continuation](../../../joi180004supp1_prod.pdf#page=36) and [p90 §11.2](../../../joi180004supp1_prod.pdf#page=90) corroborate H1 at−0.01. The signed scan, not native OCR, determines the positive reading.

**Consistency rule and calculation reproduced:** Focus D, Route A category2. The alternative-hypothesis contrast boundary is−0.01 in one copy and+0.01 in the signed copy. These literal design constants differ by0.02, or2 percentage points, and specify different favorable sets. This concerns the signed numerical boundary, not a conventional equality-versus-strict-inequality distinction.

**Display-precision interval check:** Even treating design constants as rounded displays gives native[−0.015,−0.005] and signed[0.005,0.015]. Gap0.010 divided by absolute reference0.01 gives relative discrepancy1.00>0.05. Exact design constants differ by0.02. Rounding cannot reconcile the sign.

**Necessary inputs available / exact missing inputs:** Both H0/H1 statements, common SAP date and operational threshold statements are available. No numerical input is missing for the comparison. Missing is an explicit controlling-copy statement or amendment identifying whether the positive signed boundary is intended to govern the primary NI decision.

**Alternative source-grounded interpretation:** A missing sign in the signed alternative line, or a different intended rule not carried into the operational sections, could explain the discrepancy. Matching negative H0 and operational boundaries support the negative-boundary interpretation but do not authorize changing the printed signed line.

**Direct observation versus inferred explanation:** Direct observation is the absent minus mark in the signed H1 line relative to the negative native H1 and operational rules. The production mechanism and controlling intended boundary are not observed.

**Classification:** Review domain plan_material; relationship type P_P; all relationships P_P. Both SAP copies and both protocols are PLAN because they specify design and decision rules. They remain one bound plan bundle, regardless of supplement filename or version arrangement. The article's negative-margin rule only corroborates a side, so it adds no P_R relationship. Classification confirmed; no change. Classification ambiguity: controlling-copy/chronology interpretation is not specified, but the location roles are clear.

**Evidence state:** reproduced. Determining fact: visual source reading confirms+0.01 on the signed H1 line and−0.01 on the native H1 line, with a nonoverlapping half-unit gap and relative discrepancy1.00.

**Exact remaining human question:** Which alternative-hypothesis boundary in the supplied SAP copies governs the primary noninferiority analysis?

## C008 — Post-hoc exclusion confidence interval

**Location found and source/comparator matched:** Yes. REPORT [joi180004supp2_prod.pdf, p3 eTable2 ECMO/donation exclusion row](../../../joi180004supp2_prod.pdf#page=3) prints43/971(4.4%) versus39/978(4.0%), BMV−ETI difference0.4,95% CI[−2.2,1.3], P=.63. The companion reclassification row on the same page prints41/863(4.8%) versus45/1174(3.8%), difference0.9,CI[−0.9,2.7], P=.31. Its footnote identifies chi-square or Fisher exact tests for P values, not a CI method. REPORT [main p3 post-hoc methods](../../../jama_jabre_2018_oi_180004.pdf#page=3) supplies the post-hoc scope; the continuation and results pointers on [p4](../../../jama_jabre_2018_oi_180004.pdf#page=4) and [p6](../../../jama_jabre_2018_oi_180004.pdf#page=6) corroborate that scope, without a conflicting numerical copy.

**Consistency rule and calculation reproduced:** Focus B/C, Route A category4. Apply the independent-proportion95% calculation stated in C005, independently rebuilt from this display's confirmed inputs. The companion row yields d=0.91781966,s=0.91560503,CI[−0.87673322,2.71237253], reproducing its printed endpoints. The exclusion row yields d=0.44069424,s=0.90959080,CI[−1.34207097,2.22345945], which does not reproduce the exclusion limits. Both printed intervals include zero and both P values are nonsignificant; point containment and endpoint order are satisfied. The issue is the reproducing-method comparison, not a CI/P threshold conflict.

**Display-precision interval check:** Exclusion inputs permit a[42.5,43.5],n[970.5,971.5],b[38.5,39.5],m[977.5,978.5]. Using the conservative difference/variance bounds described in C005 gives lower range[−1.46026215,−1.22381737] and upper range[2.10520688,2.34165166]. Printed−2.2 permits[−2.25,−2.15], leaving gap0.68973785 and relative gap0.68973785/2.2=0.31351720. Printed1.3 permits[1.25,1.35], leaving gap0.75520688 and relative gap0.75520688/1.3=0.58092837. Both exceed0.05. The exclusion difference range[0.33375762,0.54763189] overlaps0.4±0.05, so the point estimate itself is not challenged. Companion inputs41±0.5,863±0.5,45±0.5,1174±0.5 give lower endpoint range[−0.99260274,−0.76077350] and upper range[2.59644548,2.82827471], overlapping the printed ranges[−0.95,−0.85] and[2.65,2.75]; its endpoint gaps are zero.

**Necessary inputs available / exact missing inputs:** Both row counts/denominators, contrast,95% level, printed estimates and intervals are available for the same-display comparison. Missing is the actual CI algorithm, any row-specific method/population choice, and source calculation output for the exclusion limits. No exact equality to the named P-test is required or asserted.

**Alternative source-grounded interpretation:** A different unprinted exclusion-row CI method or input population, or an alternative intended limit reading, could explain the interval. The companion row supports the reproducing calculation but does not establish the actual algorithm selected for either row.

**Direct observation versus inferred explanation:** Direct observation is the printed pair of limits and failure of a companion-row reproducing method beyond full display allowance. A reversed intended contrast or any replacement limits are inferred possibilities, not assigned. No shared cause with C005 is established.

**Classification:** Review domain statistical_results; relationship type S_W; all relationships S_W. Both numerical rows are REPORT in the same non-plan results supplement. The article's post-hoc descriptions only corroborate scope, so they do not add S_C; no PLAN contributes a conflicting comparator. Classification confirmed; no change. Classification ambiguity: None.

**Evidence state:** reproduced. Determining fact: direct reading confirms[−2.2,1.3], while independent full half-unit computation leaves relative endpoint gaps0.31351720 and0.58092837 under a method reproducing the companion row.

**Exact remaining human question:** Which CI method, input population and source calculations generated the exclusion-row interval in eTable2?

## Scope closure and limitations

Closed scope: C001, C002, C003, C004, C005, C006, C007, C008, including all registered affected and corroborating locations and both affected Table2 PP rows. Eight complete evidence records; eight reproduced states; eight content-based classification confirmations; no transcription/location adjustment; no source-reading gap. Numerical half-unit interval computations were independently reproduced and recorded in the corresponding cards. No candidate was deleted, renumbered, adjudicated or given a disposition.

Remaining limitations are supplied-input limitations: baseline CPC-to-survival linkage and exception coding (C001); formal concurrent versus changed endpoint-family status (C002); AT mapping, promised additional result displays and any supplied replacement amendment (C003); intended greater-than comparison (C004); actual CI methods/populations/output (C005 and C008); intended ROSC row fields (C006); and controlling signed/native SAP boundary (C007). These are the exact questions recorded in each card. Sources, pre-existing assets and other agents' artifacts were preserved.
