<a id="C001"></a>

## C001 — Primary mean/Welch versus responder/Fisher specification

**Status:** Pending Human Adjudication

**Candidate statement:** The original protocol specifies a between-arm mean SOFA analysis with Welch’s t test, whereas the later SAP and report specify a patient-level responder analysis with Fisher’s exact test and a different death-handling rule. The corresponding day-15 endpoint follows the same pattern.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol vs PLAN SAP and REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective protocol and SAP are PLAN; the main article is REPORT. The protocol-to-report comparison supplies P_R and the original-protocol-to-later-SAP difference supplies P_P. P_R takes precedence.

**Classification ambiguity:** The later SAP agrees with the reported responder specification and may represent an authorized revision. The supplied package does not explicitly map the original endpoint, test and death rule to that revision.

**Exact source locations:** PLAN [DOC-002 p.7 synopsis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.24 primary endpoint/death rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=24), [p.25 corresponding day-15 mean](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 Welch analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.66 SAP responder/death rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), [p.67 Fisher analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 day-15 construction](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.69 day-15 responder continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69); REPORT [DOC-001 p.3 endpoint](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 imputation/secondary definition](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2 and statistical analyses](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).

**Source evidence:** Protocol pp.7 and 24 specify the comparative difference in mean total SOFA through day 9, an arm-level decrease of at least 1.4 points, and averaging through death for patients dying before day 9. P.27 names Welch’s t test. P.25 states the corresponding day-15 mean endpoint. SAP pp.66–67 instead form each patient’s baseline minus the mean of days 2–9, classify attainment/nonattainment, replace missing scores after death with 24, and use Fisher’s exact test with ORs and 95% CIs. Pp.68–69 repeat that approach through day 15. The article reports primary attainment in 46/131 versus 26/145, OR 2.48 (95% CI 1.42–4.32), P=.002.

**Reported-versus-comparator:** Reported: binary patient-level attainment, Fisher comparison and death-score imputation of 24. Comparator: original continuous between-arm mean difference, Welch comparison and observed mean through death. The later SAP corroborates the report while differing from the original protocol.

**Reasoning procedure:** Match the current-trial endpoint window, unit of analysis, test and death handling across original protocol, later SAP and article. Treat the related day-15 change as another location of the same specification pattern. Do not equate a continuous mean comparison with a dichotomized responder comparison merely because both mention 1.4 points.

**Calculation:** This is a categorical endpoint/test/death-rule comparison; half-unit rounding intervals and a numeric relative discrepancy are not applicable. The reported primary responder table itself yields (46×119)/(85×26)=2.4769, consistent with printed 2.48. The strict >1.4 versus ≥1.4 symbol difference is excluded from this candidate: integer daily-score averages on 8- or 14-value grids cannot equal 1.4, since 1.4×8=11.2 and 1.4×14=19.6 are nonintegers.

**Affected result or extracted value:** The primary day-9 responder definition, analysis method and death handling; the analogous day-15 endpoint construction; interpretation of the reported primary OR 2.48.

**Why context does not resolve it:** Route A, category 5 covers a replaced planned primary analysis and changed endpoint construction. Agreement between the later SAP and report is retained as a revision alternative, rather than removing the source-confirmed original-to-report comparison.

**Alternative source-grounded interpretations:** An authorized SAP revision or operational clarification may connect the specifications. Its operative version history and scope are not printed. Individual SOFA trajectories would be needed to quantify any participant-level consequences; no such consequences are asserted.

**Mechanical evidence recheck:** Every cited original page was rendered directly and visually reread. The rechecker confirmed both specifications, their document roles and the P_R/P_P precedence without a source-transcription correction. The independent audit confirmed inclusion.

**Potential downstream evidence impact:** A data extractor could record the responder effect together with an endpoint/test/death-handling specification that does not identify its relationship to the original continuous design. This review does not quantify a change in treatment effect or trial conclusions.

Checker provenance retained: F-XS-001 INCLUDE; F-ST1-009 duplicate.

<a id="C002"></a>

## C002 — Home-discharge versus ICU-discharge carry-forward eligibility

**Status:** Pending Human Adjudication

**Candidate statement:** The SAP and article methods condition last-observation-carried-forward SOFA values on discharge home, while the article results and eTable 8 describe ICU discharge. Their eligibility sets are not explicitly equated for the 23 carry-forward cases.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN SAP vs REPORT main article and REPORT results supplement; REPORT main article internal descriptions

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The PLAN-home versus REPORT-ICU comparison supplies P_R; article-home versus supplement-ICU supplies S_C; article-home versus article-ICU supplies S_W. P_R takes precedence and places the candidate in protocol_report.

**Classification ambiguity:** It is unknown whether all 23 ICU discharges also constituted home discharges or whether ICU terminology abbreviates the operational home criterion. The roles and precedence are otherwise explicit.

**Exact source locations:** PLAN [DOC-002 p.66](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66); REPORT [DOC-001 p.3 daily ICU observation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 home-discharge rule](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 ICU-discharge result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [DOC-003 p.20 eTable 8](../../../joi250116supp2_prod_1771885794.27755.pdf#page=20), [p.46 sensitivity population](../../../joi250116supp2_prod_1771885794.27755.pdf#page=46).

**Source evidence:** SAP p.66 carries forward the last recorded SOFA after discharge home before day 9; article p.5 uses that rule and separately names loss to follow-up. Article p.3 describes daily SOFA during ICU stay until discharge, and p.6 attributes 8.3% carry-forward to ICU discharge. eTable 8 names earlier ICU discharge and prints assumed day-9 counts of 10 and 13. eFigure 2 excludes carried-forward discharge cases and reports 38/121 (31.4%) versus 19/132 (14.4%), OR 2.72 (1.47–5.05), P=.001.

**Reported-versus-comparator:** Printed methods/SAP criterion: home discharge before day 9. Printed results/supplement criterion: ICU discharge before day 9. The compared quantities are the observation window and carry-forward eligibility, rather than the coherently reported patient counts.

**Reasoning procedure:** Compare the explicit triggering event across the SAP, article methods/results and supplement. Verify carry-forward totals and sensitivity exclusions independently. Keep an operational-rule question separate from any unobserved patient destination or actual reclassification.

**Calculation:** 10+13=23 and 23/276×100=8.333333%, consistent with printed 8.3%. Conservatively allowing half-unit ranges gives [22/276.5,24/275.5]×100=[7.95660%,8.71143%], overlapping printed [8.25%,8.35%]; gap=0 and relative discrepancy=0. Sensitivity denominator changes also reconcile: 131−121=10 and 145−132=13. No arithmetic discrepancy is registered.

**Affected result or extracted value:** The primary endpoint’s missing-data eligibility and observation window, and the definition of the carry-forward-excluded sensitivity population.

**Why context does not resolve it:** All Route B criteria apply: the primary missing-data rule is in focus; immediate context does not say that ICU discharge and home discharge identified the same patients at the same time; the distinction can affect how the primary and sensitivity analyses are interpreted or extracted.

**Alternative source-grounded interpretations:** All ICU discharge cases may also have been home discharges, or the result wording may summarize the home rule. The package does not establish either explanation. Exact home/ward discharge dates and the applied stop-observation transition are unavailable, so no participant-level change is inferred.

**Mechanical evidence recheck:** The exact SAP, article and supplement pages were visually confirmed. Counts and sensitivity denominator differences were reproduced and found coherent. The operational-label distinction remained, and the rechecker and auditor confirmed the full P_R/S_C/S_W classification.

**Potential downstream evidence impact:** An evidence extractor could record ICU discharge or home discharge as the primary missing-data trigger, with different implications for the observation window. No actual patient reclassification or resulting effect change is established.

Checker provenance retained: F-XS-007 INCLUDE.

<a id="C003"></a>

## C003 — Infection and omics outcome-status pattern

**Status:** Pending Human Adjudication

**Candidate statement:** Current-trial infection resolution is secondary in the protocol synopsis, later SAP and report, but exploratory in the detailed protocol and endpoint appendix. The same secondary/exploratory pattern affects omics outcomes within PLAN material.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol synopsis vs PLAN detailed protocol and SAP vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** The detailed PLAN infection hierarchy versus REPORT supplies P_R. The synopsis versus detailed PLAN infection/omics hierarchy supplies P_P. P_R takes precedence; the omics component remains plan-internal and creates no asserted missing REPORT result.

**Classification ambiguity:** The synopsis and later SAP may represent the intended or revised hierarchy, or secondary may have been used as an umbrella term. The detailed protocol explicitly separates exploratory endpoints and does not state that convention.

**Exact source locations:** PLAN [DOC-002 p.7 synopsis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.25 detailed hierarchy](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 infection test hierarchy](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.57 resolution appendix](../../../joi250116supp1_prod_1771885794.26255.pdf#page=57), [p.70 SAP infection](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.5 prespecified secondary endpoints](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 main secondary table](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 sixth secondary result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7).

**Source evidence:** Protocol p.7 lists infection resolution and genomic, epigenomic, proteomic, metabolomic and microbiomic surrogate biomarkers as secondary endpoints. P.25 places both under a distinct exploratory heading; p.27 names their analyses exploratory. P.57 labels the current ImmunoSep infection-resolution appendix as exploratory. SAP p.70 places infection resolution in its secondary sequence. Article pp.5–7 calls infection resolution by day 15 one of six prespecified secondary endpoints and reports OR 0.59 (0.38–0.91), P=.02.

**Reported-versus-comparator:** Reported/SAP/synopsis infection status: secondary. Detailed protocol and resolution appendix status: exploratory. Omics shows the same synopsis-versus-detailed-plan status difference, without a reported omics counterpart in this comparison.

**Reasoning procedure:** Match the same current-trial outcomes under the printed endpoint headings and analysis hierarchy. Distinguish current ImmunoSep content from historical PROVIDE material. Consolidate the repeated hierarchy pattern into one candidate without inferring an obligation to report exploratory omics.

**Calculation:** Outcome status is categorical; half-unit rounding and numeric relative discrepancy do not apply. OR 0.59, CI 0.38–0.91 and P=.02 identify the affected infection result, rather than establishing another numeric inconsistency.

**Affected result or extracted value:** The prespecified status assigned to the day-15 infection-resolution result and the accompanying plan-internal omics hierarchy.

**Why context does not resolve it:** Route A, category 5 covers a prespecified outcome whose status changes. Distinct secondary and exploratory headings are source-confirmed; an unprinted umbrella or amendment convention does not remove that comparison.

**Alternative source-grounded interpretations:** The synopsis and later SAP support the article’s secondary classification and could reflect a revised hierarchy. An operative amendment/version or explicit umbrella definition is missing. No missing omics effect or requirement to publish exploratory omics is inferred.

**Mechanical evidence recheck:** All affected current-trial hierarchy headings and report locations were directly visually reread. Secondary versus exploratory designations reproduced without transcription changes. The audit confirmed P_R/P_P precedence and the bounded omics component.

**Potential downstream evidence impact:** A systematic-review extraction could classify the infection result as a prespecified secondary or exploratory outcome depending on the supplied location. The candidate concerns that status and plan hierarchy, not a demonstrated change in the effect estimate.

Checker provenance retained: F-XS-004 INCLUDE; F-ST1-012 duplicate.

<a id="C004"></a>

## C004 — Immune-reversal endpoint window, composite and ascertainment

**Status:** Pending Human Adjudication

**Candidate statement:** The planned day-15 immune-reversal endpoint uses a biomarker conjunction and death/nonattainment handling, whereas the report ties the displayed result to day 28 with sustained biomarker change and at least two serial draws in a 125-patient subset.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol and SAP vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** Protocol/SAP endpoint definitions are PLAN; article and results-supplement definitions are REPORT. Their prospective-versus-reported comparison supplies P_R. Report locations corroborate one another; contextually resolved target wording and plan shorthand add no independent relationships.

**Classification ambiguity:** A supplementary day-28 analysis or an unprinted applied ferritin criterion could explain parts of the comparison. The supplied package does not map the displayed counts to a distinct day-15 result or identify the operative revised definition.

**Exact source locations:** PLAN [DOC-002 p.25](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.69](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), [p.70 continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.5 definition](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2/footnote](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 by-day-28 result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.50 eFigure 6](../../../joi250116supp2_prod_1771885794.27755.pdf#page=50).

**Source evidence:** Protocol p.25 specifies day-15 reversal: MALS ferritin decreases at least 15%; immunoparalysis Quantibrite exceeds 8000 AB/C together with ferritin below 4420 ng/mL. SAP pp.69–70 censors at day 15, repeats that conjunction and classifies death before day 15 as nonachievement. Article pp.5–6 omits the immunoparalysis ferritin conjunction in its printed definition and requires sustained change plus at least two serial draws; fewer draws mean nonattainment. It reports 46/59 (78.0%) versus 32/66 (48.5%), OR 3.76 (1.72–8.22). P.7 ties those counts to day 28. eFigure 6 describes draws and censoring through day 28, missing draws from death/discharge, the 59/66 sampled population and Cox HR 2.38 (1.50–3.77).

**Reported-versus-comparator:** Planned: day 15, phenotype-specific biomarker criteria including the immunoparalysis ferritin conjunction, and pre-day-15 death handling. Reported: displayed day-28 result with sustained-change/two-draw rules and a 125-person sampled denominator, without that printed conjunction.

**Reasoning procedure:** Compare the window, composite components, persistence/serial-draw requirements and denominator/death rules as one endpoint-specification pattern. Use the report’s absolute HLA-DR target footnote/caption to resolve isolated increase-of wording. Do not reinterpret a coherent subset count as a numerical denominator discrepancy.

**Calculation:** Categorical specification differences have no rounding interval. Subset size is coherent: 59+66=125. The percentages reproduce: 46/59×100=77.9661% lies in [77.95%,78.05%], and 32/66×100=48.4848% lies in [48.45%,48.55%]. These identifiers therefore have zero gap to their displayed percentage intervals. The specification comparison does not calculate a revised endpoint count or effect.

**Affected result or extracted value:** The immune-reversal endpoint’s follow-up window, composite definition, ascertainment and analytic population; extraction of its OR 3.76 and day-28 Cox HR 2.38.

**Why context does not resolve it:** Route A, category 5 covers changes in a prespecified outcome/composite definition. Direct-source confirmation retains day 15 versus day 28 and the changed printed conjunction/persistence rules. Those are separate from immediately resolved absolute-target wording.

**Alternative source-grounded interpretations:** The day-28 time-to-event analysis may supplement a day-15 endpoint, or ferritin below 4420 may have been applied without repetition. The displayed counts are expressly tied to day 28, and no separate day-15 version is located. Exact biomarker/death/discharge histories, operative revision and disposition of cases without sufficient serial draws are unavailable.

**Mechanical evidence recheck:** Every planned and reported endpoint page was directly visually confirmed. Report counts and percentages reconcile. The recheck and audit reproduced the window/composite/ascertainment comparison and confirmed P_R without adding contextually resolved P_P, S_C or S_W relationships.

**Potential downstream evidence impact:** An evidence extractor could associate the immune-reversal effect with different follow-up windows, composite components or sampled-population rules. No participant-level reclassification or numerical consequence is established.

Checker provenance retained: F-XS-003 INCLUDE; F-ST1-011 duplicate.

<a id="C005"></a>

## C005 — Continuous versus binary primary-outcome power basis

**Status:** Pending Human Adjudication

**Candidate statement:** The protocol bases primary-outcome power on a continuous mean SOFA difference, while the report bases it on binary attainment probabilities of 40% versus 20%; no supplied prospective calculation links those distinct bases.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol power specification vs REPORT main article power specification

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route B

**Classification rationale:** The prospective protocol power section is PLAN and the article power section is REPORT. Their effect-scale/input comparison supplies P_R and protocol_report. No separate plan-only or report-only numerical sample-size conflict is included.

**Classification ambiguity:** A revised binary calculation may have retained the same sample target, or response planning may have accompanied the continuous calculation. The revision, exact procedure and interpretation of the protocol’s dispersion wording are not supplied.

**Exact source locations:** PLAN [DOC-002 p.25 power introduction](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.26 calculation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=26); REPORT [DOC-001 p.5 Sample Size Calculation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5). The complete supplied SAP pp.63–72 has no revised binary power calculation.

**Source evidence:** Protocol pp.25–26 power a 1.4-point mean SOFA reduction with printed dispersion 3.2, 90% power, 5% significance, a two-sided independent-groups t test and nQuery Advisor 6.02. It states 117 participants per arm and 280 after approximately 15% dropout. Its 40%/60% pair describes anticipated phenotype recruitment, not treatment-arm response probabilities. Article p.5 anticipates primary attainment in 40% versus 20%, with the same nominal power, significance level and sample targets. The complete supplied SAP contains no revised binary calculation.

**Reported-versus-comparator:** Reported: binary response probabilities 0.40 and 0.20. Comparator: mean difference 1.4 with dispersion 3.2 and an independent-groups t-test calculation. Common 90% power, 5% significance and 117/group do not themselves connect these distinct planning assumptions.

**Reasoning procedure:** Compare the printed primary-outcome scale, effect-size inputs and calculation procedure. Keep normal approximations and dropout arithmetic as contextual diagnostics rather than treating an unidentified exact method as a reproduced sample-size conflict.

**Calculation:** No numeric sample-size inconsistency is registered. The contextual dropout calculation 234/.85=275.2941 differs from 280 within the workflow rule. Allowing 117±.5 per arm and 15%±.5 percentage points gives [233/.855,235/.845]=[272.5146,278.1065]; printed 280 has [279.5,280.5], leaving gap 1.3935 and relative discrepancy about .00498≤.05. Normal power approximations of 109.79/group for the continuous inputs and 108.24/group for the binary inputs are diagnostics only; input rounding and the unreported exact procedure do not establish that 117 fails. Rounding cannot identify an operative continuous-to-binary design mapping.

**Affected result or extracted value:** Interpretation and extraction of the claimed 90% power for the reported binary primary endpoint and its prospective sample-size basis.

**Why context does not resolve it:** All Route B criteria apply: power assumptions are in focus; the immediate text does not link a continuous mean calculation to the stated binary probabilities; that linkage determines what prospective power claim applies to the reported responder endpoint.

**Alternative source-grounded interpretations:** A prospective revision or parallel binary calculation could support the article while preserving 117/group. Its formula, continuity convention, inputs and version are missing. No preferred calculation, actual achieved power or underpowering consequence is asserted.

**Mechanical evidence recheck:** Both original power sections were directly visually reread, and the complete SAP map plus analytic pages were checked for a revised calculation. The effect-scale difference reproduced. The auditor confirmed that approximate sample-size and dropout comparisons do not create an additional candidate.

**Potential downstream evidence impact:** A review could copy the 90% binary-response power claim without identifying the prospective calculation that supports that scale. The candidate does not establish a numerical shortfall in sample size or achieved power.

Checker provenance retained: F-XS-002 INCLUDE; F-ST1-010 duplicate.

<a id="C006"></a>

## C006 — Binary planned versus ordinal reported infection analysis

**Status:** Pending Human Adjudication

**Candidate statement:** The plan prescribes a binary resolved/not-resolved infection comparison with Fisher/Mantel–Haenszel analysis, while the report presents four-state ordinal regression without mapping it to the planned binary result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol and SAP infection analysis vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Qualifying route:** Route B

**Classification rationale:** Both protocol and SAP locations are PLAN; article and results supplement are REPORT. P_R governs the analysis-specification difference. The reported ordinal displays corroborate each other and create no independent S_C conflict.

**Classification ambiguity:** The ordinal analysis may supplement or replace the binary analysis. The supplied package does not identify that mapping, a revised specification or a corresponding binary estimate/test.

**Exact source locations:** PLAN [DOC-002 p.27 Fisher/Mantel–Haenszel infection analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.70 binary resolved/not-resolved SAP analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.6 Table 2/statistical analysis/SAP-following statement](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 ordinal result](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.49 four-state figure](../../../joi250116supp2_prod_1771885794.27755.pdf#page=49).

**Source evidence:** Protocol p.27 names Fisher’s exact infection-resolution comparison and Mantel–Haenszel OR/CIs. SAP p.70 explicitly splits attainment/nonattainment of resolution and prescribes those methods with infection/immune strata. Article p.6 states ordinal regression for resolved, intermediate, failure and superinfection while stating that analyses followed the SAP. Counts are 58,11,32,30 of 131 versus 46,9,44,46 of 145. Article pp.6–7 and eFigure 5 report a worse-disposition OR 0.59 (0.38–0.91), with P=.02 in the article and .018 in the figure.

**Reported-versus-comparator:** Reported effect: four-category ordinal worse-disposition OR 0.59. Planned comparison: binary infection resolution/nonresolution analyzed with Fisher and Mantel–Haenszel. Reported resolution counts 58/131 and 46/145 do not supply a named planned binary effect/test.

**Reasoning procedure:** Match the same infection outcome across the plan and reported model, retaining the explicitly stated ordinal contrast. Distinguish an analysis-specification comparison from a model-versus-crude arithmetic comparison, and from a preferred-analysis recommendation.

**Calculation:** The category counts total 58+11+32+30=131 and 46+9+44+46=145. P=.018 has half-unit interval [.0175,.0185], overlapping P=.02’s [.015,.025]; copy gap and relative discrepancy=0. A crude binary resolution OR is (58×99)/(73×46)=1.70935, but this is diagnostic only and is not a conflicting comparator for the modeled ordinal OR .59. Numeric rounding does not equate the two stated analysis specifications.

**Affected result or extracted value:** Interpretation/extraction of the infection-resolution effect as a binary resolution contrast or ordinal disposition contrast, and its mapping to the prespecified analysis.

**Why context does not resolve it:** All Route B criteria apply: the planned analysis is in focus; immediate report context clearly identifies ordinal regression but does not reconcile it with the explicit binary plan; the distinction changes the quantity represented by the infection OR.

**Alternative source-grounded interpretations:** Ordinal regression could be an added analysis or a replacement; the worse-disposition caption could summarize the ordinal estimand. A revised specification, corresponding binary output, and exact ordinal coding/link/adjustment details are not supplied. No requirement that the model equal a crude ratio is imposed.

**Mechanical evidence recheck:** All five cited plan/report locations were directly visually confirmed. The binary/ordinal comparison reproduced; counts and P-value copies reconcile. Rechecker and auditor confirmed P_R and the bounded plan-mapping question.

**Potential downstream evidence impact:** A meta-analysis extractor could treat the ordinal .59 as a binary infection-resolution estimate if the analysis mapping were overlooked. No actual propagation or consequence to a pooled result is established.

Checker provenance retained: F-XS-005 INCLUDE; F-ST1-013 duplicate.

<a id="C007"></a>

## C007 — Prespecified primary and key-secondary analysis families not located

**Status:** Pending Human Adjudication

**Candidate statement:** Four prespecified primary/key-secondary analysis families are not located in the complete supplied article and results supplement, and the package does not explicitly map them to replacement or withdrawn analyses.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP primary and key secondary analyses vs complete REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route A, category 5

**Classification rationale:** The SAP specifies prospective analyses and is PLAN; the complete article and results supplement are REPORT. Their prescribed-versus-supplied reporting comparison supplies P_R. Closest report destinations are context, rather than mutually conflicting results that add report/report relationships.

**Classification ambiguity:** Reported model interactions may have replaced planned homogeneity tests, or additional results may exist outside the supplied package. Neither mapping is identified in the supplied report. Nonlocation does not establish that the analyses were never performed.

**Exact source locations:** PLAN [DOC-002 p.67 immune-state response homogeneity](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 survivor secondary means and 28-day immune-state mortality](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.71 severity/homogeneity and antibiotics](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71), [p.72 antibiotic-primary continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=72); REPORT [DOC-001 p.5 endpoint definitions](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 methods/results](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 response/mortality/post hoc results](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [p.8 interaction continuation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), [DOC-003 p.16 antibiotic footnote](../../../joi250116supp2_prod_1771885794.27755.pdf#page=16), [p.21 primary model](../../../joi250116supp2_prod_1771885794.27755.pdf#page=21), [p.22 immune response](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22), [p.23 subset baseline](../../../joi250116supp2_prod_1771885794.27755.pdf#page=23), [p.24 subset baseline continuation](../../../joi250116supp2_prod_1771885794.27755.pdf#page=24), [p.47 overall mortality](../../../joi250116supp2_prod_1771885794.27755.pdf#page=47), [p.51 primary severity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), [p.52 28-day severity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), [p.53 90-day severity](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53), with absence assessed against complete DOC-001 pp.1–12 and DOC-003 pp.1–54 result maps and source-linked text.

**Source evidence:** SAP p.67 prescribes primary-response OR homogeneity across MALS/immunoparalysis with Breslow–Day and Tarone. P.68 prescribes 28-day mortality comparisons within those immune states. P.71 prescribes primary and key-28-day severity-stratum OR/homogeneity analyses with immune-state stratification and named homogeneity tests. Pp.71–72 prescribe primary response by appropriate/non-appropriate antibiotics. The report supplies phenotype-specific response ORs, overall mortality, baseline antibiotic information, severity-specific comparisons and model interactions, but no identified outputs or replacement statements for the four families.

**Reported-versus-comparator:** Planned families versus closest supplied content:

| Prespecified family | Closest report content | Specific output not located |
|---|---|---|
| Primary immune-state response homogeneity | Article p.7 and eTable 10 p.22 phenotype response estimates | Breslow–Day/Tarone comparison of immune-state ORs |
| Key-secondary 28-day mortality within MALS/IP | Article pp.6–7 and eFigure 3 p.47 overall mortality | Within-immune-state 28-day mortality comparisons |
| Primary response by antibiotic appropriateness | Baseline antibiotic frequencies 34/41 versus 33/38 and eTable 6 footnote p.16 | Responder comparisons/effects/tests by antibiotic appropriateness |
| Primary/key-28-day severity homogeneity and immune-within-severity | eFigures 7/8 pp.51–52 severity comparisons and model interactions | Named homogeneity outputs and immune-within-severity results or explicit replacement mapping |

**Reasoning procedure:** Check complete DOC-001 pp.1–12 and DOC-003 pp.1–54 maps, the supplement index of 15 eTables/9 eFigures and fresh full-source native text; visually confirm the plausible table/figure destinations where native extraction is incomplete. Searches include Breslow, Tarone, homogeneity, appropriate, antibiotic, MALS, immunoparalysis, mortality, survivor, interaction, replacement, withdrawal and amendment. Consolidate the four structurally similar primary/key-secondary reporting-absence families into one candidate.

**Calculation:** This is bounded nonlocation of named analyses, not a numerical discrepancy; half-unit intervals and relative discrepancy are not applicable. Separate subgroup ORs are not homogeneity tests, baseline antibiotic counts are not responder outcomes, and overall mortality is not a within-immune-state result. The supplied data do not permit calculating the absent effects. Complete reporting scope is 12+54=66 pages.

**Affected result or extracted value:** Availability and prespecification mapping of the four named primary/key-secondary analysis families, including their subgroup effects and homogeneity tests.

**Why context does not resolve it:** Route A, category 5 covers planned primary or key-secondary analyses that are not reported. The closest supplied outputs do not identify the named analyses or explicitly replace/remove them. The claim is limited to nonlocation in the complete supplied reporting.

**Alternative source-grounded interpretations:** The report’s interaction analyses could replace homogeneity tests; phenotype response estimates could have been regarded as sufficient; results could exist in an unsupplied document. No such mapping is printed. Missing named outputs, subgroup cross-tabulations and replacement/removal specifications prevent effect reconstruction. The survivor-only day-1–9 mean/Student t comparison is non-key secondary context and is excluded from this candidate, as are non-key 90-day immune analyses, day-15 survivor means and exploratory ROC/omics absences. Original mean/Welch replacement is separately C001.

**Mechanical evidence recheck:** The rechecker verified every prospective statement, complete page maps/index, full-source text search and all plausible report destinations, using direct visual checks for figure content. The auditor confirmed all four included families and explicitly reaffirmed the non-key survivor-mean exclusion. The evidence state records bounded supplied-report nonlocation, not whether analyses were performed.

**Potential downstream evidence impact:** An extractor could lack named prespecified primary/key-secondary subgroup or homogeneity results, or assign nearby model interactions to them without an explicit mapping. No unreported effect size, selective-reporting mechanism or conclusion change is inferred.

Checker provenance retained: F-XS-006 INCLUDE; F-ST1-015 duplicate.


