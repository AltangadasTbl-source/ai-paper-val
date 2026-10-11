## C009 — Final significance-rule specification

Pending Human Adjudication

**Candidate statement:** The report's all-analysis .05 rule and final protocol's explicitly substituted .0459 final boundary do not specify the same decision region.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 p.4 vs PLAN DOC-002 p.84; PLAN p.188 earlier-version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route B

**Classification rationale:** Completed-report methods versus prospective final V9 methods supplies P_R alone. The earlier two-look charter is historical context, not a simultaneous P_P conflict.

**Classification ambiguity:** Nominal .05 reporting and operational .0459 testing may coexist, but the supplied report does not establish this distinction.

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 4, REPORT significance paragraph p.4](<../../../jama_cooper_2018_oi_180132.pdf#page=4>); [joi180132supp1_prod.pdf — PDF p. 84, PLAN final §15.1.3 p.84](<../../../joi180132supp1_prod.pdf#page=84>); [joi180132supp1_prod.pdf — PDF p. 188, earlier charter p.188](<../../../joi180132supp1_prod.pdf#page=188>).

**Source evidence:** Report says two-sided P < .05 for all analyses. Final plan says final ±1.996 SD/P = .0459 rather than ±1.96 SD/P = .05 after expanded interim monitoring. The earlier charter gives |Z| ≥ 1.975/P = .048 and alpha .05 for the original two-look design.

**Reported-versus-comparator:** All-analysis .05 versus explicitly replaced final .0459 rule; earlier charter retained as history.

**Reasoning procedure:** Compare explicit decision specifications, separating fixed critical regions from rounded copies and operational consequences from observed results.

**Calculation:** Copy intervals [.04585,.04595] and [.045,.055] overlap: gap 0, relative 0. They cannot establish a copy discrepancy. A hypothetical exact P = .048 meets P < .05 but not P < .0459; it illustrates the different specified regions only. Actual primary P = .94 meets neither.

**Affected result or extracted value:** Final primary-test alpha and its relation to expanded interim monitoring.

**Why context does not resolve it:** The report does not explain whether .05 is nominal reporting accompanied by the adjusted final decision boundary.

**Alternative source-grounded interpretations:** Nominal .05 reporting may coexist with operational .0459 testing; the earlier charter may be superseded by final V9's additional monitoring.

**Mechanical evidence recheck:** Source text, physical pages, roles and fixed-rule comparison confirmed. P_R/domain/reproduced agree with recheck. Actual operational rule and unsupplied SAP clarification remain missing. Remaining human question: which final rule applied, and was nominal reporting distinguished from adjusted decisions?

**Potential downstream evidence impact:** A methods extractor could copy .05 or .0459 as final alpha. No observed significance reversal or downstream conclusion change is established.

## C010 — Bleeding RR, CI and P attribution pattern

Pending Human Adjudication

**Candidate statement:** Main-table bleeding RR/CI/P tuples reproduce the opposite outcome's counts, while the supplement assigns the P values to the other outcomes.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 Table2 p.7 vs REPORT DOC-003 eTable6 p.10; REPORT DOC-001 same-display counts/intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4

**Classification rationale:** Two distinct REPORT documents supply S_C; main-table counts versus intervals supply S_W. S_C precedes S_W. Estimates, intervals and tests require statistical_results despite the attribution component.

**Classification ambiguity:** Separate undisclosed analyses remain possible; document roles are clear.

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 3, unadjusted method p.3](<../../../jama_cooper_2018_oi_180132.pdf#page=3>); [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table2 both bleeding rows p.7](<../../../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable6 both bleeding rows p.10](<../../../joi180132supp2_prod.pdf#page=10>); corroborating [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract p.1](<../../../jama_cooper_2018_oi_180132.pdf#page=1>) and [jama_cooper_2018_oi_180132.pdf — PDF p. 5, narrative p.5](<../../../jama_cooper_2018_oi_180132.pdf#page=5>).

**Source evidence:** Intracranial 47/260 versus 37/240 prints RR 1.23 (.43–3.5), P = .70; extracranial 8/260 versus 6/240 prints RR 1.17 (.79–1.74), P = .43. eTable 6 repeats counts but gives intracranial .43/extracranial .70. Main RD columns reproduce own rows.

**Reported-versus-comparator:** Main RR/CI/P tuples versus own-row count-based calculation and supplementary P assignment.

**Reasoning procedure:** RR=(a/n)/(c/m); SE(logRR)=sqrt(1/a−1/n+1/c−1/m); limits=RR×exp(±1.95996398454×SE). Check stated Pearson equal-proportion diagnostic, neighboring rows and half-unit input corners. Consolidate both rows once.

**Calculation:** Intracranial RR 1.17255717, CI [.79118130,1.73776899], P = .42666956; extracranial RR 1.23076923, CI [.43334502,3.49558164], P = .69603919. Primary, mortality and infection rows reproduce their printed intervals. Half-unit intracranial lower-limit bounds [.76973897,.81321980] versus printed [.425,.435] leave .33473897/.43=.77846; extracranial bounds [.37662053,.49716491] versus [.785,.795] leave .28783509/.79=.36435. P-copy intervals [.695,.705]/[.425,.435] leave .260/.70=.371429 or .260/.43=.604651. Point-RR differences alone are within precision.

**Affected result or extracted value:** Outcome-specific bleeding confidence limits and P values.

**Why context does not resolve it:** Route A category 4: the same reproducing method yields different own-row intervals; immediate reconstruction does not remove the printed values.

**Alternative source-grounded interpretations:** Separate analyses could explain the displays, but the supplied methods do not assign them to these rows or explain exact opposite-row reproduction.

**Mechanical evidence recheck:** Both tables' labels, counts and tuples confirmed visually and in fresh text; bounds reproduced independently. Classification and reproduced state agree. Missing definition: any separate analysis and row mapping. Remaining human question: which RR/CI/P belongs to each outcome, and were separate analyses used?

**Potential downstream evidence impact:** Extraction could associate the wide/narrow interval or .70/.43 with the other bleeding outcome. Both displayed P values exceed .05; no trial-conclusion change is asserted.

## C011 — Interim normal boundary and P threshold

Pending Human Adjudication

**Candidate statement:** A fixed normal |Z| ≥ 3 monitoring rule is paired with approximate P < .001, leaving the operative threshold unclear.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 p.188 internal normal boundary/P threshold; PLAN pp.84,152 method/version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-205

**Qualifying route:** Route B

**Classification rationale:** Prospective charter instructions are PLAN; comparison within that content supplies P_P/plan_material. Final sidedness and the earlier amendment are context, not REPORT relationships or an additional simultaneous version conflict.

**Classification ambiguity:** Approximate P may be shorthand; the intended tail convention and operative rule hierarchy remain unspecified.

**Exact source locations:** [joi180132supp1_prod.pdf — PDF p. 188, charter boundary paragraph p.188](<../../../joi180132supp1_prod.pdf#page=188>); [joi180132supp1_prod.pdf — PDF p. 84, final 3SD/two-sided convention p.84](<../../../joi180132supp1_prod.pdf#page=84>); [joi180132supp1_prod.pdf — PDF p. 152, historical amendment p.152](<../../../joi180132supp1_prod.pdf#page=152>).

**Source evidence:** Conventional three-standard-deviation |Z_k| ≥ 3 boundary, normal approximation to discrete binomial proportions, approximate P < .001. Final V9 uses two-sided tests unless specified. Earlier .005 language is version context.

**Reported-versus-comparator:** Charter's fixed 3 boundary versus literal .001 critical region; not an observed statistic/P pair.

**Reasoning procedure:** Independently integrate the normal tail under the explicitly named approximation; examine both tail conventions and retain approximate wording.

**Calculation:** At 3, one-sided P = .00134989803163 and two-sided P = .00269979606326. Literal two-sided .001 corresponds |Z| > 3.290527; one-sided corresponds Z > 3.090232. Some larger Z values satisfy both descriptions, but the boundaries differ. A fixed rule 3 is not a rounded observed statistic varying over [2.5,3.5]. Numeric-copy interval arithmetic is not applicable to this explicit decision-rule comparison. If approximate P is descriptive shorthand, it remains an alternative rather than an observed conflict.

**Affected result or extracted value:** Interim stopping specification for primary GOSE/mortality.

**Why context does not resolve it:** The source names a normal approximation but does not specify whether 3 SD or literal P < .001 controls operational decisions.

**Alternative source-grounded interpretations:** 3 SD may govern with P shorthand; a discrete calibration may exist, but no replacement boundary is supplied. Earlier .005 may be superseded.

**Mechanical evidence recheck:** Exact source and scanned amendment confirmed; normal tails independently reproduced. P_P/domain/reproduced agree with recheck; route narrowed to B. Missing operational interpretation remains bounded. Remaining human question: which threshold, tail convention and meaning of approximate applied?

**Potential downstream evidence impact:** A methods extractor could record 3 SD or a literal .001 rule. No observed crossing, stopping consequence or treatment identity is inferred.

## C012 — July 2016 cumulative primary-outcome Y series

Pending Human Adjudication

**Candidate statement:** The favorable-GOSE cumulative Y curve does not reproduce favorable block-count sums that reproduce X in the same display.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT observed interim DOC-002 p.192 block table vs cumulative chart; REPORT DOC-002 p.191 corroborates

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-301

**Qualifying route:** Route A, category 4

**Classification rationale:** Both compared displays contain observed outcomes in one supplied PDF, hence S_W/statistical_results. Prospective rules are not a conflicting comparator; p.191 only corroborates totals.

**Classification ambiguity:** Structured chart coordinates are unavailable; mixed favorable/unfavorable plotting is a possible explanation.

**Exact source locations:** [joi180132supp1_prod.pdf — PDF p. 192, favorable block table and cumulative chart p.192](<../../../joi180132supp1_prod.pdf#page=192>); [joi180132supp1_prod.pdf — PDF p. 191, July2016 GOSE totals p.191](<../../../joi180132supp1_prod.pdf#page=191>).

**Source evidence:** Both titles say favorable GOSE 5–8. Y favorable block numerators 7,2,11,5,8,6,3,5,6,5,2,4,3,6. Second cumulative Y point lies near 12 above 10;7+2=9. Page 191 prints favorable Y 73/unfavorable Y 80.

**Reported-versus-comparator:** Favorable block-count sum versus same-title blue cumulative curve; graphical readings are distinguished from exact printed numerators.

**Reasoning procedure:** Sum numerators, reproduce X, compare an early point with widened graphical uncertainty, and avoid using the accumulated endpoint as the precision anchor.

**Calculation:** Y favorable cumulative 7,9,20,25,33,39,42,47,53,58,60,64,67,73. X 10,18,20,27,36,41,50,57,62,66,69,78,81,86 reproduces orange X. Y denominator complements sum 6,12,17,22,24,30,35,42,50,57,64,69,77,80, compatible with approximate blue readings. Second favorable sum interval [8,10] versus graphical [11,13] leaves gap ≥ 1, conservative relative ≥ 1/13=.076923. Central denominator 12 gives .083333, not the lower bound. Endpoint 73/near 80 is corroboration only because fourteen half-unit inputs can overlap.

**Affected result or extracted value:** Cumulative favorable primary-GOSE Y count/curve in the July 2016 monitoring report.

**Why context does not resolve it:** Route A category 4: one cumulative method reproduces X while Y differs under the same favorable title. Reconstructed complements do not remove the graph.

**Alternative source-grounded interpretations:** Y may intentionally plot unfavorable counts while X plots favorable, but titles/legend do not define that mixture. Exact graph data are absent.

**Mechanical evidence recheck:** Source images at 110/220 dpi confirm titles, pairs and early blue point; conservative bounds reproduce. Recheck's REPORT/S_W/statistical_results/reproduced agrees. Arm identity and exact structured series are unavailable. Remaining human question: which outcome and structured series does Y represent?

**Potential downstream evidence impact:** Extraction could copy a graph-derived cumulative count instead of favorable numerator sums or misidentify Y coding. No DSMB reliance or stopping consequence is asserted.

## C013 — As-treated CT count and percentage ordering

Pending Human Adjudication

**Candidate statement:** Two normothermia CT category cells do not reconcile with No.(%) and n = 196.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 eTable10 p.18 internal heading/denominator and Marshall V/VI cells

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Classification rationale:** Heading and cells in one results table give REPORT/S_W/statistical_results; no conflicting plan or separate report is involved.

**Classification ambiguity:** Intended pair ordering remains unspecified.

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 18, eTable10 normothermia CT V/VI cells and headings p.18](<../../../joi180132supp2_prod.pdf#page=18>).

**Source evidence:** n = 196, No.(%); V 34.7 (68), VI 1 (2); other categories 3 (1.5),108 (55.1),15 (7.7) use count-first order.

**Reported-versus-comparator:** Literal count-first cell readings versus percentage arithmetic and category sum.

**Reasoning procedure:** Compute 100×count/denominator with half-unit inputs and sum category-count intervals; consolidate both cells.

**Calculation:** V implies [17.633588,17.774936]% versus [67.5,68.5], gap 49.725064/68=.731251. VI implies [.254453,.767263]% versus [1.5,2.5], gap .732737/2=.366368. Literal count sum 161.7 interval [159.65,163.75] versus denominator [195.5,196.5] leaves 31.75/196=.161990. Reversed counts 68/2 and percentages 34.7/1 reconcile the category sum 196; this is an alternative only.

**Affected result or extracted value:** As-treated normothermia Marshall V/VI counts and proportions.

**Why context does not resolve it:** Route A category 3 always registers a reproduced within-display count/denominator/percentage discrepancy even when a likely intended reading is apparent.

**Alternative source-grounded interpretations:** Both cells may use percentage(count) despite the shared count-first heading; no category-specific denominator or presentation exception is stated.

**Mechanical evidence recheck:** Visual page and fresh text confirm both cells/denominator; independent arithmetic reproduces all gaps. S_W/domain/reproduced agree. Remaining human question: which counts/proportions should be taken under the shared heading?

**Potential downstream evidence impact:** Extraction could take literal pairs or reversed readings. No primary-effect or shared-test consequence is inferred without intended values.

## C014 — Adjusted odds-ratio interval token

Pending Human Adjudication

**Candidate statement:** The adjusted OR interval prints 275 between the lower limit and 1.64.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.22 adjusted OR and printed confidence-interval tokens

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-102

**Qualifying route:** Route A, category 2

**Classification rationale:** One completed supplementary results statement gives S_W/statistical_results; the prior unadjusted OR is a different analysis, not a comparator.

**Classification ambiguity:** The intended role of 275 is unspecified.

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 22, post hoc adjusted OR statement p.22](<../../../joi180132supp2_prod.pdf#page=22>).

**Source evidence:** Adjusted OR 0.95 (0.55-275 1.64), P = .84, after time-to-randomization adjustment. Prior unadjusted OR 0.91 (.59–1.41), P = .68 is distinct.

**Reported-versus-comparator:** Undefined 275 and 1.64 both follow the lower-limit hyphen in a result presented as 95% CI.

**Reasoning procedure:** Confirm source numeral and quantify possible upper-limit magnitudes without reconstructing the unavailable adjusted model or inferring the token's origin.

**Calculation:** [274.5,275.5] versus [1.635,1.645] gives gap 272.855/1.64=166.375. Both .55–275 and .55–1.64 contain .95/null 1; no significance reversal is asserted.

**Affected result or extracted value:** Upper 95% confidence limit of the adjusted favorable-outcome OR.

**Why context does not resolve it:** Route A category 2 covers a numerical slip changing magnitude; reconstructing the likely two-limit reading does not remove 275.

**Alternative source-grounded interpretations:** 275 may be an additional insertion and the limits may be .55/1.64; another annotation is possible but undefined locally.

**Mechanical evidence recheck:** Direct-source image and fresh layout confirm 275 itself; alternative-limit arithmetic reproduces. Classification/state agree. Adjusted output remains unavailable. Remaining human question: intended upper limit and meaning of 275?

**Potential downstream evidence impact:** Extraction could take upper limit 275 or 1.64. No fitted-model reconstruction, significance conflict or observed downstream use is established.

## C015 — Planned adjusted key-secondary sensitivity analyses

Pending Human Adjudication

**Candidate statement:** Planned covariate-adjusted sensitivity analyses have no matched pneumonia or intracranial-bleeding outputs in the supplied reports.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-201

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective analysis promise versus completed-report absence gives P_R/protocol_report. Other reports corroborate absence; the update supplies context rather than a separate P_P conflict.

**Classification ambiguity:** Full external SAP is unsupplied; no supplied withdrawal of these adjusted outputs is identified.

**Exact source locations:** PLAN [joi180132supp1_prod.pdf — PDF p. 84, binary models p.84](<../../../joi180132supp1_prod.pdf#page=84>), [joi180132supp1_prod.pdf — PDF p. 85, adjusted primary/secondary promise p.85](<../../../joi180132supp1_prod.pdf#page=85>), [joi180132supp1_prod.pdf — PDF p. 183, update p.183](<../../../joi180132supp1_prod.pdf#page=183>), [joi180132supp1_prod.pdf — PDF p. 184, adjustment footnotes p.184](<../../../joi180132supp1_prod.pdf#page=184>), [joi180132supp1_prod.pdf — PDF p. 187, aligned update p.187](<../../../joi180132supp1_prod.pdf#page=187>), [joi180132supp1_prod.pdf — PDF p. 181, SAP pointer p.181](<../../../joi180132supp1_prod.pdf#page=181>). REPORT [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract p.1](<../../../jama_cooper_2018_oi_180132.pdf#page=1>), [jama_cooper_2018_oi_180132.pdf — PDF p. 3, outcomes/methods p.3](<../../../jama_cooper_2018_oi_180132.pdf#page=3>), [jama_cooper_2018_oi_180132.pdf — PDF p. 4, continuation p.4](<../../../jama_cooper_2018_oi_180132.pdf#page=4>), [jama_cooper_2018_oi_180132.pdf — PDF p. 5, results p.5](<../../../jama_cooper_2018_oi_180132.pdf#page=5>), [jama_cooper_2018_oi_180132.pdf — PDF p. 6, unadjusted sensitivity pneumonia p.6](<../../../jama_cooper_2018_oi_180132.pdf#page=6>), [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table2 p.7](<../../../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable6 p.10](<../../../joi180132supp2_prod.pdf#page=10>), [joi180132supp2_prod.pdf — PDF p. 14, eTable9 p.14](<../../../joi180132supp2_prod.pdf#page=14>), [joi180132supp2_prod.pdf — PDF p. 19, eTable11 p.19](<../../../joi180132supp2_prod.pdf#page=19>), GOSE outputs [joi180132supp2_prod.pdf — PDF p. 16, p.16](<../../../joi180132supp2_prod.pdf#page=16>), [joi180132supp2_prod.pdf — PDF p. 20, p.20](<../../../joi180132supp2_prod.pdf#page=20>), [joi180132supp2_prod.pdf — PDF p. 21, p.21](<../../../joi180132supp2_prod.pdf#page=21>), [joi180132supp2_prod.pdf — PDF p. 22, p.22](<../../../joi180132supp2_prod.pdf#page=22>). Absence scope: all DOC-001 physical pp.1–10, DOC-003 pp.1–24 and [joi180132supp3_prod.pdf — PDF p. 1, DOC-004 p.1](<../../../joi180132supp3_prod.pdf#page=1>).

**Source evidence:** Plan promises regression sensitivities of primary/secondary outcomes adjusted for prespecified baseline covariates plus any imbalanced covariates. Abstract reports pneumonia 55.0%/51.3% and intracranial bleeding 18.1%/15.4%. Adjusted labels accompany GOSE, not these adverse-event rows; main p.6 explicitly calls subset pneumonia unadjusted. Updates limit covariates for subset analyses but do not expressly withdraw the final promise.

**Reported-versus-comparator:** Explicit planned adjusted key-secondary sensitivities versus absent matched output, with ordinary unadjusted rows and distinct adjusted GOSE output present.

**Reasoning procedure:** Independently read all supplied final REPORT pages, match outcome/population/adjustment, confirm promise and abstract status, and distinguish absent output from unsupported fitted-model inference. Consolidate both outcomes under one specification.

**Calculation:** Logical comparison: explicit adjusted-secondary promise + named abstract secondary outcomes + no matched supplied adjusted output. Numeric intervals/relative discrepancy are not applicable. No adjusted effect is recomputed or inferred from counts.

**Affected result or extracted value:** Availability and planned-versus-reported status of adjusted pneumonia/intracranial-bleeding sensitivities.

**Why context does not resolve it:** Route A category 5: planned key-secondary analysis is not reported. Exploratory interpretation for multiplicity does not withdraw outcome status or adjustment promise.

**Alternative source-grounded interpretations:** Unsupplied SAP could narrow the promise or outputs may exist elsewhere; neither provides supplied-source withdrawal/output. PP/as-treated execution is a distinct specification.

**Mechanical evidence recheck:** Full report/supplement layout, contents and all sensitivity/post hoc outputs independently read; exact plan/update images and adjusted-label placement confirmed. Appended recheck reproduces P_R/domain/state. Missing external SAP and adjusted outputs/covariates remain bounded. Remaining human question: where are these outputs, or which supplied amendment withdrew/narrowed the promise?

**Potential downstream evidence impact:** Extraction could record adjusted sensitivities unavailable or confuse unadjusted outputs with promised adjusted results. No change to estimates or clinical conclusions is asserted.

