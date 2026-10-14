# Cross-source consistency review

Runtime agent: 01a12bc2-f62f-7690-92dd-2374810a7228. Fresh cross-source specialist, gpt-6.1-sol / medium. Scope: complete matched-result review of DOC-001 REPORT pp.1–12, DOC-004 REPORT pp.1–49, DOC-002 PLAN pp.1–18 and DOC-003 PLAN pp.1–7. New main/support mapping artifacts and source-matched extraction/renderings were used; no historical findings, ledgers, checker outputs, screening decisions or reports were read. All 86 source units are represented in the reviewed maps. No structured result source is supplied.

The complete scope and review contract were read. Comparisons match population, time, contrast, measure, model and analysis set before applying the threshold. Source links below are relative to this checker artifact. Findings are observations awaiting an independent inclusion screen, with no assigned candidate IDs or adjudications.

## Source confirmation and engines

Current main pp.4,8,9 and source-matched SAP pp.2,3,4,6 were visually inspected. Additional current renders of main p.3, original protocol pp.3–4 and results supplement p.21 were generated and inspected under `preprocessing/cross_confirmation/`: `main3.png`, `plan3.png`, `plan4.png`, `results21.png`. Engine: package-local pinned PyMuPDF 1.26.4 via supplied `pdf_tools.py render`, 200 dpi, CPU. Text locators were new main/results text and source-matched protocol text. SAP encoded text is unusable; readable source-matched images provided authority. No OCR or GPU engine was needed. Existing assets were unchanged.

## Complete matched-result coverage

Each row identifies a complete relationship family rather than selecting a subset of its displayed rows. The ordered lists below and the mapped displays supply the member-level checks.

| Match | Exact source scope and relationship members | Comparison outcome |
|---|---|---|
| XS01 | Main p.1 abstract, p.2 Key Points, p.4 flow/body, Table 1 pp.5–6; N001,N002,N003,N004,N007,N008,N010,N011 | Randomized3357, arms1677/1680, female56.4% vs rounded56%, age67, monotherapy53.7%, median4.6 years reconcile. |
| XS02 | Primary main pp.1,2,6, Figure2 p.7, Table2 p.8, Figure3 all-patient p.9; S001,S002,S007,S009,S016,N013,N016 | HR.96(.77–1.19), P=.70, counts163/173 agree; Figure3 rate column is F-XS-001. |
| XS03 | Unadjusted primary main p.6/Figure2 p.7 and discussion p.10; S007,S009,S050 | .94(.76–1.17) agrees; discussion exclusion≤.76 refers to available unadjusted lower bound; adjusted lower bound.77 is a different model. |
| XS04 | Table2 p.8 components versus pooled accepted outcome bars supplement pp.11–12; S017,S018,S019,S020,N201,N202,N203,N204 | Death81+94=175; stroke27+32=59; ACS48+39=87; HF30+43=73. Components overlap between participants; not summed as unique primary events. |
| XS05 | Table2 p.8 unplanned utilization/fracture/glaucoma versus supplement p.12 accepted bars; S021,S022,S023,S027,N205,N206,N207,N208 | Utilization993+1047=2040; nonvertebral152+166=318; hip20+31=51; glaucoma43+39=82. Definitions checked against supplement pp.6–17, S200,S202–S205. |
| XS06 | Abstract/Key Points/main narrative pp.1,2,6,7,10 versus all Table2 p.8 secondary and safety rows; S017–S030 | Nonsignificant components, hospitalization, falls/fractures, vision, glaucoma and cognition match printed two-sided tests. Table2 lightheadedness P=.06 and CI ending1.00 do not create a cross-location conflict. |
| XS07 | Main pp.3,8 and SAP p.2 vision,18-month cognitive decline,new dementia; S003,S028,S029,S030,S123,S124 | Final SAP definitions match report, including vision repeated slight worsening, SBT≥2 and newly≥10 or diagnosis. Original vision recall window is F-XS-008. |
| XS08 | Main pp.4,10; Figure1; supplement eFigure3 p.25,eTable4 pp.33–36,eTable5 pp.37–40; N007,N008,N017,N300,N308–N315 | Interview withdrawals/loss631=(266+63)+(244+58); unavailable101=57+44; trackable530=272+258; completion2726=3357−631. Different populations are explicit, not contradictory. |
| XS09 | Main adherence p.6/Figure1 p.4 versus eTable6 pp.41–42,eTable7 pp.43–44,eTable8 pp.45–48,eFigure4 p.26; N012,N301,N316–N323 | Respondent ≥1 adherence88%/97% agrees with1518−177 and1567−53; average participant dose adherence is distinct from aggregate medication ratio. Month72 70%/88% agrees. eTable8 restricted baseline drugs is distinct from current-drug eTable6/eFigure4. Single diuretic count movement is excluded below. |
| XS10 | Main p.7 ABPM versus supplement pp.18–19,p.49,eTable9; N014,N209,N210,N324,S010–S014,S206,S308–S318 | All matched means, differences, CIs, P values, control percentages and151/151 agree. Planned6months versus actual9.6months is explicitly disclosed with logistical explanation. |
| XS11 | Main p.7 one-year overall health versus SAP pp.3,5–6 and original protocol p.3, supplement p.21; S015,S125,S127,S211 | Actual12-month absolute score matches final SAP; original secondary versus final exploratory status is included in F-XS-003. Unadjusted means vs adjusted regression difference are not the same estimand. |
| XS12 | Main Figure3 p.9 all19 subgroup axes versus SAP p.6 thirteen-axis list; S031–S049,S128 | First13 axes match item by item; extra6 medication-class axes labeled prespecified are F-XS-002. All subgroup count pairs partition163/173 and directions agree with forest plot. |
| XS13 | Main pp.2–3 eligibility/flow p.4 versus original protocol p.2 and amendment log pp.8–16; N002,N004,N007,S101,S114–S121 | Hypertension, community dwelling and BP medication criteria match. Eligibility wording and delivery procedures are screened below; no numeric analysis-population discrepancy follows. |
| XS14 | Primary definition: original protocol p.3,SAP p.2,main pp.1,3,Figure2,Table2; S001,S003,S102 | Itemwise all-cause death; ACS/MI hospitalization/ED; stroke hospitalization/ED; HF hospitalization/ED; first occurrence agree. ACS/MI shorthand does not create an additional component. |
| XS15 | Secondary criterion list original protocol p.3,SAP p.2,main pp.3,8,report supplement p.21; S102,S123,S211 | Each primary component retained; all-cause utilization qualifier F-XS-004; nursing/LTC admission criterion F-XS-005; glaucoma/overall-health status F-XS-003. Added nonvertebral/cognition and added dementia are disclosed/final-SAP matched. |
| XS16 | Primary models/covariates original p.4 versus final SAP p.4 and report Figure2 p.7/supplement p.20; S111,S127,S009,S208 | Original model is earlier version; final SAP Cox and every ordered primary covariate agree with report. No continuing conflict inferred solely from dated model evolution. |
| XS17 | All SAP Table1 pp.4–6 model rows and ordered lists versus main method p.4/Table2 p.8,report supplement pp.20–21; S123–S127,S006,S016–S030,S209,S210 | Final primary/secondary Cox, cognition/vision/symptom Poisson,health linear regression and predefined reduced-list rule are compatible. Unreported fitted coefficients/covariate reductions are not assumed. |
| XS18 | SAP pp.3–4 ITT,censoring,missingness/nonadherence versus main p.4/report supplement p.20; S126,S127,S006,S209 | Primary/survival ITT and traceable/untraceable censoring agree. Available-data other outcomes compatible with permitted exclusion; covariate-imputation wording observations screened below. Posthoc adherence sensitivity explicitly posthoc. |
| XS19 | Sample-size inputs original protocol pp.3–5,amendment pp.9–10,main pp.3,6; N100–N111,S103–S106,S112,S115,S116,S004,S005 | 1:1,.8 power,.05 alpha,25% reduction,379→406 agree. Recruitment11700 is amended projection,actual3357 distinct. Main discloses406→255,funding stop,336finalevents; target changes are not presented as achieved original targets. |
| XS20 | Protocol interim p.4/main pp.3,6; S107,S005,S121 | Benefit≤.001,harm≤.05,clinical judgement and continued trial agree. Original200-events versus reported155 and revised target context excluded below; no unpublished interim statistic is inferred. |
| XS21 | Protocol diuretic recruitment decision p.4/main p.2; S110,N004 | Six-week versus six-month input into adaptive enrollment rule is F-XS-007. |
| XS22 | Protocol allocation p.4/main p.3 and SAP primary model p.4; S108,N005,S127 | Simple/unstratified versus permuted blocks/province-stratified assignment is F-XS-006. |
| XS23 | Full amendment chronology protocol pp.8–18,final-SAP heading pp.1,7 and result supplement p.21; S100,S114–S122,S211 | BP sample200→302 and survey/recruitment/followup extensions are explicit; outcome prespecification history assertion is F-XS-009. No historical background data is treated as trial result. |
| XS24 | Supplied plan/report multiplicity,margin,hypothesis direction,stopping fields; S004,S005,S107,S127,main Figure3 caption | Superiority,2-sided.05,95%CIs,unadjusted subgroup CIs are source-stated; no NI/equivalence margin/final multiplicity adjustment is supplied. No missing rule alone is a finding. |
| XS25 | Main Table1 versus eTable3/eFigure2; supplement baseline comparisons pp.29–40,recruitment pp.2–5,22,27,interviews p.28 | All source units checked for relationship matching; repeated baseline copies and per-time-point interview counts are peripheral. Within-display arithmetic belongs to independent numeric/statistical review, not omitted source coverage. |

## Itemwise planned-list comparison

Primary final covariates were compared in order: age; sex; continuous frailty; smoking; number non-BP medicines; overall health; prior-six-month hospitalization; CHF; diabetes; CAD; stroke/TIA; CKD excluding dialysis; dialysis; BMI>35; BMI<20; sleep apnea; exercise days; four province indicators. Every item appears in the report's primary-model caption/supplement. Original age≥80, binary frailty/cognition, ≥3 BP drugs and combined renal criterion are preserved as earlier plan content; the supplied SAP explicitly constitutes the later analysis specification.

SAP subgroup list checked one by one: age≥75; sex; Tilburg physical≥3; ≥5medications; health≤75; ≥3BP medicines; CHF; diabetes; CAD; stroke/TIA; sleep apnea; CKD with/without dialysis; zero exercise days. These correspond to Figure3's first13 axes. ACE inhibitor,ARB,beta-blocker,CCB,diuretic,combination medicines are additional axes.

SAP secondary models/covariates were checked for each mortality,stroke/ACS,HF,all-cause utilization,nonvertebral fracture,LTC,glaucoma,cognitive decline row, including their unique order and reduced-model rule. Safety vision,new dementia,symptoms,hip fracture; nocturia change/burden; cost acute/total; exploratory health; and process adherence/sleep BP were compared individually with report definitions and supplied output availability. Unreported non-key cost,nocturia and five functional EQ-5D outcomes are not treated as omitted primary/key-secondary analyses. The report explicitly cites nocturia as already reported in another publication; that publication is not supplied and was not consulted.

## Findings

### F-XS-001 — Figure3 primary-event rate column does not match the same primary-event rates elsewhere

**Locations and roles:** REPORT [main Figure3 p.9](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9), all-patient and every subgroup row; REPORT [main Table2 p.8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8), primary row; REPORT [abstract p.1](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1), [Key Points p.2](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2), [narrative p.6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6).

**Printed evidence:** Figure3 heading is “Rate per100 patient-years”; all patients163events/71.0 bedtime and173events/71.0 morning. Table2 prints same counts and rates2.30/2.44. Abstract/body round to2.3/2.4. Every Figure3 subgroup column follows the same71.0-total pattern: sex30.5+40.5 and30.4+40.6; age14.9+56.1 and14.5+56.5; frailty12.4+58.6 and12.7+58.3; polypharmacy23.0+48.0 and22.4+48.6; health28.5+42.5 and25.1+45.9; resistant7.7+63.3 and7.0+64.0; HF1.1+69.8 and1.1+69.9; diabetes12.5+58.5 each; CAD7.0+63.9 and7.3+63.7; stroke4.6+66.4 and4.8+66.2; apnea16.0+55.0 and14.4+56.6; CKD4.8+66.2 each; sedentary17.7+53.2 and18.3+52.7; ACE24.4+46.6 and25.8+45.2; ARB22.8+48.2 and19.7+51.3; beta11.6+59.4 and10.9+60.1; CCB19.2+51.7 and19.8+51.2; diuretic18.6+52.4 and19.6+51.4; combination14.1+56.9 and13.4+57.6.

**Comparison logic:** Same randomized population,first composite event,followup and count. Printed-copy intervals71.0→[70.95,71.05],2.30→[2.295,2.305],2.44→[2.435,2.445]. Gaps68.645 and68.505; relative to Figure3 copy71.0, discrepancies.96683 and.96486, exceeding.05. A different adjusted HR does not explain a descriptive event-rate column. One repeated column pattern, all affected locations retained.

**Focus area:** A/C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **Qualifying route:** Route B. **Affected result or extracted value:** primary composite and all subgroup event rates. **Why context does not resolve it:** The column assigns a rate unit to values that do not reconcile with the same primary rate in Table2; neither caption nor heading supplies another quantity definition.

**Supported alternatives:**71.0 may represent followup quantity scaled by100 rather than an event rate; total person-time is not directly printed, so this remains an interpretation, not a supplied correction. **Human question:** What quantity,unit and scaling do Figure3's71.0 and subgroup column values represent, and which primary/subgroup rates should a reader extract?

### F-XS-002 — Six medication-class subgroup analyses are labeled prespecified but absent from the supplied subgroup plan

**Locations and roles:** PLAN [SAP p.6](../../../joi250019supp2_prod_1749674951.30054.pdf#page=6); REPORT [main Figure3 p.9](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9), six medication-class axes and caption; REPORT [main narrative p.6](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6).

**Printed evidence:** SAP lists13 axes reproduced itemwise above. Figure3 additionally displays ACE inhibitor,ARB,beta-blocker,CCB,diuretic andcombination medication interactions P=.05,.44,.54,.66,.43,.72, and caption says “prespecified subgroup analyses.” Narrative says all predefined subgroups. No medication-class subgroup axes appear in supplied original protocol/amendments or SAP.

**Comparison logic:** Matching primary outcome,Cox adjustment,baseline medication use and treatment-interaction contrasts; Figure3 contains19 axes, of which13 occur in prospective list and6 do not. Baseline descriptive medication inventories and a diuretic adherence substudy are different analyses and do not prescribe primary treatment-effect interactions. Display precision is not applicable to list membership.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route A, category5. **Affected result or extracted value:** prespecification provenance of six primary-outcome medication-class subgroup analyses. **Why context does not resolve it:** Category5 always registers a reproduced prespecified analysis absent from supplied plan; general protocol/version statements do not add those six items.

**Supported alternatives:** An additional prospective analysis specification may exist, or the caption may apply only to the first13 axes. Neither is identified in supplied content. **Human question:** Where were the six medication-class treatment-effect subgroup analyses prespecified, or which Figure3 analyses does the prespecified label cover?

### F-XS-003 — Prespecified outcome statuses change between supplied plans and report

**Locations and roles:** PLAN [original protocol p.3](../../../joi250019supp1_prod_1749674951.29554.pdf#page=3); PLAN [SAP p.2](../../../joi250019supp2_prod_1749674951.30054.pdf#page=2) and [p.3](../../../joi250019supp2_prod_1749674951.30054.pdf#page=3); REPORT [main p.3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3), [Table2 p.8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8), [health result p.7](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7); REPORT [supplement changes p.21](../../../joi250019supp3_prod_1749674951.30054.pdf#page=21).

**Printed evidence:** Original protocol secondary list includes self-reported EQ-5D functional measures and overall health score; final SAP labels 12-month overall health “Exploratory.” Original new glaucoma is under “Safety”; SAP lists it as secondary item 5; main secondary list includes new glaucoma and Table 2 groups it under secondary safety. Original nocturia frequency, nocturia burden, and light-headedness are under “Tolerability”; final SAP puts nocturia frequency/burden under supplementary safety (pp.2–3) and lightheadedness under supplementary safety symptomatic hypotension (p.2), matching the main report's other-safety list. Report supplement calls changes to health and glaucoma “Changes to secondary outcomes.” Main health contrast −.75 (−1.69 to .19), P=.12; glaucoma HR 1.13 (.73–1.74), P=.58; lightheadedness RR .95 (.90–1.00), P=.06. Main says nocturia was already reported separately; that publication is not supplied.

**Comparison logic:** Same named outcomes, but secondary→exploratory (health), safety→secondary (glaucoma), and tolerability→supplementary safety (nocturia frequency, nocturia burden, lightheadedness) status transitions. Original safety→supplementary safety for syncope, falling, hip fracture, and vision is not an additional status transition: these remain safety. The health definition change to an absolute 12-month score is disclosed and aligns with final SAP; the status transitions remain source observations. No numeric display-precision issue.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R,P_P. **Qualifying route:** Route A, category 5. **Affected result or extracted value:** outcome hierarchy/prespecification status of reported 12-month health, glaucoma and lightheadedness results, and the separately described nocturia safety analyses. **Why context does not resolve it:** Category 5 includes reproduced changes of prespecified status, including disclosed changes; disclosure is retained as an alternative rather than used to suppress the observation.

**Supported alternatives:** Blinded amendments may intentionally have reclassified outcomes; “secondary safety” could describe a safety outcome that remained safety while acquiring secondary hierarchy; tolerability may have been treated as a subset of safety. Original 2016 protocol is explicitly earlier; final SAP was submitted 2021. **Classification ambiguity:** Amendments and overlapping safety/tolerability taxonomy are possible; P_R precedence retained because report also describes the altered outcome hierarchy. **Human question:** What was the final prespecified hierarchy for overall health, glaucoma, nocturia frequency/burden and lightheadedness, and when/how were these statuses changed from the original protocol?

### F-XS-004 — Planned all-cause utilization becomes unplanned utilization

**Locations and roles:** PLAN [SAP p.2](../../../joi250019supp2_prod_1749674951.30054.pdf#page=2) and [Table1 p.4](../../../joi250019supp2_prod_1749674951.30054.pdf#page=4); PLAN [original p.3](../../../joi250019supp1_prod_1749674951.29554.pdf#page=3); REPORT [main pp.1,3,8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) (specific [Table2 p.8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)); REPORT [adjudication criteria p.15](../../../joi250019supp3_prod_1749674951.30054.pdf#page=15).

**Printed evidence:** SAP “All-cause hospitalization/ED visit,” original “All-cause hospital admission”; report “All-cause unplanned hospitalization/ED visit,”993/1047,HR.93(.85–1.02),P=.10. Report excludes elective surgery and elective ED procedures,unclear unplanned events,unplanned overnight stays following planned day surgery without new presentation,and various nonacute presentations. These are explicit event exclusions beyond “all-cause.”

**Comparison logic:** SAP has no unplanned-only qualifier or corresponding criteria. The report's decision list changes which utilization events enter the endpoint, not just the name. ED extension from initial protocol is carried into finalSAP and is not a separate finding. Numeric precision is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route B. **Affected result or extracted value:** abstract secondary utilization claim and HR.93,993/1047events. **Why context does not resolve it:** The report is explicit about acute-only events; the finalSAP specifies all-cause without that restriction, and no supplied amendment identifies this endpoint narrowing.

**Supported alternatives:** All-cause may have intended all causes of acute/unplanned presentation; an operational adjudication definition may have been prospectively accepted. **Human question:** Was the final prespecified utilization endpoint all admissions/ED visits or only unplanned events, and where were the printed exclusion criteria specified?

### F-XS-005 — SAP LTC admission includes assisted living, while report requires loss of medication-timing control

**Locations and roles:** PLAN [SAP p.2](../../../joi250019supp2_prod_1749674951.30054.pdf#page=2); REPORT [Table2 p.8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8),nursing-home row and footnoteg; REPORT [supplement p.16](../../../joi250019supp3_prod_1749674951.30054.pdf#page=16).

**Printed evidence:** SAP secondary “Long-term care (LTC) admission (i.e.,to nursing home or assisted living facility).” Table2 defines admission to group living where participants no longer control medication timing,38/26events,HR1.38(.83–2.27),P=.21. Report operational criteria accept a move from low-care assisted living with personal control to higher-care medication administration by nurses/care aides.

**Comparison logic:** Itemwise SAP alternatives are nursing home OR assisted living. Report adds absence of medication-timing control and specifies a higher-care move. A move into assisted living with retained timing control satisfies literalSAP but not report footnote. This is a criterion membership difference; no numeric recomputation applies.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route B. **Affected result or extracted value:** nursing/LTC endpoint definition accompanying38/26events and HR1.38. **Why context does not resolve it:** The functional restriction determines accepted events; ordinary alternative facility names do not establish that every assisted-living admission entails loss of medication control.

**Supported alternatives:** SAP assisted-living language may intend only higher-care facilities with medication administration. **Human question:** Did the prespecified LTC endpoint include all assisted-living admissions, or only admissions entailing loss of personal medication-timing control?

### F-XS-006 — Reported blocked/province-stratified assignment differs from original simple randomization

**Locations and roles:** PLAN [original protocol p.4](../../../joi250019supp1_prod_1749674951.29554.pdf#page=4); REPORT [main p.3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3); PLAN [SAP primary-model p.4](../../../joi250019supp2_prod_1749674951.30054.pdf#page=4) corroborates final province adjustment only.

**Printed evidence:** Original allocation “simple randomization–no stratification or blocking.” Report “permuted blocks(random block sizes of10or12,stratified by province of residence).” Same individual1:1 randomized comparison,1677/1680; primary Cox includes province.

**Comparison logic:** No blocks/no strata versus two specified block sizes/five provincial strata are incompatible design specifications. All18 original/amendment pages and all7SAP pages were checked; no supplied amendment explicitly replaces allocation procedure. No rounding issue.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route B. **Affected result or extracted value:** randomization/stratification specification underlying adjusted primary HR.96(.77–1.19). **Why context does not resolve it:** Current report procedure is clear but its relationship to the supplied prospective unblocked design remains unclear; province covariate adjustment does not itself establish province-stratified randomization.

**Supported alternatives:** The separately cited final published protocol,not supplied,may contain an updated procedure; the original protocol is explicitly2016. **Human question:** Which prospective amendment specified blocked,province-stratified assignment rather than the supplied simple-randomization procedure?

### F-XS-007 — Adaptive diuretic-enrollment assessment uses six months rather than planned six weeks

**Locations and roles:** PLAN [original protocol p.4](../../../joi250019supp1_prod_1749674951.29554.pdf#page=4); REPORT [main p.2](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2).

**Printed evidence:** Plan triggers analysis after200diuretic-only enrollees,including combination pills; assesses “6-week compliance” in all bedtime-allocated BP-medication users,and would exclude further diuretic-only enrollment if diuretic adherence substantially worse. Main calls the assessment predefined but reports “6-month adherence” among diuretic-monotherapy participants,approximately three-fourths adherent,and no enrollment change.

**Comparison logic:** Decision input time6weeks versus6months and source populationall bedtimeBP users versus diuretic-monotherapy participants differ. No explicit numerical adherence cutoff is supplied; none is invented. Numeric intervals do not apply to assessment-time definitions.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route B. **Affected result or extracted value:** adaptive decision retaining diuretic-only recruitment and interpretation of the reported approximately75% adherence assessment. **Why context does not resolve it:** The different assessment time/population directly feed a planned enrollment decision; these are not peripheral followup-count differences.

**Supported alternatives:** The cited but unsupplied diuretic publication or final protocol may describe both timepoints or a blinded amendment. **Human question:** Which assessment time,population and decision rule were prospectively specified for deciding whether to continue diuretic-only recruitment?

### F-XS-008 — Vision deterioration reference window changes from study start to previous followup

**Locations and roles:** PLAN [original protocol p.3](../../../joi250019supp1_prod_1749674951.29554.pdf#page=3); PLAN [SAP p.2](../../../joi250019supp2_prod_1749674951.30054.pdf#page=2); REPORT [main p.3](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3), [Table2 p.8](../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8),footnoted.

**Printed evidence:** Original safety item “Self-reported worsening of vision(since study start–unchanged,slightly worse,much worse).” FinalSAP/report “much worse” than last followup once,or “slightly worse” than last followup on≥2occasions. Report420(25.0%)/411(24.5%),RR1.02(.89–1.17),P=.74.

**Comparison logic:** A persistent small deterioration sincebaseline can be repeatedly reported as slightly worse under original reference,while unchanged sinceprevious followup under final reference. The final binary repeated-slight/much-worse rule aligns SAP and report; original reference window differs. No hypothetical event counts are inferred; arithmetic precision is not relevant.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R,P_P. **Qualifying route:** Route B. **Affected result or extracted value:** abstract visual-safety claim and reported25.0%/24.5% vision deterioration. **Why context does not resolve it:** “Since study start” and “than last followup” imply different temporal reference definitions; neither report amendment rationale nor supplied amendment log explicitly documents this reference-window change.

**Supported alternatives:** Original wording may summarize a cumulative question rather than the final repeated interval question; a final protocol amendment may clarify the instrument. **Human question:** Which vision recall reference and aggregation rule were prespecified and actually administered,and when was any change made?

### F-XS-009 — Report supplement says several safety outcomes were not previously prespecified,although original protocol lists them

**Locations and roles:** PLAN [original protocol p.3](../../../joi250019supp1_prod_1749674951.29554.pdf#page=3); REPORT [supplement p.21](../../../joi250019supp3_prod_1749674951.30054.pdf#page=21),change4; PLAN [SAP pp.2–3](../../../joi250019supp2_prod_1749674951.30054.pdf#page=2) provides later context.

**Printed evidence:** Report says syncope,last-month falling,new glaucoma,nocturia frequency and new dementia were added as secondary safety outcomes and “had not previously been prespecified as outcomes we would analyze.” Original protocol already lists new glaucoma,syncope/fainting prior month,falls prior month underSafety,and number overnight urinations underTolerability. New dementia is genuinely absent from original list and is not part of this finding.

**Comparison logic:** Four printed named outcomes appear prospectively in2016 plan but are described as not previously prespecified in the2025 report. Original lists do not contain detailed models for these outcomes; laterSAP does. Outcome listing and model specification are distinguished rather than silently equated.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **Qualifying route:** Route B. **Affected result or extracted value:** prespecification provenance of the syncope,falling,glaucoma and nocturia safety/tolerability outcomes supporting abstract safety conclusions. **Why context does not resolve it:** The statement concerns being prespecified as outcomes,whereas the supplied prospective list includes those outcomes; the text does not explain whether “prespecified” means a fully specified inferential model rather than named outcome.

**Supported alternatives:** The report may distinguish collecting/listing safety outcomes from prespecifying inferential analysis. **Human question:** Does “not previously prespecified” mean absent as outcomes,or absence of a detailed prospective analysis method,for the four already listed safety/tolerability measures?

## Excluded observations

Only apparent issues considered and not emitted are listed here; reconciled matched results are in the coverage table.

| Location | Observation | Reason code |
|---|---|---|
| Main p.4 versus supplement p.20 | Main “did not impute missing values” follows available-data outcome analysis; supplement explicitly imputes covariates but not outcomes. Outcome-versus-covariate distinction supplies the immediate coherent reading. | CONTEXT_RESOLVES |
| SAP pp.3–4 versus supplement p.20 | SAP permits analysis-specific imputation from surrounding visits or exclusion; actual mean/modal baseline-covariate replacement differs in descriptive detail,but plan does not explicitly prohibit baseline replacement or prescribe an alternative available baseline value. No incompatible fitted result follows from supplied inputs. | CONDITIONAL_OR_UNREPORTED |
| Original primary covariates p.4 versus finalSAP p.4/report p.7 | Earlier binary/cutpoint list differs from later detailed ordered list. FinalSAP identified as later specification,report uses that list; no continuing conflicting primary specification is established solely by comparing versions. | CONTEXT_RESOLVES |
| Original interim p.4 versus main pp.3,6 | Original200event interim versus actual155; report explicitly discloses revised406→255target and half-target intent before interim,with funding context. No claim that155equals200or exactly127.5 is printed. | CONTEXT_RESOLVES |
| Original event target406 versus main final336,amendment end2023 | Funding stop and target revision expressly disclosed. Different attained totals are not conflicting copies of one target/achieved quantity. | CONTEXT_RESOLVES |
| Main p.7/supplement pp.18–19 versus plans6monthABPM | Actual median9.6months,logistical/COVID explanation,clearly distinct intended and achieved times; no claim these are same timepoint. Process assessment timing does not change primary/key-secondary result. | PERIPHERAL_COMPARISON |
| eFigure4 p.26 versus eTable6 p.42 | Bedtime diuretic allocated/off counts278/138 versus277/139; current-drug descriptive process display,one reassignment,does not change primary/key-secondary outcome,analysis population or decision rule. | PERIPHERAL_COMPARISON |
| Main Table1 versus eTable3 pp.29–32 | Printed baseline copies,including CCB percentage differences and ethnicity label variations,are peripheral matched baseline summaries; within-display percentage checks remain independent checker scope. | PERIPHERAL_COMPARISON |
| Main p.7 health means78.9/79.5 versus difference−.75 | FinalSAP multiple linear regression can produce adjusted−.75 rather than crude−.6. Supplied method supports a modeled contrast. | MODEL_VERSUS_CRUDE |
| Main p.3 original/intervention p.3,amendment p.12 | “One or more” at provider discretion versus all once-daily timing target; clinical tolerability/provider discretion and added assistant-guided delivery describe implementation,not a change in medication dose/duration or drug exposure amount. | OUT_OF_FOCUS |
| Main p.3 once/week versus protocol amendment p.12≥month between changes | Delivery pacing rather than intervention dose/duration or statistical endpoint/model. | OUT_OF_FOCUS |
| Original glaucoma exclusions p.2 versus main p.2/flow p.4 | Personal glaucoma/history/medication versus glaucoma/high pressure; usual screening descriptions do not establish an incompatible randomized/analysis population size. | TERMINOLOGY_OR_WORDING |
| Original p.3EQ-5D functional measures,cost,length-of-stay;SAP costs/nocturia;report outputs | Not all planned non-key secondary,safety,tolerability/cost outputs supplied; no primary/key-secondary omission and no comprehensive-output statement in conflict. No unsupplied nocturia publication was consulted. | CONDITIONAL_OR_UNREPORTED |
| SAP p.6 sensitivity characteristics versus eTables4–5 pp.33–40 | Overall completion/withdrawal comparison and unavailable-followup treatment comparison have distinct explicitly stated populations; details of comparisons concern retention sensitivity rather than an omitted primary/key-secondary effect analysis. | PERIPHERAL_COMPARISON |
| Province/site/calendar counts and historical/contextual MAPEC/Hygia/TIME statements | Administrative counts and non-BedMed background comparisons do not change primary/key-secondary results,analysis-population size or decision rule. Supplied contextual values not independently verified externally. | PERIPHERAL_COMPARISON |

## Limitations and completion

25 matched relationship families checked,including every primary/key-secondary duplicate result and all supplied planned statistical-design fields;9 findings and15 excluded apparent-observation patterns. Scientific coverage gaps:None. Exact intermediate graph trajectories are not printed and were not converted into invented precise quantities. Actual fitted secondary covariate coefficients,interim estimates and total person-time are not supplied. The cited final published protocol and separate nocturia publication are not supplied; alternatives involving those documents remain explicitly unconfirmed. No web or external evidence used. Original/final version and blinded-amendment context is retained in every relevant observation rather than interpreted as a protocol adjudication.
