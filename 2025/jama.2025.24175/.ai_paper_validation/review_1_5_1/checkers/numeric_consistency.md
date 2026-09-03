# Numeric Consistency Review

## Scope and method

This independent check covers all 125 stable numeric/reporting relationships in `relationships/numeric_relationship_inventory.md`: N001-N042 (main article), N043-N101 (DOC-002 protocol/SAP), and N102-N125 (DOC-003 supplement). I used the current 1.5.1 relationship maps as locators and checked direct-PDF evidence for the candidate observations below (including DOC-001 p. 7 and DOC-002 pp. 41, 48, and 50). No prior candidate, checker, or report output was used.

For counts and percentages, the numerical tolerance is ordinary display rounding: a printed one-decimal percentage must fall within 0.05 percentage points of `100*n/N`; integer totals must reconcile exactly unless the source labels categories as nonexclusive; and a displayed two-sided t-test P value is checked diagnostically against the displayed means, SDs, and arm sizes (rounding of inputs cannot explain an orders-of-magnitude discrepancy). Definitions, planned-versus-observed context, different document versions, and differing analysis populations were not silently treated as identical.

## Per-relationship coverage

`PASS` means the applicable arithmetic, denominator/proportion, total, population, unit/label, rate/count, repeated-value, and cross-location checks found no distinct candidate. `CANDIDATE PROPOSED` refers only to the detailed proposals below; it is not a stable candidate ID or adjudication.

### Main article, N001-N042

| ID | Direct source location and printed inputs checked | Applied check and result |
|---|---|---|
| N001 | DOC-001 pp. 1-2; ferritin >4420; SII ferritin <=4420 and HLA-DR <5000 | Threshold/unit/stratum-label check: PASS. |
| N002 | DOC-001 pp. 1-3; 33 sites; 1:1; q8h/q48h; 15 d; 200 mg IV/100 µg SC | Dose, schedule, unit, and site-count matching: PASS locally; cross-document site/dose comparisons are proposed below. |
| N003 | DOC-001 p. 3 Fig. 1; 672-391=281; listed exclusions 355+14+8+5+2+2+2+2+1 | Flow arithmetic: 391 and 281 reproduce exactly. PASS. |
| N004 | DOC-001 p. 3 Fig. 1; 135+146=281; 131+145=276; withdrawals 4+1=5 | Flow and primary-population total: PASS. |
| N005 | DOC-001 p. 3 Fig. 1; precision 35+18+8+1=62; placebo 51+19+2=72 | Treatment-discontinuation subgroup sums: PASS. |
| N006 | DOC-001 p. 3 Fig. 1; 59/131 and 66/145, total 125 | Subset numerator/denominator total: PASS. |
| N007 | DOC-001 pp. 1,6; N=276, 93 female (33.7%) | 93/276=33.70%; population/percentage check: PASS. |
| N008 | DOC-001 pp. 4,6; MALS 25+23=48; SII 106+122=228; 48+228=276 | Arm, stratum, and percentage reconciliation: PASS. |
| N009 | DOC-001 p. 6; deaths 21/131 and 29/145; 8.3% carried forward | 21/131=16.0%, 29/145=20.0%; stated carry-forward denominator not printed. PASS/no unsupported inference. |
| N010 | DOC-001 p. 4 Table 1; sex 89+42=131 and 94+51=145 | Sex totals and n(%) values: PASS. |
| N011 | DOC-001 p. 4 Table 1; 1+1+129=131; 0+0+145=145 | Race-category total and percentage rounding: PASS. |
| N012 | DOC-001 p. 4 Table 1; medical-history n(%) rows | Each row uses its randomized-arm denominator; categories are nonexclusive. PASS. |
| N013 | DOC-001 p. 4 Table 1; continued medical-history n(%) rows | Denominator/percentage and nonexclusive-category check: PASS. |
| N014 | DOC-001 p. 4 Table 1; ventilation 116/131,129/145; CVVH 23/131,24/145 | Percentages reproduce at one decimal; rows nonexclusive. PASS. |
| N015 | DOC-001 p. 4 Table 1; infection components 48+35+31+16+1=131; 54+32+44+12+3=145 | Mutually exclusive infection-category sums and n(%): PASS. |
| N016 | DOC-001 p. 4 Table 1; APACHE 38+93=131; 40+105=145 | Dichotomy sums and percentages: PASS. |
| N017 | DOC-001 p. 4 Table 1; CCI 54+77=131; 76+69=145 | Dichotomy sums and percentages: PASS. |
| N018 | DOC-001 p. 4 Table 1; SOFA 67+64=131; 68+77=145; scale 0-24 | Dichotomy, scale, unit, and median/IQR-label check: PASS. |
| N019 | DOC-001 p. 4 Table 1; ferritin medians/IQRs in ng/mL | Stratum and unit check: PASS. |
| N020 | DOC-001 p. 5 Table 1; mHLA-DR medians/IQRs | Unit/stratum-label check: PASS. |
| N021 | DOC-001 p. 5 Table 1; laboratory means (SD) | Measure/dispersion/unit-label check: PASS. |
| N022 | DOC-001 p. 5 Table 1; laboratory medians (IQR) | Ordering, measure, and unit-label check: PASS. |
| N023 | DOC-001 p. 5 Table 1; continued laboratory medians (IQR) | Ordering, measure, and unit-label check: PASS. |
| N024 | DOC-001 p. 5 Table 1; 36.0 (24.0-48.0), 47.0 (24.0-48.0) h | Median/IQR order and time unit: PASS. |
| N025 | DOC-001 pp. 1,3,5,7; >=1.4-point day-2-to-9 mean-SOFA decrease; 0-24 scale | Formula, direction, time window, and scale: PASS. |
| N026 | DOC-001 p. 5; secondary endpoints and >=15%/>8000 reversal thresholds | Endpoint, unit, and threshold labels: PASS. |
| N027 | DOC-001 p. 5; 40% vs 20%, alpha 5%, power 90%, 117/group, planned N=280 | Printed planning arithmetic is compatible with approximately 15% attrition after rounding; PASS. |
| N028 | DOC-001 pp. 1,6,7; 46/131=35.1%, 26/145=17.9%, difference 17.2 pp | Numerators, percentages, direction, and matched occurrences: PASS. |
| N029 | DOC-001 pp. 6-7; 57/131=43.5%, 72/145=49.7%, difference 6.1 pp | Numerators, percentages, and mortality time point: PASS. |
| N030 | DOC-001 pp. 6-7; 90/131=68.7%, 98/145=67.6%, difference 1.1 pp | Numerators, percentages, and mortality time point: PASS. |
| N031 | DOC-001 pp. 6-7; Table 2 52/131 (39.7%) versus narrative 51/131 (39.7%) | Exact cross-location count and percentage reconciliation: CANDIDATE PROPOSED. |
| N032 | DOC-001 pp. 6-7; 46/59=78.0%, 32/66=48.5%, total 125 | Subset percentages, difference, and total: PASS. |
| N033 | DOC-001 p. 6 Table 2; precision 58+11+32+30=131; placebo 46+9+44+46=145 | Day-15 disposition partitions and percentages: PASS. |
| N034 | DOC-001 p. 7; MALS 12+34=46, placebo 4+22=26 | Immune-state subgroup totals and n(%): PASS. |
| N035 | DOC-001 p. 7 Fig. 2; n=131 and n=145; days 1-9 | Figure denominator/time-window/endpoint label: PASS. |
| N036 | DOC-001 p. 8; 245/276=88.8%; 2+7+4=13; 3+2=5 SUSAR patients | Safety count, percentage, event-versus-patient label: PASS. |
| N037 | DOC-001 p. 8 Table 3; serious-AE n(%) rows | Arm denominators, percentage rounding, and event/patient framework: PASS. |
| N038 | DOC-001 p. 8 Table 3; continued safety rows | Arm denominators and event/patient framework: PASS. |
| N039 | DOC-001 p. 8 Table 3 footnote b; SOC rows are people, other rows events | Rate/count/event-versus-person label check: PASS. |
| N040 | DOC-001 p. 8; four hemorrhagic IFN-gamma cases with thrombocytopenia | Count statement has no incompatible denominator/comparator: PASS. |
| N041 | DOC-001 p. 9; cited-study values 35/65%, n=9, 34.5/15.1%,12.7/17% | Properly labeled external context, not current-trial values: PASS. |
| N042 | DOC-001 pp. 10-12; no result relationships | No applicable numeric unit: PASS. |

### DOC-002, N043-N101

| ID | Direct source location and printed inputs checked | Applied check and result |
|---|---|---|
| N043 | DOC-002 pp. 6-7; design/age >=18/day-9 endpoint | Definition and population check: PASS. |
| N044 | DOC-002 p. 6; rhIFN-gamma 100 µg SC q48h, anakinra 200 mg q8h for 15 d | Direct recheck: 100-µg dose agrees with DOC-001. Earlier 20-µg transcription is NOT REPRODUCED. |
| N045 | DOC-002 pp. 7,24-26; 1.4-point day-9 cutoff/target | Direct recheck: 1.4 agrees with report/SAP. Earlier 1.5-point transcription is NOT REPRODUCED. |
| N046 | DOC-002 pp. 9,13; entry ferritin <=4420 and HLA-DR <5000; SAP p.69 reversal >8000 | Direct recheck distinguishes 5000 entry from 8000 reversal. Earlier 8000-entry transcription is NOT REPRODUCED. |
| N047 | DOC-002 p. 10; 24 ImmunoSep sites; p. 9 concerns 14 PROVIDE sites | Protocol/SAP design agree at 24; consolidated 24/31/33 site-count comparison retained below. |
| N048 | DOC-002 pp. 11-13; SOFA >=2; <72h; ANC <1000; steroid cutoff | Threshold/unit/time-window definitions: PASS. |
| N049 | DOC-002 pp. 13-14; phenotype branches and <72h | Category/threshold/time-window check: PASS. |
| N050 | DOC-002 pp. 14-15; <72h allocation | Process-flow definition; no outcome total to reconcile. PASS. |
| N051 | DOC-002 p. 16; 1:1, 15 d, saline 20 mL/0.5 mL | Dose volume/schedule labels: PASS. |
| N052 | DOC-002 pp. 16-17; 2-8 C, >3 d outside 0-10 C | Range/order/unit check: PASS. |
| N053 | DOC-002 pp. 17-22; scheduled days 0,2,3,4,5,7,8,15,28,90 | Visit chronology and day-15/day-28/day-90 labels: PASS. |
| N054 | DOC-002 pp. 23-24; total 31.5 mL; aliquots 2.5+3+3+10+10+3 mL | Direct-page check: aliquots sum exactly to 31.5 mL. PASS. |
| N055 | DOC-002 p. 24; 1.4-point target, death-before-day-9 rule | Direct recheck corrects earlier 1.5 transcription; endpoint direction/time window: PASS. |
| N056 | DOC-002 p. 25; >=15% ferritin; >8000 and ferritin <4420 | Threshold/unit/compound-definition check: PASS. |
| N057 | DOC-002 pp. 25-26; 117/arm, about 15% drop-out, total 280 | Direct recheck corrects 112 to 117. Exact-15% inflation gives 276; the four-participant excess may be conservative rounding of “about 15%”; retained human question in NC-5. |
| N058 | DOC-002 p. 27; first treatment through 30 d/five half-lives | Safety-window label and units: PASS. |
| N059 | DOC-002 pp. 28-29; SAE criteria; severe not necessarily serious | Rate/count category-definition check: PASS. |
| N060 | DOC-002 pp. 29-32; 24 h and 15 d deadlines | Time-unit/order check: PASS. |
| N061 | DOC-002 pp. 38-40,46; 48+103+89=240 | Classification population totals: PASS. |
| N062 | DOC-002 p. 40; 88.3% day-1/day-2 reproducibility | Percentage denominator not printed; no unsupported arithmetic inference. PASS. |
| N063 | DOC-002 pp. 39-40; thresholds and 48/103/89 | Threshold and total check: PASS. |
| N064 | DOC-002 pp. 40-41; mortality percentages/CIs by class | Population/model denominator not printed in this relationship; no simple-total contradiction. PASS. |
| N065 | DOC-002 pp. 41-42,48; 21+15=36 | Randomized allocation total: PASS. |
| N066 | DOC-002 p. 41 narrative, p. 50 Fig. 1; 18/21 and 14/15 narrative; figure early deaths 18/21 and 11/15 | Matched-arm mortality-count inconsistency: CANDIDATE PROPOSED. |
| N067 | DOC-002 pp. 58-61; CPIS component 0-2 and time criteria | Score/threshold labels: PASS. |
| N068 | DOC-002 pp. 62-64; nine combinations | Algorithm count/branch label: PASS. |
| N069 | DOC-002 pp. 46-47; N=89,103,48 (total 240) | Table-column denominators: PASS. |
| N070 | DOC-002 pp. 46-47; Table 1 continuous mean±SD rows | Measure/dispersion/unit labels; no impossible range: PASS. |
| N071 | DOC-002 pp. 46-47; Table 1 categorical n(%) rows | Denominator/rounding and nonexclusive-row checks: PASS. |
| N072 | DOC-002 pp. 46-47; microbiology/comorbidity/antimicrobial n(%) rows | Denominator/rounding and nonexclusive-row checks: PASS. |
| N073 | DOC-002 p. 48; placebo n=21, personalized n=15 | Table denominator/test-label check: PASS. |
| N074 | DOC-002 p. 48 Table 2; APACHE 18.2±8.7 vs 30.5±9.4, p=.376, Student t test | Printed P is incompatible with displayed inputs: CANDIDATE PROPOSED. |
| N075 | DOC-002 p. 48; infection/comorbidity n(%) values | Percentages reproduce within tolerance; infection components 10+6+3+2=21 and 2+8+3+2=15. PASS. |
| N076 | DOC-002 p. 48; treatment n(%) values | Denominator/rounding and nonexclusive-treatment-row checks: PASS. |
| N077 | DOC-002 p. 49; SAE/AE n(%) with deaths excluded from P column | Event/person and p-column label check: PASS. |
| N078 | DOC-002 p. 50 Fig. 1; septic shock 177 but 44+2+132=178; no-shock 4+0+59=63 | Flow subgroup sum mismatch: CANDIDATE PROPOSED. |
| N079 | DOC-002 p. 51 Fig. 2; 69+37=106 deaths,34+52=86 survivors,103+89=192 | Diagnostic-table totals, sensitivity 69/106, specificity 52/86, PPV 69/103, NPV 52/89: PASS. |
| N080 | DOC-002 p. 51; n=40/43 and n=103/48 | Figure comparison denominators and labels: PASS. |
| N081 | DOC-002 p. 52; survival/death 96+144=240 and class components | Table totals and reference-group labels: PASS. |
| N082 | DOC-002 p. 53; n=20/14 day-7 analysis | Survivor population is explicitly different from randomized N; no improper denominator identity assumed. PASS. |
| N083 | DOC-002 pp. 54-57; administrative only | No applicable numeric result relationship: PASS. |
| N084 | DOC-002 p. 65; total 24 study sites | Consolidated study-site count comparison: CANDIDATE PROPOSED. |
| N085 | DOC-002 p. 65; ITT randomized patients/arm | Population definition check: PASS. |
| N086 | DOC-002 p. 66; 1.4-point day-2-to-9 threshold | Formula/threshold/time-window: PASS. |
| N087 | DOC-002 p. 66; 8 values/8, deaths=24, LOCF | Formula, scale, and missing-data rule: PASS. |
| N088 | DOC-002 p. 66; day-1 minus mean days 2-9 | Direction/scale formula: PASS. |
| N089 | DOC-002 p. 67; >1.4 responder, <=1.4 nonresponder | Threshold partitions exactly: PASS. |
| N090 | DOC-002 p. 67; 31 participating sites; >8% large-site rule | Consolidated study-site count comparison: CANDIDATE PROPOSED; 8% rule itself PASS. |
| N091 | DOC-002 p. 68; days 1-9 summed/9 among survivors | Formula/population/time-window label: PASS. |
| N092 | DOC-002 p. 68; 28- and 90-day mortality | Endpoint time-point distinction: PASS. |
| N093 | DOC-002 p. 68; days 2-15=14 values/14, deaths=24, LOCF | Formula, scale, and missingness rule: PASS. |
| N094 | DOC-002 p. 69; day-1 minus mean days2-15; >1.4 | Direction/time-window/threshold: PASS. |
| N095 | DOC-002 p. 69; >=15% and >8000 plus ferritin <4420 | Compound threshold/unit: PASS. |
| N096 | DOC-002 p. 70; >8000 restoration shorthand | Read with p. 69's complete definition; omission is not a printed contrary threshold. PASS. |
| N097 | DOC-002 p. 70; day-15 infection categories/strata | Endpoint/censoring/stratum label: PASS. |
| N098 | DOC-002 p. 70; serious/nonserious TEAE incidence by group/stratum | Rate-versus-count/stratum labels: PASS. |
| N099 | DOC-002 p. 71; ROC/Youden, 28-day total ITT | Population/outcome/cut-off definitions: PASS. |
| N100 | DOC-002 p. 71; APACHE/CCI/SOFA subgroup ORs | Subgroup/endpoint labels: PASS. |
| N101 | DOC-002 p. 72; 28- and 90-day ROC groups | Outcome/time-point/population labels: PASS. |

### DOC-003, N102-N125

| ID | Direct source location and printed inputs checked | Applied check and result |
|---|---|---|
| N102 | DOC-003 pp. 1,6-8 eTable 1; site screened/randomized rows, total randomization 276 | Component-site rows are support of N=276; no incomplete-row sum was treated as an arithmetic failure. PASS. |
| N103 | DOC-003 pp. 3-5; eligibility and assay thresholds | Units, cutoff directions, and 15-min time label: PASS. |
| N104 | DOC-003 pp. 11-12; >48 h, >=.25 ng/mL, <=60 mm Hg, <=90%, >=20/min, CPIS >=6 | Threshold/unit/direction check: PASS. |
| N105 | DOC-003 p. 13; MALS/SII classifier branches, <5000 HLA-DR | Mutually exclusive classification and units: PASS. |
| N106 | DOC-003 p. 14; n=131/145 microbiology n(%) | Denominators, rounding, and culture-unit label: PASS. |
| N107 | DOC-003 pp. 15-16; n=131/145; 34/41,33/38 subsets; 200 mg/day | Subset proportions, dose/unit and nonexclusive rows: PASS. |
| N108 | DOC-003 p. 20 eTable 8; each day measured+death(24)+LOCF=131/145; day9 100+21+10 and103+29+13 | Availability/imputation partition totals: PASS. |
| N109 | DOC-003 p. 22; 12/25,4/23,34/106,22/122 | n(%), subgroup sums, and difference labels: PASS. |
| N110 | DOC-003 p. 22; 12/25,5/23,40/106,29/122 | n(%), subgroup denominators, and day-15 label: PASS. |
| N111 | DOC-003 pp. 23-24; 125+151=276; sex 84+41=125 and99+52=151 | Subset total, sex totals, and nonexclusive rows: PASS. |
| N112 | DOC-003 pp. 25-26; SUSAR total 0+0+2+3=5; 5/276=1.8% | Safety total, percentage, and person/event labels: PASS. |
| N113 | DOC-003 pp. 27-29; any SAE 20+21+96+108=245; 245/276=88.8%; 3+8+67+167=245 | Safety totals, percentage, and relationship-row total: PASS. |
| N114 | DOC-003 pp. 30-43; any AE 20+20+104+112=256; 256/276=92.8% | Safety totals, rounding, and SOC-person/PT-event footnote: PASS. |
| N115 | DOC-003 p. 44; NNT/NNH 18 estimates and CIs | Measure/label checked; intervals crossing null/zero conventions need no numeric correction without an explicitly supplied transform rule. PASS. |
| N116 | DOC-003 p. 45; placebo145/precision131; days2-9 | Figure population/time-window labels: PASS. |
| N117 | DOC-003 p. 45; placebo145/precision131; days2-9 | Figure population/time-window labels: PASS. |
| N118 | DOC-003 p. 46; 38/121=31.4%,19/132=14.4% | Sensitivity denominators and percentages: PASS. |
| N119 | DOC-003 p. 47; risk sets 145 and131 then successive values | Survival risk-set counts are not event totals; labels/time point: PASS. |
| N120 | DOC-003 p. 48; risk sets 145 and131 then successive values | Survival risk-set counts are not event totals; labels/time point: PASS. |
| N121 | DOC-003 p. 49; four disposition percentages per arm | 22.9+24.4+8.4+44.3=100.0 and31.7+30.3+6.2+31.7=99.9 rounding. PASS. |
| N122 | DOC-003 p. 50; n=66/59, serial risk sets, >=2 draws | Subset denominators, time-to-event count label, and reversal thresholds: PASS. |
| N123 | DOC-003 p. 51; primary endpoint severity counts | Each split reproduces placebo 26/145 and precision46/131 across APACHE/CCI/SOFA partitions. PASS. |
| N124 | DOC-003 p. 52; 28-day mortality severity counts | Each split reproduces placebo72/145 and precision57/131 across partitions. PASS. |
| N125 | DOC-003 p. 53; 90-day mortality severity counts | Each split reproduces placebo98/145 and precision90/131 across partitions. PASS. |

## Distinct candidate proposals (no stable IDs; all pending human adjudication)

### NC-1 — Day-15 SOFA narrative count conflicts with Table 2 and its own percentage

- **Exact locations:** DOC-001 `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6`, Table 2; and `#page=7`, Secondary End Points narrative (N031).
- **Printed inputs:** Table 2 prints precision immunotherapy `52/131 (39.7%)`; the narrative prints `51 of 131 (39.7%)`. The placebo occurrence is `34/145 (23.4%)` in both contexts.
- **Rule/calculation/tolerance:** Exact matched endpoint/population count should agree. `52/131*100=39.6947%`, which rounds to 39.7%; `51/131*100=38.9313%`, which rounds to 38.9%, outside the one-decimal 39.7% tolerance interval [39.65,39.75).
- **Direct observation versus inference:** Directly observed: the two printed precision counts differ and only the Table-2 count produces its printed percentage. Inference: at least one occurrence may need correction; the source does not identify which.
- **Alternative:** The narrative could contain a transposed count, or Table 2 could be the inaccurate occurrence; an unstated analysis-set change is not supported because both state denominator 131 and describe the same day-15 endpoint.
- **Quality-control relevance:** The event count and percentage are reusable binary-outcome inputs.
- **Human question:** Which precision-immunotherapy numerator, 51 or 52, is the intended day-15 responder count, and should the matched text/table occurrence be corrected?

### NC-2 — Historical dose-comparison proposal: NOT REPRODUCED

- **Historical proposal provenance:** This proposal originally compared a purported DOC-002 `20 µg` dose with DOC-001 `100 µg` (N044/N002). It is retained to preserve proposal numbering and ledger provenance.
- **Direct recheck locations and inputs:** DOC-002 `joi250116supp1_prod_1771885794.26255.pdf#page=6` prints `sc rhIFNγ 100 µg once every other day`; DOC-001 `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2-3` prints `100 µg` SC every 48 hours for 15 days.
- **Rule/calculation/tolerance:** Matched dose, route, schedule, and duration should agree. The directly printed comparison is `100/100=1`; no fivefold difference exists.
- **Direct observation versus inference:** Direct observation is agreement at 100 µg. The earlier 20-µg value is not reproduced in the supplied direct PDF; its likely derivative-transcription origin is inference.
- **Alternative and human question:** An unsupplied approved version might differ, but no supplied direct page does. Should the mapping/ledger provenance be repaired to the direct 100-µg protocol dose?

### NC-3 — Historical responder-cutoff proposal: NOT REPRODUCED

- **Historical proposal provenance and direct inputs:** The original assertion of protocol `1.5` versus report/SAP `1.4` is **NOT REPRODUCED**. DOC-002 p. 7 and pp. 24-26, DOC-001, and SAP pp. 66-67 directly print 1.4 (N045, N025, N086, N089).
- **Rule/calculation/tolerance:** A matched responder cutoff should agree. Directly inspected supplied values give `1.4−1.4=0`; the asserted 0.1-point contradiction is not reproduced.
- **Direct observation versus inference:** Direct observation is agreement at 1.4. The prior 1.5 value is absent from the supplied direct evidence; its origin is inferred.
- **Alternative and human question:** An unsupplied version could differ. Should the mapping/ledger provenance be repaired to the direct 1.4-point cutoff?

### NC-4 — Historical entry-threshold proposal: NOT REPRODUCED

- **Historical proposal provenance and direct inputs:** The original 8000-entry versus 5000 proposal is **NOT REPRODUCED**. DOC-002 pp. 9 and 13, DOC-001, and DOC-003 p. 13 print entry HLA-DR below `5000`; SAP p. 69 prints above `8000` only for day-15 reversal (N046, N001, N105, N095).
- **Rule/calculation/tolerance:** Entry and reversal definitions must not be compared as the same identity. The direct entry sources agree at 5000, so the claimed entry contradiction is not reproduced.
- **Direct observation versus inference:** Direct observation is 5000 for entry and 8000 for reversal. The earlier transfer of 8000 into the entry definition is inferred.
- **Alternative and human question:** An unsupplied approved entry definition might differ. Should the mapping/ledger provenance explicitly distinguish the direct 5000 entry rule from the 8000 reversal rule?

### NC-5 — Protocol sample-size/dropout arithmetic: repaired inputs, residual human question

- **Exact location:** DOC-002 `joi250116supp1_prod_1771885794.26255.pdf#page=25-26` (N057).
- **Historical proposal provenance:** The original `112 per arm` premise is **NOT REPRODUCED** and is retained only for C005/NC-5 provenance.
- **Printed direct inputs:** `117 patients ... per trial arm`; `about 15%` dropout; total randomization `280`.
- **Rule/calculation/tolerance:** `2×117=234`; exact 15% inflation is `234/(1−.15)=275.29`, conventionally 276. A 280 target leaves 238 after exact 15% attrition (119/arm) and implies `1−234/280=16.43%` attrition. The four-participant excess over 276 may be conservative rounding of “about 15%,” rather than a contradiction.
- **Direct observation versus inference:** The printed 117/about-15%/280 values are direct. Any block-size, operational, or conservative-rounding rationale is inferred because it is not printed.
- **Quality-control relevance and human question:** Planning values are reusable. What rounding, randomization-block, or additional inflation convention produced N=280, and should the former 112-per-arm mapping/ledger premise be repaired?

### NC-6 — DOC-002 Figure 1 death count conflicts with narrative death count for personalized immunotherapy

- **Exact locations:** DOC-002 `joi250116supp1_prod_1771885794.26255.pdf#page=41`, Results narrative; and `#page=50`, Figure 1 (N066/N078).
- **Printed inputs:** Narrative: placebo `18` deaths, `85.7%` (18/21), and personalized immunotherapy `14` deaths, `93.3%` (14/15). Figure 1: placebo early termination because of death `n=18`; personalized-immunotherapy early termination because of death `n=11`; both arms are analyzed at n=21 and n=15.
- **Rule/calculation/tolerance:** For the same treatment arm and 28-day/early-termination death count, matched flow and narrative counts should agree. The placebo values agree. In the personalized arm, 11/15=73.3%, whereas the narrative's 14/15=93.3%; this is not rounding.
- **Direct observation versus inference:** Directly observed: 11 and 14 are printed for the personalized arm. Inference: the figure, narrative, or the implicit endpoint-period labeling may be inaccurate; the figure does not explicitly print “28-day.”
- **Alternative:** The 11 figure deaths may use a shorter follow-up window than the narrative's 28-day mortality, though the flow does not state that distinction.
- **Quality-control relevance:** Mortality count and follow-up definition are direct outcome inputs.
- **Human question:** Does Figure 1's `n=11` represent a different time window from 28-day mortality, or should either the figure count or narrative death count be corrected/labeled?

### NC-7 — APACHE II Table 2 P value is incompatible with its displayed t-test inputs

- **Exact location:** DOC-002 `joi250116supp1_prod_1771885794.26255.pdf#page=48`, Table 2 (N074); direct page render confirms the printed values and footnote `* comparison by the Student's t-test`.
- **Printed inputs:** Placebo n=21, APACHE II `18.2 ± 8.7`; personalized immunotherapy n=15, `30.5 ± 9.4`; printed `P=.376*`.
- **Rule/calculation/tolerance:** From displayed values, Welch diagnostic statistic is `(30.5-18.2)/sqrt(8.7^2/21+9.4^2/15)=3.99`, with approximately 30 df and two-sided P about .0004. A pooled-variance calculation is similarly below .001. Rounding means/SDs at one decimal cannot yield .376.
- **Direct observation versus inference:** Directly observed: group sizes, means, SDs, P value, and t-test footnote. Inference: the P value may be transposed from another row or a table cell/analysis may be mislabeled; the exact production cause is not supplied.
- **Alternative:** A different, unreported APACHE transformation or dataset could have been tested, but that would conflict with the printed Student-t-test row label.
- **Quality-control relevance:** Baseline severity comparison and its P value can be reused as a reported balance result.
- **Human question:** Which APACHE-II P value/test input is correct for these displayed Table-2 groups, and was `.376` transposed or generated from a different analysis?

### NC-8 — Septic-shock classification subgroup total exceeds Figure 1 parent count

- **Exact location:** DOC-002 `joi250116supp1_prod_1771885794.26255.pdf#page=50`, Figure 1 (N078).
- **Printed inputs:** Parent box: `Septic shock = 177`. Its classification box: MALS `44 (24.8%)`, immunoparalysis `2 (1.1%)`, intermediate `132 (74.0%)`.
- **Rule/calculation/tolerance:** Mutually displayed classification groups should partition the parent: `44+2+132=178`, one more than 177. The listed percentages sum to 99.9% from rounding but their counts cannot sum to the stated parent.
- **Direct observation versus inference:** Directly observed: parent and three child counts. Inference: one child count or parent count may be a typographic error; source does not state a fourth category.
- **Alternative:** One participant may have had more than one classification, but Figure 1 depicts mutually exclusive classification branches and gives no overlap label.
- **Quality-control relevance:** The flow/classification denominator affects reported group sizes and classification proportions.
- **Human question:** Which Figure-1 count is intended—septic shock parent 177 or one of the three classification counts—and was an overlap/unclassified participant omitted from the labeling?

### NC-9 — Study-site totals use three directly printed values

- **Historical proposal provenance and exact locations:** The original 28-site protocol value and DOC-001 p. 1 citation are **NOT REPRODUCED**. DOC-001 `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2` prints `33 sites`; DOC-002 protocol `joi250116supp1_prod_1771885794.26255.pdf#page=10` prints `24` ImmunoSep sites (p. 9 concerns `14` PROVIDE sites); SAP pp. 65 and 67 print `24` and `31 participating sites`, respectively (N002, N047, N084, N090).
- **Rule/calculation/tolerance:** A site count should match or specify planned versus activated versus participating context. The directly printed ImmunoSep values are 24, 31, and 33; the protocol/SAP-design value 24 agrees. They cannot be reconciled by rounding.
- **Direct observation versus inference:** Direct observation is the 24/31/33 chain. Planning-versus-participating-versus-final context is inference because the sources provide no explicit crosswalk.
- **Alternative:** The counts may intentionally describe distinct milestones rather than one total.
- **Quality-control relevance:** Site count is a trial-scale descriptor used in study characterization and cross-document verification.
- **Human question:** What does each site count measure (planned, approved, activated, recruiting, or contributing), and should the report identify the final participating-site count explicitly?

## Summary and limitations

- Relationships checked: **125/125**.
- Numbered proposal records retained: **9**. NC-2, NC-3, and NC-4 are historical proposals marked **NOT REPRODUCED** after direct-source repair; NC-5 has repaired 117-per-arm inputs and retains only its bounded rounding/inflation human question.
- Relationship records in the remaining direct-source observations: **9** (N002, N031, N047, N057, N066, N074, N078, N084, and N090). The four site-count records are one consolidated proposal; N078 supports two nonduplicate rules (mortality-count comparison and classification-subgroup sum).
- No display-zero P-value occurrence was proposed as a candidate.
- Limitations: DOC-002 has font-encoded native text, so direct rendered pages were necessary for repair confirmation. The supplied material lacks amendment history, site chronology, and planning-rounding conventions; remaining alternatives are retained for human adjudication rather than resolved here.
