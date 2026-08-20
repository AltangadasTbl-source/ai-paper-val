# Stable Quality-Control Candidate Ledger

Candidate discovery was rebuilt from complete mapped source evidence without a count limit. Genuine duplicate raw records were merged only when they concerned the same printed values, comparator, and consistency rule. Every stable candidate is **Pending Human Adjudication**; no severity, validity, acceptance, exclusion, or correction is assigned.

## C001 — Shared-placebo race missingness does not reconcile with the printed denominator

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Numeric review N007.
- **Exact source locations:** [DOC-001 Table 1 and footnote b — PDF p. 6](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>).
- **Printed evidence:** Shared placebo is `n=164`; race entries use denominator 160 and sum to 160; footnote b says race was unknown or unreported for 3 participants.
- **Rule and calculation:** `164 - (2 + 6 + 151 + 1) = 4`, not 3. Integer missingness has zero rounding tolerance.
- **Direct observation versus inference:** The one-participant mismatch is observed. An omitted category, denominator error, or footnote error is only a possible explanation.
- **Source-grounded alternatives:** Footnote b may cover a differently defined subset, but the table prints no such qualification.
- **Remaining human question:** Are four participants unclassified for race, or is one printed race denominator/numerator or the footnote count incorrect?

## C002 — SVC values have incompatible monthly-rate and 24-week-change labels

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Numeric N012; statistical pass 1 RAW-S-P1-004.
- **Exact source locations:** [DOC-001 Secondary Efficacy Outcomes — PDF p. 4](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 3A — PDF p. 16](<../../joi240158supp3_prod_1742927563.7911.pdf#page=16>).
- **Printed evidence:** The article prints `-9.32`, `-8.53`, and `-0.78` as PPN per month over 24 weeks; eTable 3A prints the same values under `24-week Change Estimate` for SVC (% predicted).
- **Rule and calculation:** A monthly rate and cumulative 24-week change are different scales. The supplied sources provide no conversion or estimand definition that permits the same `-9.32`, `-8.53`, and `-0.78` values to carry both labels; no external month-length convention is required for the printed-label contradiction.
- **Direct observation versus inference:** The conflicting labels are observed; the conversion is diagnostic and does not identify the intended label.
- **Source-grounded alternatives:** The article may contain an editorial unit label, or the eTable heading may omit a rate convention; no conversion convention is supplied.
- **Remaining human question:** Is the estimand a monthly rate or a total 24-week change, and which location should carry the intended unit?

## C003 — Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Cross-source candidate 1; statistical pass 1 RAW-S-P1-001 component.
- **Exact source locations:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Printed evidence:** Article shared-placebo slope `-1.03` with 95% CrI `-1.176 to -0.892`; eTable 2 `-1.03` with 95% CrI `-1.181 to -0.894` for Regimen C placebo with sharing.
- **Rule and calculation:** The named Bayesian shared-parameter model, group, endpoint, unit, and precision match, but both three-decimal endpoints differ (`0.005` and `0.002`).
- **Direct observation versus inference:** Endpoint differences are observed; different model runs, data locks, or transcription are possible but unlabelled.
- **Source-grounded alternatives:** An undocumented posterior run or production update could explain the difference.
- **Remaining human question:** Which primary-model posterior output and credible interval is authoritative for the shared-placebo component?

## C004 — Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Cross-source candidate 2; statistical pass 1 RAW-S-P1-001 component.
- **Exact source locations:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Printed evidence:** Article pooled-active slope `-1.00` with 95% CrI `-1.153 to -0.858`; eTable 2 `-1.00` with 95% CrI `-1.143 to -0.847`.
- **Rule and calculation:** The matched three-decimal credible-interval endpoints differ by `0.010` and `0.011`, while the point estimate and model labels agree.
- **Direct observation versus inference:** Endpoint differences are observed; an undocumented model run or transcription explanation is not established.
- **Source-grounded alternatives:** Separate production outputs may exist, but neither supplied page identifies them.
- **Remaining human question:** Which primary-model posterior output and credible interval is authoritative for pooled CNM-Au8?

## C005 — Bayesian mortality event rates differ between article text and cited eTable 2

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Numeric N016; cross-source candidate 3; statistical pass 1 RAW-S-P1-001 component.
- **Exact source locations:** [DOC-001 Primary Efficacy Outcome — PDF p. 4](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Printed evidence:** Article: shared placebo `0.007` and pooled active `0.006` events/month. eTable 2: `0.010` and `0.009` events/month for the same named Bayesian shared-parameter model.
- **Rule and calculation:** Each matched group differs by `0.003 events/month`, which cannot be the same value rounded to three decimals.
- **Direct observation versus inference:** The matched value pairs differ directly. Alternate event definitions, time scales, or model runs are not labelled.
- **Source-grounded alternatives:** One display may use an unstated alternate posterior summary or definition.
- **Remaining human question:** Do the two displays represent distinct analyses, and if not which pair is authoritative?

## C006 — Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Numeric N018; cross-source candidate 5; statistical pass 1 RAW-S-P1-003.
- **Exact source locations:** [DOC-001 Figure 3 and Biomarker Analyses — PDF p. 8](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-004 eTable 3B — PDF p. 17](<../../joi240158supp3_prod_1742927563.7911.pdf#page=17>).
- **Printed evidence:** All displays give `-9.5%` and `P=.04`; Figure 3 CI is `-17.8% to -0.5%`, narrative is `-17.8% to -0.4%`, and eTable 3B is `-18.0% to 0`.
- **Rule and calculation:** A matched result should repeat one CI unless a different analysis is labelled. Figure/text upper endpoints differ by `0.1` point at one-decimal precision, and eTable 3B prints different endpoints including an upper endpoint displayed as `0`; the unrounded eTable endpoint is unavailable.
- **Direct observation versus inference:** The endpoint differences are observed. Independent rounding or an alternate model run is possible but not supplied.
- **Source-grounded alternatives:** eTable 3B may use a different unlabelled run or precision convention.
- **Remaining human question:** What unrounded plasma-NfL interval underlies each display, and are these intended to be one result or labelled distinct analyses?

## C007 — Serum NfL regimen-only values and contrast do not reconcile across displays

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Numeric N019; cross-source candidate 4; statistical pass 1 RAW-S-P1-002.
- **Exact source locations:** [DOC-001 Figure 3 and Biomarker Analyses — PDF p. 8](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-004 eTable 3B — PDF p. 17](<../../joi240158supp3_prod_1742927563.7911.pdf#page=17>).
- **Printed evidence:** Article: placebo `+30.8%`, active `+0.4%`, difference `-23.2%` (95% CI `-39.5% to -2.5%`; `P=.03`). eTable: placebo `+26.8%`, active `+0.4%`, difference `-26.4%` (95% CI `-50.3% to -2.6%`; `P=.03`).
- **Rule and calculation:** Across locations, placebo change differs by `30.8 - 26.8 = 4.0` percentage points and the printed treatment contrast differs by `|-23.2 - (-26.4)| = 3.2` points; both confidence-interval endpoints also differ. The article's `-23.2%` is compatible with a geometric-mean-ratio diagnostic, `[(1.004 / 1.308) - 1] x 100 = -23.24%`, so crude percentage-point subtraction is not treated as an internal article inconsistency.
- **Direct observation versus inference:** The cross-display placebo, contrast, and interval differences are observed. Different fitted-contrast scales, included samples, plate handling, or model runs are possible but unlabelled.
- **Source-grounded alternatives:** A distinct ERO model, plate rule, population, or data cut may exist but is not identified in the article.
- **Remaining human question:** Which regimen-only serum-NfL model output, population, arm changes, contrast, and CI are intended for publication?

## C008 — Discussion total of 13 events conflicts with the 14 events displayed in Table 2

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Checker provenance:** Cross-source candidate 6.
- **Exact source locations:** [DOC-001 Table 2 — PDF p. 7](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>); [DOC-001 Discussion — PDF p. 9](<../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9>).
- **Printed evidence:** Table 2 reports 5/120 pooled-active and 9/162 shared-placebo death/PAV events; Discussion states a total of 13 RCT-period events in those groups.
- **Rule and calculation:** `5 + 9 = 14`, not 13.
- **Direct observation versus inference:** The one-event difference is observed. A different event definition, cutoff, or exclusion is possible but not stated in the Discussion sentence.
- **Source-grounded alternatives:** Discussion may refer to a narrower event set than Table 2's death-or-PAV endpoint.
- **Remaining human question:** Which event list and cutoff underlie the Discussion total, and does it intentionally exclude one Table 2 event?

## Registration summary

- Stable candidate set: C001, C002, C003, C004, C005, C006, C007, C008.
- Stable candidate count: 8.
- All candidates remain Pending Human Adjudication.
