# Stable candidate ledger

Pending Human Adjudication. Registration follows the independent inclusion screen; no old candidate selection or count target was used. Stable IDs are assigned in source order and are never deleted. One distinct included issue is registered. Evidence fields reflect the completed mechanical recheck; inclusion audit reflects the fresh quality auditor's confirmed conclusion.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article Table 2 cumulative-incidence columns vs REPORT main article Table 2 absolute-risk-difference column and footnote a | reproduced | CONFIRMED | F-NUM-001 |

## C001 — Five nonfatal endpoint absolute eight-year risk differences do not reconcile with the displayed risks

**Candidate statement:** For heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation, Table 2's absolute eight-year risk differences do not reconcile with the adjacent Kaplan–Meier cumulative incidences under the stated nonsurgical-minus-surgery subtraction, even allowing displayed rounding. One repeated pattern includes all five rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 cumulative-incidence columns vs REPORT main article Table 2 absolute-risk-difference column and footnote a

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Checker provenance:** Numeric reviewer root/numeric_checker emitted F-NUM-001, included by fresh root/inclusion_screen. Cross-source reviewer root/cross_checker independently emitted F-XS-001 and statistical pass 1 reviewer root/statistics_one emitted F-ST1-001; both are screened out as DUPLICATE_OF_INCLUDED and reference C001. Their complete affected locations and estimator context are retained here. The Finding IDs classification field lists the sole INCLUDE finding, as required by the contract.

**Classification rationale:** Both conflicting displays are in the same REPORT main article, making S_W the sole conflicting relationship. REPORT supplement eTable 5 corroborates the marginal risks; corroboration does not add S_C. No PLAN source is a conflicting comparator. Numerical risk-contrast identity belongs to statistical_results rather than result-attribution ambiguity.

**Classification ambiguity:** None

**Exact source locations:**

- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2](../../jama_aminian_2019_oi_190103.pdf#page=7): every surgical/control incidence, ARD point and its CI in the heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation rows, column headings, outcome-specific risk sets and footnotes a/b.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 4, Statistical Analysis](../../jama_aminian_2019_oi_190103.pdf#page=4): eight-year Kaplan–Meier cumulative incidence and absolute-risk differences, percentile bootstrap intervals from 1000 iterations, separate fully adjusted Cox models.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 1, abstract](../../jama_aminian_2019_oi_190103.pdf#page=1): all seven prespecified secondary outcomes are reported, establishing the affected component endpoints as key secondary for this review.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 8, Figure 3 panels B–F and caption](../../jama_aminian_2019_oi_190103.pdf#page=8): corresponding outcome curves and individual risk-set rules; no separate ARD population is specified.
- [joi190103supp1_prod.pdf — PDF p. 7, eTable 5 Year 8 rows](../../joi190103supp1_prod.pdf#page=7): all corresponding marginal risks/CIs corroborate the incidence side. This is supplementary corroboration, not an additional conflicting relationship.

**Source evidence:** Table 2 labels the absolute eight-year risk difference and footnote a defines nonsurgical control minus metabolic surgery. Footnote b assigns adjustment to Cox HRs and P values. Source-matched direct layout text and direct page 7 rendering agree; independent inclusion screening reread all cited source locations.

**Reported-versus-comparator:** All incidence and contrast values below are percentage points at eight years. The reported CIs remain source values; no CI is inferred by subtracting marginal limits.

| Outcome | Surgery/control initial risk sets | Surgical risk % | Control risk % | Printed ARD (95% CI) | Difference of displayed risks | Allowable subtraction interval | Allowable printed ARD interval |
|---|---|---:|---:|---|---:|---|---|
| Heart failure | 2049/10093 | 6.8 | 18.9 | 12.9 (10.4–15.1) | 12.1 | 12.00–12.20 | 12.85–12.95 |
| Coronary artery disease | 2050/10331 | 7.9 | 11.6 | 4.2 (1.9–6.8) | 3.7 | 3.60–3.80 | 4.15–4.25 |
| Cerebrovascular disease | 2245/11077 | 4.1 | 5.6 | 1.8 (−0.03–3.4) | 1.5 | 1.40–1.60 | 1.75–1.85 |
| Nephropathy | 1937/9190 | 6.1 | 16.3 | 11.1 (8.8–13.6) | 10.2 | 10.10–10.30 | 11.05–11.15 |
| Atrial fibrillation | 2135/10734 | 7.9 | 13.6 | 6.5 (4.4–8.7) | 5.7 | 5.60–5.80 | 6.45–6.55 |

**Reasoning procedure:** Match each row's endpoint, eight-year time, risk set and group direction. Read the absolute-risk subtraction rule in footnote a and the separate Cox adjustment in footnote b. Apply half-unit rounding intervals before comparing point contrasts. Check the methods and repeated marginal risks for an immediately stated alternate point estimator. Consolidate the common rule/pattern across the five rows.

**Calculation:** Each one-decimal risk and ARD allows ±0.05 percentage points. The difference of the two risks allows ±0.10 around the displayed subtraction; the reported ARD allows ±0.05. All five resulting interval pairs are disjoint. The primary composite, secondary composite and mortality rows reconcile under the same subtraction rule. No modeled HR is compared to a crude ratio, and no original model variance is reconstructed.

**Affected result or extracted value:** The eight-year absolute risk differences and associated reported bootstrap uncertainty for the five named component outcomes. A data extractor can obtain distinct points by copying the ARD column or subtracting the reported risks.

**Why context does not resolve it:** The same outcome/time/risk-set labels and explicit subtraction direction provide two nonreconciling representations. The package describes bootstrapping for intervals and adjustment for HRs, but does not identify a distinct adjusted-risk, bootstrap-point-summary, population or censoring definition for these ARD points. A reader cannot select the intended extracted risk difference at once from those displays.

**Alternative source-grounded interpretations:** The ARDs may derive from a distinct, unstated risk point-estimation procedure or population; alternatively, the displayed marginal risks and contrast need reconciliation against the original analysis output. The supplied package establishes neither explanation. Outcome-or-death rates in eTable 4 are a separately defined person-time measure and do not establish an alternative eight-year risk contrast.

**Mechanical evidence recheck:** Fresh root/evidence_recheck independently found all cited source and comparator locations, matched every printed value and rule, reproduced all five disjoint half-unit interval comparisons, and confirmed statistical_results/S_W with evidence state reproduced. No transcription correction or classification change was needed. Original ARD point estimator and analysis inputs remain unavailable; see verification/evidence_recheck.md.

**Potential downstream evidence impact:** If confirmed by human review, a systematic reviewer or data extractor could carry different absolute association estimates for these five outcomes depending on which Table 2 columns are used. No propagation, paper-level conclusion change, or change to adjusted HR significance is asserted.

**Human verification steps:** Confirm the five rows/footnote against the supplied PDF; identify the original eight-year group risks, the point estimator and analysis population used for each ARD; establish whether the risk and contrast columns share the same estimand; reconcile the associated bootstrap intervals once the estimand is identified. The displayed subtractions are comparators, not suggested final corrections.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Fresh quality auditor root/quality_audit confirms the inclusion threshold and classification for C001, with no screening repair or additional candidate. Every five-row occurrence remains one stable candidate; human adjudication remains pending.
