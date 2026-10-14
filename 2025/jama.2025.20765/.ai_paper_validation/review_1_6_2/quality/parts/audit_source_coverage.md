# Source coverage and evidence-asset quality audit

Audit runtime: 01a12c70-fcf0-7223-bf50-7ba7d37585a9. Model: gpt-6.1-sol. Reasoning effort: high. Stage: fresh quality-control auditor, source-coverage shard. Audit snapshot: 2026-10-11T19:30:56Z, with execution-manifest refresh immediately afterward. Ownership is limited to this artifact. The coordinator merges this part into the canonical quality artifact and performs any repairs to other records.

## Scope and audit result

Direct-source scientific coverage is COMPLETE: all 134 unique PDF pages have a current-run mapping row. All three direct-source rows satisfy reusable units plus fresh-required units equals total units, and mapped units equals total units. The package contains exactly three supplied PDFs and no supplied Office, workbook, or CSV source. Dependency sample files in the fallback environment are not supplied scientific sources.

The audit read the complete main quantitative map and the complete support quantitative map, the normative scope, source inventory, source coverage ledger, asset-fitness handoff, all coverage-manifest rows, execution manifest, routing preflight, tooling record, and new-derivative provenance. It independently checked source page counts, nonempty PLAN image locators, source and reusable-asset hashes, page-row uniqueness and closure, artifact existence, and mapping evidence-link paths/page ranges. Candidate inclusion, screening decisions, and the detailed numerical/statistical inventories are covered by the other assigned audit parts. This part introduces zero new scientific findings and requests no screening addition.

## Direct-source closure

| Source ID | Supplied source path | Role by content | Total pages independently confirmed | Reusable pages | Fresh-required pages | Current mapped pages | Coverage result |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | REPORT: published trial article and results | 9 | 9 | 0 | 9 | COMPLETE; 9 + 0 = 9 and 9 mapped |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PLAN: protocol versions, change statement, SAP, prospective SMS materials | 109 | 109 | 0 | 109 | COMPLETE; 109 + 0 = 109 and 109 mapped |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | REPORT: non-plan results supplement | 16 | 16 | 0 | 16 | COMPLETE; 16 + 0 = 16 and 16 mapped |

The independent page-count commands used the permitted bundled `workflow_1_6_2/scripts/pdf_tools.py info` helper with the package-local fallback interpreter. The helper reports engine `pymupdf`; the recorded pinned environment uses PyMuPDF 1.26.4. All three PDFs are unencrypted. Direct `file` independently identifies all three as PDFs and reports nine pages for DOC-001. These checks agree with `source_inventory.md` and `source_coverage.md`.

Fresh-required equals zero because usable reusable extraction or readable rendered images cover every source unit. This quantity describes the extraction burden. It does not replace a fresh scientific review: the fresh mapping agents reviewed every unit. No garbled PLAN text is credited as usable text coverage.

## Page mapping and applicability

| Mapping assignment | Exact direct-source scope | Page-row audit | Durable artifact, relative to review directory | Result |
|---|---|---|---|---|
| Main mapping | DOC-001 PDF pp. 1–9 | Nine unique rows, one for every page; p. 9 explicitly records references with no applicable trial quantitative relationship | extraction/main_quantitative_evidence.md | COMPLETE |
| Support shard 001 | DOC-002 PDF pp. 1–32 | 32 page rows; every page visually inspected from readable locators; clipped p. 13 branch confirmed by new source rendering | extraction/parts/support_plan_001.md | COMPLETE |
| Support shard 002 | DOC-002 PDF pp. 33–64 | 32 page rows; administrative/reference pages explicitly mapped; version boundary and PDF versus printed numbering retained | extraction/parts/support_plan_002.md | COMPLETE |
| Support shard 003 | DOC-002 PDF pp. 65–96 | 32 page rows; protocol continuation, changes, SAP and blank templates mapped; p. 87 fragment explicitly recorded | extraction/parts/support_plan_003.md | COMPLETE |
| Support shard 004 | DOC-002 PDF pp. 97–109 and DOC-003 PDF pp. 1–16 | 29 page rows, comprising 13 PLAN and 16 REPORT pages; all table and figure pages and front matter mapped | extraction/parts/support_plan_004_results.md | COMPLETE |
| Merged support mapping | Disjoint union of support shards | 125 page rows and 125 unique source-page keys; every PLAN p. 1–109 and every results-supplement p. 1–16 occurs exactly once | extraction/support_quantitative_evidence.md | COMPLETE |

The main map retains the participant flow, all baseline-table cells, all eleven outcome-table rows and inferential columns, all 27 Figure 2 clusters with printed follow-up counts and explicitly approximate graphical quantities, all eleven adverse-event narrative pairs, abstract/Key Points results, outcome definitions, and analysis descriptions. It distinguishes background numbers from trial results and graphical approximations from exact printed estimates. The current-run Table 2 transcription update is explicitly attributed to source recheck; it does not select a candidate.

The support map retains all protocol/SAP design and analysis specifications, parallel version statements, sample-size inputs and printed arithmetic, outcome definitions/status, intervention dose and schedules, missing-data and population specifications, blank analysis templates, and all results-supplement cells. Plan images are the transcription authority for the garbled native text. DOC-003 pp. 1–2 use the later whole-document layout locator and are explicitly mapped; pp. 3–16 were checked against rendered images. Blank templates, front matter, administrative pages, and references remain mapped units even when no applicable statistical relationship is present.

The locator transcription on DOC-003 p. 12 retains a native-text reading of `>6`, while the immediately preceding explicit image-based correction states the authoritative reading is `≥6`. This is a preserved locator plus a governing correction, not an unmapped source unit. Any extracted scientific value must use that source-image correction. Similarly, the invisible continuation below the original DOC-002 p. 13 boundary is not inferred. That supplied-source limitation does not prevent mapping the visible page.

The maps give 134 local PDF evidence links. All resolve to the supplied files and end in `#page=N` with N within the independently confirmed page count. Main-map page labels agree with their PDF page anchors. Support mapping differentiates absolute PDF pagination from local protocol/SAP pagination. The original support shard uses the additional parent-directory traversal needed for its deeper `extraction/parts/` location; merged-map links use the corresponding shallower path.

## Reusable-asset fitness and integrity

The asset-fitness handoff identifies 386 reused source-linked extraction, metadata, and image artifacts. The audit did not use historical candidate, screening, classification, disposition, or final-report records as scientific inputs. The handoff excludes those records from reusable evidence. Reusable metadata provides source identity and page locations without importing historical coverage exclusions.

DOC-001 has nine usable native/normalized text pages and full layout locators, supplemented by targeted images and fresh native layout extraction. DOC-002 has all 109 nonempty rendered JPEG locators; independent existence checks found no missing page-001.jpg through page-109.jpg. Its native/layout text is garbled. Twelve historical OCR files are empty; seven nonempty pages are partial transcription aids. The four support shards explicitly document visual reading of all 109 PLAN pages rather than substituting those text assets. DOC-003 has later layout coverage for pp. 1–2 and normalized text plus images for pp. 3–16.

Historical extraction/rendering engine versions are unrecorded and remain a provenance limitation. No version is invented. Current-run derivatives identify PyMuPDF 1.26.4 and CPU rendering/extraction. Targeted approved GPU OCR identifies RapidOCR 1.4.4, ONNX Runtime GPU 1.28.0, CUDA, and RTX 5070, with raw logs and text locators for PLAN pp. 10 and 80. The initial p. 29 trial is explicitly recorded as CPU fallback. The p. 80 OCR omits visible content, including the SMS total, and the map expressly uses the image transcription for that content.

Both commands below completed with exit status 0 and no mismatch output, from the package root:

```bash
sha256sum --check --quiet .ai_paper_validation/review_1_6_2/source_hashes_before.sha256
sha256sum --check --quiet .ai_paper_validation/review_1_6_2/reused_artifact_hashes_before.sha256
```

The first list contains three source files; the second contains 386 reusable artifacts. These checks establish that their bytes still agree with the before lists at audit time. Final after-list generation and comparison remain coordinator completion actions; this audit does not substitute for those final checks.

## Coverage-manifest audit

The audited manifest contains 48 coverage rows: 41 COMPLETE and seven still IN_PROGRESS or PLANNED at the snapshot. Every row contains exactly one plain relative artifact path. All 41 COMPLETE artifact paths exist. The seven pending paths are the canonical quality artifact, final Markdown report, and five assigned audit-part artifacts; their pending states describe the current assembly stage and do not indicate an unassigned scientific source unit. This assigned audit part now supplies one of those pending artifacts. The coordinator must update statuses as the parts and report are completed.

Every row was included in the artifact-cell and existence checks. The following grouped assessment preserves the distinction between direct-source partitions and later overlapping stage coverage:

| Manifest row group | Exact coverage assessment | Result at snapshot |
|---|---|---|
| Source inventory and evidence assets | All three sources and the reusable union; GPU and new-source derivative provenance have separate paths | COMPLETE; all paths exist |
| Main mapping, four support shards, merged support | Disjoint 134-page mapping partition plus separately identified merged union | COMPLETE; no missing or repeated direct-source page |
| Numeric checks and numeric inventory, main/support parts | Main and support scopes match the completed maps; the handoff enumerates 212 unique COMPLETE numeric IDs | COMPLETE artifact coverage; detailed relationship reasoning belongs to the statistical-coverage audit |
| Cross-source checker | Matched report/report, plan/report and plan/plan comparisons over the current maps | COMPLETE artifact coverage |
| Statistical pass 1 and statistical inventory | Exact S001–S114 enumeration on each assigned row | COMPLETE artifact coverage; full relationship confirmation belongs to the statistical-coverage audit |
| Initial inclusion screening and source/registration handoffs | Initial findings and cited source-confirmation pages assigned separately | COMPLETE artifact coverage; decisions audited in candidate parts |
| Candidate registration and three ledger parts | Complete registered ID scope distributed across bounded parts and merged ledger | COMPLETE artifact coverage; candidate-level inclusion/classification audited in candidate parts |
| Evidence recheck, three recheck parts, all-recheck facts | Complete registered ID scope with separate parts and pass-2 handoff | COMPLETE artifact coverage; evidence-card audit belongs to candidate parts |
| Statistical pass 2, three checker parts, three input shards, coverage summary | Explicit disjoint S001–S038, S039–S076 and S077–S114 inputs/checks plus merged union and summary | COMPLETE artifact coverage |
| All initial excluded-observation handoff | Checker observations retained in one path | COMPLETE artifact coverage; threshold audit belongs to the candidate/statistical parts |
| Quality handoff | Source/asset facts and 212 unique numeric IDs | COMPLETE artifact coverage |
| Canonical audit, five audit parts, report generation | Current assigned assembly stages, each with one path | PENDING completion; coordinator must close statuses after assembly |

The 212 numeric IDs are an observed inventory result: N001–N119 and N201–N293. Independent structural enumeration confirms 212 rows and 212 unique IDs, with no duplicate. This count is not a discovery or screening target. Both mappings describe fresh page-complete reconstruction and explicitly disavow use of historical scientific conclusions. No supplied audit evidence shows a candidate-count target or historical candidate list constraining this source mapping. The audit cannot infer unrecorded mental processes; its conclusion rests on source-derived scopes, durable mapping contents, and documented execution.

## Execution and tooling completion actions

The refreshed execution manifest has 24 actual-agent rows and 24 unique runtime IDs, including the coordinator and all five currently spawned auditors. The source mappings have fresh distinct mapper IDs. The statistical pass-1 runtime 01a12c43-fb96-7943-933b-ea7e7d98f89b and pass-2 runtime 01a12c69-56be-71f0-b3ab-86730a0e1482 are distinct fresh gpt-6.1-sol/high agents, with fresh high-effort pass-2 shards. Inclusion screener 01a12c4f-b7b6-7203-8c95-cfee2debbcc0 is fresh and distinct from both. Routing preflight records PASS, the default exact run model, the ten verified presets, and current-session provider. It candidly states that the original CLI launch invocation is not independently observable. Detailed relationship-pass closure is handled by the statistical audit part.

| Action or repair | Reason | Coordinator status |
|---|---|---|
| Replace tooling removal placeholder `NOT_CREATED` with `PENDING`, then `YES` after bundled removal | The same record states the fallback environment was CREATED, and the environment remains available for source inspection. The initial removal value does not describe that state. | Requested through coordinator; coordinator confirms PENDING now and final YES after removal, using the validator's schema |
| Close audit/report manifest rows only after their artifacts are assembled | Seven paths are pending at the audit snapshot. Marking them complete before writing would overstate artifact closure. | Required completion action |
| Add the fresh report-generator runtime once spawned | Current manifest correctly contains actual agents to date; report generation has not yet begun at this snapshot. | Required completion action |
| Recompute and compare final source and reusable-artifact hash lists | Before-list checks succeeded at audit time; final conservation requires end-of-run comparisons. | Required completion action |
| Render standalone HTML, remove the temporary fallback environment, finalize tooling and run validator | The requested workflow includes those final actions after report assembly. They are not yet complete at this audit stage. | Required completion action |

No input or historical artifact was modified by this auditor. Established statistical terminology in the maps remains intact; the vocabulary scan found only the established term `standard error`, with no disallowed characterization of a value or the authors' work. No severity, scientific disposition, or preferred analysis is assigned.

## Limitations and handoff

Source scientific coverage has no identified gap. Remaining limitations are historical derivative-engine versions not being recorded, garbled or partial PLAN text/OCR that is superseded by documented visual mapping, the supplied p. 13 clipping, and graphical quantities that have no exact numerical table. This coverage audit does not independently repeat all 109 mapper visual readings; it audits complete durable page maps, source-matched available locators, explicit image-reading provenance, links, counts, and integrity. Candidate auditors separately confirm the source locations that support each stable ID.

Covered source IDs: DOC-001, DOC-002, DOC-003; 134/134 mapped source units; 386/386 reusable assets match their before hashes; 48/48 manifest artifact cells audited; 134/134 merged-map evidence links resolve. New F-QA findings: zero. Screening repairs from this scope: zero. Tooling metadata repair: one requested and acknowledged by coordinator. Overall run completion remains pending the explicit final actions above.
