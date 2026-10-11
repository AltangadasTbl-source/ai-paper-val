# Main-report quantitative evidence map

Scope: DOC-001, jama_brenner_2019_oi_190039.pdf, every physical PDF page 1–7. Document role: REPORT throughout. Runtime ID: 01a12865-4595-7121-9aa1-b873e7ae3dd8. Mapping is independent of historical candidate selection. No candidates or judgments are assigned here. Local keys M001–M103 identify 103 mapping records; some records contain multiple explicitly enumerated cell inputs or matching source occurrences. Inferential difference-and-CI records M046–M063 and M064–M081 are individually reconstructible.

Evidence engines/assets: reused Poppler layout text `.ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-N.txt` for N=1,2,3,4,5,6,7; source-linked Poppler full-page render `.ai_paper_validation/document_outputs/doc-799606a72443/ocr_pages/page-5.png` visually inspected for Tables 2 and 3. Historical engine version is unrecorded. Current tooling_record.md authorizes direct Poppler/Tesseract; no fresh extraction, OCR, fallback environment, or Python helper was needed because all 7 units are reusable-backed. Native/layout text is a locator and transcription aid; evidence recheck must inspect the direct PDF for any registered candidate. Layout identifies the same blank Test cell in Table 3 men third row as the page render. No OCR values were silently substituted.

Links are relative from this extraction directory to the direct source. Percentages in tables retain source precision. Differences are aspirin minus placebo; source headings use percent notation, and interpretation as percentage points follows comparison of probabilities. Derived identities below define comparison inputs, not alternate reported analyses. No SE, test statistic, person-time, event incidence rate, odds ratio, risk ratio, or hazard ratio is reported in the main article.

## Complete page coverage

| Physical PDF page | Printed page | Exact inspected content | Reusable units | Fresh-required units | Mapped | Outcome |
|---|---:|---|---:|---:|---:|---|
| 1 | 1686 | Abstract, trial size, characteristics, endpoint results | 1 | 0 | 1 | COMPLETE |
| 2 | 1687 | Introduction, Key Points, eligibility, interventions, sampling, randomization | 1 | 0 | 1 | COMPLETE |
| 3 | 1688 | Randomization, laboratory methods, outcomes, power, statistical methods, results | 1 | 0 | 1 | COMPLETE |
| 4 | 1689 | Results, full Figure, full Table 1, adverse events | 1 | 0 | 1 | COMPLETE |
| 5 | 1690 | Full Tables 2 and 3 including footnotes; sensitivity analysis; discussion | 1 | 0 | 1 | COMPLETE |
| 6 | 1691 | Discussion, limitations, conclusion, article information | 1 | 0 | 1 | COMPLETE |
| 7 | 1692 | Funding, acknowledgments, data sharing, all 32 references | 1 | 0 | 1 | COMPLETE; no new trial result, contextual title quantities mapped |

Total 7; reusable 7; fresh-required 0; mapped 7; scientific-coverage gaps None. Article administrative dates, addresses, volume/issue/pages, reference indices and DOI digits are bibliographic locators rather than quantitative outcomes. References were inspected in full; contextual quantities in reference titles are mapped below without importing their external results.

## Design, definitions, abstract and narrative

| Key | Exact source location | Values and compatible definitions |
|---|---|---|
| M001 | [p1 abstract Design/Interventions](../../../jama_brenner_2019_oi_190039.pdf#page=1); p2 Trial Design | 2422 randomized men/women, age 40–80 years; 1208 aspirin, 1214 placebo; 14 gastroenterology practices plus 4 hospitals = 18 German sites; enrollment June 2013–November 2016; final follow-up January 27, 2017. Single 300-mg oral aspirin tablet versus placebo, 2 days before sampling. |
| M002 | [p1 abstract Results](../../../jama_brenner_2019_oi_190039.pdf#page=1) | Printed population introduction: “Among 2422 randomized patients (mean [SD] age, 59.6 [7.9] years; 1219, 50%, men), 2134 were included in the analysis (78% for primary screening colonoscopy, 22% for diagnostic colonoscopy).” Preserve the grammatical attachment and exact 1219 rather than replacing it with a derived total. |
| M003 | p1 abstract Results; [p3 Results](../../../jama_brenner_2019_oi_190039.pdf#page=3) | Advanced neoplasms 224 (10.5%) among analysis participants; CRC 8 (0.4%); advanced adenoma 216 (10.1%). Main Results repeats all quantities. |
| M004 | p1 primary result; [p2 Key Points](../../../jama_brenner_2019_oi_190039.pdf#page=2); pp3–4 Primary End Point; p5 Table 2 all/Q10.2 | Sensitivity at cutoff 10.2 μg Hb/g stool: aspirin 40.2%, placebo 30.4%; difference 9.8%, 95% CI −3.1% to 22.2%, P=.14. Key Points repeats group percentages and says no statistically significant difference. Matching counts and separately keyed CI relationship M046. |
| M005 | p1 primary result; p2 Key Points; [p4 Primary End Point continuation](../../../jama_brenner_2019_oi_190039.pdf#page=4); p5 Table 2 all/Q17 | Sensitivity at cutoff 17 μg Hb/g stool: aspirin 28.6%, placebo 22.5%; difference 6.0%, 95% CI −5.7% to 17.5%, P=.32. Key Points repeats group percentages and says no statistically significant difference. Matching counts and CI relationship M048. |
| M006 | [p2 Introduction](../../../jama_brenner_2019_oi_190039.pdf#page=2) | Background CRC deaths approximately 860000 annually globally. FIT CRC detection sensitivity 70%–80% at specificity >90%; advanced adenomas described as minority detected. These are contextual REPORT claims without supplied underlying counts here. |
| M007 | p2 Trial Design | Advanced neoplasm means CRC or advanced adenoma: size ≥1 cm, tubulovillous/villous components, or high-grade dysplasia. Target adults 40–80, no recent aspirin/other antithrombotic drugs; previous CRC, overt/FOBT-detected rectal bleeding or recent aspirin/NSAIDs excluded, details referred to results supplement eTable 1. Diagnostic colonoscopy included, including before recommended screening age; colonoscopy planned before recruitment. |
| M008 | p2 Trial Design | Four stool collection kits for each of 2 FITs. Quantitative FOB Gold Tube Screen; qualitative FD Hb/Hp Complex quick. Baseline plus samples scheduled day 2,3,4 after medication: 1 per scheduled day, 4 samples overall. Postponement allowed to subsequent days; before bowel preparation; colonoscopy within 3 months of recruitment. |
| M009 | [p3 Randomization](../../../jama_brenner_2019_oi_190039.pdf#page=3) | Blocks of 20 tablets, 10 assigned to each group; single 300-mg uncoated aspirin versus placebo. RITA randomization software version 1.24 (p2); blinding of physicians/participants and repackaging. |
| M010 | p3 Data Processing/Laboratory Methods | Two independent blinded reviewers of colonoscopy/histology. Samples stored 2–8°C. Sampling-to-arrival median 4 days, IQR 3–5 days. Quantitative analytic range 0.03–142 μg Hb/g feces, Abbott Architect c8000; blinded laboratory analysis. |
| M011 | p3 Outcomes | Primary sensitivity quantitative FIT at two predefined cutoffs 17 μg Hb/g feces (manufacturer) and 10.2 (qualitative FIT cutoff). Intention-to-screen uses samples scheduled day 2; prespecified per-protocol uses samples collected exactly day 2. Advanced-neoplasm binary reference standard as M007. Secondary: specificity, PPV, NPV; combinations of samples scheduled any day 2–4; qualitative FIT; sex-specific results; serious adverse events. Likelihood ratios/AUC designated secondary but not reported in article. |
| M012 | p3 Sample Size/Power | Assumed advanced-neoplasm prevalence 10%; 90% power, 2-sided α=.05, difference in day-2 sensitivity 24 percentage points (60% vs 36%). No explicit required total sample-size number printed in this paragraph. |
| M013 | p3 Statistical Analyses | Analyzed according to randomization group. Consent withdrawal or absence of any samples/information excluded as dropouts; no precolonoscopy stool excluded from primary analysis. R 3.4.0. Wald-adjusted sensitivity/specificity CIs: Agresti–Coull; difference CIs: Agresti–Caffo; PropCIs package. Interaction P from binomial generalized linear model. Significance: 2-sided P<.05, no multiplicity adjustment; secondary analyses exploratory. Article does not specify a primary difference P-test formula separately or provide SE/test statistics. |
| M014 | p3 Sensitivity Analysis; [p5 Sensitivity Analysis](../../../jama_brenner_2019_oi_190039.pdf#page=5) | Site-random-intercept binomial GLMM per main intention-to-screen outcome, lme4. Likelihood-ratio test of zero random-intercept variance. All P values 0.16–0.50; no statistical significance, model without random intercept retained. No row-specific test statistic printed in main article; results pointed to eTable 6. |
| M015 | p3 Results | 2422 recruited, 288 dropped out/excluded, 2134 analyzed. Similar women/men proportions; majority 93.6% aged 45–74; mean age 59.6 years; 78% colonoscopies for primary screening. Values refer to Table 1 and Figure. |
| M016 | p3 Results, eTable 2 narrative | Valid quantitative FIT day-2 scheduled samples: aspirin 1030 (95.8%), placebo 1012 (95.6%); qualitative aspirin 974 (90.6%), placebo 969 (91.5%). Group analysis denominators 1075 and 1059 in Figure/Table 1. |
| M017 | p4 Secondary End Points; p5 Table 2 all/Q10.2 | Quantitative specificity cutoff 10.2: 82.2% vs 88.7%, difference −6.4%, 95% CI −9.6 to −3.2%, P<.001; matching M047. |
| M018 | p4 Secondary End Points; p5 Table 2 all/Q17 | Quantitative specificity cutoff 17: 91.7% vs 94.8%, difference −3.1%, 95% CI −5.4 to −0.8%, P=.008; matching M049. |
| M019 | p4 Secondary End Points; p5 Table 2 all/qualitative | Qualitative sensitivity 34.7% vs 22.0%, intervention higher by 12.7 percentage points, 95% CI 0.1–24.7, P=.048; matching M050. |
| M020 | p4 Secondary End Points; p5 Table 2 all/qualitative | Qualitative specificity 83.8% vs 91.8%, intervention lower by 8.0 percentage points; signed 95% CI −11.0 to −4.9, P<.001; matching M051. |
| M021 | p4 Secondary End Points, men subgroup summary | Sensitivity higher between 8.4 (95% CI −7.5 to 23.3) and 17.6 (1.3 to 32.6) percentage points; specificity lower between 2.5 (−6.1 to 1.1) and 6.6 (−11.2 to −2.0) percentage points. Matches extremes M054,M056 and M055,M057. |
| M022 | p4 Secondary End Points, women/interaction summary | Women: sensitivity similar, specificity lower in aspirin than placebo. Sex-by-intervention interaction P all nonsignificant, range .08–.49; no outcome-specific P printed here. Six sensitivity/specificity subgroup pairs in Table 2 provide compared probabilities. |
| M023 | p4 eTable 3 narrative | Positivity at least 1 positive result among up to 3 samples scheduled days 2,3,4; higher sensitivity and lower specificity both groups than day-2 only; little change in sensitivity differences. No exact combined-result figures printed here. |
| M024 | p4 eTable 4 per-protocol narrative | Exactly-day-2 samples; men sensitivity difference quantitative lower cutoff 23.2 percentage points, 95% CI 5.0–39.5; qualitative 22.5 points, CI 4.5–38.6. Specificity differences similar to intention-to-screen. Two distinct inferential contrasts, no P or individual cell inputs printed here. |
| M025 | p4 Table 3/eTable 5 narrative | PPV/NPV day 2 after single 300 mg versus placebo: “Overall, no significant differences were seen, neither in intention-to-screen nor in per-protocol analysis.” Preserve scope word “Overall.” Table 3 all and subgroup results individually below. |
| M026 | p4 Adverse Events | Aspirin: 11 adverse events in 7 participants; 2 serious adverse events in 2 participants requiring hospitalization (appendicitis; suppurative cholangitis plus acute kidney injury), considered unrelated to drug. Placebo: 6 events in 5 participants, no serious events. All recovered. Event counts versus numbers of participants distinct; safety denominator not explicitly repeated in paragraph. |

## Figure participant flow

All rows source [PDF p4 Figure](../../../jama_brenner_2019_oi_190039.pdf#page=4); drug groups aspirin/placebo.

| Key | Exact box/footnote | Aspirin | Placebo | Total or rule |
|---|---|---:|---:|---|
| M027 | Randomized | 1208 | 1214 | Top box 2422 |
| M028 | Received as randomized; underwent colonoscopy | 1131 | 1153 | Same counts for both successive boxes |
| M029 | Did not receive as randomized or dropped out | 77 | 61 | Patients with neither any sample nor information considered dropouts (footnote b) |
| M030 | Included in analysis | 1075 | 1059 | Total 2134 |
| M031 | Excluded from primary analysis | 56 | 94 | From colonoscopy-stage totals; 150 together |
| M032 | Reasons within excluded: no stool; after colonoscopy; history blood; history CRC; aspirin takers | 32;2;20;not listed;2 | 56;not listed;30;5;3 | Preserve omitted reason as not listed rather than printed zero. Group reason sums 56 and 94. |
| M033 | Figure footnotes a,c | Eligibility-assessed number not collected | Followed up means completed colonoscopy | No inferred screening eligibility denominator |

## Table 1 full cell map

All rows source [PDF p4 Table 1](../../../jama_brenner_2019_oi_190039.pdf#page=4). Printed column headers Group, No. (%); aspirin n=1075; placebo n=1059. Each value is count (percentage).

| Key | Characteristic | Aspirin | Placebo | Denominator/definition |
|---|---|---|---|---|
| M034 | Sex men; women | 547 (50.9);528 (49.1) | 528 (49.9);531 (50.1) | Full group totals |
| M035 | Age <45;45–49 | 26 (2.4);63 (5.9) | 30 (2.8);52 (4.9) | Years, full group totals |
| M036 | Age 50–54;55–59 | 165 (15.3);315 (29.3) | 164 (15.5);318 (30.0) | Full group totals |
| M037 | Age 60–64;65–69 | 232 (21.6);144 (13.4) | 216 (20.4);153 (14.4) | Full group totals |
| M038 | Age 70–74;≥75 | 92 (8.6);38 (3.5) | 83 (7.8);43 (4.1) | Full group totals |
| M039 | Primary indication screening;diagnostic | 805 (77.9);228 (22.1) | 794 (78.2);221 (21.8) | Known indications 1033 and 1015, derived from printed counts |
| M040 | Footnote a missing primary indication | 42 | 44 | Explicit missingness; known+missing equals column n |
| M041 | Most advanced finding CRC;advanced adenoma | 3 (0.3);112 (10.4) | 5 (0.5);104 (9.8) | Full group totals, mutually exclusive highest finding |
| M042 | Most advanced finding nonadvanced adenoma;none above | 286 (26.6);674 (62.7) | 280 (26.4);670 (63.3) | Full group totals |

## Table 2 complete diagnostic cell inputs

All source [PDF p5 Table 2](../../../jama_brenner_2019_oi_190039.pdf#page=5), heading “Sensitivity and Specificity for Detecting Advanced Neoplasms at Day 2 After a Single 300-mg Aspirin Dose or Placebo.” Footnote: intention-to-screen analysis. Counts ordered TP,FN,TN,FP. TP true-positive, FN false-negative, TN true-negative, FP false-positive; Hb hemoglobin. Quantitative Q10.2/Q17 and qualitative L10.2 cutoffs in μg Hb/g. All rows retained; no patient-level data or missing classifications inferred.

| Key/cell group | Population and test | Aspirin TP,FN,TN,FP | Placebo TP,FN,TN,FP | Aspirin sensitivity,specificity % | Placebo sensitivity,specificity % |
|---|---|---|---|---|---|
| M043a | All Q10.2 | 45,67,755,163 | 31,71,807,103 | 40.2,82.2 | 30.4,88.7 |
| M043b | All Q17 | 32,80,842,76 | 23,79,863,47 | 28.6,91.7 | 22.5,94.8 |
| M043c | All L10.2 | 35,66,732,141 | 22,78,798,71 | 34.7,83.8 | 22.0,91.8 |
| M044a | Men Q10.2 | 33,44,360,90 | 15,39,387,68 | 42.9,80.0 | 27.8,85.1 |
| M044b | Men Q17 | 25,52,408,42 | 13,41,424,31 | 32.5,90.7 | 24.1,93.2 |
| M044c | Men L10.2 | 28,43,354,74 | 12,43,400,48 | 39.4,82.7 | 21.8,89.3 |
| M045a | Women Q10.2 | 12,23,395,73 | 16,32,420,35 | 34.3,84.4 | 33.3,92.3 |
| M045b | Women Q17 | 7,28,434,34 | 10,38,439,16 | 20.0,92.7 | 20.8,96.5 |
| M045c | Women L10.2 | 7,23,378,67 | 10,35,398,23 | 23.3,84.9 | 22.2,94.5 |

For each cell group: sensitivity inputs TP/(TP+FN); specificity TN/(TN+FP); sum TP+FN+TN+FP is valid sample denominator. Printed sensitivity/specificity use percent units. Cell counts and corresponding sex strata can be compared independently; no patient-time denominators.

## Table 2 individually keyed inference map

All source p5, exact table row as identified. Each CI is 95%; difference aspirin minus placebo; main methods describe Agresti–Caffo adjusted Wald intervals. P only exists where additionally repeated in p1/p4 narrative, listed explicitly; no invented subgroup P values. Source does not print sensitivity/specificity group-level CIs in Table 2.

| Key | Population/test | Measure | Aspirin % | Placebo % | Difference | 95% CI | P and exact additional occurrence |
|---|---|---|---:|---:|---:|---|---|
| M046 | All Q10.2 | Sensitivity | 40.2 | 30.4 | 9.8 | −3.1 to 22.2 | .14, pp1/4; p3 group probabilities |
| M047 | All Q10.2 | Specificity | 82.2 | 88.7 | −6.4 | −9.6 to −3.2 | <.001, p4 |
| M048 | All Q17 | Sensitivity | 28.6 | 22.5 | 6.0 | −5.7 to 17.5 | .32, pp1/4 |
| M049 | All Q17 | Specificity | 91.7 | 94.8 | −3.1 | −5.4 to −0.8 | .008, p4 |
| M050 | All L10.2 | Sensitivity | 34.7 | 22.0 | 12.7 | 0.1 to 24.7 | .048, p4 |
| M051 | All L10.2 | Specificity | 83.8 | 91.8 | −8.0 | −11.0 to −4.9 | <.001, p4 |
| M052 | Men Q10.2 | Sensitivity | 42.9 | 27.8 | 15.1 | −1.6 to 30.6 | Not printed |
| M053 | Men Q10.2 | Specificity | 80.0 | 85.1 | −5.1 | −10.0 to −0.1 | Not printed |
| M054 | Men Q17 | Sensitivity | 32.5 | 24.1 | 8.4 | −7.5 to 23.3 | Not printed; p4 range endpoint |
| M055 | Men Q17 | Specificity | 90.7 | 93.2 | −2.5 | −6.1 to 1.1 | Not printed; p4 range endpoint |
| M056 | Men L10.2 | Sensitivity | 39.4 | 21.8 | 17.6 | 1.3 to 32.6 | Not printed; p4 range endpoint |
| M057 | Men L10.2 | Specificity | 82.7 | 89.3 | −6.6 | −11.2 to −2.0 | Not printed; p4 range endpoint |
| M058 | Women Q10.2 | Sensitivity | 34.3 | 33.3 | 1.0 | −19.1 to 21.4 | Not printed |
| M059 | Women Q10.2 | Specificity | 84.4 | 92.3 | −7.9 | −12.0 to −3.8 | Not printed |
| M060 | Women Q17 | Sensitivity | 20.0 | 20.8 | −0.8 | −17.9 to 17.2 | Not printed |
| M061 | Women Q17 | Specificity | 92.7 | 96.5 | −3.7 | −6.7 to −0.8 | Not printed |
| M062 | Women L10.2 | Sensitivity | 23.3 | 22.2 | 1.1 | −17.7 to 20.9 | Not printed |
| M063 | Women L10.2 | Specificity | 84.9 | 94.5 | −9.6 | −13.5 to −5.5 | Not printed |

## Table 3 individually keyed inference map

Source [PDF p5 Table 3](../../../jama_brenner_2019_oi_190039.pdf#page=5), heading “Positive and Negative Predictive Values for Detecting Advanced Neoplasms at Day 2 After a Single 300-mg Aspirin Dose or Placebo.” Footnote intention-to-screen. Column labels PPV, NPV, Difference (95% CI); table title/definitions establish predictive percentages even though header omits explicit % signs. PPV=TP/(TP+FP), NPV=TN/(TN+FN), using corresponding Table 2 counts for same population/test. Difference CI convention M013. No P values printed in table. Every row has a separate PPV and NPV relation.

| Key | Population/test as source | Measure | Aspirin | Placebo | Difference | 95% CI | Cell input locator |
|---|---|---|---:|---:|---:|---|---|
| M064 | All Quantitative 10.2 | PPV | 21.6 | 23.1 | −1.5 | −10.7 to 7.4 | M043a TP,FP |
| M065 | All Quantitative 10.2 | NPV | 91.8 | 91.9 | −0.1 | −2.7 to 2.5 | M043a TN,FN |
| M066 | All Quantitative 17.0 | PPV | 29.6 | 32.9 | −3.2 | −17.2 to 10.5 | M043b TP,FP |
| M067 | All Quantitative 17.0 | NPV | 91.3 | 91.6 | −0.3 | −2.8 to 2.3 | M043b TN,FN |
| M068 | All Qualitative 10.2 | PPV | 19.9 | 23.7 | −3.8 | −14.4 to 6.5 | M043c TP,FP |
| M069 | All Qualitative 10.2 | NPV | 91.7 | 91.1 | 0.6 | −2.1 to 3.3 | M043c TN,FN |
| M070 | Men Quantitative 10.2 | PPV | 26.8 | 18.1 | 8.8 | −3.0 to 19.8 | M044a TP,FP |
| M071 | Men Quantitative 10.2 | NPV | 89.1 | 90.8 | −1.7 | −5.9 to 2.4 | M044a TN,FN |
| M072 | Men Quantitative 17.0 | PPV | 37.3 | 29.5 | 7.8 | −10.3 to 24.8 | M044b TP,FP |
| M073 | Men Quantitative 17.0 | NPV | 88.7 | 91.2 | −2.5 | −6.4 to 1.4 | M044b TN,FN |
| M074 | Men [blank Test cell] 10.2 | PPV | 27.5 | 20 | 7.5 | −6.4 to 20.2 | M044c TP,FP if intended qualitative identity confirmed |
| M075 | Men [blank Test cell] 10.2 | NPV | 89.2 | 90.3 | −1.1 | −5.3 to 3.0 | M044c TN,FN if intended qualitative identity confirmed |
| M076 | Women Quantitative 10.2 | PPV | 14.1 | 31.4 | −17.3 | −31.8 to −2.5 | M045a TP,FP |
| M077 | Women Quantitative 10.2 | NPV | 94.5 | 92.9 | 1.6 | −1.7 to 4.8 | M045a TN,FN |
| M078 | Women Quantitative 17.0 | PPV | 17.1 | 38.5 | −21.4 | −42.2 to 0.8 | M045b TP,FP |
| M079 | Women Quantitative 17.0 | NPV | 93.9 | 92 | 1.9 | −1.4 to 5.2 | M045b TN,FN |
| M080 | Women Qualitative 10.2 | PPV | 9.5 | 30.3 | −20.8 | −37.8 to −4.0 | M045c TP,FP |
| M081 | Women Qualitative 10.2 | NPV | 94.3 | 91.9 | 2.3 | −1.1 to 5.8 | M045c TN,FN |

Table 3 men third-row Test label is blank in both layout and full-page rendered image. “Qualitative” is therefore a proposed cross-table identity from row order/counts, not an exact printed label. Printed integer 20 and 92 are preserved rather than expanded to invented precision. Every CI lower/upper endpoint and difference retained as source, with no normalization of source rounding.

## Discussion, limitations, conclusions, contextual reference quantities

| Key | Exact source location | Values/statements retained |
|---|---|---|
| M082 | p5 Discussion opening; [p6 Conclusions](../../../jama_brenner_2019_oi_190039.pdf#page=6) | Age 40–80, one aspirin dose, no significant sensitivity increase at 2 predefined quantitative FIT cutoffs. Matches abstract conclusion and p2 Key Points. |
| M083 | p5 Discussion, previous study | Previous observational study used 2 other FITs (RIDASCREEN Haemo-/Haptoglobin Complex); sensitivity markedly increased among male low-dose aspirin users, modest decrease in specificity, not among women. No numeric effect or CI printed here. |
| M084 | p6 Discussion and Limitations first item | Designed to detect 24% absolute sensitivity increase; not powered for smaller effects. Same target as M012. |
| M085 | p6 Discussion dose/timing | 300 mg to achieve hemorrhagic effect after a single tablet; potential future lower doses 75 mg or 100 mg, single/multiple tablets over days. Primary sampling 2 days after aspirin for colonic transition. Multiple sampling days not suggested to improve performance by sensitivity analyses. Future doses are proposals, not observed group results. |
| M086 | p6 Limitations third item | Sample sizes for primary analyses “reduced by approximately 4% due to exclusions”; exclusions unrelated to treatment group. Exact denominator and exclusion subset not stated in this sentence. Do not substitute 288,150,valid-test losses or other numbers as its denominator without confirming source context. |
| M087 | p6 Limitations sixth/seventh items | 22% diagnostic colonoscopies, indication unrelated to rectal bleeding; one-time screening only, no long-run CRC incidence/mortality estimates. |
| M088 | p6 Limitations second/fourth/fifth | Multiple secondary analyses without multiple-test adjustments; few advanced neoplasms limit subtype sensitivity analyses; number excluded for preexisting aspirin/NSAID use not quantified. Scope constraints for numerical interpretation. |
| M089 | [p7 reference 1 title](../../../jama_brenner_2019_oi_190039.pdf#page=7) | Global cancer statistics 2018; 36 cancers in 185 countries. Contextual title descriptors, no underlying prevalence/death numerator printed here. |
| M090 | p7 reference 3 title | Nottingham FOBT trial 20-year follow-up; no effect estimate supplied in reference entry. |
| M091 | p7 reference 6 title | Comparison of one guaiac and 3 immunochemical fecal occult blood tests; no table-level results in reference entry. |
| M092 | p7 reference 7 title | Head-to-head FIT versus guaiac comparison among 2235 screening-colonoscopy participants; no sensitivity/specificity result printed in reference entry. |
| M093 | p7 reference 9 title | European code against cancer, 4th edition; contextual edition descriptor, no comparative result. |
| M094 | p7 reference 14 title | ASTER double-blind randomized placebo-controlled phase III protocol; contextual study phase, no observed result. |
| M095 | p7 reference 15 title | Randomized comparison of 2 FITs in population-based screening; no numeric outcome in reference entry. |
| M096 | p7 reference 19 title | Confidence intervals for proportions/differences from adding 2 successes and 2 failures. This supplied reference-title description accompanies Agresti–Caffo methods citation; it is not a independently specified article P-test. |
| M097 | p7 reference 20 entry | lme4 “Linear Mixed-Effects Models Using Eigen and S4,” version 1.1-21, accessed April 15, 2019. Software locator, distinct from article R version 3.4.0. |
| M098 | pp1,2,6 ages and eligibility matching | Abstract, Methods, Key Points, Discussion and Conclusions share adults 40–80 and no recent aspirin/antithrombotic use; no alternative observed age limits printed. |
| M099 | pp1–6 day/dose/cutoff matching | Single 300 mg; scheduled day 2 intention-to-screen versus exactly day 2 per-protocol; 10.2/17 (17.0 tables) μg Hb/g. Stool and feces units used synonymously in report. |
| M100 | pp1,3,4 prevalence matching inputs | CRC 3+5=8; advanced adenoma 112+104=216; advanced neoplasms total 224. Table 1 subgroup advanced totals 115 and 109, whereas quantitative FIT evaluable advanced totals M043 are 112 and 102 and qualitative 101 and 100. These are distinct analysis/sample-completeness quantities, all printed or directly derived from supplied counts. |
| M101 | pp3–5 sample completeness matching inputs | Quantitative all detection sums 1030 aspirin and 1012 placebo; qualitative 974 and 969; match p3 valid-sample narrative. Sex-specific detection sums available individually from M044/M045, without assuming every randomized patient yielded a valid test. |
| M102 | pp1,3,4 sex/age/indication matching inputs | Table 1 men 547+528 and women 528+531; age bins 45–74 comprise M035 age45–49 plus M036/M037/M038 age70–74; screening/diagnostic denominator excludes M040 missing indications. Abstract printed men 1219 and 50% separately retained M002. No invented SD for analyzed subset. |
| M103 | p7 non-result content coverage | Funding, funder role, compensated contributions, data sharing pointer to Supplement 4, all references 1–32 inspected. Remaining digits identify authors' cited years, journal volume/issue/pages, DOI and URLs. No additional trial counts, ratios, CI, P values, SE, rates, units, model results or clinical comparisons occur. |

## Inferential inventory handoff and limitations

Thirty-six individually keyed Table 2/Table 3 difference-CI relationships (M046–M081); six exact narrative P values are attached to M046–M051 (P<.001 appears for two separate specificity contrasts). Two additional exactly-day-2 male per-protocol difference-CI relationships in M024. One grouped interaction-P summary M022 and one grouped random-intercept likelihood-ratio P summary M014 are additionally mapped; their row-specific values are absent from the main article and belong to assigned support scope. Power/alpha rules M012, test/CI conventions M013, multiplicity rule M013/M088 and interpretation statements M004/M005/M025/M082 accompany these inferential rows. Thus 40 inferential-result units in the main report are explicitly located, including the two grouped summaries; the statistical reviewer must create stable global S identifiers and join the supplement-specific rows without double-counting matched occurrences.

No scientific coverage gap remains in DOC-001. Missing reported definitions (primary P-test formula, denominator/subset of “approximately 4%,” precise scope of abstract mean/SD and male count, blank Table 3 Test cell, row-specific interaction/random-site P values) are preserved as limitations or matching questions, not candidate diagnoses. Final scientific dispositions remain outside this mapping stage.
