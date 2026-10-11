# Coverage and execution audit part — Workflow 1.6.2

Fresh audit runtime: `root/quality_coverage_audit`, gpt-6.1-sol/high, FRESH_SPAWN. This disjoint part audits source coverage, quantitative maps, relationship coverage, reuse fitness and integrity, routing, tooling, and process records. Candidate inclusion, classification, evidence-card support, every screening decision and every checker excluded observation are assigned to `quality/parts/inclusion_classification_audit.md`; this part makes no candidate inclusion decision. The coordinator must merge both parts into `quality/evidence_quality_audit.md` without losing any stable ID.

## Coverage result

Scientific source and relationship coverage is complete. Recursive source enumeration finds exactly four supplied PDFs and no Office, workbook or CSV source. Direct `pdfinfo` independently confirms the page counts. Explicit page applicability ledgers cover every unit, including administrative and bibliography pages; these pages have a recorded applicability decision rather than an omitted mapping assignment.

| Source | Role by content | Total | Reusable | Fresh-required | Mapped | Audit result |
|---|---|---:|---:|---:|---:|---|
| DOC-001, jama_flint_2019_oi_190079.pdf | REPORT: trial article | 10 | 10 | 0 | 10 | Complete pp. 1–10 |
| DOC-002, joi190079supp1_prod.pdf | PLAN: protocol, analytic plan and pharmacotherapy appendix | 42 | 42 | 0 | 42 | Complete pp. 1–21 and disjoint pp. 22–42 |
| DOC-003, joi190079supp2_prod.pdf | REPORT: results supplement | 10 | 10 | 0 | 10 | Contents page and all nine plot pages |
| DOC-004, joi190079supp3_prod.pdf | REPORT: non-plan data-sharing statement | 1 | 1 | 0 | 1 | Administrative applicability recorded |
| Total | Four direct sources | 63 | 63 | 0 | 63 | All partitions and mapped totals close |

For each source, reusable plus fresh-required units equal total units, and mapped units equal total units. Zero fresh-required units reflects usable source-matched existing assets; every page nevertheless received fresh scientific relationship mapping. Sparse plot text is backed by complete source-matched images. Missing reusable page images elsewhere are derivative gaps closed by usable text and targeted exact-source renders, without a scientific gap.

Main mapping covers all five article tables, both figures, abstract, Key Points, narrative, captions and footnotes. The complete records retain all Table 4 arm rows, all four Table 5 contrasts, participant-flow arithmetic, risk-set sequences and outcome-specific units. Support mapping covers the complete plan schedule and footnotes, six survival-power rows, six repeated-measure-power rows, historical Table 5, the complete blinded-switch table, outcome hierarchy, analysis population, model/covariate and missingness specifications, all appendix pages, all nine result plots and the administrative data statement. Historical quantities and bibliography identifiers are identified by their actual content and are kept distinct from this trial's results.

## Relationship closure

| Relationship scope | Mapped records | Inventory records | Completion result |
|---|---:|---:|---|
| N001–N079, main article | 79 | 79 | Every ID has a numeric check record |
| N111–N132, plan core | 22 | 22 | Every ID has a numeric check record |
| N211–N236, plan appendix | 26 | 26 | Every ID has a numeric check record |
| All numeric relationships | 127 | 127 | Exact set agreement; no duplicate, missing or extra ID |
| S001–S039, main article | 39 | 39 | Both statistical passes complete |
| S040–S057, plan core | 18 | 18 | Both statistical passes complete |
| S058–S066, nine result plots | 9 | 9 | Both statistical passes complete |
| S081–S084, plan appendix | 4 | 4 | Both statistical passes complete |
| All statistical relationships | 70 | 70 | Exact set agreement; no duplicate, missing or extra ID |

Each statistical checker has exactly 70 per-ID completion rows. Their ID sets equal the inventory set, and every canonical inventory row records both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The gaps between allocated ID blocks preserve disjoint mapper assignments and do not represent missing registered relationships. Table 4 numeric inputs are cross-referenced to S017–S032; all four Table 5 inferential contrasts are explicitly covered under S038 rather than omitted because they lack separate S IDs.

The cross-source comparison coverage includes population, phase, time, contrast, model, scale and precision matching; primary abstract/body/flow agreement; all eight metabolic model results and their supplementary plots; raw within-arm versus model-estimated distinctions; eligibility, relapse composite, intervention, covariates, power, missingness and planned analysis comparisons; and historical or administrative applicability. Both statistical passes cover the complete registered relationship set rather than only findings or stable candidates. Candidate-specific interpretations and excluded-observation decisions are audited in the other assigned part.

## Reuse, preservation and reproducibility

The asset inventory contains 194 distinct paths: 171 USABLE, 22 PARTIAL and one DUPLICATE. Every listed path occurs exactly once in `reused_artifact_hashes_before.sha256`, and every hashed reused path occurs in the inventory. USABLE assets independently span DOC-001 pp. 1–10, DOC-002 pp. 1–42, DOC-003 pp. 1–10 and DOC-004 p. 1. PARTIAL plot text is paired with USABLE images; the single duplicate does not inflate page coverage. No STALE or UNREADABLE asset is recorded. Potentially mixed legacy response wrappers are inventoried by path only and were not reused as scientific conclusions. Legacy scope restrictions do not control source coverage.

Local `sha256sum -c` checks reproduce all four direct-source hashes and all 194 reused-asset hashes without a mismatch. This is an audit-time preservation check; the coordinator must still produce final after-hash manifests at completion. New derivatives remain separate from reused assets. Engine provenance distinguishes historical PyMuPDF/OCR assets from current direct Poppler CPU derivatives. Unspecified historical image engines remain documented and do not replace supplied-source authority.

Mechanical inspection of 139 PDF evidence links in the canonical maps, numeric/statistical inventories and cross-source checker resolves each relative filename to one of the four supplied PDFs and confirms that every `#page=N` is within its actual page count. No Office source is assigned fictitious pagination. Numeric records supply count/denominator arithmetic and half-unit precision intervals; statistical diagnostics state their inputs and limits. Model-based estimates, marginal summaries, paired changes, survival curves and crude ratios retain their distinct quantities. Named unavailable inputs are not invented to claim exact test or model recreation.

## Execution and discovery controls

Routing preflight is PASS, with run model gpt-6.1-sol, source DEFAULT, coordinator/high, ordinary specialists/medium, statistical and screening/recheck/audit specialists/high, Coordinator inference PASS, INTERACTIVE_CLI and Provider CURRENT_SESSION. Direct inspection confirms the project coordinator pair and all ten named agent-preset pairs. No moving model alias or provider change is recorded.

The current execution manifest contains the coordinator exactly once and 13 distinct specialist runtime IDs, including every optional shard already invoked. All specialist rows record FRESH_SPAWN and the required model/effort class. Available collaboration-service records agree with the canonical task-name IDs for the current audit, statistical pass 2, screen and recheck agents. Earlier completed stages retain their recorded runtime provenance; the service exposes canonical task names rather than a separate UUID in this session.

Statistical pass 1 is `root/statistics_pass_one`; statistical pass 2 is `root/statistics_pass_two`. Both are distinct fresh gpt-6.1-sol/high agents and differ from `root/initial_inclusion_screen`, the fresh high-effort inclusion screener. Pass 2 was performed after the full ledger, screening and mechanical recheck existed. It records no new finding, so a pass-2 inclusion-screener stage is not applicable. Both audit shards are additional fresh high-effort agents. The report generator is a later dependent stage and must be added when it is spawned.

The scientific maps and inventories document complete discovery from supplied-source evidence and eligible locators, excluding old scientific conclusions. The pre-mapping manifest defines full source coverage; relationship inventories are exhaustive and disjoint. No discovery or screening count target, top-N selection, candidate cap, comparison with other papers or calibration to earlier candidate sets is evidenced. The 25–40 minute value in `run_state.md` is solely a package-specific elapsed-time planning range, with a bounded basis covering reuse, plots, plan/report matching and mandatory agent waves; it is not a finding target or early-stopping rule.

All 26 coverage rows have exactly one undecorated relative artifact path. The 22 completed upstream rows resolve to existing artifacts. Candidate registration and recheck enumerate C001, C002, C003, C004 and C005; both statistical passes enumerate all 70 S IDs. At this audit checkpoint, the two current audit rows are ASSIGNED, the canonical audit is PENDING_MERGE and report generation is PLANNED. These sequentially dependent rows must be closed by the coordinator after their artifacts exist; they are not source or relationship coverage gaps.

Tooling records CPU, all needed direct tools available, fallback NOT_NEEDED and removal NOT_CREATED. No fallback environment exists. Current artifacts document no new OCR or GPU processing. Historical GPU provenance is explicitly historical. No source or reused artifact was modified by this audit, and no web or external literature was used.

## Repairs and completion conditions

| Repair | Reason | Status |
|---|---|---|
| Support handoff statistical block changed from S031–S066 to S040–S066, retaining 27 records | The former text overlapped main IDs and disagreed with the complete final routed set | Coordinator repair confirmed in part and canonical map |
| Numeric support provenance now calls >2/>21 historical pre-correction map readings and identifies the current ≥2/≥21 annotation | Present-tense wording no longer matched the source-confirmed current map; literal extraction and reused assets remain preserved | Coordinator repair confirmed in canonical inventory and assigned support artifacts |
| Execution-manifest blank line removed before statistical pass 2 | All runtime rows must remain in one contiguous Markdown table | Coordinator repair confirmed |
| Appendix page-render filename aligned to p41.png | The new-derivative inventory named page41.png while the mapper and actual output name p41.png | Coordinator repair confirmed in the evidence-asset inventory |

No scientific source-unit or relationship repair is required. No candidate registration or screening repair originates from this coverage part. Final report assembly, report-card/ledger agreement, canonical audit merge, inclusion-audit values, timing finalization, after-hash manifests, standalone HTML and the final validator remain dependent completion checks. A report-generator runtime and its completed coverage row must be present before final completion. Update the two audit-part rows and canonical merge row only after their durable outputs are complete.

Reconstruction limits are supplied-source limits: exact plot coordinates and shaded-band definitions; paired participant data and some Table 4 baseline contributor cells; survival event/censor times and fitted-model outputs; mixed/Poisson covariance, degrees of freedom, link/back-transformation and exact contrasts; full simulation generators and replication counts; operational endpoint/treatment/observation coding; unreported analysis outputs and undisclosed amendments. These limits are bounded, named in the evidence artifacts and leave no source unit unreviewed. No severity or scientific disposition is assigned. All stable candidates remain Pending Human Adjudication.

Neutral-language scan of all current generated Markdown artifacts found none of the prohibited descriptive terms. Candidate-card inclusion, impact wording and repeated-pattern support remain covered by the independent inclusion/classification audit part and must be preserved in the canonical merge.
