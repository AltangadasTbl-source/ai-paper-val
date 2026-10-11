# Stable Candidate Ledger

All entries are **Pending Human Adjudication**. Stable IDs were assigned after merging only the specified current-run numeric, cross-source, and statistical-pass-1 checker records. No severity, validity, disposition, correction, or exclusion is assigned here.

## C001 — Adjusted self-reported abstinence interval endpoint printed as 42

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC001.
- **Exact source locations:** DOC-001, `jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6`, Table 2, continuous abstinence self-reported only (ITT), adjusted RR column.
- **Source evidence:** Adjusted RR `2.8 (1.9 to 42)`; same-row crude RR `2.7 (1.8 to 4.1)`.
- **Reported-versus-comparator:** Printed upper endpoint `42` versus the same-row/adjacent Table 2 interval scale.
- **Reasoning/calculation:** `42/2.8=15.0` while `1.9/2.8=0.68`; no rounding tolerance can convert 42 to 4.2. Direct observation is that rendered Table 2 visibly prints `42`; the inference is that a decimal/label issue is plausible, not proven.
- **Alternative source-grounded interpretations:** A genuinely very wide adjusted mixed-model interval is possible; the package supplies no SE/model output to resolve it.
- **Quality-control relevance:** A directly reusable effect-interval field may be copied incorrectly.
- **Potential downstream evidence impact:** If confirmed, a data extractor could reproduce an erroneous adjusted RR interval in a review table.
- **Human question:** Does the fitted adjusted model intentionally yield `2.8 (1.9 to 42)`, or is the endpoint another verified value?

## C002 — Discussion labels the all-cause death percentage as TB deaths

- **Category:** Cross-document numeric inconsistency.
- **Checker provenance:** NC002; XC006.
- **Exact source locations:** DOC-001 PDF p. 8 (`jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8`), Discussion; DOC-001 PDF pp. 5-6 (`#page=5`, `#page=6`), Results/Table 2; DOC-003 PDF p. 6 (`joi250093supp2_prod_1768590553.09463.pdf#page=6`), eTable 4.
- **Source evidence:** p. 8 says `4.8%` of participants “died of TB”; Table 2 gives deaths 25/720 and 27/360; eTable 4 gives TB cause 32/52 (61.5%).
- **Reported-versus-comparator:** 4.8% labelled TB deaths versus 52/1080 all-cause deaths and 32/1080 TB-cause deaths.
- **Reasoning/calculation:** `52/1080×100=4.81%` rounds to 4.8%; `32/1080×100=2.96%` rounds to 3.0%, a 1.8-point difference beyond 0.05-point one-decimal rounding tolerance. Direct observation is the printed wording/counts; inference is that “of TB” may be unintended.
- **Alternative source-grounded interpretations:** “Died of TB” might be loose contextual wording; eTable 4 is the explicit cause classification. No other TB-death denominator is supplied.
- **Quality-control relevance:** All-cause and cause-specific mortality are distinct reusable outcomes.
- **Potential downstream evidence impact:** If confirmed, a review could misclassify all-cause mortality as TB-specific mortality.
- **Human question:** Should the discussion say all-cause deaths, or is a distinct denominator/source for 4.8% TB deaths intended?

## C003 — 178-message total conflicts with its printed frequency schedule

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC003.
- **Exact source locations:** DOC-002 PDF p. 16 (`joi250093supp1_prod_1768590553.08963.pdf#page=16`).
- **Source evidence:** `178` SMS over six months; first two months `4-5/day`, next two `2-3/day`, final two `1-2/week`.
- **Reported-versus-comparator:** Printed total 178 versus the minimum implied by its own schedule.
- **Reasoning/calculation:** With conservative 30-day months, minimum=`2×30×4 + 2×30×2 + 2×4×1=368`, 190 above 178; using 28-day months and eight weeks gives `2×28×4 + 2×28×2 + 8×1=344`, 166 above 178. Calendar variation/rounding cannot close the gap. Direct observation is the schedule/total; inference is a likely total, unit, or period error.
- **Alternative source-grounded interpretations:** Frequency units, durations, or the total may be from different unlabelled plan states.
- **Quality-control relevance:** Dose is a reproducible intervention-exposure definition.
- **Potential downstream evidence impact:** If confirmed, an intervention taxonomy or replication could use the wrong dose.
- **Human question:** Which total and schedule were intended for this protocol version?

## C004 — Repeated 2,384-participant plan names 44 and 48 facilities

- **Category:** Cross-document numeric inconsistency.
- **Checker provenance:** NC004; XC001.
- **Exact source locations:** DOC-002 PDF p. 10 (`joi250093supp1_prod_1768590553.08963.pdf#page=10`) and p. 26 (`joi250093supp1_prod_1768590553.08963.pdf#page=26`).
- **Source evidence:** Matched repeated plan: total `2,384`, approximately 50 recruits, 10% missing primary outcome, 16 pilot participants, and identical Phase-3/4 allocation assumptions; p.10 says `44` facilities, p.26 says `48` clinics.
- **Reported-versus-comparator:** 44 versus 48 sites for the same printed plan.
- **Reasoning/calculation:** Four facilities is not rounding. `2384/44=54.18`; `2384/48=49.67`, so only 48 accords with “approximately 50.” Direct observation is the two counts; inference is an unreconciled repeated-plan inconsistency.
- **Alternative source-grounded interpretations:** One could be an amendment remnant or use an unprinted facility/clinic definition.
- **Quality-control relevance:** Cluster count affects planned average recruitment and design-effect interpretation.
- **Potential downstream evidence impact:** If confirmed, a protocol reviewer could record the wrong cluster total.
- **Human question:** Which facility count governed the 2,384-participant plan, and should the other occurrence be corrected or version-labelled?

## C005 — 134-message total conflicts with its printed frequency schedule

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC005.
- **Exact source locations:** DOC-002 PDF p. 53 (`joi250093supp1_prod_1768590553.08963.pdf#page=53`).
- **Source evidence:** `134` SMS over six months; first two months `4-5/day`, next two `1-2/day`, final two `1/week`.
- **Reported-versus-comparator:** Printed total 134 versus schedule minimum.
- **Reasoning/calculation:** Conservative minimum=`2×30×4 + 2×30×1 + 2×4×1=308`, 174 above 134. Direct observation is the stated total/schedule; inference is that one component is erroneous or differently defined.
- **Alternative source-grounded interpretations:** A carried-over schedule or a different dose version may be intended.
- **Quality-control relevance:** The total and schedule should describe the same intervention exposure.
- **Potential downstream evidence impact:** If confirmed, intervention coding can misstate intensity and duration.
- **Human question:** Which of the 134 total and the three-period schedule is correct for this protocol version?

## C006 — TAM sampling header conflicts with contemporaneous narrative and equations

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** NC006; XC004.
- **Exact source locations:** DOC-002 PDF p. 55 (`joi250093supp1_prod_1768590553.08963.pdf#page=55`).
- **Source evidence:** Header says `30%`; narrative says 20% Phase 3 and all Phase 4; equations give `10×40×20%=80`, `8×40×20%=64`, `11×45=495`, `7×45=315`.
- **Reported-versus-comparator:** 30% generic header versus 20%/100% phase-specific calculation.
- **Reasoning/calculation:** 80+64=144=20% of 720 Phase-3 A participants; 495+315=810=100% of Phase-4 A participants. Neither is 30%; discrepancy is 10-70 points, not rounding. Direct observation is printed text/equations; inference is a stale/incorrect label.
- **Alternative source-grounded interpretations:** 30% could refer to an unstated pooled or earlier target.
- **Quality-control relevance:** Sampling percentage defines the TAM analysis population.
- **Potential downstream evidence impact:** If confirmed, secondary-process-study denominators could be misreported.
- **Human question:** Should the header state phase-specific 20%/all participants, or is a distinct 30% denominator intended?

## C007 — Later 2,716-participant plan gives 48 clinics versus a 63-site diagram

- **Category:** Cross-document numeric inconsistency.
- **Checker provenance:** NC007; XC002.
- **Exact source locations:** DOC-002 PDF p. 48 (`joi250093supp1_prod_1768590553.08963.pdf#page=48`), pp.51-52 (`#page=51`, `#page=52`), and p.62 (`#page=62`).
- **Source evidence:** p.48 and Diagram 1 on pp.51-52: 2,716 participants, 63 sites (27+36), approximately 43/site; p.62: 2,716, approximately 50 from 48 clinics.
- **Reported-versus-comparator:** Same later-plan total, 48/~50 versus 63/~43.
- **Reasoning/calculation:** `2716/63=43.11`; `2716/48=56.58`, not approximately 50. The 15-site difference cannot be rounding. Direct observation is printed plan/diagram; inference is an unreconciled subset or carry-forward claim.
- **Alternative source-grounded interpretations:** 48 could denote an unstated clinic subset or earlier plan.
- **Quality-control relevance:** Site count/average are sample-size and design-effect quantities.
- **Potential downstream evidence impact:** If confirmed, protocol-level cluster denominators may be copied incorrectly.
- **Human question:** What population of 48 clinics is meant, and should the p.62 statement be updated or qualified?

## C008 — Phase-4 design-effect equality does not reproduce from printed inputs

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC008.
- **Exact source locations:** DOC-002 PDF p. 64 (`joi250093supp1_prod_1768590553.08963.pdf#page=64`).
- **Source evidence:** `864+(864×0.2)=1036`; `1036/36=29`; `DE=1+0.02(29-1)=1.56`; `ESS=1036×1.56=1620`; diagram 36×45=1620.
- **Reported-versus-comparator:** Printed ESS 1620 versus exact multiplication 1616.16.
- **Reasoning/calculation:** `864×1.2=1036.8`, `1036/36=28.78`, and `1036×1.56=1616.16`. Direct observation is the formula/values; inference is that site-level rounding may have been used without being stated.
- **Alternative source-grounded interpretations:** 1620 could be a 45-per-site recruitment target rather than an exact ESS product.
- **Quality-control relevance:** The displayed sample-size rationale should be reproducible.
- **Potential downstream evidence impact:** If confirmed, a protocol appraisal could reproduce an unclear design-effect calculation.
- **Human question:** What explicit rounding sequence leads to 1,620 from the stated inputs?

## C009 — Phase-4 diagram is labelled Phase 3/Superiority

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** NC009; XC005.
- **Exact source locations:** DOC-002 PDF p.64 (`joi250093supp1_prod_1768590553.08963.pdf#page=64`), Phase-4 section/diagram.
- **Source evidence:** Local text: Phase 4, noninferiority, A vs B, 36 sites, 1620 participants; diagram: “Total clusters in `Phase 3 (Superiority trial)` = 36 sites.”
- **Reported-versus-comparator:** Phase-3/Superiority label versus local Phase-4/noninferiority plan.
- **Reasoning/calculation:** The 36-site/1620 allocation is the Phase-4 plan; Phase 3 elsewhere is 27 sites/1080 plus pilot as applicable. Labels are categorical, so no numerical tolerance applies. Direct observation is the conflicting labels; inference is a carry-over caption.
- **Alternative source-grounded interpretations:** None supplied that makes 36/1620 the local Phase-3 plan.
- **Quality-control relevance:** Phase/objective identify comparator and interpretation.
- **Potential downstream evidence impact:** If confirmed, a protocol synthesis could misclassify the trial phase and objective.
- **Human question:** Should the diagram read “Phase 4 (Non-inferiority trial)”? 

## C010 — Phase-3 design-effect display gives unreproducible 1,080 effective sample size

- **Category:** Statistical reporting inconsistency.
- **Checker provenance:** NC010; SP1-001 (S026; S025/S028 context).
- **Exact source locations:** DOC-002 PDF p. 63 (`joi250093supp1_prod_1768590553.08963.pdf#page=63`), detailed Phase-3 calculation; DOC-002 PDF p.83 (`#page=83`), repeated Phase-3 summary.
- **Source evidence:** p.63: `N=587+(587×0.2)=704`; 27 sites; `704/27=26`; `DE=1+0.02(26−1)=1.50`; “ESS = effective sample size = `704×1.50≈1080` (40/site).” p.83 repeats 704, 26, DE 1.50, and 1080/40/site.
- **Reported-versus-comparator:** 704×1.50 labelled approximately 1080 versus exact 1056 and diagram 27×40=1080.
- **Reasoning/calculation:** `704×1.50=1056`; `1080/704=1.5341`. Direct observation is the formula/product/label/site total; inference is that upward cluster rounding may have occurred, and that “effective sample size” may instead mean inflated recruitment. No displayed convention resolves it.
- **Alternative source-grounded interpretations:** A 1056 target may have been rounded up to 40 participants across 27 sites; this is plausible but unstated.
- **Quality-control relevance:** Arithmetic and terminology explain a statistical design parameter.
- **Potential downstream evidence impact:** If confirmed, sample-size rationale could be copied as a nonreproducible calculation.
- **Human question:** Was 1080 a cluster-rounded recruitment target, and should the equation/“effective sample size” label state that convention?

## C011 — MPSS score range conflicts with stated item scale

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** NC011; XC008.
- **Exact source locations:** DOC-002 PDF p.85 (`joi250093supp1_prod_1768590553.08963.pdf#page=85`).
- **Source evidence:** MPSS has `five` domains rated on a `5-point` scale and summed `5-35`.
- **Reported-versus-comparator:** Stated 5-35 range versus five 1-to-5 domains.
- **Reasoning/calculation:** Five 1-to-5 scores yield 5-25, not 5-35; no rounding applies. Direct observation is the stated description/range; inference is that an item/weighting rule is missing or one label is wrong.
- **Alternative source-grounded interpretations:** Additional items or non-unit scoring could yield 35, but none are supplied.
- **Quality-control relevance:** Scale range controls meaning/comparability of any MPSS result.
- **Potential downstream evidence impact:** If confirmed, a review could code the outcome scale incorrectly.
- **Human question:** What MPSS item count/scoring rule yields 5-35, or should the printed range be 5-25?

## C012 — Site 2008 death count and percentage lack a compatible supplied denominator

- **Category:** Rate-versus-count inconsistency.
- **Checker provenance:** NC012; XC007.
- **Exact source locations:** DOC-003 PDF p.8 (`joi250093supp2_prod_1768590553.09463.pdf#page=8`), eTable 5; DOC-003 PDF p.9 (`#page=9`), eTable 6.
- **Source evidence:** eTable 5 site 2008 recruitment/ITT denominator `40`; eTable 6 gives `5 (7.5%)` deaths.
- **Reported-versus-comparator:** 5 deaths (7.5%) versus same-site 40-person recruited/ITT denominator.
- **Reasoning/calculation:** If eTable 6 uses 40, `5/40×100=12.5%`; 7.5%=3/40. Direct observation is the count, percentage, and matched site denominator; inference is conditional because eTable 6 does not itself print a denominator. `5/0.075=66.67`, and no 66-67 site population is supplied.
- **Alternative source-grounded interpretations:** A distinct unprinted death denominator may exist.
- **Quality-control relevance:** Count/proportion pairs are readily reused in cluster summaries.
- **Potential downstream evidence impact:** If confirmed, a cluster mortality rate could be copied incorrectly.
- **Human question:** What denominator generated 7.5% at site 2008, and should the entry be 5 (12.5%), 3 (7.5%), or another verified value?

## C013 — Protocol message dose changes from 178 to 134 without supplied reconciliation

- **Category:** Cross-document numeric inconsistency.
- **Checker provenance:** XC003.
- **Exact source locations:** DOC-002 PDF p.16 (`joi250093supp1_prod_1768590553.08963.pdf#page=16`); p.53 (`#page=53`); p.80 (`#page=80`); pp.101-109 (beginning at `#page=101`); DOC-001 PDF p.3 (`jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3`).
- **Source evidence:** p.16 says `178` SMS over six months; p.53, p.80, the 1-134 message log, and main article p.3 report `134` SMS over six months, with differing within-period schedules.
- **Reported-versus-comparator:** 178 versus 134 for matched mTB-Tobacco six-month participant dose.
- **Reasoning/calculation:** Difference is 44 messages, not a precision difference. Direct observation is the displayed dose totals/schedules; inference is an unlabelled version change because the p.16 passage does not state that it was superseded.
- **Alternative source-grounded interpretations:** A formal amendment is plausible given the package’s version-change material, but no supplied statement ties p.16 to the later 134-message regimen.
- **Quality-control relevance:** Dose version identity is needed to interpret/replicate the intervention.
- **Potential downstream evidence impact:** If confirmed, evidence syntheses could attribute the observed trial to the wrong intervention regimen.
- **Human question:** Was the 178-message plan formally superseded by the 134-message regimen, and how should the obsolete/current version be labelled?

## Ledger count

- **Stable candidates:** 13 (C001-C013).
- **Status of every record:** Pending Human Adjudication.
