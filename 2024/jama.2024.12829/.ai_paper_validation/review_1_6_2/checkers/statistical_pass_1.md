# Statistical pass 1

Agent ID: 01a12bd6-b838-7691-a3a4-d96d154fa89c. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: all 203 mapped source pages and every inferential result, producing-method relationship, primary/secondary analysis-population relationship and statistical-design relationship in the complete new evidence maps. The coordinator confirmed the support map's complete lossless merge before scientific review. Canonical inventory: 132 stable relationships, each with PASS_1_COMPLETE in statistics/relationship_inventory.md. Seven findings and 18 excluded observations are recorded below. No candidate IDs or adjudications are assigned here.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md; also tooling_record.md, source/coverage/evidence inventories, the complete main map, and bounded authored sections of every support mapping part. Used only supplied evidence. No old findings, reports, screening decisions or classifications were consulted. Rendering/text extraction used the pinned package-local PyMuPDF 1.26.4 helper; all new renders were CPU 200 dpi, and no OCR was required. Source image readings supersede derivative glyph omissions.

## Findings

### F-ST1-001

**Reporting issue:** The printed 1-year outside-territory stroke incidence-difference interval excludes its own point estimate and zero despite the nonsignificant paired hazard-ratio result.

**Relationships:** S010. **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W.

**Exact locations and roles:** REPORT [main article PDF p8, Table 2, secondary row “Any stroke outside the territory of the qualifying artery within 1 y after enrollment” and table incidence-difference column](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8). The same row supplies its count/denominator, HR/CI and P comparators; M4 states 95% CI s and two-sided.05 inference. Fresh current-source render preprocessing/stat1-main-p8.png was inspected visually; direct-current-source native/layout text confirms the same signs.

**Printed values:** B3/249(1.2%), M4/252(1.6%); incidence difference−0.4 percentage points, 95% CI−2.4 to−1.7; HR 0.76(95% CI 0.17–3.40), P=.72. The report calls incidence differences post hoc; the HR is Cox-derived and the paper says similar comparison approaches for secondary outcomes.

**Rule and reproduced calculation:** The difference point−.4 is greater than the printed upper endpoint−1.7 and is outside its own ordered interval. Allowing displayed half-units yields point[−.45, −.35] and upper endpoint[−1.75, −1.65], which cannot contain the point. The printed difference interval excludes 0, whereas the same-row HR interval includes 1 and P=.72>.05. This is a route A category 1 issue regardless of the difference/HR analysis distinction. As an additional reproducing-display check, unpooled binomial Wald arithmetic d=100(3/249−4/252)=−.382482 and SE=100 sqrt[p B(1−p B)/249+p M(1−p M)/252] gives 95% CI[−2.436163, +1.671198]. That arithmetic reproduces every other non-NA distinct Table 2 difference row to its printed precision. Allowing the displayed count/denominator inputs their half-unit intervals gives a recomputed upper-limit interval[+1.264896, +2.078084]; its gap from printed[−1.75, −1.65] is 2.914896, relative discrepancy 2.914896/1.7=1.714645>.05. Category 1 itself is exempt from the relative-discrepancy screen.

**Qualifying route:** Route A, category 1. The same printed sign also meets categories 2 and 4; these are additional grounds for this single issue, not separate findings.

**Affected result or extracted value:** The 95% incidence-difference CI for 1-year stroke outside the qualifying artery territory, including whether it excludes no difference.

**Why context does not resolve it:** Category 1 always registers point-estimate containment and interval-versus-P/test conflicts. The neighboring HR/P cells do not supply an authoritative replacement for the printed difference interval.

**Alternatives and missing definitions:** The source distinguishes Cox time-to-event analysis from post hoc incidence differences, so they may be different analyses. This does not remove the point-containment conflict. The matching binomial arithmetic suggests a sign-related alternative for the upper endpoint, but no replacement is assigned. The source does not explicitly identify the incidence-difference CI construction algorithm.

**Exact human question:** Which incidence-difference interval and upper-endpoint sign should a reader extract for the 1-year outside-territory stroke row, and how does that interval relate to the stated P=.72 analysis?

### F-ST1-002

**Reporting issue:** The BMI forest analysis described as prespecified uses two strata while all supplied subgroup plans specify three BMI strata.

**Relationships:** S034, S035, S102, S128. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R.

**Exact locations and roles:** REPORT [main PDF p4, Statistical Analysis, “All subgroup analyses in the forest plot were prespecified”](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4) and [p7 Figure 2 BMI rows and interaction P](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=7). PLAN [original protocol p41 lines 760](../../../joi240088supp2_prod_1746815064.36071.pdf#page=41), [final protocol p103 lines 1779](../../../joi240088supp2_prod_1746815064.36071.pdf#page=103), [original SAP p140 subgroup list](../../../joi240088supp2_prod_1746815064.36071.pdf#page=140), and [final SAP p160 line 2768](../../../joi240088supp2_prod_1746815064.36071.pdf#page=160). The final protocol and final SAP locations were reread directly from the current PDF with the pinned helper; original-version locations corroborate that the same three-bin rule recurs. Amendment tables pp124–126 and 165–166 contain no BMI-bin amendment.

**Printed values/statements:** PLAN BMI<25, 25–30, ≥30 kg/m². REPORT BMI<25: B3/110, M17/110, HR.17(.05–.57); BMI≥25: B8/139, M17/142, HR.48(.21–1.11); shared interaction P=.17. REPORT explicitly describes all forest subgroup analyses as prespecified.

**Rule and reproduced logical comparison:** The planned BMI factor has three levels and separate 25–30/≥30 contrasts; the reported forest has two levels, combining all BMI≥25. The supplied plans do not specify the resulting two-level BMI analysis as prespecified. This is an analysis specification comparison rather than numeric rounding. No three-level interaction P or subgroup HR is reconstructed from the collapsed display. The source's 25–30 versus≥30 boundary wording is preserved and does not explain replacing both strata with≥25.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The BMI≥25 treatment-effect HR.48(.21–1.11), and the meaning/prospective specification of the BMI interaction P=.17.

**Why context does not resolve it:** Category 5 always registers an analysis described as prespecified that the supplied plan does not contain. Prespecification of the BMI factor does not establish prespecification of a different category grouping.

**Alternatives and missing definitions:** A later decision may have pooled the upper two BMI categories, or an additional plan amendment may exist, but neither is supplied or disclosed for this analysis. The observed subgroup event counts alone do not establish why the grouping changed. No preferred grouping or analysis is proposed.

**Exact human question:** Was the two-level BMI analysis with≥25 kg/m² and interaction P=.17 prespecified in a supplied plan amendment, or how should its relationship to the supplied three-level BMI analysis be recorded?

### F-ST1-003

**Reporting issue:** The reported test specification for three safety rows differs from the supplied SAP's Fisher-exact specification.

**Relationships:** S064, S065, S069, S107; S047 is the matching disabling-stroke narrative. **Focus areas:** C, D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R. Both the report's own method label and the plan comparator are necessary to this issue.

**Exact locations and roles:** PLAN [original SAP PDF p142 §12.4 AEs](../../../joi240088supp2_prod_1746815064.36071.pdf#page=142) and [final SAP p162 lines 2801–2806](../../../joi240088supp2_prod_1746815064.36071.pdf#page=162): grouped AE event comparisons use Fisher's Exact test. REPORT [results supplement p24 Table S11 overall, nervous-system and disabling-stroke rows, superscript c and footnote c](../../../joi240088supp1_prod_1746815064.21247.pdf#page=24): “Tested by Chi-square test.” Current-source render preprocessing/stat1-supp-p24.png was inspected; the final SAP source was reread directly. REPORT [main p6 disabling-stroke narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6) supplies the same .02 result. The supplement is REPORT by content; the bound SAP remains PLAN.

**Printed inputs:** Denominators B249/M252. Overall B12(4.8)/M14(5.6), P=.84 c; nervous-system B7(2.8)/M12(4.8), P=.35 c; disabling stroke B6(2.4)/M18(7.1), P=.02 c. The other twelve safety rows use Fisher superscript d. Disabling stroke is visually confirmed mRS≥2 at 1 year in the current source, matching main p3; no threshold discrepancy is claimed.

**Rule and calculation:** A prespecified method must be matched to the reported producing analysis without silently replacing either statement. The supplied final SAP specifies Fisher for every grouped AE, whereas these three rows label chi-square. Diagnostic two-sided probability-ordering Fisher calculations give .840916, .350060, .019621, reproducing all three printed P values, and that convention also reproduces every other Table S11 row. Pearson chi-square diagnostics give .710285, .253089, .013126; continuity-corrected chi-square gives .864965, .363360, .023139. The continuity-corrected values pass the display rule: after printed P half-unit allowances, relative gaps are approximately.0238, .0239, 0, respectively. Thus this finding does not assert a numeric P contradiction, does not impose Pearson as the only chi-square, and does not assert a changed significance decision. The reproducible observation is the planned-versus-reported statistical test specification and consequent producing-method identity.

**Qualifying route:** Route B. B1: an in-focus planned-versus-reported analysis specification and source-grounded method identity. B2: neither the table nor the supplied SAP explains the change or states the chi-square variant. B3: it changes which statistical test is recorded as producing the safety P values, particularly the disabling-stroke P=.02.

**Affected result or extracted value:** The generating test for the overall, nervous-system and disabling-stroke safety P values, including the extracted disabling-stroke result .02.

**Why context does not resolve it:** Exact Fisher reproduction and approximate continuity-corrected chi-square compatibility cannot identify which analysis actually produced the displayed results. The explicit plan/table method statements differ, and no reported amendment or test-selection rule resolves that difference.

**Alternatives and missing definitions:** Fisher may have been used with a different table footnote; alternatively, the analysis may have switched to a continuity-corrected chi-square calculation. The source does not specify the chi-square variant, test-selection criterion or amendment. The statistical choice itself is not criticized.

**Exact human question:** Which test produced these three safety P values, and should the relationship between the Fisher-exact SAP specification and the table's chi-square label be recorded as a disclosed analysis change or another source clarification?

### F-ST1-004

**Reporting issue:** The 90-day mRS 2 balloon-group count N=50 does not reconcile with its 2.0% label and group denominator 249.

**Relationships:** S007, S079. **Focus area:** A; it also affects the ordinal-data input for B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W. Main mRS inference corroborates relevance but is not a second conflicting document for this finding.

**Exact location and role:** REPORT [results supplement PDF p13 Figure S4, BA group header N=249 and mRS 2 leader label “2.0(N=50)”](../../../joi240088supp1_prod_1746815064.21247.pdf#page=13). Every BA category in the same bar is included: 205, 36, 50, 2, 0, 0, 1. Fresh current-source render preprocessing/stat1-supp-p13.png was inspected visually; N=50 is present in the current source, not only a text derivative. Main [p8 mRS 90-day result](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) provides contextual inference G 1.21(1.03–1.38), P=.01, without changing this within-display relationship type.

**Printed values:** N=249; mRS 2 count 50, percent 2.0. Remaining category counts 205, 36, 2, 0, 0, 1; the figure's percentage series 82.3, 14.5, 2.0, .8, 0, 0, .4.

**Rule and reproduced calculation:**50/249×100=20.080321%, not 2.0%. Allow count 50±.5 and denominator 249±.5: recomputed percentage[19.839679, 20.321932]%; printed 2.0±.05 gives[1.95, 2.05]%; gap 17.789679 and relative discrepancy 17.789679/2.0=8.894840>.05. BA category countsum 294 is also incompatible with N249: allowing each of seven count inputs±.5 gives[290.5, 297.5] versus group[248.5, 249.5], gap 41/249=.16466>.05. These are one count/denominator issue, not separate findings. A hypothetical five-person mRS 2 reading would sum 249 and its generalized-OR diagnostic is 1.20745, but that hypothetical is not substituted into the source record.

**Qualifying route:** Route A, category 3; the printed count reading also meets category 2.

**Affected result or extracted value:** The balloon-group 90-day mRS 2 category count and full ordinal distribution used in functional-outcome extraction; the count table cannot be reused mechanically to reproduce the published mRS inference without a source clarification.

**Why context does not resolve it:** Category 3 always registers within-display count/percentage/denominator discrepancies above the display threshold. A reader might reconstruct an alternative count, but category 2 does not permit replacing the printed count during extraction.

**Alternatives and missing definitions:** The percentage series and category total suggest a count-reading alternative; another denominator or category allocation would require a source explanation. The figure does not define a distinct denominator for this one category. No final correction is proposed.

**Exact human question:** Which printed count should be used for the BA 90-day mRS 2 category, and which complete ordinal count distribution corresponds to the generalized-OR analysis?

### F-ST1-005

**Reporting issue:** The original sample-size synopsis forecasts 91 endpoint events among 686 participants, which does not reproduce from its stated 1-year arm risks and 1:1 allocation.

**Relationships:** S084, S085, S086, S087. **Focus areas:** C, D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P; all relationships P_P. The main report's original 802-plan description establishes relevance but merely corroborates plan history and is not a conflicting relationship.

**Exact locations and roles:** PLAN [original protocol PDF p11 “Sample Size” synopsis](../../../joi240088supp2_prod_1746815064.36071.pdf#page=11): exponential event-time assumption, control 1-year 12.2%, BA primary-event 1-year 6.25%, hazard conversion, 5% control crossover at 3 months, 686 cases and total 91 estimated endpoint events. PLAN [p12 synopsis continuation](../../../joi240088supp2_prod_1746815064.36071.pdf#page=12): interim expansion 728 and final 802. PLAN [p18 design 1:1 and 12-month primary hypothesis](../../../joi240088supp2_prod_1746815064.36071.pdf#page=18), with [pp40–41 original detailed statistical section](../../../joi240088supp2_prod_1746815064.36071.pdf#page=40). Direct-current-source native/layout reads p11–12 and 40–41 confirmed these inputs. REPORT [main p3 original 802 sample plan](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=3) and PLAN final amendment p126 explicitly disclose later 512 re-estimation; this finding concerns the reported original design history and does not challenge the final 512 target.

**Printed values:**686 cases, estimated total 91 endpoint events across both groups; one-year M 12.2%, B6.25%; 1:1 allocation. HazardλM13.01%, λB6.45%; adjustedλM*=12.76% after 5% crossover; “90% confidence, ” bilateralα=.05 and 50% relative reduction. The synopsis separately states 728 then 802.

**Rule and reproduced calculation:** For distinct first endpoint events by the specified 1-year horizon with 343 participants per arm, E(events)=343×(.122+.0625)=63.2835. Half-unit input allowances N686±.5, 12.2%±.05 percentage point, 6.25%±.005 percentage point give recomputed[63.048863, 63.518413]events. Printed 91±.5 gives[90.5, 91.5]; gap 26.981587, relative discrepancy 26.981587/91=.296501>.05. The supplied crossover hazard adjustment reduces the control risk to 1−exp(−.1276)≈11.98% and does not raise the expected total to 91. The source explicitly uses 1-year probabilities and an exponential assumption; no longer event-counting horizon, additional event count per person or separate event-triggered accrual step is supplied to obtain 91. This is not a claim that one unprinted log-rank sample-size formula must be used.

**Qualifying route:** Route B. B1: an in-focus sample-size/power input and event forecast in supplied plan material cited as the original design. B2: the supplied inputs do not show how 91 events arise. B3: 91 versus approximately 63 events changes the event-information input a reader would extract for the original power/sample-size design.

**Affected result or extracted value:** The original planned event target/forecast 91 and the quantitative basis of the original 686→728→802 sample-size history. The final 512 sample is not adjudicated by this finding.

**Why context does not resolve it:** The paragraph provides both arm 1-year risks and event forecast but not a distinct horizon or endpoint-counting rule. The later sample amendment changes the final design, but does not reconcile the numeric relation printed for the original design.

**Alternatives and missing definitions:**91 could refer to a required-event information target rather than expected first 1-year events, or to an additional horizon/accrual calculation. An event-driven target can be internally coherent if identified and linked to accrual assumptions; those steps are not printed here. The “90% confidence” wording is not silently converted to 90% power and is not a separate finding. No preferred sample-size formula is proposed.

**Exact human question:** Does 91 denote a required information/event target or an expected 1-year event total, and what horizon, endpoint-counting rule and accrual step connect it to 686 participants and the printed arm risks?

### F-ST1-006

**Reporting issue:** The per-protocol outcome table's group headers give 249/252 while the supplied flowchart and per-protocol sensitivity table give 233/238.

**Relationships:** S053, S054, S055, S056, S062, S118. **Focus area:** A, with primary sensitivity-population interpretation under C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C; all relationships S_C, S_W.

**Exact locations and roles:** REPORT [results supplement PDF p21 Table S8 title/per-protocol group headers and all four outcome rows](../../../joi240088supp1_prod_1746815064.21247.pdf#page=21). REPORT [main PDF p5 Figure 1 per-protocol boxes](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5): B233, M238, distinct from primary B249, M252. REPORT [results supplement p23 Table S10 per-protocol row](../../../joi240088supp1_prod_1746815064.21247.pdf#page=23): B233, M238. Current-source native/layout reads M5, R21, R23 and fresh render preprocessing/stat1-supp-p21.png confirmed the headers and their per-protocol title.

**Printed values:** Table S8 B header n=249, M header n=252; PP primary B9(3.9), M33(13.9), HR.27(.13–.56), P<.001; early 6(2.6)/4(1.7), late qualifying stroke 1(.4)/18(7.6), late revascularization 3(1.3)/20(8.4). Main flowchart PP 233/238; supplement Table S10 PP 233/238.

**Rule and reproduced calculation:** These are printed copies of the sample sizes for the same per-protocol population, not crude estimates compared with Cox HR s. B header 249±.5 versus PP 233±.5 gives intervals[248.5, 249.5]and[232.5, 233.5], gap 15, relative discrepancy 15/249=.060241>.05. M252±.5 versus 238±.5 gives[251.5, 252.5]and[237.5, 238.5], gap 13, relative discrepancy 13/252=.051587>.05. The printed row percentages corroborate the smaller PP denominators: 9/233=3.8627%, 33/238=13.8655%, 6/233=2.5751%, 18/238=7.5630%. Some individual count/percentage mismatches against 249/252 would be screened under the half-unit/relative.05 rule; the qualifying discrepancy is the actual per-protocol population size copied between sources. All four Table S8 rows share one set of conflicting headers and are consolidated.

**Qualifying route:** Route B. B1: same primary sensitivity-analysis population size across reports. B2: the table explicitly labels per-protocol but gives the primary analysis's denominators. B3: a reader may extract 249/252 as the PP population or use them when interpreting the primary sensitivity HR.

**Affected result or extracted value:** The per-protocol primary-analysis Ns underlying HR.27(.13–.56), and the denominator for each per-protocol component row.

**Why context does not resolve it:** Corroborating 233/238 elsewhere does not establish whether the S 8 headers or the S 8 analysis population apply to its reported HR; a reader may record the printed Ns literally. This difference concerns an analysis-population size and is therefore not a peripheral per-time-point contributor count.

**Alternatives and missing definitions:** The S 8 headers could reflect a broader cohort while percentages reflect PP participants, or a distinct outcome-specific PP population could exist. No such split or outcome-specific denominator rule is stated. The row percentages indicate an alternative but are not assigned as a final correction.

**Exact human question:** Which Ns define the per-protocol cohort for Table S8 and its HR .27 result, and how should its 249/252 headers be reconciled with 233/238 in the flowchart and Table S10?

### F-ST1-007

**Reporting issue:** The center-adjusted primary-outcome display gives nine balloon-group events while the full primary-outcome display gives eleven with the same 249 group header.

**Relationships:** S001, S017, S050. **Focus areas:** A, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C; all relationships S_C.

**Exact locations and roles:** REPORT [results supplement PDF p19 Table S6, primary row, B group header and center-adjustment footnotes](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19): header 249, 9(3.9), adjusted HR.32(.16–.62), P.001; the footnote describes adjustment for group and two center categories, Beijing Tiantan versus others. REPORT [main p8 Table 2 primary row](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8): 249 header, 11(4.4), HR.32(.16–.63), P<.001. REPORT [main p6 center-adjustment narrative](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6): same adjusted HR.32(.16–.62), P.001, with no different population described. Current-source R19 and M8 were read directly and visually inspected in preprocessing/stat1-supp-p19.png and stat 1-main-p8.png.

**Printed values:** B9(3.9)versus 11(4.4), both N249 and same composite endpoint definition. M34(13.5)appears in both. Adjusted versus main HR s are retained as distinct model results and not compared as crude effects.

**Rule and reproduced calculation:** A modeled adjustment may change an HR, but the table's printed No.(%)is still a raw event count and requires its own population/endpoint definition. Count 9±.5=[8.5, 9.5]versus 11±.5=[10.5, 11.5]gives gap 1, relative discrepancy 1/11=.090909>.05. Percent 3.9±.05 versus 4.4±.05 gives gap.40, relative discrepancy.40/4.4=.090909>.05. No different N, endpoint window or exclusion rule is printed for S 6. The within-table 9/249 versus 3.9 percentage discrepancy alone would pass the half-unit/relative.05 screen, so it is not the independent ground for this finding.

**Qualifying route:** Route B. B1: a primary outcome count differs between matched report displays beyond precision. B2: model adjustment alone does not identify a new event count or analysis cohort. B3: it changes the count/risk extracted for the adjusted primary analysis.

**Affected result or extracted value:** The balloon-group primary event count and risk in the center-adjusted primary analysis, associated with HR.32(.16–.62), P.001.

**Why context does not resolve it:** The source specifies center adjustment but not a changed cohort or outcome definition; all printed Ns remain 249/252. A reader cannot identify from the supplied methods which two balloon-group events, if any, are not included in the adjusted primary display.

**Alternatives and missing definitions:** A complete-case or other restricted model cohort could explain fewer events, or an additional descriptive population could have been used. The source does not give any such cohort definition or event-exclusion step. Similar HR s do not identify the raw count. No replacement count or model is proposed.

**Exact human question:** Which primary event count and analysis population underlie Table S6's nine balloon-group events, and what population or endpoint step distinguishes that count from Table 2's eleven events?

## Excluded observations

Only apparent issues that were considered and not emitted are listed. Each has exactly one reason code. Coherent routine checks remain in the 132 relationship records rather than this table. An excluded row never suppresses any of the seven independent findings above.

| Location | Observation | Reason code |
|---|---|---|
| REPORT R24 footnote b versus M3 adverse-event definition | Native/map text rendered >2, but fresh current-source image prints ≥2 in both reports; derivative-only threshold difference. | NOT_REPRODUCED |
| REPORT M7 forest HR CI s versus interaction P column | Apparent significant within-stratum CI versus nonsignificant P compares different nulls; the P column is interaction and not the row's treatment test. | NOT_REPRODUCED |
| REPORT M7 hypoperfusion I.99/HRNA | Zero-control-events interaction could have unstable fit, but no coefficient/variance/convergence output establishes a printed conflict. | CONDITIONAL_OR_UNREPORTED |
| REPORT M8 mRS 90 d versus R13 | An OR reconstructed excluding all ties differs from 1.21; the half-tie WMW generalized OR diagnostic is 1.20745 and the reported definition allows that convention. | CONTEXT_RESOLVES |
| REPORT M8/R13 mRS 1 y P | Tie-corrected WMW diagnostic P.004838 versus printed.01: gap from printed[.005, .015]is.000162, relative.0162≤.05; individual SAS/CI options absent. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN P102/P161 versus REPORT M4 | Planned ordinal-logistic model replaced by WMW after explicit proportional-odds failure, with producing analysis stated; not a changed outcome status or unreported primary/key secondary analysis. | CONTEXT_RESOLVES |
| PLAN P156 versus REPORT M4/M6/R19 | Center adjustment called post hoc despite planned center sensitivity; pooling other centers is compatible with the nonspecific SAP and the wording does not identify an independent result change. | TERMINOLOGY_OR_WORDING |
| PLAN P161 versus REPORT M5/R17 | Planned between-arm restenosis OR absent; restenosis is unranked secondary and not a 1-year primary/key secondary omission or changed status. | CONDITIONAL_OR_UNREPORTED |
| PLAN P11 versus P41/P134 |90% confidence versus 80% power are not matched quantities; no 90% power definition is printed. | TERMINOLOGY_OR_WORDING |
| PLAN P12/P41/P134/P166 |728 after interim and 10% attrition versus final 802: inverse-retention rounding interval gap≈1.37/802=.0017≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT R22/R23 ATS headers |249/252 versus 247/254 gives a half-unit gap 1 per arm, relative≤.0041; row percentage comparisons also≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT R13 Figure S5 |AMM count sum 249 versus header 252 and 169/252=67.063% versus 67.9% are both below relative.05; all other category pairs are within display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT M7/M8 versus R13 Figure S5 |AMM total 1-year death 1 versus mRS 6 count 2 is a cross-location secondary time-point distribution comparison without a demonstrated primary event or analysis-population size change. | PERIPHERAL_COMPARISON |
| PLAN P11 versus REPORT M3 |Original medical risk 12.2% versus printed 12%:half-unit intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN P103/P153 versus REPORT M3 |One-sided .025 planning versus two-sided .05 reported convention have equal normal critical values; these are not matched copies of the same-sided alpha. | NOT_REPRODUCED |
| PLAN P76/P151 versus P69/P103/P153 |50% relative hypothesis versus 15%→7% planning risks: half-unit input ranges allow relative 48.276%–58.065%, overlapping 50±.5%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT R6 diagram versus M3/PLAN P69/P73 |30±3 versus 30±7 visit schedule copies do not establish changed endpoint windows, event assignment, primary/key secondary result or population. | PERIPHERAL_COMPARISON |
| PLAN P8/P65/P89/P152 versus REPORT M3/R25 |Broad BP management phrases versus detailed DM targets; the DM-specific targets appear in the results supplement and no changed primary decision rule or intervention dose/duration is demonstrated. | OUT_OF_FOCUS |

## Completion and limitations

All 132 canonical relationships have explicit pass 1 records; all 203 source units are mapped in the new main/support evidence maps. Seven findings preserve every affected location and supplied alternative; no candidate count target was used. Five fresh current-source PNG derivatives were produced with the supplied helper, PyMuPDF 1.26.4, CPU 200 dpi, and are listed in the relationship inventory. No new OCR, source change or reused asset change occurred. Individual event times, individual ordinal observations, Cox variance/test options, exact generalized-OR CI algorithm and sample-size accrual/software equations are not supplied; those named limitations constrain exact mechanical reconstruction without leaving a scientific coverage unit unmapped. All findings were checked against current direct sources, and all sources are final authority over native/OCR aids. A distinct fresh high-effort agent must perform pass 2; this agent has not been promoted or reused for that stage.

## Explicit completed relationship index

Mechanical packaging expansion of the completed grouped relationship ranges. Scientific checks and source-specific outcomes remain in the canonical inventory and the pass procedures above; this index makes every reviewed ID explicit and introduces no additional scientific decision.

| Relationship ID | Completed pass marker |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
| S066 | PASS_1_COMPLETE |
| S067 | PASS_1_COMPLETE |
| S068 | PASS_1_COMPLETE |
| S069 | PASS_1_COMPLETE |
| S070 | PASS_1_COMPLETE |
| S071 | PASS_1_COMPLETE |
| S072 | PASS_1_COMPLETE |
| S073 | PASS_1_COMPLETE |
| S074 | PASS_1_COMPLETE |
| S075 | PASS_1_COMPLETE |
| S076 | PASS_1_COMPLETE |
| S077 | PASS_1_COMPLETE |
| S078 | PASS_1_COMPLETE |
| S079 | PASS_1_COMPLETE |
| S080 | PASS_1_COMPLETE |
| S081 | PASS_1_COMPLETE |
| S082 | PASS_1_COMPLETE |
| S083 | PASS_1_COMPLETE |
| S084 | PASS_1_COMPLETE |
| S085 | PASS_1_COMPLETE |
| S086 | PASS_1_COMPLETE |
| S087 | PASS_1_COMPLETE |
| S088 | PASS_1_COMPLETE |
| S089 | PASS_1_COMPLETE |
| S090 | PASS_1_COMPLETE |
| S091 | PASS_1_COMPLETE |
| S092 | PASS_1_COMPLETE |
| S093 | PASS_1_COMPLETE |
| S094 | PASS_1_COMPLETE |
| S095 | PASS_1_COMPLETE |
| S096 | PASS_1_COMPLETE |
| S097 | PASS_1_COMPLETE |
| S098 | PASS_1_COMPLETE |
| S099 | PASS_1_COMPLETE |
| S100 | PASS_1_COMPLETE |
| S101 | PASS_1_COMPLETE |
| S102 | PASS_1_COMPLETE |
| S103 | PASS_1_COMPLETE |
| S104 | PASS_1_COMPLETE |
| S105 | PASS_1_COMPLETE |
| S106 | PASS_1_COMPLETE |
| S107 | PASS_1_COMPLETE |
| S108 | PASS_1_COMPLETE |
| S109 | PASS_1_COMPLETE |
| S110 | PASS_1_COMPLETE |
| S111 | PASS_1_COMPLETE |
| S112 | PASS_1_COMPLETE |
| S113 | PASS_1_COMPLETE |
| S114 | PASS_1_COMPLETE |
| S115 | PASS_1_COMPLETE |
| S116 | PASS_1_COMPLETE |
| S117 | PASS_1_COMPLETE |
| S118 | PASS_1_COMPLETE |
| S119 | PASS_1_COMPLETE |
| S120 | PASS_1_COMPLETE |
| S121 | PASS_1_COMPLETE |
| S122 | PASS_1_COMPLETE |
| S123 | PASS_1_COMPLETE |
| S124 | PASS_1_COMPLETE |
| S125 | PASS_1_COMPLETE |
| S126 | PASS_1_COMPLETE |
| S127 | PASS_1_COMPLETE |
| S128 | PASS_1_COMPLETE |
| S129 | PASS_1_COMPLETE |
| S130 | PASS_1_COMPLETE |
| S131 | PASS_1_COMPLETE |
| S132 | PASS_1_COMPLETE |
