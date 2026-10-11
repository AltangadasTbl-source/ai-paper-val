# Mechanical Evidence Recheck — Part 002

Scope: C019, C020, C021, C022, C023, C024, C025, C026, C027, C028, C029, C030, C031. Every ID remains Pending Human Adjudication. Source values were read visually on freshly rendered exact supplied PDF pages; layout text was only a locator. No legacy audit, external source, GPU, or custom Python was used.

Derivative engine: direct Poppler pdftoppm 25.03.0, PNG at 105 dpi, and direct pdftotext 25.03.0 with layout preservation. Unique derivatives are under `preprocessing/recheck002/`. Exactly 32 distinct source pages were rendered and visually inspected: main REPORT pp. 1, 3, 4, 7; results REPORT supplement p. 3; PLAN supplement pp. 10, 12, 21, 24, 25, 33, 36, 37, 47, 49, 52, 65, 66, 67, 72, 76, 79, 80, 87, 90, 91, 103, 112, 121, 124, 130, 133. Repeated summary p. 11 is not needed as an authoritative comparator for C030; the original full decision rule is confirmed at p. 37. All three direct-source hashes match the coordinator's before hashes. Direct awk arithmetic is saved in `preprocessing/recheck002/calculations.txt`.

Evidence-state summary: recorded_candidate 10; record_input_error 2; not_reproduced 1; repaired_residual 0. No category, document-role, or relationship-type changes are required. C021/C023 retain their registered comparison classification while its same-operation premise is unsupported; classification records the comparison and does not establish a discrepancy.

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C019 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN original/later protocol monthly accrual versus PLAN duration and targets | plan_material | recorded_candidate | retain |
| C020 | Measure, label, or scale inconsistency | P_P | P_P | PLAN IDS neurological-purpose sentence versus PLAN IDS procedural construct definition | plan_material | recorded_candidate | retain |
| C021 | Measure, label, or scale inconsistency | P_P | P_P | PLAN IDS CRF collection wording versus PLAN prehospital assessment chronology | plan_material | record_input_error | discuss |
| C022 | Measure, label, or scale inconsistency | P_P | P_P | PLAN VAS neurological-purpose sentence versus PLAN VAS procedural construct definition | plan_material | recorded_candidate | retain |
| C023 | Measure, label, or scale inconsistency | P_P | P_P | PLAN VAS CRF collection wording versus PLAN prehospital assessment chronology | plan_material | record_input_error | discuss |
| C024 | Statistical reporting inconsistency | P_P | P_P | PLAN image SAP positive alternative threshold versus PLAN native SAP negative threshold and PLAN image SAP CI rule | plan_material | recorded_candidate | retain |
| C025 | Measure, label, or scale inconsistency | P_P | P_P | PLAN IDS impossible category coding versus PLAN attained-score calculation rule | plan_material | recorded_candidate | retain |
| C026 | Cross-document numeric inconsistency | P_R | P_R | PLAN historical TI percentage versus REPORT main historical TI percentage | protocol_report | recorded_candidate | retain |
| C027 | Measure, label, or scale inconsistency | P_R | P_R | REPORT main centre-number/site label versus PLAN trial roster number/site label | protocol_report | recorded_candidate | retain |
| C028 | Numeric or arithmetic inconsistency | S_C | S_C | REPORT main primary favorable-survivor counts versus REPORT results supplement regrouped counts | statistical_results | recorded_candidate | retain |
| C029 | Cross-document numeric inconsistency | P_P | P_P | PLAN later consolidated body centre total versus PLAN centre amendment total | plan_material | recorded_candidate | retain |
| C030 | Statistical reporting inconsistency | P_P | P_P | PLAN protocol/SAP inclusive hypothesis sets versus PLAN strict CI rule | plan_material | recorded_candidate | retain |
| C031 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT main primary inputs versus derived arithmetic from same REPORT inputs | statistical_results | not_reproduced | exclude |

Suggested review disposition is a mechanically derived human-review pre-fill, never an adjudication.

## C019 — Protocol monthly accrual does not multiply to its total target

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Original summary [PLAN PDF p. 10](../../../joi180004supp1_prod.pdf#page=10), original §6.3 table [p. 24](../../../joi180004supp1_prod.pdf#page=24), later summary [p. 65](../../../joi180004supp1_prod.pdf#page=65) and [p. 66](../../../joi180004supp1_prod.pdf#page=66), and later §6.3 table [p. 79](../../../joi180004supp1_prod.pdf#page=79) were visually inspected.
2. **Source value/text matched:** Yes. Tables print 2000 subjects, 20 centres, 24 months, 100 subjects/centre, and 5 subjects/centre/month. The summary gives the same expected numbers, with the later summary split across pp. 65–66.
3. **Comparator matched:** Yes. Monthly rate, calendar inclusion period, centre count, and total/per-centre targets are adjacent same-schedule inputs in §6.3.
4. **Consistency rule applicable:** Applicable conditionally to a constant exact monthly accrual rate across all 24 inclusion months and all 20 centres. It is not a rule that an aspirational rounded monthly target must equal a minimum final sample size.
5. **Calculation or logical comparison reproduced:** Direct awk: 20×100=2000; 5×24=120 per centre; 5×24×20=2400. A 100-patient target over 24 active months requires 4.166666667/month; 100/5=20 active months. The literal exact-rate interpretation does not reconcile.
6. **Necessary inputs available:** All displayed arithmetic inputs are available. **Exact missing inputs or definitions:** Whether 5/month is rounded, aspirational, or applies only to active recruitment months; whether all centres accrue simultaneously for all 24 months; whether 2000 is a minimum rather than an exact operational total.
7. **Source-grounded alternative interpretation:** The table is headed recruitment methods and its summary calls the values expected inclusions. An operational target may exceed the minimum sample-size target, or individual centres may recruit for fewer than 24 calendar months. These possibilities are not specified quantitatively.
8. **Direct observation versus inferred explanation:** Direct: the five numbers are printed together. Derived: the product is 2400. Inferred and unconfirmed: a shorter active schedule or aspirational rate explains the difference.
9. **Exact remaining human question:** Does 5/month/centre apply to 20 active months, represent an approximate recruitment aspiration, or imply a different centre-specific accrual schedule from the stated 24-month inclusion period?
10. **Document role of every comparator:** All five cited locations are PLAN by content: prospective protocol recruitment methods/summary. Neither later actual enrolment nor a report is part of this mismatch.
11. **Classification confirmation:** Category Numeric or arithmetic inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** The comparison is entirely among prospective planning numbers inside the bound protocol bundle. **Classification ambiguity:** Rate and duration semantics are unspecified, but document roles are clear. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. Visual confirmation reproduces the printed product discrepancy under the named exact-rate interpretation; operational definitions remain for human review. **Suggested review disposition:** retain.

## C020 — IDS described as a day 28 neurological-function scale

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. §7.2 [PLAN PDF p. 25](../../../joi180004supp1_prod.pdf#page=25) and repeated [p. 80](../../../joi180004supp1_prod.pdf#page=80); §7.1.2 IDS definition [p. 24](../../../joi180004supp1_prod.pdf#page=24) and repeated [p. 79](../../../joi180004supp1_prod.pdf#page=79), all visually inspected.
2. **Source value/text matched:** Yes. §7.2 includes IDS, VAS, mRS and primary endpoint CPC in the statement that they are used for assessment of neurologic function at day 28.
3. **Comparator matched:** Yes. §7.1.2 defines IDS as a quantitative measure of intubation complexity based on seven airway difficulty parameters, including attempts, operators, alternative techniques, laryngoscopic grade, lifting force, laryngeal manipulation, and vocal cord position.
4. **Consistency rule applicable:** Applicable to the printed measurement-construct label. A named score defined as procedural difficulty is not thereby a neurological-function score. This observation does not question why procedural data are collected in the trial.
5. **Calculation or logical comparison reproduced:** Logical identity comparison: the seven listed IDS components quantify intubation difficulty; none is a day 28 neurologic-function rating. §7.1.4–5 separately assigns mRS/CPC to day 28 disability/neurological outcome.
6. **Necessary inputs available:** Named scale and both construct statements are available. **Exact missing inputs or definitions:** Whether the collective §7.2 sentence is intended to describe every listed scale's construct individually or the trial's assessment programme collectively; no transformation from IDS to neurological function is given.
7. **Source-grounded alternative interpretation:** §7.2 is a timetable/assessment-methods section and may summarize a set of trial-specific measures serving the overall day 28 assessment programme. Its collective sentence can be loose framing rather than a literal redefinition of IDS.
8. **Direct observation versus inferred explanation:** Direct: IDS appears in the neurologic-function sentence and has an airway-complexity definition. Derived: those literal constructs differ. Inferred and unconfirmed: collective phrasing or template wording caused the mismatch.
9. **Exact remaining human question:** Is the §7.2 neurologic-function phrase intended to characterize IDS itself, or the trial assessment programme, and how should the IDS construct be extracted?
10. **Document role of every comparator:** All four locations are PLAN: prospective protocol definitions and timetable text, including the later version.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** A protocol's scale-purpose sentence is compared with its protocol definition. **Classification ambiguity:** Collective programme purpose versus individual scale label. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. Both conflicting literal construct descriptions are present, with sentence scope remaining an explicit interpretation question. **Suggested review disposition:** retain.

## C021 — IDS collection time versus prehospital chronology

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. §10.2 [PLAN PDF p. 33](../../../joi180004supp1_prod.pdf#page=33) and repeated [p. 87](../../../joi180004supp1_prod.pdf#page=87); chronology tables [p. 21](../../../joi180004supp1_prod.pdf#page=21) and [p. 76](../../../joi180004supp1_prod.pdf#page=76), all visually inspected.
2. **Source value/text matched:** Yes, with a critical distinction. The source says CPC scale data, mRS, IDS and VAS are “collected directly from the CRF at day 28 (+7 days).” It does not say IDS is measured anew at that time.
3. **Comparator matched:** Yes. IDS has an X in enrolment/out-of-hospital period and blank in-hospital and 28-day columns. Page 87 also lists IDS among procedural data preceding the separate in-hospital and day 28 sections; the day 28 follow-up list names CPC/mRS, not IDS.
4. **Consistency rule applicable:** The registered same-operation timing rule is not established. Measurement/assessment and collection from an existing CRF are different operations; equating them requires an additional definition absent from the source.
5. **Calculation or logical comparison reproduced:** The two literal time phrases are reproduced, but the alleged contradictory timing for the same operation is not. Prehospital IDS assessment can coexist with later CRF retrieval. The labels alone do not establish that retrieval occurred, nor establish contradictory measurement times.
6. **Necessary inputs available:** Scale name, chronology X, and day 28 CRF wording are available. **Exact missing inputs or definitions:** The operational meaning of “collected directly from the CRF”; when IDS was first assessed/entered; whether §10.2 describes later data extraction or an erroneous measurement timetable.
7. **Source-grounded alternative interpretation:** The phrase “from the CRF,” the source-data heading, the procedural definition, and the page 87 separation of procedural from follow-up data support a later retrieval/collection reading. This is grounded in wording, not an invented clinical process.
8. **Direct observation versus inferred explanation:** Direct: distinct chronology and CRF-collection statements. Unsupported inference in registration: they identify the same measurement operation. Possible but unconfirmed explanation: data retrieval at day 28 from an earlier procedural record.
9. **Exact remaining human question:** Does §10.2 describe later collection of an earlier IDS record, or does it intend a day 28 IDS assessment? Confirm the first assessment, entry and retrieval times separately.
10. **Document role of every comparator:** All four locations are PLAN protocol chronology/source-data procedures; all roles confirmed by content.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** The registered timing comparison lies wholly within prospective protocol content. **Classification ambiguity:** The two operations cannot be aligned from supplied wording. No role/type change; the comparison's alignment premise changes its evidence state.
12. **Evidence state and determining fact:** record_input_error. The registered mismatch equates CRF collection with prehospital assessment without source support, and the residual wording question cannot be settled from the package. **Suggested review disposition:** discuss.

## C022 — VAS described as a day 28 neurological-function scale

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. §7.2 [PLAN PDF p. 25](../../../joi180004supp1_prod.pdf#page=25) and [p. 80](../../../joi180004supp1_prod.pdf#page=80), versus §7.1.3 [p. 24](../../../joi180004supp1_prod.pdf#page=24) and [p. 79](../../../joi180004supp1_prod.pdf#page=79), all visually inspected.
2. **Source value/text matched:** Yes. VAS is included with IDS, mRS and CPC in the sentence describing assessment of neurologic function at day 28.
3. **Comparator matched:** Yes. §7.1.3 states that the investigator directly evaluates bag-valve-mask ventilation difficulty using a Visual Analog Scale, a subjective-measurement instrument. These exact cited paragraphs do not themselves print a 0–100 range; that extra range is unnecessary for this comparison.
4. **Consistency rule applicable:** Applicable to the literal construct label: mask ventilation difficulty and neurological function are distinct specified constructs, even when both contribute to a trial assessment programme.
5. **Calculation or logical comparison reproduced:** Logical identity comparison: VAS is defined to measure procedural mask ventilation difficulty, while §7.2 collectively attributes neurologic-function assessment at day 28. The direct mismatch is in purpose wording, not a numeric scale-range calculation.
6. **Necessary inputs available:** Both construct descriptions and VAS identity are available. **Exact missing inputs or definitions:** Scope of the collective §7.2 statement; whether it is a programme-level description rather than a per-scale label. No neurological transformation of the ventilation VAS is supplied.
7. **Source-grounded alternative interpretation:** The assessment-methods section may list all research-specific scales and describe their contribution to the overall trial programme collectively. That would preserve the separately explicit procedural definition.
8. **Direct observation versus inferred explanation:** Direct: ventilation-difficulty definition and neurologic-function sentence. Derived: different literal construct labels. Unconfirmed inference: broad collective wording accounts for the difference.
9. **Exact remaining human question:** Does §7.2 assign a neurological construct to the ventilation VAS, or describe the assessment programme collectively, and which purpose should a data extractor record?
10. **Document role of every comparator:** All four locations are PLAN prospective protocol definitions/assessment timetable; later version does not change role.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** Internal protocol purpose/definition comparison, distinct from the IDS scale comparison C020. **Classification ambiguity:** Individual construct versus collective programme framing. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. The cited procedural and neurological-purpose phrases are reproduced directly; a sentence-scope interpretation remains. **Suggested review disposition:** retain.

## C023 — VAS collection time versus prehospital chronology

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. §10.2 [PLAN PDF p. 33](../../../joi180004supp1_prod.pdf#page=33) and [p. 87](../../../joi180004supp1_prod.pdf#page=87); chronology [p. 21](../../../joi180004supp1_prod.pdf#page=21) and [p. 76](../../../joi180004supp1_prod.pdf#page=76), all visually inspected.
2. **Source value/text matched:** Yes. VAS appears in the sentence saying data are collected directly from the CRF at day 28 (+7 days). The sentence does not state a new day 28 ventilation difficulty measurement.
3. **Comparator matched:** Yes. VAS for ventilation difficulty with bag-valve is marked only in the enrolment/out-of-hospital period. Page 87 separately lists ventilation VAS among procedural data, while its day 28 follow-up list contains CPC and mRS.
4. **Consistency rule applicable:** Not established for the registered same-operation contradiction: collection from a CRF is not necessarily the original investigator assessment marked in chronology.
5. **Calculation or logical comparison reproduced:** The distinct literal time descriptions are found. Their alignment as two incompatible times for one VAS measurement is unsupported. An earlier assessment subsequently collected from its record fits the supplied distinction, although the workflow is not defined completely.
6. **Necessary inputs available:** VAS identity, out-of-hospital X and day 28 CRF wording are available. **Exact missing inputs or definitions:** First VAS assessment/entry time and the meaning of later collection from the CRF; whether §10.2 is retrieval wording or a timetable error.
7. **Source-grounded alternative interpretation:** “From the CRF” and the source-data section heading permit later data retrieval; procedural VAS content and the distinct page 87 follow-up list support separating retrieval from assessment.
8. **Direct observation versus inferred explanation:** Direct: chronology assignment and CRF-collection statement. Unsupported inference: both denote the same measurement event. Unconfirmed but source-grounded alternative: prehospital measurement followed by day 28 collection from the record.
9. **Exact remaining human question:** Is day 28 (+7) the retrieval time for an earlier VAS record or an intended VAS assessment time? Confirm assessment, entry and collection as separate operations.
10. **Document role of every comparator:** All four locations are PLAN prospective protocol chronology and source-data procedures, confirmed by content.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** A protocol-internal timing comparison, separate from the IDS record C021. **Classification ambiguity:** Same-operation alignment is not supplied. No category/role/type change.
12. **Evidence state and determining fact:** record_input_error. The registered comparison rests on an unsupported alignment of measurement with CRF collection; the package cannot determine the residual interpretation. **Suggested review disposition:** discuss.

## C024 — Image SAP alternative uses positive rather than negative NI margin

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Image SAP §4.1 [PLAN PDF p. 130](../../../joi180004supp1_prod.pdf#page=130), native-text SAP §4.1 [p. 121](../../../joi180004supp1_prod.pdf#page=121), and image SAP §8.2.1 [p. 133](../../../joi180004supp1_prod.pdf#page=133), all visually inspected, including the signs.
2. **Source value/text matched:** Yes. Image SAP H0 reads πBVM−πTI≤−0.01, but H1 reads πBVM−πTI≥0.01 without a minus sign before 0.01. A printed leading plus is not present; “positive” means the unsigned positive number.
3. **Comparator matched:** Yes. Native-text SAP H1 reads πBVM−πTI≥−0.01. Image SAP decision rule requires the CI lower limit higher than −0.01. Both SAP pages show the same 18.FEB.2015 date and Page 5 of 9 for §4.1.
4. **Consistency rule applicable:** Literal sign/value identity is applicable to the same contrast, endpoint and SAP section. Sign comparison needs no estimator or variance assumption. This is distinct from the shared-inclusive-boundary issue C030.
5. **Calculation or logical comparison reproduced:** Direct awk: 0.01−(−0.01)=0.02 probability units=2 percentage points. At d=0, the image alternative d≥0.01 is false while the native-text alternative d≥−0.01 is true. The image hypothesis pair leaves −0.01<d<0.01 in neither printed set.
6. **Necessary inputs available:** Contrast, threshold signs, endpoint and same SAP section/date are printed. **Exact missing inputs or definitions:** Whether image H1 deliberately specifies superiority by +1 percentage point, or has a missing minus sign; which supplied SAP representation governed implementation.
7. **Source-grounded alternative interpretation:** An omitted minus sign in the scan/text representation is consistent with its own −0.01 CI rule and the parallel native-text SAP. A deliberately stronger alternative would require an explanation not given here.
8. **Direct observation versus inferred explanation:** Direct: positive image threshold versus negative native threshold/CI margin. Derived: 2-percentage-point separation and uncovered interval. Inferred and unconfirmed: missing-sign production error.
9. **Exact remaining human question:** Is image SAP H1 intended to use −0.01 or intentionally +0.01, and how does that threshold relate to its printed −0.01 CI decision rule?
10. **Document role of every comparator:** All three pages are PLAN prospective statistical analysis plan content. The native-text version corroborates the negative margin and conflicts with image H1; a report is unnecessary to establish this observation.
11. **Classification confirmation:** Category Statistical reporting inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** The substantive discrepancy is within/between SAP representations in one bound plan bundle. **Classification ambiguity:** Representation/sign intent; roles clear. No classification change or P_R addition.
12. **Evidence state and determining fact:** recorded_candidate. Direct visual inspection confirms the absent minus in image H1 and the negative margin in the comparator and decision rule. **Suggested review disposition:** retain.

## C025 — IDS impossible-intubation score has two printed coding rules

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Original IDS appendix [PLAN PDF p. 52](../../../joi180004supp1_prod.pdf#page=52) and repeated appendix [p. 103](../../../joi180004supp1_prod.pdf#page=103), both visually inspected.
2. **Source value/text matched:** Yes. The difficulty table's IDS Score column reads “IDS = ∞” for “Impossible intubation.”
3. **Comparator matched:** Yes. On the same page the Rules for Calculating IDS Score table states: “Impossible intubation: IDS takes the value attained before abandonment of intubation attempts.” The component table labels total IDS as the sum of scores N1–N7.
4. **Consistency rule applicable:** Applicable to numeric coding if both rows prescribe the stored IDS score for the same impossible/abandoned procedure. Infinity and a finite attained sum are distinct values, without rounding tolerance.
5. **Calculation or logical comparison reproduced:** The rules add finite points for a finite number of attempts/operators/alternative techniques, plus bounded procedural contributions. An attained finite sum therefore differs from ∞. No observed participant score was supplied or reconstructed.
6. **Necessary inputs available:** Both coding statements and finite sum rule are printed. **Exact missing inputs or definitions:** Whether ∞ is an outcome/difficulty-category sentinel while the attained sum is a separate numeric field; whether a special override exists for abandoned procedures.
7. **Source-grounded alternative interpretation:** The upper table is a Degree of Difficulty classification and the lower table is a calculation rule. They could designate a conceptual impossible category and a separately recorded attained numerical score, but both are labeled IDS and no separate fields are defined.
8. **Direct observation versus inferred explanation:** Direct: ∞ category row and attained-score rule on the same page. Derived: finite attained sum differs from an infinity sentinel. Inferred and unconfirmed: two different data fields resolve the wording.
9. **Exact remaining human question:** For abandoned impossible intubation, is the recorded IDS the finite attained sum, ∞, or two separately labeled fields, and what rule distinguishes them?
10. **Document role of every comparator:** Both original/repeated appendices are PLAN scale-coding instructions inside prospective protocol material.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** All substantive coding comparators are plan-internal. **Classification ambiguity:** Category sentinel versus stored numeric value. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. Both numerical coding descriptions are visually confirmed; their data-field relationship remains undefined. **Suggested review disposition:** retain.

## C026 — Matched historical TI percentage differs between plan and report

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Protocol background [PLAN PDF p. 12](../../../joi180004supp1_prod.pdf#page=12) and repeated [p. 67](../../../joi180004supp1_prod.pdf#page=67); main sample-size background [REPORT PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3) and discussion [p. 7](../../../jama_jabre_2018_oi_180004.pdf#page=7), all visually inspected.
2. **Source value/text matched:** Yes. Both protocol versions describe Hasegawa's 649,359-patient Japanese study and 30-day neurologically favorable survival of 2.9% among 367,837 BMV patients versus 1.0% among 41,972 TI patients.
3. **Comparator matched:** Yes. Main p. 7 describes the same 649,359 Japanese study, favorable functional survival, and TI versus BMV as 1.1% versus 2.9%. Main p. 3 gives approximately 650,000 and a TI rate of 1.1%, with BMV rounded to 3% and an OR 0.38 (0.36–0.39).
4. **Consistency rule applicable:** Matched printed historical percentage identity is supported by study attribution, exact p. 7 cohort total, airway strategies and BMV rate. An exact statistical contradiction still depends on TI subset/endpoint/unadjusted-versus-adjusted alignment not fully printed in the report.
5. **Calculation or logical comparison reproduced:** Direct awk: 1.1−1.0=0.1 percentage point. These are distinct one-decimal printed TI percentages for the closely matched historical comparison. At a rounding-bin boundary, differing rounding conventions could explain adjacent labels; a single policy would not produce both.
6. **Necessary inputs available:** Attributed study, total cohort, airway strategies and printed percentages are available. **Exact missing inputs or definitions:** TI favorable-survivor count, report TI denominator, exact endpoint horizon in the report discussion, and whether both percentages are the same unadjusted quantity with the same rounding rule.
7. **Source-grounded alternative interpretation:** Main p. 3 also prints an odds ratio, and p. 7 discusses robustness after confounder adjustment. Either the selected historical statistic or rounding may differ; the supplied article does not explicitly identify a different percentage population/statistic for 1.1%.
8. **Direct observation versus inferred explanation:** Direct: printed TI 1.0% and 1.1%, same attributed study and supporting identifiers. Derived: 0.1-point difference. Unconfirmed inference: different adjustment, subset or rounding explains it.
9. **Exact remaining human question:** Do 1.0% and 1.1% refer to the same historical TI cohort, favorable-neurological-survival horizon and unadjusted percentage, and what event count/statistic/rounding accounts for the difference?
10. **Document role of every comparator:** Protocol pp. 12/67 are PLAN even though they present historical data inside prospective background. Main pp. 3/7 are REPORT article background/discussion content.
11. **Classification confirmation:** Category Cross-document numeric inconsistency; relationship type P_R; all relationships P_R; review domain protocol_report. **Classification rationale:** The substantive historical percentage discrepancy crosses PLAN and REPORT content. The two report occurrences corroborate 1.1%; the two plan versions corroborate 1.0%, adding no other relationship. **Classification ambiguity:** Exact statistic alignment/rounding remains conditional. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. Visual source inspection reproduces the closely matched printed percentages, with the missing historical statistic definitions explicitly bounded. **Suggested review disposition:** retain.

## C027 — Numeric center identifier 5 assigned inconsistent site

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Main Outcomes [REPORT PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), trial centre roster [PLAN PDF p. 47](../../../joi180004supp1_prod.pdf#page=47) and [p. 49](../../../joi180004supp1_prod.pdf#page=49). Main numerical CPR subset [REPORT p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4) was also visually inspected.
2. **Source value/text matched:** Yes. Main p. 3 says investigative “Center No. 5: Saint Pierre.” Main p. 4 identifies 115 patients from center No. 5, with 56 BMV and 59 ETI patients.
3. **Comparator matched:** Yes. Original roster p. 47 assigns Center 05 to François-Xavier Duchateau, Hôpital Beaujon, Clichy; p. 49 assigns Center 17 to Pierre Mols, CHU Saint-Pierre, Brussels.
4. **Consistency rule applicable:** Applicable if the article's numbered trial centre uses the protocol's site identifier scheme. The same identifier then has incompatible site labels. A separate monitoring-study number would be a distinct scheme rather than an arithmetic failure.
5. **Calculation or logical comparison reproduced:** Centre-number identity comparison gives reported 5→Saint Pierre versus planned 05→Beaujon and 17→Saint-Pierre. The subset itself reconciles 56+59=115; the candidate concerns the site label attached to that numerical subset.
6. **Necessary inputs available:** Printed centre number, site names, roster assignments and CPR sample count are available. **Exact missing inputs or definitions:** Final investigator roster/renumbering history and whether the CPR substudy employed independent centre numbers; the package does not identify a substudy-specific numbering map at the cited report location.
7. **Source-grounded alternative interpretation:** The article calls the site an investigative centre and discusses a single-site post-hoc monitoring subset. A separate monitoring identifier could account for 5; alternatively the article or earlier roster may use an outdated site label. Neither mechanism is established.
8. **Direct observation versus inferred explanation:** Direct: incompatible printed number/site mappings and matching subset number. Derived: identity conflict if the same centre-number system applies. Inferred and unconfirmed: separate numbering or a transcription caused it.
9. **Exact remaining human question:** Which physical site supplied the 56 BMV/59 ETI CPR records, and does report “Center No. 5” use the protocol site-number scheme or a separate monitoring scheme?
10. **Document role of every comparator:** Main pp. 3/4 are REPORT outcome-method/result content. Roster pp. 47/49 are PLAN prospective participating-centre assignments.
11. **Classification confirmation:** Category Measure, label, or scale inconsistency; relationship type P_R; all relationships P_R; review domain protocol_report. **Classification rationale:** The site identifier attached to reported numerical observations conflicts with the plan's identifier/site mapping. **Classification ambiguity:** Possible undisclosed numbering scheme or final roster revision. No additional relationship arises from report p. 4 corroboration. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. Source mappings are reproduced exactly; the unprovided numbering definition remains the registered human question. **Suggested review disposition:** retain.

## C028 — Before-ROSC reassignment does not conserve favorable survivors

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Primary outcome [REPORT main PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4) and post-hoc eTable 2 second analysis [REPORT results PDF p. 3](../../../joi180004supp2_prod.pdf#page=3), visually inspected.
2. **Source value/text matched:** Yes. Main primary ITT favorable functional survival/CPC 1–2 at day 28 is 44/1018 BMV and 43/1022 ETI.
3. **Comparator matched:** Yes. eTable 2 second block says patients intubated after BMV before ROSC are considered in the ETI group; Survival with CPC≤2 at day 28 is 41/863 BMV and 45/1174 ETI. This is distinct from the first eTable block explicitly excluding ECMO-CPR/uncontrolled donation.
4. **Consistency rule applicable:** Pure reassignment between two arms conserves the combined favorable-survivor count, provided outcome definition and patient inclusion are unchanged. The second block does not itself state additional outcome exclusions.
5. **Calculation or logical comparison reproduced:** Direct awk: 44+43=87 versus 41+45=86; combined delta −1. BMV loses three favorable survivors and ETI gains two. The three-patient reduction in combined denominators (2040 versus 2037) provides a possible population-change context, not the missing favorable survivor's identity.
6. **Necessary inputs available:** Both numerator pairs, endpoint labels and regrouping description are supplied. **Exact missing inputs or definitions:** IDs/outcomes of the three omitted patients; whether exclusions beyond reassignment apply; whether one CPC outcome was recoded; exact analysis membership for the second block.
7. **Source-grounded alternative interpretation:** The displayed denominator total is smaller in the second block, so a favorable survivor may have been omitted under an unprinted eligibility rule. That possibility could explain the numerator difference and is grounded in displayed totals; it is not evidence identifying the cause.
8. **Direct observation versus inferred explanation:** Direct: 44/43 and 41/45, matched day 28 favorable endpoint and regrouping label. Derived: loss of one combined success. Inferred and unconfirmed: an exclusion, recoding or numerator transcription explains it.
9. **Exact remaining human question:** Which favorable survivor is absent or differently coded in the second post-hoc block, and what additional inclusion/outcome rule, if any, accompanies before-ROSC reassignment?
10. **Document role of every comparator:** Main p. 4 and non-plan eTable 2 p. 3 are REPORT results content in two distinct supplied documents.
11. **Classification confirmation:** Category Numeric or arithmetic inconsistency; relationship type S_C; all relationships S_C; review domain statistical_results. **Classification rationale:** Cross-document REPORT numerator conservation; no prospective plan is a conflicting comparator. **Classification ambiguity:** Additional unprinted membership/outcome changes may explain the totals. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. The exact numerator loss is reproduced; the causal membership explanation is unavailable and remains an explicit human question. **Suggested review disposition:** retain.

## C029 — Later consolidated protocol retains 20 centers after amendment to 25

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Later consolidated protocol summary [PLAN PDF p. 65](../../../joi180004supp1_prod.pdf#page=65), §4.2.2 [p. 72](../../../joi180004supp1_prod.pdf#page=72), and MS1 centre amendment comparison [p. 112](../../../joi180004supp1_prod.pdf#page=112), all visually inspected.
2. **Source value/text matched:** Yes. Later protocol header identifies V1.4 dated 22 September 2015 and V2 dated 22 January 2016. Summary states 20 study centres; §4.2.2 states 20 participating centres: 15 France, 5 Belgium.
3. **Comparator matched:** Yes. Amendment p. 112 explicitly contrasts prior total 20 with modified total 25, withdraws Belgian centre 19, and states addition of six centres 21–26. It also explicitly separates the participating-centre list from the protocol so future site changes do not require a protocol version change. Non-English original amendment wording is described here in English.
4. **Consistency rule applicable:** Applicable to contemporaneous current participating-centre statements if the later consolidated body is intended as a current statement incorporating that amendment. Historical planning counts or deliberately fixed body context would require a different interpretation.
5. **Calculation or logical comparison reproduced:** Direct awk: 20−1+6=25. Withdrawn centre 19 is Belgian; p. 112 explicitly identifies six additions, with the first three displayed at French sites. The explicit amended total 25, versus later body 20, is sufficient without relying on the full country split of all six additions. The registered 21 France/4 Belgium extrapolation is not needed to establish this comparison.
6. **Necessary inputs available:** Body versions/dates, 20 count, country split, and explicit amendment 20→25 are available. **Exact missing inputs or definitions:** Whether later body totals are current or intentionally historical; the effective roster referenced by the V1.4/V2 consolidated body; date/effect mapping of the detached roster to that body.
7. **Source-grounded alternative interpretation:** The amendment expressly detaches the roster to avoid protocol version changes. This could explain retention of a historical 20-centre body while a separately governed current roster contains 25. The later body does not label its 20 as historical at the cited locations.
8. **Direct observation versus inferred explanation:** Direct: later body 20 versus amended roster total 25 and roster-detachment explanation. Derived: 20−1+6. Inferred and unconfirmed: the later body is stale or intentionally retains background rather than current count.
9. **Exact remaining human question:** Are the consolidated V1.4/V2 body counts current or historical, and which detached roster/count governs those versions after the 20→25 amendment?
10. **Document role of every comparator:** All three locations are PLAN prospective protocol/amendment material by content, despite being combined in a supplied supplement.
11. **Classification confirmation:** Category Cross-document numeric inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** Protocol versions and roster amendment stay plan-internal within the bound bundle. Actual enrolling centres are a different quantity and add no P_R/S_C relationship. **Classification ambiguity:** Effective-date alignment and intentionally detached roster. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. The literal later-body and amended-roster counts are reproduced, with their intended temporal framing still undefined. **Suggested review disposition:** retain.

## C030 — Printed null and alternative share the same noninferiority boundary

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Original hypothesis [PLAN PDF p. 36](../../../joi180004supp1_prod.pdf#page=36) and strict CI rule [p. 37](../../../joi180004supp1_prod.pdf#page=37); later hypothesis [p. 90](../../../joi180004supp1_prod.pdf#page=90) and rule [p. 91](../../../joi180004supp1_prod.pdf#page=91); native SAP hypothesis [p. 121](../../../joi180004supp1_prod.pdf#page=121) and rule [p. 124](../../../joi180004supp1_prod.pdf#page=124). Later summary [p. 66](../../../joi180004supp1_prod.pdf#page=66) also corroborates the strict rule; these pages were visually inspected.
2. **Source value/text matched:** Yes. All three hypothesis versions display H0: πbag−πtracheal≤−0.01 and H1: πbag−πtracheal≥−0.01. Native SAP uses BVM/TI notation for the same contrast.
3. **Comparator matched:** Yes. Original/later protocol and SAP specify noninferiority if the lower CI limit is higher than −0.01, a strict greater-than decision. No plus/minus sign question is needed here; the image SAP sign discrepancy belongs to C024.
4. **Consistency rule applicable:** Literal hypothesis-set intersection can be checked at the declared boundary without any unreported variance/model assumption. Intended mathematical disjointness is the notation question, not evidence that an implemented test or fitted result was wrong.
5. **Calculation or logical comparison reproduced:** Direct awk substitution d=−0.01 gives (d≤−0.01)=1, (d≥−0.01)=1, and (d>−0.01)=0. The printed null/alternative sets share the boundary, while the operational CI decision excludes equality.
6. **Necessary inputs available:** Both inequalities, contrast, margin and strict CI language are supplied. **Exact missing inputs or definitions:** Whether the inclusive alternative intentionally denotes closure/limiting shorthand; intended point-hypothesis partition at equality and implementation treatment of that boundary.
7. **Source-grounded alternative interpretation:** The strict operational CI rule consistently gives the test decision, so inclusive H1 notation may be conventional limiting shorthand rather than an intended overlapping decision region. The plans do not explain that convention.
8. **Direct observation versus inferred explanation:** Direct: inclusive ≤ and ≥ at the same margin and “higher than” CI criterion. Derived: boundary intersection. Inferred and unconfirmed: shorthand rather than accidental non-strict notation; no inference about trial conclusion follows.
9. **Exact remaining human question:** Is the alternative's inclusive boundary intentional shorthand, or should the intended disjoint hypothesis partition be read as strict above −0.01? Confirm notation intent against the operational CI rule.
10. **Document role of every comparator:** All cited original/later protocol, SAP and summary locations are PLAN prospective statistical specification content.
11. **Classification confirmation:** Category Statistical reporting inconsistency; relationship type P_P; all relationships P_P; review domain plan_material. **Classification rationale:** Shared-boundary notation versus strict decision wording stays inside plan material; report results merely using a CI would not add a conflicting relationship. **Classification ambiguity:** Closure shorthand versus intended literal partition. No classification change.
12. **Evidence state and determining fact:** recorded_candidate. The boundary overlap is reproduced directly under the printed inequalities; intended notation convention remains for humans. **Suggested review disposition:** retain.

## C031 — Emitted primary ITT rounding comparison, disproven after input correction

**Status:** Pending Human Adjudication.

1. **Location found:** Yes. Main abstract [REPORT PDF p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1), primary contrast definition [p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), and primary outcome [p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), all visually inspected.
2. **Source value/text matched:** Yes. Abstract and primary text print 44/1018 BMV versus 43/1022 ETI favorable functional survivors, difference 0.11%, one-sided 97.5% CI −1.64% to infinity, and noninferiority P=.11.
3. **Comparator matched:** The correct comparator uses those primary numerators 44 and 43. Main p. 4 also prints secondary overall survival 55/1018 versus 54/1022; those are different endpoint inputs and cannot be assigned to the primary arithmetic comparison.
4. **Consistency rule applicable:** Applicable: 100×(primary BMV proportion−primary ETI proportion), followed by ordinary rounding to two decimal percentage points. No estimator or variance rule is needed to compare the simple primary point difference at this precision.
5. **Calculation or logical comparison reproduced:** Direct awk independently gives 100×(44/1018−43/1022)=0.114763993710 percentage points and printf %.2f=0.11, agreeing with both source occurrences. The different secondary calculation is 100×(55/1018−54/1022)=0.118993152607, which was the draft's misassigned arithmetic. The registered primary rounding mismatch is explicitly disproven.
6. **Necessary inputs available:** All primary arithmetic inputs and display precision are printed. **Exact missing inputs or definitions:** None for this point-estimate recheck. Exact noninferiority variance/P convention is not fully specified here, but it is immaterial to the disproven rounding comparison.
7. **Source-grounded alternative interpretation:** Correct endpoint matching alone explains the apparent draft discrepancy; no alternative estimator, truncation or hidden calculation is required to obtain the printed 0.11.
8. **Direct observation versus inferred explanation:** Direct: primary 44/43 and displayed 0.11, secondary 55/54. Derived: primary arithmetic rounds to 0.11. The draft input mix-up is documented in the current ledger and independently confirmed numerically; it is an evidence-record issue, with no residual source inconsistency.
9. **Exact remaining human question:** Confirm that this stable card records the primary/secondary input mix-up and the source-reproduced 0.11 result; no unresolved arithmetic question remains for this comparison.
10. **Document role of every comparator:** All exact printed inputs and the contrast definition are REPORT main-article content. The computed comparator is derived from those REPORT values, not a separate document or PLAN comparator.
11. **Classification confirmation:** Category Numeric or arithmetic inconsistency; relationship type S_W; all relationships S_W; review domain statistical_results. **Classification rationale:** The retained registered comparison concerns within-main-report primary arithmetic, although its mismatch is disproven. **Classification ambiguity:** None for endpoint identity after reading primary versus secondary source headings. No classification change.
12. **Evidence state and determining fact:** not_reproduced. Correct directly confirmed primary inputs yield 0.114763993710→0.11; thus the registered rounding mismatch is explicitly disproven, with no residual question. **Suggested review disposition:** exclude. This mechanically derived pre-fill does not delete the ID or adjudicate it.
