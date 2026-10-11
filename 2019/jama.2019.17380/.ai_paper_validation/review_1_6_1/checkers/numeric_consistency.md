# Numeric consistency review

Fresh numeric_consistency_reviewer stage, gpt-6.1-sol / medium. Scope: all 4 direct sources,64 physical PDF pages;77 complete numeric relationship groups N001–N077 in [numeric inventory](../relationships/numeric_relationship_inventory.md). All main Tables 1–3, Figures 1–4, supplement eTables 1–11/eFigures 1–3, protocol sample-size/dose/endpoint formulas and addendum numeric assumptions reviewed. Scientific input: exact supplied sources, source/asset/tooling inventories and both complete current evidence maps. No old selection/report content, web evidence, external literature, or raw data used. Source roles are by content: main/results/data-sharing REPORT; entire original protocol/addendum bundle PLAN.

Arithmetic used exact counts and half-last-digit intervals for displayed measurements, percentages, differences and ratios. Counts are not rounded. Adjusted/imputed estimates and Cox HRs are not replaced by crude calculations. All 77 groups complete. Findings:2 consolidated patterns. Excluded observations:15 consolidated observations. No C IDs or adjudications assigned.

## Direct confirmation and engines

Direct Poppler pdftotext -layout from supplied PDFs confirmed the eTable 7 text and all main figure/table numeric content. Fresh direct pdftoppm renders confirmed main PDF pp.8,9 and supplement PDF pp.12,18,19 visually, including graph column headings that native text may omit. Command pattern: `pdftoppm -f N -l N -singlefile -scale-to 1800 -png SOURCE.pdf .ai_paper_validation/review_1_6_1/preprocessing/numeric-NAME`. Engine direct Poppler 26.01.0, CPU. Outputs: preprocessing/numeric-main-p8.png; preprocessing/numeric-main-p9.png; preprocessing/numeric-supp2-p12.png; preprocessing/numeric-supp2-p18.png; preprocessing/numeric-supp2-p19.png. These are new derivatives, not reused assets, and no supplied/reused file changed. Direct source links below are final evidence authorities.

## Findings

### F-NUM-001

**Title:** Assignment counts and group mean summaries do not align in the primary-outcome subgroup displays, repeated in the ACR displays.

**Relationships:** N002, N017, N021, N024, N026, N027, N068, N076, N077.

**Exact compared locations and roles:** REPORT [main article Figure 1, PDF p.6](../../../jama_de_boer_2019_oi_190122.pdf#page=6), REPORT [main Table 1, PDF p.5](../../../jama_de_boer_2019_oi_190122.pdf#page=5), REPORT [main Table 2 and Figure 3, PDF p.8](../../../jama_de_boer_2019_oi_190122.pdf#page=8), REPORT [main Figure 4, PDF p.9](../../../jama_de_boer_2019_oi_190122.pdf#page=9), REPORT [supplement eTable 6, PDF p.11](../../../joi190122supp2_prod.pdf#page=11), REPORT [supplement eFigure 2, PDF p.18](../../../joi190122supp2_prod.pdf#page=18), REPORT [supplement eFigure 3, PDF p.19](../../../joi190122supp2_prod.pdf#page=19). All figure rows are listed below, including repeated subgroup occurrences.

**Printed inputs, rule and calculation:** Figure 1 assigns 370 to D+O,333 to D+placebo,289 to placebo+O,320 to both placebos. Thus D active=703, D placebo=609, O active=659,O placebo=653. Figure 3, however, prints overall Placebo 703,mean−13.1(SD14.4); Vitamin D609,mean−12.3(SD14.8). Figure 4 prints overall Placebo 659,mean−13.1(SD14.8); Omega 3 653,mean−12.2(SD14.5). Table 2 on the same main PDF p.8 has active D change−12.3 and placebo−13.1, active O−12.2 and placebo−13.1. The means therefore follow their displayed treatment labels while the N values do not follow the source-defined assignment counts. This is more than a group-name variation: taking each displayed N,mean,SD triplet literally pairs primary-outcome summaries with the opposite assignment-size information. Exact integers have no display-precision tolerance.

Table 1 also identifies D active white 240+211=451 and D placebo white 199+207=406;Figure 3 puts 451 under Placebo and 406 underVitamin D. D active black 73+75=148 versus D placebo 59+71=130; Figure 3 again puts 148/130 under Placebo/Vitamin D. D<20 counts 62+48=110 active,41+44=85 placebo;20–<30 is 230 active/203 placebo;≥30 is 332 active/297 placebo;all printed with opposite N headings. Figure 3 other-assignment rows put D+O-placebo 333 under Placebo and both placebos 320 underVitamin D;O active row 370 under Placebo and 289 underVitamin D. Figure 4's other-assignment row has O active,D placebo 289 under Placebo and both placebos 320 under Omega 3;D active row 370 under Placebo and 333 under Omega 3.

Supplement eFigure 2 overall N703 under Placebo and 609 under Active intervention accompany geometric change 3.02 and 2.97, respectively. eTable 6 assigns 3.02 to D placebo and 2.97 to D active. eFigure 3 overall N659 under Placebo and 653 under Active accompany 3.05 and 2.94; eTable 6 assigns 3.05 to O placebo and 2.94 to O active. This repeats the count-to-summary alignment pattern without changing the modeled ratio identity.

**Every affected display row:** Pair order below is literal displayed Placebo N / Active N. The D table applies to both main Figure 3 and supplement eFigure 2; the O table applies to both main Figure 4 and supplement eFigure 3. These are affected locations of one consolidated pattern, not independent findings. No raw-data claim is made about unprinted adjusted subgroup values.

| Vitamin D display row | Printed N pair | Omega-3 display row | Printed N pair |
|---|---|---|---|
| Overall |703/609|Overall|659/653|
| White |451/406|EPA/DHA≤2.2|332/347|
| Black |148/130|EPA/DHA>2.2|308/292|
| ACR<30 |635/559|ACR<30|596/598|
| ACR≥30 |67/50|ACR≥30|62/55|
| D<20 |110/85|hsCRP≤.2|334/335|
| D20–<30 |230/203|hsCRP>.2|323/316|
| D≥30 |332/297|fish<1.5|354/329|
| eGFR≥60 |612/531|fish≥1.5|295/310|
| eGFR<60 |89/76|D placebo|289/320|
| BMI<25 |87/87|D active|370/333|
| BMI25–<30 |228/205|Not applicable|—|
| BMI≥30 |364/294|Not applicable|—|
| O placebo |333/320|Not applicable|—|
| O active |370/289|Not applicable|—|

**Focus area:** A (counts and denominators), with population-to-result attribution relevant to extraction.

**Proposed review domain:** statistical_results. Proposed relationship set S_C,S_W; internal main comparisons alone reproduce the primary-outcome alignment issue, while results supplement repeats it with internally matching mean comparators. No PLAN source is involved.

**Affected result or extracted value:** Group N attached to the five-year primary eGFR mean(SD) change in Figures 3/4, including overall and subgroup triplets; repeated group N attached to the five-year ACR geometric-change(SD) triplets. A data extractor using displayed N alongside group SD obtains a different pairing than the randomized-arm population. This qualifies through primary-outcome analysis-size extraction, rather than merely a peripheral label comparison. The overall adjusted primary difference 0.9 and reported P values are not shown to change by this comparison.

**Why context does not resolve it:** Within each figure the N/mean/SD columns are presented as belonging to one group. Neither caption discloses a different count population or independent ordering of N versus mean/SD. Swapping whole group headings would conflict with Table 2/eTable 6 means; retaining all printed cells would conflict with Figure 1 and Table 1 counts. The supplied text supports an N-column alignment explanation, but does not explicitly state which subgroup counts, dispersions or triplets should be used together. The uncertainty affects extraction of primary-outcome N with SD and extends across repeated rows, not just a missing character. Independent screening should specifically assess whether a field reader nevertheless resolves this pattern at once.

**Alternatives and missing definition:** One interpretation is that the N columns follow active/placebo order while mean columns follow placebo/active order. Another is that N denotes an undisclosed differently assigned population; no figure caption defines such a population. The second interpretation does not naturally reconcile overall counts or the known four-arm stratification. The display alone does not establish a complete alternative cell mapping.

**Exact human question:** Which treatment-group and subgroup participant counts belong with each displayed five-year eGFR mean(SD) change in Figures 3/4, and does the same count-to-summary mapping apply to eFigures 2/3?

### F-NUM-002

**Title:** Complete-case ACR analysis has conflicting population totals within eTable 7.

**Relationship:** N069.

**Exact compared locations and roles:** REPORT [supplement eTable 7 heading, baseline/year 5 N columns and asterisk footnote, physical PDF p.12](../../../joi190122supp2_prod.pdf#page=12). REPORT [main retention text, physical PDF p.4](../../../jama_de_boer_2019_oi_190122.pdf#page=4) and REPORT [supplement eTable 6 year 5 counts, physical PDF p.11](../../../joi190122supp2_prod.pdf#page=11) corroborate urine availability but are not needed to reproduce the internal table discrepancy.

**Printed inputs:** Heading: “Participants With Available Baseline and Year 5 Measurements (N = 944*)”. Both baseline and year 5 rows give D active 504,placebo 440 and O active 477,placebo 467. Asterisk footnote:1312 enrolled;1311 baseline urine samples;991 of these also donated year 5 and “were included in this analysis”;320 baseline but not year 5 excluded;1 missing baseline excluded. Main text has 945 final urine samples; eTable 6 final counts 505+440=945 and 478+467=945.

**Rule and calculation:** The two marginal partitions must each sum to the same total complete-case analysis size. 504+440=944 and 477+467=944 match the heading. In the footnote,1311−320=991, and 1312−320−1=991. Thus the footnote's included count is 47 greater than the heading/table total. If 944 is the final included population,1311−944=367 baseline-sample participants are outside it, rather than 320. Exact counts cannot reconcile through rounding. Even allowing hypothetical half-unit intervals,944 has[943.5,944.5] and 991 has[990.5,991.5], which do not overlap. This interval diagnostic is unnecessary for exact integer N but confirms display precision cannot bridge 47 participants.

**Focus area:** A.

**Proposed review domain:** statistical_results. Relationship S_W (within one results supplement); main availability text is corroboration, not an independent conflicting-source relationship.

**Affected result or extracted value:** Analysis-population size and inclusion/exclusion counts for the baseline/year 5 complete-case ACR sensitivity results: vitamin D ratio 1.03(95%CI.86,1.22),P.77;omega 3 ratio.93(.78,1.11),P.44. Population size 944 versus 991 could be extracted from the same table. No change in reported treatment-effect conclusion is established.

**Why context does not resolve it:** The asterisk directly connects heading N 944 to a footnote explicitly saying 991 were included in this analysis. Immediate context supports 944 through both arm partitions, but also offers a fully self-consistent 991 included/320 excluded account. It does not explain 47 additional exclusions or distinguish returned specimens from available measurements in a way reconciling the explicit analysis inclusion claim. Choosing a population definition or treating footnote counts as a separate subset requires an unstated explanation. This is an analysis-population-size comparison, not merely a per-time-point count difference.

**Alternatives and missing definition:** The footnote may describe returned samples rather than usable measurements, leaving 47 unusable paired samples unreported; alternatively, its 991 and 320 may describe a different participant set. Neither explanation is provided, and the explicit included-in-analysis wording does not name a separate set. The heading/arm totals support 944 as one possible intended N without explaining the competing complete accounting.

**Exact human question:** Does eTable 7's complete-case ACR analysis include 944 or 991 participants, and what eligibility or measurement-availability accounting connects its baseline/year 5 arm counts to its stated included and excluded totals?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main Table 1 p.5; supplement eTables 2/3 pp.7/8 | Baseline medication counts or percentages differ between descriptive displays. They do not change a primary/key secondary result or analysis population. | PERIPHERAL_COMPARISON |
| Main Table 1 p.5 | Whole percentages sometimes sum to 99 or 101. Half-percentage-point intervals and nonmissing denominators reconcile these displays. | ROUNDING_OR_DISPLAY_PRECISION |
| Main Table 1 p.5; main p.4 | The 31% minority narrative depends on treatment of missing race responses; this is a baseline descriptive comparison. | PERIPHERAL_COMPARISON |
| Main Figure 1 p.6; supplement eTable 4 p.9 | 934 final blood measurements versus 932 complete cases reconcile with four missing baseline eGFR values, two also missing final values. | CONTEXT_RESOLVES |
| Main Figure 2 B/D p.7 versus Table 2 p.8 and eTable 6 p.11 | Omega-3 contributor counts repeat vitamin D counts at individual time points. Totals are unchanged; separate primary/ACR population definitions and tables establish the results. | PERIPHERAL_COMPARISON |
| Main Table 2 p.8; supplement eTables 4–9 pp.9–14 | Subtracting observed means or dividing observed geometric means need not reproduce adjusted, imputed changes. Explicit model and imputation notes distinguish the quantities. | MODEL_VERSUS_CRUDE |
| Main Table 2 p.8; supplement eTables 4/5 pp.9/10 | Nominal −12.3−(−13.1)=0.8 versus 0.9, omega-3 year 2 −0.2 versus −0.3, and sensitivity-analysis differences fit combined input rounding intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Main Table 3 p.9; supplement eTable 10 p.15 | Rate differences 0.3 versus nominal 2.7−2.5=0.2, or 0.1 versus 1.7−1.7=0, permit overlapping display intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p.4 and Table 3 p.9 | Composite 164 versus component sum 80+11+80=171 reflects explicitly overlapping participants. | CONTEXT_RESOLVES |
| Main Table 3 p.9; supplement eTable 10 p.15 | Cox hazard ratios need not match crude event-count or incidence-rate ratios. | MODEL_VERSUS_CRUDE |
| Supplement eTable 2 p.7, SGLT2 row | D25(6%)/21(4%) does not follow the common year 5 response-denominator ranges implied by other drug classes. This medication-exposure display is descriptive and changes no endpoint, analysis population or decision rule. | PERIPHERAL_COMPARISON |
| Supplement eTables 5/8 pp.10/13; eTable 1 p.6 | Observed baseline counts 1029/1030 for eGFR and 1031 for ACR are subsets of the adherent population N1032; baseline measurement missingness distinguishes contributor counts. | CONTEXT_RESOLVES |
| Main Figure 3 p.8; supplement eTables/eFigures | A missing closing parenthesis and ratio displays described as difference/change do not obscure quantities identified by column headings, null values and units. | NOTATION_OR_TYPOGRAPHY |
| PLAN pp.15,16,21 | Vitamin D 2000 IU paired with 40 μg versus 50 μg elsewhere, and omega composition 40:30 versus report 465:375, leave the consistently printed IU and total 840 mg doses identifiable. These numeric unit observations do not make endpoint extraction unclear. | CONTEXT_RESOLVES |
| PLAN p.33; main p.3; all rate tables | Full preliminary simulation distributions and exact person-time are not reported. A failed power/rate reproduction would depend on unavailable inputs. | CONDITIONAL_OR_UNREPORTED |

## Limitations

No scientific coverage gap. Exact person-time and unrounded model outputs are not supplied. Graphical adjusted subgroup estimates/CIs have no printed numeric endpoints, so no exact values were invented from pixels. Proposed findings were confirmed in direct source renders. This numeric stage leaves statistical-method and planned/report design findings to the fresh respective specialists while retaining all relevant numeric inputs in N inventory; this is specialization, not omitted source coverage.
