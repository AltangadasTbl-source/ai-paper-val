# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

**Every observation in this report is Pending Human Adjudication.** This is a quantitative reporting quality-control review, not a finding of invalidity, correction, or a conclusion about the paper.

## Executive Quality-Control Summary

Complete current-run coverage identified **13** distinct candidate consistency issues (C001-C013). The candidates concern arithmetic, labels, denominators, scale descriptions, and cross-document identities. Small preventable reporting defects can matter if confirmed because downstream evidence extraction may copy a value, label, denominator, or intervention description; this report does not assert that copying, conclusion change, or harm occurred.

## Package and Reused-Evidence Provenance

The direct-source package comprised three PDFs: [DOC-001 main article](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), [DOC-002 Supplement 1](<../joi250093supp1_prod_1768590553.08963.pdf#page=1>), and [DOC-003 Supplement 2](<../joi250093supp2_prod_1768590553.09463.pdf#page=1>). Source identities and before-review hashes are recorded in `review_1_5_1/source_inventory.md` and `review_1_5_1/source_hashes_before.sha256`.

Reusable page-addressable text was used as a locator only for DOC-001 pp. 1-9 and DOC-003 pp. 3-16, with direct-PDF confirmation. DOC-002 pp. 1-109 and DOC-003 pp. 1-2 required fresh direct-source mapping. The reusable-asset inventory and before-reuse hash snapshot are `review_1_5_1/evidence_asset_inventory.md` and `review_1_5_1/reused_artifact_hashes_before.sha256`.

## Scope, Complete Coverage, and Exclusions

All **134/134** direct PDF pages were mapped: DOC-001 9/9, DOC-002 109/109, and DOC-003 16/16. Reusable and fresh-required units partition the scope exactly: 23 reusable and 111 fresh-required pages. The full ledger is in `review_1_5_1/source_coverage.md` and the unit-level assignments are in `review_1_5_1/coverage_manifest.md`.

The review was limited to reproducible quantitative reporting consistency: numeric/arithmetic, denominator/proportion/total, statistical, cross-document, measure/label/scale, and rate-versus-count relationships. It did not undertake a general methodology, clinical, novelty, misconduct, raw-data, or external-literature review. Coherent display-zero P values were not candidates; no stable candidate was created on that basis.

## Quantitative and Statistical Relationship Coverage

The current-run numeric inventory contains **88/88** completed relationships. The statistical inventory contains **41/41** relationships, independently reviewed in statistical pass 1 and pass 2. Pass 1 identified the relationship later represented by C010; pass 2 reviewed all 41 relationships, the full ledger, and recheck facts, and added no distinct candidate. Both passes retained `DISPLAY_ZERO_NOT_CANDIDATE` handling where applicable.

Supporting artifacts: `review_1_5_1/relationships/numeric_relationship_inventory.md`, `review_1_5_1/statistics/relationship_inventory.md`, `review_1_5_1/checkers/statistical_pass_1.md`, and `review_1_5_1/checkers/statistical_pass_2.md`.

## Candidate Index

| ID | Candidate | Category |
|---|---|---|
| [C001](#c001--adjusted-self-reported-abstinence-interval-endpoint-printed-as-42) | Adjusted self-reported abstinence interval endpoint printed as 42 | Numeric or arithmetic inconsistency |
| [C002](#c002--discussion-labels-the-all-cause-death-percentage-as-tb-deaths) | Discussion labels all-cause death percentage as TB deaths | Cross-document numeric inconsistency |
| [C003](#c003--178-message-total-conflicts-with-its-printed-frequency-schedule) | 178-message total conflicts with its frequency schedule | Numeric or arithmetic inconsistency |
| [C004](#c004--repeated-2384-participant-plan-names-44-and-48-facilities) | Repeated 2,384-participant plan names 44 and 48 facilities | Cross-document numeric inconsistency |
| [C005](#c005--134-message-total-conflicts-with-its-printed-frequency-schedule) | 134-message total conflicts with its frequency schedule | Numeric or arithmetic inconsistency |
| [C006](#c006--tam-sampling-header-conflicts-with-contemporaneous-narrative-and-equations) | TAM sampling header conflicts with narrative and equations | Measure, label, or scale inconsistency |
| [C007](#c007--later-2716-participant-plan-gives-48-clinics-versus-a-63-site-diagram) | 2,716-participant plan gives 48 clinics versus 63 sites | Cross-document numeric inconsistency |
| [C008](#c008--phase-4-design-effect-equality-does-not-reproduce-from-printed-inputs) | Phase-4 design-effect equality does not reproduce | Numeric or arithmetic inconsistency |
| [C009](#c009--phase-4-diagram-is-labelled-phase-3superiority) | Phase-4 diagram is labelled Phase 3/Superiority | Measure, label, or scale inconsistency |
| [C010](#c010--phase-3-design-effect-display-gives-undocumented-1080-effective-sample-size) | Phase-3 design-effect display gives undocumented 1,080 effective sample size | Statistical reporting inconsistency |
| [C011](#c011--mpss-score-range-conflicts-with-stated-item-scale) | MPSS score range conflicts with stated item scale | Measure, label, or scale inconsistency |
| [C012](#c012--site-2008-death-count-and-percentage-lack-a-compatible-supplied-denominator) | Site 2008 death count and percentage lack a compatible denominator | Rate-versus-count inconsistency |
| [C013](#c013--protocol-message-dose-changes-from-178-to-134-without-supplied-reconciliation) | Protocol message dose changes from 178 to 134 without reconciliation | Cross-document numeric inconsistency |

## Candidate Evidence Cards

## C001 — Adjusted self-reported abstinence interval endpoint printed as 42

**Pending Human Adjudication**

**Candidate statement:** The printed adjusted self-reported abstinence RR interval has upper endpoint 42, an unusual interval field requiring confirmation against the fitted model output.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-001 [main article — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table 2, continuous abstinence, self-reported only (ITT), adjusted RR.

**Source evidence:** Adjusted RR is printed as `2.8 (1.9 to 42)`; the same row's crude RR is `2.7 (1.8 to 4.1)`.

**Reported-versus-comparator:** Printed upper endpoint `42` versus the same-row estimate and companion interval context.

**Reasoning procedure:** Direct observation is that the rendered table visibly prints 42. The derived asymmetry is a transcription-quality signal, not proof of a different endpoint; mixed-effects model output is unavailable.

**Calculation:** `42/2.8=15.0`; `1.9/2.8=0.6786`. Ordinary rounding cannot convert 42 to 4.2.

**Alternative source-grounded interpretations:** A genuinely wide asymmetric interval remains possible under the stated mixed-effects model; the package lacks coefficient, SE, and model-output details.

**Mechanical evidence recheck:** Direct PDF rendering confirmed the printed `2.8 (1.9 to 42)` and the listed crude comparator.

**Quality-control relevance:** An interval field should be transcribed and verified accurately.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an erroneous adjusted RR interval into a review table.

**Human verification steps:** Inspect the fitted adjusted-model output and verify whether 42 is the intended endpoint; do not infer 4.2 as a correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Discussion labels the all-cause death percentage as TB deaths

**Pending Human Adjudication**

**Candidate statement:** The discussion's 4.8% phrase “died of TB” matches the all-cause death total rather than the supplied TB-cause count.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001 [main article — PDF p. 8](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>), Discussion; [PDF p. 5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) and [PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Results/Table 2; DOC-003 [Supplement 2 — PDF p. 6](<../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable 4.

**Source evidence:** The discussion says 4.8% died of TB; Table 2 gives 25/720 and 27/360 deaths, and eTable 4 classifies 32/52 deaths as TB cause.

**Reported-versus-comparator:** 4.8% labelled TB deaths versus 52/1080 all-cause deaths and 32/1080 TB-cause deaths.

**Reasoning procedure:** Compare the discussion label with matched all-cause counts and the explicitly classified cause count.

**Calculation:** `52/1080×100=4.81%` (4.8%); `32/1080×100=2.96%` (3.0%).

**Alternative source-grounded interpretations:** “Died of TB” could be loose contextual wording; eTable 4 is the explicit cause classification and no alternate TB-death denominator is supplied.

**Mechanical evidence recheck:** Direct pages confirmed the wording, all-cause counts, and TB-cause count.

**Quality-control relevance:** All-cause and cause-specific mortality are distinct reusable outcomes.

**Potential downstream evidence impact:** If confirmed, a review could misclassify all-cause mortality as TB-specific mortality.

**Human verification steps:** Confirm whether the discussion should say all-cause deaths or identify a distinct TB-death denominator/source.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — 178-message total conflicts with its printed frequency schedule

**Pending Human Adjudication**

**Candidate statement:** A six-month plan states 178 SMS but its own minimum printed schedule exceeds that total.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 16](<../joi250093supp1_prod_1768590553.08963.pdf#page=16>).

**Source evidence:** `178` SMS over six months; first two months `4-5/day`, next two `2-3/day`, final two `1-2/week`.

**Reported-versus-comparator:** Printed total 178 versus the schedule's conservative minimum.

**Reasoning procedure:** Apply the lowest printed frequency in each period using conservative month/week durations.

**Calculation:** `2×28×4 + 2×28×2 + 8×1=344`, 166 above 178; at 30-day months, `368`.

**Alternative source-grounded interpretations:** “Message” may mean a send, template, or another undefined unit; frequency, duration, or total may be from unlabelled plan states.

**Mechanical evidence recheck:** Direct PDF rendering confirmed the total and schedule; the corrected 28-day minimum is 344.

**Quality-control relevance:** Dose is a reproducible intervention-exposure definition.

**Potential downstream evidence impact:** If confirmed, an intervention taxonomy or replication could use the wrong dose.

**Human verification steps:** Identify the intended message unit, schedule, period, and protocol version.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Repeated 2,384-participant plan names 44 and 48 facilities

**Pending Human Adjudication**

**Candidate statement:** Matched repeated plan text gives 44 facilities in one location and 48 clinics in another.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 10](<../joi250093supp1_prod_1768590553.08963.pdf#page=10>) and [PDF p. 26](<../joi250093supp1_prod_1768590553.08963.pdf#page=26>).

**Source evidence:** Both locations describe the 2,384-participant plan, approximately 50 recruits, 10% missing primary outcome, 16 pilot participants, and matching Phase-3/4 allocation assumptions, but list 44 and 48 sites.

**Reported-versus-comparator:** 44 versus 48 sites for the same printed plan.

**Reasoning procedure:** Compare repeated plan identities and their implied recruits per site.

**Calculation:** `2384/44=54.18`; `2384/48=49.67`; the latter aligns with approximately 50.

**Alternative source-grounded interpretations:** Facility/clinic definitions or amendment chronology may differ but are not supplied.

**Mechanical evidence recheck:** Direct pages confirmed both counts and shared plan context.

**Quality-control relevance:** Cluster count affects planned recruitment and design-effect interpretation.

**Potential downstream evidence impact:** If confirmed, a protocol reviewer could record the wrong cluster total.

**Human verification steps:** Establish which count governed the plan and whether the other occurrence needs correction or version labeling.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — 134-message total conflicts with its printed frequency schedule

**Pending Human Adjudication**

**Candidate statement:** A 134-message six-month statement conflicts with the minimum implied by its printed schedule.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 53](<../joi250093supp1_prod_1768590553.08963.pdf#page=53>).

**Source evidence:** `134` SMS over six months; first two months `4-5/day`, next two `1-2/day`, final two `1/week`.

**Reported-versus-comparator:** Printed total 134 versus schedule minimum.

**Reasoning procedure:** Apply the lowest stated frequency with conservative durations.

**Calculation:** `2×28×4 + 2×28×1 + 8×1=288`, 154 above 134; the 30-day calculation is 308.

**Alternative source-grounded interpretations:** Unique-template versus send units or an unlabelled version may explain the text; p. 80 has a different 134-message schedule but does not label p. 53 as a separate plan state.

**Mechanical evidence recheck:** Direct rendering confirmed the statement at p. 53, correcting a stale p. 51 locator.

**Quality-control relevance:** The total and schedule should identify the same intervention exposure.

**Potential downstream evidence impact:** If confirmed, intervention coding could misstate intensity or duration.

**Human verification steps:** Verify the dose definition and protocol version for the p. 53 schedule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — TAM sampling header conflicts with contemporaneous narrative and equations

**Pending Human Adjudication**

**Candidate statement:** A TAM sampling header says 30%, while contemporaneous phase-specific narrative and equations show 20% Phase 3 and all Phase 4 participants.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 55](<../joi250093supp1_prod_1768590553.08963.pdf#page=55>).

**Source evidence:** Header `30%`; narrative `20%` in Phase 3 and all in Phase 4; equations `10×40×20%=80`, `8×40×20%=64`, `11×45=495`, and `7×45=315`.

**Reported-versus-comparator:** 30% header versus 20%/100% phase-specific calculation.

**Reasoning procedure:** Sum phase-specific samples and compare each to its stated base.

**Calculation:** `80+64=144=20%` of 720 Phase-3 A participants; `495+315=810=100%` of Phase-4 A participants.

**Alternative source-grounded interpretations:** 30% could refer to an unstated pooled or earlier target.

**Mechanical evidence recheck:** Direct page inspection confirmed the header, narrative, and equations at p. 55.

**Quality-control relevance:** Sampling percentage defines the TAM analysis population.

**Potential downstream evidence impact:** If confirmed, a secondary-process-study denominator could be misreported.

**Human verification steps:** Clarify whether the header should be phase-specific or identify its distinct 30% denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Later 2,716-participant plan gives 48 clinics versus a 63-site diagram

**Pending Human Adjudication**

**Candidate statement:** A later 2,716-participant plan presents 48 clinics and approximately 50 recruits per clinic, while related text and diagram present 63 sites and approximately 43 per site.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 48](<../joi250093supp1_prod_1768590553.08963.pdf#page=48>), [PDF p. 51](<../joi250093supp1_prod_1768590553.08963.pdf#page=51>), [PDF p. 52](<../joi250093supp1_prod_1768590553.08963.pdf#page=52>), and [PDF p. 62](<../joi250093supp1_prod_1768590553.08963.pdf#page=62>).

**Source evidence:** p. 48 and the pp. 51-52 diagram give 2,716 participants, 63 sites (27+36), and approximately 43/site; p. 62 gives 2,716, approximately 50 from 48 clinics.

**Reported-versus-comparator:** Same plan total with 48/~50 versus 63/~43.

**Reasoning procedure:** Compare repeated total, site counts, and implied mean recruits.

**Calculation:** `2716/63=43.11`; `2716/48=56.58`; site counts differ by 15.

**Alternative source-grounded interpretations:** The 48 clinics may be an unstated subset or earlier plan.

**Mechanical evidence recheck:** Direct pages confirmed p. 48 and pp. 51-52 rather than stale p. 46 and pp. 49-50 locators, and confirmed p. 62.

**Quality-control relevance:** Site count and average are sample-size/design-effect quantities.

**Potential downstream evidence impact:** If confirmed, protocol-level cluster denominators could be copied incorrectly.

**Human verification steps:** Define the 48-clinic population and reconcile or version-label the p. 62 statement.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Phase-4 design-effect equality does not reproduce from printed inputs

**Pending Human Adjudication**

**Candidate statement:** A Phase-4 display equates 1,036 multiplied by 1.56 to 1,620, although the exact product differs.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 64](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>).

**Source evidence:** `864+(864×0.2)=1036`; `1036/36=29`; `DE=1+0.02(29-1)=1.56`; `ESS=1036×1.56=1620`; diagram `36×45=1620`.

**Reported-versus-comparator:** Displayed `1036×1.56=1620` versus exact product and the separate site-target total.

**Reasoning procedure:** Recalculate displayed arithmetic while retaining the diagram as a separately reproducible cluster target.

**Calculation:** `864×1.2=1036.8`; `1036×1.56=1616.16`; `36×45=1620`.

**Alternative source-grounded interpretations:** A cluster-level ceiling/allocation step can explain 1,620 but is not stated.

**Mechanical evidence recheck:** Direct page inspection confirmed both the printed equality and 36-by-45 diagram.

**Quality-control relevance:** Sample-size rationale should state reproducible rounding/allocation conventions.

**Potential downstream evidence impact:** If confirmed, a protocol appraisal could reproduce an unclear design-effect calculation.

**Human verification steps:** Identify the rounding/allocation sequence and distinguish the cluster target from the arithmetic product.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Phase-4 diagram is labelled Phase 3/Superiority

**Pending Human Adjudication**

**Candidate statement:** A diagram within a Phase-4 noninferiority section is labelled “Phase 3 (Superiority trial).”

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 64](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>).

**Source evidence:** Local text says Phase 4, noninferiority, A vs B, 36 sites, 1,620 participants; diagram says “Total clusters in Phase 3 (Superiority trial) = 36 sites.”

**Reported-versus-comparator:** Phase-3/Superiority label versus local Phase-4/noninferiority plan.

**Reasoning procedure:** Match the diagram's 36-site/1,620-participant allocation to the local Phase-4 plan and distinguish it from Phase 3.

**Calculation:** `18+18=36`; `36×45=1620`; the separate Phase-3 plan uses 27 sites and 1,080 participants.

**Alternative source-grounded interpretations:** A carry-over caption is plausible but not established by the supplied record.

**Mechanical evidence recheck:** Direct PDF rendering confirmed the categorical label conflict.

**Quality-control relevance:** Phase and objective identify comparator and interpretation.

**Potential downstream evidence impact:** If confirmed, a protocol synthesis could misclassify the trial phase or objective.

**Human verification steps:** Confirm the intended phase/objective label for the diagram.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Phase-3 design-effect display gives undocumented 1,080 effective sample size

**Pending Human Adjudication**

**Candidate statement:** A Phase-3 display reports `704×1.50≈1080` and calls it effective sample size without documenting the cluster-rounding/allocation transition or terminology.

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 63](<../joi250093supp1_prod_1768590553.08963.pdf#page=63>) and [PDF p. 83](<../joi250093supp1_prod_1768590553.08963.pdf#page=83>).

**Source evidence:** p. 63 gives `N=587+(587×0.2)=704`, 27 sites, `704/27=26`, `DE=1+0.02(26−1)=1.50`, and `ESS=704×1.50≈1080 (40/site)`; p. 83 repeats 704, 26, DE 1.50, and 1080/40/site.

**Reported-versus-comparator:** `704×1.50≈1080` and “effective sample size” versus exact multiplication and the independent `27×40=1080` cluster allocation.

**Reasoning procedure:** Recalculate the displayed product, then distinguish a possible upward cluster target from an information-equivalent effective sample size.

**Calculation:** `704×1.50=1056`; `1080/704=1.5341`; `27×40=1080`.

**Alternative source-grounded interpretations:** The 1,056 design-effect-inflated target may have been rounded upward to 40 per site; that is plausible but unstated, and 1,080 is not asserted impossible.

**Mechanical evidence recheck:** Direct PDF rendering confirmed p. 63 and repeated p. 83 (correcting a stale p. 82 locator).

**Quality-control relevance:** Arithmetic and terminology should explain a statistical design parameter.

**Potential downstream evidence impact:** If confirmed, a sample-size rationale could be copied as a nonreproducible calculation.

**Human verification steps:** Confirm the cluster-rounding rule and whether “effective sample size” should instead describe an inflated recruitment target.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — MPSS score range conflicts with stated item scale

**Pending Human Adjudication**

**Candidate statement:** The MPSS description names five 5-point domains but gives a summed 5-35 range without explaining the scoring rule.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 85](<../joi250093supp1_prod_1768590553.08963.pdf#page=85>).

**Source evidence:** MPSS has `five` domains rated on a `5-point` scale and summed `5-35`.

**Reported-versus-comparator:** Printed 5-35 range versus the stated five-domain 5-point description.

**Reasoning procedure:** Evaluate the range conditionally under ordinary unit-spaced 1-to-5 coding; the observed issue is that the description does not explain 35.

**Calculation:** Under ordinary 1-to-5 coding, five items span `5×1=5` to `5×5=25`, not 35.

**Alternative source-grounded interpretations:** Additional items, non-unit coding, weights, anchors, or transformation could yield 35; none is supplied.

**Mechanical evidence recheck:** Direct rendering confirmed the definition at p. 85, correcting a stale p. 84 locator.

**Quality-control relevance:** Scale range controls meaning and comparability of an MPSS result.

**Potential downstream evidence impact:** If confirmed, a review could code the outcome scale incorrectly.

**Human verification steps:** Obtain the response anchors, item count, weights, and scoring rule that produce the stated range.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Site 2008 death count and percentage lack a compatible supplied denominator

**Pending Human Adjudication**

**Candidate statement:** Site 2008 is reported as 5 deaths (7.5%) without a denominator compatible with the supplied same-site recruitment/ITT total.

**Category:** Rate-versus-count inconsistency

**Exact source locations:** DOC-003 [Supplement 2 — PDF p. 8](<../joi250093supp2_prod_1768590553.09463.pdf#page=8>), eTable 5; [PDF p. 9](<../joi250093supp2_prod_1768590553.09463.pdf#page=9>), eTable 6.

**Source evidence:** eTable 5 gives site 2008 recruitment/ITT denominator `40`; eTable 6 gives `5 (7.5%)` deaths without printing a denominator.

**Reported-versus-comparator:** 5 deaths (7.5%) versus matched same-site 40-person recruitment/ITT denominator.

**Reasoning procedure:** Treat the 40 as a cross-table comparator, not as an eTable 6 observation; retain every calculation as conditional.

**Calculation:** If denominator is 40, `5/40×100=12.5%`; `5/0.075=66.67`, and no 66-67 site population is supplied.

**Alternative source-grounded interpretations:** A distinct unprinted death denominator may exist.

**Mechanical evidence recheck:** Direct pages confirmed the count/percentage, absence of an eTable 6 denominator, and 40 in eTable 5.

**Quality-control relevance:** Count/proportion pairs are readily reused in cluster summaries.

**Potential downstream evidence impact:** If confirmed, a cluster mortality rate could be copied incorrectly.

**Human verification steps:** Identify the denominator for 7.5%; do not presume a replacement count, percentage, or denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Protocol message dose changes from 178 to 134 without supplied reconciliation

**Pending Human Adjudication**

**Candidate statement:** Protocol and main-article materials give 178 and 134 messages for the six-month mTB-Tobacco participant dose without an explicit crosswalk or supersession statement.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-002 [Supplement 1 — PDF p. 16](<../joi250093supp1_prod_1768590553.08963.pdf#page=16>), [PDF p. 53](<../joi250093supp1_prod_1768590553.08963.pdf#page=53>), [PDF p. 80](<../joi250093supp1_prod_1768590553.08963.pdf#page=80>), and [PDF p. 101](<../joi250093supp1_prod_1768590553.08963.pdf#page=101>) through [PDF p. 109](<../joi250093supp1_prod_1768590553.08963.pdf#page=109>); DOC-001 [main article — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>).

**Source evidence:** p. 16 says 178 SMS; pp. 53 and 80 say 134 with differing schedules; pp. 101-109 show a 1-134 log; main p. 3 reports 134 unique messages as `100+30+4`.

**Reported-versus-comparator:** 178 versus 134 for matched six-month intervention dose.

**Reasoning procedure:** Compare the displayed total, schedule, message-log range, and main-article component total while retaining unlabelled version change as inference.

**Calculation:** `178−134=44`; `100+30+4=134`; the log begins at 1 and ends at 134.

**Alternative source-grounded interpretations:** A formal amendment is plausible, but supplied material does not explicitly link the 178-message passage to the later 134-message regimen or establish what participants received.

**Mechanical evidence recheck:** Direct pages confirmed both schedules/totals, the 1-134 log, and the main-article components; p. 53 replaces a stale p. 51 locator.

**Quality-control relevance:** Dose-version identity is needed to interpret and replicate an intervention.

**Potential downstream evidence impact:** If confirmed, evidence syntheses could attribute the trial to the wrong intervention regimen.

**Human verification steps:** Obtain the amendment/version crosswalk and label obsolete versus current regimen without assuming either.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations identify fields that a systematic review, meta-analysis, guideline, protocol synthesis, or data extractor might copy: effect interval endpoints, mortality type, message dose, site count, sample-size arithmetic, phase/objective labels, scale ranges, and count/percentage pairs. This is a conditional evidence-extraction consideration only; the review does not claim propagation, changed conclusions, or serious harm.

## Limitations and Missing Definitions

DOC-002's embedded text layer was substitution-garbled. All 109 pages were freshly rendered and visually mapped; this is a derivative-quality limitation rather than an uncovered scientific unit. CPU OCR was nonresponsive, so direct rendered-page inspection was used. The package lacks model output for C001; explicit message-unit and amendment crosswalks for C003, C005, and C013; facility/clinic definitions and chronology for C004 and C007; rounding/allocation conventions for C008 and C010; complete MPSS anchors/scoring for C011; and the eTable 6 death denominator for C012. Figure-only Bayesian values lacked printed numeric endpoints and were not reconstructed.

## Human Adjudication Checklist

1. Verify each card against the cited direct PDF page.
2. Obtain missing model output, denominator, scoring, schedule, or version documentation where identified.
3. Determine validity, importance, and action for each candidate in the blank card fields.
4. Record initials and notes; retain the stable ID regardless of the eventual human decision.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

- **Profile:** 1.5.1
- **Source-unit counts:** 134 total; 111 fresh-source; 23 reusable-backed
- **Scientific coverage:** COMPLETE — 134/134 direct-source pages mapped; 88 numeric and 41 statistical relationships checked
- **Source hash snapshot:** `review_1_5_1/source_hashes_before.sha256`
- **Reused-artifact hash snapshot:** `review_1_5_1/reused_artifact_hashes_before.sha256`
- **Canonical evidence recheck:** `review_1_5_1/verification/evidence_recheck.md`
- **Evidence-quality audit:** `review_1_5_1/quality/evidence_quality_audit.md`

### Agent Execution

All manifested current-run agents are recorded in `review_1_5_1/agent_execution_manifest.md`: coordinator (gpt-5.6-sol/high); reuse asset curator; main evidence mapper; four support evidence mappers; numeric consistency reviewer; cross-source reviewer; statistical pass 1 (gpt-5.6-terra/high); interrupted evidence-recheck attempt; evidence-recheck retry (gpt-5.6-sol/high); statistical pass 2 (gpt-5.6-terra/high); evidence-quality auditor (gpt-5.6-sol/high); and report generator (gpt-5.6-terra/medium).

### Performance

- **Target basis:** Three direct PDF sources totaling 134 pages, with usable reusable extraction expected for 23 pages and fresh direct-source mapping required for 111 pages; the package has one short main article, one long 109-page support document, and one 16-page support document, requiring parallel mapping plus two complete statistical passes.
- **Total source units:** 134
- **Fresh-source units:** 111
- **Target elapsed minutes:** 50-75
- **Started UTC:** 2026-09-03T03:46:35Z
- **Finished UTC:** 2026-09-03T05:33:39Z
- **Observed elapsed minutes:** 107.1
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** DOC-002's embedded text extraction was substitution-garbled, requiring fresh rendering and full visual inspection of 109 pages; CPU Tesseract was nonresponsive; the first high-reasoning evidence recheck returned no durable artifact and the full 13-candidate recheck was repeated in a fresh specialist.

### Token Accounting and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

The runtime exposed no authoritative response-level token counts for the coordinator or specialists, so every manifested agent is recorded with `UNAVAILABLE`; the zero below is the known subtotal, not an estimate of actual use. Cached input/cache-write counts are input subsets and reasoning counts are output subsets; they are not added again to total tokens. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not an invoice. Per-agent detail is in `review_1_5_1/token_usage_ledger.csv` and `review_1_5_1/token_usage_summary.md`.

| Model | Known input tokens | Known output tokens | Known total tokens | Known token cost (USD) | Count status |
|---|---:|---:|---:|---:|---|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 | INCOMPLETE |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 | INCOMPLETE |
