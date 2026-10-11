# Complete numeric consistency review

Fresh mandatory numeric checker /root/numeric_review; gpt-6.1-sol/medium, provider inherited unchanged. Scope: all N001–N135, extended N136–N140, and numeric cells inside every S001–S137 group. The complete checked inventory is [numeric_relationship_inventory.md](../relationships/numeric_relationship_inventory.md) with four disjoint bounded parts. No old candidate/report conclusions or external sources used. No severity, validity, stable C IDs or dispositions assigned. Every observation requires human adjudication.

## Direct-source authority and tools

All fresh text derivatives use direct Poppler pdftotext 26.01.0 with layout preservation; all fresh PNG derivatives use direct Poppler pdftoppm 26.01.0. No OCR or fallback engine was used. Each derivative's source and exact page range are identified below and in its filename.

Direct Poppler pdftotext -layout derivatives written under preprocessing/numeric: main-p1.txt,main-p4.txt,main-p5-p8.txt; results-p3-p9.txt; plan-p7.txt,plan-p11.txt,plan-p15.txt,plan-p17.txt,plan-p27.txt,plan-p30-p31.txt,plan-p32.txt. Exact physical page scopes are in filenames; source links below point to supplied PDFs. Direct pdftoppm -singlefile -png -scale-to1800 derivatives results-p4.png,main-p8.png,results-p9.png were visually inspected. Reused source-matched worksheet render preprocessing/support_mapping/protocol-p42.png visually inspected for its threshold. All tools available per tooling_record.md; fallback NOT_NEEDED. Sources/reused derivatives preserved; fresh derivatives are locator/transcription assets, not substitutes for exact sources.

Every mapped group explicitly checked. Whole-number percentages allow0.5percentage-point rounding tolerance; one-decimal differences allow0.05pp. Exact patient counts allow0 count discrepancy. Inputs already rounded as means/SD use their full half-last-unit intervals before pooling. Continuous medians and IQRs are not assumed means or pooled as weighted means. Censoring is permitted in time-at-risk rows; risk depletion is not event count.

## Distinct local observations

### B01 — Main difficult-weaning percentage

**Relationship IDs:** N037.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [main PDF p5](../../../jama_thille_2019_oi_190108.pdf#page=5), REPORT; Table1, HFalone difficult weaning; n302, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 92/302 with 31%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=30.463576%; nearest whole percent30%. The printed percentage differs by0.536424pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** Categories203+92+7=302. Percentages67+31+2=100, while independently rounded cells would67+30+2=99. Sum-preserving integer allocation could explain the displayed31; no rounding rule is printed.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Were these percentages independently rounded or deliberately adjusted to total100%, and which convention should a reader use for92/302?

### B02 — Main day90 mortality percentage

**Relationship IDs:** S012.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [main PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT; Table2, HFalone mortality atday90; n302, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 65/302 with 21%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=21.523179%; nearest whole percent22%. The printed percentage differs by0.523179pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** Time-to-death analysis can use different summaries, but row is No.(%) with n302 and exact counts. Truncation would21; adjacent patient-meeting-criteria row with the same65/302 prints22.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Is21% a deliberate survival-based/truncated summary, or should the count65 and n302 be presented with their ordinary rounded percentage?

### B03 — Nonhypercapnic difficult-weaning percentage

**Relationship IDs:** S085.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p3](../../../joi190108supp2_prod.pdf#page=3), REPORT; eTable2, nonhypercapnic HFalone difficult weaning; n254, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 70/254 with 27%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=27.559055%; nearest whole percent28%. The printed percentage differs by0.559055pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** 177+70+7=254. Printed70+27+3=100%; ordinary independent rounding70+28+3=101%. Sum-preserving adjustment could explain27; convention absent.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Is27% a category-balancing adjustment, or does70/254 require a different printed percentage or denominator?

### B04 — Nonhypercapnic prolonged-weaning percentage

**Relationship IDs:** S085.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p3](../../../joi190108supp2_prod.pdf#page=3), REPORT; eTable2, nonhypercapnic NIV prolonged weaning; n276, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 12/276 with 5%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=4.347826%; nearest whole percent4%. The printed percentage differs by0.652174pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** 194+70+12=276. Printed70+25+5=100%; independently rounded70+25+4=99%. Intentional balancing could explain5, although standard largest-remainder allocation would change difficult25 to26.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Was5% deliberately allocated to make categories total100%, or is its numerator/denominator/percentage misaligned?

### B05 — Hypercapnic HF ineffective-cough percentage

**Relationship IDs:** S109/N123.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p4](../../../joi190108supp2_prod.pdf#page=4), REPORT; eTable2, hypercapnic HFalone ineffective cough No./totalNo.(%), printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 14/45 with 69%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=31.111111%; nearest whole percent31%. The printed percentage differs by37.888889pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** (45−14)/45×100=68.888889% rounds69%, the complement. Nonhypercapnic entries and pooled main65/284(23) follow the numerator percentage convention.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Does69% refer to effective rather than ineffective cough, or which printed numerator/denominator/percentage should describe ineffective cough?

### B06 — Hypercapnic NIV ineffective-cough percentage

**Relationship IDs:** S109/N123.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p4](../../../joi190108supp2_prod.pdf#page=4), REPORT; eTable2, hypercapnic NIV ineffective cough No./totalNo.(%), printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 16/59 with 73%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=27.118644%; nearest whole percent27%. The printed percentage differs by45.881356pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** (59−16)/59×100=72.881356% rounds73%, the complement. Main86/322(27) uses pooled16+70 over59+263.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Does73% describe the complementary cough category, or which cell component is intended for ineffective cough?

### B07 — Hypercapnic HF abundant-secretion percentage

**Relationship IDs:** S110/N123.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p4](../../../joi190108supp2_prod.pdf#page=4), REPORT; eTable2, hypercapnic HFalone abundant secretions No./totalNo.(%), printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 20/46 with 57%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=43.478261%; nearest whole percent43%. The printed percentage differs by13.521739pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** (46−20)/46×100=56.521739% rounds57%, the complement; main121/288(42) follows20+101 over46+242.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Does57% describe patients without abundant secretions, or which cell component is intended for abundant secretions?

### B08 — Hypercapnic NIV abundant-secretion percentage

**Relationship IDs:** S110/N123.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p4](../../../joi190108supp2_prod.pdf#page=4), REPORT; eTable2, hypercapnic NIV abundant secretions No./totalNo.(%), printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 23/61 with 62%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=37.704918%; nearest whole percent38%. The printed percentage differs by24.295082pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** (61−23)/61×100=62.295082% rounds62%, the complement; main114/326(35) uses23+91 over61+265.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Does62% describe patients without abundant secretions, or which cell component is intended for abundant secretions?

### B09 — Hypercapnic NIV ICU-reintubation percentage

**Relationship IDs:** S115.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p6](../../../joi190108supp2_prod.pdf#page=6), REPORT; eTable3, NIV reintubation upuntilICUdischarge; n63, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 6/63 with 9%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=9.523810%; nearest whole percent10%. The printed percentage differs by0.523810pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** Truncating instead of rounding yields9%, but other rows use ordinary rounding. Difference−11.3 reconciles10/48 versus6/63 and therefore supports the displayed counts.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Was9% obtained by truncation or a different denominator, and which quantity should describe6/63 reintubations?

### B10 — Hypercapnic NIV mortality-or-reintubation percentage

**Relationship IDs:** S120.
**Primary candidate category:** Denominator, proportion, or total inconsistency.
**Compared locations and document roles:** [results supplement p6](../../../joi190108supp2_prod.pdf#page=6), REPORT; eTable3, NIV mortality orreintubation inICU; n63, printed numerator/denominator or group header and percentage at the same location, REPORT.
**Printed inputs:** 6/63 with 9%.
**Reproducible rule and calculation:** Percentage=100×numerator/denominator=9.523810%; nearest whole percent10%. The printed percentage differs by0.523810pp, beyond0.5pp tolerance.
**Direct observation versus inference:** The printed count, denominator and percentage are direct observations. The division and ordinary independent-rounding comparison are derived diagnostics; the unknown production convention is not inferred.
**Alternatives and missing definitions:** Truncation yields9%; difference−13.4 agrees with6/63−11/48. This is a distinct composite result row fromB09.
**Quality-control relevance:** Numerator and displayed proportion can give different extracted categorical results; the possible downstream consequence is bounded data-extraction ambiguity, not a paper-conclusion claim.
**Exact human question:** Was9% obtained by truncation or a different denominator, and which quantity should describe6/63 composite events?

### B11 — Nonhypercapnic day90 mortality absolute difference

**Relationship IDs:** S136.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [results supplement p7](../../../joi190108supp2_prod.pdf#page=7), REPORT, eTable4 mortality atday90 HF/NIV count cells, group headers and absolute-difference cell.
**Printed inputs:** HF54(21),n254;NIV50(18),n276; difference−3.8(95%CI−9.9to3.6).
**Rule/calculation/tolerance:** NIVminusHF=100×(50/276−54/254)=−3.143900pp, nearest tenth−3.1; displayed−3.8 differs0.656100pp >0.05.
**Direct observation versus inference:** Counts,headers,−3.8 are direct; arithmetic diagnostic assumes the same unadjusted risk difference used throughout the table.
**Alternatives/missing definitions:** An adjusted or other estimand could differ, but no different adjustment is specified for this row. CI midpoint−3.15 is compatible with the count-based difference; it is supporting arithmetic, not proof of the CI method.
**Quality-control relevance:** This effect value can be extracted independently from the event counts.
**Exact human question:** Is−3.8 a transcription value, or what separately defined estimand/population produces it from the displayed mortality counts?

### B12 — Nonhypercapnic mortality among reintubated difference

**Relationship IDs:** S134.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [results supplement p7](../../../joi190108supp2_prod.pdf#page=7), REPORT, eTable4 mortality inICU ofreintubated patients, explicit conditional denominators and difference cell.
**Printed inputs:** HF17/49(35),NIV9/35(26); difference−8.9(95%CI−27.1to11.2).
**Rule/calculation/tolerance:** 100×(9/35−17/49)=−8.979592pp, nearest tenth−9.0; printed−8.9 differs0.079592pp >0.05.
**Direct observation versus inference:** Inputs direct; ordinary one-step unadjusted difference is diagnostic.
**Alternatives/missing definitions:** A truncated magnitude gives−8.9, or a separately estimated contrast could do so. Integer group percentages alone give−9, and independently rounded one-decimal group percentages25.7−34.7 also give−9.0; the package does not state a truncation/alternative-estimator convention for this row.
**Quality-control relevance:** Small precision differences can propagate when the contrast is copied instead of computed.
**Exact human question:** Is−8.9 intentionally truncated or separately estimated, or should the reported contrast reconcile under the same calculation as the displayed17/49 and9/35?

### B13 — Main ICU death-or-reintubation difference at a rounding boundary

**Relationship IDs:** S014.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [main PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT, Table2 mortality orreintubation inICU, count cells/headers and difference cell.
**Printed inputs:** HF64/302(21),NIV51/339(15); difference−6.2(95%CI−12.2to−0.2).
**Rule/calculation/tolerance:** One-step unadjusted difference100×(51/339−64/302)=−6.147805pp, nearest tenth−6.1. Printed−6.2 differs0.052195pp, just0.002195pp outside0.05 tolerance.
**Direct observation versus inference:** Printed inputs direct; diagnostic assumes a one-step difference from exact count ratios.
**Alternatives/missing definitions:** Two-stage rounding reconciles the value:64/302→21.2%,51/339→15.0%, then15.0−21.2=−6.2. This alternative is explicitly reproducible and could explain the observation; the package does not specify one-step versus two-stage rounding.
**Quality-control relevance:** Conditional precision-convention ambiguity in extracted risk differences; no asserted substantive effect change.
**Exact human question:** Was this contrast intentionally formed from rounded component percentages, or should contrasts follow a single rounding step from the exact counts?

### B14 — Respiratory-failure difference differs across main locations

**Relationship IDs:** S003.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [main PDF p1](../../../jama_thille_2019_oi_190108.pdf#page=1), REPORT, abstract respiratory-failure outcome; [main PDF p6](../../../jama_thille_2019_oi_190108.pdf#page=6), REPORT, secondary-outcome respiratory-failure narrative; [main PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT, Table2 respiratory-failure row and headers.
**Printed inputs:** Abstract/narrative−8.7%;Table2−8.5%; sameCI−15.2to−1.8 andP=.01;HF88/302,NIV70/339.
**Rule/calculation/tolerance:** Matched outcome/arms/timepoints should reconcile at0.1pp precision. Direct difference0.2pp exceeds combined0.1pp rounding allowance. Count-derived100×(70/339−88/302)=−8.490105pp rounds−8.5.
**Direct observation versus inference:** The two printed differences are directly different. Count arithmetic supports one side, without presuming the original production mechanism.
**Alternatives/missing definitions:** Different models or measured denominators might yield another value, but these locations refer to the same7day respiratory-failure comparison and give identical inferential tuple; no differing estimand is identified.
**Quality-control relevance:** Extracting from abstract versusTable2 yields different effect values.
**Exact human question:** Which difference/estimand is intended at all three matching locations, and is−8.7 from an undisclosed calculation or a transcription?

### B15 — ICU stay contrast under a percent-unit header

**Relationship IDs:** S007.
**Primary candidate category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** [main PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT, Table2 shared header “Absolute Difference, % (95% CI)” versus ICU length-of-stay row labelled median(IQR),days.
**Printed inputs:** HF11(7to19)days,NIV12(7to19)days; difference0.5(−1.6to2.6) under%header.
**Rule/calculation/tolerance:** A difference on an untransformed day scale has unit days; a percent contrast requires a specified normalizing/transform rule. Unit mismatch is categorical, no numeric rounding tolerance.
**Direct observation versus inference:** Header and day-labelled rows direct; identifying the intended contrast unit/estimand requires clarification. No claim that0.5 must equal12−11.
**Alternatives/missing definitions:** Shared%header may have been intended only for binary outcomes, with0.5 measured in days; a percent effect or another estimator is possible but not defined.
**Quality-control relevance:** A reviewer can extract0.5 as percent rather than days.
**Exact human question:** What unit and estimator apply to the ICU stay contrast, and should the table header distinguish its day-scale result from binary percentage-point differences?

### B16 — Hospital stay contrast under a percent-unit header

**Relationship IDs:** S008.
**Primary candidate category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** [main PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT, Table2 shared%contrast header and hospital length-of-stay row labelled days.
**Printed inputs:** HF23(15to39)days,NIV25(15to42)days; difference2.3(−1.4to6.1) under “Absolute Difference, % (95% CI)”.
**Rule/calculation/tolerance:** Same dimension rule asB15, applied to a distinct result row; percent versus days is not a rounding discrepancy.
**Direct observation versus inference:** Printed header/row direct; unit interpretation conditional on unspecified estimator. Rounded medians allow contrasts from1to3days, so2.3 is not separately labelled an arithmetic inconsistency.
**Alternatives/missing definitions:** Generic header may unintentionally apply%to a days result; separately normalized percent contrast would need definition.
**Quality-control relevance:** Unit ambiguity in the hospital-stay effect extracted for secondary evidence products.
**Exact human question:** Is2.3 a day-scale or percent contrast, and which estimator/unit should be stated for this hospital-stay result?

### B17 — HF patient-per-center IQR does not match complete center counts

**Relationship IDs:** N059,N125–N134,N138.
**Primary candidate category:** Cross-document numeric inconsistency.
**Compared locations and document roles:** [main PDF p6](../../../jama_thille_2019_oi_190108.pdf#page=6), REPORT, Table1 participating centers, patients percenter median(IQR); [results supplement p8](../../../joi190108supp2_prod.pdf#page=8), REPORT, all30 HF patient denominators in eTable5.
**Printed inputs:** Main10(9–25),30participating centers; eTable5 HF denominators sorted1,2,2,2,3,4,5,5,6,7,7,8,10,10,10,10,11,11,12,12,12,13,14,14,15,16,17,19,19,25;sum302.
**Rule/calculation/tolerance:** Median10 agrees. Linear sampleQ1=5.25,Q3=13.75; median-of-halvesQ1=5,Q3=14. Whole-count display tolerance0.5patient and ordinary sample-quantile choice cannot turn the75th percentile near14 into the unique maximum25 orQ1near5into9.
**Direct observation versus inference:**30denominators and main9–25 direct; sorted distribution/quartiles derived. An exact unsupplied quantile algorithm is not inferred.
**Alternatives/missing definitions:** Main may use a different patient set or another dispersion statistic. Entire eTable5 population302 matches main;25 is maximum, while9 is neither minimum nor ordinary lower quartile, so merely relabelling as full range does not reconcile both bounds.
**Quality-control relevance:** Center-distribution characteristics can be copied as study descriptors.
**Exact human question:** Which30center population and dispersion/quantile convention generate9–25, or which patient-per-center summary is intended?

### B18 — NIV patient-per-center IQR does not match complete center counts

**Relationship IDs:** N059,N125–N134,N138.
**Primary candidate category:** Cross-document numeric inconsistency.
**Compared locations and document roles:** [main PDF p6](../../../jama_thille_2019_oi_190108.pdf#page=6), REPORT, Table1 NIV patients percenter median(IQR); [results supplement p8](../../../joi190108supp2_prod.pdf#page=8), REPORT, all30 NIV patient denominators.
**Printed inputs:** Main13(9–23),30centers;sorted2,2,3,4,5,5,6,7,7,7,9,9,11,12,12,13,13,13,13,13,13,14,16,16,17,17,17,19,21,23;sum339.
**Rule/calculation/tolerance:** Median12.5 supports printed13. LinearQ1=7,Q3=15.5;median-of-halves7–16. Whole-count tolerance0.5 and ordinary quantile choice cannot reconcile printed9–23;23 is sole maximum.
**Direct observation versus inference:** Counts/mainIQR direct; quantiles derived; no preferred quantile algorithm imposed.
**Alternatives/missing definitions:** Different population/statistic might differ, but eTable5 and main population339 coincide. A range explanation would require lower2, not9.
**Quality-control relevance:** Distinct NIV study-description result can be extracted inconsistently.
**Exact human question:** Which center population and IQR definition yield9–23, or is a different dispersion statistic intended?

### B19 — Conditional pooled NIV pre-SBT PaCO2 SD

**Relationship IDs:** N046,S096,N136,N137.
**Primary candidate category:** Cross-document numeric inconsistency.
**Compared locations and document roles:** [main PDF p5](../../../jama_thille_2019_oi_190108.pdf#page=5), REPORT, Table1 ventilator settings beforeSBT PaCO2 mean(SD) and NIV group header; [results supplement p4](../../../joi190108supp2_prod.pdf#page=4), REPORT, eTable2 beforeSBT PaCO2 mean(SD) in both NIV strata and group headers.
**Printed inputs:** Main40(8)mmHg,n339; nonhypercapnic37(8),n276;hypercapnic51(8),n63.
**Rule/calculation/tolerance:** If all measurements form the same n276+n63=n339 partition, sample pooledSD=sqrt([(275×8²)+(62×8²)+(276×63/339)×14²]/338)=9.672330mmHg. Permit mean andSD±0.5in each subgroup;minimum gap13 andSD7.5 give minimum pooledSD9.040442, larger than maximum8.5allowed for mainSD8. Population-SD rather than sample-SD convention changes only negligible terms and does not close the gap. Pooledmean39.601770 is compatible40.
**Direct observation versus inference:** All cells/labels/group totals direct; incompatible variance identity is conditional inference on matched measured n/population.
**Alternatives/missing definitions:** Variable-specific blood-gas measured n may differ from group headers; groups may summarize a different available-data subset despite matching beforeSBT label. Main explicitly reports endSBT measured n221/241 but no beforeSBT row n; do not impute those endSBT n into this calculation.
**Quality-control relevance:** Rounded SDs used in continuous-outcome extraction can be inconsistent under a same-population partition.
**Exact human question:** What actual measured n and patient subsets underlie each beforeSBT PaCO2 cell, and, if the subsets match the displayed339 partition, which SD/stratum input should reconcile?

### B20 — PLAN study-duration components sum48 rather than51months

**Relationship IDs:** N087,N113.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [protocol p32](../../../joi190108supp1_prod.pdf#page=32), PLAN, section5.6 total study duration; [protocol p11](../../../joi190108supp1_prod.pdf#page=11), PLAN, synopsis total/duration components.
**Printed inputs:** p32total51months “with36months for the study and12months for analysis”; patientparticipation3months,recruitment36months. p11total51 with39months study and12analysis.
**Rule/calculation/tolerance:**36+12=48,3months short of51;integer month-component sum tolerance0. p11provides39+12=51.
**Direct observation versus inference:** Printed totals/components direct; sum mismatch direct arithmetic. Followup accounting as the missing3months is an explanatory possibility, not assigned as final correction.
**Alternatives/missing definitions:**36could refer only to recruitment, with3additional followupmonths included in51but omitted from the decomposition; synopsis39supports that explanation.
**Quality-control relevance:** Internal plan timeline can be copied with conflicting component durations; does not establish actual recruitment failure.
**Exact human question:** Does the p32component36mean recruitment only, with additional3monthsfollowup, or which decomposition of51months is intended?

### B21 — REPORT versusPLAN reintubation acidosis threshold

**Relationship IDs:** N011,N108.
**Primary candidate category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** [main PDF p4](../../../jama_thille_2019_oi_190108.pdf#page=4), REPORT, severe respiratory failure leadingtoreintubation, respiratory-acidosis criterion; [protocol p31](../../../joi190108supp1_prod.pdf#page=31), PLAN, section5.4reintubation criteria, respiratory-acidosis criterion continuedfromp30.
**Printed inputs:** MainpH<7.25withPaCO2>45mmHg;PLANpH<7.35withPaCO2>45mmHg. Both require at least2severe-failure criteria and use RR>35,FiO2>=80orPF<=100. Ordinary nonsevere ARF pH<7.35 is separately printed in both documents.
**Rule/calculation/tolerance:** Matched numeric decision boundary differs0.10pHunit; threshold definitions are exact, not means allowing rounding intervals. A pH7.30withPaCO2>45satisfies one printed acidosis criterion but not the other; this hypothetical boundary calculation illustrates the direct discrepancy, not a claim about an actual patient.
**Direct observation versus inference:** Different criterion values direct; whether counts65/49or57/39used either criterion cannot be inferred without data.
**Alternatives/missing definitions:** An amended criterion or more stringent reporting definition may explain the difference; the supplied protocol retains7.35and the report7.25.
**Quality-control relevance:** This definition underlies reported criterion-positive patient counts and their interpretation; no claim of protocol violation.
**Exact human question:** Which pH threshold actually generated the reported reintubation-criteria counts, and was the7.25versus7.35change documented?

### B22 — PLAN historical Su sample total400versus406

**Relationship IDs:** N091,S032,S037.
**Primary candidate category:** Numeric or arithmetic inconsistency.
**Compared locations and document roles:** [protocol p15](../../../joi190108supp1_prod.pdf#page=15), PLAN, historical trial background paragraph “included400patients”; [protocol p17](../../../joi190108supp1_prod.pdf#page=17), PLAN, Table1Su2012armheaders.
**Printed inputs:** Narrative400;TableNIVn202andoxygenn204.
**Rule/calculation/tolerance:**202+204=406,6above400; if a reported exact sample count, tolerance0participants.
**Direct observation versus inference:** Values direct; sum exact. Intentional broad rounding not declared in the count sentence.
**Alternatives/missing definitions:**400may be a two-significant-figure narrative approximation or a different included/randomized population; package does not supply that distinction. “around10%” elsewhere explicitly signals approximation for reintubation, but not for the count sentence.
**Quality-control relevance:** Distinct historical source sample size may be copied from the plan background into summaries.
**Exact human question:** Is400an intentional rounded sample description or another population, and how does it relate to the table’s406patients?

### B23 — PLAN oxygenation readiness boundaries differ across text and worksheet

**Relationship IDs:** N102,N120.
**Primary candidate category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** [protocol p27](../../../joi190108supp1_prod.pdf#page=27), PLAN, weaning-procedure readiness paragraph and appendix-reference sentence; [protocol p42](../../../joi190108supp1_prod.pdf#page=42), PLAN, appendix2worksheet first-stage ventilation readiness line.
**Printed inputs:** p27SpO2>90%onFiO2<=40%orPF>=150withPEEPupto8; p42SpO2>=92%withFiO2<=40%andPEEP<=8. p27states annex protocol proposed when center lacks a weaning protocol.
**Rule/calculation/tolerance:** Same readiness oxygenation dimension uses different exact boundaries; a value91%onFiO2=40%,PEEP8satisfies the text SpO2condition but not the worksheet condition. Exact cutoff comparison has no rounding tolerance; other conditions held equal only for illustration.
**Direct observation versus inference:** Differing thresholds directly observed; no actual patient eligibility/count is imputed from the illustrative91%.
**Alternatives/missing definitions:** Worksheet may deliberately impose a stricter local operational implementation rather than reproduce the general consensus criterion, and different center protocols are expressly possible. The supplied numeric criteria nevertheless differ; applicability needs human clarification.
**Quality-control relevance:** Numeric readiness-definition extraction from the two PLANlocations differs; no broad study-design or actual patient-count conclusion.
**Exact human question:** Is>=92%a deliberately stricter annex implementation than>90%, and which supplied readiness boundary was intended to be applied to the study population?

### B24 — Survival time-axis origin disagrees with title

**Relationship IDs:** N135,S137.
**Primary candidate category:** Measure, label, or scale inconsistency.
**Compared locations and document roles:** [results supplement p9](../../../joi190108supp2_prod.pdf#page=9), REPORT, eFigure title and x-axis label; [results supplement p1](../../../joi190108supp2_prod.pdf#page=1), REPORT, contents repeats figure titlefromextubation (corroboration).
**Printed inputs:** Title “Cumulative Probability of Survival From Extubation to Day90”;x-axis “Days Since Intubation”;ticks0,15,30,45,60,75,90,initialrisk302/339.
**Rule/calculation/tolerance:** A single plotted time scale cannot simultaneously identify its origin as intubation and extubation unless an origin translation is supplied. Categorical origin mismatch has no rounding tolerance.
**Direct observation versus inference:** Title and axis directly visually read from exactsourcep9; no curve-derived exact effect estimated.
**Alternatives/missing definitions:** Axis label may be stale or title may describe an intended endpoint; a distinct variable timeorigin could exist but is not defined.
**Quality-control relevance:** Figure can be interpreted/extracted on a different clinical time horizon.
**Exact human question:** Does the plotted survival curve start at intubation or extubation, and which title/axis/underlying time variable should agree?

## Completion and bounded noncandidate checks

Complete277groups:140Nplus137S numeric components, across all assigned mapped source units.24distinct local observationsB01–B24 emitted without a count target; potential overlap with statistical/cross-source lanes intentionally preserved for coordinator comparison. Scientific source coverage gaps None.

All subgroup counts, population partitions and measured cough/secretion denominator sums reconcile; all30center row arithmetic and percentages reconcile; all16figure stratum risk sums reconcile; all main/stratum pooled mean ranges and35of36SDrounding ranges overlap. The lone disjoint SD is explicitly conditionalB19. Plan590inflated10%→650is compatible conservative rounding; historical estimates/ranges are not exact actual-trial outcomes. Observed rescueNIV20hmean does not demonstrate persistence ofARFbeyondthePLAN2hconditionalintubation rule. Reintubation risk decrements are not automatically events. Day90eFigureP=.37versusTable2P=.30is referred to statistical/cross-source methods checking rather than a pure arithmetic observation. Repeated rounded physiological means and complementary ventilator percentages do not establish duplicate data. PaO2/dioxide translation ambiguity alone is not emitted as a quantitative candidate.

Limitations: per-variable blood-gas n/subset matching, quantile algorithm, categorical balancing/truncation/contrast rounding convention and some contrast estimands absent from package. They are named in affected observations; none authorizes omission or confident production-mechanism inference.

