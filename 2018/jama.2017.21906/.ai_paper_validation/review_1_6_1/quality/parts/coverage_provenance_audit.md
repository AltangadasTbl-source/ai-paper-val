# Coverage and provenance quality audit

Audit runtime: `/root/audit_coverage`, fresh `gpt-6.1-sol` with high reasoning effort. Scope: all direct-source units, reusable/fresh-required partition, mapping coverage, numeric and statistical inventory completeness, both statistical passes, coverage artifacts, routing, tooling, execution identity, integrity and source-link pagination. Candidate inclusion, screening decisions and checker exclusions belong to the disjoint candidate/screening audit; this part assigns no candidate judgment or scientific disposition. Audit snapshot UTC: 2026-10-11T03:24:22Z.

## Coverage result

Scientific coverage is complete: four direct PDFs, 80 unique physical pages, 79 reusable-backed units plus one fresh-required unit, and 80 mapped units. Every direct-source row closes both arithmetic requirements. The main and support page ledgers have disjoint, complete source assignments; administrative pages and pages without applicable new results remain explicitly accounted for.

| Direct source | Content role | Total | Reusable | Fresh-required | Mapped | Audit result |
|---|---|---:|---:|---:|---:|---|
| DOC-001, jama_huffman_2018_oi_170166.pdf | REPORT, all pages | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002, joi170166supp1_prod.pdf | PLAN, all pages | 32 | 31 | 1 | 32 | COMPLETE |
| DOC-003, joi170166supp2_prod.pdf | PLAN, all pages | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004, joi170166supp3_prod.pdf | REPORT p. 1 and pp. 17–27; PLAN pp. 2–16 | 27 | 27 | 0 | 27 | COMPLETE |
| Total unique units | Page-specific roles retained | 80 | 79 | 1 | 80 | COMPLETE |

The direct package inventory was independently enumerated with `rg --files` for PDF, DOC, DOCX, XLS, XLSX and CSV extensions, excluding workflow/generated derivatives. Only these four direct PDFs were found. Direct `pdfinfo` reconfirmed 12, 32, 9 and 27 physical pages respectively. The source inventory distinguishes prospective protocol/SAP/operational material from report results by content. In particular, the sample toolkit and blank checklists on DOC-004 pp. 2–16 are PLAN; their demonstration values are not trial outcomes. Mixed document content is resolved at the compared page rather than inferred from a supplement filename.

The main page ledger contains each physical page 1–12 once. The support ledger contains each DOC-002 page 1–32, DOC-003 page 1–9 and DOC-004 page 1–27 once. Main table coverage retains all 27 Table 1 rows, 21 Table 2 rows and 10 Table 3 rows, all 20 participant-flow boxes, all 14 Figure 3 subgroup rows, and all 60 Figure 2 cohort/step/outcome points and intervals. Support coverage retains all 17 rows in each baseline eTable 1–4, all 40 eTable 5 outcome/model tuples, 10 eTable 6 tuples, 16 eTable 7 effect/interval tuples, and complete graphical displays on pp. 24–27. Source-linked narrative, caption, eligibility, model, direction, time and decision-rule definitions are included in the maps and family inventories.

DOC-002 p. 14 is a closed fresh-required unit. The missing embedded Time and Events diagram was directly rendered by the support mapper using Poppler `pdftoppm` 25.03.0 at 150 dpi. This auditor opened `preprocessing/support-DOC-002-14.png` and confirmed the diagram and its Presentation Date, Discharge Date and Discharge Date + 30 Days labels. The fresh diagram is represented in SUP-P04/S403 and its page inspection ledger. It is not counted as a reused artifact. The revised source-coverage row governs the earlier initial curation count.

## Complete relationship-unit accounting

Mechanical checks processed every individual numeric and statistical inventory row, including its ID, available exact-location metadata or enclosing source/table location, printed-evidence cells, comparison/check cells and applicable completion markers. No uniform table schema was imposed on the differently structured shards: some exact source links are supplied by the immediately enclosing table definition, and the graphical tables have additional columns. There are no blank populated-row cells or duplicated relationship IDs. Every row has source-location support in its row or enclosing source/table definition.

| Relationship scope | Registered rows | Durable completeness evidence |
|---|---:|---|
| Main numeric N001–N100 | 100 | relationships/parts/numeric_main_a.md |
| Main numeric N101–N189 | 89 | relationships/parts/numeric_main_b.md |
| Support numeric N190–N298 | 109 | relationships/parts/numeric_support.md |
| All numeric relationships | 298 | relationships/numeric_relationship_inventory.md |
| Main statistical/model S001–S094 and PLAN S400–S417 | 112 | Both main-A statistical inventory parts |
| Main graphical S095–S154 | 60 | Both main-B statistical inventory parts |
| Support baseline/graph/method S155–S237 | 83 | Both support statistical inventory parts |
| Support outcome/method S320–S388 | 69 | Both support-outcome statistical inventory parts |
| All statistical relationships | 324 | statistics/relationship_inventory.md |

The canonical numeric ID set equals the disjoint union of all three numeric parts: 298 rows, 298 unique IDs. The canonical statistical ID set equals each pass's disjoint union of four parts: 324 rows, 324 unique IDs. Every canonical S row contains both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. Pass 1 parts carry 112 + 60 + 83 + 69 = 324 completion records. Pass 2 parts preserve those 324 pass-1 records and add 324 pass-2 records. The explicitly enumerated S scopes in `coverage_manifest.md` equal the complete statistical inventory for both stages, with no missing or additional ID. Intentional gaps between reserved support/PLAN ID blocks are not missing relationships.

All 60 main Figure 2 graphical point/interval relationships receive separate statistical keys, matched to N113–N172. The support baseline interval scope includes all 17 eTable 1 differences and all 51 eTable 2 control/intervention/difference tuples. The 34 arm-marginal intervals omitted from the support mapper's initial inferential-tuple summary were included in the complete checking inventory, so the final support printed-tuple count is 68 baseline tuples plus 66 outcome tuples = 134. This expansion is evidence-completeness repair, not a selection boundary. The 83-row baseline/graph/method statistical shard comprises 68 printed tuples plus 15 graph/method relationships. The 69-row outcome shard comprises 66 tuples plus three associated method relationships. Eighteen PLAN families receive S400–S417 coverage, including power, population, missingness, primary model, subgroup specification, interim boundaries and prospective intervention definitions.

Graphical readings remain explicitly approximate; no exact unprinted coordinates, event counts or statistical tests are substituted. Missing test construction, covariance/variance, regression contributor counts, interaction coding, missing-outcome/imputation details and stepped-wedge power inputs remain named limitations. Those limitations constrain reproducibility without creating omitted scientific units.

## Artifact and execution accounting

The coverage manifest has 43 data rows at this snapshot. Every Artifact cell contains exactly one plain POSIX relative path, without combined paths, link decoration or prose. All 39 completed rows resolve to existing artifacts. The two assigned quality parts and the planned canonical audit/report paths were legitimately pending their production at this snapshot; this part supplies one of those paths. Each scientific shard part is listed separately and its relationship ID set is represented in the corresponding canonical inventory/checker artifact. Candidate-stage canonical scopes enumerate C001 and C002; the auxiliary coverage audit row expressly has no independent candidate assignment.

The execution manifest contains 20 distinct entries: one current coordinator, seven ordinary medium-effort specialists, and twelve high-effort statistical/screening/recheck/audit specialists. Every entry uses the exact model ID `gpt-6.1-sol`. Every specialist is recorded `FRESH_SPAWN`; the coordinator appears once as `CURRENT_SESSION`. No duplicate runtime identity or role-effort discrepancy was found. Artifact runtime declarations and the available live/completed-agent listing agree with the manifest after normalization of the leading canonical slash.

| Mandatory execution requirement | Audit evidence |
|---|---|
| Fresh statistical pass 1 | `/root/statistics_1_main_a`, gpt-6.1-sol/high; distinct fresh main-B, support and outcome shard agents |
| Different fresh statistical pass 2 | `/root/statistics_2_main_a`, gpt-6.1-sol/high; distinct fresh main-B, support and outcome shard agents |
| Independent fresh inclusion screener | `/root/screen_initial`, gpt-6.1-sol/high, distinct from checker, mapper, recheck and audit identities |
| Fresh mechanical recheck | `/root/recheck_initial`, gpt-6.1-sol/high |
| Fresh final audits | `/root/audit_candidates` and `/root/audit_coverage`, gpt-6.1-sol/high, disjoint scopes |
| Conditional pass-2 screener | Not applicable: completed pass 2 emitted no new findings |
| Fresh report generator | Future required stage; must be recorded once when spawned |

Routing preflight reports PASS, coordinator inference PASS, `INTERACTIVE_CLI`, `CURRENT_SESSION`, and all ten named presets. Read-only checks of package `.codex/config.toml` and all ten `.codex/agents/*.toml` reconfirmed the fixed coordinator/high, ordinary/medium and statistical/screening/recheck/audit/high pairs. No moving model alias or provider configuration was introduced in the reviewed artifacts. The recorded first mandatory curator inference passed before mapping.

## Integrity, links and neutral wording

Read-only `sha256sum -c` checks returned OK for all four direct sources and all 77 reused assets. All native/layout, OCR, page image and metadata assets remain unchanged. The newer targeted diagram/SAP/screening renders have separate current-run provenance and do not alter the reused hash list. Hash-before records and source identities match the current files.

A shell check visited every PDF evidence-link occurrence in current review Markdown: 1329 occurrences at this snapshot, zero unresolved paths, and zero page numbers outside their direct source's physical page range. Relative traversal was resolved from each artifact's actual directory. The source mapping and fresh diagram use truthful physical PDF locations. No Office pagination is asserted for this PDF-only package.

The direct tooling probe and recorded versions agree: PDF information/text/rendering and hashing are available; CPU OCR and Office conversion are absent; Pandoc is available. Existing source-matched OCR plus visual inspection supplies scanned-page coverage. No fallback environment was created, so `NOT_NEEDED` and `NOT_CREATED` are supported. No additional OCR, GPU or web operation was performed for this audit. No unapproved Python helper was used.

A case-insensitive whole-word scan of generated review Markdown found only established statistical terminology and quoted source caption terms among the restricted vocabulary, such as standard error and error bars. The audited coverage, provenance and relationship narratives use neutral quality-control wording without a scientific disposition. Candidate-specific human blank fields, conclusion impact, downstream bounds and inclusion judgments are audited by the separate candidate/screening part.

The maps and checker provenance consistently state reconstruction from source-linked evidence rather than earlier review conclusions. Complete independent page ledgers, newly mapped diagram coverage, full relationship inventories, expansion to include all arm-marginal intervals, and complete second-pass scopes support that recorded discovery boundary. No count target, top-N rule, old candidate list, cross-paper calibration or early finding stop is present in the reviewed discovery/coverage instructions or artifacts. The package-specific 22–35 minute target is an elapsed-time planning range; it is not a candidate target or scientific scope boundary. This artifact audit cannot independently reconstruct unrecorded runtime actions, and does not claim to do so.

## Repair record and remaining closure

| Repair or closure item | Concrete reason | Audit status |
|---|---|---|
| Existing mapping repair: DOC-002 p. 14 fresh-required reclassification | Embedded diagram absent from reusable text; source unit requires direct visual mapping | Closed in source coverage, mapper evidence and fresh render |
| Existing relationship repair: 34 eTable 2 arm-marginal intervals | Initial support tuple summary counted differences but not both arm intervals | Closed in both full statistical passes and canonical inventory |
| New coverage/provenance repair requested by this auditor | None: audited scientific unit, relationship, hash and execution scopes reconcile | No additional scientific repair |
| Final audit merge and coverage statuses | Assigned parts must be merged into the canonical audit, retaining every stable C ID | Coordinator closure required after both parts finish |
| Report generation, timing and final checks | Report generator stage has not yet occurred; Finished UTC/performance fields are PENDING | Future required closure, not represented as complete |

Before final completion, the coordinator must add the fresh report-generator manifest entry, complete the report and canonical audit, mark their coverage rows COMPLETE, finalize timing after Markdown assembly, recompute final source/reused hashes, render standalone HTML, and obtain the final validator PASS. Any elapsed-time exceedance must be recorded with bounded causes. This snapshot does not claim the future report, final timing, final hash-after records, rendering or validator result already exists.

Covered stable IDs for coordination: C001 and C002 are the complete current stable ledger scope and belong to the companion candidate-inclusion audit; this part contains no C heading and no competing inclusion assessment. Scientific-coverage limitations: no omitted source or relationship units; exact unprinted graphical/test/model inputs remain bounded as above.
