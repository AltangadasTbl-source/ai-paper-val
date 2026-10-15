# Fresh Main-Paper Quantitative Evidence Map

Scope: DOC-001, jama_debar_2025_oi_250046_1755300121.13587.pdf, PDF pages 1–14 (printed pages 592–605). Document role: REPORT by content. Mapped: 14/14. This is extraction only; no candidate selection or scientific judgments are assigned. Local descriptive keys MAIN001–MAIN116 identify 116 complete relationship groups; canonical N/S inventory assignment belongs to the coordinator/checkers. Each table-row key includes every group and contrast, rather than sampling a result. Every inferential row carries its printed 95% intervals and omnibus P value.

Evidence precedence: supplied PDF; fresh direct native extraction; original page text and original rendered images/OCR only as locators. No prior scientific map, checker, candidate, screen, or report was read. Eligible locators are .ai_paper_validation/document_outputs/DOC-001-MAIN/normalized_text/page_NNN.txt and original page_images/page_NNN.png; original OCR pp.9–11 was used only alongside direct PDF native text and visual confirmation. Native derivatives labeled rotated/unusable were not used. Fresh derivative: preprocessing/main_restart/direct_native.txt, produced from the supplied PDF pp.1–14 using supplied workflow_1_6_2/scripts/pdf_tools.py text with package-local interpreter and PyMuPDF 1.26.4, CPU. No fresh OCR was needed. Original images pp.9–11 were visually inspected to confirm table headings, exact row alignment, all displayed signs and interval endpoint order. Original OCR has incidental glyph substitutions (for example 230% for ≥30%); the values below follow direct native PDF text and page images. All source links below are relative to this extraction artifact.

Abbreviations throughout: PT = painTRAINER; HC = health coach; UC = usual care plus. Group order in triple entries is always PT / HC / UC. Contrast order is always PT vs UC / HC vs UC / HC vs PT. Parentheses after estimates contain printed 95% CI endpoints unless explicitly marked SD/IQR. Preserve −0.0 and −0.00 as printed signed zeros; do not sort displayed interval endpoints. Percentages are percentage units; RR and SMD are dimensionless; NNT is participants per additional response. Binary response is ≥30% improvement from baseline unless stated otherwise.

## Unit closure

| PDF page | Printed page | Exact mapped scope | Closure |
|---|---:|---|---|
| 1 | 592 | Abstract, sample, intervention, outcome hierarchy, demographic aggregates, adjusted primary results and all contrasts | COMPLETE |
| 2 | 593 | Key Points, eligibility and design, site/recruitment timing, clinical thresholds | COMPLETE |
| 3 | 594 | Randomization, treatment doses/duration, outcome construction and follow-up times | COMPLETE |
| 4 | 595 | Sample size, power, modeling, missing data, all results narrative and baseline aggregates | COMPLETE |
| 5 | 596 | Figure 1 flow, exclusions, all arm counts, session groups, follow-up, footnotes | COMPLETE |
| 6 | 597 | Every Table 1 row through primary baseline outcome | COMPLETE |
| 7 | 598 | Every remaining Table 1 row and footnote; primary/secondary narrative; adverse-event totals | COMPLETE |
| 8 | 599 | Figure 2 axes, all observed counts, caption; all adverse-event group values; discussion claims | COMPLETE |
| 9 | 600 | Every Table 2 row and footnote; all groups, RR contrasts, omnibus tests and NNTs | COMPLETE |
| 10 | 601 | Every Table 3 row for severity, intensity, interference, social and physical functioning | COMPLETE |
| 11 | 602 | Every Table 3 row for both global-impression outcomes and all Table 3 footnotes | COMPLETE |
| 12 | 603 | Discussion/limitations/conclusion matching claims; article information has no additional applicable quantitative result | COMPLETE |
| 13 | 604 | References only: no applicable trial relationship; citation numbering/bibliographic numbers are not study results | COMPLETE_NO_APPLICABLE |
| 14 | 605 | References only: no applicable trial relationship; citation numbering/bibliographic numbers are not study results | COMPLETE_NO_APPLICABLE |

## Abstract, methods, narrative aggregates and prespecified matching keys

| Key | Exact source location | Reconstructed relationship and matching occurrences |
|---|---|---|
| MAIN001 | [p.1 abstract design/interventions](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1); pp.2–3 design/randomization; p.5 Figure 1 | Phase 3 comparative-effectiveness parallel 3-group RCT; individually randomized equal 1:1:1; eligible analyzed randomized population 2331, HC 778/PT 776/UC 777. Four US health systems; enrolled Jan 2021–Feb 2023; follow-up ends Apr 2024. Figure 1 total allocated 2333 includes 2 UC participants not meeting EHR eligibility; primary analysis retains 2331. |
| MAIN002 | p.1 abstract outcomes; p.2 Key Points; p.3 Primary Outcome; p.9 Table 2 | Primary binary outcome: attaining/exceeding MCID defined ≥30% decrease in pain severity from pre-randomization baseline to 3 months; composite modified 11-item BPI-SF mean, scale 0–10, higher = worse; 6/12 months secondary time points. Key Points says at least 30% improvement at 3 months, benefits sustained 12 months, HC better than PT at 3 months. |
| MAIN003 | p.1 abstract demographic/completion results; p.4 Results; p.6 Table 1; p.5 Figure 1 | Eligible randomized 2331; age 58.8(SD 14.3)y; women 1712[74%]; rural/medically underserved 1030[44%]; completed trial 2210(94.8%). Body p.4 repeats 2331/2210 without percentage. Figure 1 withdrawal counts 43/45/16 and deaths 3/7/7 provide separate end-of-follow-up status quantities. |
| MAIN004 | p.1 abstract primary percentages; pp.4/7 Primary Outcomes; p.9 severity 3 mo; p.8 Figure 2 | At 3 mo adjusted response HC 32.0(29.3–35.0)%; PT 26.6(23.4–30.2)%; UC 20.8(18.0–24.0)%. Body omnibusP<.001. Matching complete binary row MAIN080. |
| MAIN005 | p.1 abstract contrasts; p.7 Primary Outcomes; p.9 severity 3 mo | HC vs UC RR1.54(1.30–1.82); PT vs UC 1.28(1.06–1.55); HC vs PT 1.20(1.03–1.40). Abstract describes both active groups significantly more likely than UC and HC more effective than PT. |
| MAIN006 | p.1 abstract conclusion; pp.7–8 Results/discussion; p.12 Conclusions | Abstract: significant benefits active groups vs UC at 6/12 months for severity and other secondary pain/functioning outcomes; modest improvement in pain and functional/quality-of-life outcomes. Body: active-vs-UC severity differences persist 6/12 months with attenuated RRs; HC-vs-PT difference no longer significant 6/12 months. Discussion says broader outcomes show similar sustained improvement and remote-program outcomes do not differ 6/12 months; p.12 sustained greater severity reduction through 12 months. Match all rows MAIN080–MAIN109, not only severity. |
| MAIN007 | p.2 Methods recruitment/eligibility | Four systems: KPGeorgia, KPNorthwest, KPWashington, Essentia. Recruitment Jan 2021–Feb 2023, 26 months; follow-up Apr 2021–Apr 2024. Age≥18, English, care within past year, internet/telephone. EHR outpatient pain encounters≥1 Essentia or≥2 KP, >60 days apart within 360 days. High-impact chronic pain via Graded Chronic Pain Scale–Revised; PEG≥12. |
| MAIN008 | p.2 eligibility criteria; p.5 Figure 1 footnotea | PEG3 items each 0–10, summed 0–30, higher = worse. Screen tiered: high-impact chronic pain first, then PEG≥12, then other criteria. No surgery for common musculoskeletal pain past 60 days; no malignant cancer except nonmelanoma skin cancer past 60 days; no hospice/palliative care past 360 days; no CBT/psychoeducation/behavioral pain skills past 6 months/current/nextmonth; no inpatient/intensive outpatient substance-use services current/nextmonth; no pain surgery planned within 12 months. |
| MAIN009 | p.3 randomization; p.5 Figure 1 footnoteb | Individual allocation 1:1:1 after baseline. Stratified sex(male/female), baseline severity<7/≥7, clinical site, rural/medically underserved yes/no. Within strata random permuted blocks 3/6/9. Outcome assessors and enrollment/eligibility staff blinded. Monthly candidate sampling additionally stratified urban vs rural/medically underserved; recruitment letter then email approx 5 days later and telephone follow-up. |
| MAIN010 | pp.1–3 interventions | Both active treatments 8 sessions with similar content and usual pain care allowed. HC 12 master's-level coaches, one-on-one telephone/video, 45–60 min/session approx 1/week, all 8 intended within 12 weeks after randomization. PT online 30–45 min/session approx 1/week, all 8 intended within 12 weeks; onboarding call, access 1 year, technical/outreach support. Prespecified outreach examples >10 days since last session or≥3 sessions in 9 days; no treatment-content guidance. UC mailed ACPA2020 resource guide. |
| MAIN011 | p.3 Primary Outcome scoring | All 4 intensity items and≥4 of 7 interference items required to score 11-item severity. Severity composite mean 0–10 higher = worse. Baseline and 3/6/12 months measured online/telephone/postal according to preference. Binary MCID≥30%decrease vs baseline. Match Table 1 primary baseline and Table 2 severity and Table 3 continuous severity. |
| MAIN012 | pp.3–4 Secondary Outcomes; p.1 abstract | Binary secondary MCID≥30%improvement in intensity 4-item mean and interference 7-item mean, each 0–10 higher = worse. Continuous changes in severity/intensity/interference at 3/6/12 months also assessed. PROMIS social 4 items, physical 6 items; patient global impression of change pain/general modified 7-point scale. All abstract secondary endpoints reported at 3/6/12 months. |
| MAIN013 | p.4 Sample Size | Planned 2331=777/group, 90%power to detect 7.5 percentage-point difference (RR1.5) for each active vs UC at 3 mo; UC response 15%; retention 80%; Fisher least significant difference multiplicity control; 10000 modified Poisson simulation replications in R3.6.2. No numerical interim/stopping boundary reported in main paper. |
| MAIN014 | p.4 Statistical Analysis primary | Intention-to-treat principle all analyses. Binary modified Poisson regression for adjusted RR/95%CI; GEE working independence, robust sandwich standard errors, clustering at highest level within-person or within-HC. Group indicators, time indicators, group×time interactions for time-specific effects. No printed standard-error values or test-statistic values in main paper. |
| MAIN015 | p.4 Statistical Analysis adjustment | Prespecified adjustment baseline pain severity, sex, site, rural/medically underserved residence, multisite pain, co-occurring mental health condition. Adjusted percentages and 95%CIs computed centering covariates at means across all participants. Secondary models same structures plus baseline value of secondary outcome. Match Table 2 footnoteb and Table 3 footnoteb. |
| MAIN016 | p.4 Statistical Analysis NNT | Adjusted NNT=1/(difference in adjusted response proportion between groups), to contextualize binary outcomes. Table 2 labels adjusted No.needed to treat(95%CI). Each row/contrast transcribed MAIN080–MAIN088; footnoted/e mapped MAIN110. |
| MAIN017 | p.4 continuous methods; p.11 Table 3 footnoted | Continuous secondary: linear regression with GEE for within-arm adjusted mean/95%CI, between-arm adjusted mean difference/95%CI and SMD at eachtime. SMD=adjusted difference / SD of change in UC at that time. Interpretation thresholds small 0.2–0.5, moderate>0.5–0.8, large>0.8. Denominator SD itself not printed. |
| MAIN018 | p.4 missing data | Primary missing outcome handled by(1)prespecified adjustment; (2)nonignorable pattern-mixture imputation among participants with≥1 follow-up; (3)inverse probability of missing weighting for no follow-up. Missing covariates mean-imputed. Missingness sensitivity analyses described planned/conducted. Locators eTables 1–6/eFigure 2; sensitivityeTable 7, Supplement 4. |
| MAIN019 | p.4 statistical tests; pp.9/11 omnibus footnotes | Analyses R4.4.1 on Windows 10; alltests 2-sidedα=.05. Table 2/Table 3 omnibus Wald test any difference across 3 groups. Between-group comparisons only if omnibusP<.05 under least significant difference. Confidence intervals 95%. OmnibusP is not labeled a pairwiseP. |
| MAIN020 | p.4 Results follow-up/adherence | Among 7628 screened, 2331 eligible randomized, 2210 completed. Any follow-up PT 643[83%], HC 690[89%], UC 703[90%]; PT approximately 6–7%lower overall. At 3 mo PT 70%, HC 82%, UC 80%, described 10%lower PT. ≥1 session PT 527(68%), HC 660(85%); ≥6 sessions therapeutic dose PT 371(43%), HC 548(70%). Match Figure 1 MAIN030–MAIN033 and supplementary eFigure 1 locator. |
| MAIN021 | p.4 Results baseline narrative | Almost 40%≥65; age 58.8(SD 14.3); 74%women; 75%White non-Hispanic; 44%rural/medically underserved; 33%negative social determinant. Multiple musculoskeletal pain conditions 73%, mean 2.5(SD 1.3); high severity BPI≥7:25.5%; depressionPHQ8≥10:47.8%; anxietyGAD7≥10:27.8%; at least moderate sleep disturbance 43.3%; long-term opioid 9.6% among sites with dispense data. Match Table 1 all rows, sourceSupplement 5 locator. |
| MAIN022 | p.7 Secondary Outcomes | Secondary patterns described significantly better PT/HC vs UC 3 mo and sustained 12 mo with modest attenuation. Narrative 3 mo severity SMD PT−0.26, HC−0.36 vs UC; table rows fullytranscribed MAIN089–MAIN091, retaining printedtime/values. No adjudication is attached. |

## Figure 1: complete flow reconstruction

All following keys: [PDF p.5, printed p.596, Figure 1](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5). Quantities are participants unless explicitly events/providers. Follow-up can overlap later withdrawal/death; footnote g says assessments may have occurred before those events.

| Key | Flow or footnote quantity | Complete printed values and nesting |
|---|---|---|
| MAIN023 | Invitation-to-screen |62125 mailed after EHR screening at 4 systems; 54497 excluded:36656 could not be reached, 17803 declined screening, 38 deceased; 7628 screened. |
| MAIN024 | Screening ineligible |4481 ineligible:2993 no high-impact chronic pain; 245 PEG<12; 1243 one or more other reasons. Listed other reasons 411 behavioral treatment, 273 planned surgery, 189 no internet/phone, 121 not English-speaking, 95 cognitive/hearing impairment, 34 substance-use treatment. Reasons within 1243 are not labeled exhaustive unique counts. |
| MAIN025 | Eligibility-to-consent |3147 eligible; 672 excluded:339 declined, 333 unreachable; 2475 consent complete. |
| MAIN026 | Consent-to-randomized |142 excluded:118 unreachable, 24 declined baseline; 2333 randomized. |
| MAIN027 | Allocation and primary analyzed set |PT 776 allocated/776 analyzed; HC 778 allocated/778 analyzed; UC 779 allocated, 777 mailed resource guide, 2 not meeting EHR criteria, 777 analyzed. |
| MAIN028 | PT session completion |371 completed 6–8; 156 completed 1–5; 249 completed none; total 776. No-session subgroup footnote c:13 withdrew, 1 incarcerated, 2 died; 233 remained. Among 233:212 unreachable, 8 no longer interested, 5 other health/life issues, 3 did not like intervention, 3 no reason, 2 no time. |
| MAIN029 | HC session completion |548 completed 6–8; 112 completed 1–5; 118 none; total 778. None-session 118:16 withdrew, 1 died; 101 remained:74 unreachable, 16 no time, 3 other health/life issues, 3 no reason, 2 did not like intervention, 2 no longer interested, 1 privacy concerns. |
| MAIN030 | PT follow-up |3 mo 542; 6 mo 547; 12 mo 583; any 643; withdrawn 43; died 3; primary analysis 776. |
| MAIN031 | HC follow-up |3 mo 635; 6 mo 621; 12 mo 639; any 690; withdrawn 45; died 7; primary analysis 778. |
| MAIN032 | UC follow-up |3 mo 621; 6 mo 622; 12 mo 639; any 703; withdrawn 16; died 7; primary analysis 777. |
| MAIN033 | Session/assessment relationships |Figure footnote f: follow-up assessed regardless sessions. Anyfollow-up counts are not completer-only denominators. PT≥1=371+156, HC≥1=548+112; threshold≥6=6–8 session category. Body p.4 prints ≥1 session 527/660 and≥6 session 371/548. |
| MAIN034 | Provider clustering descriptors |12 HCproviders; medianpatients/provider 69(IQR52–76), range 24–110. Connect highest-levelHC clustering MAIN014. |
| MAIN035 | Full Figure 2 observation correspondence |Figure 1 counts match Figure 2 p.8 observation grid at 3/6/12 mo:UC 621/622/639, PT 542/547/583, HC 635/621/639. Table 2 n 643/690/703 is any follow-up; Figure 2 counts are observed-at-time. |

## Table 1: every baseline row

Sources: [p.6 Table 1](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=6) and [p.7 continuation/footnotes](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7). All table columns PTn 776 / HCn 778 / UCn 777. Counts include explicit nonmissing denominators. No P values/effect estimates in this table. Triple order PT/HC/UC.

| Key | Page, row and unit | PT | HC | UC |
|---|---|---|---|---|
| MAIN036 |6 Age mean(SD), years |58.8(13.9), n 776|58.8(14.5), n 778|58.8(14.3), n 777|
| MAIN037 |6 Age≥65 years, count/total(%) |291/776(37.5)|305/778(39.2)|304/777(39.1)|
| MAIN038 |6 Female |571/776(73.6)|572/778(73.5)|569/777(73.2)|
| MAIN039 |6 Male |205/776(26.4)|206/778(26.5)|208/777(26.8)|
| MAIN040 |6 College degree/higher |332/770(43.1)|347/767(45.2)|344/770(44.7)|
| MAIN041 |6 Not employed |400/769(52.0)|416/771(54.0)|418/769(54.4)|
| MAIN042 |6 Household income<$50000 |266/671(39.6)|217/643(33.7)|251/681(36.9)|
| MAIN043 |6 Married/domestic partnered |484/761(63.6)|512/768(66.7)|511/771(66.3)|
| MAIN044 |6 American Indian/Alaska Native |6/751(0.8)|11/760(1.4)|11/755(1.5)|
| MAIN045 |6 Asian |10/751(1.3)|6/760(0.8)|11/755(1.5)|
| MAIN046 |6 Black/African American non-Hispanic |119/751(15.8)|118/760(15.5)|113/755(15.0)|
| MAIN047 |6 Hispanic |21/751(2.8)|26/760(3.4)|30/755(4.0)|
| MAIN048 |6 Native Hawaiian/other Pacific Islander |1/751(0.1)|0/760(no percentage printed)|1/755(0.1)|
| MAIN049 |6 White non-Hispanic |573/751(76.3)|572/760(75.3)|554/755(73.4)|
| MAIN050 |6 ≥1 race [printed label] |21/751(2.8)|27/760(3.6)|35/755(4.6)|
| MAIN051 |6 Rural/medically underserved |340/776(43.8)|345/778(44.3)|345/777(44.4)|
| MAIN052 |6 Any negative social determinant |261/763(34.2)|231/766(30.2)|266/769(34.6)|
| MAIN053 |6 Financial resource strain |198/770(25.7)|170/771(22.0)|199/771(25.8)|
| MAIN054 |6 Housing instability |134/766(17.5)|101/763(13.2)|129/767(16.8)|
| MAIN055 |6 Food insecurity |116/769(15.1)|100/773(12.9)|117/768(15.2)|
| MAIN056 |6 Transportation insecurity |57/772(7.4)|56/774(7.2)|57/773(7.4)|
| MAIN057 |6 Pain severity≥7 |195/776(25.1)|199/778(25.6)|200/777(25.7)|
| MAIN058 |6 Pain duration>5 years |532/775(68.6)|536/778(68.9)|541/777(69.6)|
| MAIN059 |6 Hip, knee, foot pain |494/776(63.7)|487/778(62.6)|495/777(63.7)|
| MAIN060 |6 Back pain |402/775(51.9)|401/777(51.6)|422/777(54.3)|
| MAIN061 |6 Hand, arm, shoulder pain |298/774(38.5)|301/778(38.7)|284/777(36.6)|
| MAIN062 |6 Neck pain |202/776(26.0)|207/778(26.6)|213/777(27.4)|
| MAIN063 |6 Widespread pain |141/775(18.2)|176/775(22.7)|143/777(18.4)|
| MAIN064 |6 Headache/migraine |95/775(12.3)|131/778(16.8)|117/777(15.1)|
| MAIN065 |6 Abdominal, pelvic, genital pain |58/775(7.5)|73/777(9.4)|66/775(8.5)|
| MAIN066 |6 Toothache/jaw pain |37/776(4.8)|54/777(6.9)|52/777(6.7)|
| MAIN067 |6 Musculoskeletal pain condition count median(IQR) |2.0(1–3), n 776|2.0(1–3), n 778|2.0(1–3), n 777|
| MAIN068 |6 pain health care encounters past year median(IQR) |6.0(3–12), n 776|6.0(3–13), n 778|6.0(3–11), n 777|
| MAIN069 |6 Long-term opioid |43/569(7.6)|60/566(10.6)|60/562(10.7)|
| MAIN070 |6 Anxiety/depression diagnosis |300/776(38.7)|322/778(41.4)|343/777(44.1)|
| MAIN071 |6 Moderate to severe depression |373/775(48.1)|373/777(48.0)|370/777(47.6)|
| MAIN072 |6 Moderate to severe anxiety |206/774(26.6)|218/778(28.0)|224/777(28.8)|
| MAIN073 |6 Moderate to severe sleep disturbance |332/772(43.0)|331/775(42.7)|342/772(44.3)|
| MAIN074 |6 Substance use disorder diagnosis |31/776(4.0)|31/778(4.0)|24/777(3.1)|
| MAIN075 |6 Charlson Comorbidity Index median(IQR) |0.0(0–1.25), n 776|1.0(0–2), n 778|1.0(0–2), n 777|
| MAIN076 |6 Primary baseline severity 0–10 mean(SD) |5.8(1.6), n 776|5.9(1.7), n 778|5.9(1.6), n 777|
| MAIN077 |7 Secondary baseline intensity 0–10 mean(SD) |5.4(1.6), n 776|5.6(1.7), n 778|5.5(1.6), n 777|
| MAIN078 |7 Secondary baseline interference 0–10 mean(SD) |6.0(1.9), n 776|6.0(1.9), n 778|6.1(1.9), n 777|
| MAIN079 |7 Secondary baseline functioning limitations, count/total(%) |Social 258/758(34.0); physical 563/764(73.7)|Social 283/770(36.8); physical 566/770(73.5)|Social 277/765(36.2); physical 580/773(75.0)|

## Table 2: complete adjusted binary outcome relationships

Source: [p.9, printed p.600, Table 2](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9). Headings visually confirmed against source page image. Group denominators PT 643 / HC 690 / UC 703 (any follow-up participants). Modified Poisson/GEE adjusted ≥30% response; each group value is adjusted percentage(95%CI). Contrast values RR(95%CI). Omnibus WaldP tests all 3 groups; NNT columns use same contrast order. Primary outcome severity 3 mo; all other rows under secondary outcomes. All 3 mo rows marked primary time pointg.

| Key | Outcome, time | Group adjusted %: PT / HC / UC | Adjusted RR: PT−UC / HC−UC / HC−PT | Omnibus P | NNT(95%CI): PT−UC / HC−UC / HC−PT |
|---|---|---|---|---|---|
| MAIN080 |Severity 3 mo|26.6(23.4–30.2) /32.0(29.3–35.0) /20.8(18.0–24.0)|1.28(1.06–1.55) /1.54(1.30–1.82) /1.20(1.03–1.40)|<.001|18(10–71) /9(7–14) /19(11–102)|
| MAIN081 |Severity 6 mo|32.9(29.5–36.7) /37.1(34.1–40.5) /22.9(20.0–26.1)|1.44(1.21–1.70) /1.62(1.39–1.90) /1.13(0.98–1.30)|<.001|10(7–19) /8(6–11) /24(12–186)|
| MAIN082 |Severity 12 mo|35.9(32.4–39.7) /38.3(36.8–39.9) /27.1(24.1–30.5)|1.32(1.13–1.54) /1.41(1.25–1.59) /1.07(0.96–1.19)|<.001|12(8–26) /9(7–13) /41(17–76)|
| MAIN083 |Intensity 3 mo|24.3(21.2–27.8) /27.0(24.0–30.5) /17.7(15.1–20.7)|1.37(1.12–1.69) /1.53(1.26–1.86) /1.11(0.93–1.33)|<.001|16(10–43) /11(8–20) /37(14–57)|
| MAIN084 |Intensity 6 mo|26.9(23.7–30.5) /31.8(28.3–35.7) /21.1(18.3–24.3)|1.27(1.06–1.54) /1.51(1.26–1.80) /1.18(1.00–1.40)|<.001|18(10–76) /10(7–17) /21(11–5524)|
| MAIN085 |Intensity 12 mo|32.1(28.7–35.8) /33.7(31.2–36.3) /26.4(23.4–29.8)|1.21(1.03–1.43) /1.28(1.11–1.47) /1.05(0.92–1.20)|.003|18(10–106) /14(9–31) /63(18–38)|
| MAIN086 |Interference 3 mo|30.6(27.3–34.4) /35.6(33.7–37.6) /23.4(20.5–26.8)|1.31(1.10–1.55) /1.52(1.32–1.75) /1.16(1.02–1.32)|<.001|14(9–40) /9(7–12) /21(12–100)|
| MAIN087 |Interference 6 mo|37.0(33.5–40.9) /40.9(37.0–45.1) /24.3(21.3–27.6)|1.52(1.30–1.79) /1.68(1.43–1.98) /1.10(0.96–1.27)|<.001|8(6–13) /7(5–9) /26(11–67)|
| MAIN088 |Interference 12 mo|39.6(36.1–43.5) /42.3(40.6–44.0) /30.6(27.4–34.2)|1.29(1.12–1.49) /1.38(1.23–1.55) /1.07(0.97–1.18)|<.001|12(8–25) /9(7–13) /39(16–79)|

## Table 3: complete adjusted continuous outcome relationships

Sources: [p.10, printed p.601, Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11, printed p.602, continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All values below are as printed, with interval ordering/signs retained and confirmed visually. Linear regression/GEE adjusted randomized population average effects at mean covariates. Columns exactly group means PT/HC/UC, then adjusted mean difference PT−UC/HC−UC/HC−PT, omnibusP, then SMD PT−UC/HC−UC/HC−PT. Values in SMD columns are mapped by printed headings, not rearranged. Each estimate has its own printed 95%CI. Severity/intensity/interference units points 0–10, negativechange=improvement; PROMIS Tscorechange positive=improvement. PGIC pain/general headings say mean change but footnotes define status-since-study scale 1–7, higher = worse. Group counts shown once above outcome block: severity/intensity/interference 643/690/703; social 636/683/696; physical 639/684/699; PGIC-pain637/687/702; PGIC-general640/687/702. Every 3 mo marked primary time pointe.

| Key | Page, outcome, time | Group mean(95%CI): PT / HC / UC | Mean difference(95%CI): PT−UC / HC−UC / HC−PT | Omnibus P | SMD(95%CI): PT−UC / HC−UC / HC−PT |
|---|---|---|---|---|---|
| MAIN089 |10 Severity 3 mo|−1.2(−1.3 to−1.0) /−1.2(−1.3 to−1.1) /−0.8(−0.9 to−0.6)|−0.4(−0.6 to−0.2) /−0.4(−0.6 to−0.3) /−0.0(−0.2 to 0.1)|<.001|−0.25(−0.28 to−0.02) /−0.34(−0.36 to−0.13) /−0.13(−0.15 to 0.08)|
| MAIN090 |10 Severity 6 mo|−1.3(−1.4 to−1.1) /−1.4(−1.5 to−1.3) /−0.9(−1.0 to−0.8)|−0.4(−0.6 to−0.2) /−0.5(−0.7 to−0.4) /−0.1(−0.3 to 0.1)|<.001|−0.26(−0.34 to−0.08) /−0.36(−0.43 to−0.19) /−0.12(−0.19 to 0.04)|
| MAIN091 |10 Severity 12 mo|−1.5(−1.6 to−1.3) /−1.4(−1.6 to−1.3) /−1.1(−1.2 to−0.9)|−0.4(−0.6 to−0.2) /−0.4(−0.6 to−0.2) /0.0(−0.2 to 0.2)|<.001|−0.25(−0.24 to 0.01) /−0.36(−0.35 to−0.12) /−0.11(−0.11 to 0.12)|
| MAIN092 |10 Intensity 3 mo|−0.9(−1.0 to−0.8) /−0.9(−1.0 to−0.8) /−0.6(−0.7 to−0.5)|−0.3(−0.5 to−0.1) /−0.3(−0.5 to−0.2) /−0.0(−0.2 to 0.2)|<.001|−0.21(−0.21 to−0.01) /−0.29(−0.30 to−0.11) /−0.08(−0.09 to 0.09)|
| MAIN093 |10 Intensity 6 mo|−1.0(−1.1 to−0.9) /−1.1(−1.2 to−1.0) /−0.7(−0.9 to−0.6)|−0.2(−0.4 to−0.1) /−0.3(−0.5 to−0.2) /−0.1(−0.3 to 0.1)|<.001|−0.17(−0.23 to−0.06) /−0.27(−0.32 to−0.17) /−0.04(−0.10 to 0.05)|
| MAIN094 |10 Intensity 12 mo|−1.1(−1.3 to−1.0) /−1.1(−1.3 to−1.0) /−0.9(−1.0 to−0.8)|−0.2(−0.4 to−0.1) /−0.2(−0.4 to−0.1) /0.0(−0.2 to 0.2)|.01|−0.16(−0.16 to 0.00) /−0.27(−0.26 to−0.12) /−0.03(−0.03 to 0.11)|
| MAIN095 |10 Interference 3 mo|−1.3(−1.4 to−1.1) /−1.4(−1.5 to−1.2) /−0.8(−1.0 to−0.7)|−0.5(−0.7 to−0.3) /−0.5(−0.7 to−0.3) /−0.1(−0.3 to 0.2)|<.001|−0.25(−0.28 to−0.03) /−0.34(−0.37 to−0.13) /−0.13(−0.15 to 0.07)|
| MAIN096 |10 Interference 6 mo|−1.5(−1.6 to−1.3) /−1.6(−1.8 to−1.4) /−1.0(−1.1 to−0.8)|−0.5(−0.7 to−0.3) /−0.6(−0.8 to−0.4) /−0.1(−0.4 to 0.1)|<.001|−0.27(−0.34 to−0.08) /−0.37(−0.44 to−0.19) /−0.14(−0.21 to 0.04)|
| MAIN097 |10 Interference 12 mo|−1.6(−1.8 to−1.5) /−1.6(−1.8 to−1.5) /−1.2(−1.3 to−1.0)|−0.5(−0.7 to−0.3) /−0.5(−0.7 to−0.3) /0.0(−0.2 to 0.2)|<.001|−0.26(−0.25 to 0.01) /−0.37(−0.36 to−0.11) /−0.12(−0.12 to 0.12)|
| MAIN098 |10 Social 3 mo|1.5(1.0 to 2.1) /2.2(1.7 to 2.7) /0.7(0.3 to 1.2)|0.8(0.0 to 1.5) /1.5(0.8 to 2.2) /0.7(−0.0 to 1.4)|<.001|0.12(0.23 to 0.11) /0.01(0.12 to−0.00) /0.20(0.29 to 0.19)|
| MAIN099 |10 Social 6 mo|2.2(1.6 to 2.8) /2.5(2.0 to 3.1) /1.0(0.5 to 1.5)|1.2(0.4 to 1.9) /1.5(0.8 to 2.2) /0.3(−0.4 to 1.1)|<.001|0.18(0.23 to 0.05) /0.06(0.11 to−0.06) /0.26(0.30 to 0.15)|
| MAIN100 |10 Social 12 mo|2.6(2.0 to 3.2) /2.7(2.2 to 3.3) /1.4(0.8 to 1.9)|1.3(0.5 to 2.1) /1.4(0.6 to 2.1) /0.1(−0.7 to 0.9)|.001|0.19(0.21 to 0.01) /0.07(0.09 to−0.10) /0.27(0.28 to 0.12)|
| MAIN101 |10 Physical 3 mo|1.4(1.1 to 1.8) /1.7(1.4 to 2.1) /1.0(0.7 to 1.4)|0.4(−0.1 to 0.9) /0.7(0.2 to 1.2) /0.3(−0.2 to 0.8)|.02|0.09(0.16 to 0.07) /−0.02(0.05 to−0.04) /0.16(0.22 to 0.15)|
| MAIN102 |10 Physical 6 mo|2.0(1.6 to 2.4) /1.8(1.4 to 2.1) /1.4(1.0 to 1.7)|0.6(0.1 to 1.2) /0.4(−0.1 to 0.9) /−0.3(−0.8 to 0.3)|.05|0.15(0.09 to−0.06) /0.02(−0.03 to−0.18) /0.22(0.16 to 0.05)|
| MAIN103 |10 Physical 12 mo|2.2(1.8 to 2.7) /2.1(1.7 to 2.5) /1.3(0.9 to 1.7)|0.9(0.3 to 1.5) /0.8(0.2 to 1.4) /−0.1(−0.7 to 0.5)|.004|0.20(0.18 to−0.03) /0.07(0.04 to−0.16) /0.27(0.25 to 0.09)|
| MAIN104 |11 PGIC pain 3 mo|2.2(2.1 to 2.3) /2.0(1.9 to 2.1) /2.9(2.8 to 3.0)|−0.7(−0.8 to−0.6) /−0.9(−1.0 to−0.8) /−0.2(−0.3 to−0.1)|<.001|−0.62(−0.81 to−0.19) /−0.62(−0.76 to−0.25) /−0.37(−0.51 to−0.05)|
| MAIN105 |11 PGIC pain 6 mo|2.2(2.1 to 2.3) /2.1(2.0 to 2.2) /2.8(2.7 to 2.9)|−0.6(−0.8 to−0.5) /−0.7(−0.8 to−0.5) /−0.1(−0.2 to 0.1)|<.001|−0.54(−0.59 to−0.05) /−0.55(−0.60 to−0.16) /−0.29(−0.33 to 0.06)|
| MAIN106 |11 PGIC pain 12 mo|2.2(2.1 to 2.3) /2.2(2.1 to 2.4) /2.8(2.7 to 2.9)|−0.6(−0.8 to−0.5) /−0.6(−0.7 to−0.4) /0.1(−0.1 to 0.2)|<.001|−0.55(−0.50 to 0.05) /−0.57(−0.54 to−0.08) /−0.29(−0.25 to 0.14)|
| MAIN107 |11 PGIC general 3 mo|2.0(1.9 to 2.1) /1.6(1.5 to 1.7) /2.7(2.6 to 2.8)|−0.7(−0.8 to−0.6) /−1.1(−1.2 to−1.0) /−0.4(−0.5 to−0.3)|<.001|−0.66(−1.04 to−0.38) /−0.66(−0.98 to−0.42) /−0.40(−0.67 to−0.18)|
| MAIN108 |11 PGIC general 6 mo|2.1(2.0 to 2.2) /1.8(1.7 to 1.9) /2.5(2.5 to 2.6)|−0.5(−0.6 to−0.3) /−0.7(−0.9 to−0.6) /−0.2(−0.4 to−0.1)|<.001|−0.46(−0.69 to−0.24) /−0.50(−0.70 to−0.32) /−0.24(−0.41 to−0.07)|
| MAIN109 |11 PGIC general 12 mo|2.0(1.9 to 2.1) /1.9(1.8 to 2.0) /2.6(2.5 to 2.7)|−0.6(−0.7 to−0.4) /−0.7(−0.8 to−0.5) /−0.1(−0.3 to 0.0)|<.001|−0.53(−0.64 to−0.11) /−0.58(−0.67 to−0.22) /−0.28(−0.36 to 0.03)|

## Footnotes, figures, adverse events and remaining matching relationships

| Key | Exact source location | Complete relationships/definitions |
|---|---|---|
| MAIN110 | p.9 Table 2 footnotes a–i | a: Unadjusted results in eTable 9, Supplement 4. b: Modified Poisson/GEE binary adjusted means at mean covariate distribution. c: Omnibus Wald test across 3 groups; pairwise comparisons only if P<.05. d: NNT for 1 additional ≥30% response = 1/adjusted proportion difference. e: If absolute risk difference CI contains zero, NNT includes infinity: positive lower limit to infinity and negative upper limit to negative infinity (number needed to harm). f: Severity, 11-item mean, 0–10, ≥30% improvement. g: Primary time point. h: Intensity, 4-item mean, 0–10, ≥30% improvement. i: Interference, 7-item mean, 0–10, ≥30% improvement. |
| MAIN111 | p.11 Table 3 footnotes a–i | a: Unadjusted results in eTables 10 and 11, Supplement 4. b: Linear regression/GEE adjusted group means and differences at mean covariates. c: Omnibus Wald test across 3 groups; pairwise comparisons only if P<.05 under least significant difference. d: SMD = adjusted difference/SD of change in UC at given time. e: 3-month primary time point. f: Social PROMIS, 4 items each 1–5, T score mean 50, SD 10, higher is better; ≤40 moderate (40–30) or severe (<30) limitations. g: Physical PROMIS, 6 items each 1–5, same T score and cut points. h and i: PGIC pain and general, 1 item each, scale 1–7: 1 much better, 2 moderately better, 3 a little better, 4 no change, 5 a little worse, 6 moderately worse, 7 much worse; higher indicates worsening. |
| MAIN112 | p.7 Table 1 footnotes a–i | a: EHR/ICD-10-CM diagnoses. b: Self-reported sex, using EHR if missing. c: Missing values excluded from denominators. d: Self-report. e: Hispanic regardless of other selections; multiple races recategorized as multiple. f: Rural census tracts use 2010 RUCA codes 4–10; medically underserved census tracts have primary care or mental health shortage designation. g: Severity, 11-item mean, 0–10, higher is worse. h: Past-year ICD-10-CM musculoskeletal conditions: back, neck, limb/joint/arthritis, fibromyalgia, headache, orofacial/ear/TMJ, chest, general pain. i: Opioid fills ≥60 days supply in 90 days pre-randomization, 3 of 4 sites; Essentia unavailable. |
| MAIN113 | p.7 Table 1 footnotes j–q | j: PHQ-8 sum of 8 items each 0–3, total 0–24, higher is worse; cut points 10 moderate, 15 moderately severe, 20 severe. k: GAD-7 sum of 7 items each 0–3, total 0–21; higher is worse; cut points 5 mild, 10 moderate, 15 severe. l: PROMIS sleep 6 a, 6 items each 1–5, T mean 50 and SD 10, higher is worse; ≥60 moderate (60–70) or severe (>70). m: Charlson, 19 conditions, weights 1/2/3/6, sum 0–37; 0 none, higher is worse. n: Intensity, 4-item mean 0–10, higher is worse. o: Interference, 7-item mean 0–10, higher is worse. p: Social 4 a, 4 items each 1–5, T mean 50 and SD 10, higher is better; ≤40 moderate (40–30) or severe (<30) limitations. q: Physical 6 b, 6 items each 1–5, same T score and cut points. |
| MAIN114 | p.8 Figure 2 | Adjusted percentage with ≥30% reduction in severity versus months since randomization 3/6/12; 3 months labeled Primary; y-axis percentage ticks 0/10/20/30/40/50/60; series UC/PT/HC; whiskers 95% CIs; adjustment in Table 2 footnote b. No individual numerical response labels printed in plot; plotted means and CIs correspond to MAIN080–MAIN082. Observed counts UC 621/622/639, PT 542/547/583, HC 635/621/639. |
| MAIN115 | pp.7–8 Adverse Events | Hospitalized participants 183 (7.9%), 247 events; deaths 17 (0.7%). PT 55 participants (7.1%) with 81 events; HC 65 (8.4%) with 84 events; UC 63 (8.1%) with 82 events. Deaths PT 3 (0.4%), HC 7 (0.9%), UC 7 (0.9%). Corresponding randomized analysis-arm denominators 776/778/777, total 2331. No hospitalization or death identified as related or possibly related. Nonserious adverse events were not systematically collected; participant-initiated reports HC 16 (2.0%), PT 1 (0.1%), UC 0; majority in HC mild and unrelated. Adverse-event reports are distinct from hospitalized participants and hospitalization events. |
| MAIN116 | pp.8 and 12 Discussion, Limitations, Conclusions | Greater 3-month severity improvement in both active groups versus UC; HC greater than PT. Modest active benefits at 6 and 12 months, with no HC relative benefit at later points. Other pain, physical, social and global outcomes described as similar patterns over the year. Roughly 40% rural/underserved in discussion versus 44% in abstract/body and Table 1 MAIN051; lower PT adherence and follow-up. Missing outcome bias addressed with imputation and nonresponse weighting; potential bias may remain. Conclusion: greater severity reduction sustained 12 months versus UC. Article information p.12 has no additional trial numeric or inferential relationships; references pp.13–14 have no applicable units. |

## Complete matching and boundary notes

The trial-wide analysis population and treatment contrast are MAIN001/003/009/014/015/018/019; retain participant-level randomization and highest-level clustering when matching any model result. Binary primary matching uses MAIN002/004/005/080/114; secondary time-point severity MAIN081/082; intensity MAIN083–085; interference MAIN086–088. Continuous severity MAIN022/089–091; intensity MAIN092–094; interference MAIN095–097; social MAIN098–100; physical MAIN101–103; PGIC pain MAIN104–106; PGIC general MAIN107–109. Every complete row carries all three groups and all three contrasts. Narrative claims MAIN006/022/116 are mapped to the complete rows rather than selected comparisons.

Plans/supplements were outside this agent's assigned evidence units and were not independently reviewed. Main-paper pointers retained for cross-source matching: protocolSupplement 1; SAPSupplement 2; intervention descriptionSupplement 3; non-planresultsSupplement 4 eTables 1–7 missingness, eTable 9 unadjusted binary, eTables 10/11 unadjusted continuous, eFigure 1 session completion, eFigure 2 missingness; Supplement 5 additional baselines; Supplement 6 data sharing statement. No person-time or rate outcome, OR/HR, noninferiority/equivalence margin, printed regression coefficient standard error, or numeric test statistic appears in the assigned main units. These are explicit no-applicable categories, not omitted extraction.

Limitations: direct PDF/OCR executables were unavailable, covered by pinned PyMuPDF native extraction and eligible original source-page images. New fresh-required main units: none (14 reusable-backed units all freshly mapped). Scientific coverage gaps: none. Values are transcriptions, not diagnoses; all statistical calculations and inclusion decisions remain with assigned checkers. This artifact preserves the source's displayed precision and interval ordering.
