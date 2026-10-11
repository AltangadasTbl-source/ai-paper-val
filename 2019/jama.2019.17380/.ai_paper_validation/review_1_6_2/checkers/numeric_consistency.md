# Numeric consistency review — Workflow 1.6.2

Fresh numeric consistency specialist; scope all 70 mapper N groups and four added groups N052–N055, total 74. Every constituent count, denominator, percentage, allocation, flow branch, analysis set, event marginalization and numeric measure label was reviewed. Full completed records: [numeric inventory](../relationships/numeric_relationship_inventory.md). Five findings below consolidate repeated patterns; six excluded observations are recorded once. No stable candidate IDs assigned. Source roles are determined from content. No scientific coverage gap.

Direct-source confirmation used Poppler `pdftotext -layout` on main PDF pp7–9, results supplement pp7/12/18/19 and protocol pp15/21, plus visual inspection of source-matched canonical page images. Image-only eFigures 2/3 were additionally rendered freshly from the supplied PDF on CPU with `pdftoppm -f 18 -l 19 -scale-to 2000 -png joi190122supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric_checker/supp2`. Both images were read visually; derivatives are `preprocessing/numeric_checker/supp2-18.png` and `preprocessing/numeric_checker/supp2-19.png`, engine Poppler pdftoppm, CPU, no OCR. Native text contains only captions for these image-only displays. Direct-source and fresh image readings match the mapped count cells.

## Findings

### F-NUM-001

**Reporting issue:** Omega-3 contributor-count rows in Figure 2 repeat the vitamin-D counts and conflict with the matched omega-3 population.

**Relationships:** N001,N046,N047,N052,N108. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationships:** S_W and S_C (primary S_C by precedence).

**Compared locations and roles:** REPORT [main article p7, Figure 2 panels B/D and contributor caption](../../../jama_de_boer_2019_oi_190122.pdf#page=7); REPORT [main article p8, Table 2 omega-3 rows](../../../jama_de_boer_2019_oi_190122.pdf#page=8); REPORT [results supplement p11, eTable 6 omega-3 rows](../../../joi190122supp2_prod.pdf#page=11). REPORT [main article p1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=1) corroborates the population cap.

**Printed inputs:** Figure 2 panelB placebo 607/459/438 and omega 701/531/496 at baseline/year 2/year 5; Table 2 omega placebo 651/491/462 and active 657/499/472. Figure 2 panelD placebo 609/463/440 and omega 702/529/505; eTable 6 placebo 653/490/467 and active 658/502/478. PanelsA/C print exactly the same contributor rows asB/D. Allocation contains 659 omega-active participants.

**Rule and calculation:** For two displayed copies, each integer gets±.5; interval gap=absolute difference−1. Reference is matched table count. All eGFR panelB cells are retained: active gaps 43/657=.06545,31/499=.06212,23/472=.04873; placebo 43/651=.06605,31/491=.06314,23/462=.04978. The first two time points exceed.05; year 5 eGFR alone does not. Baseline active 701±.5 also exceeds allocation 659 reconstructed from 370±.5+289±.5: allocation[658,660], observed[700.5,701.5], gap 40.5/659=.06146. All urine panelD cells exceed.05: active 43/658=.06535,26/502=.05179,26/478=.05439; placebo 43/653=.06585,26/490=.05306,26/467=.05567. Example intervals: active baseline eGFR[700.5,701.5] versus[656.5,657.5]; gap 43. Urine year 5 active[504.5,505.5] versus[477.5,478.5]; gap 26.

**Qualifying route:** Route A, category 2 (substituted contributor counts change magnitude beyond display precision). The above-allocation baseline count and primary-outcome population also satisfy Route B.

**Affected result or extracted value:** Intervention-specific sample sizes accompanying the primary omega-3 eGFR distribution and secondary urine-ACR distribution. Both full panels are affected locations of one repeated copying pattern; subthreshold year 5 eGFR comparisons are not separate findings.

**Why context does not resolve it:** Route A category 2 applies to the reproduced printed count cells. The caption expressly calls these data contributors; the omega 701/702 baseline cells exceed all omega-active randomized participants. No alternative analysis population is named. Recognizing repeated D rows does not remove the printed count a data extractor may take.

**Alternatives:** A separate graph population could in principle have different observation counts, but cannot contain more distinct omega-active participants than randomized. A repeated count-row layout is supported by exact matches with D panels; whether plotted data themselves follow the labels is not established from supplied summaries.

**Human question:** Which intervention-specific participant counts and populations should accompany every time point in Figure 2 omega-3 panels B/D, and do the plotted distributions use the same matching populations as Table 2/eTable 6?

### F-NUM-002

**Reporting issue:** Repeated subgroup displays associate active-arm participant counts with placebo outcome columns and placebo counts with active outcome columns.

**Relationships:** N021–N024,N040,N053,N054,N115,N117. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationships:** S_W and S_C (primary S_C). This is one repeated count-column attribution pattern across four figures; it does not assert that outcome values require swapping.

**Compared locations and roles:** REPORT [main article p8 Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), REPORT [main article p9 Figure 4](../../../jama_de_boer_2019_oi_190122.pdf#page=9), REPORT [supplement p18 eFigure 2](../../../joi190122supp2_prod.pdf#page=18), REPORT [supplement p19 eFigure 3](../../../joi190122supp2_prod.pdf#page=19). Comparators are REPORT [main article p5 Table 1 allocation, race and 25(OH)D categories](../../../jama_de_boer_2019_oi_190122.pdf#page=5), REPORT [main article p6 Figure 1 allocation](../../../jama_de_boer_2019_oi_190122.pdf#page=6), and REPORT [supplement p11 eTable 6 ACR changes](../../../joi190122supp2_prod.pdf#page=11).

**Printed inputs and affected locations:** Figure 3 and eFigure 2 place placebo 703/active 609 overall. Table 1 and allocation instead establish D active 370+333=703, D placebo 289+320=609. Both D figures place white 451/406, black 148/130,25(OH)D<20 counts 110/85,20–<30 counts 230/203,≥30 counts 332/297 under placebo/active. Table 1 marginal active/placebo counts are respectively 451/406,148/130,110/85,230/203,332/297, demonstrating opposite count attribution. Their ACR counts 635/559 and 67/50, eGFR 612/531 and 89/76, BMI 87/87,228/205,364/294 are retained as affected count columns under the same display pattern, without inventing external subgroup comparators. Omega-randomization strata in both D figures: placebo 333/320 and omega 370/289 under D placebo/D active; allocation expects 320/333 and 289/370.

Figure 4/eFigure 3 place overall omega-placebo 659/active 653 (this pair alone is subthreshold). Their vitamin-D-placebo stratum prints placebo 289/active 320; allocation expects 320/289. Their vitamin-D-active stratum prints placebo 370/active 333; allocation expects 333/370. All other omega figure subgroup count cells are recorded in N054/N117; no unsupported replacement is asserted.

**Rule and calculation:** A derived marginal sum of two integer inputs receives±1. D placebo 609 reference interval[608,610], printed 703[702.5,703.5], gap 92.5/609=.15189; D active 703 interval[702,704], printed 609[608.5,609.5], gap 92.5/703=.13158. White placebo derived 406±1 versus 451±.5: gap 43.5/406=.10714; active 451±1 versus 406±.5:43.5/451=.09645. Black gap 16.5/130=.12692 and 16.5/148=.11149. VitaminD<20 gap 23.5/85=.27647 and 23.5/110=.21364;20–<30 gap 25.5/203=.12562 and 25.5/230=.11087;≥30 gap 33.5/297=.11279 and 33.5/332=.10090. Single allocation-cell comparisons use two±.5 copies: omega-active stratum in D figures 370 vs289 gap 80/289=.27682 and 289 vs370 gap 80/370=.21622; omega-placebo stratum 333 vs320 gap 12/320=.0375 and 320 vs333 gap 12/333=.03604, retained only as subthreshold occurrences of the pattern. In omegafigures vitaminDplacebo-stratum 289 vs320 gap 30/320=.09375 and 320 vs289 gap 30/289=.10381; vitaminDactive-stratum 370 vs333 gap 36/333=.10811 and 333 vs370 gap 36/370=.09730.

Within Figure 3/eFigure 2, ACR strata printed under placebo sum 635+67=702, matching D active nearly fully rather than placebo 609. Sum interval[701,703] versus overall placebo 703[702.5,703.5] overlaps internally, but that overall placebo count conflicts with allocatedplacebo 609 above; this corroborates count-column attribution, not a separate subtotal finding.

**Qualifying route:** Route A, category 2 (substituted arm-count cells change extracted magnitudes), also Route B for primary-result subgroup sample sizes.

**Affected result or extracted value:** Counts paired with primary eGFR and secondary ACR subgroup means/dispersion values, including overall and factorial-cell counts. All four figures and every affected row count are retained in the consolidated pattern.

**Why context does not resolve it:** Route A category 2 applies. In Figure 3 the printed mean changes placebo−13.1/active−12.3 match Table 2, whereas their counts match opposite arms. In eFigure 2 placebo 3.02/active 2.97 matches eTable 6. Thus swapping the complete outcome columns does not resolve the count-value association. A reader cannot infer whether only counts or subgroup output columns require clarification.

**Alternatives:** Count columns may have been placed under opposite arm headers, while outcome columns retain the reported treatment contrast. A different subgroup analysis set cannot explain overallDplacebo 703 above its randomized 609 or opposite allocation-cell counts. Outcome-value attribution beyond independently matched overall changes remains a human question.

**Human question:** Which participant counts belong to each placebo/active subgroup result in Figures 3/4 and eFigures 2/3, and were count columns alone transposed or were subgroup outcome summaries also associated with different allocation cells?

### F-NUM-003

**Reporting issue:** eTable 7 paired-urine analysis population and exclusion accounting do not reconcile within one display.

**Relationship:** N109. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Compared locations and roles:** REPORT [supplement p12 eTable 7 title, baseline/year 5 rows and footnote](../../../joi190122supp2_prod.pdf#page=12).

**Printed inputs:** TitleN 944; Dbaseline/year 5 counts 504+440=944; omega 477+467=944. Footnote 1312 enrolled,1311 baseline samples,991 paired and included,320 baseline-but-no-year 5 exclusions,1 no-baseline exclusion.

**Rule and calculation:** Title/body imply exclusions among baseline responders 1311−944=367, whereas footnote prints 320. Allow 1311±.5 and 944±.5: recomputedexcluded[366,368]; printed 320 interval[319.5,320.5]; gap 45.5/320=.14219>.05. If deriveincluded 944 from 504±.5+440±.5 instead of title, included[943,945], baseline-minus-included[365.5,368.5], gap 45/320=.140625 still qualifies. Full-partition check 944+320+1=1265 versus 1312: the total-relative gap alone is below.05; excluded-count discrepancy is the reproduced relationship. Footnote 991+320=1311 internally reconciles, but conflicts with the separately printed body population;991 vs944 alone gap 46/991=.04642 (or46/944=.04873) is subthreshold and does not independently justify finding.

**Qualifying route:** Route A, category 3 (counts, analysis population and exclusions within one table).

**Affected result or extracted value:** Number excluded from the complete-case urine-ACR sensitivity analysis and accounting supporting its paired analysis population.

**Why context does not resolve it:** Route A category 3 applies to the reproduced exclusion comparison. Both sets are printed as the same included/excluded paired-sample analysis. The body consistently gives 944 while the footnote consistently supports 991; the supplied table does not state an additional eligibility filter for the 47-person difference.

**Alternatives:** Footnote 991/320 may describe a different available-sample subset, but that subset is expressly described as included in this analysis. An unstated additional 47-person filter or a repeated historical footnote could explain production, but neither is supplied evidence of the intended accounting.

**Human question:** How many participants with baseline urine samples were included and excluded in eTable 7, and what source-defined filter reconciles the title/body N 944 with footnote 991 included/320 excluded?

### F-NUM-004

**Reporting issue:** The year 5 vitamin-D-placebo SGLT 2 inhibitor count/percentage is incompatible with the same-column response denominator supported by the table.

**Relationship:** N104. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Compared locations and roles:** REPORT [supplement p7 eTable 2, vitamin-D-placebo year 5 biguanide and SGLT 2 rows and denominator footnote](../../../joi190122supp2_prod.pdf#page=7).

**Printed inputs:** Vitamin-D-placebo biguanides 313(74%), SGLT 2 inhibitors 21(4%); overall year 5N916 nonmissing responses. SameSGLT 2 row D active 25(6%), overall 46(5%), omega 24(5%)/22(5%).

**Rule and calculation:** The same column/time response denominator implied by313±.5 and 74±.5% is[312.5/.745,313.5/.735]=[419.4631,426.5306]. With 21±.5, recomputed percentage interval[100×20.5/426.5306,100×21.5/419.4631]=[4.80622,5.12560]%. Printed 4±.5% interval[3.5,4.5]%; gap.30622/4=.07655>.05. With nominal denominator near 423,21/423=4.96%, not 4%. The D active 25(6%) pair may point to a related switched percentage/denominator pattern, but under full half-count input intervals its gap is at most.27504/6=.04584 and is not independently reproduced. Count 25+21=46 reconciles; the finding is the placebo percentage/denominator relationship.

**Qualifying route:** Route A, category 3 (count and percentage within one table).

**Affected result or extracted value:** Year 5 SGLT 2 use proportion for the vitamin-D-placebo arm, printed 4% rather than the range supported by the other same-column row.

**Why context does not resolve it:** Route A category 3 applies if the footnote's common nonmissing response population governs the medication rows. The footnote supplies year-specific response N but no medication-specific denominator exception for SGLT 2. The ordinary same-column year 5 rows support about 423 respondents;21 at4% would require roughly 467–614 after half-unit count/percentage allowance.

**Alternatives:** A medication-specific denominator could change the computation; the supplied footnote does not describe one. Printed 4% could have used the opposite-arm responder denominator, but that is an inferred mechanism. No denominator is assigned as a final correction.

**Human question:** What exact vitamin-D-placebo year 5 denominator was used for SGLT 2 inhibitors 21(4%), and does it differ from the respondent population underlying other medication rows such as313(74%)?

### F-NUM-005

**Reporting issue:** The supplied plan assigns two different microgram equivalents to the same 2000 IU vitamin-D dose.

**Relationship:** N101. **Focus area:** D (planned intervention dose). **Proposed review domain:** plan_material. **Proposed relationship:** P_P.

**Compared locations and roles:** PLAN [protocol p15 sectionV.e.1](../../../joi190122supp1_prod.pdf#page=15); PLAN [protocol p21 sectionVII.a first dose statement and upper-intake paired-unit statement](../../../joi190122supp1_prod.pdf#page=21).

**Printed inputs:** Eachactivepill 2000 IU(40µg) onp 15; interventiondose 2000 IU(40µg) repeatedp 21;p21 upper intakelevel 50µg or2000 IU. No external conversion is used: the supplied paired-unit upper-limit statement supplies comparator 50µg for 2000 IU.

**Rule and calculation:** Equivalent doses of the same substance using the same unit conversion should give the same microgram quantity. Treat 2000 IU±.5 and comparator 2000 IU±.5 with 50µg±.5: impliedmicrogramdose interval[1999.5×49.5/2000.5,2000.5×50.5/1999.5]=[49.47526,50.52526]. Printed 40µg±.5 gives[39.5,40.5]; gap 8.97526/40=.22438>.05. Direct 40 vs50 copies also give gap 9/50=.18. The IU reading is consistent, while microgramreading changes magnitude.

**Qualifying route:** Route A, category 2 (substituted digit in a printed intervention-dose quantity changes magnitude).

**Affected result or extracted value:** Planned vitamin-D intervention dose expressed in micrograms, a unit a reader could extract when describing or comparing the randomized intervention.

**Why context does not resolve it:** Route A category 2 applies to the printed numeric dose. The repeated 2000 IU reading suggests an intended dose in one unit, but does not reconcile the two distinct printed microgram quantities; the numeric reading is not merely a missing unit symbol.

**Alternatives:** The study-pill microgram equivalent or the upper-limit paired-unit statement could be the differing transcription. The source also calls the selected dose lower than the stated 2000 IU upper limit despite both printing 2000 IU; that safety wording is not separately registered. No preferred dose or external conversion is proposed.

**Human question:** Which microgram equivalent accompanies the prespecified 2000 IU cholecalciferol dose, and which supplied paired-unit statement explains the 40µg versus 50µg discrepancy?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp1/4 minority 31%; Table 1 p5 race counts | Explicit race denominators 361+327+284+314=1286; all 20 directly printed minority-count inputs sum 429. Allow each minority count±.5 and each denominator±.5: recomputed proportion[100×419/1288,100×439/1284]=[32.53106,34.19003]%. Printed 31% interval[30.5,31.5]; gap 1.03106/31=.03326≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p2 enrollment 1320 versus actual 1312 | Goal differs from achieved cohort; even literal two-copy gap 7/1320=.00530≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main Table 1 p5 versus supplementary baseline medication copies | Baseline descriptive values and nonmissing denominators are matched; differences caused by treating randomized N as the response N are not reproduced; no such denominator is stated. | NOT_REPRODUCED |
| REPORT main Table 2 and supp eTables 4–9 | Crude subtraction of time-specific means, or crude ratios of printed cross-sectional geometric means, differs from adjusted/MI longitudinal change; footnotes distinguish these quantities. | MODEL_VERSUS_CRUDE |
| REPORT supplement eFigure 2 p18 versus eTable 6 p11 | Overall P.89 versus.90: intervals[.885,.895]and[.895,.905]touch; gap 0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement eFigures 2/3 pp18/19 captions | Captions say difference while plot/table label ratio; null 1/logticks and geometric change values identify multiplicative quantity immediately. No evidence of additive computation. | TERMINOLOGY_OR_WORDING |

## Limitations and completion

The tables do not print every arm-specific respondent denominator, person-time total, raw repeated observation, or preliminary simulation variance. Those gaps do not create standalone findings. F-NUM-004 names its common-response interpretation and denominator alternative for independent inclusion screening. Graphical forest endpoints are not reconstructed as exact printed confidence limits. Both eFigure direction arrows were communicated to the statistical lane for source-grounded direction review. All assigned numeric relationships received completed checks; zero unreviewed units.
