# Bounded quality-audit packet main_early

Mechanically copied complete assigned current-run evidence, with source filenames and PDF pages preserved. Links originally remain relative to their named original artifact; use exact supplied source path for authority. No selection by scientific outcome.

<!-- Original artifact/scope: extraction/main_quantitative_evidence.md -->

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

Sources: [p.10, printed p.601, Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11, printed p.602, continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All values below are as printed, with interval ordering/signs retained and confirmed visually. Linear regression/GEE adjusted randomized population average effects at mean covariates. Columns exactly group means PT/HC/UC, then adjusted mean difference PT−UC/HC−UC/HC−PT, omnibusP, then SMD PT−UC/HC−UC/HC−PT. Values in SMD columns are mapped by printed headings, not rearranged. Each estimate has its own printed 95%CI. Severity/intensity/interference units points 0–10, negativechange=improvement; PROMIS Tscorechange positive=improvement. PGIC pain/general headings say mean change but footnotes define status-since-study scale 1–7, higher = worse. Group counts shown once above outcome block: severity/intensity/interference 643/690/703; social 636/683/696; physical 639/684/699; bothPGIC640/687/702. Every 3 mo marked primary time pointe.

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


<!-- Original artifact/scope: pass1 main S001–S055 -->

# Bounded statistical pass2 input: main_early

Complete assigned pass1 records only; scope is disjoint by stable S ID. The complete ledger, screening log, recheck facts and excluded-observation packet remain required cross-lane inputs.


### S001

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN001/009/014/034; pp.1–5.
- Relationship: Randomization and analysis units.
- Printed inputs/method: Individual 1:1:1 randomized; strata sex, baseline severity, site, rural/underserved; GEE highest-level within-person or health-coach clustering; 12 coaches.
- Pass1 checks and conclusion: Design and correlation units are explicitly distinguished. No independent-samples assumption imposed; no clustering contradiction found.
- Pass2: PENDING



### S002

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN001/003/018/020/027/030–035; pp.1,4,5,8–11.
- Relationship: Analysis population and missingness denominators.
- Printed inputs/method: 2333 allocated minus 2 EHR-ineligible UC =2331 eligible analysis population; 776/778/777; any-follow-up643/690/703; inverse-probability weighting for no follow-up.
- Pass1 checks and conclusion: Counts reconcile with stated eligible ITT principle and weighting. Table model contributor counts differ from target randomized population without a conflict.
- Pass2: PENDING



### S003

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN002/004/005/011/080; pp.1–4,7–9.
- Relationship: Primary outcome definition and decision direction.
- Printed inputs/method: ≥30% decrease from baseline severity, 0–10 higher=worse, 3mo primary; 6/12 secondary. Active-vs-UC RR>1 favors improvement.
- Pass1 checks and conclusion: Scale, threshold, contrast and direction agree; superiority claim checked against all primary RRs. No noninferiority or equivalence rule applies.
- Pass2: PENDING



### S004

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN012/111–113; pp.3–4,7,11.
- Relationship: Secondary outcome construction and direction.
- Printed inputs/method: Intensity4 and interference7 items; PROMIS higher=better; PGIC1–7 higher=worse; all3/6/12mo.
- Pass1 checks and conclusion: Continuous changes and PGIC status-since-start distinguished; coherent stated linear analysis not questioned. Wording about PGIC change is not a new numerical result.
- Pass2: PENDING



### S005

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN013; p.4 Sample Size.
- Relationship: Sample size and power inputs.
- Printed inputs/method: 2331=777×3; 90% power; UC15%, active22.5%=15%+7.5%; RR1.5;80%retention;10000 modified-Poisson simulations; Fisher LSD.
- Pass1 checks and conclusion: 777×3=2331 and .225/.15=1.5 reproduce. Exact simulation power cannot be reconstructed without simulation data-generating specification, seed and fit/gate rules; no contradictory printed sample size established. No preferred method imposed.
- Pass2: PENDING



### S006

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN014/019/110; pp.4,9.
- Relationship: Primary GEE and test method.
- Printed inputs/method: Modified Poisson, independent working correlation, robust sandwich standard error, time/group/interaction; Wald omnibus across3 groups; two-sidedα=.05.
- Pass1 checks and conclusion: Stated model coherent with repeated binary measures and coaching cluster. No printed numeric test statistic or standard error; do not infer degrees of freedom or sandwich corrections.
- Pass2: PENDING



### S007

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN015/017; p.4.
- Relationship: Adjustment and secondary baseline variables.
- Printed inputs/method: Baseline severity, sex, site, rural/underserved, multisite pain, mental health; same structure plus secondary baseline.
- Pass1 checks and conclusion: Reported covariates are defined, model scope coherent. Plan comparisons assigned distinct shard; source does not require replacing adjustment with crude estimates.
- Pass2: PENDING



### S008

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN015/110/111; pp.4,9,11.
- Relationship: Adjusted group predictions and target estimand.
- Printed inputs/method: Covariates centered at mean values across participants; randomized population average effects.
- Pass1 checks and conclusion: All table tuples explicitly model-adjusted; crude ratios not substitute estimators. Predicted binary proportions and RRs reproduce their algebra within precision.
- Pass2: PENDING



### S009

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN017/111; pp.4,11.
- Relationship: Continuous model and contrast method.
- Printed inputs/method: Linear regression/GEE adjusted group mean, differences and SMD at eachtime; group/time/interaction structure.
- Pass1 checks and conclusion: All21 continuous rows checked for additive group contrast consistency with half-unit rounding; no qualifying group-mean/MD discrepancy.
- Pass2: PENDING



### S010

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN017/111; pp.4,11.
- Relationship: SMD definition and shared denominator.
- Printed inputs/method: Each SMD=adjusted MD / SD(change in UC) at the given outcome/time; positive common SD across3 contrasts; SD value unprinted.
- Pass1 checks and conclusion: Check sign and additive contrast identity without inferring SD magnitude; F-ST1-004. All63 SMD intervals checked; containment F-ST1-002, descending order F-ST1-003.
- Pass2: PENDING



### S011

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN016/110; pp.4,9.
- Relationship: NNT definition and interval rule.
- Printed inputs/method: NNT=1/adjusted response-proportion difference; if RD CI includes0, NNT includes infinity and negative NNH branch.
- Pass1 checks and conclusion: All27 points/intervals checked. F-ST1-001 containment; F-ST1-005 reciprocal display discrepancy; F-ST1-006 finite-NNT versus null-containing RR intervals. Exact RD CI method remains unprinted; alternatives retained.
- Pass2: PENDING



### S012

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN018; p.4.
- Relationship: Outcome imputation and weighting.
- Printed inputs/method: Nonignorable pattern-mixture for≥1follow-up; inverse probability missingness weighting for no follow-up; sensitivity analyses planned/conducted.
- Pass1 checks and conclusion: Sequential observation groups defined and nonoverlapping; no logical contradiction found from main. Supplement inferential details assigned report shard.
- Pass2: PENDING



### S013

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN018; p.4.
- Relationship: Missing covariate data.
- Printed inputs/method: Mean imputation stated for missing covariates.
- Pass1 checks and conclusion: Explicit internally coherent choice; categorical encoding details absent without a conflicting number or statement; not a finding.
- Pass2: PENDING



### S014

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN019/110/111; pp.4,9,11.
- Relationship: Confidence, sidedness and significance.
- Printed inputs/method: All tests2-sidedα=.05; 95%CIs; omnibus Wald across3groups.
- Pass1 checks and conclusion: No omnibus P treated as pairwise P; no inferred covariance or degrees of freedom. Each row's null pattern reviewed at stated level.
- Pass2: PENDING



### S015

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN013/019/110/111; pp.4,9,11.
- Relationship: Multiplicity and omnibus gate.
- Printed inputs/method: Fisher least significant difference; pairwise comparisons onlyif omnibusP<.05.
- Pass1 checks and conclusion: All30 row gates reviewed:29 printedP<.05; physical6=.05 has rounding interval[.045,.055], exact gate cannot be determined. No interim/stopping boundary printed in main.
- Pass2: PENDING



### S016

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN002/004/005/080; pp.1–2,7–9.
- Relationship: Abstract and Key Points primary inference.
- Printed inputs/method: HC32.0(29.3–35.0)%, PT26.6(23.4–30.2)%, UC20.8(18.0–24.0)%; RR1.54/1.28/1.20 with95%CIs excluding1.
- Pass1 checks and conclusion: All estimates, CIs, contrast direction and 3mo superiority match; no numerical mismatch between abstract and primary row.
- Pass2: PENDING



### S017

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN006/080–082/114/116; pp.1,7–9,12.
- Relationship: Severity longitudinal inference.
- Printed inputs/method: Bothactive-vs-UC significant at3/6/12; HC-vs-PT3mo significant,6/12not significant.
- Pass1 checks and conclusion: All9RR CIs have asserted null patterns. Figure series/95%CIs agree visually and display no additional printed estimate/test tuples.
- Pass2: PENDING



### S018

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN006/022/089–109/116; pp.1,7–12.
- Relationship: Secondary inference narrative and SMD copies.
- Printed inputs/method: Narrative3mo severity SMD−.26PT/−.36HC vsTable3−.25/−.34. Overallpatterns described significant benefits pain/function.
- Pass1 checks and conclusion: Copy gaps0/.01 relative0/.0294 meet display precision; no finding. Broad overall-pattern wording not read as a universal everycontrast test; excluded wording observation recorded once.
- Pass2: PENDING



### S019

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN035/114; pp.5,8–9.
- Relationship: Figure2 graph and contributor counts.
- Printed inputs/method: 3/6/12 severity adjusted means and95%CIs; UC621/622/639, PT542/547/583, HC635/621/639.
- Pass1 checks and conclusion: Every plotted group/time and whisker compared visually withTable2. Counts agree withFigure1; time-specific observations differ fromany-follow-up counts by definition.
- Pass2: PENDING



### S020

- Status: PASS_1_COMPLETE
- Scope and role: REPORT main, MAIN007/008/023–079/112/113/115/116; pp.2–8,12–14.
- Relationship: Remaining pages and nonapplicable methods.
- Printed inputs/method: BaselineTable1 has SD/IQR notCIs and noinferential P; adverse outcomes counts/no formaltests; reference-onlypp.13–14.
- Pass1 checks and conclusion: Numeric-only totals delegated numeric checker; no inferential tuples omitted. No HR/OR/rate/person-time, NI/equivalence, numeric interim/stopping, numeric standard error or numeric test statistic in main. BPI missing-item wording screened once.
- Pass2: PENDING



### S021

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — group adjusted estimates.
- Printed tuples: 26.6(23.4–30.2) / 32.0(29.3–35.0) / 20.8(18.0–24.0).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S022

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.28(1.06–1.55) / 1.54(1.30–1.82) / 1.20(1.03–1.40).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S023

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN080, Severity 3 mo — NNT construction and intervals.
- Printed tuples: 18(10–71) / 9(7–14) / 19(11–102).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING



### S024

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — group adjusted estimates.
- Printed tuples: 32.9(29.5–36.7) / 37.1(34.1–40.5) / 22.9(20.0–26.1).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S025

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.44(1.21–1.70) / 1.62(1.39–1.90) / 1.13(0.98–1.30).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S026

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN081, Severity 6 mo — NNT construction and intervals.
- Printed tuples: 10(7–19) / 8(6–11) / 24(12–186).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. HC–UC reciprocal point differs beyond half-unit tolerance: F-ST1-005. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S027

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — group adjusted estimates.
- Printed tuples: 35.9(32.4–39.7) / 38.3(36.8–39.9) / 27.1(24.1–30.5).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S028

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.32(1.13–1.54) / 1.41(1.25–1.59) / 1.07(0.96–1.19).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S029

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN082, Severity 12 mo — NNT construction and intervals.
- Printed tuples: 12(8–26) / 9(7–13) / 41(17–76).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S030

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — group adjusted estimates.
- Printed tuples: 24.3(21.2–27.8) / 27.0(24.0–30.5) / 17.7(15.1–20.7).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S031

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.37(1.12–1.69) / 1.53(1.26–1.86) / 1.11(0.93–1.33).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S032

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN083, Intensity 3 mo — NNT construction and intervals.
- Printed tuples: 16(10–43) / 11(8–20) / 37(14–57).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S033

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — group adjusted estimates.
- Printed tuples: 26.9(23.7–30.5) / 31.8(28.3–35.7) / 21.1(18.3–24.3).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S034

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.27(1.06–1.54) / 1.51(1.26–1.80) / 1.18(1.00–1.40).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S035

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN084, Intensity 6 mo — NNT construction and intervals.
- Printed tuples: 18(10–76) / 10(7–17) / 21(11–5524).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING



### S036

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — group adjusted estimates.
- Printed tuples: 32.1(28.7–35.8) / 33.7(31.2–36.3) / 26.4(23.4–29.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S037

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.21(1.03–1.43) / 1.28(1.11–1.47) / 1.05(0.92–1.20).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=.003 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S038

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN085, Intensity 12 mo — NNT construction and intervals.
- Printed tuples: 18(10–106) / 14(9–31) / 63(18–38).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Containment does not reconcile for contrast3: F-ST1-001. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S039

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — group adjusted estimates.
- Printed tuples: 30.6(27.3–34.4) / 35.6(33.7–37.6) / 23.4(20.5–26.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S040

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — between-group estimates and omnibus test.
- Printed tuples: 1.31(1.10–1.55) / 1.52(1.32–1.75) / 1.16(1.02–1.32).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S041

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN086, Interference 3 mo — NNT construction and intervals.
- Printed tuples: 14(9–40) / 9(7–12) / 21(12–100).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. No null-containing-RR/finite-NNT pattern requiring further review.
- Pass2: PENDING



### S042

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — group adjusted estimates.
- Printed tuples: 37.0(33.5–40.9) / 40.9(37.0–45.1) / 24.3(21.3–27.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S043

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — between-group estimates and omnibus test.
- Printed tuples: 1.52(1.30–1.79) / 1.68(1.43–1.98) / 1.10(0.96–1.27).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S044

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN087, Interference 6 mo — NNT construction and intervals.
- Printed tuples: 8(6–13) / 7(5–9) / 26(11–67).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. HC–UC reciprocal point differs beyond half-unit tolerance: F-ST1-005. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S045

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — group adjusted estimates.
- Printed tuples: 39.6(36.1–43.5) / 42.3(40.6–44.0) / 30.6(27.4–34.2).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S046

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — between-group estimates and omnibus test.
- Printed tuples: 1.29(1.12–1.49) / 1.38(1.23–1.55) / 1.07(0.97–1.18).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 RR estimates lies inside its ordered95%CI; RR directions and ratios of adjusted proportions reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S047

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.9, MAIN088, Interference 12 mo — NNT construction and intervals.
- Printed tuples: 12(8–25) / 9(7–13) / 39(16–79).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: modified Poisson/GEE, robust sandwich, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 NNT tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Reciprocal points reconcile or fall within display precision. Finite HC–PT NNT CI accompanies RR CI including1: F-ST1-006; RD interval method remains unspecified.
- Pass2: PENDING



### S048

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — group adjusted estimates.
- Printed tuples: -1.2(-1.3 to-1.0) / -1.2(-1.3 to-1.1) / -0.8(-0.9 to-0.6).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S049

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.4(-0.6 to-0.3) / -0.0(-0.2 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S050

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN089, Severity 3 mo — SMD construction and intervals.
- Printed tuples: -0.25(-0.28 to-0.02) / -0.34(-0.36 to-0.13) / -0.13(-0.15 to 0.08).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common positive UC-change-SD identity does not reconcile beyond display precision: F-ST1-004 (all20 affected outcome/time rows retained).
- Pass2: PENDING



### S051

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — group adjusted estimates.
- Printed tuples: -1.3(-1.4 to-1.1) / -1.4(-1.5 to-1.3) / -0.9(-1.0 to-0.8).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S052

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.5(-0.7 to-0.4) / -0.1(-0.3 to 0.1).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



### S053

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN090, Severity 6 mo — SMD construction and intervals.
- Printed tuples: -0.26(-0.34 to-0.08) / -0.36(-0.43 to-0.19) / -0.12(-0.19 to 0.04).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: All3 SMD tuples checked for point containment, endpoint order, effect direction, stated construction and interval compatibility. Point containment reconciles. Endpoint order reconciles. Common-SD/additivity discrepancies fall within display-precision tolerance; excluded row recorded.
- Pass2: PENDING



### S054

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — group adjusted estimates.
- Printed tuples: -1.5(-1.6 to-1.3) / -1.4(-1.6 to-1.3) / -1.1(-1.2 to-0.9).
- Tuple order: PT / HC / UC.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 group estimates lies inside its ordered95%CI. Binary percentages are in[0,100]; continuous scales/direction correspond to outcome definition. These are adjusted predictions, not crude sample means. No group estimate/interval finding.
- Pass2: PENDING



### S055

- Status: PASS_1_COMPLETE
- Scope and role: REPORT DOC-001 p.10, MAIN091, Severity 12 mo — between-group estimates and omnibus test.
- Printed tuples: -0.4(-0.6 to-0.2) / -0.4(-0.6 to-0.2) / 0.0(-0.2 to 0.2).
- Tuple order: PT–UC / HC–UC / HC–PT.
- Model/confidence/test inputs: linear regression/GEE, adjusted;95%CIs; two-sidedα=.05; source modelS006–S015.
- Pass1 checks: Each of all3 MD estimates lies inside its ordered95%CI; MD directions and contrasts of group means reconcile allowing printed precision. OmnibusP=<.001 is a3-group Wald test, not a pairwiseP. Printed omnibus gate is below.05. Pairwise null patterns checked without inventing pairwiseP, covariance or degrees of freedom.
- Pass2: PENDING



<!-- Original artifact/scope: statistics/parts/pass2_main_early.md -->

# Statistical pass 2 relationship update — main early

Fresh agent: `/root/stat2_main_early`, gpt-6.1-sol/high, FRESH_SPAWN. Assigned scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055. This part is owned by this agent; the coordinator performs the canonical merge.

Each record below uses the complete current `candidate_ledger.md` (C001–C017), `screening/inclusion_screen.md` (26 initial decisions), `verification/evidence_recheck.md` (17 facts), and `review_packets/checker_exclusions.md` (47 original rows), plus `review_packets/pass2_main_early_input.md`. Scope and contract read completely. These inputs are current-run evidence only. REPORT main is DOC-001; prospective protocol/SAP roles are PLAN; intervention/results/workbook roles are REPORT.

Direct sources: [main methods p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [main binary results p.9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), [main continuous results p.10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [continuation and definitions p.11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Other exact locations are named individually below. Current native text is a locator; directly inspected current exact-source renders control the comparisons. Visual pages: DOC-001 1,3,4,5,7,8,9,10,11,12; native text covers remaining main pages and reference-only material. Five fresh main renders use pinned PyMuPDF1.26.4,200dpi,CPU; their engine record is `preprocessing/stat2_main_early/engine_record.md`. Other renders are current-run exact-source derivatives and were only read.

Checks in every applicable tuple: point containment; endpoint order; scale/reference-group direction; matching count and denominator meaning; estimate construction; stated 95% confidence/two-sided .05 level; omnibus versus pairwise test identity; Fisher-LSD gate; report/plan and cross-report candidate implications. Precision uses every displayed input/output half-unit and remaining gap/absolute printed value≤.05 as the screen, except category1. No SE, degrees of freedom, covariance, exact Wald reference distribution, estimand mapping or interval algorithm is supplied by convention. No NI/equivalence rule applies and no numerical interim/stopping boundary is stated in these main relationships.

### S001

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S001; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.3–5: individual allocation, twelve coaches and highest-level GEE clustering reread; randomization unit and correlation unit are different explicitly stated quantities.
- Independent pass-2 calculation/logic: No additional count/model inconsistency. Coach count is not a cluster-randomization claim.
- Existing candidate and cross-lane implications: None.
- Unresolved definitions and limits: Exact cluster implementation/finite-sample sandwich correction not supplied; no numeric claim depends on importing either.
- New finding: None; no previously screened finding re-emitted.

### S002

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S002; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,4,5,9–11: allocation/eligible/any-follow-up/model contributor headers compared.
- Independent pass-2 calculation/logic: 2333−2=2331;776+778+777=2331;643+690+703=2036. Observed-at-time totals are subsets of any-follow-up and need not equal weighted target population.
- Existing candidate and cross-lane implications: C002 affects therapeutic adherence percentage only; C007 affects primary missing-data hierarchy; C015 concerns supplementary subset count convention, not these full-trial denominators.
- Unresolved definitions and limits: Actual weight/model matrices unavailable; different denominator types are explicitly defined and not substituted.
- New finding: None; no previously screened finding re-emitted.

### S003

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S003; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,3,7,9: primary severity threshold, baseline-to-three-month window and Table2 read.
- Independent pass-2 calculation/logic: ≥30% decrease on higher-worse scale means improvement; active/UC RR>1 favors active. Three primary intervals exclude1; stated superiority direction reconciles.
- Existing candidate and cross-lane implications: None beyond linked method candidates C005/C007; no new endpoint/status difference.
- Unresolved definitions and limits: No NI/equivalence margin applies.
- New finding: None; no previously screened finding re-emitted.

### S004

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S004; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.3,4,7,11: intensity/interference, PROMIS and both one-item PGIC scale footnotes read.
- Independent pass-2 calculation/logic: Pain decreases, functioning increases and PGIC lower scores denote benefit. Since-start PGIC item is identifiable from adjacent footnotes; no competing numerical assignment established.
- Existing candidate and cross-lane implications: C006 preserves planned/reported secondary adjustment; C016 addresses supplementary raw-summary identity.
- Unresolved definitions and limits: PGIC has no prerandomization change-impression baseline. Outcome-specific baseline adjustment applicability is retained in C006 rather than assumed.
- New finding: None; no previously screened finding re-emitted.

### S005

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S005; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 sample-size paragraph read.
- Independent pass-2 calculation/logic: 777×3=2331;15%+7.5 percentage points=22.5%;.225/.15=1.5. Source states10000 modified-Poisson simulations/Fisher LSD, so a normal two-proportion calculation is diagnostic only.
- Existing candidate and cross-lane implications: No additional candidate; original simulation exclusion retained.
- Unresolved definitions and limits: Full data-generating specification, random seed, joint gate/success criterion and simulation fit details absent;90% exact power cannot be independently rebuilt.
- New finding: None; no previously screened finding re-emitted.

### S006

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S006; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 model description and p.9 footnotes read.
- Independent pass-2 calculation/logic: Modified Poisson/GEE, independence working correlation and robust highest-level sandwich structure are explicitly coherent with repeated measures and coach clustering. Omnibus Wald differs from pairwise CI contrasts.
- Existing candidate and cross-lane implications: C005/C007 concern specification/primary-role comparisons, without changing this source-stated model family.
- Unresolved definitions and limits: No numerical standard error, test statistic, exact reference distribution, df or covariance supplied; none inferred.
- New finding: None; no previously screened finding re-emitted.

### S007

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S007; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 primary/secondary covariate descriptions reread, matched to complete ledger/recheck.
- Independent pass-2 calculation/logic: Six stated main factors plus secondary baseline adjustment are identified. Do not substitute crude ratios.
- Existing candidate and cross-lane implications: C005: prespecified age differs in report/plan/full supplement sets; C006: per-outcome baseline addition differs from explicit plan wording. Both remain present, without re-emission.
- Unresolved definitions and limits: Final per-outcome design matrices and prospective expanded specification absent; primary-factor inheritance is a source-grounded alternative.
- New finding: None; no previously screened finding re-emitted.

### S008

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S008; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 and Table2/3 footnotes pp.9/11 reread.
- Independent pass-2 calculation/logic: Covariates centered at means; model-adjusted predictions/contrasts target randomized population. Each Table2 RR point agrees with corresponding adjusted percentage ratio under half-unit bounds.
- Existing candidate and cross-lane implications: C005/C007 concern covariate and missing-data mapping; existing estimate construction observations C003/C004 retain their local arithmetic.
- Unresolved definitions and limits: Unrounded predictors/predictions absent. Model-based quantities are not equated with crude counts.
- New finding: None; no previously screened finding re-emitted.

### S009

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S009; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 linear GEE and pp.10–11 adjusted mean/MD headings reread.
- Independent pass-2 calculation/logic: One-decimal group means and MDs can satisfy additive contrasts within their rounding intervals. Positive/negative effect direction follows each scale; no independent-samples analysis imported.
- Existing candidate and cross-lane implications: C003/C010 concern SMD construction/containment, distinct from the compatible adjusted mean/MD displays; C006 adjustment mapping retained.
- Unresolved definitions and limits: Fitted linear-model covariance/unrounded means not supplied; no exact omnibus P reconstructed.
- New finding: None; no previously screened finding re-emitted.

### S010

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S010; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 common UC-change SD definition; pp.10–11 SMD columns/footnote d reread.
- Independent pass-2 calculation/logic: Positive common denominator requires sign preservation and a+c=b. Severity3 gap .025/.34=.073529; severity6 HC−PT gap .005/.12=.041667 when recomputing from other two SMDs. Direct interval containment and ordering reviewed separately.
- Existing candidate and cross-lane implications: C003 retains twenty construction rows; C010 retains fourteen outside-interval tuples. F-ST1-003 descending-order-only observation already screened CONTEXT_RESOLVES and is not re-emitted.
- Unresolved definitions and limits: Exact UC-change SDs, unrounded contrasts and CI construction absent. No separate fitted contrast assignment or covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S011

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S011; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 reciprocal definition and p.9 all27 NNT tuples/footnotes read.
- Independent pass-2 calculation/logic: NNT=100/percentage-point difference. All points/endpoints ordered except existing containment63(18–38). Two local reciprocal gaps remain>.05; six matched RR/NNT null readings remain different.
- Existing candidate and cross-lane implications: C004 reciprocal points; C008 RR/NNT null-coverage ambiguity; C009 point containment. Distinct rules retained; no duplicate new finding.
- Unresolved definitions and limits: Risk-difference CI method/endpoints, integer convention, common covariance and parameter-specific analysis mapping absent. Different interval constructions remain alternatives.
- New finding: None; no previously screened finding re-emitted.

### S012

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S012; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 imputation/weighting paragraph read.
- Independent pass-2 calculation/logic: ≥1 follow-up pattern-mixture group and no-follow-up inverse-probability weighting group partition observation categories; weighting does not create direct raw observations.
- Existing candidate and cross-lane implications: C007 retains role hierarchy against SAP; C012/C013/C014 supplementary primary missing-data model membership/coding/test implications read in full recheck.
- Unresolved definitions and limits: Imputation/weight model matrices not supplied. Plan amendment support for current approach remains explicit alternative.
- New finding: None; no previously screened finding re-emitted.

### S013

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S013; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 missing-covariate sentence read.
- Independent pass-2 calculation/logic: Mean imputation is expressly stated and internally coherent. Encoding choices alone do not create a reproduced numeric or method contradiction.
- Existing candidate and cross-lane implications: No additional candidate.
- Unresolved definitions and limits: Categorical covariate coding under mean imputation unprinted; do not infer an encoding or propose a different method.
- New finding: None; no previously screened finding re-emitted.

### S014

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S014; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 and pp.9/11 inference footnotes read.
- Independent pass-2 calculation/logic: Two-sidedα=.05,95%CIs and three-group omnibus Wald explicitly identified. Pairwise intervals not treated as identical to omnibus P; no source-level pairwise P supplied.
- Existing candidate and cross-lane implications: C008/C009/C010 retain interval implications; C014 current supplementary interval/P conflicts read, not added to unrelated main rows.
- Unresolved definitions and limits: Exact df/covariance/test statistics/standard errors absent; pairwise P values not reconstructed.
- New finding: None; no previously screened finding re-emitted.

### S015

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S015; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.4 sample-size multiplicity and pp.9/11 Fisher-LSD footnotes; physical6 P=.05 on p.10 read.
- Independent pass-2 calculation/logic: All30 omnibus gates checked at printed precision;29<.05. Physical6 P interval[.045,.055] permits P<.05, so no reproduced gate breach. Omnibus and pairwise null patterns need not match.
- Existing candidate and cross-lane implications: No new multiplicity candidate; screened rounding observation retained.
- Unresolved definitions and limits: Unrounded physical6 omnibus P unavailable. No numeric interim/stopping boundary or NI/equivalence rule printed here.
- New finding: None; no previously screened finding re-emitted.

### S016

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S016; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.1 abstract, p.2 Key Points and p.9 primary row matched.
- Independent pass-2 calculation/logic: 32.0/26.6/20.8 and RR1.54/1.28/1.20 with their95%CIs match corresponding body estimates/contrasts; each primary RR CI excludes1.
- Existing candidate and cross-lane implications: No additional copy/significance issue; C005/C007 method-specification implications remain distinct.
- Unresolved definitions and limits: Pairwise P values are not supplied; absence does not conflict with CI-based superiority statements.
- New finding: None; no previously screened finding re-emitted.

### S017

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S017; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.1,7–9,12 longitudinal narrative, Figure2 and Table2 severity rows read.
- Independent pass-2 calculation/logic: All six active/UC CIs exclude1; HC/PT3 excludes1,6/12 include1. Narrative uses corresponding primary-response inferential direction; no equivalence conclusion asserted.
- Existing candidate and cross-lane implications: C008 preserves finite NNT/null-containing HC/PT intervals at6/12; this does not alter correctly matched RR narrative.
- Unresolved definitions and limits: Figure has no extra printed test tuple; no covariance inferred from graph.
- New finding: None; no previously screened finding re-emitted.

### S018

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S018; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.7 narrative SMD−.26/−.36 and p.10 severity3−.25/−.34 read; pp.1,7–12 overall benefit text read.
- Independent pass-2 calculation/logic: Half-unit copy intervals touch/overlap forPT;HC gap.01/.34=.029412≤.05. Overall-pattern wording is not an explicit every-contrast significance claim.
- Existing candidate and cross-lane implications: C003 concerns within-Table3 construction, independently of these screened copy differences. No new narrative finding.
- Unresolved definitions and limits: Wording scope is not resolved by assuming a universal claim; wording doubt screened as specified.
- New finding: None; no previously screened finding re-emitted.

### S019

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S019; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.5 Figure1, p.8 Figure2 and p.9 Table2 matched.
- Independent pass-2 calculation/logic: All nine adjusted severity points/95%whiskers visually agree with Table2; contributor counts UC621/622/639,PT542/547/583,HC635/621/639 match Figure1. Time-specific observed counts differ by definition from any-follow-up.
- Existing candidate and cross-lane implications: No new count/figure issue. C015 pertains a different supplementary subgroup header.
- Unresolved definitions and limits: No numerical graph-only CI endpoint printed; visual agreement is not a pixel-derived exact test.
- New finding: None; no previously screened finding re-emitted.

### S020

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S020; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main pp.2–8,11–14 baseline/adverse results/scoring/remaining material revisited through native text and relevant renders.
- Independent pass-2 calculation/logic: Baseline SD/IQR labels distinct from inferential CIs; adverse events are descriptive. No HR/OR/rate/person-time, NI/equivalence or numerical SE/test-statistic/stopping tuple introduced in remaining main material.
- Existing candidate and cross-lane implications: C002 count/percentage issue retained; no additional inferential relationship hidden in baseline/reference material.
- Unresolved definitions and limits: All11-item versus minimum-item wording is identifiable instrument-scoring context; no reported score contradiction established.
- New finding: None; no previously screened finding re-emitted.

### S021

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S021; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 group adjusted percentages inPT/HC/UC order: 26.6(23.4–30.2),32.0(29.3–35.0),20.8(18.0–24.0); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S022

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S022; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 PT/UC,HC/UC,HC/PTRRs: 1.28(1.06–1.55),1.54(1.30–1.82),1.20(1.03–1.40); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. All3 exclude1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S023

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S023; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity3 PT/UC,HC/UC,HC/PTNNTs: 18(10–71),9(7–14),19(11–102); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None; point/interval checks reconcile.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S024

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S024; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 group adjusted percentages inPT/HC/UC order: 32.9(29.5–36.7),37.1(34.1–40.5),22.9(20.0–26.1); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S025

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S025; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 PT/UC,HC/UC,HC/PTRRs: 1.44(1.21–1.70),1.62(1.39–1.90),1.13(.98–1.30); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S026

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S026; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity6 PT/UC,HC/UC,HC/PTNNTs: 10(7–19),8(6–11),24(12–186); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C004: HC/UC37.1−22.9→NNT[6.993007,7.092199] versus8[7.5,8.5],gap.407801/8=.050975; C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S027

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S027; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 group adjusted percentages inPT/HC/UC order: 35.9(32.4–39.7),38.3(36.8–39.9),27.1(24.1–30.5); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S028

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S028; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 PT/UC,HC/UC,HC/PTRRs: 1.32(1.13–1.54),1.41(1.25–1.59),1.07(.96–1.19); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S029

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S029; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Severity12 PT/UC,HC/UC,HC/PTNNTs: 12(8–26),9(7–13),41(17–76); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S030

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S030; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 group adjusted percentages inPT/HC/UC order: 24.3(21.2–27.8),27.0(24.0–30.5),17.7(15.1–20.7); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S031

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S031; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 PT/UC,HC/UC,HC/PTRRs: 1.37(1.12–1.69),1.53(1.26–1.86),1.11(.93–1.33); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S032

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S032; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity3 PT/UC,HC/UC,HC/PTNNTs: 16(10–43),11(8–20),37(14–57); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1;PT/UC reciprocal gap.115385/16=.007212 screens out.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S033

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S033; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 group adjusted percentages inPT/HC/UC order: 26.9(23.7–30.5),31.8(28.3–35.7),21.1(18.3–24.3); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S034

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S034; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 PT/UC,HC/UC,HC/PTRRs: 1.27(1.06–1.54),1.51(1.26–1.80),1.18(1.00–1.40); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT lower endpoint is printed1.00. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S035

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S035; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity6 PT/UC,HC/UC,HC/PTNNTs: 18(10–76),10(7–17),21(11–5524); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None additional; HC/PT RR lower1.00 is rounded boundary and no pairwiseP printed. Finite NNT large upper limit is not itself a conflicting test.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S036

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S036; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 group adjusted percentages inPT/HC/UC order: 32.1(28.7–35.8),33.7(31.2–36.3),26.4(23.4–29.8); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S037

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S037; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 PT/UC,HC/UC,HC/PTRRs: 1.21(1.03–1.43),1.28(1.11–1.47),1.05(.92–1.20); omnibusP.003; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S038

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S038; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Intensity12 PT/UC,HC/UC,HC/PTNNTs: 18(10–106),14(9–31),63(18–38); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C009:63>38;C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S039

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S039; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 group adjusted percentages inPT/HC/UC order: 30.6(27.3–34.4),35.6(33.7–37.6),23.4(20.5–26.8); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S040

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S040; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 PT/UC,HC/UC,HC/PTRRs: 1.31(1.10–1.55),1.52(1.32–1.75),1.16(1.02–1.32); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. All3 exclude1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: No additional tuple-specific candidate.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S041

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S041; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference3 PT/UC,HC/UC,HC/PTNNTs: 14(9–40),9(7–12),21(12–100); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: None; point/interval checks reconcile.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S042

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S042; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 group adjusted percentages inPT/HC/UC order: 37.0(33.5–40.9),40.9(37.0–45.1),24.3(21.3–27.6); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S043

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S043; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 PT/UC,HC/UC,HC/PTRRs: 1.52(1.30–1.79),1.68(1.43–1.98),1.10(.96–1.27); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S044

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S044; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference6 PT/UC,HC/UC,HC/PTNNTs: 8(6–13),7(5–9),26(11–67); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C004:HC/UC40.9−24.3→NNT[5.988024,6.060606] versus7[6.5,7.5],gap.439394/7=.062771;C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S045

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S045; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 group adjusted percentages inPT/HC/UC order: 39.6(36.1–43.5),42.3(40.6–44.0),30.6(27.4–34.2); direct render reread.
- Independent pass-2 calculation/logic: Each point is contained, all endpoints ordered, rates in[0,100]. Source model-adjusted prediction definition preserved; count denominator is not substituted.
- Existing candidate and cross-lane implications: C005/C007 concern specification/analysis role; no new tuple-specific inconsistency.
- Unresolved definitions and limits: Unrounded adjusted predictions absent; no exact SE or raw-count identity imposed.
- New finding: None; no previously screened finding re-emitted.

### S046

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S046; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 PT/UC,HC/UC,HC/PTRRs: 1.29(1.12–1.49),1.38(1.23–1.55),1.07(.97–1.18); omnibusP<.001; direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered; adjusted rate ratios reconcile within half-unit precision. active/UC exclude1;HC/PT includes1. OmnibusP passes the Fisher-LSD gate and is a3-group test, not a pairwiseP.
- Existing candidate and cross-lane implications: C008 retains corresponding RR/NNT null-coverage ambiguity; no new RR/P assertion.
- Unresolved definitions and limits: No pairwiseP, covariance, df or exact contrast SE supplied; these are not inferred.
- New finding: None; no previously screened finding re-emitted.

### S047

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S047; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.9 Table2 Interference12 PT/UC,HC/UC,HC/PTNNTs: 12(8–25),9(7–13),39(16–79); p.4 reciprocal rule/direct renders reread.
- Independent pass-2 calculation/logic: Every tuple's point containment, endpoint order, direction and reciprocal point checked with percentage±.05/integer±.5; findings are only existing implications below. Other reciprocal gaps≤.05 screened as one precision pattern.
- Existing candidate and cross-lane implications: C008:HC/PT finite interval vsRR including1.
- Unresolved definitions and limits: RD interval endpoints/construction, integer convention and any separate RR/RD mapping unprinted. Different parameter-specific interval methods retained; no joint covariance inferred.
- New finding: None; no previously screened finding re-emitted.

### S048

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S048; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 adjustedPT−1.2(−1.3,−1.0),HC−1.2(−1.3,−1.1),UC−.8(−.9,−.6); direct render reread.
- Independent pass-2 calculation/logic: Points contained, endpoints ordered, lower-worse pain decreases indicate benefit; one-decimal mean/MD arithmetic compatible.
- Existing candidate and cross-lane implications: No new group tuple issue; C006 adjustment specification applies.
- Unresolved definitions and limits: Unrounded adjusted means/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S049

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S049; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 MDPT/UC−.4(−.6,−.2),HC/UC−.4(−.6,−.3),HC/PT−0.0(−.2,.1),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered, directions agree. Group mean differences andMDs have overlapping rounding intervals. Active/UC CIs exclude0;HC/PT includes0;omnibus gate met.
- Existing candidate and cross-lane implications: No newMD/test candidate;C003 concerns paired SMDs.
- Unresolved definitions and limits: Exact df,covariance,SE andpairwiseP unprinted; not inferred.
- New finding: None; no previously screened finding re-emitted.

### S050

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S050; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity3 SMD−.25(−.28,−.02),−.34(−.36,−.13),−.13(−.15,.08),contrastPT/UC,HC/UC,HC/PT;direct render reread.
- Independent pass-2 calculation/logic: Contained/ordered;contrast signs follow pain reduction. Common-SD identityHC/UC=PT/UC+HC/PT predicts[−.390,−.370]vsprinted[−.345,−.335],gap.025/.34=.073529.
- Existing candidate and cross-lane implications: ExistingC003 includes this exact row; no re-emission.
- Unresolved definitions and limits: Actual UC-changeSD/unroundedMD/SMD/interval construction absent.
- New finding: None; no previously screened finding re-emitted.

### S051

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S051; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 adjustedPT−1.3(−1.4,−1.1),HC−1.4(−1.5,−1.3),UC−.9(−1.0,−.8);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered, higher-worse pain reduction direction coherent. Group mean/contrast rounding feasible.
- Existing candidate and cross-lane implications: No newgroup tuple issue;C006 applies.
- Unresolved definitions and limits: Unrounded adjustedmeans/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S052

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S052; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 MD−.4(−.6,−.2),−.5(−.7,−.4),−.1(−.3,.1),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;groupmeancontrast roundingfeasible. Active/UC exclude0;HC/PT includes0;three-group omnibusgate met.
- Existing candidate and cross-lane implications: No newMD/testcandidate;C003 reference row construction checked inS053.
- Unresolved definitions and limits: Exact SE/df/covariance/pairwiseP absent;not inferred.
- New finding: None; no previously screened finding re-emitted.

### S053

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S053; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity6 SMD−.26(−.34,−.08),−.36(−.43,−.19),−.12(−.19,.04);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;additiveHC/PT fromotherSMDs[−.110,−.090]vs[−.125,−.115],gap.005/.12=.041667≤.05. MD/SMDscalingHC/PT gap.001429/.12=.011905≤.05. This row is precision-compatible.
- Existing candidate and cross-lane implications: C003 uses this reproducing reference row; original exclusionretained. No newcandidate.
- Unresolved definitions and limits: AbsoluteUC-changeSD unavailable; only scale-independent identities checked.
- New finding: None; no previously screened finding re-emitted.

### S054

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S054; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity12 adjustedPT−1.5(−1.6,−1.3),HC−1.4(−1.6,−1.3),UC−1.1(−1.2,−.9);direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;mean/MD roundingfeasible. Source pain direction coherent.
- Existing candidate and cross-lane implications: No newgroup issue;C003/C010 affectSMDcolumns in thisrow, assigned nextshard.
- Unresolved definitions and limits: Unroundedadjustedmeans/covariance absent.
- New finding: None; no previously screened finding re-emitted.

### S055

- Status: PASS_1_COMPLETE; PASS_2_COMPLETE
- Named inputs: assigned packet S055; complete ledger, screening log, mechanical recheck and all 47 checker exclusions named above.
- Source checks and printed evidence: REPORT main p.10 severity12 MD−.4(−.6,−.2),−.4(−.6,−.2),0.0(−.2,.2),omnibusP<.001;direct render reread.
- Independent pass-2 calculation/logic: Contained,ordered;groups/MDcontrast roundingfeasible. Active/UC exclude0;HC/PT includes0;omnibusgate met. MatchedSMDPT/UC CIincludes0 whereasMDCIexcludes0; this is an interval-scaling implication ofexistingSMDpattern.
- Existing candidate and cross-lane implications: ExistingC003/C010 preserve the SMDconstruction/containment. Coordinator alerted to maintain cross-columnCI implication; no duplicatefinding emitted.
- Unresolved definitions and limits: SMDinterval construction and jointMD/SMDcovariance unavailable; do not assume identicalconfidence construction.
- New finding: None; no previously screened finding re-emitted.

Completion: 55/55 assigned relationships explicitly PASS_2_COMPLETE. New findings0. The checker part separately records the seven consolidated apparent observations screened during this shard and the complete47-row original-exclusion revisit.



<!-- Original artifact/scope: checkers/parts/stat1_main.md -->

# Statistical Pass 1 — Main-Paper Shard

Runtime agent: /root/stat1_main; fresh gpt-6.1-sol/high. Exact scope: DOC-001 main REPORT, physical PDF pages 1–14; MAIN001–MAIN116; S001–S110. All 270 estimate–95% interval tuples and 30 omnibus tests reviewed; all 27 NNT and 63 SMD tuples included. Findings: 6 consolidated patterns. Excluded observations: 7. Each relationship is PASS_1_COMPLETE. This part does not adjudicate candidates.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Used current fresh main map, supplied main PDF native text and exact original rendered source pages; all tables and cited signs/order on pages 9–11 visually confirmed. No web or old review conclusions used. Supplement statistical rows and plan-internal relationships are disjoint peer assignments. Links below target the supplied main PDF. All compared locations have role REPORT; proposed primary relationship S_W and all relationships S_W.

### F-ST1-001

A Table 2 NNT point lies beyond its printed confidence interval.

- Exact locations and roles: REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, pain intensity at 12 months, health coach vs painTRAINER NNT column; see MAIN085 derived-family record S038.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 1.
- Printed values, rule and calculation: The tuple is 63 (95% CI, 18–38). A confidence interval must contain its point estimate. Here 63 > 38. Even half-unit intervals leave the point at least 62.5 and the upper endpoint at most 38.5, a gap of 24 (24/63 = 0.381). Category 1 is not screened by display precision.

- **Affected result or extracted value:** Health coach vs painTRAINER NNT for ≥30% pain-intensity improvement at 12 months.
- **Why context does not resolve it:** The printed point and interval fail the category-1 containment rule; reconstructing a possible intended endpoint does not resolve which interval to extract.
- Alternatives and missing definitions: A substituted interval endpoint, a point attached to another row or a differently derived interval could explain the display; no replacement value is inferred.
- Exact human question: What point estimate and 95% interval should a reader use for the 12-month pain-intensity health-coach vs painTRAINER NNT?

### F-ST1-002

Repeated Table 3 SMD points lie outside their printed intervals.

- Exact locations and roles: REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, severity 12 months, intensity 12 months, interference 12 months, physical functioning 6 and 12 months; REPORT [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 continuation, PGIC–pain at 12 months. Derived-family records: S056, S065, S074, S089, S092, S101.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 1.
- Printed values, rule and calculation: Fourteen printed tuples are listed below. For containment, compare the point with both interval endpoints; it lies beyond both in each tuple. Sorting the physical-function endpoints still does not contain the point. Examples: severity 12-month painTRAINER vs usual care −0.25 < −0.24; physical 6-month painTRAINER vs usual care 0.15 > 0.09; PGIC–pain 12-month painTRAINER vs usual care −0.55 < −0.50. These are direct category-1 observations without inferential-method assumptions; display precision cannot screen them.
| Outcome/time | Contrast | Printed SMD (95% CI) |
|---|---|---|
| Severity 12 mo | painTRAINER vs usual care plus | -0.25(-0.24 to 0.01) |
| Severity 12 mo | health coach vs usual care plus | -0.36(-0.35 to-0.12) |
| Intensity 12 mo | health coach vs usual care plus | -0.27(-0.26 to-0.12) |
| Interference 12 mo | painTRAINER vs usual care plus | -0.26(-0.25 to 0.01) |
| Interference 12 mo | health coach vs usual care plus | -0.37(-0.36 to-0.11) |
| Physical 6 mo | painTRAINER vs usual care plus | 0.15(0.09 to-0.06) |
| Physical 6 mo | health coach vs usual care plus | 0.02(-0.03 to-0.18) |
| Physical 6 mo | health coach vs painTRAINER | 0.22(0.16 to 0.05) |
| Physical 12 mo | painTRAINER vs usual care plus | 0.20(0.18 to-0.03) |
| Physical 12 mo | health coach vs usual care plus | 0.07(0.04 to-0.16) |
| Physical 12 mo | health coach vs painTRAINER | 0.27(0.25 to 0.09) |
| PGIC pain 12 mo | painTRAINER vs usual care plus | -0.55(-0.50 to 0.05) |
| PGIC pain 12 mo | health coach vs usual care plus | -0.57(-0.54 to-0.08) |
| PGIC pain 12 mo | health coach vs painTRAINER | -0.29(-0.25 to 0.14) |

- **Affected result or extracted value:** The fourteen standardized-effect points or intervals listed below, across severity, intensity, interference, physical functioning and PGIC–pain.
- **Why context does not resolve it:** The category-1 point-containment failure remains under either printed or sorted physical-function endpoint order; the immediate table does not identify an extractable replacement.
- Alternatives and missing definitions: Endpoints or point estimates might have been attached to different contrasts or time points. The SMD CI construction is not stated sufficiently to reconstruct replacements; no reordering or replacement is performed.
- Exact human question: Which SMD point and 95% interval belong together for each listed outcome, time point and contrast?

### F-ST1-003

The social-role and physical-function SMD interval endpoints descend throughout Table 3.

- Exact locations and roles: REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social-role functioning and physical functioning, all three time points and all three SMD columns: S077, S080, S083, S086, S089, S092.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route B.
- Printed values, rule and calculation: All eighteen intervals in the table below print their first limit above their second. For example, social role 3-month painTRAINER vs usual care is 0.12 (0.23 to 0.11): lower-limit rounding range [0.225,0.235] remains above upper-limit range [0.105,0.115], minimum order gap 0.110; relative to 0.23 this is 0.478. The smallest remaining order gap is physical 3-month health coach vs painTRAINER, 0.22 to 0.15: minimum gap 0.060, relative 0.273. Every row exceeds display tolerance. Reversing endpoint order is numerical interval reading rather than a symbol or wording slip.
| Outcome/time | painTRAINER vs usual care | Health coach vs usual care | Health coach vs painTRAINER |
|---|---|---|---|
| Social 3 mo | 0.12(0.23 to 0.11) | 0.01(0.12 to-0.00) | 0.20(0.29 to 0.19) |
| Social 6 mo | 0.18(0.23 to 0.05) | 0.06(0.11 to-0.06) | 0.26(0.30 to 0.15) |
| Social 12 mo | 0.19(0.21 to 0.01) | 0.07(0.09 to-0.10) | 0.27(0.28 to 0.12) |
| Physical 3 mo | 0.09(0.16 to 0.07) | -0.02(0.05 to-0.04) | 0.16(0.22 to 0.15) |
| Physical 6 mo | 0.15(0.09 to-0.06) | 0.02(-0.03 to-0.18) | 0.22(0.16 to 0.05) |
| Physical 12 mo | 0.20(0.18 to-0.03) | 0.07(0.04 to-0.16) | 0.27(0.25 to 0.09) |

- **Affected result or extracted value:** The ordered lower and upper limits for all eighteen social-role/physical-function standardized-effect intervals.
- **Why context does not resolve it:** Although descending order is visible, the surrounding table also contains incompatible SMD points and formulas (separate findings), so sorting does not establish which interval belongs to which effect. This bears directly on extraction of confidence limits.
- Alternatives and missing definitions: The endpoints might be globally reversed, or columns/limits may be misattached; sorting alone cannot address physical-function containment. No preferred CI method is proposed.
- Exact human question: What are the lower and upper SMD confidence limits, and their contrast assignments, for the listed social-role and physical-function rows?

### F-ST1-004

Printed SMDs do not reproduce the stated common usual-care change-SD construction.

- Exact locations and roles: REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), Statistical Analysis, SMD definition; REPORT [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 footnote d repeats it; REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 SMD/MD columns, all outcome-time rows except severity 6 months. Records S010 and twenty derived-family records listed in the inventory.
- Focus area: B and C.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 4.
- Printed values, rule and calculation: The source states SMD = adjusted between-group mean difference / SD of change among usual-care participants for that outcome/time. A positive shared denominator requires SMD(HC–PT) = SMD(HC–UC) − SMD(PT–UC). Each displayed SMD has half-unit ±0.005, so subtracting two allows ±0.010; the third has ±0.005. Seventeen rows fail beyond relative gap 0.05, listed below. Three more rows satisfy this additive identity but do not share a denominator with their printed MDs: severity 12 months, intensity 3 months, interference 12 months. From the PT–UC MD and SMD and the rounded-zero HC–PT MD (±0.05), the recomputed HC–PT SMD ranges are respectively [−0.03643,0.03643], [−0.043,0.043], [−0.02944,0.02944]; printed HC–PT SMDs are −0.11, −0.08, −0.12 (±0.005). Minimum gaps/printed magnitudes = 0.06857/0.11=0.623, 0.032/0.08=0.400, 0.08556/0.12=0.713. Also physical-function 3-month HC–UC MD 0.7 vs SMD −0.02; physical-function 6/12-month HC–PT MD −0.3/−0.1 vs SMD +0.22/+0.27; PGIC–pain 12-month HC–PT MD +0.1 vs SMD −0.29 reverse signs under any positive SD. These are exact algebra from the stated definition, not crude/model comparisons or approximate Wald diagnostics. Severity 6-month discrepancies are excluded once by precision.
| Outcome/time | Printed SMDs: PT–UC / HC–UC / HC–PT | Recomputed HC–PT interval from first two SMDs | Minimum gap / absolute printed HC–PT |
|---|---|---|---|
| Severity 3 mo | -0.25 / -0.34 / -0.13 | [-0.100, -0.080] | 0.025 / 0.13 = 0.192 |
| Intensity 6 mo | -0.17 / -0.27 / -0.04 | [-0.110, -0.090] | 0.045 / 0.04 = 1.125 |
| Intensity 12 mo | -0.16 / -0.27 / -0.03 | [-0.120, -0.100] | 0.065 / 0.03 = 2.167 |
| Interference 3 mo | -0.25 / -0.34 / -0.13 | [-0.100, -0.080] | 0.025 / 0.13 = 0.192 |
| Interference 6 mo | -0.27 / -0.37 / -0.14 | [-0.110, -0.090] | 0.025 / 0.14 = 0.179 |
| Social 3 mo | 0.12 / 0.01 / 0.2 | [-0.120, -0.100] | 0.295 / 0.20 = 1.475 |
| Social 6 mo | 0.18 / 0.06 / 0.26 | [-0.130, -0.110] | 0.365 / 0.26 = 1.404 |
| Social 12 mo | 0.19 / 0.07 / 0.27 | [-0.130, -0.110] | 0.375 / 0.27 = 1.389 |
| Physical 3 mo | 0.09 / -0.02 / 0.16 | [-0.120, -0.100] | 0.255 / 0.16 = 1.594 |
| Physical 6 mo | 0.15 / 0.02 / 0.22 | [-0.140, -0.120] | 0.335 / 0.22 = 1.523 |
| Physical 12 mo | 0.2 / 0.07 / 0.27 | [-0.140, -0.120] | 0.385 / 0.27 = 1.426 |
| PGIC pain 3 mo | -0.62 / -0.62 / -0.37 | [-0.010, 0.010] | 0.355 / 0.37 = 0.959 |
| PGIC pain 6 mo | -0.54 / -0.55 / -0.29 | [-0.020, -0.000] | 0.265 / 0.29 = 0.914 |
| PGIC pain 12 mo | -0.55 / -0.57 / -0.29 | [-0.030, -0.010] | 0.255 / 0.29 = 0.879 |
| PGIC general 3 mo | -0.66 / -0.66 / -0.4 | [-0.010, 0.010] | 0.385 / 0.40 = 0.963 |
| PGIC general 6 mo | -0.46 / -0.5 / -0.24 | [-0.050, -0.030] | 0.185 / 0.24 = 0.771 |
| PGIC general 12 mo | -0.53 / -0.58 / -0.28 | [-0.060, -0.040] | 0.215 / 0.28 = 0.768 |

- **Affected result or extracted value:** SMD points and their contrast assignments in twenty of the twenty-one continuous outcome/time rows.
- **Why context does not resolve it:** The supplied definition and table headings establish the denominator and comparisons, but the printed values do not reproduce them. A missing alternative standardization rule is the human question.
- Alternatives and missing definitions: Different contrast-specific standardizers, an outcome/time-column displacement, or SMDs from another analysis could produce different values; each differs from the printed shared-UC-SD definition and needs explicit mapping. Actual UC-change SD values are absent, but additivity/sign and the stated rounding bounds do not require their magnitude.
- Exact human question: Which adjusted mean differences, usual-care change SDs and contrast/time assignments produced the printed SMDs, and does the stated common-SD definition apply to every Table 3 row?

### F-ST1-005

Two NNT points exceed the display tolerance for the stated reciprocal formula.

- Exact locations and roles: REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), NNT definition; REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2 footnote d and health coach vs usual care NNT points for severity 6 months and interference 6 months; records S011, S026 and S044.
- Focus area: B and C.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 4.
- Printed values, rule and calculation: Severity at 6 months: adjusted percentages 37.1% and 22.9%, NNT 8. Half-unit percentage intervals give RD [0.141,0.143], reciprocal [6.993007,7.092199]; printed NNT interval [7.5,8.5], gap 0.407801, relative 0.050975. Interference at 6 months: 40.9% and 24.3%, NNT 7; RD [0.165,0.167], reciprocal [5.988024,6.060606]; printed NNT interval [6.5,7.5], gap 0.439394, relative 0.062771. The stated reciprocal method reproduces other rows or leaves them within the precision rule; these two are above 0.05. Full tuple checks preserved in the inventory.

- **Affected result or extracted value:** Health coach vs usual care NNT points for six-month severity and interference response.
- **Why context does not resolve it:** The method/display discrepancy is reproduced above the fixed precision threshold. A possible upward integer-rounding rule is retained as an alternative rather than silently added to the supplied formula.
- Alternatives and missing definitions: Rounding NNTs upward rather than to nearest integer yields 8 and 7 here and can reconcile the table. The source does not state that convention; no claim is made that the estimated risk difference itself differs.
- Exact human question: Were these NNTs rounded upward to whole participants, and what unrounded reciprocal values and display rule generated the reported points?

### F-ST1-006

Finite positive NNT intervals accompany null-containing RR intervals for the same contrasts.

- Exact locations and roles: REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, health coach vs painTRAINER, severity 6/12 months, intensity 3/12 months, interference 6/12 months; Table 2 footnotes b,d,e; REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), shared binary model and NNT definition. Records S026, S029, S032, S038, S044, S047.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route B.
- Printed values, rule and calculation: All six RR intervals include 1, while all six printed NNT intervals are finite and positive. RR=1 and risk difference=0 are the same equality-of-response null for these matched adjusted group responses. Footnote e explicitly requires an NNT interval including infinity, with a negative NNH branch, when its RD interval contains zero. Inverting the finite NNT intervals implies strictly positive RD intervals: severity 6 [1/186,1/12], severity 12 [1/76,1/17], intensity 3 [1/57,1/14], intensity 12 [1/38,1/18], interference 6 [1/67,1/11], interference 12 [1/79,1/16]. The observation is exact interval/null reading. Compatibility with a common confidence-set construction cannot be reproduced because the RD/NNT CI construction is not stated; different parameter-specific interval methods are an explicit alternative, not an inferred contradiction in a specific variance formula.
| Outcome/time | HC–PT RR (95% CI) | HC–PT NNT (95% CI) |
|---|---|---|
| Severity 6 mo | 1.13(0.98–1.30) | 24(12–186) |
| Severity 12 mo | 1.07(0.96–1.19) | 41(17–76) |
| Intensity 3 mo | 1.11(0.93–1.33) | 37(14–57) |
| Intensity 12 mo | 1.05(0.92–1.20) | 63(18–38) |
| Interference 6 mo | 1.10(0.96–1.27) | 26(11–67) |
| Interference 12 mo | 1.07(0.97–1.18) | 39(16–79) |

- **Affected result or extracted value:** The six HC–PT NNT intervals, whether they support a finite benefit interval and which limits an evidence extractor should record.
- **Why context does not resolve it:** The same table/source model prints opposite null coverage for the matched response contrasts and gives an infinity rule, but omits the RD confidence-interval method. Readers cannot determine whether different CI methods explain this or whether NNT limits need another assignment.
- Alternatives and missing definitions: RR and RD intervals may come from different valid interval constructions and have different finite-sample coverage; covariance, transformation and exact RD limits are not inferred. No pairwise P value is printed. The intensity 12-month point-containment issue is separately tracked in F-ST1-001.
- Exact human question: Which risk-difference confidence intervals and interval construction generated these six NNT intervals, and how should their null coverage be interpreted alongside the same-contrast RR intervals?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.10, Table 3 severity 6 months, SMDs −0.26/−0.36/−0.12 | Shared-SD additivity predicts HC–PT [−0.110,−0.090], printed half-unit [−0.125,−0.115]; gap .005/.12=.0417. MD/SMD shared-denominator rounding discrepancy is likewise below .05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.7 secondary narrative vs p.10 severity 3-month SMD row | Narrative −0.26/−0.36 vs table −0.25/−0.34: half-unit gaps0/.010, relative0/.0294. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.10 physical functioning 6-month omnibus P=.05 and footnote p.11 pairwise gate P<.05 | The printed P rounding interval[.045,.055] includes values that satisfy the stated gate; exact unrounded gate result cannot be determined. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.4 Sample Size | Exact 90% simulated power cannot be rebuilt without the complete simulation specification; 2331=777×3,7.5 percentage points andRR1.5 reconcile, with no contradicted sample size. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.11 Table 3 PGIC headings/footnotes | Mean change label versus a since-start-of-study global-impression scale: scale coding and outcome meaning are evident from adjacent footnotes. | TERMINOLOGY_OR_WORDING |
| REPORT main p.3 primary scoring and p.7 Table1 footnote g | Requirement of all4 intensity and at least4/7 interference items versus mean of11-item instrument wording does not establish a conflicting reported score. | TERMINOLOGY_OR_WORDING |
| REPORT main pp.1,7 secondary benefit narrative vs physical-function rows p.10 | Overall-pattern statements summarize benefits while individual physical-function contrasts vary in null coverage; whether wording means every contrast is not established. | TERMINOLOGY_OR_WORDING |

## Scope closure and limitations

All S001–S110 records have PASS_1_COMPLETE. Every Table 2/Table 3 tuple and row-level omnibus test was checked. Figure 2 matches severity rows at all three time points; the abstract and primary-result narrative agree with primary estimates and intervals. Method checks cover analysis units, population, model, adjustment, missingness, sidedness, confidence, multiplicity, inference direction and power arithmetic. Main pages13–14 contain only references. Numeric-only Table1/flow/adverse-event arithmetic remains the numeric review assignment, while analysis-population implications were reviewed here. No main inferential relationship omitted.

Named limitations: exact sample-size simulation cannot be recreated from printed inputs alone; numeric test statistics, standard errors, robust degrees of freedom, actual UC-change SDs and the RD/NNT interval construction are absent. No missing model detail alone was emitted. Supplement/PLAN inferential rows are peer scopes. Direct PDF tools were absent; pinned PyMuPDF fresh native text and supplied-source page images provided coverage. No new Python helper written. No candidate IDs or adjudications assigned.



<!-- Original artifact/scope: checkers/parts/stat2_main_early.md -->

# Statistical pass 2 — main early shard

Fresh specialist: `/root/stat2_main_early`; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN, distinct from every pass-1 runtime. Exact runtime ID is supplied by the coordinator spawn record for the execution manifest.

Assigned relationships: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055. Completed55/55 individually in `statistics/parts/pass2_main_early.md`. This checker part is bounded by the assigned S IDs. The coordinator merges all disjoint pass-2 parts; this is not a claim that the other S IDs were covered by this agent.

## Inputs and source checks

Read QUALITY_CONTROL_SCOPE.md and the complete1.6.2 review contract; complete current candidate ledgerC001–C017; all26 initial screening decisions; all17 mechanical recheck facts; all47 original checker excluded-observation rows; and the complete assigned packet. No legacy conclusion or web input used. The direct-source roles are content-based: main, results, intervention description and workbook REPORT; protocol/SAP PLAN.

Current-source main visual pages1,3,4,5,7,8,9,10,11,12 were read, alongside the current native main text for remaining baseline/reference material. Table2's27 group predictions,27RRs,27NNTs and local method/interval footnotes were reread; Table3's general common-SD method and relevant first severity rows were reread, with all existing SMD-pattern recheck facts reviewed. Native text was a locator, and source renders controlled printed value readings. Five fresh renders use pinned PyMuPDF1.26.4,200dpi,CPU; `preprocessing/stat2_main_early/engine_record.md` records them. Source and prior/current reused derivatives were preserved.

Direct sources: [mainp4 methods](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [mainp9 Table2](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), [mainp10 Table3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [mainp11 definitions](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

## Findings

No distinct new finding was emitted. Existing screened findings are not re-emitted. This result follows source-grounded checks, without a count target.

C002 remains the adherence numerator/denominator/percentage candidate. C003 retains twenty SMD construction rows, including severity3 in this shard; C004 retains two main reciprocal points and the supplementary reminder-letter point; C008 retains six RR/NNT null-coverage pairs; C009 retains63(18–38); C010 retains fourteen SMD containment tuples. C005/C006/C007 retain covariate/secondary adjustment/primary missing-data hierarchy comparisons, including source-grounded alternative amendment/inheritance readings. C011–C017 supplementary/workbook recheck implications were read in full; none supplies a distinct contradiction in these assigned main results.

All three primary RR intervals exclude1 and agree with stated benefit and abstract/body copies. Each of the27 binary group andRR tuples is contained and ordered. Adjusted prediction ratios agree withRR points under their half-unit bounds. All NNT points/intervals and reciprocal points were checked; the qualifying instances are alreadyC004/C008/C009. The physical6 omnibusP=.05 interval[.045,.055] permits the statedP<.05 gate; it is not a same-pair interval/P contradiction because the omnibus and pairwise hypotheses differ. SMD/MD columns have further null-coverage implications within existing construction/containment patterns; source data do not identify exact separate interval construction. The coordinator was alerted to maintain these implications in the later main shard.

## Existing screening decisions revisited

All26 decisions were reread, including seven SCREENED_OUT rows. Five duplicate decisions retain the included issue and every affected location: F-ST1-005/206→C004; F-ST1-203→C012; F-ST1-204→C013; F-ST1-601→C016. F-XS-001 remains terminology/operational-description wording without changed reported population. F-ST1-003 is descending endpoint order alone: sorting leaves the same two endpoint values; every outside-point occurrence already remainsC010 and no numeric sign/digit substitution is established. It is not an additional reproduced route-A category2 value slip; no prior screened finding was re-emitted.

The scope forbids removing interval/P or point-containment observations as rounding; C009/C010/C014 remain present, including null-adjacent endpoints. It permits removing non-category1 arithmetic gaps≤.05. C004's main reciprocal gaps .050975 and .062771 are retained above that threshold; C003's severity6 reference discrepancy is below it.

## Complete original exclusion revisit

Every original packet row is enumerated below with a local locator label. These labels are audit locators, not finding or candidate IDs. Repeated packet observations remain separately enumerated for proof of the47-row reread; the seven distinct main-shard apparent observations are listed once in the Excluded observations table.

| Original row locator | Original apparent issue | Original reason code | Independent pass-2 route-A/display-precision assessment |
|---|---|---|---|
| NUM1 | Pattern/follow-up counts | ROUNDING_OR_DISPLAY_PRECISION | Half-unit total gap1/2036=.000491;visit gap4.5/5449=.000826;no above-.05 within-display count conflict. |
| NUM2 | Copied baseline descriptives | ROUNDING_OR_DISPLAY_PRECISION | Copy gaps below.05; baseline-copy comparison additionally peripheral. C017 remains distinct within-cell percentage issue. |
| NUM3 | Other reciprocal NNT/SMD points | ROUNDING_OR_DISPLAY_PRECISION | Main intensity3 PT/UC gap.115385/16=.007212;reference severity6 SMD gap≤.05. C003/C004 above-threshold rows remain included. |
| NUM4 | eTables10/11 medians versus fitted MDs | CONDITIONAL_OR_UNREPORTED | No source equality between descriptive median and modeled mean established; does not supply category4 reproducing method. |
| NUM5 | TIDieR fidelity totals | CONDITIONAL_OR_UNREPORTED | 193+89+17=299;training total not provided, so1791+2350 is not asserted exhaustive4626 partition. No reproduced missing count. |
| NUM6 | Target versus contributor/weight totals | CONTEXT_RESOLVES | 2331 target,2036 participants and6108 visits are defined different quantities;no result/count is relabeled. |
| NUM7 | Roughly40% residence versus44% | CONTEXT_RESOLVES | Approximate prose does not replace numeric baseline extraction; no category2 printed-value slip established. |
| XS1 | Narrative/Table3 severity3 SMD copies | ROUNDING_OR_DISPLAY_PRECISION | PT half-unit intervals meet;HC gap.01/.34=.029412. |
| XS2 | Primary/sensitivity/unadjusted estimates | NOT_REPRODUCED | Different identified models/populations are not matching copies;C007 retains role conflict. |
| XS3 | eTable9 adjusted title/unadjusted notes | CONTEXT_RESOLVES | Immediate footnote and introduction identify unadjusted analysis; no printed numeric mismatch established. |
| XS4 | eTable10 mean/median wording | CONTEXT_RESOLVES | Raw changes labeled median/IQR; fitted contrasts explicitly mean/CI. UnlikeC016, no source-discrete raw-center contradiction established. |
| XS5 | Plan interference descriptor/time-cell wording | TERMINOLOGY_OR_WORDING | Named seven-item interference subscale and adjacent three-month timeframe identify intended quantity;no category5 status change. |
| XS6 | 140 versus454 onboarding calendar context | PERIPHERAL_COMPARISON | Same8/9/2021 boundary and explicit454/1877 analysis sizes;not a conflicting analysis-population denominator. |
| XS7 | Workbook468 versus471 patterns | ROUNDING_OR_DISPLAY_PRECISION | [470,472] vs[467.5,468.5] gap1.5/471=.003185≤.05. |
| XS8 | Unrepeated operational eligibility criteria | CONDITIONAL_OR_UNREPORTED | Main omission alone does not affirm inclusion of excluded participants or change a supplied analysis count. |
| XS9 | Moderator/mediator plan details | PERIPHERAL_COMPARISON | Ancillary plan-only timing/equation details do not change reported primary/key-secondary result or decision rule. |
| XS10 | PGIC and group/outcome names | TERMINOLOGY_OR_WORDING | Scale/group context immediately identifies same outcome/arms; no changed result assignment. |
| XS11 | Ancillary absent analyses | CONDITIONAL_OR_UNREPORTED | No absent analysis designated primary/key secondary in this report or claimed present; no category5 omission established. |
| MAIN1 | Severity6 shared-SD SMD additivity | ROUNDING_OR_DISPLAY_PRECISION | RecomputedHC/PT[−.110,−.090] vs[−.125,−.115],gap.005/.12=.041667≤.05;alternative choice of compared column also screened. |
| MAIN2 | Narrative/Table severity3 SMD copies | ROUNDING_OR_DISPLAY_PRECISION | PT gap0;HC gap.01/.34=.029412≤.05. |
| MAIN3 | Physical6 P=.05 versus pairwise gate | ROUNDING_OR_DISPLAY_PRECISION | [.045,.055] permits P<.05;omnibus gate not a same-pair interval/test contradiction. |
| MAIN4 | Simulated90% power reproduction | CONDITIONAL_OR_UNREPORTED | Explicit simulation algorithm incompletely specified;no contradictory printed n and no normal diagnostic method established to reproduce display. |
| MAIN5 | PGIC mean-change heading | TERMINOLOGY_OR_WORDING | Immediate since-start item/1–7 coding identifies quantity;no conflicting extracted numeric result. |
| MAIN6 | All11 versus minimum-item BPI wording | TERMINOLOGY_OR_WORDING | Instrument definition and scoring completeness rule do not establish contradictory reported score. |
| MAIN7 | Overall secondary benefit narrative | TERMINOLOGY_OR_WORDING | Overall-pattern wording does not assert significance for every individual contrast;do not elevate wording doubt. |
| REPORT1 | Follow-up patterns/workbook counts | ROUNDING_OR_DISPLAY_PRECISION | Same pattern asNUM1/XS7;above-half-unit but remaining relative gaps≤.05. |
| REPORT2 | Other supplementary NNT points | ROUNDING_OR_DISPLAY_PRECISION | Largest other gap.048611≤.05. C004 retains all above-threshold reciprocal points; no missing category4 occurrence identified from this row. |
| REPORT3 | eTable3 numeric CI-width/P diagnostics | CONDITIONAL_OR_UNREPORTED | Normal-Wald approximation alone lacks exact coefficient-test/df/CI rule;seven direct null/P conflicts retainedC014. No supported estimate/interval reproduction method for this extra diagnostic. |
| REPORT4 | Imputation coefficient clinical direction | CONDITIONAL_OR_UNREPORTED | Conditional imputation coefficients lack sign/estimand mapping to clinical responder direction;no direct source direction contradiction. |
| REPORT5 | Weight normalization sample size | CONTEXT_RESOLVES | Local2036 and3×2036=6108 identify scaling analysis size;target population remains separately2331. |
| REPORT6 | Base pain severity list omission | CONTEXT_RESOLVES | Narrative and both full models explicitly include it;no unidentified output model or unreported prespecified-analysis absence. |
| REPORT7 | eTable9 adjusted title | TERMINOLOGY_OR_WORDING | Immediate unadjusted statement/footnote identifies statistic;same observation asXS3, no numeric quantity change. |
| REPORT8 | eTable10 median versus mean effect | CONTEXT_RESOLVES | Raw median and GEE mean effect are distinct;no required algebraic equality. |
| REPORT9 | Virtual Coach labels | TERMINOLOGY_OR_WORDING | Clinical intervention names map immediately in three-arm context;no affected numeric attribution. |
| PLAN1 | Independent-proportion n diagnostics | CONDITIONAL_OR_UNREPORTED | Normal/continuity algorithms not stated;report states10000 modified-Poisson simulations. No same-display reproduction premise established. |
| PLAN2 | Relative change/response-ratio wording | TERMINOLOGY_OR_WORDING | Table explicitly defines active/UC ratio;rates/ratio arithmetic coherent. |
| PLAN3 | Interference row intensity description | TERMINOLOGY_OR_WORDING | Same cell names seven-item interference scale and30% reduction;no change to actual composite/status. |
| PLAN4 | Time measurement list omits3months | CONTEXT_RESOLVES | Adjacent timeframe and analytic text explicitly include3months;no prespecified analysis absent. |
| PLAN5 | Moderator6 versus3months | PERIPHERAL_COMPARISON | Ancillary plan-only comparison not altering reported primary/key-secondary result, sample size or decision rule. |
| PLAN6 | Mediator equation missing Z term | PERIPHERAL_COMPARISON | No supplied fitted mediator result;does not identify contradiction in reported primary/key-secondary model. |
| PLAN7 | Support baseline versus notification | CONTEXT_RESOLVES | Protocol expressly states notification survey serves as mediator baseline;source resolves origin. |
| PLAN8 | Eligibility amendment history | PERIPHERAL_COMPARISON | Historical/current version detail not an actual reported population-count conflict;amendment disclosed. |
| PLAN9 | Qualitative framework list counts | OUT_OF_FOCUS | Not participant/event/power/statistical decision counts;category3 does not apply. |
| PLAN10 | Routine safety chart review amendment | CONTEXT_RESOLVES | SAP explicitly removes routine hospitalization review and retains stated conditional/death review;procedural update disclosed. |
| RAW1 | Remaining fractional PGIC centers | ROUNDING_OR_DISPLAY_PRECISION | Nearest ordinary-median gap.05 gives relative.0172–.0313≤.05;five larger-gap cells alreadyC016. |
| RAW2 | Raw-arm numerical permutation | CONDITIONAL_OR_UNREPORTED | Model mean differences need not equal raw medians;21-row arithmetic permutation is diagnostic, not established arm mapping. |
| RAW3 | Physical6/12 omnibus reconstruction | CONDITIONAL_OR_UNREPORTED | Same-covariance normal-CI reconstruction depends on unstated jointCI/test rule/df. Category4 names estimate/interval reproduction;not a standalone omnibusP under assumed covariance. No.05 null conflict. |

No original row established an additional reproduced always-register observation. In particular, normal-Wald and joint-Wald examples remain labelled diagnostics; a method establishing a shared exact confidence/test construction is not supplied. No degrees of freedom, covariance or estimand mapping is inferred. A reproducing stated estimate/interval method was used for C003/C004; the additional standalone omnibusP diagnostic does not satisfy that premise merely by fitting selected rows.

## Excluded observations

Only apparent issues independently considered and not emitted in the assigned main relationship scope are listed. Reconciled checks remain in the individual S records. Existing included candidate observations are cross-referenced above, not duplicated here.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp10 severity6 shared-SD SMDs−.26/−.36/−.12 | HC/PT implied[−.110,−.090] versus printed[−.125,−.115], gap.005/.12=.041667≤.05; MD/SMD scaling gap likewise≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp7 narrative versusp10 severity3 SMDs | PT copy half-unit intervals touch;HC−.36 versus−.34 gap.01/.34=.029412≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp10 physical6 omnibusP=.05 versusp11 pairwise gateP<.05 | UnroundedP can be within[.045,.05), satisfying the gate; omnibus versus pairwise CIs are different hypotheses. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp4 Sample Size | Exact90% simulated power lacks full data-generating/fit/gate specification; printed2331=777×3 andRR1.5 inputs reconcile. Normal sample-size calculations are diagnostic only. | CONDITIONAL_OR_UNREPORTED |
| REPORT mainp11 PGIC heading andfootnotes | Mean-change heading refers to an explicitly coded since-start impression item; no competing extracted numerical assignment established. | TERMINOLOGY_OR_WORDING |
| REPORT mainp3 scoring andp7 Table1 note | All11-item instrument description versus4 intensity/at least4 interference completeness criterion does not establish a conflicting supplied score. | TERMINOLOGY_OR_WORDING |
| REPORT mainpp1,7 overall secondary-benefit narrative | Overall-pattern wording does not explicitly claim every contrast is significant, so varying physical-function null coverage supplies no direct narrative reversal. | TERMINOLOGY_OR_WORDING |

## Limitations and handoff

ExactUC changeSDs, unrounded predictions/contrasts, RD interval/NNT construction and integer convention, omnibus reference distribution/df/covariance and simulation details are not supplied; each relevant S record names the missing definition. The assigned main source locations were readable; no source-reading gap remains in this shard. The global47-row exclusion reread uses the literal source-linked current packet plus complete screening/recheck facts; this shard did not visually reread every unassigned ancillary protocol/supplement exclusion location, and makes no independent replacement statistical computation for those locations. Their direct-source relationship coverage belongs to the other disjoint pass-2 shards.

Counts:55 assigned relationships,55 PASS_2_COMPLETE,0 new findings,7 consolidated excluded observations,47/47 original exclusions reread,26/26 screening decisions reread,17/17 stable recheck facts considered. Durable outputs: `checkers/parts/stat2_main_early.md`, `statistics/parts/pass2_main_early.md`; initial canonical `checkers/statistical_pass_2.md` contains this part until coordinator merge. No stable candidate ID was added/deleted and no human disposition was assigned.

