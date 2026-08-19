# Statistical Consistency Review — Pass 1

## Pass identity and scope

- **Runtime agent ID:** `/root/statistics_pass_1`
- **Model / reasoning effort:** `gpt-5.6-terra` / `high`
- **Scope:** `S001` through `S065` in `statistics/relationship_inventory.md`, covering all mapper-designated inferential relationships and all displayed result-level inferential relationships in the merged main/support evidence maps.
- **Outcome:** 65 relationships completed; 4 uncapped raw candidates; 0 display-zero records.
- **Boundary:** these are quality-control observations for human adjudication. They have no C IDs, severity, validity, acceptance, rejection, or correction assignment.

## Methods and limitations

Point estimates were checked for interval containment and endpoints for order. Direction was checked against the stated contrast, effect measure, scale, graphical/narrative label, and matched repetition. A P/CI/SE check was called a diagnostic only when a table supplied an SE and an apparent repeated-measures estimate; it was not used as a replacement for the reported analysis because the source does not explicitly identify the CI/test construction for every output. Cox intervals are profile-likelihood intervals where stated, so no Wald-P reconstruction was made. No sidedness, degrees of freedom, covariance structure, variance estimator, multiplicity adjustment, model version, denominator, or estimand mapping was inferred when absent.

No coherent finite-precision display-zero P value occurred in the assigned scope. Therefore no `DISPLAY_ZERO_NOT_CANDIDATE` record was required.

## Raw candidate observations

### RAW-S-P1-001 — Primary-model component values differ between the article and its cited eTable 2

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** `jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4`, Primary Efficacy Outcome; `joi240158supp3_prod_1742927563.7911.pdf#page=15`, eTable 2, “Primary Efficacy Analysis of Function and Mortality with Bayesian Shared Parameter Model.”
- **Direct observation:** The main article says the shared-placebo ALSFRS-R slope is -1.03 (95% CrI, -1.176 to -0.892), the pooled-active slope is -1.00 (-1.153 to -0.858), and mortality event rates are 0.007 and 0.006 events/month, respectively. It directs readers to eTable 2. eTable 2, under the same named Bayesian shared-parameter model, prints slopes -1.03 (-1.181 to -0.894) and -1.00 (-1.143 to -0.847), and mortality event rates 0.010 and 0.009 events/month.
- **Rule:** Matched source locations explicitly identify the same Bayesian shared-parameter primary analysis and same shared-placebo/pooled-active components. Such a repeated result should have the same displayed component intervals and rates unless a different analysis run, population, time, or estimand is explicitly identified.
- **Derived diagnostic:** The slope interval differences exceed a one-last-digit presentation change in at least one endpoint, and 0.007/0.006 versus 0.010/0.009 cannot be reconciled by rounding to the displayed three decimals.
- **Alternative source-grounded interpretation:** The sources may reproduce different undocumented fitted-model runs or analytic versions; the supplied PDFs do not label a different model, population, run date, or estimand for the eTable.
- **Exact human question:** Do the article text and eTable 2 intentionally report different Bayesian model runs, and if so which model specification/population/run date applies to each printed component estimate?

### RAW-S-P1-002 — Serum NfL primary-analysis values differ between the article and ERO eTable 3B

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** `jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8`, Figure 3 and Biomarker Analyses; `joi240158supp3_prod_1742927563.7911.pdf#page=17`, eTable 3B, pooled CNM-Au8 versus regimen placebo, serum NfL.
- **Direct observation:** The article identifies serum NfL as regimen-placebo versus combined-dose CNM-Au8 and prints placebo change +30.8%, active change +0.4%, difference -23.2% (95% CI -39.5% to -2.5%), P=.03. The matched ERO eTable 3B prints placebo +26.8%, active +0.4%, difference -26.4% (95% CI -50.3% to -2.6%), P=.03.
- **Rule:** The relationship has the same outcome, regimen-placebo comparator, pooled-active comparison, and 24-week repeated-measures presentation. Exact repeated arm change, contrast, and interval values should agree unless a different model/run/population is identified.
- **Derived diagnostic:** The active value and rounded P agree, but the placebo change, contrast, and both interval endpoints differ. The supplied labels do not disclose a distinct analysis run.
- **Alternative source-grounded interpretation:** The eTable could represent a distinct ERO model or data cut not described in the article prose; the article does state that serum NfL was analysed with regimen placebo because plates differed, but it does not identify a separate output matching the eTable values.
- **Exact human question:** Which serum-NfL model output is intended for the stated regimen-placebo/pool-active Week-24 analysis, and do the discrepant values arise from a documented population, processing, or data-cut difference?

### RAW-S-P1-003 — Plasma NfL CI upper endpoint differs within the main-article Figure 3/text repetition

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** `jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8`, Figure 3A annotation and Biomarker Analyses prose.
- **Direct observation:** Figure 3A prints -9.5% (95% CI, -17.8% to -0.5%), P=.04. The nearby prose for the same plasma-NfL comparison prints -9.5% (95% CI, -17.8% to -0.4%), P=.04.
- **Rule:** Same-page, same comparison, point estimate, lower endpoint, and P value identify a matched repeated CI; a CI endpoint should reproduce identically unless a distinct calculation is labelled.
- **Derived diagnostic:** The upper endpoint differs by 0.1 percentage point. This is an observed transcription/repetition mismatch, not a derived P-value critique.
- **Alternative source-grounded interpretation:** One display may have been independently rounded from an unprinted higher-precision value or one may be a typographical error; no separate calculation is named.
- **Exact human question:** What is the authoritative unrounded plasma-NfL upper CI endpoint for the displayed -9.5% contrast, and which location should be corrected if the two displays are intended to repeat the same result?

### RAW-S-P1-004 — SVC unit/scale label differs between article prose and eTable 3A

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4`, Secondary Efficacy Outcomes; `joi240158supp3_prod_1742927563.7911.pdf#page=16`, eTable 3A, SVC (% predicted).
- **Direct observation:** The article calls the 24-week SVC values -9.32 versus -8.53 and their -0.78 difference “PPN per month.” eTable 3A carries the same values under “24-week Change Estimate” for “SVC (% predicted)” without a per-month unit.
- **Rule:** A single repeated 24-week SVC estimate should use one compatible unit/scale label. “24-week change” in percent predicted and “percent predicted normal per month” are different rate/scale labels.
- **Derived diagnostic:** The same numeric values recur across locations, strengthening the match; no conversion factor or separate rate model is supplied that would reconcile the two unit labels.
- **Alternative source-grounded interpretation:** “Per month” in the article may be a label-only wording error, or the table may omit a rate unit; the source does not state a conversion or alternative estimand.
- **Exact human question:** Is the reported SVC estimand a total 24-week change in percent predicted or a monthly rate, and which label should govern the repeated values?

## Relationship-level compatibility notes

- `S003`, `S004`, `S005`, `S008`-`S018`, `S019`-`S021`, and `S023`-`S053`: all displayed point estimates lie within their stated intervals and all endpoints are ordered.
- Table 2 HR labels and their direction are compatible with the stated event outcome. Its profile-log-likelihood CIs prevent a presumed Wald P-value calculation.
- eTable 3A/B rows with displayed SEs have only diagnostic approximate P/CI agreement recorded in the inventory; no inferential contradiction is asserted from finite printed precision.
- eTable 3B NfL CI endpoints displayed as `0` are endpoints rounded to integer precision, not P-value display zeros and not candidates solely because a rounded interval endpoint meets the null.
- eFigure sensitivity uses placebo-minus-active direction, whereas article prose uses active-minus-placebo direction. After sign reversal its estimate/CI agree; `.05` versus `.051` is compatible finite precision.

## Handoff

Pass 2 must revisit every `S001`-`S065` against the complete cross-lane candidate ledger and evidence-recheck facts, including denominator, arithmetic, population, duplicate-value, label/scale, rate/count, figure, and cross-source implications. It must retain all four raw observations unless a later coordinator assigns stable C IDs; it may append newly found raw candidates without suppressing these records.

## Explicit pass-1 completion index

| Stable ID | Status |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
