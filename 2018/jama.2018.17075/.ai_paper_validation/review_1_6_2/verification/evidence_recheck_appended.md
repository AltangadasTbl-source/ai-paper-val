# Exact-source evidence recheck — appended stable candidate

Runtime agent ID: `01a129e4-f611-7510-9c03-ccbe60dedc0d`. Model: `gpt-6.1-sol`; reasoning effort: high; start mode: FRESH_SPAWN. Assigned and covered stable ID: C015 only. Finding provenance: F-ST2-201; mapped relationships S410, S442, S444 and S453. Scope and mechanical-recheck contract were read. Source files, earlier audit artifacts and other agents' outputs were preserved. This part supplies mechanical evidence facts; inclusion audit remains PENDING_AUDIT and status remains Pending Human Adjudication.

## C015 — Planned adjusted key-secondary sensitivity analyses

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST2-201

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope. PLAN DOC-002 p.181 supplies an external SAP pointer as context.

**Evidence state:** reproduced

**Inclusion audit:** PENDING_AUDIT

**Classification rationale:** The final protocol's prospective adjusted-analysis specification is PLAN by its content. The prospective June SAP update and amended flowcharts are also PLAN. The main article and completed results supplement describe observed final analyses and are REPORT. The sharing statement describes this completed publication and is REPORT context. The conflict is between a PLAN promise and supplied REPORT output coverage, making the primary relationship P_R and domain protocol_report. The two report documents corroborate the same absence; they do not conflict with each other for this candidate, so S_C is not added. The update neither independently conflicts with the protocol for this issue nor supplies a second plan-internal inconsistency, so P_P is not added. No S_W comparison establishes this omission. P_R is the sole relationship and therefore satisfies precedence P_R > P_P > S_C > S_W. No registered role, primary relationship, all-relationships or domain change is needed.

**Classification ambiguity:** The complete published SAP referenced on physical p.181 is not supplied locally. Its operative contents and any subsequent narrowing of the protocol's promise cannot be established from a reference alone. This is a missing-source limitation, not evidence of a local withdrawal.

### Exact locations found and source/comparator matches

All page numbers below are physical PDF pages. The protocol's physical pp.84–85 have printed footers 32–33 of 86; the results supplement's physical pages are one above its printed appendix page numbers. The source page, including layout and adjustment-label placement, was visually confirmed from a fresh direct render for every individually cited location below.

| Exact supplied-source location | Role by content | Location found and exact relevant match | Function in comparison |
|---|---|---|---|
| [DOC-002 p.84, final V9 §15.2, binary secondary-outcome bullet](../../../joi180132supp1_prod.pdf#page=84) | PLAN | Hospital/six-month mortality and adverse events are included among binary secondary outcomes; log-binomial and identity-binomial regression estimate risk ratios and risk differences with 95% CIs. | Identifies the adverse-event outcomes within the promised secondary-analysis scope. |
| [DOC-002 p.85, §15.2 third continuing bullet](../../../joi180132supp1_prod.pdf#page=85) | PLAN | “Sensitivity analyses of the primary and secondary outcomes will be performed using regression models adjusting for pre-specified baseline covariates as well as any covariate exhibiting substantial imbalance between randomisation arms, as recommended [36].” | Direct adjusted-analysis promise, reproduced verbatim. Adjustment for prespecified covariates is unconditional; imbalance adds covariates and does not condition the entire promise. |
| [DOC-002 p.85, next continuing bullet](../../../joi180132supp1_prod.pdf#page=85) | PLAN | A separate bullet promises primary/secondary sensitivity analyses in compliant cooling patients versus controls and according to actual treatment received. | Per-protocol and as-treated analyses are a separate specification and do not themselves establish covariate adjustment. |
| [DOC-001 p.1, abstract Results](../../../jama_cooper_2018_oi_180132.pdf#page=1) | REPORT | Pneumonia 55.0% versus 51.3%; increased intracranial bleeding 18.1% versus 15.4%, hypothermia versus normothermia. | Both outcomes are key secondary under the scope's abstract-results definition. These displayed proportions match registration. |
| [DOC-001 p.3, Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=3) | REPORT | Secondary outcomes include proportions with adverse events, explicitly intracranial bleeding and pneumonia, within 10 days of randomization. | Matches outcome identity and reported window. |
| [DOC-001 p.3, Statistical Analysis, final paragraph](../../../jama_cooper_2018_oi_180132.pdf#page=3) | REPORT | Primary favorable GOSE and secondary mortality/adverse events are compared using unadjusted chi-square equal-proportion tests, with frequencies, RR/RD and 95% CIs. The following sentence describes hierarchic multivariable log-binomial sensitivity regression. | Ordinary adverse-event reporting and a general sensitivity-method description are present. |
| [DOC-001 p.4, left-column continuation](../../../jama_cooper_2018_oi_180132.pdf#page=4) | REPORT | Sensitivity regression adjusts for extended IMPACT-TBI, treating randomization strata as random effects and reporting RR with 95% CI. Right-column text says all secondary outcomes should be interpreted as exploratory because multiplicity was not adjusted. | Confirms the general adjustment description but supplies no adverse-event-specific adjusted estimate. Exploratory interpretation does not withdraw the adjusted-analysis promise. |
| [DOC-001 p.5, Primary Outcome and Adverse Events](../../../jama_cooper_2018_oi_180132.pdf#page=5) | REPORT | Primary GOSE result is similar after IMPACT-TBI adjustment; adverse-event paragraph repeats pneumonia 55.0% versus 51.3% and intracranial bleeding 18.1% versus 15.4%. | Adjustment discussion is attached to GOSE; the adverse-event paragraph provides proportions. |
| [DOC-001 p.6, bottom-left continuation](../../../jama_cooper_2018_oi_180132.pdf#page=6) | REPORT | Per-protocol pneumonia RR 1.23 (95% CI 1.04–1.47), P=.02 and as-treated pneumonia RR 1.29 (1.09–1.53), P=.003 are explicitly described as unadjusted. | Confirms that the supplementary subset pneumonia estimates do not supply the promised covariate-adjusted output. |
| [DOC-001 p.7, Table 2](../../../jama_cooper_2018_oi_180132.pdf#page=7) | REPORT | Severity-adjusted favorable-GOSE RR 0.98 (0.87–1.11), P=.75 is a separate row. Pneumonia is 143/260 versus 123/240, RR 1.07 (0.91–1.27), P=.40; intracranial bleeding is 47/260 versus 37/240. No second adjusted adverse-event output appears. | Source matches registration; the explicitly adjusted row applies to GOSE only. The distinct bleeding tuple-attribution candidate is not the basis of this absence comparison. |
| [DOC-003 p.10, eTable 6](../../../joi180132supp2_prod.pdf#page=10) | REPORT | Pneumonia 143 (55.0) versus 123 (51.3), P=.40; intracranial bleeding 47 (18.1) versus 37 (15.4), P=.43. Columns give n=260 and n=240; no adjusted companion rows. | Corresponding adverse-event report display matches the supplied counts and has no adjusted result. |
| [DOC-003 p.14, eTable 9](../../../joi180132supp2_prod.pdf#page=14) | REPORT | Separate severity-adjusted favorable-GOSE RR 1.04 (0.65–1.69), P=.86. Pneumonia 93/132 versus 92/161, RR 1.23 (1.04–1.47), P=.02; intracranial bleeding 26/132 versus 29/161, RR 1.09 (0.68–1.76), P=.71. | GOSE adjustment label is contained in its own row; no adjusted adverse-event counterpart is present. |
| [DOC-003 p.19, eTable 11](../../../joi180132supp2_prod.pdf#page=19) | REPORT | Separate severity-adjusted GOSE row is printed as “unfavorable outcome”, RR 1.11 (0.70–1.76), P=.65. Pneumonia 94/133 versus 107/196, RR 1.29 (1.09–1.53), P=.003; intracranial bleeding 26/133 versus 39/196, RR 0.98 (0.63–1.53), P=.94. | The printed adjustment label concerns GOSE and is not a column-wide adverse-event adjustment label. Registration described this generically as a GOSE output; its exact favorable/unfavorable wording does not change C015's comparison. |
| [DOC-003 p.16, per-protocol sensitivity primary-outcome paragraph](../../../joi180132supp2_prod.pdf#page=16) | REPORT | Sensitivity compliance definition is based on first 72 hours; output is primary favorable GOSE, unadjusted RR 1.00 (0.77–1.30), P=.98. | Does not supply an adjusted adverse-event estimate. |
| [DOC-003 p.20, as-treated sensitivity primary-outcome paragraph](../../../joi180132supp2_prod.pdf#page=20) | REPORT | First-72-hour compliance sensitivity output is primary favorable GOSE, unadjusted RR 1.02 (0.80–1.31), P=.85. | Does not supply an adjusted adverse-event estimate. |
| [DOC-003 p.21, missingness text and eTable 12](../../../joi180132supp2_prod.pdf#page=21) | REPORT | Worst/best-case and multiple-imputation scenarios address missing primary favorable GOSE. | Does not supply an adjusted adverse-event estimate. |
| [DOC-003 p.22, post hoc adequate-cooling analysis](../../../joi180132supp2_prod.pdf#page=22) | REPORT | Multivariable logistic regression adjusts favorable GOSE for baseline imbalance/time to randomization. | Adjusted output concerns GOSE, not pneumonia or intracranial bleeding. No C014 interval-token comparison is made here. |
| [DOC-002 p.181, published SAP reference](../../../joi180132supp1_prod.pdf#page=181) | PLAN | Supplies citation and external link to the published SAP, not its full body. | Defines the exact unavailable prospective source; no external access was undertaken. |
| [DOC-002 p.183, June 12 SAP update](../../../joi180132supp1_prod.pdf#page=183) | PLAN | Additions preceded data lock/unblinding. Main clinically relevant dose analyses are added to previously described depth analyses; subset compliance uses >48 hours at ≤35°C within 96 hours. | Prospective update context; no express withdrawal of adjusted secondary analyses is printed. |
| [DOC-002 p.184, both flowchart adjustment footnotes](../../../joi180132supp1_prod.pdf#page=184) | PLAN | Both footnotes state outcome analyses will only be adjusted for baseline extended IMPACT-TBI probability of 6-month unfavorable outcome. | Limits adjustment covariates for these subset analyses, rather than stating that adverse-event analyses will be omitted. |
| [DOC-002 p.187, amended flowcharts, both adjustment footnotes](../../../joi180132supp1_prod.pdf#page=187) | PLAN | Both repeat the extended IMPACT-TBI-only adjustment statement; header says figures are aligned with June 12 text. | Subsequent supplied amendment retains an adjustment statement and contains no explicit adverse-event-adjustment withdrawal. |
| [DOC-004 p.1, Data Sharing Statement](../../../joi180132supp3_prod.pdf#page=1) | REPORT | Describes partial data-set sharing; supporting document types are “None”. No estimates or outcome-analysis output. | Entire supplied sharing source checked; it provides no missing adjusted result. |

### Logical comparison, precision and input availability

**Consistency rule applicable:** Yes. Focus D and Route A, category 5 apply to a planned primary or key secondary analysis absent from reporting. Pneumonia and intracranial bleeding are secondary under REPORT p.3 and key secondary because both are reported in its abstract. The specific plan promise is covariate-adjusted sensitivity regression, not simply any sensitivity analysis.

**Logical comparison reproduced:** Yes, separately for both affected outcomes: (1) final PLAN p.85 expressly promises adjusted primary/secondary analyses; (2) the named adverse event is in the secondary and abstract-result scope; (3) complete supplied final REPORT coverage contains ordinary event results but no matching output identified as that adverse event's covariate-adjusted sensitivity analysis; (4) the supplied PLAN update does not explicitly withdraw the promise. Both outcomes share this rule and reporting pattern, retaining one C015.

**Display-precision interval check:** Not applicable to the registered logical discrepancy. There is no printed adjusted adverse-event estimate to compare with a recomputed value; therefore neither a recomputed numeric interval nor a relative numeric discrepancy can be formed. The observed absence cannot be reconciled by half-unit intervals. Counts/proportions are transcription and outcome-identity matches only. No model-based result is compared with a crude recomputation and no adjusted estimate is reconstructed.

**Necessary inputs available:** Yes for the presence/analysis-identity comparison: exact plan wording, report outcome identity, abstract key-secondary basis, analysis descriptions, all supplied final report pages, and local SAP updates. They are sufficient to reproduce this supplied-package discrepancy.

**Exact missing inputs or definitions:** Full published SAP body referenced at DOC-002 p.181; any operative withdrawal or narrowing of adjusted-secondary analyses not printed in the supplied updates; exact prespecified adverse-event covariate set; fitted adjusted pneumonia/intracranial-bleeding estimates, CIs and reporting locations. Participant-level data and fitted-model details are unnecessary for establishing absence and are not used.

**Full absence check:** DOC-001 pp.1–10, DOC-003 pp.1–24 and DOC-004 p.1 were independently read through fresh direct Poppler layout extraction, including contents, all tables, figures' titles/captions, footnotes, methods and supplementary sensitivity/post hoc text. Complete occurrence searches covered adjustment, sensitivity, pneumonia and bleeding. Every candidate-supporting positive source/comparator location was then confirmed from fresh exact-page renders, including adjustment-label boundaries. Remaining report pages concern baseline data, flow, temperature/pressure, mortality/survival, primary GOSE, references or publication details. No matching adjusted adverse-event output was located. This conclusion is limited to the supplied final REPORT materials and does not assert absence from publications or sources outside the package.

### Alternatives, observation and remaining question

**Source-grounded alternative interpretation:** REPORT pp.3–4's general adjustment sentence may intend only primary GOSE, supported by the explicit GOSE adjustment discussion/row on pp.5/7. That interpretation explains the observed output scope but does not reconcile it with final PLAN p.85's broader secondary-outcome promise. A later complete SAP could have narrowed that promise, or outputs could exist in an unsupplied publication. The p.181 pointer and June update establish why those possibilities must remain named; the supplied pages do not establish either. Treating secondary results as exploratory on REPORT p.4 is a multiplicity interpretation and is not an explicit withdrawal. Implementing the separate per-protocol/as-treated bullet on PLAN p.85 is not evidence that covariate adjustment for these two adverse events was reported.

**Direct observation versus inferred explanation:** Direct observations are the explicit prospective adjustment promise, the abstract/report secondary-outcome identities, the ordinary reported adverse-event output, the GOSE-specific adjustment labels, the unadjusted subset pneumonia wording, and absence of matched adjusted outputs across the supplied final report pages. No reason for the omission, actual model-fitting decision, covariate impact, clinical consequence or analysis outside the supplied package is inferred.

**Recheck fact determining evidence state:** Exact PLAN p.85 retains the unconditional baseline-covariate adjustment promise for secondary outcomes; both named abstract adverse events meet key-secondary scope; every supplied final REPORT source lacks a matched adjusted output. The registered logical discrepancy therefore remains, with no transcribed value or location needing alteration: reproduced.

**Exact remaining human question:** Where are the prespecified covariate-adjusted sensitivity outputs for pneumonia and new/increased intracranial bleeding reported, or which supplied operative amendment narrowed or withdrew final protocol §15.2's adjusted-secondary-analysis specification?

## Final classification table for assigned appended ID

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C015 | protocol_report | P_R | P_R | PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope | reproduced | PENDING_AUDIT | F-ST2-201 |

## Derivative provenance

Engine: direct Poppler `pdftotext` and `pdftoppm` 25.03.0. Compute device: CPU, as recorded in tooling_record.md. No OCR, fallback environment, GPU or external source was used. All new derivatives are confined to `review_1_6_2/preprocessing/` and have the unique `recheck2-` prefix. Extraction text was used as a locator and transcription aid; the source remains authority.

Commands executed from the package root:

```bash
pdftotext -layout jama_cooper_2018_oi_180132.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-complete.txt
pdftotext -layout joi180132supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-complete.txt
pdftotext -layout -f 84 -l 86 joi180132supp1_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-84-86.txt
pdftotext -layout joi180132supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck2-sharing-complete.txt
```

Fresh renders used `pdftoppm -f N -l N -scale-to 1800 -singlefile -png SOURCE OUTPUT_PREFIX` for PLAN pages 84,85,181,183,184,187; main REPORT pages 1,3,4,5,6,7; results REPORT pages 10,14,16,19,20,21,22. Output prefixes are exactly `preprocessing/recheck2-plan-N`, `preprocessing/recheck2-main-N`, or `preprocessing/recheck2-results-N` beneath the review root. Sharing p.1 used the same command with `-scale-to 1400` and prefix `preprocessing/recheck2-sharing-1`.

SHA-256 values for all newly produced derivatives follow:

```text
c49a9d57cdf257bc5d4cacfc77fb68cb5cbd1693387e3d5d266d6da19ea69bdf  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-1.png
0398a1e95c4fb14483e6853b95596d4127a3ab24c4d6d7895ecee79fad1b8e62  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-3.png
05707ef99cf43c3a0112517d75232bd93430e723709a7d9a5eae3c199d2427d6  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-4.png
3d1f18f93a240c1bba1387acfb3af26b524566eab18ab56d757f98769fe9a01c  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-5.png
fa1c9272acf0e925d766f6e50461e4416eea6ce256ef466faf08717922b8b545  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-6.png
59eb589b70679a45683a1244dfd740d19a0ed2d64acc4bc580217095c2b6dd7d  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-7.png
867457d9166b3f1178904b57b1a750a11cbd8388b2130a8cf20543ca998d39fe  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-main-complete.txt
e81cd7789db71aec1ae650753cef1d2ebccb249c5fad3c30a9f12aeb644a41f6  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-181.png
548ccdbbba8ae0a85c5564cd308001387813afd48c1bc076d2cb0d791cc5e49b  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-183.png
de295f4e121b1a8f3d404aeef91bfde85aacfc8e40225b653f8e0dd76a0979d5  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-184.png
f8bcfded1187036240452fd43cf394b257427a421ce64a9cf3a68d31ab45b5fe  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-187.png
f9a0e592a9ba8fa197f8c5589e46a869131eb93a0b201ab11dfd6a975f77b254  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-84-86.txt
f155dc7a97636aa66ec863609e2d590e8b9631bfc53a178a51de7691db3ff3f7  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-84.png
df2470f3da24ef446e4af85607bac824834d061b149504d34c49957c7ee2fa85  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-plan-85.png
8c00b43743c68bb74d67fec998123b79869d9547581baa0fda8a4995e94d72d0  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-10.png
7f4ae648dfb3b6172380b672aad9a6e97643cf709052b625a47eb8232ec6761e  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-14.png
0625a3abcce2abd513d9c559b4ecf006ac8120c883296bb9a9dd83673383dadd  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-16.png
5357bcfad2a44fdba6b0b5a852a1f7dfd427937c50b747d91827f0939bf21e14  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-19.png
8f66d54913d0cf100a4ca1e841b6f044063aa30b99a8fe4bce66db52e77a20ad  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-20.png
2c5113fef7211df863d1e9416487535e4472e9a9dae216e4497d6b2221b1ca1d  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-21.png
952ea77dbbdf3f9c0ba285bbfe77ca0e21977f3a02a5a2d8d779c72377d2e120  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-22.png
03284febe6698e62ae2d047a11b48b7431fa9532a3ad72c60fed1bb8c8cb7609  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-results-complete.txt
a46deac6de242c92c19514853b5caa02ecd4be4a5e632b18f0b47fe5688fce85  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-sharing-1.png
687915b05fc55301caa855fed573571a59c4c85d06047c0ba0f7387a9332c2c7  .ai_paper_validation/review_1_6_2/preprocessing/recheck2-sharing-complete.txt
```

Covered IDs: C015. Count: 1 complete recheck; evidence-state count reproduced=1. Unresolved inputs are the external full SAP, any operative narrowing/withdrawal and missing adjusted-output locations stated above; no assigned source location remains unconfirmed. Artifact: `verification/evidence_recheck_appended.md`.
