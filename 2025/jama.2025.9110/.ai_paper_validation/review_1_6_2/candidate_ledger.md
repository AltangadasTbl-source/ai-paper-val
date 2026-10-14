# Workflow 1.6.2 Candidate Ledger

All candidates remain **Pending Human Adjudication**. This ledger registers only independently included issues. IDs follow first occurrence in the main article: the ventilation and ICU results in abstract order, then the primary-power rationale. Assigned IDs are retained through every subsequent evidence state. Evidence states are finalized from the fresh mechanical recheck; inclusion audits are finalized from the fresh canonical quality audit; all three are CONFIRMED for inclusion only.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, S_C | PLAN protocol and SAP vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-003 |
| C002 | statistical_results | S_W | S_W | REPORT main article Table 2 vs REPORT main article abstract and narrative | reproduced | CONFIRMED | F-ST1-001 |
| C003 | protocol_report | P_R | P_R | PLAN SAP vs REPORT main article | reproduced | CONFIRMED | F-ST1-004 |

## C001 — Planned ventilation Cox analysis replaced by a tobit mean contrast

**Status:** Pending Human Adjudication.

**Candidate statement:** The active SAP's key-secondary time-to-liberation Cox analysis is replaced by a reported tobit analysis of ventilation hours, and its planned cause-specific hazard ratio is not reported.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN protocol and SAP vs REPORT main article and results supplement

**Finding IDs:** F-XS-003

**Checker provenance:** cross_source_consistency_reviewer F-XS-003; statistics_pass_1 F-ST1-002 is independently reproduced and screened out as DUPLICATE_OF_INCLUDED. Its complete additional locations and observations belong to this same candidate.

**Qualifying route:** Route A, category 5.

**Classification rationale:** Prospective PLAN analysis specifications conflict with the reported replacement analysis (P_R). The main article's SAP-concordance assertion also conflicts with the separate results supplement's explicit replacement disclosure (S_C). P_R takes precedence over S_C. Agreement between protocol and SAP is corroboration, not P_P; repeated numerical main results do not add S_W. This refinement was identified and confirmed by the fresh evidence rechecker.

**Classification ambiguity:** The results supplement explicitly discloses the replacement; no superseding plan for that change is supplied.

**Exact source locations:**

- REPORT [main article p. 1, abstract ventilation effect](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1).
- REPORT [main article p. 4, SAP-concordance statement](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- REPORT [main article p. 5, repeated ventilation mean contrast](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5).
- REPORT [main article p. 7, Table 2 ventilation row](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- PLAN [protocol p. 21, lines 679–684](../../joi250040supp1_prod_1753124024.37199.pdf#page=21).
- PLAN [SAP p. 18, lines 416–431](../../joi250040supp2_prod_1753124024.37799.pdf#page=18).
- PLAN [SAP p. 28, Table 1 ventilation analysis](../../joi250040supp2_prod_1753124024.37799.pdf#page=28).
- REPORT [results supplement p. 4, Duration of invasive ventilation](../../joi250040supp3_prod_1753124024.38098.pdf#page=4).
- REPORT [results supplement p. 6, metobit/margins](../../joi250040supp3_prod_1753124024.38098.pdf#page=6).

**Source evidence:** The SAP specifies cumulative-incidence summaries and a cause-specific Cox hazard ratio for liberation from ventilation, adjusting for period and delayed start, stratifying by ICU, with ICU-cluster robust standard errors. Mortality is a competing risk with deaths censored; a 48-hour palliative-extubation rule is supplied. The results supplement expressly describes a lower-bounded continuous response rather than the SAP time-to-event response, with an ICU-random-effect tobit model and observed-outcome margins.

**Reported-versus-comparator:** Reported mean difference 6.8 h (95% CI −3.0 to 16.5), P=.17; comparator is the planned ventilation cause-specific HR analysis, whose result is absent from the complete supplied report map.

**Reasoning procedure:** Match the same ventilation outcome across the active SAP and report; distinguish mean hours from a time-to-liberation hazard ratio; inspect the complete report for the planned analysis. Ventilation is key secondary because its numerical effect is in the abstract.

**Calculation:** Categorical model/estimand replacement; display-precision arithmetic does not apply. No preferred method, reconstructed HR, or power calculation is proposed.

**Affected result or extracted value:** The key-secondary ventilation effect measure and its mortality-handling definition.

**Why context does not resolve it:** Route A category 5 requires registering the unreported planned key-secondary analysis. Disclosure explains the replacement but does not supply the planned HR result.

**Alternative source-grounded interpretations:** A later amendment may authorize replacement, or the report may intentionally present only the replacement. The supplied package discloses the change without a later plan or the planned HR output.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** Every cited location and printed model/result was confirmed directly from supplied PDF native text or fresh source-page rendering. Native searches of all main and results pages, with fresh visual inspection of results pp. 23–32, locate no planned ventilation Cox HR. The absence claim is bounded to supplied report files. C001 adds the corroborating main p. 5 result and the S_C classification refinement; no registered value or page required correction. Full facts and derivative provenance are in verification/evidence_recheck.md.

**Potential downstream evidence impact:** An extractor could record a mean-hour effect where the supplied prospective plan specified a time-to-event HR. This does not establish that either analysis is preferable or that the paper's conclusion changed.

**Remaining human question:** Was the planned Cox analysis formally replaced, and is its cause-specific HR available or intentionally unreported?

## C002 — Printed ICU confidence interval and P value have different null-status readings

**Status:** Pending Human Adjudication.

**Candidate statement:** Table 2 prints an ICU live-discharge HR of 0.93 (95% CI 0.88–1.00) with P=.04: the printed interval includes the ratio null while the printed test is below .05.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 vs REPORT main article abstract and narrative

**Finding IDs:** F-ST1-001

**Checker provenance:** statistics_pass_1; related S009, S024 and S044.

**Qualifying route:** Route A, category 1.

**Classification rationale:** The HR, confidence interval, test and repeated interval all occur in one REPORT document. No plan or supplement is a conflicting comparator.

**Classification ambiguity:** None.

**Exact source locations:**

- REPORT [main article p. 1, abstract ICU-discharge interval](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1).
- REPORT [main article p. 4, two-sided testing and threshold](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- REPORT [main article p. 5, secondary-outcome ICU interval](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5).
- REPORT [main article p. 7, Table 2 ICU row and footnote b](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).

**Source evidence:** Cause-specific HR 0.93; frequentist 95% CI 0.88 to 1.00; P=.04. The interval is copied in the abstract and narrative. Point containment and endpoint ordering reconcile.

**Reported-versus-comparator:** Printed upper CI endpoint 1.00 versus ratio null 1; same-row P=.04 versus .05.

**Reasoning procedure:** Apply the printed 95% interval/test null-status comparison. Do not reconstruct a fitted test from an assumed Wald method.

**Calculation:** 0.88 ≤ 1 ≤ 1.00, whereas .04 < .05. The printed P interval [0.035,0.045] remains below .05. Route A category 1 is exempt from the rounding exclusion. An unrounded upper limit in [0.995,1.005] could display as 1.00 and remains an alternative explanation.

**Affected result or extracted value:** The confidence interval and significance reading of the key-secondary ICU live-discharge HR.

**Why context does not resolve it:** Route A category 1 always registers the reproduced printed interval/test conflict, with rounded underlying endpoints or different inferential procedures retained as alternatives.

**Alternative source-grounded interpretations:** The upper confidence limit may be below 1 before rounding; alternatively, the interval and P value may arise from different procedures. Unrounded output, numerical standard error/test statistic and exact construction are not supplied.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** Fresh main Table 2 rendering and direct main PDF text confirm all registered HR, interval and P values and repeated locations. The category-1 exception and rounding alternative were checked without reconstructing a fitted test. Roles, S_W relationship and statistical_results domain are unchanged. Full facts are in verification/evidence_recheck.md.

**Potential downstream evidence impact:** An extractor could code different null-status readings from the printed CI and P value. No conclusion change or propagated consequence is asserted.

**Remaining human question:** What are the unrounded limits and exact test construction for the printed HR/CI/P combination?

## C003 — Original primary-power correlation assumptions differ between SAP and report

**Status:** Pending Human Adjudication.

**Candidate statement:** The active SAP's original-power lower correlation extreme 0.001 differs from the report's 0.01 lower bound beyond display precision, without an explicit mapping of the calculations.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP vs REPORT main article

**Finding IDs:** F-ST1-004

**Checker provenance:** statistics_pass_1; related S021 and S036.

**Qualifying route:** Route B.

**Classification rationale:** PLAN SAP and REPORT main article attach differing correlation inputs to the original primary sample-size rationale. The protocol corroborates the SAP side and does not create a separate plan-internal relationship.

**Classification ambiguity:** The report may describe a refined or additional sensitivity calculation; no supplied statement maps that calculation to the SAP assumptions.

**Exact source locations:**

- REPORT [main article p. 3, original sample-size rationale begins](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3).
- REPORT [main article p. 4, correlation assumptions and continuation](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- PLAN [SAP p. 13, lines 301–308](../../joi250040supp2_prod_1753124024.37799.pdf#page=13).
- PLAN [SAP p. 14, lines 309–321](../../joi250040supp2_prod_1753124024.37799.pdf#page=14).
- Corroborating PLAN [protocol p. 20, lines 651–665](../../joi250040supp1_prod_1753124024.37199.pdf#page=20).

**Source evidence:** SAP specifies exchangeable correlation, CV 0.5 and ICC 0.02 with lower/upper extremes 0.001/0.1. Main specifies within-cluster/within-period correlation 0.01–0.05, base 0.02; cluster autocorrelation 0.64–0.96, base 0.8; CV 0.5. Both passages attach the rationale to the original eight-cluster/four-period one-day target, before a separately identified post-completion calculation.

**Reported-versus-comparator:** Original-power lower correlation limit 0.01 in REPORT versus 0.001 in PLAN. Added autocorrelation is contextual and is not a standalone omission candidate.

**Reasoning procedure:** Match the original power calculation, rather than the distinct after-completion rationale; compare the printed lower correlation inputs using their half-unit intervals. Do not assume a power algorithm or covariance construction.

**Calculation:** PLAN 0.001 → [0.0005,0.0015]; REPORT 0.01 → [0.005,0.015]. Gap 0.0035; relative discrepancy 0.0035/0.01=0.35 > 0.05. Upper 0.1 → [0.05,0.15] and upper 0.05 → [0.045,0.055] overlap, so the upper comparison alone is screened by precision.

**Affected result or extracted value:** Correlation sensitivity inputs supporting the original primary one-day/80%–90% power rationale.

**Why context does not resolve it:** B1: primary-power inputs are in focus D. B2: a narrowed subset or revised covariance calculation is possible, but the supplied paragraph does not identify which specification produced the quoted original power. B3: reproduction or extraction of that rationale uses materially different lower correlation limits.

**Alternative source-grounded interpretations:** The report may summarize additional or refined sensitivity calculations inside the broader SAP settings. Exact calculator configuration, formula and alpha are not supplied; no numerical power discrepancy is claimed from their absence.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** Fresh SAP/protocol source renders and direct main PDF text confirm the lower/upper inputs and original-versus-after-completion passage placement. The lower-bound gap 0.0035 and relative discrepancy 0.35 reproduce; upper-bound intervals overlap. Roles, P_R relationship and protocol_report domain are unchanged. No actual power calculation is inferred. Full facts are in verification/evidence_recheck.md.

**Potential downstream evidence impact:** An extractor or reproducing reader could record distinct inputs for the original power rationale. No loss of actual power or change in the primary conclusion is asserted.

**Remaining human question:** Which correlation structure and sensitivity bounds produced the quoted original power, and how does the report specification relate to the active SAP?
