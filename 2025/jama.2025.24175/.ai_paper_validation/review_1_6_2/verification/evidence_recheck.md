# Mechanical evidence recheck

All stable candidates remain **Pending Human Adjudication**. This canonical artifact merges the completed disjoint C001–C007 and C008–C014 specialist parts. All fourteen evidence states are reproduced, and all classifications were confirmed. Evidence states describe direct-source reproduction, not a disposition. The separately retained results_candidates_recheck.md preserves the second part's provenance.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. The current ledger and screening provenance were used to locate each registered comparison, without adopting the checker or screen's conclusions as authority. Exact original PDF pages were freshly rendered by the supplied fallback helper and visually reread. Current evidence maps and fresh direct-source native text were used for the bounded reporting-absence search. No legacy scientific conclusion or external evidence was read. No source or reused asset was modified.

## Source confirmation and derivative provenance

DOC-001 is REPORT by its article content; DOC-002 compared pages are PLAN by their current ImmunoSep protocol/SAP content; DOC-003 is REPORT by its results-table/figure content. Historical PROVIDE material bound within DOC-002 supplies no current-trial comparator here. Every source link below is relative to this verification folder and resolves to an exact physical PDF page.

The assigned cited-page union contains 31 unique pages, below the 32-page context bound. Confirmation was performed in two bounded waves:

| Wave | Exact directly reread source pages | Fresh derivative provenance artifact |
|---|---|---|
| 1 | DOC-001 pp.3,5,6,7,8; DOC-002 pp.7,24,25,26,27,57,66,67,68,69,70,71,72 | preprocessing/recheck-wave1/provenance.md |
| 2 | DOC-003 pp.16,20,21,22,23,24,46,47,49,50,51,52,53 | preprocessing/recheck-wave2/provenance.md |

All images were freshly produced from the supplied PDF by `workflow_1_6_2/scripts/pdf_tools.py render`, using PyMuPDF 1.26.4, 200 dpi, CPU. The recorded run compute preference is GPU_USER_REQUESTED; no OCR was necessary, and the recorded PDF-render engine uses CPU. Complete DOC-001 pp.1–12 and DOC-003 pp.1–54 were additionally extracted directly with the same helper's `text` command to `preprocessing/recheck-wave1/main-full-native.txt` and `preprocessing/recheck-wave2/report-full-native.txt`. Native text omits parts of embedded figure panels, so direct visual examination governs all relevant figure content.

## C001 — Primary mean/Welch versus responder/Fisher specification

**Cited locations found:** Yes, every registered location. PLAN: [DOC-002 p.7 synopsis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.24 primary endpoint and death rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=24), [p.25 day-15 endpoint](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 statistical analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.66 SAP primary construction](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), [p.67 threshold and Fisher analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 day-15 construction](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.69 day-15 responder continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69). REPORT: [DOC-001 p.3 endpoint](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 death imputation and day-15 endpoint](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2, methods and primary result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).

**Source printed text matched:** Protocol p.7 specifies a difference in mean total SOFA until day 9. P.24 specifies the comparative difference in mean total SOFA, at least a 1.4-point decrease in the immunotherapy arm compared with standard care, and use of the mean through the day of death for patients dying before day 9. P.25 lists change of mean total SOFA on day 15. P.27 names Welch's t test for primary mean differences.

**Comparator printed text matched:** SAP p.66 defines patient-level baseline minus the mean of eight daily values, days 2–9; missing values for death are 24. P.67 splits achievement/nonachievement and names Fisher's exact test, ORs and 95% CIs. Pp.68–69 repeat the construction for the 14 values on days 2–15 and Fisher comparison. REPORT p.3 defines the proportion attaining at least a 1.4-point decrease; p.5 assigns 24 from death through day 15; p.6 reports 46/131 versus 26/145, unadjusted OR 2.48 (1.42–4.32), P=.002, and Fisher comparison.

**Consistency rule applicable:** Focus D and Route A, category 5: distinguish the prospectively specified continuous arm-mean endpoint/test from the reported binary responder endpoint/test. The corresponding day-15 element and primary death handling are affected locations of the same specification pattern.

**Logical comparison reproduced and display precision:** Yes. An arm-level difference tested by Welch is a different analysis from the proportion passing a threshold tested by Fisher; averaging only through death is different from filling remaining scores with 24. These are categorical specifications; half-unit rounding and relative discrepancy do not reconcile them. The SAP's >1.4 and article's ≥1.4 alone are not part of this reproduced discrepancy: for integer daily scores, the stipulated changes are integer multiples of 1/8 or 1/14, and 1.4×8=11.2 and 1.4×14=19.6 are not integers. This observation does not eliminate the continuous-versus-binary comparison.

**Necessary inputs available:** Yes for the registered logical comparison: both endpoint definitions, day windows, death rules, planned Welch test and reported Fisher analysis are printed. **Exact missing inputs/definitions:** An operative version history or amendment explicitly connecting the original continuous primary analysis to the later responder specification; participant-level SOFA values would be needed to quantify resulting classification changes but are not needed to reproduce the specification difference.

**Source-grounded alternative interpretation:** The later SAP agrees with the responder analysis and may represent an authorized revision or operational clarification. The supplied locations do not give the explicit original-to-revised mapping. **Direct observation versus inferred explanation:** The two specifications and analysis methods are directly printed. Revision authorization, actual analytic conduct and any participant-level effect are not inferred.

**Exact remaining human question:** Which operative endpoint/test/death-handling specification governed the primary and corresponding day-15 results, and where is the documented revision linking it to the original mean/Welch specification?

**Classification confirmed:** Every DOC-002 compared location is PLAN and every DOC-001 compared location is REPORT. Primary relationship **P_R**; all relationships **P_R, P_P**; domain **protocol_report**. P_P records the actual original-protocol versus later-SAP specification difference, not mere plan corroboration. Precedence P_R > P_P selects P_R. No classification correction. Classification ambiguity is the status and scope of the later SAP revision, not the content roles.

**Evidence state: reproduced.** Determining fact: direct source confirms the continuous/Welch and binary/Fisher/death-rule specifications coexist in the supplied package. No registered transcription or location correction was needed.

## C002 — Home-discharge versus ICU-discharge carry-forward eligibility

**Cited locations found:** Yes, all six. PLAN: [DOC-002 p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66). REPORT: [DOC-001 p.3 ICU observation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 home-discharge rule](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 ICU-discharge result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [DOC-003 p.20 eTable 8](../../../joi250116supp2_prod_1771885794.27755.pdf#page=20), [p.46 eFigure 2 sensitivity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=46).

**Source printed text matched:** SAP p.66 carries forward the last recorded SOFA for patients discharged home before day 9. Article p.5 uses the same home-discharge rule and separately names loss to follow-up.

**Comparator printed text matched:** Article p.3 captures SOFA daily during ICU stay until discharge; p.6 attributes cumulative 8.3% carry-forward to ICU discharge before day 9. eTable 8 explicitly describes carry-forward for patients discharged earlier from the ICU and prints assumed day-9 counts 10 and 13. eFigure 2 excludes patients discharged before day 9 whose SOFA was carried forward, with 38/121 (31.4%) versus 19/132 (14.4%), OR 2.72 (1.47–5.05), P=.001.

**Consistency rule applicable:** Focus D, Route B. Carry-forward eligibility determines the primary endpoint's missing-data window and sensitivity-population membership. ICU discharge and discharge home can denote distinct clinical transitions; the text does not identify them as equivalent for these patients.

**Logical comparison reproduced and display precision:** Yes for the operational specification difference, not a numeric count discrepancy. The 10+13=23 carry-forward patients reproduce 23/276×100=8.333333%. Conservatively allowing 10 and 13 their half-unit intervals and 276 its own gives a recomputed percentage interval [7.95660%,8.71143%], overlapping printed 8.3%'s [8.25%,8.35%]; discrepancy and relative discrepancy are zero. Exact integer counts likewise reproduce the displayed percentage. The sensitivity exclusions 131−121=10 and 145−132=13 reconcile. Numerical agreement cannot establish that each ICU discharge was a home discharge.

**Necessary inputs available:** Yes for the comparison: explicit home and ICU criteria, SOFA measurement window, carry-forward counts and sensitivity denominators. **Exact missing inputs/definitions:** Home/ward discharge dates for these 23 patients; whether ICU discharge coincided with home discharge; the precise stop-observation/carry-forward transition applied to the primary endpoint.

**Source-grounded alternative interpretation:** All 23 ICU discharges may also have been home discharges, or the report's ICU terminology may abbreviate the operational home criterion. Neither equivalence is stated. **Direct observation versus inferred explanation:** The printed location labels differ. No claim is made about any patient's destination, changed SOFA value or actual protocol conduct.

**Exact remaining human question:** Which discharge event triggered carry-forward, and were all 23 primary-analysis carry-forward cases discharged home when ICU observation ended?

**Classification confirmed:** DOC-002 p.66 is PLAN; all article/results-supplement locations are REPORT. Primary relationship **P_R**; all relationships **P_R, S_C, S_W**; domain **protocol_report**. The PLAN-home versus REPORT-ICU comparison supplies P_R; article-home versus supplement-ICU supplies S_C; article-home versus article-ICU supplies S_W. Precedence selects P_R. No classification correction. Unknown equivalence of the discharge events is the classification/content ambiguity.

**Evidence state: reproduced.** Determining fact: the original printed home and ICU carry-forward criteria remain distinct without a supplied statement equating their eligibility sets.

## C003 — Current-trial infection/omics status pattern

**Cited locations found:** Yes, all eight. PLAN: [DOC-002 p.7 synopsis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.25 detailed hierarchy](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 test hierarchy](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.57 resolution appendix](../../../joi250116supp1_prod_1771885794.26255.pdf#page=57), [p.70 SAP infection analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70). REPORT: [DOC-001 p.5 endpoints](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 main secondary table](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 sixth secondary result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7).

**Source printed text matched:** Protocol synopsis p.7 lists both infection resolution and genomic/epigenomic/proteomic/metabolomic/microbiomic surrogate biomarkers under secondary study endpoint. Detailed protocol p.25 places both under a distinct exploratory study endpoints heading; p.27 explicitly calls the infection-resolution and surrogate-biomarker analyses exploratory. P.57's current ImmunoSep appendix labels infection-resolution criteria as applying to the exploratory study endpoint.

**Comparator printed text matched:** SAP p.70 places infection resolution within its secondary-endpoint sequence. Article p.5 explicitly lists six prespecified secondary endpoints including infection resolution by day 15; p.6 lists infection assessment under main secondary outcomes and reports OR 0.59 (0.38–0.91), P=.02; p.7 calls it the sixth secondary result. The omics component has no reported outcome-status counterpart in this registered comparison.

**Consistency rule applicable:** Focus D and Route A, category 5, changed outcome status. The current protocol's explicit secondary and exploratory hierarchy is a statistical-design comparison, not a historical PROVIDE comparison or a difference in shortened endpoint names.

**Logical comparison reproduced and display precision:** Yes: secondary and exploratory status coexist under distinct headings. Infection crosses PLAN/REPORT; the parallel omics status pattern is PLAN-internal. No half-unit arithmetic or numerical relative discrepancy applies to outcome status. The infection OR, CI and P value are identifiers of the affected result, not an additional statistical contradiction.

**Necessary inputs available:** Yes: headings, outcome labels and reported infection result. **Exact missing inputs/definitions:** An operative hierarchy/version or amendment; whether the synopsis uses secondary as an explicit umbrella covering exploratory outcomes. No participant-level data are necessary for this comparison.

**Source-grounded alternative interpretation:** The synopsis and later SAP support the report's secondary status, and could reflect the intended or revised hierarchy. The detailed protocol and appendix expressly distinguish exploratory status without explaining such umbrella usage. **Direct observation versus inferred explanation:** The differing hierarchy labels are directly printed; their editorial or amendment mechanism is not inferred. No requirement to report exploratory omics is inferred.

**Exact remaining human question:** Which hierarchy and version governed the infection-resolution outcome, and what amendment or explicit hierarchy convention reconciles the secondary versus exploratory designations and the accompanying plan-internal omics pattern?

**Classification confirmed:** All compared DOC-002 locations are PLAN by current prospective content; all DOC-001 locations are REPORT. Primary relationship **P_R**; all relationships **P_R, P_P**; domain **protocol_report**. The detailed PLAN versus REPORT infection status supplies P_R; synopsis versus detailed PLAN infection/omics status supplies P_P. Precedence selects P_R. No classification correction. Omics has P_P only and is not asserted to have an absent REPORT result relationship.

**Evidence state: reproduced.** Determining fact: direct source retains explicit secondary versus exploratory headings for the same current-trial outcome family.

## C004 — Reversal endpoint window/composite/ascertainment

**Cited locations found:** Yes, all seven. PLAN: [DOC-002 p.25](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), [p.70 continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70). REPORT: [DOC-001 p.5 definition](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2 and footnote](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 day-28 result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.50 eFigure 6](../../../joi250116supp2_prod_1771885794.27755.pdf#page=50).

**Source printed text matched:** Protocol p.25 places reversal at day 15: MALS ferritin decrease at least 15%; immunoparalysis Quantibrite above 8000 AB/C with ferritin below 4420 ng/mL. SAP p.69 explicitly censors the endpoint at day 15, repeats the biomarker conjunction and treats MALS death before day 15 as nonachievement. P.70 treats immunoparalysis death before day 15 as nonachievement and continues the test specification.

**Comparator printed text matched:** Article p.5 gives the two biomarker criteria without the ferritin conjunction for immunoparalysis. P.6 requires sustained ferritin decrease or an absolute HLA-DR target above 8000 across follow-up, with at least two serial draws; fewer draws mean nonattainment. It reports reversal 46/59 (78.0%) versus 32/66 (48.5%), OR 3.76 (1.72–8.22). P.7 explicitly identifies these counts with reversal by day 28. eFigure 6 p.50 describes the 59/66 sampled population, draws through day 28, missing draws from death/discharge, sustained thresholds, at least two draws, and Cox HR 2.38 (1.50–3.77) censored by day 28.

**Consistency rule applicable:** Focus D and Route A, category 5: compare the prospective endpoint window, composite definition and ascertainment/death handling with the reported reversal result. The day-28 Cox display corroborates the reported window; no preference for another analysis is proposed.

**Logical comparison reproduced and display precision:** Yes. Day 15 versus day 28 and one biomarker conjunction versus a printed definition omitting ferritin and adding sustained-change/serial-draw requirements cannot reconcile through numerical rounding. The report's isolated increase-of wording on p.5 is resolved by its absolute-target footnote and figure caption; it is not an additional S_W or S_C relationship. The 59+66=125 subgroup count is internally coherent; 46/59×100=77.9661% and 32/66×100=48.4848% fall within the printed percentage half-unit intervals [77.95%,78.05%] and [48.45%,48.55%]. Thus no count-percentage discrepancy is inferred from these identifiers.

**Necessary inputs available:** Yes for the specification comparison: prospective criteria, death rules, report persistence/draw rules, reported day-28 window and subgroup denominators. **Exact missing inputs/definitions:** The operative window/composite specification and revision; whether ferritin <4420 was applied despite omission; how all patients without adequate serial draws entered or were omitted from the reported 125-person denominator; patient biomarker/death/discharge histories needed to quantify the effect.

**Source-grounded alternative interpretation:** The day-28 Cox output might supplement a day-15 endpoint, or the ferritin conjunction might have been applied without repetition. The article expressly ties the displayed reversal counts to day 28 and the supplied package does not identify a separate day-15 version of those counts. SAP p.70's shorthand is interpreted in the context of the full immediately preceding p.69 conjunction, not treated as a separate P_P issue. **Direct observation versus inferred explanation:** Window, criteria and denominator are printed. No patient is presumed reclassified, and no causal explanation for the sampled subset is inferred beyond the caption's missing-draw description.

**Exact remaining human question:** Which window, biomarker composite, sustained-change requirement and missing-draw/denominator rules define the reported prespecified reversal result, and how do they map to the planned day-15 definition?

**Classification confirmed:** DOC-002 locations are PLAN; DOC-001/DOC-003 locations are REPORT. Primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**. Report locations agree about the relevant operational interpretation; PLAN shorthand is contextually resolved. No classification correction.

**Evidence state: reproduced.** Determining fact: direct source confirms a planned day-15 biomarker-conjunction endpoint and a reported day-28 persistence/draw-based endpoint without an explicit mapping.

## C005 — Continuous versus binary power basis

**Cited locations found:** Yes. PLAN: [DOC-002 p.25 power introduction](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.26 power calculation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=26). REPORT: [DOC-001 p.5 Sample Size Calculation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5). The supplied SAP pp.63–72 was checked through the complete current plan map and directly reread analytic pp.66–72; its cover/glossary/study-population content supplies no revised binary power calculation.

**Source printed text matched:** Protocol p.25 powers a 1.4-point reduction in mean SOFA. P.26 prints 90% power, 5% significance, anticipated dispersion 3.2, a two-sided independent-groups t test and nQuery Advisor 6.02. It states 117 per arm and 280 after approximately 15% dropout. The p.26 40%/60% pair describes anticipated phenotype recruitment, not arm-specific response probabilities.

**Comparator printed text matched:** Article p.5 anticipates primary attainment in 40% of intervention versus 20% of control patients, 90% power, 5% significance, 117 per group and 280 with approximately 15% dropout. It does not print a revised binary calculation formula or procedure.

**Consistency rule applicable:** Focus D and Route B: power inputs and effect scale determine interpretation of the reported binary primary outcome's power. An effect-size basis stated as a continuous mean difference is distinct from one stated as two response probabilities, even if the required sample is numerically the same.

**Logical comparison reproduced and display precision:** Yes for the design-basis difference. No numerical sample-size inconsistency is asserted. Rounding cannot transform a continuous mean difference into binary response probabilities. For the contextual dropout calculation, 234/.85=275.2941 versus 280 is below the .05 threshold; allowing 117 its half-unit interval in each arm and 15% its half-unit interval gives [233/.855,235/.845]=[272.5146,278.1065]. Printed 280 has [279.5,280.5], gap 1.3935 and relative discrepancy 0.00498, still within the display-precision exclusion. The protocol's unusually worded dispersion is preserved without assuming a unique exact calculation.

**Necessary inputs available:** Yes for the effect-scale comparison: mean difference, dispersion wording, t-test method, binary response probabilities and common nominal power/sample size. **Exact missing inputs/definitions:** A prospective binary sample-size calculation or amendment, exact calculation procedure/continuity convention, and the operative interpretation of the protocol dispersion wording. These limit precise sample-size reproduction, not the printed power-basis comparison.

**Source-grounded alternative interpretation:** A revised calculation may have preserved 117/group, or a threshold-response planning assumption may have been used alongside the continuous calculation. Neither linkage is supplied. **Direct observation versus inferred explanation:** The two power bases are directly printed. No claim is made that 117 fails a particular exact procedure or that the study achieved a particular realized power.

**Exact remaining human question:** Which prospective calculation or documented revision supports the report's 40%-versus-20% binary primary-response power claim?

**Classification confirmed:** Protocol locations are PLAN; article power section is REPORT. Primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**. No classification correction. The missing operative revision is a content ambiguity, not a reason to change roles.

**Evidence state: reproduced.** Determining fact: the exact prospective and reported power statements use distinct continuous and binary effect-scale inputs without a supplied linkage.

## C006 — Binary planned versus ordinal reported infection analysis

**Cited locations found:** Yes, all five. PLAN: [DOC-002 p.27 Fisher/Mantel–Haenszel](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.70 binary SAP specification](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70). REPORT: [DOC-001 p.6 Table 2 and methods](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 ordinal result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.49 four-state figure](../../../joi250116supp2_prod_1771885794.27755.pdf#page=49).

**Source printed text matched:** Protocol p.27 names Fisher exact infection-resolution comparison and Mantel–Haenszel OR/CIs. SAP p.70 explicitly divides patients into achieving or not achieving resolution, compares those two groups by Fisher, and calculates OR/CIs by Mantel–Haenszel, with planned infection/immune strata.

**Comparator printed text matched:** Article p.6 states ordinal regression for resolved, intermediate, failure and superinfection, while stating that all analyses followed the SAP. Table 2 counts are 58,11,32,30 of 131 versus 46,9,44,46 of 145, with OR 0.59 (0.38–0.91) for worse outcome, P=.02. P.7 expressly identifies ordinal regression. eFigure 5 p.49 labels four states and OR for worse disposition 0.59 (0.38–0.91), P=.018; its caption groups the three nonresolution categories as worse outcomes.

**Consistency rule applicable:** Focus D and Route B: identify whether the reported infection estimate is the planned binary resolution analysis or a four-category ordinal analysis. The differing model/endpoint analysis affects interpretation and extraction of the named OR.

**Logical comparison reproduced and display precision:** Yes: an explicitly binary Fisher/Mantel–Haenszel comparison differs from the explicitly ordinal regression. The source counts total 131 and 145, and there is no count-total issue here. The P=.018 versus P=.02 copies have half-unit intervals [.0175,.0185] and [.015,.025], overlapping with discrepancy and relative discrepancy zero. A crude binary resolution OR can be calculated, but it is not compared numerically with the modeled ordinal OR as an inconsistency. No display-precision rule equates the distinct analysis specifications.

**Necessary inputs available:** Yes for the specification comparison: binary plan, four states, ordinal report method and reported estimate. **Exact missing inputs/definitions:** A revised infection-analysis specification; whether a binary estimate/test was produced in addition; ordinal coding/link and any adjustment details sufficient to identify its exact model. Patient-level data are not required to observe the specification difference.

**Source-grounded alternative interpretation:** Ordinal regression may supplement or replace binary resolution, and the worse-disposition caption may summarize an ordinal estimand. The article identifies ordinal regression clearly, but the package does not show the mapping to the prescribed binary analysis or a corresponding binary result. **Direct observation versus inferred explanation:** Printed binary versus ordinal methods are direct observations. No claim is made that a model estimate must equal a crude ratio, or that the reported model has an unsupported particular link.

**Exact remaining human question:** Did the four-state ordinal result supplement or replace the planned binary infection-resolution result, and which operative specification or supplied result establishes that mapping?

**Classification confirmed:** Both DOC-002 locations are PLAN; both DOC-001 and DOC-003 locations are REPORT. Primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**. The reported ordinal locations corroborate each other; they create no independent S_C conflict. No classification correction.

**Evidence state: reproduced.** Determining fact: direct source specifies a binary planned comparison and an ordinal reported comparison, with no supplied replacement/addition mapping.

## C007 — Prespecified primary/key-secondary analyses not located

**Cited locations found:** Yes, every registered prospective and report location, including the explicitly bounded context. PLAN: [DOC-002 p.67 immune-state homogeneity](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 survivor-mean context and 28-day mortality subgroups](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.71 severity/homogeneity and antibiotics](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71), [p.72 antibiotic continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72). REPORT: [DOC-001 p.5 definitions](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 methods/results](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 response/mortality/post hoc results](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [p.8 interaction continuation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), [DOC-003 p.16 antibiotic footnote](../../../joi250116supp2_prod_1771885794.27755.pdf#page=16), [p.21 primary model](../../../joi250116supp2_prod_1771885794.27755.pdf#page=21), [p.22 immune-state response](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22), [p.23 subset baseline](../../../joi250116supp2_prod_1771885794.27755.pdf#page=23), [p.24 subset baseline continuation](../../../joi250116supp2_prod_1771885794.27755.pdf#page=24), [p.47 overall mortality](../../../joi250116supp2_prod_1771885794.27755.pdf#page=47), [p.51 primary severity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), [p.52 28-day severity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), [p.53 90-day severity context](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53).

**Source printed text matched:** P.67 prescribes Breslow–Day and Tarone comparison of primary-response ORs across MALS/immunoparalysis. P.68 prescribes MALS and immunoparalysis subgroup analyses for 28-day mortality. P.71 prescribes primary and 28-day-mortality severity-stratum OR/homogeneity analyses with immune-state stratification and named Breslow–Day/Tarone tests. Pp.71–72 prescribe primary-response analysis separately by appropriate versus non-appropriate antibiotics. These are the four included analysis families.

**Comparator content matched and bounded absence reproduced:** The complete 12-page article map and complete 54-page results-supplement map/index were checked, and fresh full-source native text was searched for Breslow, Tarone, homogeneity, appropriate, antibiotic, MALS, immunoparalysis, mortality, survivor, interaction, replacement, withdrawal and amendment wording. The results supplement's original p.1 index lists all 15 tables and 9 figures and supplies no additional named analysis destination. The directly reread relevant report pages confirm the following:

| Prescribed family | Closest supplied report content | Exact absent or unmapped result |
|---|---|---|
| Primary-response immune-state homogeneity | Article p.7 and eTable 10 p.22 show separate MALS/IP response estimates/tests | No Breslow–Day/Tarone homogeneity result comparing those immune-state ORs |
| Key-secondary 28-day mortality in MALS/IP | Article Table 2/p.7 and eFigure 3 p.47 show total-population mortality; eFigures 8/9 split severity, not immune phenotype | No within-MALS/IP 28-day mortality comparison/result |
| Primary-response by antibiotic appropriateness | eTable 6 medication footnote p.16 defines baseline active-antibiotic frequencies; the map locates 34/41 versus 33/38 on p.15 | No primary-responder comparison or effect/test by appropriate/non-appropriate antibiotics; baseline treatment frequencies are not response outcomes |
| Primary/key-28-day severity homogeneity and immune-within-severity results | eFigures 7/8 pp.51–52 give severity-specific treatment comparisons and panel-B model interactions, used in article pp.7–8 | No named Breslow–Day/Tarone results or immune-within-severity analysis outputs; no statement mapping the interaction output to those planned tests |

All page-level map rows for DOC-001 pp.1–12 and DOC-003 pp.1–54 were included in the reporting-scope check, including no-applicable administrative/reference pages. Native-text searches alone cannot exclude unextractable figure content; that limitation was closed at relevant figures by fresh visual confirmation. The claim is limited to the supplied REPORT package and its documented mappings. It does not claim the analyses were never performed.

**Explicit bounded context:** SAP p.68 also describes survivor-only day-1–9 mean SOFA using Student's t test, with nine values including day 1. It is a distinct secondary continuous mean, not explicitly key secondary and not in the abstract. Its absence alone does not enlarge the registered primary/key-secondary pattern. Likewise, non-key 90-day immune analyses, day-15 survivor means and exploratory ROC/omics absences are not additional included components. ETable 11 pp.23–24 contains baseline comparisons of the serial-draw subset, not a prospective outcome analysis. P.53 is examined 90-day context only. Original primary mean/Welch replacement is separately C001.

**Consistency rule applicable:** Focus D and Route A, category 5, planned primary/key-secondary analyses not located in supplied reporting. Structurally identical absence observations are consolidated into one candidate; this is not a new candidate per test or score.

**Logical comparison reproduced and display precision:** Yes, within the explicitly bounded supplied package. Named planned analyses are printed and the corresponding outputs or explicit replacement/removal specification are not located. Half-unit intervals and relative numeric discrepancy are not applicable to absence of a named analysis. Separate response ORs, a total-population mortality result, baseline antibiotic counts and logistic interactions cannot be silently assigned to a named absent analysis.

**Necessary inputs available:** Yes: exact planned tests/outcomes/strata, complete supplied reporting inventory and exhaustive maps, directly reread plausible destinations and source text. **Exact missing inputs/definitions:** The named analysis outputs or their explicit replacement/removal specification; result-level immune-by-severity and antibiotic-response cross-tabulations; any document not supplied to this package. Such missing data prevent quantifying the absent effects but are not required to reproduce bounded nonlocation.

**Source-grounded alternative interpretation:** The displayed interaction analyses may have replaced the planned homogeneity tests; phenotype response results may have been considered sufficient without a homogeneity output; analyses could be available in another, unsupplied report. None is identified as the planned-analysis mapping in supplied content. **Direct observation versus inferred explanation:** Prospective analysis statements, report destinations and bounded nonlocation are directly checked facts. Whether analysis was performed, consciously omitted, replaced or available elsewhere remains unknown.

**Exact remaining human question:** Where are the prespecified primary/key-secondary results for these four analysis families, or the explicit specification documenting their replacement or removal from the supplied reporting?

**Classification confirmed:** Every prospective DOC-002 location is PLAN. Every compared DOC-001/DOC-003 location and the complete reporting maps/index are REPORT. Primary relationship **P_R**; all relationships **P_R**; domain **protocol_report**. Report displays are closest comparators/context, not mutually conflicting results that add S_C or S_W. No classification correction. Mapping of interaction tests to prespecified homogeneity tests remains the content ambiguity.

**Evidence state: reproduced.** Determining fact: all four included prospective analysis families are source-confirmed and their specific outputs or explicit replacement/removal mapping are not located across the complete supplied reporting inventory, with each plausible destination visually checked.

## Final classification and evidence facts for this disjoint part

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | PLAN original protocol vs PLAN later SAP and REPORT article | reproduced | None; original/later PLAN comparison is an actual relationship |
| C002 | protocol_report | P_R | P_R, S_C, S_W | PLAN home-discharge rule vs REPORT article/supplement ICU-discharge descriptions, including article-internal contrast | reproduced | None |
| C003 | protocol_report | P_R | P_R, P_P | PLAN synopsis/detailed protocol/SAP outcome hierarchy vs REPORT article infection hierarchy | reproduced | None; omics status component is PLAN-internal only |
| C004 | protocol_report | P_R | P_R | PLAN reversal specification vs REPORT article/results-supplement reversal specification | reproduced | None; report absolute-target context and PLAN shorthand are not separate relationships |
| C005 | protocol_report | P_R | P_R | PLAN continuous power basis vs REPORT binary power basis | reproduced | None |
| C006 | protocol_report | P_R | P_R | PLAN binary infection analysis vs REPORT ordinal infection analysis | reproduced | None; report copies corroborate each other |
| C007 | protocol_report | P_R | P_R | PLAN primary/key-secondary analysis specifications vs complete supplied REPORT scope | reproduced | None; closest report outputs are context, not added report/report conflicts |

Part counts: 7 covered IDs; 7 reproduced; 0 reproduced_after_transcription_correction; 0 not_reproduced; 0 classification changes. Every cited affected or bounded-context location for this part was found. Unresolved items are precisely the per-ID human questions and missing inputs above; no scientific coverage gap remains in the assigned recheck scope.
# Mechanical evidence recheck: results candidates

Scope: C008, C009, C010, C011, C012, C013, C014. All seven stable IDs and every affected location were rechecked separately. All remain Pending Human Adjudication. This artifact records evidence facts and classification; it assigns no adjudication or proposed replacement result.

The complete `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_2/review_contract.md`, the assigned ledger cards and classification rows, screening groups G08–G14, and corresponding current-run checker facts were read. Printed values were then independently read from fresh renders of exact supplied PDFs. Existing text, screening calculations and checker conclusions were locators, not final authority. No external source or earlier-run scientific conclusion was used.

## Recheck coverage and provenance

Eleven unique source pages were freshly rendered and visually inspected: DOC-003 pp.22,27,29,44,51,52,53; DOC-001 pp.6,7,8; DOC-002 p.70. The extra DOC-003 p.29 confirms the patient-count definition supporting the safety comparisons. No new OCR was needed.

The recorded missing direct rendering capability was handled with the supplied helper and temporary package-local interpreter. Every derivative uses PyMuPDF 1.26.4, 200 dpi, CPU PDF rendering. The tooling record's `GPU_USER_REQUESTED` records the user's GPU OCR request; no GPU OCR engine or OCR derivative was needed here. Sources and reused assets were read without modification.

Command template, run once for every row below:

```bash
.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render "SOURCE.pdf" --page N ".ai_paper_validation/review_1_6_2/preprocessing/recheck_results/OUTPUT.png" --dpi 200
```

| Source | Physical PDF page | Derivative relative to review_1_6_2 | Engine and device |
|---|---:|---|---|
| joi250116supp2_prod_1771885794.27755.pdf | 22 | preprocessing/recheck_results/supp-22.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 27 | preprocessing/recheck_results/supp-27.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 29 | preprocessing/recheck_results/supp-29.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 44 | preprocessing/recheck_results/supp-44.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 51 | preprocessing/recheck_results/supp-51.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 52 | preprocessing/recheck_results/supp-52.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp2_prod_1771885794.27755.pdf | 53 | preprocessing/recheck_results/supp-53.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 6 | preprocessing/recheck_results/main-6.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 7 | preprocessing/recheck_results/main-7.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf | 8 | preprocessing/recheck_results/main-8.png | PyMuPDF 1.26.4; CPU; 200 dpi |
| joi250116supp1_prod_1771885794.26255.pdf | 70 | preprocessing/recheck_results/plan-70.png | PyMuPDF 1.26.4; CPU; 200 dpi |

Independent arithmetic was performed in JavaScript without Python scientific orchestration. Two-sided Fisher values use the probability-order definition: for treatment sample size n, comparator size m, total events K, and treatment events a, sum `choose(K,x)*choose(n+m-K,n-x)/choose(n+m,n)` over feasible integer x whose probability is no larger than the observed probability at a. Log-factorial evaluations avoid overflow. Floating-point summation within approximately 4×10⁻¹³ of 1 is reported as 1. Every displayed exact count's half-unit interval contains only its displayed integer for an exact contingency calculation.

| ID | Locations found and source/comparator matched | Primary relationship | All relationships | Review domain | Evidence state |
|---|---|---|---|---|---|
| C008 | Yes, all four eTable 10 rows | S_W | S_W | statistical_results | reproduced |
| C009 | Yes, MALS patient risks and NNH1 point/direction | S_W | S_W | statistical_results | reproduced |
| C010 | Yes, both patient-risk pairs, both intervals and test specification | S_W | S_W | statistical_results | reproduced |
| C011 | Yes, five affected rows and all 13 companion rows | S_W | S_W | statistical_results | reproduced |
| C012 | Yes, both APACHE rows and all five companion rows in each panel | S_W | S_W | statistical_results | reproduced |
| C013 | Yes, both complete six-row arrays, outcome captions and narrative use | S_W | S_W | report_internal_inconsistency | reproduced |
| C014 | Yes, named point, both limits, P value and outcome caption | S_W | S_W | statistical_results | reproduced |

All role, primary relationship, all-relationship and review-domain assignments are confirmed; zero classification changes. DOC-003 and DOC-001 contain reported trial results and are REPORT by content. DOC-002 p.70 is prospective SAP material and is PLAN by content. Corroboration from another document is identified below and is not counted as an additional conflicting relationship.

## C008 — Source-printed unadjusted day-15 immunoparalysis OR

**Status:** Pending Human Adjudication

**Location found:** Yes. [DOC-003 p.22, eTable 10](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22), final row for the day-15 mean-SOFA responder endpoint in sepsis-induced immunoparalysis, plus all three companion unadjusted-OR rows in the same table. The fresh source render confirms the table title, response window, column alignment and explicit unadjusted label.

**Source printed value/text matched:** Yes. Precision immunotherapy 40/106 (37.7%), placebo 29/122 (23.8%); difference 13.9 (1.9–25.6); unadjusted OR **1.194** (1.09–3.45); P=.030. The point is visibly 1.194, not 1.94.

**Comparator matched:** Yes. The other three rows show 12/25 versus 4/23 with OR 4.38, 34/106 versus 22/122 with OR 2.15, and 12/25 versus 5/23 with OR 3.32.

**Consistency rule applicable:** Yes. The source explicitly labels the point unadjusted. The count-based binary odds-ratio method reproduces all three companion points, supporting Route A category 4. This comparison does not require equating a model-based estimate with a crude ratio.

**Calculation reproduced and display precision:** `40×(122−29)/[(106−40)×29] = 1.943573668`. Companion points independently reproduce as 4.384615385, 2.146464646 and 3.323076923. Allowing all four displayed count inputs their half-unit intervals gives OR range `[39.5×92/(67×29.5), 40.5×94/(65×28.5)] = [1.838603592,2.055060729]`. The printed point interval is [1.1935,1.1945]. The minimum gap is 0.644103592 and relative discrepancy is 0.644103592/1.194 = **0.539450245**, above 0.05. Allowing continuous half-unit count values is conservative; requiring exact integers would narrow the recomputed range. The geometric center of its displayed CI is approximately 1.93920, additional corroboration rather than a substitute result.

**Necessary inputs available:** Yes for the registered point comparison: all four cell-count inputs, comparator rows and the unadjusted label. **Exact missing inputs or definitions:** an alternative unadjusted computation or different underlying analysis population that could associate 1.194 with this row is not identified. These are unnecessary to reproduce the count-supported discrepancy but necessary to explain its origin.

**Source-grounded alternative interpretation:** The point could refer to an unprinted population or another computation. The display supplies neither distinction; no such interpretation is adopted. Neighboring counts and CI may help a reader reconstruct a plausible intended value, but the recheck does not replace the printed point.

**Direct observation versus inferred explanation:** Direct observation is the source-printed 1.194 under an unadjusted-OR label and its failure to reproduce by the method reproducing the other rows. A digit substitution, publication transcription or different analysis is an inferred possible mechanism only.

**Classification confirmed:** Every conflicting location is REPORT within DOC-003. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No PLAN statement is needed or in conflict. Classification ambiguity: no alternative method/population is identified, but document roles are clear.

**Evidence state:** **reproduced**. Determining fact: exact source visual confirms 1.194, and the conservative recomputation remains separated by relative discrepancy 0.539450245. No registered source value or source location needed transcription correction.

**Exact remaining human question:** Which unadjusted odds ratio and analysis inputs belong to the day-15 immunoparalysis response comparison, and how does 1.194 reconcile with 40/106 versus 29/122 and the neighboring rows' count-reproducing method?

## C009 — MALS NNH1 harm/benefit direction

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.27, eTable 13 Any SAE row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27); [p.44, eTable 15 MALS NNH1 row and harm-induction label](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). Supplemental definition checked at [p.29, eTable 13 footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29): the flagged data represent numbers of patients; other subrows represent event numbers. The Any SAE row on p.27 carries that footnote marker.

**Source printed value/text matched:** Yes. MALS NNH1 is **8.8**, 95% CI 3.2–10.0, explicitly labeled number of patients needed to treat to **induce at least 1 serious TEAE**. Abbreviations define NNH as number needed to harm.

**Comparator matched:** Yes. MALS anakinra N=25, Any SAE 20 (80.0%); MALS placebo N=23, Any SAE 21 (91.3%). The patient-count footnote supports treating these as risks of at least one event.

**Consistency rule applicable:** Yes. Under treatment-minus-placebo direction, inducing an additional serious event requires a positive risk increase. The observed treatment risk is smaller. The reported magnitude alone is close to the unsigned reciprocal, but the harm-induction label associates that magnitude with the opposite direction. This is the registered Route A category 2 direction/reference-group comparison.

**Calculation reproduced and display precision:** RD=`20/25−21/23 = −0.113043478`; signed reciprocal=`−8.846153846`. Conservative independent half-unit count/denominator intervals give RD lower `19.5/25.5−21.5/22.5 = −0.190849673` and upper `20.5/24.5−20.5/23.5 = −0.035605732`. The signed reciprocal interval is [−28.085365854,−5.239726027], disjoint from the printed point's [8.75,8.85]. Minimum signed gap is 13.989726027 and relative discrepancy is **1.589741594**, above 0.05. Printed risk intervals [79.95,80.05]% and [91.25,91.35]% likewise preserve a negative treatment-minus-placebo difference, [−11.40,−11.20] percentage points. This candidate concerns direction, not rounding of the unsigned magnitude.

**Necessary inputs available:** Yes: affected patient counts, group denominators, patient-count definition, point and explicit induce-harm wording. **Exact missing inputs or definitions:** the table's treatment/reference-group sign convention and whether absolute reciprocals are used for benefit and harm alike are not supplied.

**Source-grounded alternative interpretation:** An unsigned reciprocal convention or a reversed comparator could generate positive 8.8. The label does not explain such a convention or distinguish prevention from induction for this row. The alternative is recorded without assuming the direction the authors intended.

**Direct observation versus inferred explanation:** Direct facts are fewer patients with any SAE under anakinra and the positive point under an induce-harm label. An unsigned calculation or switched reference group is an inferred explanation, not a source-printed method.

**Classification confirmed:** Both conflicting table locations are REPORT in DOC-003; p.29 is REPORT corroboration of the input definition. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No role or relationship ambiguity alters these fields.

**Evidence state:** **reproduced**. Determining fact: the exact printed patient risks retain the opposite treatment-minus-placebo direction from the positive harm-induction reading, including conservative half-unit ranges.

**Exact remaining human question:** Does MALS 8.8 represent the number needed to prevent or to induce a serious TEAE, and what treatment/reference-group and sign convention define it?

## C010 — NNH1 confidence intervals versus source-specified safety tests

**Status:** Pending Human Adjudication

**Locations found:** Yes. Conflicting REPORT results are [DOC-003 p.27, eTable 13 MALS and immunoparalysis Any SAE patient rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27) and [p.44, eTable 15 corresponding NNH1 intervals](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44). The [p.29 footnote a](../../../joi250116supp2_prod_1771885794.27755.pdf#page=29) confirms patient counts. Methodological corroboration is [DOC-001 p.6, significance and all-analyses-follow-SAP statements](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) and [DOC-002 p.70, Safety and two-sided significance rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70).

**Source printed value/text matched:** Yes. MALS NNH1 8.8 with 95% CI **3.2–10.0**; immunoparalysis NNH1 47.6 with 95% CI **9.9–55.8**. Both are finite positive intervals labeled 95% CIs for the number needed to induce at least one serious TEAE.

**Comparator matched:** Yes. MALS 20/25 versus 21/23; immunoparalysis 96/106 versus 108/122. DOC-002 p.70 explicitly specifies Fisher's exact comparison of serious/nonserious TEAE incidence between treatments in each immune stratum, with two-sided .05 significance. DOC-001 p.6 states P<.05 and that analyses followed the SAP. No safety P value for these two rows is printed at the compared table locations; the values below are independently recomputed under the supplied test, not transcribed publication P values.

**Consistency rule applicable:** Yes, as an interval-versus-specified-test comparison (Route A category 1). A conventional confidence set for the reciprocal of the same risk difference must accommodate the no-effect/infinite-number limit when its corresponding comparison is nonsignificant. The printed finite positive intervals omit that limit. The source permits comparison to a named safety test, while the missing interval procedure remains the precise human question.

**Calculation reproduced and display precision:** Independent probability-order two-sided Fisher summation gives **P=.419120073** for MALS and **P=.669907887** for immunoparalysis, both above .05. Positive finite NNH intervals imply reciprocal risk-difference intervals [1/10.0,1/3.2]=[.100000,.312500] and [1/55.8,1/9.9]=[.017921,.101010], neither containing zero. Exact-integer half-unit count ranges cannot change the contingency tables. Even granting each printed bound its .05 half-unit uncertainty, all limits remain finite and positive: MALS [3.15,3.25] and [9.95,10.05]; immunoparalysis [9.85,9.95] and [55.75,55.85]. Thus no display rounding reaches the no-effect limit. Category 1 is not subject to the relative-discrepancy .05 exclusion. C009 separately records the MALS direction comparison, which uses a different rule.

**Necessary inputs available:** Yes for this bounded recheck: patient counts, denominators, named safety test, two-sided significance level and confidence level. **Exact missing inputs or definitions:** the NNH confidence procedure, whether the bounds are an ordinary connected interval or shorthand for a split confidence set, whether they use signed or absolute risk differences, and whether their analysis population differs from the Any SAE rows. The precise interval computation cannot be reconstructed from the supplied text.

**Source-grounded alternative interpretation:** The intervals could arise from a different analysis/population or could abbreviate a split confidence set crossing the reciprocal singularity. A confidence interval procedure and the Fisher test could also be nonmatching procedures. None of those interpretations is specified in the supplied display; each remains an alternative rather than removal of the registered interval/test comparison.

**Direct observation versus inferred explanation:** Direct source facts are finite positive 95% bounds, patient counts and the safety test specification. The nonsignificant P values are independently reproduced calculations from those inputs. No source-printed P value, undocumented confidence construction or computational mechanism is asserted.

**Classification confirmed:** The conflicting numerical locations are both REPORT in DOC-003. DOC-001 p.6 is REPORT methods corroboration; DOC-002 p.70 is PLAN methods corroboration by prospective content. Neither corroborating location states a competing result. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. The SAP does not create P_R, and main-article method corroboration does not create S_C. Classification ambiguity: the relation of the interval procedure to the specified test is undefined, as recorded in the human question.

**Evidence state:** **reproduced**. Determining fact: the exact finite positive NNH1 confidence bounds exclude the no-effect limit while independent application of the supplied safety test to the corresponding exact patient counts is nonsignificant in both strata. This evidence state does not decide which interval/test interpretation applies.

**Exact remaining human question:** Which patient-risk comparison, sign convention and confidence transformation produced these two NNH1 intervals, and how do the reported finite bounds relate to the nonsignificant Fisher safety comparisons or to a split confidence set?

## C011 — Five panel-A P values under the companion-row reproducing test

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, eFigure 7 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), all APACHE II, CCI and SOFA rows; [p.52, eFigure 8 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), all corresponding rows; [p.53, eFigure 9 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53), all corresponding rows. Corroborating methods at [DOC-001 p.6](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) name Fisher's exact comparisons. All five affected rows and all 13 companion rows were visually read from their original page renders.

**Source printed value/text matched:** Yes. The five affected rows have P=.439, .003 and .035 for primary-response APACHE II≥25, CCI≥5 and SOFA≥10 respectively; P=.045 for day-28 SOFA≥10; P=.209 for day-90 SOFA≥10.

**Comparator matched:** Yes. The table below transcribes every integer event/denominator pair with treatment first; the source plots display placebo first. Panel captions identify primary attainment, 28-day mortality and 90-day mortality respectively. Switching column order does not change a two-sided Fisher test.

**Consistency rule applicable:** Yes. The same probability-order two-sided Fisher calculation reproduces 13 of 18 rows under the workflow display rule, with companion support in each display. The five other printed P values fail that reproducing method beyond .05 relative discrepancy. Route A category 4 applies. This comparison does not reinterpret panel-B model/interaction tests as Fisher tests.

**Calculation reproduced and display precision:** All 18 independent calculations are recorded below. For each numeric printed P with three decimals, the printed half-unit interval is P±.0005. Each exact input count's half-unit interval contains only the displayed integer for an exact contingency table. The recomputed P interval is consequently the singleton result of that table. Gap is the distance from that value to the printed half-unit interval; relative gap divides by the printed P.

| Page/outcome | Row | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Minimum gap | Relative gap |
|---|---|---|---|---:|---:|---:|---:|
| 51 primary | APACHE II≥25 | 12/38 | 8/40 | .439 | .303200218 | .135299782 | .308199958 |
| 51 primary | APACHE II<25 | 34/93 | 18/105 | .002 | .002176542 | 0 | 0 |
| 51 primary | CCI≥5 | 20/54 | 7/76 | .003 | .000158910 | .002341090 | .780363217 |
| 51 primary | CCI<5 | 26/77 | 19/69 | .475 | .474644233 | 0 | 0 |
| 51 primary | SOFA≥10 | 25/67 | 11/68 | .035 | .006531327 | .027968673 | .799104929 |
| 51 primary | SOFA<10 | 21/64 | 15/77 | .083 | .082691021 | 0 | 0 |
| 52 day 28 | APACHE II≥25 | 22/38 | 27/40 | .489 | .483109060 | .005390940 | .011024416 |
| 52 day 28 | APACHE II<25 | 35/93 | 45/105 | .472 | .471707802 | 0 | 0 |
| 52 day 28 | CCI≥5 | 24/54 | 50/76 | .020 | .019643739 | 0 | 0 |
| 52 day 28 | CCI<5 | 33/77 | 22/69 | .231 | .231037136 | 0 | 0 |
| 52 day 28 | SOFA≥10 | 35/67 | 48/68 | .045 | .034400792 | .010099208 | .224426837 |
| 52 day 28 | SOFA<10 | 22/64 | 24/77 | .721 | .720788007 | 0 | 0 |
| 53 day 90 | APACHE II≥25 | 31/38 | 32/40 | >.99 | 1.000000000 | 0 | Not applicable; inequality satisfied |
| 53 day 90 | APACHE II<25 | 59/93 | 66/105 | >.99 | 1.000000000 | 0 | Not applicable; inequality satisfied |
| 53 day 90 | CCI≥5 | 39/54 | 64/76 | .123 | .125049970 | .001549970 | .012601380 |
| 53 day 90 | CCI<5 | 51/77 | 34/69 | .045 | .044623206 | 0 | 0 |
| 53 day 90 | SOFA≥10 | 49/67 | 57/68 | .209 | .146989715 | .061510285 | .294307583 |
| 53 day 90 | SOFA<10 | 41/64 | 41/77 | .231 | .231336669 | 0 | 0 |

The five affected printed intervals are [.4385,.4395], [.0025,.0035], [.0345,.0355], [.0445,.0455] and [.2085,.2095]. Each affected relative gap exceeds .05. Two companion rows have nonzero gaps, but their relative gaps .011024416 and .012601380 are below .05 and therefore support reproduction under the stipulated display rule.

**Necessary inputs available:** Yes: all 18 integer contingency tables, their printed P values, outcome/stratum labels, and companion evidence for the reproducing test. **Exact missing inputs or definitions:** any row-specific alternative test, contingency population, sidedness or adjustment that explains the five affected P values is not printed. No patient data are necessary for the exact-table calculation; unprinted row-specific differences cannot be determined.

**Source-grounded alternative interpretation:** A distinct test or population may have generated the five P values. The immediate displays do not label a different row-specific procedure, and the other rows reproduce under the stated calculation. This alternative remains the human question, not an assumed mechanism.

**Direct observation versus inferred explanation:** Direct facts are the counts and P values in all three panels. Fisher values and gap calculations are independent reproductions. The identity of any alternative test or source of the discrepancy is inferred only as a possibility. Exact forest-plot interval endpoints are not inferred from pixels.

**Classification confirmed:** All conflicts are within the REPORT results supplement DOC-003. REPORT main-article p.6 supplies method corroboration, not a contradictory cross-document result. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No classification change or additional S_C relation is warranted.

**Evidence state:** **reproduced**. Determining fact: all five printed values and contingency inputs are confirmed at their exact source locations, the same method reproduces the 13 other rows under the display rule, and each affected relative gap exceeds .05.

**Exact remaining human question:** Which test and contingency counts produced each of the five affected panel-A P values, and what row-specific distinction explains their separation from the Fisher calculation that reproduces the companion rows?

## C012 — Repeated APACHE coefficient versus companion-row interval construction

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, eFigure 7 panel B APACHE II≥25 main-effect row and all five companion rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51); [p.52, eFigure 8 panel B corresponding row and all five companion rows](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52). Both complete panels were visually checked.

**Source printed value/text matched:** Yes, both pages print APACHE II≥25 OR **.47**, 95% CI **.30–1.62**, P=**.70**. This is the main-effect row, distinct from the APACHE-treatment row beneath it.

**Comparator matched:** Yes, all five other rows have identical points and limits on both pages, as transcribed in the calculation table. The source labels all bounds 95% CIs for ORs.

**Consistency rule applicable:** Yes. A log-symmetric ratio interval has geometric center `sqrt(lower×upper)`. The method reproduces all five other rows in each panel under the workflow half-unit/.05 rule, but not the APACHE main-effect row. This supplies the same-display method support required for Route A category 4. No approximation of a P-value test is used as the basis of this candidate; the source-printed .70 is recorded without claiming an independent Wald-test contradiction.

**Calculation reproduced and display precision:** APACHE center `sqrt(.30×1.62)=.697137002`. The endpoint ranges [.295,.305] and [1.615,1.625] imply geometric-center range [.690235467,.704006392]. The source point range [.465,.475] is separated by gap .215235467; relative discrepancy **.457947802**, above .05. Every companion point has two decimals, so its interval is point±.005; the endpoints likewise use ±.005.

| Row, on both pages | Printed OR (95% CI) | Geometric center | Center range from rounded limits | Minimum gap to printed-point range | Relative gap |
|---|---|---:|---|---:|---:|
| APACHE II≥25 | .47 (.30–1.62) | .697137002 | [.690235467,.704006392] | .215235467 | .457947802 |
| APACHE II≥25×precision immunotherapy | 1.85 (.66–5.19) | 1.850783618 | [1.842871401,1.858675604] | 0 | 0 |
| CCI≥5 | .22 (.09–.53) | .218403297 | [.211246302,.225444006] | 0 | 0 |
| CCI≥5×precision immunotherapy | 5.79 (2.34–15.05) | 5.934391291 | [5.927062932,5.941714820] | .132062932 | .022808797 |
| SOFA≥10 | .56 (.27–1.19) | .566833309 | [.560379336,.573258232] | 0 | 0 |
| SOFA≥10×precision immunotherapy | 3.08 (1.37–6.96) | 3.087911916 | [3.081164553,3.094652646] | 0 | 0 |

The CCI-treatment companion has a nonzero gap, but .022808797 is within .05 and therefore reproduces under the stipulated rule. This is not a claim that every companion interval is exactly log-symmetric to all printed digits. The independent arithmetic slightly refines approximate companion centers in the registration text (1.85046, 5.93456 and 3.08799); no source reading was changed and the method-support conclusion is unchanged.

**Necessary inputs available:** Yes for the same-display construction comparison: the point and both limits of every row, precision and interval labels. **Exact missing inputs or definitions:** the exact interval-construction procedure, coefficient standard errors/covariance and whether this APACHE row alone uses a non-log-symmetric method are not printed. A P-value test definition is not needed to establish the registered geometric-center comparison.

**Source-grounded alternative interpretation:** A non-log-symmetric interval procedure could apply to this row, or its point and bounds could come from different coefficients/analyses. The page does not identify such a row-specific distinction. The missing method remains the human question; no preferred procedure or replacement point is proposed.

**Direct observation versus inferred explanation:** Direct observations are repeated .47 (.30–1.62), .70 and the ten companion rows. Geometric-center/gap values are independent arithmetic. A substituted value, mixed row or different interval method is an inferred possible explanation only. Repetition under different outcome captions is separately recorded as C013 and is not the rule establishing C012.

**Classification confirmed:** Both conflicting rows and all method-support comparators are REPORT in DOC-003. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No PLAN comparison or cross-document result conflict participates. Classification ambiguity: the exact confidence procedure remains unspecified.

**Evidence state:** **reproduced**. Determining fact: both exact source rows match and fail the geometric construction beyond .05 relative discrepancy while all five companion rows in each panel reproduce under the same display rule. Companion arithmetic refinement is not a source-transcription correction.

**Exact remaining human question:** Which coefficient and interval-construction procedure produced .47 (.30–1.62) in each APACHE II≥25 main-effect row, and does a documented row-specific interval procedure explain its separation from the companion-row construction?

## C013 — Six-row output attributed to two different outcomes

**Status:** Pending Human Adjudication

**Locations found:** Yes. [DOC-003 p.51, complete eFigure 7 panel B and caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), and [p.52, complete eFigure 8 panel B and caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52). Also found and reread: [DOC-001 p.7, Post Hoc and Subgroup Analyses opening](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7) and [p.8, interaction-narrative continuation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8).

**Source printed value/text matched:** Yes. eFigure 7 is titled attainment of the primary endpoint according to baseline severity; its panel-B caption explicitly assigns interaction tests to the primary endpoint. eFigure 8 is titled 28-day mortality according to baseline severity; its panel-B caption explicitly assigns interaction tests to 28-day mortality. The six OR/CI/P rows are identical at displayed precision.

**Comparator matched:** Yes, the entire corresponding output array was compared row by row, including interaction markers and P-value inequality:

| Corresponding row in both panels | OR | 95% CI | P |
|---|---:|---|---:|
| APACHE II≥25 | .47 | .30–1.62 | .70 |
| APACHE II≥25×precision immunotherapy | 1.85 | .66–5.19 | .24 |
| CCI≥5 | .22 | .09–.53 | .001 |
| CCI≥5×precision immunotherapy | 5.79 | 2.34–15.05 | <.0001 |
| SOFA≥10 | .56 | .27–1.19 | .13 |
| SOFA≥10×precision immunotherapy | 3.08 | 1.37–6.96 | .007 |

Panel-A events differ between the outcomes: treatment/placebo APACHE-high 12/38 versus 8/40 for response and 22/38 versus 27/40 for death; CCI-high 20/54 versus 7/76 and 24/54 versus 50/76; SOFA-high 25/67 versus 11/68 and 35/67 versus 48/68. DOC-001 p.8 attributes significant high-CCI/high-SOFA interactions to primary attainment with eFigure 7 and to decreased 28-day mortality with eFigure 8. The p.7 opening merely begins that narrative; neither main-article page prints a separate conflicting six-row coefficient array.

**Consistency rule applicable:** Yes, the registered rule is result-to-outcome attribution under Route B, focus B/C. The same complete printed output is assigned to distinct outcomes, and the package does not distinguish the model/coding that would identify which coefficient belongs to each outcome. The affected extraction is the six-row model output, particularly the CCI and SOFA interaction coefficients and tests supporting the 28-day mortality narrative. This is a bounded attribution question; equality of rounded outputs alone does not prove that two analyses cannot coincide.

**Logical comparison reproduced and display precision:** All six rows, all 18 point/limit values and all six P entries match between pages. Their half-unit intervals overlap completely, so the numeric copy discrepancy is zero. The registered inconsistency is the unresolved attribution of that whole array to two separately named outcome analyses; it is not a claim of a beyond-rounding numeric difference. No calculation comparing modeled interactions with crude subgroup odds ratios is used. The different source-printed event counts independently confirm that the captions refer to distinct endpoints.

**Necessary inputs available:** Yes to reproduce the repeated array, distinct outcome captions, different event arrays and narrative use. **Exact missing inputs or definitions:** the dependent outcome and its coding for each fitted model, model structure/covariates, reference groups, coefficient meanings and source model outputs are not provided in sufficient detail to explain the exact repeated array. Those details are necessary to determine which output should be extracted for each outcome, not to observe the repeated array.

**Source-grounded alternative interpretation:** Two distinct outcome analyses could coincidentally yield identical rounded output, or coding/model distinctions could lead to the displayed equality. Their existence is possible, but no supplied statement identifies one. No copying mechanism is asserted, and no modeled-versus-crude contradiction is alleged.

**Direct observation versus inferred explanation:** Direct observation is six identical displayed OR/CI/P rows under primary-response and 28-day-death captions and narrative use for both outcomes. Unclear coefficient-to-outcome mapping is the bounded consequence recorded for human review. A duplicated production step, misassigned caption, or coincident output is an inferred possible explanation only.

**Classification confirmed:** The conflicting outcome attribution is within DOC-003 REPORT content. DOC-001 pp.7–8 are REPORT narrative corroboration, without a directly conflicting coefficient array. Primary relationship **S_W**; all relationships **S_W**; review domain **report_internal_inconsistency**, because the issue concerns which outcome the numeric array belongs to. C012 separately handles interval construction. No S_C is added for narrative corroboration and no PLAN relationship exists. Classification ambiguity: exact model/output assignment remains unspecified, not the document roles.

**Evidence state:** **reproduced**. Determining fact: direct-source comparison confirms the entire identical array, the distinct explicit outcome labels and unresolved output attribution in immediate context. This state records that observation, not a determination that the analyses must have different numerical outputs.

**Exact remaining human question:** Which outcome model generated each panel-B array, and which coefficients, intervals and tests apply to primary response and to 28-day mortality for each of the six displayed rows? If distinct analyses yielded the same rounded array, what source specification identifies their outcome coding and model mapping?

## C014 — 90-day APACHE-treatment point outside its interval

**Status:** Pending Human Adjudication

**Location found:** Yes. [DOC-003 p.53, eFigure 9 panel B APACHE II≥25×precision immunotherapy row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53). The same page's panel-B caption explicitly identifies 90-day mortality. The interaction row was distinguished from the APACHE main-effect row above it.

**Source printed value/text matched:** Yes. OR **.11**, 95% CI **.36–3.42**, P=**.86**.

**Comparator matched:** Yes. The row's lower .36 and upper 3.42 are printed in the 95% CI column on the same line; .86 is printed in its P-value column. The source row label and outcome caption match the registration.

**Consistency rule applicable:** Yes. An estimate must be contained in its stated interval. Point .11 is below lower bound .36. This is Route A category 1; no exact fitted model, confidence construction or raw data are required to check containment.

**Calculation reproduced and display precision:** `.11 < .36`. Point half-unit interval [.105,.115], lower-bound interval [.355,.365], upper-bound interval [3.415,3.425]. Even the greatest allowed point is below the least allowed lower bound: minimum gap `.355−.115=.240`; relative gap `.240/.11=2.181818182`. No half-unit reading permits containment. Route A category 1 is never removed by the .05 display rule. The printed CI contains 1 and P>.05; the registered issue is point containment, not a separately inferred interval/P disagreement.

**Necessary inputs available:** Yes: point, both limits, row label, confidence level and outcome. **Exact missing inputs or definitions:** the underlying coefficient/model output that identifies whether the point or limits belong to a different quantity is not supplied. That input is unnecessary for containment reproduction but needed to identify the intended row output.

**Source-grounded alternative interpretation:** A digit/decimal substitution or an interval assigned from another coefficient could account for the reading. The source does not select an explanation; a geometric center or neighboring result is not adopted as a replacement point.

**Direct observation versus inferred explanation:** Direct observation is the printed .11 and .36–3.42 on the named interaction row. Noncontainment is direct arithmetic. A publication-production mechanism or intended alternative value is an inference only.

**Classification confirmed:** Point and comparator limits are REPORT in the same DOC-003 display. Primary relationship **S_W**; all relationships **S_W**; review domain **statistical_results**. No classification change, PLAN comparison or cross-document discrepancy is involved.

**Evidence state:** **reproduced**. Determining fact: exact source point and limits match, and their half-unit intervals cannot satisfy containment.

**Exact remaining human question:** Which odds ratio and 95% confidence limits belong to the APACHE II≥25×precision-immunotherapy row for 90-day mortality, and what source output identifies that point/interval pairing?

## Bounded remaining inputs

Seven IDs covered, seven evidence states `reproduced`, zero `reproduced_after_transcription_correction`, zero `not_reproduced`, zero classification changes. Every registered affected source location is found; the definition-support location DOC-003 p.29 was additionally inspected. No unreadable page or OCR limitation remains in this shard. Remaining inputs are the exact unadjusted computation/population for C008, direction convention for C009, NNH confidence construction and test mapping for C010, row-specific tests/counts for C011, interval procedure for C012, outcome-model attribution for C013, and underlying point/interval pairing for C014. These bound the explanatory human questions; they do not authorize changing or deleting IDs.
