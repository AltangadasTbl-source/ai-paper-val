# Statistical relationship inventory — support pass 1 shard

Runtime agent: agent:/root/statistics_one_support; fresh spawn; gpt-6.1-sol; reasoning effort high. Pass 1 only. Exact assigned scope: S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271. These canonical IDs are retained.

Counts: 41 relationship families; six sensitivity result rows; 21 site families/42 site rows; 14 side-effect families/28 Yes-No pairs. Direct DOC-004 results pages2–6 were read as newly rendered source images and fresh sorted-layout/native text. All 41 IDs receive PASS_1_COMPLETE below. Source-method pages from the main article3–4 and SAP12–14 were consulted solely to interpret this assigned result scope; independent main/PLAN checks belong to the other shard.

## Source grounding and tooling

DOC-004 is REPORT by content: populated trial-result tables. Effect contrast is sildenafil citrate versus placebo; RR null1, 95%CI, two-tailed P<.05 from [REPORT main p.4](../../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4). Models are printed in DOC-004 table footnotes. [PLAN SAP p.12](../../../../joi250034supp2_prod_1750956984.11521.pdf#page=12), [p.13](../../../../joi250034supp2_prod_1750956984.11521.pdf#page=13), and [p.14](../../../../joi250034supp2_prod_1750956984.11521.pdf#page=14) define GEE correlation, independent GLM comparisons, actual-treatment safety sets, and the four sensitivity strategies. No superiority, noninferiority, equivalence, interim or stopping conclusion is printed in these assigned result tables. Multiplicity and prospective comparison are reviewed in the independent main/PLAN shard; the site analysis is expressly post hoc in main p.4.

Fresh derivatives under preprocessing/statistics_one_support/: results-pages2-6.layout.txt (package-local pdf_tools.py, PyMuPDF1.26.4 sorted reading order, CPU); page-2.png, page-3.png, page-4.png, page-5.png, page-6.png (same helper/PyMuPDF1.26.4, 200dpi, CPU); main-methods3-4.native.txt and SAP-methods12-14.native.txt (same helper/PyMuPDF1.26.4 native text, CPU). Every image was visually inspected. No fresh OCR or GPU processing was necessary. Supplied sources and reused derivatives were preserved.

## Complete assigned evidence

The following populated values were copied from the current support map and checked afresh against exact source pages. Empty cells and printed dashes remain explicit; no placeholder result has been introduced.

## DOC-004 eTable 1: all sensitivity results

Exact REPORT source: [PDF page 2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2). Columns always SC versus placebo. Header randomized babies SC N=1634, P N=1641. Counts in rows use their own outcome denominator. All intervals95%CI and effect measure printed RR. For this table GEE log-binomial adjusts twin clustering; GLM log-binomial does not. Footnote18sets of twins. “Not Done” cordpH<7 assumed No for non-imputed composite; imputation adds not-done events using pooled tested event rate with none of other components, stratified twin status. Indicator models include cord-testing “Not Done” to adjust imputation. Missing is preserved separately from Not Done.

| N/S locator | Result/model/contrast | SC all printed categories | Placebo all printed categories | RR(95%CI); P | Matching main/SAP key |
|---|---|---|---|---|---|
| N201 / S231 | Composite10, pH imputed, GEE | Yes85/1625(5.2%); No1540/1625(94.8%); Missing9 | Yes87/1625(5.4%); No1538/1625(94.6%); Missing16 | 1.01(0.75–1.36); .943 | primary sensitivity imputed composite / S224,S225 |
| N202 / S232 | pH<7.0 after imputation, GEE | Yes14/1629(0.9%); No1211/1629(74.3%); NotDone404/1629(24.8%); Missing5 | Yes8/1637(0.5%); No1154/1637(70.5%); NotDone475/1637(29.0%); Missing4 | 1.62(0.68–3.85); .276 | pH sensitivity / S224,S225 |
| N203 / S233 | Composite9 excluding cordpH, GEE | Yes75/1625(4.6%); No1550/1625(95.4%); Missing9 | Yes80/1625(4.9%); No1545/1625(95.1%); Missing16 | 0.96(0.70–1.31); .796 | primary sensitivity9 / S225 |
| N204 / S234 | Composite10, GLM, no twin cluster adjustment | Yes83/1625(5.1%); No1542/1625(94.9%); Missing9 | Yes84/1625(5.2%); No1541/1625(94.8%); Missing16 | 0.99(0.74–1.33); .937 | primary no-cluster sensitivity / S225 |
| N205 / S235 | Composite10, GLM, cord NotDone indicator-adjusted | No counts printed in this row | No counts printed in this row | 0.98(0.73–1.31); .882 | primary indicator-adjusted sensitivity / S225 |
| N206 / S236 | Composite10, pH imputed, GLM, cord NotDone indicator-adjusted | No counts printed in this row | No counts printed in this row | 0.97(0.73–1.30); .844 | primary imputed indicator-adjusted / S225 |

## DOC-004 eTable 2: every site-stratified outcome

Exact REPORT sources: [page3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3), [page4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4), [page5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5). M = Mater Mother's Hospital; O = Other sites. Effect is SC versus placebo, printed relative risk(95%CI), log-binomial regression (footnote on5). Count entry preserves numerator/denominator and printed percentage; “0” without a printed percentage remains “0”. Empty inferential cells are explicitly blank; a printed dash is retained. P interaction refers to site×treatment family rather than either site's individual P. “Not Done” cordpH<7 assumed No; the dagger also appears on CS-or-IVB heading as printed. No statement of GEE in this table's model footnote. Primary, secondary and tertiary status are table headings. Match each family to the same semantic outcome in the main article, with site as an added subgroup key; primary/component families also match S204–S209, operative families S210–S212.

| N/S locator | Status/outcome/page | Site | SC n/N(%) | Placebo n/N(%) | RR(95%CI) | P | Site interaction P |
|---|---|---|---|---|---|---|---|
| N207 / S237 | Primary composite /3 | M | 16/883(1.8%) | 24/887(2.7%) | 0.67(0.36–1.25) | .209 | .158 |
| N207 / S237 | Primary composite /3 | O | 67/742(9.0%) | 60/738(8.1%) | 1.11(0.80–1.55) | .537 | same family |
| N208 / S238 | Secondary intrapartum stillbirth /3 | M | 0/883 | 0/887 | printed dash | blank | blank |
| N208 / S238 | Secondary intrapartum stillbirth /3 | O | 0/746 | 0/750 | printed dash | blank | blank |
| N209 / S239 | Secondary28-day neonatal death /3 | M | 0/883 | 0/887 | printed dash | blank | blank |
| N209 / S239 | Secondary28-day neonatal death /3 | O | 0/742 | 0/740 | printed dash | blank | blank |
| N210 / S240 | Secondary Apgar<4at5min /3 | M | 1/883(0.1%) | 1/887(0.1%) | 1.00(0.06–16.03) | .997 | .676 |
| N210 / S240 | Secondary Apgar<4at5min /3 | O | 4/746(0.5%) | 2/750(0.3%) | 2.01(0.37–10.94) | .419 | same family |
| N211 / S241 | Secondary cord arterialpH<7 /3 | M | 2/883(0.2%) | 2/887(0.2%) | 1.00(0.14–7.12) | .996 | .315 |
| N211 / S241 | Secondary cord arterialpH<7 /3 | O | 10/746(1.3%) | 3/750(0.4%) | 3.35(0.93–12.13) | .065 | same family |
| N212 / S242 | Secondary neonatal encephalopathy /3 | M | 0/883(0.0%) | 0/887(0.0%) | blank | blank | blank |
| N212 / S242 | Secondary neonatal encephalopathy /3 | O | 1/742(0.1%) | 1/738(0.1%) | 0.99(0.06–15.87) | .997 | blank |
| N213 / S243 | Secondary neonatal seizures within28days /3 | M | 0/883(0.0%) | 0/887(0.0%) | blank | blank | blank |
| N213 / S243 | Secondary neonatal seizures within28days /3 | O | 2/742(0.3%) | 1/738(0.1%) | 1.99(0.18–21.89) | .574 | blank |
| N214 / S244 | Secondary neonatal-unit admission>48h /3 | M | 11/883(1.2%) | 13/887(1.5%) | 0.85(0.38–1.89) | .690 | .931 |
| N214 / S244 | Secondary neonatal-unit admission>48h /3 | O | 39/746(5.2%) | 48/750(6.4%) | 0.82(0.54–1.23) | .334 | same family |
| N215 / S245 | Secondary respiratory support>4h /4 | M | 5/883(0.6%) | 17/887(1.9%) | 0.30(0.11–0.80) | .016 | .015 |
| N215 / S245 | Secondary respiratory support>4h /4 | O | 32/746(4.3%) | 30/750(4.0%) | 1.07(0.66–1.75) | .779 | same family |
| N216 / S246 | Secondary PPHN /4 | M | 0/883(0.0%) | 1/887(0.1%) | blank | blank | blank |
| N216 / S246 | Secondary PPHN /4 | O | 1/746(0.1%) | 2/750(0.3%) | 0.50(0.05–5.53) | .574 | blank |
| N217 / S247 | Secondary meconium aspiration /4 | M | 1/883(0.1%) | 2/887(0.2%) | 0.50(0.05–5.53) | .574 | .214 |
| N217 / S247 | Secondary meconium aspiration /4 | O | 8/746(1.1%) | 3/750(0.4%) | 2.68(0.71–10.07) | .144 | same family |
| N218 / S248 | Secondary CSorIVB fetal distress /4 | M | 169/883(19.1%) | 157/887(17.7%) | 1.08(0.89–1.32) | .435 | .591 |
| N218 / S248 | Secondary CSorIVB fetal distress /4 | O | 174/746(23.3%) | 150/750(20.0%) | 1.17(0.96–1.42) | .119 | same family |
| N219 / S249 | Tertiary CS fetal distress primary indication /4 | M | 73/883(8.3%) | 69/887(7.8%) | 1.06(0.78–1.46) | .705 | .718 |
| N219 / S249 | Tertiary CS fetal distress primary indication /4 | O | 69/746(9.2%) | 60/750(8.0%) | 1.16(0.83–1.61) | .390 | same family |
| N220 / S250 | Tertiary IVB fetal distress primary indication /4 | M | 96/883(10.9%) | 88/887(9.9%) | 1.10(0.83–1.44) | .512 | .726 |
| N220 / S250 | Tertiary IVB fetal distress primary indication /4 | O | 105/746(14.1%) | 90/750(12.0%) | 1.17(0.90–1.53) | .234 | same family |
| N221 / S251 | Tertiary CS other indications /4 | M | 148/883(16.8%) | 133/887(15.0%) | 1.12(0.90–1.39) | .310 | .815 |
| N221 / S251 | Tertiary CS other indications /4 | O | 143/746(19.2%) | 124/750(16.5%) | 1.16(0.93–1.44) | .184 | same family |
| N222 / S252 | Tertiary IVB other indications /4 | M | 54/883(6.1%) | 61/887(6.9%) | 0.89(0.62–1.27) | .516 | .559 |
| N222 / S252 | Tertiary IVB other indications /4 | O | 40/746(5.4%) | 53/750(7.1%) | 0.76(0.51–1.13) | .174 | same family |
| N223 / S253 | Tertiary emergency operative birth FD factor /4 heading,5 values | M | 224/883(25.4%) | 206/887(23.2%) | 1.09(0.93–1.29) | .293 | .927 (on4) |
| N223 / S253 | Tertiary emergency operative birth FD factor /5 | O | 247/746(33.1%) | 225/750(30.0%) | 1.10(0.95–1.28) | .196 | same family |
| N224 / S254 | Tertiary CS FD factor /5 | M | 106/883(12.0%) | 93/887(10.5%) | 1.14(0.88–1.49) | .312 | .859 |
| N224 / S254 | Tertiary CS FD factor /5 | O | 127/746(17.0%) | 108/750(14.4%) | 1.18(0.93–1.50) | .164 | same family |
| N225 / S255 | Tertiary IVB FD factor /5 | M | 118/883(13.4%) | 113/887(12.7%) | 1.05(0.82–1.33) | .697 | .920 |
| N225 / S255 | Tertiary IVB FD factor /5 | O | 120/746(16.1%) | 117/750(15.6%) | 1.03(0.82–1.30) | .797 | same family |
| N226 / S256 | Tertiary spontaneous vaginal birth /5 | M | 494/883(55.9%) | 521/887(58.7%) | 0.95(0.88–1.03) | .235 | .450 |
| N226 / S256 | Tertiary spontaneous vaginal birth /5 | O | 370/746(49.6%) | 410/750(54.7%) | 0.91(0.82–1.00) | .050 | same family |
| N227 / S257 | Tertiary postpartum hemorrhage>1Liter /5 | M | 73/880(8.3%) | 72/882(8.2%) | 1.02(0.74–1.39) | .920 | .036 |
| N227 / S257 | Tertiary postpartum hemorrhage>1Liter /5 | O | 91/741(12.3%) | 56/745(7.5%) | 1.63(1.19–2.24) | .002 | same family |

## DOC-004 eTable 3: every side-effect row

Exact REPORT source: [page6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6). Safety/treatment-received denominators SC1552/P1557; footnote excludes148women receiving no treatment. Printed P is Fisher's exact test. No RR/CI printed. Matching main key safety/side-effects/actual-treatment; PLAN counterparts S217,S229 and SAP24 table10 (which additionally lists migraine-like headache). A zero Yes cell has no printed percentage. Blank P cells remain blank.

| N/S locator | Side-effect | SC Yes; No | Placebo Yes; No | P |
|---|---|---|---|---|
| N228 / S258 | Headache | 3(0.2%);1549(99.8%) | 7(0.4%);1550(99.6%) | .343 |
| N229 / S259 | Diarrhoea | 0;1552(100.0%) | 1(0.1%);1556(99.9%) | .999 |
| N230 / S260 | Dizziness | 0;1552(100.0%) | 5(0.3%);1552(99.7%) | .062 |
| N231 / S261 | Flushing | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N232 / S262 | Gastro-oesophageal reflux/dyspepsia | 2(0.1%);1550(99.9%) | 1(0.1%);1556(99.9%) | .624 |
| N233 / S263 | Myalgia/limb pain | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N234 / S264 | Visual changes | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N235 / S265 | Vomiting | 0;1552(100.0%) | 1(0.1%);1556(99.9%) | .999 |
| N236 / S266 | Bronchitis | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N237 / S267 | Cellulitis/skin rash | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N238 / S268 | Epistaxis | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N239 / S269 | Hypo/paraesthesia | 1(0.1%);1551(99.9%) | 1(0.1%);1556(99.9%) | .999 |
| N240 / S270 | Tremor | 0;1552(100.0%) | 0;1557(100.0%) | blank |
| N241 / S271 | Vaginal itch | 0;1552(100.0%) | 0;1557(100.0%) | blank |


## Pass 1 records

All displayed count/denominator percentages were recalculated. Every nonzero fraction lies within its printed one-decimal half-unit percentage interval; zero-event entries remain zero or blank as printed. All count totals within these displays reconcile. Safety total1552+1557=3109; plus excluded148 gives3257 women, as corroborated by main p.4 actual-treatment description. Every populated RR is positive, lies inside its ordered CI, and has an interval/null reading consistent with its own P at.05. Models/covariate labels distinguish the six sensitivity rows without substituting another analysis.

| S ID | Exact REPORT location | Pass 1 status | Checks and result |
|---|---|---|---|
| S231 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | Counts 85+1540=1625 and 87+1538=1625; with Missing9/16 totals1634/1641. Ordered CI contains1.01 and null1; P.943 is nonsignificant. GEE differs from crude RR, as permitted. Imputation/model inputs not fully printed. |
| S232 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | 14+1211+404=1629 and 8+1154+475=1637; with Missing5/4 totals1634/1641. All percentages reconcile. CI contains1.62 and null1; P.276 agrees. GEE RR is not a crude ratio; NotDone retained as printed after partial imputation. |
| S233 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | 75+1550=1625 and 80+1545=1625, with Missing9/16 reconciling randomized headers. CI contains.96 and null1; P.796 agrees. Nine-component label clearly identifies omitted pH component. |
| S234 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | 83+1542=1625 and 84+1541=1625. Independent-binomial diagnostic RR.988095, CI.735343–1.327724 and P approximately.937 reproduce printed.99(.74–1.33),P.937. No-cluster GLM is explicitly identified. |
| S235 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | Count cells are empty, preserved without attribution. CI.73–1.31 contains.98 and null1; P.882 agrees. NotDone-indicator GLM is identified; covariate cross-tabulations not printed, so no exact model reconstruction is asserted. |
| S236 | [REPORT DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2) | PASS_1_COMPLETE | Count cells are empty, preserved without attribution. CI.73–1.30 contains.97 and null1; P.844 agrees. Imputed/NotDone-indicator GLM is identified; covariate/twin-imputation cross-tabulations not printed. |
| S237 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.158419 reconciles the printed family P; interaction test type is not asserted from convention. |
| S238 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 0 printed RR/CI/P rows: ordered endpoints and point containment; no printed RR/CI/P result; independent-binomial diagnostics reproduce the populated rows. Interaction P is blank; no value inferred. Printed RR dash, blank P and blank interaction for both zero-event sites retained. |
| S239 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 0 printed RR/CI/P rows: ordered endpoints and point containment; no printed RR/CI/P result; independent-binomial diagnostics reproduce the populated rows. Interaction P is blank; no value inferred. Printed RR dash, blank P and blank interaction for both zero-event sites retained. |
| S240 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.675726 reconciles the printed family P; interaction test type is not asserted from convention. |
| S241 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.314579 reconciles the printed family P; interaction test type is not asserted from convention. |
| S242 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 1 printed RR/CI/P row: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction P is blank; no value inferred. Mater inferential cells are blank and retained. |
| S243 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 1 printed RR/CI/P row: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction P is blank; no value inferred. Mater inferential cells are blank and retained. |
| S244 | [REPORT DOC-004 p.3](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=3) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.930784 reconciles the printed family P; interaction test type is not asserted from convention. |
| S245 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; Mater CI excludes1 with P.016, Other CI includes1 with P.779; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.015088 reconciles the printed family P; interaction test type is not asserted from convention. |
| S246 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 1 printed RR/CI/P row: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction P is blank; no value inferred. Mater inferential cells are blank and retained. |
| S247 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.213883 reconciles the printed family P; interaction test type is not asserted from convention. |
| S248 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.590748 reconciles the printed family P; interaction test type is not asserted from convention. |
| S249 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.717976 reconciles the printed family P; interaction test type is not asserted from convention. |
| S250 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.725522 reconciles the printed family P; interaction test type is not asserted from convention. |
| S251 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.815096 reconciles the printed family P; interaction test type is not asserted from convention. |
| S252 | [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.558928 reconciles the printed family P; interaction test type is not asserted from convention. |
| S253 | [REPORT DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) and [REPORT DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.927359 reconciles the printed family P; interaction test type is not asserted from convention. Heading/interaction appears on p.4; both site values are on p.5. |
| S254 | [REPORT DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.858679 reconciles the printed family P; interaction test type is not asserted from convention. |
| S255 | [REPORT DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; every printed CI includes1 with P>.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.920147 reconciles the printed family P; interaction test type is not asserted from convention. |
| S256 | [REPORT DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; Mater CI includes1 with P.235; Other CI reaches1.00 with P.050, so both printed readings are nonsignificant under P<.05; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.450433 reconciles the printed family P; interaction test type is not asserted from convention. |
| S257 | [REPORT DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) | PASS_1_COMPLETE | Both site count/percentage rows checked. 2 printed RR/CI/P rows: ordered endpoints and point containment; Mater CI includes1 with P.920, Other CI excludes1 with P.002; independent-binomial diagnostics reproduce the populated rows. Interaction diagnostic P0.035584 reconciles the printed family P; interaction test type is not asserted from convention. |
| S258 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 3+1549=1552 and 7+1550=1557; percentages reconcile. Two-sided probability-ordered Fisher diagnostic P.342964 reproduces.343; no RR/CI is printed. |
| S259 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 0+1552=1552 and 1+1556=1557; percentages reconcile. Fisher diagnostic P1 compared with printed.999 is screened by display precision; no interval conflict. |
| S260 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 0+1552=1552 and 5+1552=1557; percentages reconcile. Fisher diagnostic P.062301 reproduces.062 and is nonsignificant; no RR/CI is printed. |
| S261 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved. No estimable RR/CI or inferential conclusion is printed. |
| S262 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 2+1550=1552 and 1+1556=1557; percentages reconcile. Probability-ordered Fisher diagnostic P.624277 reproduces.624; alternative doubled-tail definition is not imposed. |
| S263 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S264 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S265 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 0+1552=1552 and 1+1556=1557; percentages reconcile. Fisher diagnostic P1 versus printed.999 is within display precision; no interval conflict. |
| S266 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S267 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S268 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S269 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | 1+1551=1552 and 1+1556=1557; percentages reconcile. Fisher diagnostic P1 versus printed.999 is within display precision; no interval conflict. |
| S270 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |
| S271 | [REPORT DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6) | PASS_1_COMPLETE | Both Yes0; No1552/1557, both100.0%, reconcile denominators. P blank preserved; no interval or statistical conclusion supplied. |

## Diagnostic calculations and limitations

The following are diagnostic reconstructions, not assertions that a particular test statistic or variance estimator was printed. Site table model footnote says log-binomial regression. For its populated two-arm rows, R=(a/n)/(b/m), s²=1/a−1/n+1/b−1/m, diagnostic CI=exp(logR±1.959964s), and diagnostic P=2Φ(−abs(logR/s)). This reproduces all35 populated site RR/CI/P rows at their display precision. For independent two-site interaction diagnostics, a no-interaction common-RR binomial likelihood was fitted with a separate placebo risk for each site and compared with the saturated four-risk likelihood. Its one-contrast likelihood-ratio tail reproduces all16 populated interaction Ps after rounding. The covariance, variance estimator, and test used by the authors are not inferred solely from these reconstructions. For Fisher diagnostics, probability-ordering over the conditional hypergeometric distribution reproduces headache, dizziness, and reflux rows; it supplies1 for the three near-unit printed Ps handled by the display rule.

| S ID | Site | Diagnostic RR | Diagnostic lower95% | Diagnostic upper95% | Diagnostic P |
|---|---|---:|---:|---:|---:|
| S237 | M | 0.66969 | 0.35822 | 1.25199 | 0.209122 |
| S237 | O | 1.11065 | 0.79597 | 1.54972 | 0.536955 |
| S240 | M | 1.00453 | 0.06293 | 16.03479 | 0.997449 |
| S240 | O | 2.01072 | 0.36941 | 10.94459 | 0.419094 |
| S241 | M | 1.00453 | 0.14182 | 7.11545 | 0.996390 |
| S241 | O | 3.35121 | 0.92598 | 12.12828 | 0.065360 |
| S242 | O | 0.99461 | 0.06233 | 15.87156 | 0.996948 |
| S243 | O | 1.98922 | 0.18077 | 21.89009 | 0.574085 |
| S244 | M | 0.84999 | 0.38287 | 1.88700 | 0.689569 |
| S244 | O | 0.81686 | 0.54200 | 1.23109 | 0.333753 |
| S245 | M | 0.29545 | 0.10948 | 0.79733 | 0.016079 |
| S245 | O | 1.07239 | 0.65850 | 1.74640 | 0.778807 |
| S246 | O | 0.50268 | 0.04568 | 5.53181 | 0.574057 |
| S247 | M | 0.50227 | 0.04563 | 5.52907 | 0.573649 |
| S247 | O | 2.68097 | 0.71402 | 10.06640 | 0.144030 |
| S248 | M | 1.08131 | 0.88862 | 1.31578 | 0.434987 |
| S248 | O | 1.16622 | 0.96111 | 1.41510 | 0.119218 |
| S249 | M | 1.06276 | 0.77511 | 1.45716 | 0.705420 |
| S249 | O | 1.15617 | 0.83053 | 1.60947 | 0.389915 |
| S250 | M | 1.09585 | 0.83335 | 1.44104 | 0.512387 |
| S250 | O | 1.17292 | 0.90197 | 1.52527 | 0.234001 |
| S251 | M | 1.11782 | 0.90171 | 1.38573 | 0.309572 |
| S251 | O | 1.15941 | 0.93221 | 1.44198 | 0.183798 |
| S252 | M | 0.88926 | 0.62404 | 1.26718 | 0.515993 |
| S252 | O | 0.75876 | 0.50973 | 1.12946 | 0.173776 |
| S253 | M | 1.09230 | 0.92646 | 1.28783 | 0.293322 |
| S253 | O | 1.10366 | 0.95039 | 1.28165 | 0.196008 |
| S254 | M | 1.14495 | 0.88068 | 1.48852 | 0.312032 |
| S254 | O | 1.18223 | 0.93400 | 1.49643 | 0.163875 |
| S255 | M | 1.04898 | 0.82469 | 1.33426 | 0.696842 |
| S255 | O | 1.03114 | 0.81632 | 1.30249 | 0.796963 |
| S256 | M | 0.95247 | 0.87887 | 1.03224 | 0.235348 |
| S256 | O | 0.90728 | 0.82310 | 1.00006 | 0.050143 |
| S257 | M | 1.01619 | 0.74394 | 1.38808 | 0.919586 |
| S257 | O | 1.63377 | 1.18996 | 2.24311 | 0.002402 |

| S ID | Diagnostic likelihood-ratio interaction P |
|---|---:|
| S237 | 0.158419 |
| S240 | 0.675726 |
| S241 | 0.314579 |
| S244 | 0.930784 |
| S245 | 0.015088 |
| S247 | 0.213883 |
| S248 | 0.590748 |
| S249 | 0.717976 |
| S250 | 0.725522 |
| S251 | 0.815096 |
| S252 | 0.558928 |
| S253 | 0.927359 |
| S254 | 0.858679 |
| S255 | 0.920147 |
| S256 | 0.450433 |
| S257 | 0.035584 |

The GEE sensitivities cannot be exactly refitted from these aggregate counts: individual twin pair outcomes and GEE fitted covariance/variance inputs are absent. The imputed sensitivities omit stratum-specific tested rates, no-other-component fractions, and arm-specific eligible NotDone counts. Indicator-adjusted GLMs omit treatment×testing-status outcome cross-tabulations. None of those absences establishes a printed contradiction. All six sensitivity CIs/Ps agree at the null/significance level. A log-scale CI-halfwidth diagnostic can reconcile the printed Ps with RRs1.010915,1.618995,.959510,.988248,.978101,.971447 respectively, all inside the corresponding displayed point-estimate intervals; this is a display check, not a reconstruction of unavailable GEE fits.

Findings:0. Excluded apparent observations:4, recorded once in checkers/parts/statistical_support_pass_1.md. No coverage limitation; the specified model-refit limitations remain. Pass2 must be performed by a distinct fresh runtime agent and revisit every ID with ledger/screen/recheck facts.

