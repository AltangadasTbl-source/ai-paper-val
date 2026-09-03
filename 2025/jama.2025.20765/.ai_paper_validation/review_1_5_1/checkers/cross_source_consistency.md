# Cross-Source Consistency Review

## Scope, method, and boundaries

This checker reviewed the complete current-run quantitative maps for DOC-001 (main article, PDF pp. 1-9), DOC-002 (protocol/SAP, PDF pp. 1-109), and DOC-003 (supplementary tables/figure, PDF pp. 1-16). It used the direct-source-linked current-run maps and global relationship inventories only; no legacy candidate, checker, or report artifact was used as scientific input.

Before calling a difference, the checker matched the study phase/version where supplied, population, time point, arm contrast, endpoint definition, analysis set, measure, model/adjustment status, unit, reference group, and displayed precision. Prospective protocol quantities are not treated as observed trial results. All items below are provisional quality-control candidates for human adjudication; no C ID, severity, disposition, or correction is assigned.

## Qualifying provisional candidates

### XC001 — Same protocol sample-size specification names two different facility totals

- **Category:** Cross-document numeric inconsistency.
- **Exact locations:** DOC-002 PDF p. 10 (`joi250093supp1_prod_1768590553.08963.pdf#page=10`), protocol sample-size specification; DOC-002 PDF p. 26 (`joi250093supp1_prod_1768590553.08963.pdf#page=26`), repeated sample-size specification.
- **Matched result:** prospective total of 2,384 smokers with TB, approximately 50 recruits per health facility/clinic, 10% without a primary outcome, 16 pilot participants, Phase-3 16 A/8 C clusters, and Phase-4 20 A/20 B clusters.
- **Printed values:** p. 10 says approximately 50 recruits from **44 health facilities**; p. 26 says approximately 50 recruits from **48 health clinics [clusters]**.
- **Comparison logic:** the surrounding total, phase allocations, pilot inclusion, assumptions, and units identify the two passages as repetitions of the same prospective specification. The site count changes from 44 to 48 without a stated version/date or reconciliation. Moreover, 2,384/44 = 54.18 and 2,384/48 = 49.67, so only the latter is approximately 50 under ordinary rounding.
- **Supported alternatives / limits:** the two passages could preserve different amendment states, but neither mapped passage identifies one as superseded. This is a planning-document issue, not a comparison with the observed 1,080-person Phase-3 trial result.
- **Human verification question:** Which facility count governed the 2,384-participant protocol calculation, and should the other repeated passage be corrected or explicitly version-labelled?

### XC002 — Later protocol gives incompatible facility counts for its 2,716-participant plan

- **Category:** Cross-document numeric inconsistency.
- **Exact locations:** DOC-002 PDF p. 46 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`), high-level plan; DOC-002 PDF pp. 49-50 (`joi250093supp1_prod_1768590553.08963.pdf#page=49`, `joi250093supp1_prod_1768590553.08963.pdf#page=50`), Diagram 1; DOC-002 PDF p. 62 (`joi250093supp1_prod_1768590553.08963.pdf#page=62`), statistics section.
- **Matched result:** later-protocol, prospective phases 2-4 recruitment plan including 16 pilot participants.
- **Printed values:** p. 46 says **2,716** smokers, approximately **43** recruits from **63** health facilities/clusters. Diagram 1 gives 27 Phase-3 sites and 36 Phase-4 sites, also **63** sites, with 1,096 (including 16 pilot) + 1,620 = **2,716**. p. 62 instead says **2,716** smokers, approximately **50** recruits from **48** health clinics/clusters.
- **Comparison logic:** the 63-site version reconciles arithmetically: 2,716/63 = 43.11. The p. 62 48-site version is not the Diagram 1 site total and 2,716/48 = 56.58, not approximately 50 at the displayed precision.
- **Supported alternatives / limits:** p. 62 could be an unmarked carry-forward from an earlier plan or use a distinct, unstated subset of clinics. No supplied text attaches such a qualifier to its 48-clinic statement.
- **Human verification question:** Does the p. 62 statistic-section statement require a 63-site/approximately-43 correction, or does 48 denote a specified subset that should be named?

### XC003 — Protocol intervention dose changes from 178 to 134 SMS messages without a supplied reconciliation

- **Category:** Cross-document numeric inconsistency / measure-label inconsistency.
- **Exact locations:** DOC-002 PDF p. 16 (`joi250093supp1_prod_1768590553.08963.pdf#page=16`); DOC-002 PDF p. 51 (`joi250093supp1_prod_1768590553.08963.pdf#page=51`); DOC-002 PDF p. 80 (`joi250093supp1_prod_1768590553.08963.pdf#page=80`); DOC-001 PDF pp. 1 and 3 (main intervention description; `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1`, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3`); DOC-002 PDF pp. 101-109 (`joi250093supp1_prod_1768590553.08963.pdf#page=101`).
- **Matched result:** mTB-Tobacco intervention message dose for a six-month intervention participant.
- **Printed values:** DOC-002 p. 16 says **178 SMS messages over 6 months** (4-5/day for first 2 months, 2-3/day for next 2, 1-2/week for last 2). DOC-002 p. 51 says **134 SMS messages over 6 months** (4-5/day for first 2 months, 1-2/day for next 2, 1/week for final 2). DOC-002 p. 80 and its message log enumerate **134** messages; the main article likewise reports **134** messages, with a more specific first-month/second-month/final-four-month schedule.
- **Comparison logic:** all locations identify the same intervention name, six-month duration, and intended participant unit. 178 and 134 are not alternative displayed precisions of one dose; the within-period frequencies also differ.
- **Supported alternatives / limits:** the supplied package contains a version-change log elsewhere, so amendment of the intervention is plausible. The mapped p. 16 passage does not supply a version/date or supersession statement tying it to the later 134-message regimen. This candidate does not assert which regimen participants actually received.
- **Human verification question:** Was the 178-message schedule formally superseded by the 134-message schedule, and should the document identify the governing version and remove or label the obsolete schedule?

### XC004 — TAM sampling row label conflicts with its narrative and displayed calculations

- **Category:** Measure, label, or scale inconsistency.
- **Exact location:** DOC-002 PDF p. 53 (`joi250093supp1_prod_1768590553.08963.pdf#page=53`), TAM narrative and table.
- **Matched result:** prospective Technology Assessment Model sampling of mTB-Tobacco participants, by phase and country.
- **Printed values:** table row label: **“TAM questionnaire (30% of participants in the mTB-Tobacco groups)”**. Same-page narrative: **20%** of Phase-3 mTB-Tobacco participants in each country and **all** Phase-4 mTB-Tobacco participants. Same-page calculations: Phase 3, 10 sites x 40 x 20% = **80** and 8 x 40 x 20% = **64**; Phase 4, 11 x 45 = **495** and 7 x 45 = **315**.
- **Comparison logic:** 80 + 64 = 144, which is 20% of the 720 Phase-3 A participants; 495 + 315 = 810, the full Phase-4 A population. Neither calculation is compatible with a common 30% sampling label.
- **Supported alternatives / limits:** “30%” could be a stale generic label and the narrative/equations could be the intended phase-specific specification. The source gives no statement resolving it.
- **Human verification question:** Should the table heading state phase-specific 20%/100% sampling, or was a 30% TAM target intended with erroneous narrative/equations?

### XC005 — Phase-4 recruitment diagram is labelled as Phase 3 superiority

- **Category:** Measure, label, or scale inconsistency.
- **Exact location:** DOC-002 PDF p. 64 (`joi250093supp1_prod_1768590553.08963.pdf#page=64`), Phase-4 non-inferiority section and recruitment diagram.
- **Matched result:** prospective Phase-4 A-versus-B non-inferiority recruitment plan.
- **Printed values:** surrounding section: Phase 4, **36** clusters (18 per arm), **1,620** participants / 45 per site, A versus face-to-face support B, non-inferiority. Diagram box: **“Total clusters in Phase 3 (Superiority trial) = 36 sites”**, followed by **“Patients to be recruited = 1620.”**
- **Comparison logic:** the 36-site, 1,620-participant allocation belongs to the local Phase-4 A/B plan; Phase 3 is separately stated as 27 sites and 1,080 recruitment (plus 16 pilot where specified). The phase/framework label therefore conflicts with the matched numeric plan.
- **Supported alternatives / limits:** this can be a diagram-label carryover; no alternative phase-specific population makes the displayed 36/1,620 values a Phase-3 plan in the supplied later protocol.
- **Human verification question:** Should the box read “Phase 4 (Non-inferiority trial)” while retaining the 36-site/1,620-participant quantities?

### XC006 — Discussion labels the all-cause death percentage as TB deaths

- **Category:** Cross-document numeric inconsistency / rate-versus-count inconsistency.
- **Exact locations:** DOC-001 PDF p. 8 Discussion/Limitations (`jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8`); DOC-001 PDF p. 5 Results (`jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5`); DOC-001 PDF p. 6 Table 2 (`jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6`); DOC-003 PDF p. 6 eTable 4 (`joi250093supp2_prod_1768590553.09463.pdf#page=6`).
- **Matched result:** death outcome among the 1,080 randomized trial participants during the six-month follow-up.
- **Printed values:** DOC-001 p. 8 says **“4.8% of trial participants died of TB within 6 months.”** DOC-001 pp. 5-6/Table 2 report deaths **25/720 (3.5%)** mHealth and **27/360 (7.5%)** usual care, totaling **52/1,080 = 4.81%**, with the outcome labelled death. DOC-001 p. 5 and DOC-003 eTable 4 identify TB as the cause for **32/52 (61.5%)** deaths.
- **Comparison logic:** 4.8% matches 52 all-cause deaths divided by 1,080 randomized participants, not the 32 TB-cause deaths (32/1,080 = 2.96%). Thus the discussion’s “of TB” label conflicts with the cause-specific tabulation while its percentage matches all-cause mortality.
- **Supported alternatives / limits:** a different denominator for TB-cause deaths is not supplied. This finding concerns the causal label attached to the percentage, not the reported all-cause arm counts, HR, or conclusion.
- **Human verification question:** Was “of TB” unintended wording for all-cause mortality, or is there an unreported denominator/source for the stated 4.8% TB-death percentage?

### XC007 — eTable 6 site 2008 death count and percentage do not align with the matched recruitment denominator

- **Category:** Rate-versus-count inconsistency.
- **Exact locations:** DOC-003 PDF p. 8 eTable 5 (`joi250093supp2_prod_1768590553.09463.pdf#page=8`); DOC-003 PDF p. 9 eTable 6 (`joi250093supp2_prod_1768590553.09463.pdf#page=9`).
- **Matched result:** site 2008, randomized trial-cluster recruitment and death outcome.
- **Printed values:** eTable 5 gives site 2008 recruitment **40/N (100%)** and a six-month ITT denominator of **40**. eTable 6 gives site 2008 **5 deaths (7.5%)**.
- **Comparison logic:** if the death percentage uses the matched recruited/ITT cluster denominator used by the adjacent cluster tables, 5/40 x 100 = **12.5%**, not 7.5%. The 7.5% display equals 3/40, whereas the printed count is 5.
- **Supported alternatives / limits:** eTable 6 does not explicitly print its denominator. A different denominator might have been intended, but 5/0.075 = 66.67 is not compatible with the supplied 40-person recruited cluster and no 66-67-person population is supplied for this site. This is not a comparison to the distinct follow-up, sensitivity, or adverse-event denominators elsewhere in the supplement.
- **Human verification question:** What is the denominator for eTable 6 site-level death percentages, and should site 2008 read 5 (12.5%), 3 (7.5%), or another verified value?

### XC008 — MPSS stated item/scale structure does not yield its printed total-score range

- **Category:** Measure, label, or scale inconsistency.
- **Exact location:** DOC-002 PDF p. 84 (`joi250093supp1_prod_1768590553.08963.pdf#page=84`).
- **Matched result:** prospective Mood and Physical Symptoms Scale (MPSS) measurement definition.
- **Printed values:** the page says MPSS has **five domains**, each rated on a **5-point** scale, and is summed to a range of **5-35**.
- **Comparison logic:** under the printed description of five 1-to-5 domain scores, the attainable sum is 5 through 25, not 5 through 35. The page supplies no additional item count, weighting, or non-unit scoring rule that would create a 35-point maximum.
- **Supported alternatives / limits:** an unstated multi-item or weighted MPSS construction could make 5-35 correct. The package does not supply that construction, so this is a label/scale-definition inconsistency rather than an assertion about data values.
- **Human verification question:** Does the planned MPSS comprise additional scored items or a non-unit scoring rule, and if not, should the stated total-score range be 5-25?

## Coherent matches and non-candidate coverage

- **Main-paper internal repetitions:** DOC-001 abstract, Key Points, Results narrative, and Table 2 agree for the CO <10 ppm ITT primary outcome: 300/720 (41.7%) versus 55/360 (15.3%), RR 3.0 (95% CI 2.0-4.9). Counts, time point, CO threshold, ITT status, and displayed precision match.
- **Main versus supplement observed outcomes:** DOC-003 eTable 3 repeats the main-paper six-month adherence means (174.3 [21.501] versus 178.0 [12.1]) and P=.232 is compatible with main P=.23 at displayed precision. DOC-003 eTable 4 reconciles 25 + 27 = 52 deaths and its cause rows reconcile to the same arm and overall counts. DOC-003 eTable 5 cluster ITT abstinence counts aggregate to the main 300/720 and 55/360 primary-outcome counts. DOC-003 eTable 8's all-participant unadjusted RR 2.890 (1.983-4.709) is compatible by displayed precision with the main paper's PP crude RR 2.9 (2.0-4.7), not the ITT effect; its distinct analysis population was retained.
- **Definitions and observed results:** protocol/SAP and main paper agree on continuous abstinence at six months, CO <10 ppm, the no-more-than-five tobacco-use rule, cotinine treatment for concomitant smokeless use, and the distinct seven-day point-abstinence outcomes at week 9 and month 6. No prospective-only definition was treated as a conflicting observed result.
- **Adverse events:** main-paper any-severity percentages are consistent with the DOC-003 eTable 10 arm-category summaries when the eTable’s 699/334 adverse-event analysis denominators are retained; these must not be substituted for the 720/360 ITT denominators.
- **Versioned prospective units:** early/later protocol changes in total sample size (2,384 versus 2,716/2,700), phase allocations, and message schedules were not compared to observed DOC-001 enrollment as if they had a common analysis population. Explicitly version-marked phase changes on DOC-002 p. 77 are non-candidates when the relevant version is stated. Blank CRF/SAP template pages (DOC-002 pp. 93-100 and 97-109) have no observed numerical result and are not zero-valued comparators. DOC-003 eFigure/Figure S1 has no exact printed survival estimate for numerical matching.
- **Display-zero rule:** no P=0 or p=.000 display was registered. DOC-003 uses P<.001 threshold displays for some adverse-event comparisons, which are not literal-zero values and are not candidates on that basis.

## Counts and limitations

- **Mapped source scope reviewed:** DOC-001 9/9 PDF pages; DOC-002 109/109 PDF pages; DOC-003 16/16 PDF pages, via the current-run canonical evidence maps and relationship inventories.
- **Matched relationship groups checked:** 34 principal main-result/cross-document groups plus all mapped prospective-plan, template, and structured-supplement comparator groups; prospective-only and blank/template groups are explicitly documented above rather than forced into observed-result comparisons.
- **Qualifying provisional candidates emitted:** 8 (XC001-XC008).
- **Limitations:** source-version chronology is incompletely stated for several DOC-002 passages; no external source was used. DOC-003 eFigure has no exact printed numeric survival values. Some eTable 6 percentages lack an explicitly printed denominator; XC007 therefore records the exact human verification requirement instead of assuming a denominator. Candidate facts should be rechecked against the direct PDFs before ledger assignment.
