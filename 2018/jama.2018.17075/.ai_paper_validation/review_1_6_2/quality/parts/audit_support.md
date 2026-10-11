# Independent quality audit — support shard

Pending Human Adjudication. Fresh gpt-6.1-sol/high runtime `01a129ea-c9cd-7963-af96-35c47b46ef8d`. Assigned stable IDs C009, C010, C011, C012, C013, C014, C015; ten screening finding rows; 59 checker exclusions. Coverage/execution controls and C001–C008 belong to the distinct main auditor. This shard makes no substitute completion claim about that separate scope.

Read: complete normative scope and review contract; report-card requirements; complete current classification table; assigned ledger, recheck and checker cards; relevant records from both statistical passes; assigned screening and exclusion rows. Source-based relationships, rather than a count objective, controlled this audit. Closure counts below describe completed work only. No earlier candidate/screening/classification/report artifact was used as scientific input. Sources and prior artifacts were preserved; no web, external literature, raw data, preferred analysis, severity or scientific disposition was used.

Fresh direct Poppler layout extraction covers all four supplied PDFs. Candidate source values and critical visual material were independently inspected in source-matched page renders. All seven assigned stable IDs occur in the current recheck. Every assigned finding has one original screening decision. Every assigned card below provides the exact source locations, bounded interpretation and extraction impact needed for report assembly. No candidate rests only on a display-zero P value.

## C009 — Final significance-rule specification

**Candidate statement:** The report's all-analysis .05 rule and final protocol's explicitly substituted .0459 final boundary do not specify the same decision region.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 p.4 vs PLAN DOC-002 p.84; PLAN p.188 earlier-version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced by explicit fixed-rule replacement, qualifying by Route B: focus D; nominal versus adjusted decision testing is not distinguished locally; the extracted final primary-test alpha is affected.

**Finding IDs:** F-XS-003

**Qualifying route:** Route B

**Classification rationale:** Completed-report methods versus prospective final V9 methods supplies P_R alone. The earlier two-look charter is historical context, not a simultaneous P_P conflict.

**Classification ambiguity:** Nominal .05 reporting and operational .0459 testing may coexist, but the supplied report does not establish this distinction.

**Exact source locations:** [REPORT significance paragraph p.4](../../../../jama_cooper_2018_oi_180132.pdf#page=4); [PLAN final §15.1.3 p.84](../../../../joi180132supp1_prod.pdf#page=84); [earlier charter p.188](../../../../joi180132supp1_prod.pdf#page=188).

**Source evidence:** Report says two-sided P<.05 for all analyses. Final plan says final ±1.996 SD/P=.0459 rather than ±1.96 SD/P=.05 after expanded interim monitoring. The earlier charter gives |Z|≥1.975/P=.048 and alpha .05 for the original two-look design.

**Reported-versus-comparator:** All-analysis .05 versus explicitly replaced final .0459 rule; earlier charter retained as history.

**Reasoning procedure:** Compare explicit decision specifications, separating fixed critical regions from rounded copies and operational consequences from observed results.

**Calculation:** Copy intervals [.04585,.04595] and [.045,.055] overlap: gap0, relative0. They cannot establish a copy discrepancy. A hypothetical exact P=.048 meets P<.05 but not P<.0459; it illustrates the different specified regions only. Actual primary P=.94 meets neither.

**Affected result or extracted value:** Final primary-test alpha and its relation to expanded interim monitoring.

**Why context does not resolve it:** The report does not explain whether .05 is nominal reporting accompanied by the adjusted final decision boundary.

**Alternative source-grounded interpretations:** Nominal .05 reporting may coexist with operational .0459 testing; the earlier charter may be superseded by final V9's additional monitoring.

**Mechanical evidence recheck:** Source text, physical pages, roles and fixed-rule comparison confirmed. P_R/domain/reproduced agree with recheck. Actual operational rule and unsupplied SAP clarification remain missing. Remaining human question: which final rule applied, and was nominal reporting distinguished from adjusted decisions?

**Potential downstream evidence impact:** A methods extractor could copy .05 or .0459 as final alpha. No observed significance reversal or downstream conclusion change is established.

**Evidence-card audit and repair:** Align active prose to P_R alone and retain zero copy gap, actual P=.94 and historical qualification. F-QA-101 below adds duplicate audit provenance for the same issue; no additional stable candidate is needed.

## C010 — Bleeding RR, CI and P attribution pattern

**Candidate statement:** Main-table bleeding RR/CI/P tuples reproduce the opposite outcome's counts, while the supplement assigns the P values to the other outcomes.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 Table2 p.7 vs REPORT DOC-003 eTable6 p.10; REPORT DOC-001 same-display counts/intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Reproduced by the opposite-row intervals/tests and differing report copies. Route A category4 applies: a method reproduces neighboring rows but not the two own-row interval assignments beyond precision.

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4

**Classification rationale:** Two distinct REPORT documents supply S_C; main-table counts versus intervals supply S_W. S_C precedes S_W. Estimates, intervals and tests require statistical_results despite the attribution component.

**Classification ambiguity:** Separate undisclosed analyses remain possible; document roles are clear.

**Exact source locations:** [unadjusted method p.3](../../../../jama_cooper_2018_oi_180132.pdf#page=3); [Table2 both bleeding rows p.7](../../../../jama_cooper_2018_oi_180132.pdf#page=7); [eTable6 both bleeding rows p.10](../../../../joi180132supp2_prod.pdf#page=10); corroborating [abstract p.1](../../../../jama_cooper_2018_oi_180132.pdf#page=1) and [narrative p.5](../../../../jama_cooper_2018_oi_180132.pdf#page=5).

**Source evidence:** Intracranial47/260 versus37/240 prints RR1.23(.43–3.5), P=.70; extracranial8/260 versus6/240 prints RR1.17(.79–1.74), P=.43. eTable6 repeats counts but gives intracranial .43/extracranial .70. Main RD columns reproduce own rows.

**Reported-versus-comparator:** Main RR/CI/P tuples versus own-row count-based calculation and supplementary P assignment.

**Reasoning procedure:** RR=(a/n)/(c/m); SE(logRR)=sqrt(1/a−1/n+1/c−1/m); limits=RR×exp(±1.95996398454×SE). Check stated Pearson equal-proportion diagnostic, neighboring rows and half-unit input corners. Consolidate both rows once.

**Calculation:** Intracranial RR1.17255717, CI[.79118130,1.73776899], P=.42666956; extracranial RR1.23076923, CI[.43334502,3.49558164], P=.69603919. Primary, mortality and infection rows reproduce their printed intervals. Half-unit intracranial lower-limit bounds[.76973897,.81321980] versus printed[.425,.435] leave .33473897/.43=.77846; extracranial bounds[.37662053,.49716491] versus[.785,.795] leave .28783509/.79=.36435. P-copy intervals[.695,.705]/[.425,.435] leave .260/.70=.371429 or .260/.43=.604651. Point-RR differences alone are within precision.

**Affected result or extracted value:** Outcome-specific bleeding confidence limits and P values.

**Why context does not resolve it:** Route A category4: the same reproducing method yields different own-row intervals; immediate reconstruction does not remove the printed values.

**Alternative source-grounded interpretations:** Separate analyses could explain the displays, but the supplied methods do not assign them to these rows or explain exact opposite-row reproduction.

**Mechanical evidence recheck:** Both tables' labels, counts and tuples confirmed visually and in fresh text; bounds reproduced independently. Classification and reproduced state agree. Missing definition: any separate analysis and row mapping. Remaining human question: which RR/CI/P belongs to each outcome, and were separate analyses used?

**Potential downstream evidence impact:** Extraction could associate the wide/narrow interval or .70/.43 with the other bleeding outcome. Both displayed P values exceed .05; no trial-conclusion change is asserted.

**Evidence-card audit and repair:** Carry full input-precision bounds rather than only initial point diagnostics. F-XS-002 and both row occurrences remain one pattern; no source-production mechanism is inferred.

## C011 — Interim normal boundary and P threshold

**Candidate statement:** A fixed normal |Z|≥3 monitoring rule is paired with approximate P<.001, leaving the operative threshold unclear.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 p.188 internal normal boundary/P threshold; PLAN pp.84,152 method/version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Route B applies to the reproduced fixed critical-region comparison: focus D; operational interpretation is unresolved; extraction of the primary/mortality stopping specification changes. A1's estimate/interval wording does not expressly cover a standalone prospective boundary pair, so the route is repaired without changing the ID or evidence state.

**Finding IDs:** F-ST1-205

**Qualifying route:** Route B

**Classification rationale:** Prospective charter instructions are PLAN; comparison within that content supplies P_P/plan_material. Final sidedness and the earlier amendment are context, not REPORT relationships or an additional simultaneous version conflict.

**Classification ambiguity:** Approximate P may be shorthand; the intended tail convention and operative rule hierarchy remain unspecified.

**Exact source locations:** [charter boundary paragraph p.188](../../../../joi180132supp1_prod.pdf#page=188); [final 3SD/two-sided convention p.84](../../../../joi180132supp1_prod.pdf#page=84); [historical amendment p.152](../../../../joi180132supp1_prod.pdf#page=152).

**Source evidence:** Conventional three-standard-deviation |Z_k|≥3 boundary, normal approximation to discrete binomial proportions, approximate P<.001. Final V9 uses two-sided tests unless specified. Earlier .005 language is version context.

**Reported-versus-comparator:** Charter's fixed3 boundary versus literal .001 critical region; not an observed statistic/P pair.

**Reasoning procedure:** Independently integrate the normal tail under the explicitly named approximation; examine both tail conventions and retain approximate wording.

**Calculation:** At3, one-sided P=.00134989803163 and two-sided P=.00269979606326. Literal two-sided .001 corresponds |Z|>3.290527; one-sided corresponds Z>3.090232. Some larger Z values satisfy both descriptions, but the boundaries differ. A fixed rule3 is not a rounded observed statistic varying over[2.5,3.5]. Numeric-copy interval arithmetic is not applicable to this explicit decision-rule comparison. If approximate P is descriptive shorthand, it remains an alternative rather than an observed conflict.

**Affected result or extracted value:** Interim stopping specification for primary GOSE/mortality.

**Why context does not resolve it:** The source names a normal approximation but does not specify whether3SD or literal P<.001 controls operational decisions.

**Alternative source-grounded interpretations:**3SD may govern with P shorthand; a discrete calibration may exist, but no replacement boundary is supplied. Earlier .005 may be superseded.

**Mechanical evidence recheck:** Exact source and scanned amendment confirmed; normal tails independently reproduced. P_P/domain/reproduced agree with recheck; route narrowed to B. Missing operational interpretation remains bounded. Remaining human question: which threshold, tail convention and meaning of approximate applied?

**Potential downstream evidence impact:** A methods extractor could record3SD or a literal .001 rule. No observed crossing, stopping consequence or treatment identity is inferred.

**Evidence-card audit and repair:** Replace active Route A1/exemption assertions with Route B and retain approximation and historical context. Support wording changes; the stable ID and reproduced source fact remain.

## C012 — July 2016 cumulative primary-outcome Y series

**Candidate statement:** The favorable-GOSE cumulative Y curve does not reproduce favorable block-count sums that reproduce X in the same display.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT observed interim DOC-002 p.192 block table vs cumulative chart; REPORT DOC-002 p.191 corroborates

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Route A category4 applies: cumulative addition reproduces X but not Y, with conservative separated intervals and minimum relative gap1/13=.076923>.05. Observed interim result content is REPORT within the overall PLAN bundle.

**Finding IDs:** F-ST1-301

**Qualifying route:** Route A, category 4

**Classification rationale:** Both compared displays contain observed outcomes in one supplied PDF, hence S_W/statistical_results. Prospective rules are not a conflicting comparator; p.191 only corroborates totals.

**Classification ambiguity:** Structured chart coordinates are unavailable; mixed favorable/unfavorable plotting is a possible explanation.

**Exact source locations:** [favorable block table and cumulative chart p.192](../../../../joi180132supp1_prod.pdf#page=192); [July2016 GOSE totals p.191](../../../../joi180132supp1_prod.pdf#page=191).

**Source evidence:** Both titles say favorable GOSE5–8. Y favorable block numerators7,2,11,5,8,6,3,5,6,5,2,4,3,6. Second cumulative Y point lies near12 above10;7+2=9. Page191 prints favorableY73/unfavorableY80.

**Reported-versus-comparator:** Favorable block-count sum versus same-title blue cumulative curve; graphical readings are distinguished from exact printed numerators.

**Reasoning procedure:** Sum numerators, reproduce X, compare an early point with widened graphical uncertainty, and avoid using the accumulated endpoint as the precision anchor.

**Calculation:** Y favorable cumulative7,9,20,25,33,39,42,47,53,58,60,64,67,73. X10,18,20,27,36,41,50,57,62,66,69,78,81,86 reproduces orange X. Y denominator complements sum6,12,17,22,24,30,35,42,50,57,64,69,77,80, compatible with approximate blue readings. Second favorable sum interval[8,10] versus graphical[11,13] leaves gap≥1, conservative relative≥1/13=.076923. Central denominator12 gives .083333, not the lower bound. Endpoint73/near80 is corroboration only because fourteen half-unit inputs can overlap.

**Affected result or extracted value:** Cumulative favorable primary-GOSE Y count/curve in the July2016 monitoring report.

**Why context does not resolve it:** Route A category4: one cumulative method reproduces X while Y differs under the same favorable title. Reconstructed complements do not remove the graph.

**Alternative source-grounded interpretations:** Y may intentionally plot unfavorable counts while X plots favorable, but titles/legend do not define that mixture. Exact graph data are absent.

**Mechanical evidence recheck:** Source images at110/220dpi confirm titles, pairs and early blue point; conservative bounds reproduce. Recheck's REPORT/S_W/statistical_results/reproduced agrees. Arm identity and exact structured series are unavailable. Remaining human question: which outcome and structured series does Y represent?

**Potential downstream evidence impact:** Extraction could copy a graph-derived cumulative count instead of favorable numerator sums or misidentify Y coding. No DSMB reliance or stopping consequence is asserted.

**Evidence-card audit and repair:** Active prose must use REPORT/S_W/statistical_results and lower-bound denominator13. Historical PLAN/P_P wording may remain identified as history. Do not claim exact point labels or endpoint-only qualification.

## C013 — As-treated CT count and percentage ordering

**Candidate statement:** Two normothermia CT category cells do not reconcile with No.(%) and n196.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 eTable10 p.18 internal heading/denominator and Marshall V/VI cells

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Route A category3: within-display counts/denominator/percentages remain separated beyond precision, regardless of reconstructable reversed ordering or otherwise peripheral baseline comparisons.

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Classification rationale:** Heading and cells in one results table give REPORT/S_W/statistical_results; no conflicting plan or separate report is involved.

**Classification ambiguity:** Intended pair ordering remains unspecified.

**Exact source locations:** [eTable10 normothermia CT V/VI cells and headings p.18](../../../../joi180132supp2_prod.pdf#page=18).

**Source evidence:** n196, No.(%); V34.7(68), VI1(2); other categories3(1.5),108(55.1),15(7.7) use count-first order.

**Reported-versus-comparator:** Literal count-first cell readings versus percentage arithmetic and category sum.

**Reasoning procedure:** Compute100×count/denominator with half-unit inputs and sum category-count intervals; consolidate both cells.

**Calculation:** V implies[17.633588,17.774936]% versus[67.5,68.5], gap49.725064/68=.731251. VI implies[.254453,.767263]% versus[1.5,2.5], gap .732737/2=.366368. Literal count sum161.7 interval[159.65,163.75] versus denominator[195.5,196.5] leaves31.75/196=.161990. Reversed counts68/2 and percentages34.7/1 reconcile the category sum196; this is an alternative only.

**Affected result or extracted value:** As-treated normothermia Marshall V/VI counts and proportions.

**Why context does not resolve it:** Route A category3 always registers a reproduced within-display count/denominator/percentage discrepancy even when a likely intended reading is apparent.

**Alternative source-grounded interpretations:** Both cells may use percentage(count) despite the shared count-first heading; no category-specific denominator or presentation exception is stated.

**Mechanical evidence recheck:** Visual page and fresh text confirm both cells/denominator; independent arithmetic reproduces all gaps. S_W/domain/reproduced agree. Remaining human question: which counts/proportions should be taken under the shared heading?

**Potential downstream evidence impact:** Extraction could take literal pairs or reversed readings. No primary-effect or shared-test consequence is inferred without intended values.

**Evidence-card audit and repair:** F-ST1-101 and pass-2 duplicate remain attached to the same two-cell pattern. No additional ID or final replacement is assigned.

## C014 — Adjusted odds-ratio interval token

**Candidate statement:** The adjusted OR interval prints275 between the lower limit and1.64.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.22 adjusted OR and printed confidence-interval tokens

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Route A category2 applies to a source-confirmed printed numerical insertion with competing magnitude readings far beyond precision. It is not solely derivative text or punctuation.

**Finding IDs:** F-ST1-102

**Qualifying route:** Route A, category 2

**Classification rationale:** One completed supplementary results statement gives S_W/statistical_results; the prior unadjusted OR is a different analysis, not a comparator.

**Classification ambiguity:** The intended role of275 is unspecified.

**Exact source locations:** [post hoc adjusted OR statement p.22](../../../../joi180132supp2_prod.pdf#page=22).

**Source evidence:** Adjusted OR0.95(0.55-275 1.64), P=.84, after time-to-randomization adjustment. Prior unadjusted OR0.91(.59–1.41), P=.68 is distinct.

**Reported-versus-comparator:** Undefined275 and1.64 both follow the lower-limit hyphen in a result presented as95% CI.

**Reasoning procedure:** Confirm source numeral and quantify possible upper-limit magnitudes without reconstructing the unavailable adjusted model or inferring the token's origin.

**Calculation:**[274.5,275.5] versus[1.635,1.645] gives gap272.855/1.64=166.375. Both .55–275 and .55–1.64 contain .95/null1; no significance reversal is asserted.

**Affected result or extracted value:** Upper95% confidence limit of the adjusted favorable-outcome OR.

**Why context does not resolve it:** Route A category2 covers a numerical slip changing magnitude; reconstructing the likely two-limit reading does not remove275.

**Alternative source-grounded interpretations:**275 may be an additional insertion and the limits may be .55/1.64; another annotation is possible but undefined locally.

**Mechanical evidence recheck:** Direct-source image and fresh layout confirm275 itself; alternative-limit arithmetic reproduces. Classification/state agree. Adjusted output remains unavailable. Remaining human question: intended upper limit and meaning of275?

**Potential downstream evidence impact:** Extraction could take upper limit275 or1.64. No fitted-model reconstruction, significance conflict or observed downstream use is established.

**Evidence-card audit and repair:** Preserve the token and bounded alternatives; do not silently normalize it or assign a production mechanism. No remaining support omission for the stated observation.

## C015 — Planned adjusted key-secondary sensitivity analyses

**Candidate statement:** Planned covariate-adjusted sensitivity analyses have no matched pneumonia or intracranial-bleeding outputs in the supplied reports.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

Route A category5 applies: final §15.2 explicitly promises adjusted secondary analyses, the abstract makes pneumonia/intracranial bleeding key-secondary under the scope, and complete supplied reporting lacks matched adjusted outputs. Missing analysis presence, not merely missing model detail, is the basis.

**Finding IDs:** F-ST2-201

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective analysis promise versus completed-report absence gives P_R/protocol_report. Other reports corroborate absence; the update supplies context rather than a separate P_P conflict.

**Classification ambiguity:** Full external SAP is unsupplied; no supplied withdrawal of these adjusted outputs is identified.

**Exact source locations:** PLAN [binary models p.84](../../../../joi180132supp1_prod.pdf#page=84), [adjusted primary/secondary promise p.85](../../../../joi180132supp1_prod.pdf#page=85), [update p.183](../../../../joi180132supp1_prod.pdf#page=183), [adjustment footnotes p.184](../../../../joi180132supp1_prod.pdf#page=184), [aligned update p.187](../../../../joi180132supp1_prod.pdf#page=187), [SAP pointer p.181](../../../../joi180132supp1_prod.pdf#page=181). REPORT [abstract p.1](../../../../jama_cooper_2018_oi_180132.pdf#page=1), [outcomes/methods p.3](../../../../jama_cooper_2018_oi_180132.pdf#page=3), [continuation p.4](../../../../jama_cooper_2018_oi_180132.pdf#page=4), [results p.5](../../../../jama_cooper_2018_oi_180132.pdf#page=5), [unadjusted sensitivity pneumonia p.6](../../../../jama_cooper_2018_oi_180132.pdf#page=6), [Table2 p.7](../../../../jama_cooper_2018_oi_180132.pdf#page=7); [eTable6 p.10](../../../../joi180132supp2_prod.pdf#page=10), [eTable9 p.14](../../../../joi180132supp2_prod.pdf#page=14), [eTable11 p.19](../../../../joi180132supp2_prod.pdf#page=19), GOSE outputs [p.16](../../../../joi180132supp2_prod.pdf#page=16), [p.20](../../../../joi180132supp2_prod.pdf#page=20), [p.21](../../../../joi180132supp2_prod.pdf#page=21), [p.22](../../../../joi180132supp2_prod.pdf#page=22). Absence scope: all DOC-001 physical pp.1–10, DOC-003 pp.1–24 and [DOC-004 p.1](../../../../joi180132supp3_prod.pdf#page=1).

**Source evidence:** Plan promises regression sensitivities of primary/secondary outcomes adjusted for prespecified baseline covariates plus any imbalanced covariates. Abstract reports pneumonia55.0%/51.3% and intracranial bleeding18.1%/15.4%. Adjusted labels accompany GOSE, not these adverse-event rows; main p.6 explicitly calls subset pneumonia unadjusted. Updates limit covariates for subset analyses but do not expressly withdraw the final promise.

**Reported-versus-comparator:** Explicit planned adjusted key-secondary sensitivities versus absent matched output, with ordinary unadjusted rows and distinct adjusted GOSE output present.

**Reasoning procedure:** Independently read all supplied final REPORT pages, match outcome/population/adjustment, confirm promise and abstract status, and distinguish absent output from unsupported fitted-model inference. Consolidate both outcomes under one specification.

**Calculation:** Logical comparison: explicit adjusted-secondary promise + named abstract secondary outcomes + no matched supplied adjusted output. Numeric intervals/relative discrepancy are not applicable. No adjusted effect is recomputed or inferred from counts.

**Affected result or extracted value:** Availability and planned-versus-reported status of adjusted pneumonia/intracranial-bleeding sensitivities.

**Why context does not resolve it:** Route A category5: planned key-secondary analysis is not reported. Exploratory interpretation for multiplicity does not withdraw outcome status or adjustment promise.

**Alternative source-grounded interpretations:** Unsupplied SAP could narrow the promise or outputs may exist elsewhere; neither provides supplied-source withdrawal/output. PP/as-treated execution is a distinct specification.

**Mechanical evidence recheck:** Full report/supplement layout, contents and all sensitivity/post hoc outputs independently read; exact plan/update images and adjusted-label placement confirmed. Appended recheck reproduces P_R/domain/state. Missing external SAP and adjusted outputs/covariates remain bounded. Remaining human question: where are these outputs, or which supplied amendment withdrew/narrowed the promise?

**Potential downstream evidence impact:** Extraction could record adjusted sensitivities unavailable or confuse unadjusted outputs with promised adjusted results. No change to estimates or clinical conclusions is asserted.

**Evidence-card audit and repair:** Two outcomes remain one pattern. C006 concerns primary binary OR output, C010 bleeding tuple attribution and C014 a post hoc GOSE interval token: different rules. Complete absence scope and external-SAP limitation must carry to the report.

## Final classification table for the assigned stable IDs

Every row agrees with its audited card. The coordinator must write CONFIRMED to the corresponding ledger rows and retain identical classification values in final report cards. Finding IDs here are the included finding IDs; screened-out duplicate provenance remains separately attached.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C009 | protocol_report | P_R | P_R | REPORT DOC-001 p.4 vs PLAN DOC-002 p.84; PLAN p.188 earlier-version context | reproduced | CONFIRMED | F-XS-003 |
| C010 | statistical_results | S_C | S_C, S_W | REPORT DOC-001 Table2 p.7 vs REPORT DOC-003 eTable6 p.10; REPORT DOC-001 same-display counts/intervals | reproduced | CONFIRMED | F-ST1-002 |
| C011 | plan_material | P_P | P_P | PLAN DOC-002 p.188 internal normal boundary/P threshold; PLAN pp.84,152 method/version context | reproduced | CONFIRMED | F-ST1-205 |
| C012 | statistical_results | S_W | S_W | REPORT observed interim DOC-002 p.192 block table vs cumulative chart; REPORT DOC-002 p.191 corroborates | reproduced | CONFIRMED | F-ST1-301 |
| C013 | statistical_results | S_W | S_W | REPORT DOC-003 eTable10 p.18 internal heading/denominator and Marshall V/VI cells | reproduced | CONFIRMED | F-NUM-101 |
| C014 | statistical_results | S_W | S_W | REPORT DOC-003 p.22 adjusted OR and printed confidence-interval tokens | reproduced | CONFIRMED | F-ST1-102 |
| C015 | protocol_report | P_R | P_R | PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope | reproduced | CONFIRMED | F-ST2-201 |

Assigned partition counts: seven stable IDs; seven CONFIRMED, zero QUESTIONED; seven reproduced. Domains: protocol_report2, plan_material1, statistical_results4, report_internal_inconsistency0. Primary relationships: P_R2, P_P1, S_C1, S_W3. Repeated patterns remain consolidated and all stable IDs preserved.

## Ten original screening-decision audits

The canonical table gives exactly one original decision for each assigned finding. Seven INCLUDE rows and three duplicate rows map to the seven assigned candidates. Decisions were independently checked in both directions; duplicate observations are retained because their locations and provenance support the existing issue.

| Finding ID | Original decision | Reason code | Candidate ID | Independent audit |
|---|---|---|---|---|
| F-NUM-101 | INCLUDE | MEETS_THRESHOLD | C013 | Retain: Route A3, both CT cells source-confirmed; precision gaps .731251/.366368. |
| F-ST1-002 | INCLUDE | MEETS_THRESHOLD | C010 | Retain: Route A4, reproducing neighboring-row method and opposite bleeding tuple pattern, full input-precision gaps confirmed. |
| F-ST1-101 | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C013 | Retain: same V/VI ordering pattern and same display as F-NUM-101; both cells retained in C013. |
| F-ST1-102 | INCLUDE | MEETS_THRESHOLD | C014 | Retain: Route A2,275 printed in source interval, alternative upper-limit magnitude gap reproduced. |
| F-ST1-205 | INCLUDE | MEETS_THRESHOLD | C011 | Retain INCLUDE; repair qualifying-route support to Route B, fixed critical regions and bounded operational ambiguity. |
| F-ST1-301 | INCLUDE | MEETS_THRESHOLD | C012 | Retain: Route A4; source graphical count comparison reproduced with minimum gap1/13; repair active role/domain prose to REPORT/S_W/statistical_results. |
| F-XS-002 | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C010 | Retain: same bleeding attribution pattern, adding cross-report P-copy evidence; no additional stable issue. |
| F-XS-003 | INCLUDE | MEETS_THRESHOLD | C009 | Retain: Route B explicit final critical-rule replacement; zero rounded-copy gap is disclosed, historical charter adds no P_P. |
| F-XS-008 | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 | Retain: same normal boundary/P specification; historical .005 retained as context rather than another simultaneous rule. |
| F-ST2-201 | INCLUDE | MEETS_THRESHOLD | C015 | Retain: Route A5; complete supplied REPORT absence check and abstract key-secondary qualification confirmed; one adjusted-analysis pattern for two outcomes. |

## Individual audit of the 59 assigned checker exclusions

Row references are stable within `checkers/excluded_observations_audit_handoff.md`: NUM2 means numeric table2; ST1-S support table2; ST1-P PLAN table3; ST1-M monitoring table4; XS cross-source table1; ST2-S support table2; ST2-M monitoring table4. Each observation was assessed against all five route A categories before route B and its recorded exclusion code. A descriptive IQR is not an effect confidence interval; missing methodology alone is not a reproduced conflict; different populations or explicitly modeled estimates do not establish matched-result discrepancies. The two duplicate-provenance repairs below preserve original rows and add audit screening rows. No assigned exclusion creates a new distinct stable issue.

| Audit row | Exact observation/location | Original reason code | Audit conclusion and concrete basis |
|---|---|---|---|
| NUM2-01 | DOC-003 p.21, most-likely133/260 versus51.1% | ROUNDING_OR_DISPLAY_PRECISION | Retain: half-unit ratio[50.863724,51.445087]% overlaps[51.05,51.15], gap0, relative0; not A3 beyond precision. |
| NUM2-02 | DOC-003 pp.14,19,22 adjustedRR1.04/1.11,OR.95 versus crude counts | MODEL_VERSUS_CRUDE | Retain: adjusted labels explicit; crude equality not required. C014's independent printed token is separately included, so no A1/A2/A4 conflict is suppressed. |
| NUM2-03 | DOC-003 pp.13–14,18–19 mortality denominators160/195 versus baseline161/196 | CONDITIONAL_OR_UNREPORTED | Retain: no claim every baseline participant has observed mortality; individual displayed count/percentage pairs reconcile. One missing observation does not establish A3 or planned-population conflict. |
| NUM2-04 | DOC-003 p.15 eFigure4,37–41 followed by43–48 | NOTATION_OR_TYPOGRAPHY | Retain: axis bin label with evident six-hour context, no changed displayed count/estimate/CI or identified primary/key output attribution; A2's numeric-result slip not established. |
| ST1-S-01 | DOC-003 pp.16,20,72h AUC cutoff absent locally | CONDITIONAL_OR_UNREPORTED | Retain: numerical cutoff not locally supplied, source points to SAP; no competing threshold or named changed result reproduced. No A5 omission of a planned output established. |
| ST1-S-02 | DOC-003 pp.14,19,PP favorable versus AT unfavorable adjusted labels | CONDITIONAL_OR_UNREPORTED | Retain: different populations/models; missing adjusted model mapping means no same-result reversal reproduced. No crude fitted-effect identity is imposed. |
| ST1-S-03 | DOC-003 p.21,most-likelyRR CI.95–1.06 versus crude diagnostic.85–1.21 | CONDITIONAL_OR_UNREPORTED | Retain: supplied source specifies CMH/stratification/imputation distinct from unadjusted rows; missing strata/pooling prevent a same-engine A4 comparison. CI contains estimate/null and P=.88 is nonsignificant, so no A1 decision conflict. |
| ST1-S-04 | DOC-003 p.21,133/260 versus51.1% | ROUNDING_OR_DISPLAY_PRECISION | Retain: ratio interval[50.863724,51.445087]% overlaps[51.05,51.15]; gap0, relative0. Even exact-count excess .003846/51.1=.0000753≤.05. |
| ST1-P-01 | DOC-002 pp.27,83 versus DOC-001 p.3,80% versus82% power | ROUNDING_OR_DISPLAY_PRECISION | Retain: printed intervals[79.5,80.5]/[81.5,82.5] gap1/82=.012195≤.05; different approximate software contexts do not establish a precise same-method A4 conflict. |
| ST1-P-02 | DOC-002 pp.83–84 versus DOC-001 p.4,.0459 final boundary versus.05 | ROUNDING_OR_DISPLAY_PRECISION | Repair provenance via F-QA-101: copy intervals overlap, but final p.84 explicitly replaces the fixed decision rule. Route B qualifies the already included C009. Audit code DUPLICATE_OF_INCLUDED/C009; preserve original exclusion. |
| ST1-P-03 | DOC-002 p.84 versuspp.85–86,eleven tests versus six occasions | TERMINOLOGY_OR_WORDING | Retain: five occasions×two endpoints plus mortality-only occasion=11 endpoint assessments. Six recruitment looks and eleven endpoint tests are different quantities; no A2 numeric-rule conflict reproduced. |
| ST1-P-04 | DOC-002 pp.15,19,144,deleted ICU-discharge mortality | NOT_REPRODUCED | Retain: visually confirmed V2→V3 amendment expressly deletes this outcome; no simultaneous inconsistent specification or undisclosed A5 status change. |
| ST1-P-05 | DOC-002 pp.15,19,140,72–73,AQOL8 versusSF12 | NOT_REPRODUCED | Retain: source amendment expressly replaces the instrument; supplied documented version change resolves the comparison. A5 is not inferred from a withdrawn version alone. |
| ST1-P-06 | DOC-002 pp.22,78,139,144,148 versus DOC-001 p.4,planned run-in versus8realized | PERIPHERAL_COMPARISON | Retain: documented pilot/run-in changes and realized nonrandomized count do not change randomized primary population or decision rule; A3 local count conflict absent. |
| ST1-P-07 | DOC-002 pp.72–73 versus DOC-001 pp.3–4,secondary versus exploratory interpretation | TERMINOLOGY_OR_WORDING | Retain: report formally defines them secondary; exploratory caution is tied to multiplicity. No A5 outcome-status reassignment is printed. |
| ST1-P-08 | DOC-002 pp.72–73,84 versus DOC-001 p.3,unreported sliding dichotomy/QOL/cost/CACE | PERIPHERAL_COMPARISON | Retain for these named ordinary secondary outputs: no supplied key designation or abstract result. This does not screen the distinct promised adjusted key-secondary AE output, already C015. |
| ST1-P-09 | DOC-002 pp.25,81 versuspp.19,72 and DOC-001 pp.2–3,six-month anchor | CONTEXT_RESOLVES | Retain: injury/randomization separated by≤3h enrollment window, same follow-up/cohort evident. No differently attributed printed primary estimate or changed analysis size/decision is established. |
| ST1-P-10 | DOC-002 p.73 versus DOC-001 p.4,time-to33°C interaction versusχ² association | TERMINOLOGY_OR_WORDING | Retain: within-cooling-arm relationship is explicit; no second factor/test statistic establishing an inferential conflict. No A1 interval/test contradiction. |
| ST1-P-11 | DOC-002 pp.84–85 versus DOC-001 pp.3–4,external SAP covariate list unavailable | CONDITIONAL_OR_UNREPORTED | Retain narrow observation: unavailable exact list alone conflicts with no printed covariate list. C015 independently retains absent promised adjusted key-secondary output. |
| ST1-P-12 | DOC-002 pp.183,187,mapper>48h versus source<48h early-death line | NOT_REPRODUCED | Retain: exact scanned p.187 prints<48h and agrees with update prose; derivative-only transcription discrepancy is not an author-report candidate. |
| ST1-P-13 | DOC-002 pp.183,187,exact48h compliance equality omitted | CONDITIONAL_OR_UNREPORTED | Retain: no supplied participant/result at equality; absent boundary detail alone is not a changed output, test or documented planned-versus-reported rule conflict. |
| ST1-P-14 | DOC-002 pp.85–86 versus DOC-001 p.3,SAE7d aftercessation versusAE10d | NOT_REPRODUCED | Retain: notification/ascertainment of SAEs and predefined10d adverse-event outcomes are different quantities. No matched endpoint-window contradiction. |
| ST1-P-15 | DOC-002 p.132,propofol terminalAUC product formula | PERIPHERAL_COMPARISON | Retain: separate unreported PK substudy, no parent primary/key result or planned decision depends on it. No report output, reproducing display method or effect estimate supplies A1–A5. |
| ST1-P-16 | DOC-002 pp.99–100 versusp.131,propofol passive versusparentactive rewarming | PERIPHERAL_COMPARISON | Retain: separate PK occasion description; no supplied primary/key result relies on this appendix wording. Distinct from ordinary rewarming maximum C004. |
| ST1-P-17 | DOC-002 p.177 versuspp.174–175,V8 adoption dates | PERIPHERAL_COMPARISON | Retain: administrative dates/header versions, no changed statistical decision or population. No A5 output/status change is reproduced. |
| ST1-M-01 | DOC-002 pp.189,191,193,tests/sidedness/score dispersion omitted | CONDITIONAL_OR_UNREPORTED | Retain: these units are observed REPORT by content, not prospective PLAN rules. Means/diagnostic SDs reconcile; no printed interval/statistic/conclusion conflicts. Missing names alone do not qualify A1/A4/B. |
| XS-01 | DOC-001 abstract/Table1,402men versus207+194=401 | ROUNDING_OR_DISPLAY_PRECISION | Retain: count-sum interval[400,402] overlaps402 interval[401.5,402.5], gap0/402=0. Even exact1/402=.002488≤.05; no independent A3 beyond-precision mismatch. |
| XS-02 | DOC-001 methods/Figure3 versus DOC-002 follow-up,injury/randomization anchor | TERMINOLOGY_OR_WORDING | Retain: same cohort and six-month endpoint, enrollment≤3h; no matched result misattribution or different analytic size is established. |
| XS-03 | DOC-001 p.3 versus DOC-002 pp.77,99,100,.25 versus.17 rewarming | CONTEXT_RESOLVES | Repair provenance via F-QA-102: ordinary report ceiling differs from recommended routine plan ceiling; urgent exceptions are separately specified. Route B already C004, audit DUPLICATE_OF_INCLUDED/C004. |
| XS-04 | DOC-001 p.3 versus DOC-002 pp.83–84,power82/80/82.3 andN364/366 | ROUNDING_OR_DISPLAY_PRECISION | Retain:82 interval[81.5,82.5] overlaps82.3[82.25,82.35];80/82 gap1/82=.012195;364/366 gap1/366=.002732; all≤.05. Context distinguishes original/updated designs. |
| XS-05 | DOC-002 pp.152,85,188,secondlook256versus250 | ROUNDING_OR_DISPLAY_PRECISION | Retain: [255.5,256.5]/[249.5,250.5] gap5/250=.02≤.05; no beyond-precision changed monitoring rule remains from the observed look size. |
| XS-06 | DOC-002 pp.84–86,178–179,elevenanalyses versus sixlooks | TERMINOLOGY_OR_WORDING | Retain:5×2+1=11 endpoint assessments across six recruitment occasions; different counting units explain the prose. |
| XS-07 | DOC-002 p.187 versusPD053 apparent>48h | NOT_REPRODUCED | Retain: exact source prints<48h; update/report interpretation cannot use the locator's earlier opposite sign as evidence. |
| XS-08 | DOC-002 p.85 versuspp.183,187,PPallcontrols versusupdatedsubset | CONTEXT_RESOLVES | Retain: supplied update explicitly changes eligibility/compliance subset definitions; an acknowledged operative amendment differs from an unresolved simultaneous P_P conflict. |
| XS-09 | DOC-001 pp.4,8 versus DOC-002 secondary list,exploratoryinterpretation | TERMINOLOGY_OR_WORDING | Retain: formal secondary labels retained, multiplicity caveat changes interpretive caution rather than prespecified status. No A5 status change. |
| XS-10 | DOC-001 p.3 versus DOC-002,unreported sliding/QOL/economics/CACE/SACE/adjustedCox | OUT_OF_FOCUS | Retain for named outputs: no supplied key-secondary designation or abstract mortality/SACE result. Do not generalize exclusion to all secondary analyses; adjusted abstract pneumonia/bleeding omission is separately C015. |
| XS-11 | DOC-003 eTable5 versus DOC-002 survivor outcomes,favorable/unfavorable | TERMINOLOGY_OR_WORDING | Retain: complement within observed survivors is distinguishable from SACE counterfactual target; no same-analysis result with reversed reference/direction established. |
| XS-12 | DOC-001 pp.3,5 versus DOC-002 pp.85–86,AE10d versusSAE7daftercessation | NOT_REPRODUCED | Retain: different event/reporting definitions, no matched-window conflict. |
| XS-13 | DOC-001 abbreviatedeligibility versusfullcriteria,18–60 versus≥18/<60 | TERMINOLOGY_OR_WORDING | Retain: detailed reported criteria match the plan; abridged estimated-age wording supplies no different population/result. |
| XS-14 | Original/finalplan amendments,age/BP/window/AQOL/ICUmortality/run-in/sample | CONTEXT_RESOLVES | Retain: changes expressly documented in supplied amendments; no undisclosed contemporaneous mismatch. Named sample/power rules remain mapped separately. |
| XS-15 | DOC-001 pp.4,8 versus DOC-003 eTable3,never33°C versuswithdrawals | CONTEXT_RESOLVES | Retain: different event/subset definitions are printed. If compared as27%/28.5%, intervals[26.5,27.5]/[28.45,28.55] gap.95/28.5=.033333≤.05; no A3 or beyond-precision matched-copy discrepancy. |
| XS-16 | Main/sensitivity baseline copies acrossITT/PP/AT/dose sets | PERIPHERAL_COMPARISON | Retain: different populations and ordinary baseline descriptions; within-display C013 is independently registered, so exclusion does not suppress A3. |
| XS-17 | Main/supplement temperaturefigures,anchors/populations/medians versusLSmeans | NOT_REPRODUCED | Retain: quantities, time anchors and analysis sets differ; no matched estimate/interval/test conflict is reproduced. |
| XS-18 | DOC-003 eFigure2 versusarticle,logrank.5349versusCox.54 | CONTEXT_RESOLVES | Retain: different named tests. Even a numerical-copy diagnostic gives.5349[.53485,.53495] versus.54[.535,.545] with a tiny .00005/.54=.0000926 gap≤.05; no A1 interval/statistic conflict established. |
| XS-19 | DOC-002 pp.76,92,146,motorwithdrawal<4 versus≤4/wordlabel | TERMINOLOGY_OR_WORDING | Retain: field label identifies withdrawal and source describes clinician suitability, without conflicting analysis-set size or reported outcome value. No printed estimate/count/significance change establishes A2; immediate procedural context resolves the intended motor category. |
| XS-20 | DOC-002 pp.124,168,TEG48and72versus48–72 | TERMINOLOGY_OR_WORDING | Retain: immediate Sample1 text identifies one prewarming sampling window and a fresh sample for a second assay temperature; no supplied key result or decision depends on the table wording. |
| XS-21 | DOC-002 p.131 passivePKrewarming versusparentguide | OUT_OF_FOCUS | Retain: separate substudy occasion with no supplied primary/key output or paired temperature comparison. Not the parent routine-rate rule C004. |
| XS-22 | DOC-002 p.132 terminalAUC formula | OUT_OF_FOCUS | Retain: PK substudy method not used for a supplied parent primary/key result; no printed inferential or count conflict meets A1–A5. |
| XS-23 | DOC-002 pp.174–177,180,dates/sites/calendarcopies | PERIPHERAL_COMPARISON | Retain: administrative copies without changed statistical decision or primary population. Target extension itself is documented, not an undisclosed conflict. |
| XS-24 | DOC-003 pp.8,15,contributors/timebin/displayzeroP | PERIPHERAL_COMPARISON | Retain compound row within its named scope: contributors/time label do not change a primary/key result; display-zero P alone is explicitly excluded. Independent C013/C014 issues are not covered by this row. |
| XS-25 | DOC-002 SAPpointers,externaldepththresholds unavailable | CONDITIONAL_OR_UNREPORTED | Retain narrow observation: absence of local full SAP cannot by itself prove replacement/absence of depth analyses. C015 rests on a supplied explicit adjusted-analysis promise and named missing outputs, not this pointer. |
| ST2-S-01 | DOC-003 pp.16,20,local72hAUCcutoff unavailable | CONDITIONAL_OR_UNREPORTED | Retain: SAP pointer and no competing supplied threshold/result; repeats ST1-S-01 without an A5 omission. |
| ST2-S-02 | DOC-003 pp.14,19,PP/AT adjustedlabels/modelmapping | CONDITIONAL_OR_UNREPORTED | Retain: different fitted models/populations do not reproduce a same-result contradiction; F-XS-009 already has a separate screening record, outside this ten-row assignment. |
| ST2-S-03 | DOC-003 p.21,CMHmostlikelyRR versuscrudeCI | CONDITIONAL_OR_UNREPORTED | Retain: stated different method and unavailable strata/pooling, no A4 same-engine demonstration or A1 null/P decision conflict. |
| ST2-S-04 | DOC-003 p.21,133/260 versus51.1% | ROUNDING_OR_DISPLAY_PRECISION | Retain: [50.863724,51.445087]% overlaps[51.05,51.15]; gap0, relative0. |
| ST2-S-05 | DOC-003 p.15,37–41 axisbin | NOTATION_OR_TYPOGRAPHY | Retain: six-hour chronology identifies the intended bin; no printed estimate/count/CI or named primary/key attribution changes. |
| ST2-S-06 | DOC-003 p.18,MarshallV/VI pairordering | DUPLICATE_OF_INCLUDED | Retain: route A3 issue already C013; both affected cells and all source evidence remain. |
| ST2-S-07 | DOC-003 p.22,adjustedCI275 | DUPLICATE_OF_INCLUDED | Retain: route A2 issue already C014; same source token and result. |
| ST2-M-01 | DOC-002 pp.189,191,193,tabletests/scoredispersion unavailable | CONDITIONAL_OR_UNREPORTED | Retain: observed REPORT content; all available means/diagnosticSD/count-percent pairs reconcile, no printed CI/statistic/conclusion conflict. Missing definitions alone do not meet A1–A5 or B. |

Assigned exclusion counts: NUM2=4, ST1-S=4, ST1-P=17, ST1-M=1, XS=25, ST2-S=7, ST2-M=1; total59. Fifty-seven decisions retained and two duplicate-provenance repairs requested. All exclusions coded ROUNDING_OR_DISPLAY_PRECISION are explicitly checked above against the .05 relative-discrepancy rule; none contains an undisclosed interval/P significance conflict. Earlier PLAN labels on observed monitoring results are corrected in this audit to REPORT by content.

## F-QA-101 — Duplicate closure for the explicit final decision rule

**Origin:** Statistical pass1 excluded table3, row2, ST1-P-02 above. Original row preserves ROUNDING_OR_DISPLAY_PRECISION for .0459 versus .05.

**Exact sources and roles:** PLAN [final V9 §15.1.3 p.84](../../../../joi180132supp1_prod.pdf#page=84) versus REPORT [all-analysis significance rule p.4](../../../../jama_cooper_2018_oi_180132.pdf#page=4). The final plan expressly substitutes ±1.996 SD/P=.0459 rather than ±1.96 SD/P=.05; report says two-sided P<.05 indicates significance for all analyses.

**Reproduction:** Half-unit numeric-copy ranges overlap, gap0. That correctly excludes a simple rounded-copy discrepancy, but does not reconcile the express critical-region replacement. A hypothetical exact .048 satisfies the report rule but not the final planned rule; actual primary .94 satisfies neither. No observed decision reversal is asserted.

**Qualifying route:** Route B. Focus D; nominal-versus-adjusted final testing remains unspecified locally; affected extracted value is final primary-test alpha. Proposed domain protocol_report; primary/all relationships P_R/P_R. Older charter is historical context only.

**Alternative and missing definition:** Nominal .05 reporting could coexist with adjusted final decisions; the supplied report does not state this. Exact operational distinction remains the human question.

**Audit screening decision:** SCREENED_OUT; DUPLICATE_OF_INCLUDED; C009. The same qualifying issue is already registered under F-XS-003, so a second stable ID would duplicate the same rule and location. Preserve the original exclusion and add this sole audit row, retaining F-QA-101 as C009 provenance. Source proof was independently confirmed here; no new stable ID requires appended mechanical recheck.

## F-QA-102 — Duplicate closure for routine rewarming rate

**Origin:** Cross-source excluded table1, row3, XS-03 above. Original CONTEXT_RESOLVES rationale says the report's up-to .25°C/h contains planned .17 and permits urgent faster rates.

**Exact sources and roles:** REPORT [ordinary rewarming target p.3](../../../../jama_cooper_2018_oi_180132.pdf#page=3) versus PLAN [final §12.11 p.77](../../../../joi180132supp1_prod.pdf#page=77), [routine flowchart p.99](../../../../joi180132supp1_prod.pdf#page=99), and [routine management/special considerations p.100](../../../../joi180132supp1_prod.pdf#page=100).

**Reproduction:** Report gives ordinary target up to .25°C/h. Final plan gives .17°C/h and a recommended routine maximum .5°C per3h; appendices repeat .17 and separately permit urgent faster rewarming. Half-hundredth ranges [.245,.255]/[.165,.175] leave gap .070/.17=.411765>.05. A broader ceiling containing the recommended rate does not identify which ordinary maximum governed; emergency exceptions are separately contextualized rather than establishing .25 as the routine plan ceiling.

**Qualifying route:** Route B. Focus D intervention specification; ordinary target versus recommended maximum remains unclear; affected extracted value is routine assigned rewarming-rate specification. Proposed domain protocol_report; primary/all relationships P_R/P_R. The plan wording is a recommendation rather than a universal rigid prohibition.

**Alternative and missing definition:** Broader report ceiling may contain planned routine practice, and urgent departures are allowed. No actual rate adherence, protocol violation or clinical consequence is inferred. Remaining human question: which routine rate specification governed and how does the report's ordinary ceiling relate to the plan recommendation?

**Audit screening decision:** SCREENED_OUT; DUPLICATE_OF_INCLUDED; C004. Main auditor owns that stable card; this narrow source-based exclusion audit independently confirms the same location/rule pattern. Preserve the original row, append the sole audit row and attach F-QA-102 provenance to existing C004. No additional stable ID or new issue is proposed.

### Two requested canonical audit-screen rows

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-QA-101 | quality_control_auditor | audit | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C009 |
| F-QA-102 | quality_control_auditor | audit | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |

These new finding IDs require exactly one screening decision each. Their duplicate decisions retain all source evidence without creating a second stable issue. No original screening decision is overwritten.

## Repair register and remaining field checks

| Repair | Reason and coordinator action |
|---|---|
| C009 active all-relationship prose | Carry P_R alone: the earlier charter describes disclosed historical monitoring context, not a simultaneous conflicting P_P specification. Preserve initial recommendation only as clearly identified history. |
| C011 qualifying route | Carry Route B instead of A1's estimate/interval exemption; retain explicit fixed decision-region comparison, approximate-P alternative and no observed-crossing claim. The ID, P_P/domain and reproduced state remain. |
| C012 active role/domain prose | Carry observed REPORT/S_W/statistical_results despite the bundle's overall PLAN role; preserve initial role recommendation as history. |
| C012 graphical relative bound | Carry1/13=.076923 as conservative minimum;1/12=.083333 is central-reference arithmetic only. Do not rely on endpoint73/near80 after cumulative half-unit allowance. |
| F-QA-101 | Append duplicate audit-screen row for ST1-P-02; the numeric-copy precision screen does not fully close its explicit critical-rule observation, already C009. |
| F-QA-102 | Append duplicate audit-screen row for XS-03; containment of .17 within up-to .25 and emergency exceptions do not close the already registered routine-rule comparison C004. |
| All seven inclusion-audit fields | Write CONFIRMED and the concrete route/reproduction reasons to ledger and final report. |
| Final evidence-card fields | Carry every exact bold label in these seven complete cards, including bounded downstream impact and exact source links. Original ledger summaries are shorter than final-card requirements; the supportable fields are supplied here and in exact-source recheck. |
| Monitoring excluded rows | Interpret DOC-002 pp.189,191,193 as observed REPORT by content; this is a role clarification, with original exclusion provenance preserved. |

No unsupported adjusted-versus-crude equality, exact unreported chart coordinate, observed stopping consequence or causal production mechanism is needed for these seven observations. No unresolved arithmetic discrepancy, false physical pagination or missing assigned source location remains in this shard. The repeated bleeding rows, CT cells, Y curve and two adjusted adverse-event outputs each remain one pattern. Potential evidence impact is confined to named extractable values or reporting availability; no actual propagation or conclusion change is claimed. The two QA findings concern already registered issues, so no additional stable ID or appended-candidate recheck is required.

At this audit point the final report was not yet assembled. Ledger/report identity must be mechanically checked by the coordinator after assembly; the classification table above is the exact seven-row reference. This limitation does not leave assigned source or inclusion work open.

## Reproducibility and limitations

Fresh locator derivatives: `preprocessing/qa-support-main-layout.txt` from DOC-001 physical pp.1–10; `preprocessing/qa-support-plan-layout.txt` from DOC-002 pp.1–194; `preprocessing/qa-support-results-layout.txt` from DOC-003 pp.1–24; `preprocessing/qa-support-sharing-layout.txt` from DOC-004 p.1. Commands were `pdftotext -layout SOURCE OUTPUT` using direct Poppler25.03.0, CPU. No new render, OCR, GPU or fallback environment was needed. The main coordinator already announced CPU processing. Exact visual confirmation used current-run source-matched recheck renders for main pp.7 and supplementary pp.10,18,22; plan pp.84,85,152,188,191,192 and update pp.183,184,187. Source-matched reusable page images confirmed scanned amendments pp.140,144,148. These page images were used as source evidence, not as earlier scientific decisions.

RR/log-Wald and Pearson calculations were independently performed in JavaScript from the printed counts. Half-unit lower-limit extrema enumerate all16 input corners. Normal tails use composite Simpson integration of exp(−x²/2)/sqrt(2π) from the stated z to12 with20000 equal subintervals; omitted mass above12 is negligible for all displayed digits. Direct CT ratios and copied half-unit ranges reproduce the table values above. Reproduction requires only the listed source inputs and formulas, not individual patient data.

Supplied-evidence limitations: full external SAP; operational nominal/adjusted alpha distinction; precise tail/decision convention for approximate charter P; structured chart series and masked-arm identity; adjusted model outputs. They bound explanations and consequences rather than preventing the completed assigned source audit. Parent controls whole-package coverage/execution and later report equality. No source/reusable input was changed.

Closure: seven assigned IDs audited; CONFIRMED7/QUESTIONED0; ten original screening decisions checked; all59 assigned exclusions closed,57 retained and2 duplicate-provenance repairs. Two new audit finding IDs F-QA-101/F-QA-102, zero new distinct stable issues. Canonical merge must return these seven IDs in addition to the main shard's IDs.

Final local checks: all41 PDF evidence links resolve to supplied filenames and truthful physical pages within counts10/194/24/1. Seven candidate headings, seven candidate statements, seven bounded downstream-impact fields and seven CONFIRMED markers reproduce. The59 assigned exclusion rows plus seven candidate headings total66. No prohibited descriptive vocabulary is present.

Fresh locator SHA-256 values:

```text
867457d9166b3f1178904b57b1a750a11cbd8388b2130a8cf20543ca998d39fe  preprocessing/qa-support-main-layout.txt
958fa2aaade2d604962295538a334d7685e26c15dfe22f8c5a85bbf6562e420c  preprocessing/qa-support-plan-layout.txt
03284febe6698e62ae2d047a11b48b7431fa9532a3ad72c60fed1bb8c8cb7609  preprocessing/qa-support-results-layout.txt
687915b05fc55301caa855fed573571a59c4c85d06047c0ba0f7387a9332c2c7  preprocessing/qa-support-sharing-layout.txt
```
