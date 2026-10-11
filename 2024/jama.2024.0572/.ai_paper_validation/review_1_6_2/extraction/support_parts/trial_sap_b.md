# Trial SAP support mapping, shard B

## Scope and provenance

- Source: DOC-004, `joi240006supp3_prod_1708623114.99733.pdf`, physical PDF pages 21–40 only; printed page numbers equal physical pages in this shard.
- Document role: PLAN, SELECT 2 Statistical Analysis Plan V1.0.0, November 20, 2022. The CONFIDENTIAL watermark and date/version repeat on pages; no amendment or alternate version is disclosed on these assigned pages.
- Complete fresh scientific mapping of 20/20 assigned units, all reusable-backed; fresh-required extraction units 0; images inspected 20/20. No source, reused asset, or other agent output modified.
- Read each assigned OCR file `review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/ocr/page-NN.txt` and visually inspected each corresponding `pages/page-NN.png` under `.ai_paper_validation/`. Legacy rendering/OCR engine versions unrecorded; no new derivative or OCR produced. CPU device recorded in current tooling record.
- The OCR is only a transcription aid: all quantitative thresholds, labels, and formulas below follow the page image. The assigned units contain no workbook, cached cell values, or spreadsheet formulas.
- Local relationship keys TB01–TB20 below map each page. Matching keys identify concepts for subsequent alignment with main-paper extraction; this shard has no authority to inspect unassigned main-paper pages or diagnose findings.
- Coverage gaps: none. One no-applicable page (p25, references only). Templates on pp26–35 contain illustrative placeholders rather than observed trial data. Formula subscripts and symbols on pp39–40 are recorded as printed, with explicit notation observations; no inference about their statistical consistency is made.

## Page-by-page extraction and relationship map

### TB01 — PDF p21: secondary analyses and subgroup table start

Evidence: [DOC-004 p21](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=21). Sections 10.2.3.10.3–10.2.4.

Early neurological improvement missing values follow symptomatic ICH section 10.2.3.4.3, which is outside this shard and must be joined to shard A. Output: proportion exhibiting early neurological improvement, and relative risk with 95% confidence interval and P value using modified Poisson regression. This page continues the early-improvement definition from prior pages; it is not a standalone new definition.

Secondary outcome: quality of life score at 90-day follow-up, measured using NeuroQoL. Outcome measure is the score distribution. Null hypothesis is no significant distribution difference between patients assigned EVT and MM. Missing data are not imputed (printed sentence says “Missing data for length of the quality of life score will not be imputed”). Summary is median (IQR); treatment effect is difference in median values with 95% CI and P value from median regression.

Section 10.2.4 prespecifies repeating primary efficacy, functional independence (mRS 0–2), and independent ambulation (mRS 0–3) analyses within subgroups; effect size and 95% CI appear in Figure 3 forest plot. Visually recovered full table rows, including rows omitted in OCR: age <70/≥70; presentation NIHSS <20/≥20; clot ICA/MCA-M1; time last known well to randomization 0–12/12–24 and 0–6/6–24 (time units supplied by later figure: hours). Matching main-paper keys: early neurological improvement; NeuroQoL; ordinal mRS; binary mRS0–2 and mRS0–3; age/NIHSS/occlusion/time subgroup analyses.

### TB02 — PDF p22: subgroup table continuation; planned displays; as-treated rationale

Evidence: [DOC-004 p22](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=22). Sections 10.2.4, 10.2.5, 11.1.

Subgroups continuing TB01:

| Factor | Printed strata/definition |
|---|---|
| Perfusion (rCBF <30%) lesion volume | <70/≥70 ml; <100/≥100 ml; <150/≥150 ml |
| CT ASPECTS | 6–10, 3–5, 0–2, based on core laboratory ASPECTS |
| Perfusion mismatch profile 1 | Ratio ≥1.8 AND volume ≥15 ml, present yes/no |
| Perfusion mismatch profile 2 | Ratio ≥1.2 AND volume ≥10 ml, present yes/no |
| Restricted trial population 1 | Yes/no membership in population excluding (a) ASPECTS6–10 within 6 hours of last known well AND (b) ASPECTS6–10 with rCBF<30% lesion <70 ml within 6–16 hours |
| Restricted trial population 2 | Yes/no membership in population with CT ASPECTS <6 AND perfusion rCBF<30% lesion volume ≥70; unit not printed in this row, figure p34 specifies ml |
| Hemisphere | Right/left |
| Geographic location | US sites/non-US sites |

Planned manuscript: Table1 key baseline by patient group; Table2 primary and key secondary outcomes. Figure1 Grotta stacked bars of each mRS grade by assignment in ITT. Figure2 analogous bars for as-treated and per-protocol. Figure3 primary-outcome subgroup effect sizes with 95% CIs for section10.2.4. Supplementary Figure1 CONSORT flow.

Section11.1 begins rationale that assigned EVT may not be received, e.g. spontaneous symptom resolution between randomization and procedure; continuation p23. Matching keys: imaging strata, mismatch profile, hemisphere/site interaction, analysis population and output status.

### TB03 — PDF p23: alternate populations and exploratory/tertiary imaging analyses

Evidence: [DOC-004 p23](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=23). Sections11.1–12.

As-treated rationale continues: no arterial occlusion on baseline angiogram after spontaneous or thrombolysis-induced recanalization; MM-assigned subjects may receive EVT. After study completion, repeat primary Wilcoxon–Mann–Whitney measure of superiority within the adaptive-design sample, classifying patients as treated. Per-protocol includes only subjects meeting every eligibility criterion, imaging eligibility determined by central core laboratory, and receiving randomized treatment.

Section12 title is “Pre-specified exploratory analyses”; text calls the following “pre-specified tertiary analyses” in patients receiving EVT or best medical management and explicitly permits their reporting or nonreporting in the primary trial manuscript. Imaging analyses individually listed:

1. Association between imaging profiles and thrombectomy clinical outcomes/treatment effect.
2. Thrombectomy efficacy by large-core definition: ASPECTS≤5 regardless of core size; ischemic core≥50 mL regardless of CT ASPECTS; ASPECTS≤5 AND core≥50 mL.
3. Functional independence by imaging modality.
4. Heterogeneity of treatment effect by imaging modality.
5. Ceiling effect of core volume on thrombectomy outcomes.
6. Ceiling effect of CT ASPECTS on thrombectomy outcomes.
7. Joint treatment modification by CT ASPECTS and perfusion rCBF<30% lesion volume.
8. Mismatch treatment effects using ratio≥1.8 AND volume≥15 ml; ratio≥1.2 AND volume≥10 ml.
9. Overestimation of baseline perfusion infarct core processed by core laboratory.
10. Total ischemic lesion volume effect on EVT efficacy and safety: union of manually delineated NCCT hypodensity volume and reprocessed CTP rCBF<30% tissue volume when technically feasible; otherwise the larger of these two volumes.
11. Age modification of association between EVT and clinical outcomes.

Matching keys: imaging analysis status; large-core modality definitions; ASPECTS/perfusion continuous and categorical effects; mismatch thresholds; ischemic lesion union/max rule; functional independence; core overestimation. No model, interaction test, spline specification, or multiplicity rule for these tertiary analyses appears on this page.

### TB04 — PDF p24: exploratory/tertiary continuation; administrative material

Evidence: [DOC-004 p24](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=24). Section12 continuation.

Effect modifiers individually listed: stroke severity; occlusion location; time to treatment; ischemic core volume; ASPECTS; presence of mismatch; left versus right hemisphere; transfer status. Additional tertiary analyses: workflow; time metrics; EVT cost effectiveness; adjunctive thrombolysis benefit; tandem occlusion presence; tenecteplase versus alteplase; utility-weighted mRS evaluation; discharge location; time to DNR-CC decision in subjects transitioned to comfort care. EVT-treated-only tertiary analyses: anesthesia technique, reperfusion status after thrombectomy, interventional parameters, procedural metrics. Status follows p23: tertiary/exploratory, may or may not be in primary manuscript. No numerical cutoffs, fitted models, or estimated values added here.

Acknowledgment credits randomization implementation and power/operating-characteristic analysis. Start of reference list only; acknowledgment/reference material adds no result-relevant quantitative relationship. Matching keys: interaction analyses and safety/procedural outcomes, utility-weighted mRS, discharge outcomes.

### TB05 — PDF p25: references only, no applicable quantitative relationship

Evidence: [DOC-004 p25](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=25). References2–10, including adaptive-design, missing-data, and historical thrombectomy publications. Titles include historical 6–16-hour and 6–24-hour windows, bibliographic year/volume/page/DOI numbers; none specifies a new SELECT2 endpoint, method, count, planned analysis, or trial result. NO_APPLICABLE_RESULT_RELEVANT_CONTENT. No external referenced source consulted.

### TB06 — PDF p26: illustrative Table1 baseline template start

Evidence: [DOC-004 p26](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=26). Section15 “Illustrative tables and figures.” Table1 ITT baseline stratified by allocated treatment. Columns Total, allocated EVT+MM (EVT arm), allocated MM only (MM arm); each N=xx, empty numerical cells. These are formatting plans, not observed counts.

Planned rows: age years median[IQR]; sex males/females n(%); history hypertension; congestive heart failure n(%); coronary artery disease n(%); atrial fibrillation n(%); diabetes n(%); transient ischemic attack n(%); stroke n(%); hemisphere right/left n(%); clot ICA, MCA-M1, tandem occlusions n(%); transfer to EVT-capable center n(%); IV thrombolysis total and IV alteplase n(%). Matching key: baseline ITT characteristics and denominator/population labels. Hypertension row has no explicit n(%) label on this page, while most other history rows do.

### TB07 — PDF p27: illustrative Table1 clinical/time rows

Evidence: [DOC-004 p27](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=27). Same empty Total/EVT/MM columns. Planned rows: IV tenecteplase n(%); NIHSS at presentation to EVT-capable center median[IQR]; general anesthesia n(%). Time rows all minutes median[IQR]: last known well to randomization; arrival to CT; arrival to CTP; arrival to arterial puncture; puncture to reperfusion/end of procedure. “Imaging parameters” heading continues p28. No observed values. Matching keys: baseline clinical/time metrics, thrombolysis/anesthesia, randomization interval.

### TB08 — PDF p28: illustrative Table1 imaging rows and units

Evidence: [DOC-004 p28](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=28). Empty table columns continue. Planned rows all median[IQR]: baseline CT ASPECTS; perfusion rCBF<30% lesion volume ml; tissue Tmax>6s volume ml; tissue Tmax>10s volume ml. Footnote expands NIH, ASPECTS, EVT, IQR, ml. No actual medians or counts. Matching keys: core/penumbra imaging labels, thresholds, milliliter units.

### TB09 — PDF p29: illustrative Table2 ITT clinical outcome template start

Evidence: [DOC-004 p29](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=29). Clinical outcomes stratified by assigned treatment. Columns assigned EVT+MM and assigned MM only, each N=xx; effect-size column with 95% CI. Empty result cells.

Planned rows: mRS90-day median[IQR]; functional independence mRS0–2 at90days n(%); independent ambulation mRS0–3 at90days n(%); symptomatic ICH within24hours n(%) marked *; neurological worsening within24hours n(%) marked #; all-cause mortality within90days n(%); procedural complications total n(%). No separate P-value column printed here. Definitions of marked rows appear p31. Matching keys: primary mRS, key binary outcomes, safety and mortality, assigned-arm denominators.

### TB10 — PDF p30: illustrative Table2 safety/procedural/discharge continuation

Evidence: [DOC-004 p30](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=30). Empty same arm/effect95%CI columns. Complication subrows: surgical-site hematoma n(%); surgical-site infection n(%); vascular injury due to EVT n(%) marked +. Successful reperfusion mTICI≥2b n(%). Discharge disposition n(%) categories: home; acute-care facility; inpatient rehabilitation; skilled nursing; hospice; in-hospital death. Early neurological improvement n(%) marked $; quality-of-life score begins and continues p31. No observed values. Matching keys: procedural events, mTICI, discharge categories, neurological improvement.

### TB11 — PDF p31: illustrative Table2 definition footnotes

Evidence: [DOC-004 p31](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=31). Quality-of-life row continues NeuroQoL median(IQR).

* Symptomatic ICH: parenchymal hemorrhage type2 OR remote parenchymal hemorrhage associated with NIHSS increase≥4 points at24-hour follow-up; SITS-MOST criteria after core laboratory hemorrhagic-transformation adjudication.

# Neurological worsening: NIHSS increase≥4 at24-hour follow-up relative to presentation at EVT-capable center.

+ Vascular injury footnote includes xx peripheral/intracranial dissection patients, xx perforation patients, xx other vascular complication patients; xx placeholders remain.

$ Early neurological improvement: NIHSS improvement≥8 points relative to presentation at EVT-capable center OR NIHSS0–1 at24-hour follow-up. Matching keys: event threshold/time/baseline comparator, safety adjudication, NeuroQoL.

### TB12 — PDF p32: illustrative Figure1 ITT mRS distribution

Evidence: [DOC-004 p32](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=32). Figure1 mRS90-day distribution by treatment assignment in ITT. Two bars “ASSIGNED TO EVT ARM”/“ASSIGNED TO MM ARM”; each seven XX segments, legend mRS0,1,2,3,4,5,6. Percent axis0% to100%,10% ticks. XX and equal example widths are illustration, not trial result percentages. Matching key: ordinal mRS distribution, ITT assigned-arm labels.

### TB13 — PDF p33: illustrative Figure2 alternate population mRS

Evidence: [DOC-004 p33](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=33). Figure2 mRS90-day distribution in predefined alternate populations. A as-treated bars “RECEIVED EVT”/“RECEIVED MM”; B per-protocol bars “ASSIGNED TO EVT ARM”/“ASSIGNED TO MM ARM”. All seven mRS0–6 segments marked XX. Both percent axes0–100 with10-point ticks. Matching key: analysis-set sensitivity output and treatment reference labels; no observed distribution values.

### TB14 — PDF p34: illustrative Figure3 complete subgroup forest plot

Evidence: [DOC-004 p34](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=34). ITT EVT effect across prespecified subgroups, effect size95%CI. All displayed point/CI entries are illustrative 1.00(0.50,2.00), not trial estimates. Axis ticks .4,1,2.5; left “Favors MM”, right “Favors EVT”. Table contains31 rows: age2; NIHSS2; ICA/M1 2; time0–12/12–24 and0–6/6–24 4; rCBF<30% volume70/100/150 thresholds6; CT ASPECTS6–10/3–5/0–2 3; mismatch1.8/15 yes/no2; mismatch1.2/10 yes/no2; restricted population1 yes/no2; restricted population2 yes/no2; hemisphere2; US/non-US2. Definitions exactly match TB01–TB02, with ≥70 ml unit explicit for restricted population2. Matching keys: subgroup forest effect identity/direction; each imaging/time threshold. No actual subgroup sample size, effect estimate, or P value is provided.

### TB15 — PDF p35: illustrative supplementary CONSORT flow

Evidence: [DOC-004 p35](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=35). All N= fields blank. Assessed, randomized, excluded: clinical inclusion unmet; clinical exclusion met; imaging inclusion unmet; imaging exclusion met; unable to obtain consent; other. Assignment EVT+MM: received EVT; did not receive EVT with access route unavailable and protocol violation/crossover. Assignment MM: received MM; did not receive MM with protocol violation/crossover. Both lost-to-follow-up boxes: unable to reach; withdrew. Analysis rows: ITT analyzed per arm; as-treated analyzed (EVT box protocol violation/crossover; MM box access route unavailable and violation/crossover); per-protocol analyzed and excluded (ASPECTS6–10 AND core<50 ml; treatment not received as assigned; other). Footnote “Not mutually exclusive.” Matching keys: participant flow, assigned/as-treated/per-protocol populations, imaging eligibility. No real count exists to sum.

### TB16 — PDF p36: AppendixA minimization general framework

Evidence: [DOC-004 p36](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=36). K treatments T1…TK, equal1:1:…:1 allocation; S balancing variables X1…XS; variable f has Qf levels, Zf∈{1,…,Qf}, new patient observed level lf. For treatment k, count existing participants Nk(Zf=lf). Hypothetical assignment increments only treatment k count by1. Imbalance Ik(Zf=lf)=D(N1(Zf=lf),…,Nk(Zf=lf)+1,…,NK(Zf=lf)); D measures variation of nonnegative integers. Overall weighted sum Gk=Σ(f=1…S)wfIk(Zf=lf), k1…K; wf is variable weight. Text describes “weighted average”; formula is the printed weighted sum. Matching key: randomization balancing algorithm, analysis stratification variables. This is a planned method formula, not a fitted result.

### TB17 — PDF p37: AppendixA minimization implementation

Evidence: [DOC-004 p37](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=37). Step3 chooses k*=argmin(k)Gk and gives highest allocation probability to k*. For variance D, printed Gk=2[ΣwfNk(Zf=lf)]/(K−1)+constant; k*=argmin(k)ΣwfNk(Zf=lf). SELECT2 uses T1/T2 allocation1:1.

| Balancing factor | Printed levels | Weight |
|---|---|---:|
| Age | <60,60–69,70–79,80–85years | 3 |
| Presentation NIHSS | 6–9,10–15,16–20,>20 | 4 |
| Clot location | M1,ICA | 3 |
| Onset to randomization | 0–8,9–16,17–24hours | 3 |
| CTP/MRP core volume | <50cc,50–100cc,101–150,151–200,>200 | 4 |
| Target mismatch profiles | 0,1 | 2 |
| Hemisphere | Right,left | 2 |
| Center | Level cell blank | 1 |
| Physician ASPECTS | 3–4,5–6,7–8,9–10 | 3 |

Image reveals target mismatch/hemisphere/center rows absent in OCR. Matching keys: minimization covariates, weighting, eligibility/core/ASPECTS stratification. Units for third and later core categories follow preceding cc labels.

### TB18 — PDF p38: AppendixA biased allocation probabilities

Evidence: [DOC-004 p38](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=38). First patient equal randomization. Subsequent assignments compare G1/G2: if G1>G2, assign T2 probability p=0.9; if G1=G2, assign T2 probability0.5; if G1<G2, assign T2 probability1−p=0.1. Visually confirmed every branch names T2; OCR had different treatment-label transcription in tie/lower branches. Rest consists references; bibliographic numerals add no trial relationship. Matching key: randomized treatment probability and balancing design.

### TB19 — PDF p39: AppendixB adaptive interim/stopping method

Evidence: [DOC-004 p39](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=39). J=6 groups; ΠJ entire population; Π1…Π5 respectively G1A; G1A+G1B; +G2A; +G2B; +G3A. Group component definitions are outside this shard. W_i^l is sum of Rankin-score ranks from EVT at interim l, subgroup Π_i. n_i^l and n_0i^l are EVT and MM enrolled numbers at interim l.

Printed standardization: Z_i^l = [W_i^l − n_i^l(n_i^l+n_0i^l+1)/2] / [n_i^l n_0i^l(n_i^l+n_0i^l+1)/12]^(1/2).

Whole-population efficacy stopping: Z_J^l≥b. Otherwise, subgroup selection if tilde(Z_J^l)≤tilde(b). Printed tilde-statistic right-hand side uses W_i^l and n_i^l,n_0i^l subscripts (despite left J): [W_i^l−n_i^l(n_i^l+n_0i^l+1)/2−n_i^l n_0i^l θ] / [n_i^l n_0i^l(n_i^l+n_0i^l+1)/12]^(1/2). Preserve that printed indexing; do not silently substitute J.

Select subgroup hat(i) with largest Z_i^l for i≠J; future enrollment only this subgroup; maximum total N remains560. At later stage l′, selected-subgroup efficacy if Z_hat(i)^(l′)≥b; may stop futility if tilde(Z_hat(i)^(l′))≤tilde(b). No observed interim statistic or operational stopping event is given. Matching keys: adaptive design, ordinal rank direction, interim efficacy/futility, enrichment, group membership, enrollment cap.

### TB20 — PDF p40: AppendixB final boundary and design inputs

Evidence: [DOC-004 p40](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=40). If neither whole-population efficacy/futility boundary ever occurs, proceed final stage; claim EVT efficacy if Z_J^(l=3)≥c. Maximum N560; interim N200 and380; typeI error0.025; power0.9. Printed boundaries b=2.604, tilde(b)=−1.897, c=2.772. θ projected treatment effect at maximum sample size. Printed hypotheses: H0:P(Y≤X)=1/2; HA=P(Y≤X)=1/2+θ. Y Rankin score in MM; X Rankin score in EVT. Fixed-sample projected effect θ calculation printed (Z_(1−α)+Z_(1−β))/sqrt(3N)=0.0791. Text attributes rationale to supplied reference citation only; external article not consulted. Remaining references add no SELECT2 quantitative inputs. Matching keys: maximum/sample timing/power/alpha; decision boundaries; WMW probability orientation; primary design effect.

## Cross-page joins and limitations

TB01 early-improvement missing values require section10.2.3.4.3 from shardA; TB01 subgroup repetition requires primary/functional-independence/ambulation methods in shardA. TB02–TB04 preserve planned subgroup versus tertiary/exploratory status for later report comparison. TB06–TB15 are all illustrative output plans, with no observed values. TB16–TB18 contain complete assigned minimization specification; TB19 subgroup labels require earlier-page definitions; TB19–TB20 contain full assigned appendix decision boundaries.

Every assigned unit has a page record; quantitative content is fully mapped without candidate diagnosis. The page25 no-applicable conclusion follows visual inspection. Supplied image/OCR quality is adequate for these records. Final candidate confirmation remains against exact supplied PDF locations. No source-linked extraction gap remains.
