# Main numeric consistency review

Scope: DOC-001, REPORT, all 14 physical PDF pages and all relationships N001–N120. All 120 records were checked, including every table row, figure stratum, outcome count and matched abstract/body occurrence. Administrative/reference pages 12–14 contain no additional result relationship. Review uses the complete scope and review contract, current mapping, direct Poppler source extraction and reusable page images 5, 7 and 9. No legacy scientific conclusions were used. Inferential test reconciliation is separately assigned to the statistical reviewers; numeric containment and direction were checked here.

## Findings

### F-NUM-001

**Title:** Follow-up MRI analysis-population count does not reconcile between report locations.

**Compared locations and document roles:** REPORT DOC-001 [physical p. 4, Results, final baseline-imaging sentence](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4); REPORT DOC-001 [physical p. 9, Association of Follow-Up Infarct Volume and Infarct Growth](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9); REPORT DOC-001 [physical p. 11, discussion of MR diffusion follow-up](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=11). Relationships N019 and N113; both compared locations are within the same REPORT, proposed relationship S_W.

**Printed inputs:** p. 4 states, “Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336 patients (98%).” p. 9 explicitly identifies patients with “MR diffusion follow-up (n = 204 [61%])” for infarct-growth analysis. p. 11 describes MR diffusion follow-up as comprising two-thirds of the population. The total analysis population is 336.

**Rule and calculation:** A follow-up MRI subgroup of 204 cannot be contained in a total follow-up MRI group of 8 under the same modality/time-point definition. Counts 8 and 204 have half-unit intervals [7.5, 8.5] and [203.5, 204.5], respectively: minimum gap 195 patients, relative discrepancy 195/8 = 24.375. Percentage copies 2% and 61% have intervals [1.5, 2.5] and [60.5, 61.5]: gap 58 percentage points, relative discrepancy 58/2 = 29. Allowing count and denominator half-units gives 8/336 a percentage range [100×7.5/336.5, 100×8.5/335.5] = [2.229, 2.534]% and 204/336 [100×203.5/336.5, 100×204.5/335.5] = [60.475, 60.954]%. The internal count/percentage pairs individually reconcile; the conflict is between populations labeled follow-up MRI.

**Focus area:** A, analysis-population size and matched imaging count.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** The size and modality composition of the follow-up MRI population used for infarct-growth results, including the medians 68, 95 and 125 mL in the p. 9 analysis.

**Why context does not resolve it:** Both locations explicitly say follow-up imaging. The p. 9 analysis population exceeds the p. 4 total MRI follow-up count by 196 patients. This changes the population size for a reported analysis, so the comparison is not peripheral. The source does not distinguish separate follow-up windows or alternative modality definitions that reconcile the counts.

**Alternatives and missing definition:** Table 1 p. 5 baseline MR DWI counts are 3 + 5 = 8, which may suggest that p. 4 refers to baseline rather than follow-up imaging, but that is an inferred explanation; its printed temporal label remains follow-up. Alternatively, distinct follow-up acquisitions or subsets could have been intended, but no such count definition is supplied at the compared locations. The p. 11 approximate fraction corroborates a substantially larger follow-up group and is not separately registered.

**Exact human question:** Which acquisition time point and MRI population does the p. 4 count 8/336 represent, and how should it be reconciled with the p. 9 MR diffusion follow-up population of 204?

### F-NUM-002

**Title:** Large-core EVT outcome proportions in the discussion do not reconcile with the printed mRS distribution.

**Compared locations and document roles:** REPORT DOC-001 [physical p. 7, Figure 2B, EVT core ≥100 mL, n = 51](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7); REPORT DOC-001 [physical p. 10, Discussion, paragraph beginning “EVT benefit in ordinal analysis”](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10). Relationships N073 and N117. Proposed relationship S_W.

**Printed inputs:** Figure 2B displays percentages 2, 6, 10 and 20 in the mRS 0, 1, 2 and 3 categories of the EVT ≥100-mL group. Its mRS 5 and 6 segments show 10 and 53; the legend-color-defined mRS 4 segment is absent, not printed as a numeral zero. The discussion describes the core ≥100-mL EVT population as approximately 80% having mRS 4 or worse and says “1 in 5 patients still achieved independent ambulation after EVT.” Independent ambulation is explicitly mRS 0–3 (p. 3 and Table 2).

**Rule and calculation:** The printed mRS 0–3 segments sum to 2 + 6 + 10 + 20 = 38%, whereas one in five represents 20%. Allowing every whole-percentage input ±0.5 gives [36, 40]%. A whole-percentage 20 has [19.5, 20.5]%; minimum gap is 15.5 percentage points, relative discrepancy 15.5/20 = 0.775. Conversely, the complement of mRS 0–3 gives 62% mRS ≥4 with interval [60, 64]%, versus the 80% interval [79.5, 80.5]%; gap 15.5 percentage points, relative discrepancy 15.5/80 = 0.19375. Summing the two visible mRS 5–6 segments gives 63%, compatible with 62% after independent rounding. It does not approach 80%. The broad word “approximately” supplies no quantitative alternative interval; ordinary whole-percentage precision leaves a substantial conflict.

**Focus area:** A, primary mRS outcome distribution and derived functional-outcome threshold.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** The 90-day outcome distribution and independent-ambulation proportion among EVT patients with core ≥100 mL, specifically whether mRS 0–3 is about 20% or about 38% and mRS ≥4 about 80% or about 62%.

**Why context does not resolve it:** The figure and discussion identify the same core threshold and EVT population. The difference changes the extraction and interpretation of the primary mRS outcome distribution; it is not merely a peripheral secondary time-point comparison. Figure legend colors and caption identify categories, and the definition of independent ambulation is explicit. The 18-percentage-point difference exceeds the precision rule. The two complementary percentages are one repeated pattern, consolidated here.

**Alternatives and missing definition:** Figure 2 is intention-to-treat, while “received EVT” in the discussion could refer to as-treated classification. The report describes only two MM-to-EVT crossovers; such a change cannot explain a reduction from about 38% to about 20% in a 51-person stratum without additional unreported population changes. Another possibility is a different core-volume threshold or outcome cut point, but neither is stated in the discussion sentence. No alternative is adopted as a correction.

**Exact human question:** Which population, core-volume threshold and mRS cut point underlie the discussion’s approximately 80% mRS ≥4 and one-in-five independent-ambulation statements, and how do they reconcile with Figure 2B?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p. 5 Table 1, coronary artery disease; N033 | Header n168 gives 39/168 = 23.214% vs 23.5% and 25/168 = 14.881% vs 15.4%. Even treating counts as exact, gaps after the printed ±0.05% interval are 0.236/23.5 = 0.0100 and 0.469/15.4 = 0.0305; allowing count/denominator half-units only reduces them. Both are below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 5 Table 1, tenecteplase, thrombolytics and anesthesia; N053, N054 | Tenecteplase is nested in thrombolytic recipients, not all168 participants: 4/33 = 12.121% vs12.5% and 1/28 = 3.571% vs3.7%; residual relative gaps are below0.05 even with exact counts. Anesthesia100/168 =59.524% vs59.9%, thrombolytics28/168 =16.667% vs16.8%, also within threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 7 Figure 2, all four arm rows; N071, N072, N073, N074 | Whole-percentage segment totals are101,101,101,99. Independent half-unit intervals contain100; category colors, rather than text extraction order, establish missing-width categories. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp. 6, 7 and9, aRR abbreviation expansion; N080, N083, N086, N090, N092, N094, N098, N100, N102 | “Absolute risk reduction” expansion differs from the ratio quantity evident from modified Poisson methods, null1, ratio-valued intervals and footnotes stating higher rate ratio. The ratio interpretation is immediately identifiable; no conflict with an evidently computed alternate numeric measure was reproduced. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 9 Table3; N088, N090, N092, N094, N096, N098, N100, N102 | Crude within-arm mismatch/no-mismatch outcome ratios and median comparisons differ from some adjusted estimates; the table explicitly adjusts age, NIHSS, time and core. Direction reversals relative to crude counts do not establish a numeric conflict. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p. 11 discussion “two-thirds” versus p. 9 204(61%); N113 | Approximate prose fraction is not an additional independent population discrepancy; the materially different p. 4 count is retained in F-NUM-001. | DUPLICATE_OF_INCLUDED |

## Completion and limitations

All N001–N120 received an explicit review result in the companion inventory. Findings: 2. Excluded-observation rows: 6. Scientific coverage gaps: None. Exact patient category counts are not printed in Figure 2, and Figure 3 provides no exact pointwise prediction table; its plotted directions, category colors, axis scales and definitions were reviewed without inventing values. Inferential significance conflicts at rounded interval endpoints are the statistical lane's assigned checks and are not treated as rounding exclusions here.
# Numeric consistency checker — results A

Scope: DOC006 physical PDF pp1–32, REPORT. Complete relationship scope N1001–N1118 (118 records), including 48 paired bins, all 192 binary count/percentage arm cells in 32 forest cohorts across 3 outcomes, and 378 category percentages in54distribution arm bars. Direct source-linked visual confirmation: eFigure3p8, eFigure9p15, eFigure13p19, eFigure20x-aa p32; source-linked mapping covers all remaining assigned components. One finding; three excluded observations; zero scientific-coverage gaps. No statistical estimate/P compatibility substitution; that lane owns the mapped inferential relationships.

### F-NUM-101

**Title:** eFigure13 adverse-outcome directional annotations reverse the printed RR contrast.

**Locations and document roles:** REPORT results supplement [physical p19, eFigure13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19): all16rows, title, count headers, relative-risk axis definition, and direction annotations. REPORT same supplement [physical p15, eFigure9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=15), title/axis contrast and direction annotations, is corroborating direction context. This is S_W; all relationships S_W. Direct matched-source page images inspected; derivative values are locators, not substituted authority.

**Printed inputs:** eFigure13 defines complete dependence or death, mRS5–6 at90days. Axis explicitly says relative risk of achieving mRS5–6 in thrombectomy compared with medical management. BelowRR1 the annotation reads “Favours Medical Management”; aboveRR1 it reads “Favours Thrombectomy.” All16printed point estimates lie below1. The complete affected display is:

| Stratum | EVT count (%) | MM count (%) | RR (95% CI) | RR half-unit interval |
|---|---|---|---|---|
| NCCT<70(132) | 27(39.71) | 39(60.94) | .68(.49-.95) | [0.675,0.685] |
| NCCT≥70(204) | 49(49.00) | 63(60.58) | .77(.62-.97) | [0.765,0.775] |
| largest<70(80) | 14(33.33) | 17(44.74) | .82(.49-1.37) | [0.815,0.825] |
| largest≥70(256) | 62(49.21) | 85(65.38) | .72(.60-.88) | [0.715,0.725] |
| NCCT<100(207) | 37(35.92) | 60(57.69) | .61(.46-.81) | [0.605,0.615] |
| NCCT≥100(129) | 39(60.00) | 42(65.62) | .87(.69-1.10) | [0.865,0.875] |
| largest<100(165) | 26(32.50) | 44(51.76) | .62(.44-.86) | [0.615,0.625] |
| largest≥100(171) | 50(56.82) | 58(69.88) | .78(.64-.96) | [0.775,0.785] |
| NCCT<150(297) | 69(45.70) | 85(58.22) | .76(.62-.93) | [0.755,0.765] |
| NCCT≥150(39) | 7(41.18) | 17(77.27) | .55(.33-.94) | [0.545,0.555] |
| largest<150(273) | 59(43.70) | 78(56.52) | .72(.58-.90) | [0.715,0.725] |
| largest≥150(63) | 17(51.52) | 24(80.00) | .69(.48-.97) | [0.685,0.695] |
| profile1.2/10 0(74) | 12(35.29) | 23(57.50) | .67(.41-1.10) | [0.665,0.675] |
| profile1.2/10 1(262) | 64(47.76) | 79(61.72) | .74(.61-.90) | [0.735,0.745] |
| profile1.8/15 0(211) | 50(45.05) | 61(61.00) | .76(.60-.95) | [0.755,0.765] |
| profile1.8/15 1(125) | 26(45.61) | 41(60.29) | .71(.53-.97) | [0.705,0.715] |

**Rule and calculation:** Under the printed adverse-outcome definition and EVT/MM contrast, RR<1 means lower risk of complete dependence/death in EVT; RR>1 means higher risk in EVT. The axis assignments reverse that reading. For instance NCCT<70 prints27(39.71%) vs39(60.94%) and adjustedRR0.68(0.49–0.95); its RR interval[0.675,0.685] lies wholly below null1, but the plotted left half is labeled favorable to MM. This calculation uses the adjusted RR's own printed contrast, not a crude ratio as a replacement estimate. eFigure9 uses the same outcome/contrast and labels left favorable to thrombectomy/right favorable to MM.

**Display precision:** RR half-unit intervals above range from[0.545,0.555] to[0.865,0.875], all entirely below the exact dimensionless null1. Minimum gap to null1 is0.125 (relative0.125 against null1), maximum0.445; neither display precision nor uncertainty about rounding can place these point estimates above1. Directional annotation is qualitative and has no numeric half-unit interval of its own. No interval-versus-P claim is made. Count/denominator percentages in the display reconcile under the inventory rule.

**Focus area:** B, direction of effect across estimate, outcome, reference group and figure.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category2.

**Affected result or extracted value:** Direction of EVT treatment effect on90-day complete dependence/death across every NCCT/composite-core and composite-mismatch stratum in eFigure13. A reader using favorable-side annotations would reverse the treatment interpretation of each plotted RR.

**Why context does not resolve it:** Category2 applies to a direction/reference statement reversing printed numerical values. The outcome and arm contrast are explicit, but the favorable labels give the opposite treatment reading. The favorable label remains a printed interpretation even though another figure corroborates the RR convention.

**Alternatives and missing definition:** The labels may reflect the favorable-outcome convention used for mRS0–2/0–3, or the outcome/reference definition may have been intended differently. The source supplies no alternate favorable-outcome coding for this figure. Those are alternative interpretations, not assertions of a production mechanism. A reciprocal RR is not printed and is not substituted.

**Exact human question:** For eFigure13, should the favorable-side annotations follow the printed adverse mRS5–6 EVT/MM risk contrast, or is a different outcome or reference-group convention intended for these16reported RRs?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC006 p9 eFigure4 9–12h; p12 eFigure6a≥150mL and6b≥150mL; pp26–32 integer category bars | Integer percentage pairs68/33,28/73,83/18 total101; category sums vary around100. Independent half-unit sums contain100 and feasible category integer-count bounds contain their N. Remaining gap0; no count discrepancy reproduced. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC006 p17 eFigure11 NCCT≥150mL | AdjustedRR0.12(.01–1.05) differs markedly from crude(1/17)/(1/22)=1.2941. The supplied analysis specifies adjusted modified-Poisson modeling; comparing this to a crude ratio does not reproduce a label/measure inconsistency. No reverse-direction favorable claim is made in this row's numerical label. | MODEL_VERSUS_CRUDE |
| DOC006 pp13–19 forests versus p8 flow | Forest/distribution totals168/168 differ from explicitly labeled as-treated170/166. Main article Methods p4 specifies randomized allocation for treatment effects across strata and as-treated for within-arm imaging associations. The forest strata are randomized treatment effects, so unlike analysis definitions explain the apparent mismatch. Plan/report population comparison belongs to the cross-source lane. | CONTEXT_RESOLVES |

## Complete check result

N1001–N1118 all checked. Counts, exclusions, subgroups, denominator-percentage cells and distribution feasibility reconcile at stated precision. F-NUM-101 is the one consolidated directional pattern covering all16rows. Native graphs have no printed fitted-point coordinates; no invented numerical fitted estimates were used. Limitations: exact numeric fitted coordinates cannot be checked where not supplied; axes/outcomes/contrast and graphical direction were mapped. Source and reusable assets preserved; no new preprocessing derivatives.

# Numeric consistency checker: results B and administrative sources

Scope: DOC-006 physical PDF pp.33–53 (all13 eTables and final6 eFigure20 panels); DOC-002 pp.1–30; DOC-007 p.1. All52 assigned pages assessed. Relationships N2001–N2120:120 grouped records; one repeated-pattern finding; eight excluded apparent observations. Scientific gaps: None.

Read complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Reconstructed checks from the current complete results_b_admin map, source-linked reusable native text and all21 source-rendered DOC-006 images, with direct source pdftotext confirmation for pp.47–50. DOC-007 checked directly; DOC-002 administrative applicability assessed using complete per-page mapping and reusable text. No old conclusions or web used. CPU; direct text engine Poppler26.01.0, legacy rendered engine version unrecorded. No sources or reused artifacts changed.

Every local count/percentage triple, categorical total, nested/disjoint outcome partition, figure percentage vector, population partition, median/IQR ordering, estimate containment, direction and effect-measure identity was checked. All120 records and complete cell appendix are in relationships/numeric_parts/results_b.md. Adjusted estimates and prognostic volume slopes were not substituted with crude ratios. P/CI and model-specific inferential reproduction are independently tracked by statistical specialists.

### F-NUM-201

Discordant imaging profile2: mRS threshold count attribution and disjoint outcome totals do not reconcile in eTables9 and10.

- **Compared locations and document roles:** REPORT DOC-006 eTable9 physical p.47, discordant imaging profile2 (ASPECTS6–10 and CTP/MRI core≥70ml), functional independence and independent ambulation rows, and p.48 same profile complete dependence/death row; REPORT DOC-006 eTable10 physical p.49, discordant profile2 (ASPECTS6–10 and composite core≥70ml), functional independence and independent ambulation rows, and p.50 complete dependence/death row. Corroborating conflicting matched location: REPORT DOC-006 eTable8 pp.45–46, CTP/MRI discordant profile2 functional independence/ambulation cells. Physical page locators: [eTable8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45), [eTable8 continuation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46), [eTable9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47), [eTable9 continuation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48), [eTable10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49), [eTable10 continuation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50).
- **Printed inputs:** eTable9 MM has mRS0–2:1/11(9.1%), mRS0–3:3/11(27.3%), mRS5–6:10/11(90.9%); EVT has0/12(0%) for both favorable thresholds and8/12(66.7%) for mRS5–6. eTable10 MM has mRS0–2:2/12(16.7%), mRS0–3:4/12(33.3%), mRS5–6:11/12(91.7%); EVT has0/14(0%) for both favorable thresholds and9/14(64.3%) for mRS5–6. In eTable8 the corresponding CTP/MRI favorable counts are instead EVT1/12(8%),3/12(25%) and MM0/11(0%),0/11(0%); its adverse counts are EVT8/12(67%) and MM10/11(91%). eTables9/10 additionally print MM median(IQR)6(6,6), while the reported MM independent-ambulation counts imply27.3%/33.3% at mRS≤3.
- **Rule and calculation:** mRS0–3 and mRS5–6 are mutually exclusive in the same stated population, so their sum cannot exceed100%; mRS0–2 is also disjoint from mRS5–6. In eTable9 MM,3+10=13 exceeds11 and27.3+90.9=118.2%. In eTable10 MM,4+11=15 exceeds12 and33.3+91.7=125.0%;2+11=13 exceeds12 and16.7+91.7=108.4%. These are internal display contradictions and do not compare adjusted estimates with crude quantities.
- **Display-precision calculation:** treating every printed one-decimal percentage as±0.05 percentage points gives sum intervals[118.1,118.3],[124.9,125.1],[108.3,108.5]%. Even allowing the integer100% upper bound its own half-unit interval[99.5,100.5] gives minimum gaps17.6,24.4,7.8 percentage points and conservative relative discrepancies0.176,0.244,0.078, all above0.05. The exact normalization bound100% gives still larger gaps. The eTable8/eTable9 MM independent-ambulation percentages0% and27.3% have intervals[−0.5,0.5] and[27.25,27.35], gap26.75 points;relative discrepancy26.75/27.3=0.9799. EVT25% and0% yield intervals[24.5,25.5] and[−0.5,0.5], gap24 points;relative discrepancy24/25=0.96. Thus the matched favorable-outcome count attribution discrepancy also exceeds precision; nearby concordant-denominator changes are not used to establish the finding.
- **Focus area:** A, counts and denominators, with quantity-changing treatment attribution.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W; all compared locations are within the same REPORT document.
- **Qualifying route:** Route A, category3 (counts within one display); repeated favorable-count arm-attribution pattern retained in the same finding, rather than registered separately.
- **Affected result or extracted value:** treatment-specific functional independence and independent ambulation event counts/proportions in discordant imaging profile2, for CTP/MRI and composite core definitions; extraction of medical-management versus EVT subgroup outcomes and interpretation of accompanying mRS distributions.
- **Why context does not resolve it:** Route A category3 applies regardless of reconstruction of an intended reading. Both tables explicitly label MM then EVT and use the same within-profile denominators across outcome thresholds. The printed MM cells cannot all describe one mRS distribution; neighboring tables suggest a treatment attribution alternative but do not establish which supplied cells are authoritative.
- **Alternatives and missing definition:** favorable-outcome numerators may have been attached to different treatment columns than intended; alternatively the outcome rows could represent different undocumented populations or outcome coding. Each table explicitly prints the same denominator and profile definition, and no row-specific population distinction is supplied. The underlying counts and intended treatment attribution require confirmation; no correction is proposed.
- **Exact human question:** For discordant imaging profile2 in eTables9 and10, which treatment arm and analysis population do the mRS0–2 and mRS0–3 counts represent, and how do they reconcile with the same arm's mRS5–6 counts and mRS distribution? For CTP/MRI profiles, which counts should a data extractor use when eTable8 assigns the favorable events to EVT but eTable9 assigns them to MM?
- **Relationship inventory:** N2091, N2092, N2093, N2094, N2096, N2097, N2098, N2099, N2100, N2101, N2102, N2103, N2104, N2105, N2120. The complete inventory is authoritative for exact grouping; all affected cells are enumerated there and in its appendix.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-006 p.35,eTable1 coronary artery disease |39/170=22.94% versus23.2%;25/166=15.06% versus15.6%. Conservative half-count/denominator intervals give the latter[14.7147,15.4079]% versus[15.55,15.65]%;gap0.1421/15.6=0.0091. The apparent discrepancy does not exceed0.05; unknown row-specific denominators need not be inferred. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 p.36,eTable1 tenecteplase |4(12.5%) and1(3.7%) are treatment-subset cells;parent thrombolytic counts33/28 give12.12%/3.57%, within input/output half-unit intervals. Denominator is not the entire arm. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 p.36,eTable1 IV thrombolytics/general anesthesia |28/166=16.87% versus17.0%;100/170=58.82% versus59.5%. Half-unit intervals overlap or leave relative gap below0.05;no qualifying count/percentage inconsistency. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 pp.33–34,eFigure20 |Some seven-category percentage rows total99%,101% or102%; seven independently rounded integer percentages allow these sums. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 pp.38,41,eTables2/5 |EVT65/168 versus66/170 and MM31/168 versus30/166 for ambulation;tables explicitly distinguish intention-to-treat from as-treated. | CONTEXT_RESOLVES |
| DOC-006 pp.33–34,43–44,eFigure20/eTable7 |Figure core mismatch arm totals168/168;table7 arm totals170/166. Printed as-treated table7 title explains the different population. | CONTEXT_RESOLVES |
| DOC-006 pp.43–50,eTables7–10 adjusted measures |Several aRR/aRD/aGenOR point directions or magnitudes differ from crude ratios/differences of printed outcome frequencies (for example eTable8 EVT discordant1 mRS0–2 crude ratio(21/76)/(10/75)=2.07 versusaRR0.51). Models/adjustment and conditional within-arm comparisons are explicit;no display claims these estimates are crude. | MODEL_VERSUS_CRUDE |
| DOC-006 pp.45–48,eTables8/9 concordant denominator/adverse counts |EVT denominator75 versus74,MM82 versus83;adverse counts42 versus41 and59 versus60. All count intervals overlap or residual differences are below0.05. These nearby cells do not remove the larger discordant2 pattern. | ROUNDING_OR_DISPLAY_PRECISION |

Limitations: baseline row-specific denominators and eTable7 treatment/last-column headings are not printed; adjusted estimates and median summaries cannot be regenerated from aggregate data alone. All supplied cells assessed;no scientific coverage gap. Source-rendered images and direct native PDF extraction independently agree for every finding input. Statistical specialists own estimate/test method reconciliation, including comparison of aRR versus aRD significance for the same contrast;those comparisons have not been screened out here.
