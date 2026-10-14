# Exact-source evidence recheck: C014, C015, C016, C017, C018, C019

Runtime agent: 01a12c63-ca83-7d51-ad07-f4248a018f40; model gpt-6.1-sol; reasoning effort high; fresh spawn. Every ID remains Pending Human Adjudication. Read QUALITY_CONTROL_SCOPE.md, review_contract.md, settings.toml, tooling_record.md, source_inventory.md and the complete assigned stable ledger part. Confirmed 18 unique source pages visually, within the 32-page bound: DOC-001 pp.1,3,6; DOC-002 pp.9,47,48,63,64,65,77,83,85; DOC-003 pp.6,8,9,12,13,14. Text derivatives were locators only.

Image provenance: existing current-run CPU source renders `preprocessing/st1-main-006.png`, `cross_main_3.png`, `cross_plan_47.png`, `cross_plan_48.png`, `cross_plan_63.png`, `numeric_support_plan_p64.png`, `cross_plan_65.png`, `cross_plan_77.png`, `cross_plan_83.png`, `cross_plan_85.png`, `numeric_support_p006.png`, `cross_supp_8.png`, `numeric_support_p009.png`, `cross_supp_12.png`, `numeric_support_p013.png`; reusable exact-page image `review_1_5_1/preprocessing/DOC-002/page_images/page-009.jpg`. Two new CPU renders use recorded fallback PyMuPDF 1.26.4, 200 dpi: `pdf_tools.py render` DOC-001 --page 1 to `preprocessing/recheck003_main001.png`, and DOC-003 --page 14 to `preprocessing/recheck003_supp014.png`. No OCR was needed; recorded GPU_USER_REQUESTED applies to OCR, while rendering remains CPU. No source or reusable artifact was modified. Arithmetic below was independently recomputed with direct numerical interval arithmetic.

## C014 — Fourteen interval rows

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes for every affected row in [DOC-001 p.6, Table 2](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), [DOC-003 p.12, eTable 8](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>) and [DOC-003 p.13, eTable 9](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>). [DOC-003 p.14 notes](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identify RR, covariate adjustment and mixed-effects clustering, but no row-specific interval construction. All are REPORT by displayed trial-results content. Table 2 self-report adjusted upper endpoint is literally `42`, and its lower endpoint is `1.9`; no decimal was silently inserted.

**Consistency rule applicable; calculation reproduced:** Diagnostic log-symmetry reconstruction U*=E²/L. Independent displayed input intervals E±hE and L±hL imply [(E−hE)²/(L+hL),(E+hE)²/(L−hL)]; compare with U±hU. Half-units depend on every printed decimal count, including .5 for literal 42. The table lists all 14 independently reproduced discrepancies; relative gap is gap/|printed U|. Every value exceeds .05. This is the route A category 4 display rule supported by other rows, not a claim that every possible RR interval must be log-symmetric.

| Source display / affected row | Printed E; L; U | Recomputed U* interval | Printed U interval | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Table 2 CO<10 PP adjusted | 3.1; 2.1; 5.2 | [4.326744,4.840244] | [5.15,5.25] | .309756 | .059568 |
| Table 2 CO<6 PP crude | 3.6; 2.14; 6.87 | [5.875291,6.240047] | [6.865,6.875] | .624953 | .090968 |
| Table 2 CO<6 PP adjusted | 3.8; 2.3; 7.7 | [5.984043,6.587778] | [7.65,7.75] | 1.062222 | .137951 |
| Table 2 self-report adjusted | 2.8; 1.9; 42 | [3.878205,4.390541] | [41.5,42.5] | 37.109459 | .883559 |
| eTable 8 All | 2.890; 1.983; 4.709 | [4.209332,4.214371] | [4.7085,4.7095] | .494129 | .104933 |
| eTable 8 age ≥40 | 2.953; 2.048; 5.092 | [4.255434,4.260397] | [5.0915,5.0925] | .831103 | .163217 |
| eTable 8 primary education | 2.638; 1.849; 4.07 | [3.761236,3.766125] | [4.065,4.075] | .298875 | .073434 |
| eTable 8 secondary education | 2.719; 1.348; 4.83 | [5.480343,5.488445] | [4.825,4.835] | .645343 | .133611 |
| eTable 8 active occupation | 2.989; 1.933; 4.885 | [4.619153,4.624637] | [4.8845,4.8855] | .259863 | .053196 |
| eTable 8 dependent/retired | 2.587; 1.329; 3.986 | [5.031954,5.039636] | [3.9855,3.9865] | 1.045454 | .262281 |
| eTable 8 smoking <24 years | 3.511; 1.884; 7.127 | [6.539459,6.546659] | [7.1265,7.1275] | .579841 | .081358 |
| eTable 8 reading SMS No | 2.198; 1.288; 3.299 | [3.747774,3.754099] | [3.2985,3.2995] | .448274 | .135882 |
| eTable 9 CO<10 crude | 2.9; 1.8; 6.4 | [4.390541,4.972857] | [6.35,6.45] | 1.377143 | .215179 |
| eTable 9 CO<10 adjusted | 3.1; 1.9; 6.5 | [4.770513,5.363514] | [6.45,6.55] | 1.086486 | .167152 |

Comparator rows were visually matched and independently recomputed. Table 2 self-report crude 2.7[1.8,4.1], week 9 crude 2.6[1.8,3.9]/adjusted 2.7[1.8,4.3], month 6 crude 2.7[2.0,3.8]/adjusted 2.7[1.9,4.0], and success 1.2[.9,1.6]/1.2[.9,1.5] all have overlapping reconstructed and printed upper-limit intervals. eTable 8 age <40 2.672[1.472,4.857] yields [4.846799,4.853725], relative gap .000571; no formal education 2.880[1.566,5.542] gives [5.293023,5.300083], relative gap .043561; smoking ≥24 2.446[1.550,3.911] gives [3.857124,3.862770], relative gap .012204; reading Yes 2.769[1.743,4.318] gives [4.396095,4.401796], relative gap .017970. These four satisfy the workflow precision tolerance; they are not asserted to have exact overlap. eTable 9 CO<6 3.6[2.4,5.4]/3.8[2.4,6.2], week 9 2.5[1.7,3.6]/2.6[1.7,3.8], month 6 2.58[1.8,3.6]/2.7[1.8,4.0], and success 1.1[.7,1.6]/1.1[.7,1.5] all overlap under the same half-unit rule.

**Necessary inputs available:** Every printed triple and display precision needed for this diagnostic is available. **Exact missing inputs/definitions:** Fitted coefficients/covariance, transformation from model to RR, interval-construction algorithm and any row-specific method switches are absent. No universal Wald construction, confidence-interval/P-value conflict or point-outside-interval issue is inferred.

**Alternative interpretation:** The report describes mixed-effects modeling; nonsymmetric profile, bootstrap or transformed marginal-risk intervals could produce the observed endpoints. Different row procedures could be intended. These are possible explanations, not observed algorithms.

**Direct observation versus inferred explanation:** Directly observed are the printed triples and reproduced differences under a rule fitting other display rows within the workflow tolerance. A decimal slip or production mechanism is unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows

**Finding IDs:** F-ST1-001

**Classification rationale:** The same pattern is consolidated across displays, without asserting a matched-result conflict between documents. PLAN corroboration is not used. No classification change.

**Classification ambiguity:** Row-specific interval construction is unknown; no universal inferential convention or production mechanism is asserted.

**Evidence state:** reproduced

Determining fact: all 14 printed triples match and all 14 diagnostic interval gaps remain >.05 relatively.

**Exact remaining human question:** Which estimate/interval construction produced each of the 14 rows, and are the printed limits, including literal 42, intended for that construction?

## C015 — Failure definition windows

Pending Human Adjudication.

**Location found; source value/text matched; comparator matched:** Yes. [DOC-002 p.9 lines179–180](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=9>) says month 5 or later and is headed V6.0 07.03.25; [p.47 lines1319–1320](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>) says month 6 or later; [p.77 lines2413–2415](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes replacing month 5 with month 6 in v6; [SAP p.85 lines2685–2686](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=85>) retains month 5 or later. All four are PLAN by prospective endpoint/amendment content. REPORT impact locations [DOC-001 p.1 abstract](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), [p.3 Trial Outcomes](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) and [p.6 Table 2](<../../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) contain the secondary failure result/pointer; Table 2 prints 1/720 versus 2/360. Abstract prints failure 0.1% versus0.5%; it does not itself print the event counts or define a smear window.

**Rule applicable; comparison reproduced; precision:** Month 5-or-later and month 6-or-later are categorically different endpoint windows; display rounding is inapplicable. The historical amendment explains the v4→v6 change but does not reconcile the retained month-5 SAP definition with the amended month-6 definition. No specific event is inferred to change classification.

**Inputs available/missing:** Competing definitions, explicit amendment and three reported events are available. Final endpoint dictionary, amendment/SAP hierarchy, event smear dates and programme-register classification rules actually used are absent. **Alternative interpretation:** Amended protocol could govern, SAP could govern, or programme records could apply a separately defined rule. **Direct versus inferred:** Contradictory printed windows are direct; participant reclassification or numerical outcome effects are unestablished.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result

**Finding IDs:** F-XS-009, F-ST1-011

**Classification rationale:** REPORT does not supply a competing threshold, so it creates no P_R relationship. No classification change. Specify p.9 as an earlier-positioned component explicitly headed V6.0, rather than imply it is v4.

**Classification ambiguity:** Final protocol/SAP precedence and governing endpoint dictionary are absent; disclosed amendment does not reconcile all retained definitions.

**Evidence state:** reproduced

Determining fact: exact plan month-5 and month-6 windows remain different after reading the amendment.

**Exact remaining human question:** Which supplied plan rule and smear-positive window classified the three reported failures: month 5 or later or month 6 or later?

## C016 — Phase 3 cluster power inputs

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes. PLAN [DOC-002 p.48 lines1348–1350](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>) gives 18 intervention and 9 control clusters, 90% power, 5% level, 18%/8% abstinence; [p.63 lines1886–1907](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>) gives these rates/power and 27 clusters, 18/9 allocation, and1080 participants; [p.65 lines1958–1961](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=65>) retains 16 intervention and8 control with the same rates/power; [p.77 lines2416–2424](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes increasing Phase3 v4 16/8,888 participants to v6 18/9,1080; [SAP p.83 lines2629–2638](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>) gives27 clusters,2:1,90%/5%,18%/8%,1080. All are PLAN by prospective design/power content. Peripheral PLAN [p.64 Phase4](<../../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>) uses18/18, while the repeated p.65 Phase4 paragraph uses20/20; p.77 amendment describes40→36 Phase4 clusters. This context does not expand the included Phase3 issue.

**Rule applicable; calculation reproduced; precision:** Intervention-arm copies 18±.5 and16±.5 have intervals[17.5,18.5] and[15.5,16.5], gap1, relative1/16=.0625>.05. Control9±.5 and8±.5 touch. Independently rounded arm sums[26,28] and[23,25] have gap1/24=.041667; that sum alone does not qualify. The basis is the intervention-arm input attached to the primary trial power specification.

**Inputs available/missing:** Allocations, rates, significance/power and disclosed amendment are available. A final governing power calculation and an explicit statement that p.65 is historical or a distinct scenario are absent. **Alternative interpretation:** p.65 may retain earlier-version text; both allocations might have been evaluated without being differentiated. The source itself discloses the change, so no undisclosed amendment is asserted. **Direct versus inferred:** Direct is the incompatible repeated current-plan power-input paragraph; its production mechanism is inferred and unestablished.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context

**Finding IDs:** F-XS-011, F-ST1-009

**Classification rationale:** Reported27-cluster trial only corroborates one side and adds no P_R relationship. No classification change.

**Classification ambiguity:** p.65 could preserve historical inputs without saying so. Unreported Phase4 context does not expand the included candidate.

**Evidence state:** reproduced

Determining fact: current supplied plan power paragraphs retain18 versus16 intervention clusters beyond the workflow precision threshold.

**Exact remaining human question:** Which Phase3 allocation/power calculation governs, and is the16/8 paragraph intended solely as historical text?

## C017 — Two cause-of-death percentages

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.6 eTable4](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>) prints usual-care Drug user1(7.4%) and Severe pneumonia1(7.4%), usual-care total deaths27, each overall affected count1 and mHealth0. Same-display stroke2(7.4%) and fall1(3.7%) corroborate the27 denominator. All usual-care cause counts sum27.

**Rule applicable; calculation reproduced; precision:** For each affected cell100×1/27=3.703704%. Half-unit input reconstruction100×[.5/27.5,1.5/26.5]=[1.818182,5.660377]%; displayed7.4% permits[7.35,7.45]%, leaving gap1.689623 and relative.228327>.05. Both occurrences are independently confirmed, one repeated pattern under route A category3.

**Inputs available/missing:** Printed count, common death total, percentages and sums are available. No separate cause-specific denominator is defined. **Alternative interpretation:** The7.4% could correspond to two deaths or another denominator, but no such switch is printed; table sums support the displayed one death in each row. **Direct versus inferred:** Count/percentage/denominator mismatch is observed; copying or other production mechanisms are unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.6 affected cells vs same-table death total

**Finding IDs:** F-NUM-101

**Classification rationale:** Both affected cells and comparator total occur within the same REPORT table; no classification change.

**Classification ambiguity:** None.

**Evidence state:** reproduced

Determining fact: both1(7.4%) cells fail the co-located27-death denominator rule beyond precision.

**Exact remaining human question:** What count, denominator and percentage should be extracted for each of the two usual-care death-cause rows?

## C018 — Site 2008 mortality cell

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.9 eTable6](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=9>) prints Control2008 5(7.5). All other death cells follow an N40 percentage rule, e.g. Control2002 3(7.5), Control2004 4(10.0), mHealth2012 5(12.5). REPORT [p.8 eTable5](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=8>) prints site2008 recruitment40/484 and ITT12/40, with observed12/35; denominator35 belongs to observed abstinence contributors, not a defined mortality denominator. eTable6 death counts sum52:27 control and25 mHealth.

**Rule applicable; calculation reproduced; precision:** N40 reproduces other death percentages.100×5/40=12.5%; half-unit input range100×[4.5/40.5,5.5/39.5]=[11.111111,13.924051]% versus[7.45,7.55]%, gap3.561111, relative.474815>.05. N40 is inferred from the same-display reproducing rule and explicitly corroborated by site population elsewhere; it is not printed as an N column in eTable6. Thus route A category4 supports the observation independently of the table-denominator formulation of category3.

**Inputs available/missing:** Death count, percentage, matching other cells and site population are available. A separate mortality denominator or row-specific population definition is absent. **Alternative interpretation:** Three of40 would produce7.5%, whereas five of40 produces12.5%; another denominator requires a definition. Counts/sums corroborate five without assigning a corrected value. **Direct versus inferred:** Printed5(7.5) and other-cell pattern are direct; N40 is supported inference; production mechanism is unestablished.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator

**Finding IDs:** F-NUM-102

**Classification rationale:** Both locations are within one REPORT document; no cross-document relationship. No classification change.

**Classification ambiguity:** N40 is inferred from the same-display pattern and corroborated by the printed ITT population; eTable6 does not print a separate denominator column.

**Evidence state:** reproduced

Determining fact: the source cell does not reproduce the N40 rule fitting all other death cells, with relative gap>.05.

**Exact remaining human question:** What mortality count, denominator and percentage governs site2008 in eTable6?

## C019 — Signed treatment-failure contrast

Pending Human Adjudication.

**Location found; source and comparator matched:** Yes: REPORT [DOC-003 p.13 eTable9](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>) prints mHealth1/695,0.1%[0.01,0.8] versus usual-care2/333,0.6%[0.1,2.2], difference0.5[-0.4,1.3]. REPORT [p.14 note b](<../../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identifies “Absolute difference” without a row-specific reversal. Other rows reproduce mHealth-minus-usual-care:43.2−16.5=26.7;38.0−11.4=26.6;50.8−22.5=28.3;57.5−24.6=32.9;3.2−2.1=1.1; success92.5−92.5=0.

**Rule applicable; calculation reproduced; precision:**100×(1/695−2/333)=−.456716 percentage points. Half-unit count/denominator input range[−.679989,−.233792], versus displayed positive[.45,.55], leaves gap.683792/|.5|=1.367585>.05. Rounded printed arm risks independently imply[−.60,−.40]. Thus the affected row reverses the common display contrast under route A category2. The minus sign inside the printed CI is present; no separate interval-construction issue is inferred.

**Inputs available/missing:** Counts, populations, risks, point difference, interval and other-row contrast are available. An explicit signed-reference definition or unsigned/row-specific contrast switch is absent. **Alternative interpretation:** “Absolute” may mean an unsigned magnitude, or this row could reverse the reference groups; a different model-based contrast could be intended. The common pattern and signed interval are retained rather than assuming a universal meaning of “absolute.” **Direct versus inferred:** Positive printed point difference versus negative common signed contrast is observed; intended reference or mechanism is inferred and unresolved.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference

**Finding IDs:** F-NUM-103

**Classification rationale:** Risks, difference, common contrast and note are within one REPORT document; no classification change.

**Classification ambiguity:** An unsigned magnitude or row-specific reference switch remains an alternative interpretation.

**Evidence state:** reproduced

Determining fact: exact printed positive.5 fails the mHealth-minus-usual-care rule fitting the other rows, beyond display precision.

**Exact remaining human question:** Does the treatment-failure row use mHealth-minus-usual-care, and what signed difference and matching interval should be extracted?

All six IDs have exact-source confirmations and classification checks; no source location remained unreadable. Remaining inputs are the named row-specific statistical definitions, final plan hierarchy/power specification, outcome-event dictionary, and any alternate denominators/reference groups. These limit explanatory reconstruction and remain human questions.
