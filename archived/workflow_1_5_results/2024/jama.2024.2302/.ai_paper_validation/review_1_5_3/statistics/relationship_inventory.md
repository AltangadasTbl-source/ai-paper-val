# Statistical Relationship Inventory — Pass 1

## Scope and stable-ID normalization

- **Pass:** Statistical pass 1 (`gpt-5.6-terra`, high-effort fresh specialist; runtime task ID `/root/statistical_pass_1`).
- **Scope:** All 20 mapper-assigned inferential relationships: main-map `S001`-`S013` and support-map `S-SUP-001`-`S-SUP-007`.
- **Normalization rule:** Main-map IDs retain their supplied package-wide sequence. Support-map IDs are normalized in mapper order to `S014`-`S020`; the original support ID remains in every record. No relationships were collapsed.
- **Methods:** Source-linked checks covered point-estimate containment, endpoint ordering, sign/direction, effect measure and scale labels, repetitions across supplied sources, and interval/P-value/test/statistic/SE compatibility only where compatible definitions were supplied. A numeric reconstruction below is explicitly a diagnostic approximation, never a replacement for the reported model.
- **Status convention:** Each record below has `PASS_1_COMPLETE`. This pass creates no `C` IDs and assigns no disposition, validity, severity, or correction.

## Stable relationship records

### S001 — Primary SAE, abstract form

- **Mapper source:** main `S001`; [PDF-001 p. 1](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1>), matched p. 6 and p. 8.
- **Relationship:** 44/159 (28%) early vs 27/149 (18%) late; Bayesian late-minus-early RD −7.9% (95% CrI −16.9% to 0%) and posterior benefit probability 97%.
- **Pass-1 checks:** Estimate is within the printed ordered CrI; negative RD and benefit direction agree with late-relative-to-early labeling. The p. 6/p. 8 repetitions differ only in stated display precision and remain compatible. The result is Bayesian; no P-value/test/SE compatibility calculation is applicable.
- **Cross-location note:** The companion eTable 2 frequentist result is not used as a same-model comparator; it has explicitly different frequentist CI/P-value reporting (S015).
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S002 — Hospital days, abstract form

- **Mapper source:** main `S002`; [PDF-001 p. 1](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1>), matched p. 6.
- **Relationship:** Median (IQR) hospital days 19.0 (9.8-35.0) early vs 16.0 (7.0-38.0) late; Bayesian RR 0.91 (95% CrI 0.74-1.11), benefit probability 82%.
- **Pass-1 checks:** RR is contained within its ordered positive CrI; RR below 1 and the stated “fewer hospital days” benefit definition agree. No Bayesian P value, test statistic, or SE is supplied.
- **Cross-location note:** The eTable’s frequentist RR/CI/P value is separately tracked in S016 and is not a contradiction merely because it is a different inferential framework.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S003 — Abstract subgroup-benefit summary

- **Mapper source:** main `S003`; [PDF-001 p. 1](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1>), matched p. 7-p. 8.
- **Relationship:** Posterior probability of benefit is 99% in the <28-week and bronchopulmonary-dysplasia subgroups.
- **Pass-1 checks:** The detailed matched results (S009-S012) repeat 99% for those two subgroup rows and define benefit as RR <1/RD <0 for late relative to early. No interval/P-value calculation is applicable to a posterior probability alone.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S004 — Planned primary-effect assumptions and sample size

- **Mapper source:** main `S004`; [PDF-001 p. 4](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>).
- **Relationship:** Planned 30% early vs 20% late event rates; 586 with outcome data for 80% power at two-sided α=.05, with 615 planned enrollment after 5% loss allowance.
- **Pass-1 checks:** This is a prespecified frequentist design calculation, not an observed effect. Its denominator and direction labels are explicit. The source does not provide its exact power-test formula, variance convention, or allocation rounding, so no independent power recomputation is used as a candidate rule.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S005 — Article analysis populations, models, and priors

- **Mapper source:** main `S005`; [PDF-001 p. 4](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>).
- **Relationship:** ITT excluding withdrawals; Bayesian logistic/negative-binomial mixed models with GA and site terms; GEE logistic frequentist primary analysis after mixed-model nonconvergence; stated neutral-prior range 0.33-3.0 for categorical/count intervention effects.
- **Pass-1 checks:** Model labels and the exception for the frequentist primary analysis are explicit. The distinct SAP prior specifications in S018 are a supplied cross-document definition mismatch and are recorded as pre-ID candidate `P1-S-003`; no assumption is made about an undocumented amendment.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S006 — Interim stopping result

- **Mapper source:** main `S006`; [PDF-001 p. 4](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>), matched S020.
- **Relationship:** At 309 infants in February 2021, posterior probability of decreased SAE rate with late repair was 97%, above the 95% efficacy threshold.
- **Pass-1 checks:** The observed 97% exceeds the printed >95% rule, and direction agrees with the stated late-repair benefit. No estimate, interval, posterior distribution, or stopping-bound computation is supplied, so no further compatibility calculation is applicable.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S007 — Bayesian primary SAE model result

- **Mapper source:** main `S007`; [PDF-001 p. 6](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), matched p. 1, p. 2, p. 8.
- **Relationship:** 44/159 vs 27/149; RD −7.9% (95% CrI −16.9 to 0), RR 0.68 (0.45-1.01), posterior benefit 97%.
- **Pass-1 checks:** Both estimates are contained in ordered intervals; RD/RR signs and benefit definition agree. Table 2 calls the interval a CrI and identifies a Bayesian logistic model, preventing a P-value/SE test reconstruction. Figure 3’s overall RD −0.08 (−0.17 to 0.002) is compatible finite-precision display of this Bayesian result, not an independent conflict.
- **Cross-location note:** S015’s RD −9.0% and RR 0.65 are frequentist values with 95% CIs/P=.01; the source labels the frameworks distinctly.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S008 — Bayesian hospital-day model result

- **Mapper source:** main `S008`; [PDF-001 p. 6](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), matched p. 1.
- **Relationship:** RR 0.91 (95% CrI 0.74-1.11), posterior benefit 82%; RD is NA for the count outcome.
- **Pass-1 checks:** The RR lies in an ordered positive CrI and direction agrees with the stated fewer-days benefit. The NA RD cell agrees with the count-outcome measure label; no Bayesian P value/test/SE is supplied.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S009 — Gestational-age subgroup narrative result

- **Mapper source:** main `S009`; [PDF-001 p. 7](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7>), matched S011.
- **Relationship:** <28 weeks RR 0.61 (0.39-0.94), benefit 99%; ≥28 weeks RR 0.92 (0.47-1.75), benefit 61%; interaction probability 91%.
- **Pass-1 checks:** Each RR is within an ordered positive CrI and the direction agrees with late-relative-to-early benefit. The S011 figure repeats values. The `≥28` actual-result label differs from the SAP’s planned `>28` label (S019); that concrete boundary-label mismatch is recorded as `P1-S-004`.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S010 — BPD and surgical-approach subgroup narrative result

- **Mapper source:** main `S010`; [PDF-001 p. 7](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7>), matched S012-S013.
- **Relationship:** BPD RR 0.50 (0.27-0.87), benefit 99%; no BPD RR 0.85 (0.51-1.37), benefit 75%; BPD interaction probability 95%; no stated approach modification.
- **Pass-1 checks:** Estimates are contained in ordered positive CrIs; directions agree with the benefit definition. The source provides posterior probabilities rather than P values and does not provide interaction intervals/SEs.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S011 — Figure 3 gestational-age subgroup detail

- **Mapper source:** main `S011`; [PDF-001 p. 8](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>).
- **Relationship:** Event counts, RDs, RRs, 95% CrIs, and posterior benefit probabilities for <28 and ≥28 weeks.
- **Pass-1 checks:** All RDs/RRs are inside correctly ordered intervals; each negative RD/RR <1 agrees with the late-relative-to-early favorable definition. Raw count contrasts need not equal model-adjusted RD/RR and are not treated as a contradiction. The ≥28 label is included in `P1-S-004`.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S012 — Figure 3 BPD subgroup detail

- **Mapper source:** main `S012`; [PDF-001 p. 8](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>).
- **Relationship:** Event counts, RDs, RRs, 95% CrIs, and posterior benefit probabilities for BPD yes/no.
- **Pass-1 checks:** Point estimates are contained in ordered intervals; signs/directions and effect labels agree. No P value/test statistic/SE or interaction interval is supplied.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S013 — Figure 3 surgical-approach and overall detail

- **Mapper source:** main `S013`; [PDF-001 p. 8](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>), matched S007.
- **Relationship:** Laparoscopic, open, and overall event counts, RDs, RRs, 95% CrIs, and probabilities.
- **Pass-1 checks:** Each point estimate is contained in an ordered interval and directions agree with favorable-outcome labeling. Overall Figure 3 values are compatible with Table 2 after their explicitly different display precision (RD −0.08 [−0.17 to 0.002] vs −7.9% [−16.9% to 0]).
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S014 — Analysis framework and estimands

- **Mapper source:** support `S-SUP-001`; [PDF-003 p. 4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=4>), [PDF-003 pp. 7-8](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=7>), [PDF-004 p. 5](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>).
- **Relationship:** SAP defines Bayesian analyses as primary and frequentist analyses as secondary; binary/count/ordinal/continuous model and interval labels are specified.
- **Pass-1 checks:** The result-specific model/interval distinctions make S015-S016 different-framework comparators rather than duplicate point estimates. The primary endpoint wording differs across actual source locations (>1 vs at least one) and the time-origin wording differs (enrollment vs randomization); these supplied label/definition mismatches are `P1-S-001` and `P1-S-005`.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S015 — Frequentist eTable 2 primary SAE result

- **Mapper source:** support `S-SUP-002`; [PDF-004 p. 5](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>).
- **Relationship:** 44/159 vs 27/149; late-minus-early RD −9.0% (95% CI −16.5% to −2.0%), P=.01; RR 0.65 (0.46-0.92), P=.01.
- **Pass-1 checks:** Both estimates are contained in ordered CIs and have direction consistent with late benefit. **Diagnostic approximation:** using displayed RR/CI endpoints, log(RR)≈−0.431 and implied SE≈0.177, giving two-sided normal-tail P≈.015. It is only a rounded diagnostic: exact coefficient, SE, P-value rounding rule, and whether the displayed CI uses the exact same GEE implementation are not supplied. It therefore yields no P/CI candidate. The `>1 SAE` endpoint label conflicts with the matched main table’s `≥1` label and is `P1-S-001`.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S016 — Frequentist eTable 2 hospital-day result

- **Mapper source:** support `S-SUP-003`; [PDF-004 p. 5](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>).
- **Relationship:** Medians/IQRs 19.0 (9.8,35) vs 16.0 (7,38); RR 0.91 (95% CI 0.74-1.12), P=.36, negative-binomial model.
- **Pass-1 checks:** RR is contained in an ordered positive CI and direction agrees with fewer late-group hospital days. **Diagnostic approximation:** displayed log-RR and CI imply SE≈0.106 and a two-sided normal-tail P≈.37; the printed .36 is not a source-grounded contradiction because exact model coefficient, SE, inferential test, and rounding policy are not supplied. No RD/P cell is printed for this count outcome, consistent with the measure label.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S017 — SAP frequentist/Bayesian computation definitions

- **Mapper source:** support `S-SUP-004`; [PDF-003 pp. 7-8](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=7>).
- **Relationship:** Binary outcomes report RR/RD from logistic models; count outcomes RR; ordinal OR; continuous mean difference; 95% CI/CrI conventions and posterior benefit thresholds are stated.
- **Pass-1 checks:** The measure/scale labels explain why no RD is printed for hospital days and why raw proportions are not expected to equal adjusted model estimates. No contradictory interval or direction is identified within this definition record.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S018 — SAP priors and diagnostics

- **Mapper source:** support `S-SUP-005`; [PDF-003 p. 8](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=8>).
- **Relationship:** Binary categorical intervention prior is log-OR Normal(0,0.7), described as OR 1.0 (95% CrI 0.2-4); count prior RR 1.0 (0.33-3.3), plus specified remaining priors and MCMC diagnostics.
- **Pass-1 checks:** The prior-scale labels and endpoints are explicit. They conflict with the main article’s stated 0.33-3.0 range for both categorical/count outcomes (S005); this is `P1-S-003`. No supplied source establishes whether one document describes an approved amendment or a simplified post hoc summary.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S019 — Sensitivity and subgroup inferential plan

- **Mapper source:** support `S-SUP-006`; [PDF-003 p. 9](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=9>), [PDF-002 p. 13](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=13>).
- **Relationship:** mITT sensitivity/PP plan; hierarchical subgroup analyses including GA `<28`/`>28`; interaction prior Normal(0, SD 0.6) in SAP.
- **Pass-1 checks:** The planned GA upper stratum is printed `>28`, while the article reports `≥28` (S009/S011), yielding `P1-S-004`. The protocol and SAP interaction-prior descriptions are source-specific planned definitions; absent an amendment/version-to-analysis mapping, they are not mechanically equated.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

### S020 — Interim inferential rule and observed stop statement

- **Mapper source:** support `S-SUP-007`; [PDF-002 p. 14](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=14>), [PDF-003 p. 4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=4>).
- **Relationship:** Efficacy rule probability of decreased SAEs >95%; observed April 2021 probability 97%, with safety rule >90% increased harm.
- **Pass-1 checks:** 97% exceeds 95%; direction and the repeated stop statement agree with S006. No posterior interval/SE/test statistic is supplied for an independent quantitative recheck.
- **Status:** `PASS_1_COMPLETE`; `PASS_2_COMPLETE`.

## Pass-1 pre-ID candidate records

These are quality-control candidates for later stable-ID registration and exact-source recheck. They are not adjudications and have no `C` IDs.

### P1-S-001 — Matched primary endpoint is labeled `≥1` in the article and `>1` in the supplement

- **Category:** Measure, label, or scale inconsistency.
- **Exact direct-source evidence:** [PDF-001 p. 6, Table 2](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>) labels the matched 44/159 versus 27/149 outcome “Had ≥1 serious adverse event.” [PDF-004 p. 5, eTable 2](<../../../joi240020supp3_prod_1710443209.75411.pdf#page=5>) labels the same group counts, denominators, and frequentist estimates “Infant had > 1 SAE.” The protocol likewise prints `>1` at [PDF-002 p. 2](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=2>), while the SAP prints “≥ 1 SAE” at [PDF-003 p. 4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=4>).
- **Consistency rule:** `≥1` includes infants with exactly one SAE; `>1` excludes them. Identical matched counts cannot represent both endpoint definitions unless no analysed infant had exactly one SAE, which is not supplied.
- **Direct observation vs diagnostic reasoning:** Direct observation is the conflicting threshold labels and matched reported counts. The possible absence of exactly-one-SAE infants is not inferred.
- **Exact human question:** Which threshold was used for the reported 44/159 and 27/149 primary outcome, and should all matched source labels be corrected to that threshold?

### P1-S-002 — Planned secondary hospital-day medians differ across the protocol and SAP

- **Category:** Cross-document numeric inconsistency.
- **Exact direct-source evidence:** [PDF-002 p. 3](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=3>) states the planned 3-day median difference as “18 hospital days for early IH repair versus 15 for late IH repair.” [PDF-003 p. 3](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=3>) states the planned values are 8 versus 5 and explicitly says the protocol’s 18/15 values are incorrect; [PDF-003 p. 4](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=4>) repeats 8/5, alongside means 18/13.
- **Consistency rule:** The same described 3-day median hospital-day hypothesis cannot have both 18/15 and 8/5 group medians.
- **Direct observation vs diagnostic reasoning:** Direct observation is the printed 18/15 and 8/5 values plus the SAP’s clarification. No claim is made about which design values should govern without human review.
- **Exact human question:** Confirm the authoritative secondary-outcome design medians and whether the preserved protocol should carry a correction/erratum note.

### P1-S-003 — Bayesian intervention-prior ranges differ between the article and SAP

- **Category:** Statistical reporting inconsistency.
- **Exact direct-source evidence:** [PDF-001 p. 4](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>) says categorical and count outcomes used an OR or RR prior centered at 1.0 with 95% CrI 0.33-3.0. [PDF-003 p. 8](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=8>) specifies categorical log-OR Normal(0, SD 0.7), described as OR 1.0 (95% CrI 0.2-4), and a count RR prior 1.0 (0.33-3.3).
- **Consistency rule:** These printed endpoint ranges are not the same prior specifications on the stated OR/RR scales.
- **Direct observation vs diagnostic reasoning:** Direct observation is the different stated ranges. Whether the SAP was amended, the article simplified a range, or different priors were used by outcome is not supplied.
- **Exact human question:** Identify the final analysis prior for each primary/major-secondary outcome and reconcile the article and SAP descriptions.

### P1-S-004 — Gestational-age subgroup boundary is printed as `≥28` in results and `>28` in the planned definition

- **Category:** Measure, label, or scale inconsistency.
- **Exact direct-source evidence:** [PDF-001 p. 8, Figure 3](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>) reports `<28 wk` and `≥28 wk`; [PDF-003 p. 9](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=9>) describes the planned GA moderator as `<28; >28 weeks`; [PDF-003 p. 3](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=3>) uses the same `>28` randomization-stratum wording.
- **Consistency rule:** `≥28` includes exactly 28 weeks while `>28` does not. These printed subgroup definitions therefore do not have the same boundary.
- **Direct observation vs diagnostic reasoning:** Direct observation is the different inequality symbols. The count or treatment of infants at exactly 28 weeks is not supplied and is not inferred.
- **Exact human question:** What GA cut point and rounding convention defined the actual subgroup/stratum, and should the planned or reported label be corrected?

### P1-S-005 — Primary-outcome time origin differs between protocol and SAP/article definitions

- **Category:** Measure, label, or scale inconsistency.
- **Exact direct-source evidence:** [PDF-002 p. 3](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=3>) defines the primary measure “from enrollment through 10 months after enrollment,” and [PDF-002 p. 11](<../../../joi240020supp1_prod_1710443209.74911.pdf#page=11>) repeats “10 months after enrollment.” [PDF-003 p. 7](<../../../joi240020supp2_prod_1710443209.75411.pdf#page=7>) defines it from “randomization to 10-month post-randomization”; [PDF-001 p. 6, Table 2 footnote](<../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>) describes the observation period as from randomization until 10 months later.
- **Consistency rule:** Enrollment and randomization are different named time origins; the supplied sources do not define them as identical or quantify any interval between them.
- **Direct observation vs diagnostic reasoning:** Direct observation is the different time-origin terminology. No difference in event counts is inferred.
- **Exact human question:** Were enrollment and randomization operationally the same instant for endpoint ascertainment, and what time origin should label the primary analysis consistently?

## Display-zero coverage

- No assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent finite-precision display zero. Accordingly, no `DISPLAY_ZERO_NOT_CANDIDATE` record was needed in this inventory.

## Pass-1 limitations

- No exact coefficient, SE, variance estimator, degrees of freedom, sidedness, or P-value rounding policy is supplied for the eTable results; diagnostic P approximations in S015-S016 are not candidate rules.
- The supplied sources do not include raw data or a final-analysis amendment log that maps protocol/SAP definitions and priors to each published result.
- Bayesian CrIs and posterior benefit probabilities were not converted into frequentist P values or test statistics.
