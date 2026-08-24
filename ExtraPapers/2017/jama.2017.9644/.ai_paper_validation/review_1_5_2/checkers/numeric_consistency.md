# Numeric Consistency Review

## Scope and method

Complete fresh review of all 81 stable numeric/reporting relationships (`N001`–`N081`). Evidence was read from the direct PDFs and fresh layout/render assets cited in the two extraction maps. Calculations use the printed numerator/denominator, integer total, or stated definition. Percentages are accepted when the absolute difference between printed and computed percentage is at most 0.06 percentage points (one-decimal rounding, allowing endpoint representation effects), unless a different printed precision is stated. A displayed adjusted effect is not required to equal an unadjusted raw difference. No legacy audit artifact or external source was used.

`PASS` means the stated arithmetic, identity, label, or cross-location check reconciled at the displayed precision. `NO_APPLICABLE_ARITHMETIC` means the relationship is a definition, time/window, or qualitative/contextual value for which no source-grounded arithmetic comparison exists. `SIGNAL` is a provisional candidate signal only; it has no candidate ID, disposition, or severity.

## Explicit record for every stable N relationship

| ID | Exact source location | Check and reproducible result | Status |
|---|---|---|---|
| N001 | DOC-001 p1, p4, p7 | 192 + 189 = 381; all repeated group totals match. | PASS |
| N002 | DOC-001 p1 | Trial period, 8 centers, and 6-hour window are descriptive identifiers; no conflicting occurrence mapped. | PASS |
| N003 | DOC-001 p1, p3 | Primary endpoint is consistently mTICI 2b/3 after all procedures. | PASS |
| N004 | DOC-001 p1, p4 | 174/381=45.67%=45.7%; 363/381=95.28%=95.3%; timing matches repeated summary. | PASS |
| N005 | DOC-001 p1, p6 | 164/192=85.42%=85.4%; 157/189=83.07%=83.1%; raw difference=2.35 pp=2.4 pp. Abstract, text, and Table 2 agree. | PASS |
| N006 | DOC-001 p1, p6-p7 | Named NIHSS-24-h, mRS-90-d, death-90-d, and procedure-event outcomes retain their time labels. | PASS |
| N007 | DOC-001 p2 | Eligibility/population definitions do not conflict with reported randomized population. | PASS |
| N008 | DOC-001 p2 | 1:1 allocation and center/IV-tPA strata are consistent with the reported adjustment labels. | PASS |
| N009 | DOC-001 p3 | At least 3 assigned attempts before rescue and all-procedure endpoint distinguish first-line/all-procedure quantities. | PASS |
| N010 | DOC-001 p3 | Secondary endpoint labels distinguish mTICI threshold, time, and clinical scale. | PASS |
| N011 | DOC-001 p3, p8 | Symptomatic ICH definition (ICH plus NIHSS worsening >=4 or death) is compatible with Table 3 label. | PASS |
| N012 | DOC-001 p4 | 640 assessed - 259 excluded = 381 randomized. | PASS |
| N013 | DOC-001 p4 | 61 + 113 + 77 + 2 = 253 not meeting inclusion criteria. | PASS |
| N014 | DOC-001 p4 | Contact: 174+18=192 and 15+3=18. Stent: 170+19=189 and 12+1+5+1=19. | PASS |
| N015 | DOC-001 p4, p6 | 181+11=192; 176+13=189; 357/381=93.70%=93.7%. | PASS |
| N016 | DOC-001 p4, p7 | 181+11=192; 182+6+1=189; 181+182=363 and 363/381=95.3%. | PASS |
| N017 | DOC-001 p4, p1, p5 | Overall NIHSS 16.2 and onset-to-puncture 227 min agree with abstract; group Table-1 values are compatible descriptive components. | PASS |
| N018 | DOC-001 p5 Table 1 | Men: 103/192=53.65%=53.7%; 104/189=55.03%=55.0%. Ages are correctly labelled mean (SD), years. | PASS |
| N019 | DOC-001 p5 Table 1 | Each hypertension/diabetes/lipid/smoking fraction recalculates within 0.05 pp; unequal denominators are stated missing-data denominators, not a total partition. | PASS |
| N020 | DOC-001 p5 Table 1 | Each vascular-history/antithrombotic fraction recalculates within rounding tolerance. Antiplatelet and anticoagulant are not stated mutually exclusive. | PASS |
| N021 | DOC-001 p5 Table 1 | BP and NIHSS retain mean(SD) and stated units/scale; NIHSS missingness is 3 total (1 contact), compatible with 191+187 observed values. | PASS |
| N022 | DOC-001 p5 Table 1 | Contact prestroke-mRS counts 158+17+5+8+2=190; stent 159+16+11+3=189; percentages reconcile. | PASS |
| N023 | DOC-001 p5 Table 1 | ASPECTS scale is 0-10 with higher=fewer changes; 5 missing (1 contact) means 191 contact and 185 stent observations if the footnote applies to this measure, which is compatible with the group totals. | PASS |
| N024 | DOC-001 p5 Table 1 | Contact 100+48+22+4=174; stent 104+31+33+8=176; 174+176=350=381-(27 spontaneous lysis+4 groin failures). | PASS |
| N025 | DOC-001 p5 Table 1 | Clot-burden scale 0-10 with lower=higher burden is consistent; 254 assessed with 129 contact gives 125 stent; clot length 293 with 147 contact gives 146 stent. | PASS |
| N026 | DOC-001 p5 Table 1 | Arterial-occlusion scores: contact 153+1+13+10=177; stent 160+2+8+5=175. | PASS |
| N027 | DOC-001 p5 Table 1 | 37/146=25.34%=25.3%; 37/138=26.81%=26.8%; favorable collateral definition is 3-4 on a 0-4 scale. | PASS |
| N028 | DOC-001 p5 Table 1 | Cause categories: 13+88+91=192 and 17+75+97=189; rounded percentages total 100.0 each. | PASS |
| N029 | DOC-001 p5 Table 1 | Admission/rtPA/anesthesia fractions recalculate; anesthesia denominators 191+188=379 match 3 missing (1 contact). | PASS |
| N030 | DOC-001 p5 Table 1 | All four timing measures are consistently labelled minutes and median(IQR); no arithmetic identity applies. | PASS |
| N031 | DOC-001 p5 Table 1 footnotes | Footnote missingness accords with relationship-specific denominators N021-N030; no unsupported pooled denominator was used. | PASS |
| N032 | DOC-001 p6 Table 2 | 164/192=85.4%, 157/189=83.1%; raw difference 2.35 pp is compatible with adjusted RD 2.4 pp; exact repeats N005. | PASS |
| N033 | DOC-001 p6 Table 2 | 140/153=91.50%=91.5%; 140/165=84.85%=84.9%; separate per-protocol population makes it non-comparable as an ITT total. | PASS |
| N034 | DOC-001 p6 Table 2 | 163/192=84.9%; 163/189=86.2%; study-site sensitivity is explicitly distinct from core-lab result. | PASS |
| N035 | DOC-001 p6 Table 2 | 72/192=37.5%; 73/189=38.6%; mTICI 3 is a subset endpoint with correctly signed raw difference -1.1 pp. | PASS |
| N036 | DOC-001 p6 Table 2 | 108/192=56.3%; 107/189=56.6%; raw difference -0.3 pp is compatible with adjusted RD +0.4 pp. | PASS |
| N037 | DOC-001 p6 Table 2 | 121/192=63.0%; 128/189=67.7%; raw difference -4.7 pp. | PASS |
| N038 | DOC-001 p6 Table 2 | 55/192=28.646%=28.7% and 67/189=35.450%=35.5% at displayed one-decimal precision; raw difference -6.8 pp. | PASS |
| N039 | DOC-001 p6 Table 2 | 83/192=43.2%; 94/189=49.7%; raw difference -6.5 pp. | PASS |
| N040 | DOC-001 p6, p7 | 63/192=32.8%; 45/189=23.8%; raw difference 9.0 pp; repeated narrative agrees. | PASS |
| N041 | DOC-001 p6 Table 2 | NIHSS change is mean change, not a count/rate; adjusted mean difference 0.38 is within its printed CI -1.42 to 2.18. | PASS |
| N042 | DOC-001 p6, p7 | 82/181=45.3%; 91/182=50.0%; denominators equal completed/dead follow-up cohorts, and repeated narrative agrees. | PASS |
| N043 | DOC-001 p6 | mRS retains ordinal 0-6 scale, 5+6 combination, and common-OR improvement direction; 0.76 CI 0.53-1.10 includes 1. | PASS |
| N044 | DOC-001 p6 footnotes | mTICI 0-3/2a/2b/2c labels and 11/13 unavailable core-lab counts agree with N015. | PASS |
| N045 | DOC-001 p6 | 181+176=357; 357/381=93.7%. The 92% balloon-guide statement lacks numerator, so no count reconstruction is justified. | PASS |
| N046 | DOC-001 p7 | First-line failures 68+51=119; rescue 57/68=83.8%, 42/51=82.4%; all-group rescue repeats N040. | PASS |
| N047 | DOC-001 p7 | Attempts and time are labelled median(IQR; range) and minutes; subset time denominator is not printed, so no unsupported denominator test. | PASS |
| N048 | DOC-001 p7 Figure 2A | Contact segments 8+2+18+92+72=192 and stent 5+5+22+84+73=189; 2b+3 gives 164/157, matching Table 2. | PASS |
| N049 | DOC-001 p7 Figure 2B | Contact segments 26+6+39+66+55=192 and stent 20+9+32+61+67=189; 2b+3 gives 121/128, matching Table 2 first-line outcome. | PASS |
| N050 | DOC-001 p7 Figure 2 footnotes | Four groin failures as mTICI 0 and 20 all-procedure/22 first-line site substitutions match stated missingness handling. | PASS |
| N051 | DOC-001 p7 Figure 2A-B | Axis says “Patients, %”; embedded integers total group n and reproduce count numerators. See SIG-N051 below. | SIGNAL |
| N052 | DOC-001 p6-p7 | NIHSS, mRS-assessed 363/381=95.3%, mRS<=2 fractions/effects, and common OR repeat Table 2 at same precision. | PASS |
| N053 | DOC-001 p7, p8 | Death: 35+35=70 and 70/363=19.3%. In the stent column, intracranial hemorrhage prints 85/188 (46.2), but 85/188=45.2% at one decimal; symptomatic ICH prints 12/188 (6.5), but 12/188=6.4%. | SIGNAL |
| N054 | DOC-001 p7, p8 | Pooled events equal Table 3 pairs: SAH 13+13=26; vasospasm 5+12=17; embolization 7+5=12; perforation 5+3=8; dissection 5+2=7. | PASS |
| N055 | DOC-001 p8 Table 3 | Death and component count sums reconcile. In the stent column, hemorrhagic infarction 49/188 computes 26.1%, not 26.6%; type 1 24/188 computes 12.8%, not 13.0%; type 2 25/188 computes 13.3%, not 13.6%. | SIGNAL |
| N056 | DOC-001 p8 Table 3 | Parenchymal-hematoma component counts sum 19+14=33, but the stent fraction 33/188 computes 17.6%, not 17.4%; type 1 19/188 computes 10.1%, not 10.3%; type 2 14/188 computes 7.4%, not 7.6%. Intraventricular/remote rows explicitly use 184 and reconcile. | SIGNAL |
| N057 | DOC-001 p8 Table 3 | In the stent column, symptomatic ICH 12/188 computes 6.4%, not 6.5%, and subarachnoid hemorrhage 13/188 computes 6.9%, not 7.1%. Other listed fractions checked here reconcile. The multiple-event footnote affects cross-row totals, not within-row fraction arithmetic. | SIGNAL |
| N058 | DOC-001 p8 Table 3 footnotes | Count-once-per-event-type and HI/PH definitions support N054-N057 and prevent invalid component-total comparison. | PASS |
| N059 | DOC-001 p8 | Exploratory clot-contact time is 13 vs 22 minutes with explicit unplanned status; no denominator/effect scale is printed. | PASS |
| N060 | DOC-001 p8, p4 | 381 and 8 centers repeat N001/N002. “90% received allocated treatment” is compatible with 344/381=90.3% (174+170 assigned-technique receipt); rescue/crossover labels remain distinct. | PASS |
| N061 | DOC-001 p8-p9 | Discussion endpoint/direction statements match Table 2/3; no numerical claim contradicts the printed intervals. | PASS |
| N062 | DOC-001 p9, p8 | In-study different-territory embolization 7/192=3.65%=3.7%; external retrospective figures are explicitly contextual and not trial comparators. | PASS |
| N063 | DOC-001 p9, p3 | Stated 15% superiority target is consistently labelled as design premise; conclusion does not relabel the study as equivalence/noninferiority. | PASS |
| N064 | DOC-002 p2 | 84% vs 68% historical observational result is explicitly external/background; it is not a trial-result denominator or matched report comparison. | PASS |
| N065 | DOC-002 p2-p3 | Planned outcomes and subgroup/time labels establish comparison identities; no result arithmetic applies. | PASS |
| N066 | DOC-002 p3 | Age >18, artery, six-hour, 1:1/strata definitions match the protocol’s own population specification. | PASS |
| N067 | DOC-002 p4-p5 | Maximum three passes, discretionary rescue, and ITT retention are coherent definitions, not mutually exclusive totals. | PASS |
| N068 | DOC-002 p5, p12 | Protocol primary TICI 2b-3/final angiography and TICI threshold >=50% are internally consistent; article’s mTICI wording is a terminology difference, not a numeric contradiction. | PASS |
| N069 | DOC-002 p13 | mRS categories are consecutively 0 through 6; mRS<=2 favorable definition is scale-compatible. | PASS |
| N070 | DOC-002 p6 | Planned 27-month study, 24-month inclusion, maximum 3-month participation and scheduled 24-hour/90-day outcomes are not observed result totals. | PASS |
| N071 | DOC-002 p6-p7 | Planned categorical frequency/% and continuous summary/test labels are internally coherent. | PASS |
| N072 | DOC-002 p7 | 85%-70%=15 percentage points; (85-70)/70=21.43% relative increase. Sentence says “increase ... by 21%” without scale. See SIG-N072. | SIGNAL |
| N073 | DOC-003 p2-p3; DOC-001 p4,p6 | Missing mTICI: groin failures n=4 as 0; absent core read replaced by site result n=20 at end procedure/n=22 first line. These agree across supplied report/supplement. | PASS |
| N074 | DOC-003 p4; DOC-001 p4 | Frontline rows total 174 aspiration and 186 stent devices, whereas headers are 174/175. Rows are device uses, and multiple devices per patient are permitted; 175 stent-first versus main flow 170 received assigned stent remains undefined. See SIG-N074. | SIGNAL |
| N075 | DOC-003 p4; DOC-001 p6-p7 | Rescue device rows total 84 aspiration and 74 stent, vs headers 63/45; a device-detail table plus multiple attempts/switching prevents a participant-total contradiction. 63/45 exactly match main rescue patient counts. | PASS |
| N076 | DOC-003 p5; DOC-001 p7 | mRS counts: 24+35+23+25+25+14+35=181; 40+38+13+26+17+13+35=182; total 363 matches completed assessment. | PASS |
| N077 | DOC-003 p6; DOC-001 p6 | Overall 164/192=85.4% and 157/189=83.1%, with matched primary outcome definition and displayed OR/P, repeat Table 2. | PASS |
| N078 | DOC-003 p6 | IV-rtPA subgroup partitions: aspiration 56+108=164 and 66+126=192; stent 50+107=157 and 65+124=189. | PASS |
| N079 | DOC-003 p6; DOC-001 p5 | Site denominator sums 170/192 and 168/189, not full group. Source does not call them a complete partition; available site values match Table 1 category counts, so no missingness contradiction. | PASS |
| N080 | DOC-003 p6; DOC-001 p5 | CBS denominators sum 129/192 and 125/189, consistent with assessed CBS totals. Scale is 0-10, with lower CBS=higher burden; no full-partition claim. | PASS |
| N081 | DOC-003 p6; DOC-001 p5 | Clot-length denominators sum 147/192 and 146/189, matching 293 assessed; unplanned label and <8/>=8 categories are clear. | PASS |

## Provisional candidate signals

### SIG-N053A — Table 3 stent intracranial-hemorrhage fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: stent-retriever intracranial hemorrhage `85/188 (46.2)`.
- **Comparator/rule/calculation:** `85 / 188 × 100 = 45.2128%`, which rounds to `45.2%`, not `46.2%`.
- **Alternative:** `85/184=46.2%`; nearby stent rows explicitly print denominator 184, so either the denominator or percentage may reflect another analysis total. The source does not identify which element governs this row.
- **Exact human question:** What denominator produced 46.2%, and should the printed fraction or percentage be revised?

### SIG-N053B — Table 3 stent symptomatic-ICH fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: stent-retriever symptomatic intracranial hemorrhage `12/188 (6.5)`.
- **Comparator/rule/calculation:** `12 / 188 × 100 = 6.3830%`, which rounds to `6.4%`, not `6.5%`.
- **Alternative:** `12/184=6.5%`; the intended denominator is not stated separately from the printed 188.
- **Exact human question:** Does 6.5% use an intended denominator of 184, or is the percentage inconsistent with the printed fraction?

### SIG-N055A — Table 3 stent hemorrhagic-infarction fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `49/188 (26.6)`.
- **Comparator/rule/calculation:** `49 / 188 × 100 = 26.0638%`, which rounds to `26.1%`, not `26.6%`.
- **Alternative:** `49/184=26.6%`; an intended 184 denominator would reconcile, but the printed denominator is 188.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N055B — Table 3 stent hemorrhagic-infarction type 1 fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `24/188 (13.0)`.
- **Comparator/rule/calculation:** `24 / 188 × 100 = 12.7660%`, which rounds to `12.8%`, not `13.0%`.
- **Alternative:** `24/184=13.0%`; the printed row does not name 184.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N055C — Table 3 stent hemorrhagic-infarction type 2 fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `25/188 (13.6)`.
- **Comparator/rule/calculation:** `25 / 188 × 100 = 13.2979%`, which rounds to `13.3%`, not `13.6%`.
- **Alternative:** `25/184=13.6%`; the intended denominator is unresolved.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N056A — Table 3 stent parenchymal-hematoma fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `33/188 (17.4)`.
- **Comparator/rule/calculation:** `33 / 188 × 100 = 17.5532%`, which rounds to `17.6%`, not `17.4%`.
- **Alternative:** The percentage may use an unprinted row-specific denominator; neither 188 nor the nearby 184 denominator yields 17.4% at one decimal.
- **Exact human question:** What denominator produced 17.4%, and which printed element is intended?

### SIG-N056B — Table 3 stent parenchymal-hematoma type 1 fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `19/188 (10.3)`.
- **Comparator/rule/calculation:** `19 / 188 × 100 = 10.1064%`, which rounds to `10.1%`, not `10.3%`.
- **Alternative:** `19/184=10.3%`; the printed row does not state that denominator.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N056C — Table 3 stent parenchymal-hematoma type 2 fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `14/188 (7.6)`.
- **Comparator/rule/calculation:** `14 / 188 × 100 = 7.4468%`, which rounds to `7.4%`, not `7.6%`.
- **Alternative:** `14/184=7.6%`; the intended denominator is unresolved.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N057A — Table 3 stent subarachnoid-hemorrhage fraction does not reproduce

- **Exact location and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=8`, Table 3: `13/188 (7.1)`.
- **Comparator/rule/calculation:** `13 / 188 × 100 = 6.9149%`, which rounds to `6.9%`, not `7.1%`.
- **Alternative:** `13/184=7.1%`; the printed denominator is 188.
- **Exact human question:** Which denominator and percentage are intended for this row?

### SIG-N051 — Figure 2 count-versus-percent display-label ambiguity

- **Exact locations and printed inputs:** `jama_lapergue_2017_oi_170084.pdf#page=7`, Figure 2A-B. Axis: “Patients, %.” Figure 2A contact embedded values `8, 2, 18, 92, 72`, group `n=192`; stent values `5, 5, 22, 84, 73`, group `n=189`.
- **Comparator/rule/calculation:** An axis labelled as a percentage display normally identifies segment values as percentages or makes the unit clear. Here the embedded values sum to `192` and `189` and 2b+3 equals the Table-2 count numerators `164` and `157`, so the embedded integers act as counts while bar geometry is percentage-scaled.
- **Tolerance:** exact integer sums; no rounding tolerance needed.
- **Direct observation versus inference:** Directly observed: the axis wording and all embedded integers. Inference: the values are count-like and the presentation could leave the embedded-number unit ambiguous.
- **Alternative:** The figure may intentionally use a percentage axis while showing unlabelled count labels, a valid combined display convention.
- **Quality-control relevance:** A reader extracting Figure-2 values could confuse count and percentage units, with bounded downstream evidence-reuse risk.
- **Exact human question:** Does Figure 2 intentionally combine percentage-scaled bars with embedded counts, and if so should the embedded number unit be labelled explicitly?

### SIG-N072 — protocol sample-size effect-scale wording ambiguity

- **Exact location and printed inputs:** `joi170084supp1_prod.pdf#page=7`, lines 288-295: stent-retriever rate `70%`, ADAPT rate `85%`, and “increase ... by `21%`.”
- **Comparator/rule/calculation:** `85%-70%=15` percentage points, whereas `15/70=21.43%` relative increase. Thus `21%` reconciles only if it denotes a relative increase, not an absolute percentage-point increase.
- **Tolerance:** 21% is within normal whole-percent rounding of 21.43% relative increase.
- **Direct observation versus inference:** Directly observed: all three printed percentages/wording. Inference: the sentence leaves the measurement scale unstated.
- **Alternative:** “21%” may be conventional relative-effect wording and not an error.
- **Quality-control relevance:** Sample-size premises can be misabstracted if the effect scale is not stated.
- **Exact human question:** Was the stated 21% intended as a relative increase, and should the protocol label it explicitly as relative rather than percentage points?

### SIG-N074 — frontline stent-retriever denominator/label mismatch across eTable and flow diagram

- **Exact locations and printed inputs:** `joi170084supp2_prod.pdf#page=4`, eTable “Frontline Strategy” has Stent Retriever First `(n=175)`; its stent-column device rows sum to `186`. `jama_lapergue_2017_oi_170084.pdf#page=4`, Figure 1 reports `189` randomized to stent retriever and `170` received a stent retriever as randomized.
- **Comparator/rule/calculation:** The table title says device details “According to the Assigned Groups,” yet the frontline header uses `175`, not the flow’s `170` assigned-stent recipients or `189` randomized. Device-row total `1+1+2+1+101+56+9+1+1+3+8+2=186`, confirming rows are not necessarily mutually exclusive patients. The source does not define what patient/event denominator `175` represents.
- **Tolerance:** integer identity comparison; no rounding tolerance applies.
- **Direct observation versus inference:** Directly observed: 175, 170, 189, and the row counts/labels. Inference: the table header may use a device-use or treatment-exposure population different from flow receipt.
- **Alternative:** Five participants not receiving a stent “as randomized” may nevertheless have stent-retriever frontline use under another table definition, or the header may count procedures rather than patients.
- **Quality-control relevance:** An undefined denominator can misstate treatment uptake or create incorrect device-use totals in later data extraction.
- **Exact human question:** What exactly does the eTable’s “Stent Retriever First (n=175)” count, and how does it reconcile with 170 patients reported as receiving a stent retriever as randomized?

## Completion and limitations

- Stable N records completed: 81/81 (`N001`–`N081`).
- Provisional qualifying signals: 12 (`SIG-N051`, `SIG-N053A`, `SIG-N053B`, `SIG-N055A`, `SIG-N055B`, `SIG-N055C`, `SIG-N056A`, `SIG-N056B`, `SIG-N056C`, `SIG-N057A`, `SIG-N072`, `SIG-N074`).
- No display-zero P value was registered as a signal or candidate. No C IDs, severity labels, validity determinations, or dispositions were assigned.
- Limitation: direct-source PDFs do not define the eTable’s `n=175` denominator or provide protocol amendment/SAP-version provenance. This review therefore records the printed discrepancy/ambiguity and its alternatives without asserting cause.
