# Final Evidence-Quality Audit

## Audit conclusion

This audit procedure is complete for the current Workflow 1.5.2 artifacts. The artifact chain is internally consistent for the registered empty relationship and candidate sets, but the scientific-content review is source-access limited. All 69 supplied PDF pages received fresh structural unit records; none received readable native text, layout text, rendered-page evidence, or CPU OCR. Accordingly, structural source-unit coverage is complete, while completeness of the paper's actual quantitative and statistical relationship universe cannot be established from this run.

**Stable candidate set is empty. No stable candidates were identified.**

- **Direct sources:** 4 PDF files.
- **Direct source units:** 69 PDF pages.
- **Fresh-required source units:** 69.
- **Structurally mapped source units:** 69.
- **Registered numeric/reporting relationships:** 0 `N` IDs.
- **Registered inferential-statistical relationships:** 0 `S` IDs.
- **Stable quality-control candidates:** 0 `C` IDs.
- **Mechanical evidence recheck:** 0/0 stable `C` IDs.
- **Audit ID return:** complete empty `C` set; there is no `C` heading to reproduce.

The zero relationship and candidate counts are access-limited inventory results. They are not a paper-level finding that the article or supporting PDFs contain no quantitative results, statistical results, or reporting inconsistencies.

## Direct-source and evidence-inventory audit

The fresh source inventory contains exactly the four root-level supplied PDFs: DOC-001 with 11 pages, DOC-002 with 37 pages, DOC-003 with 7 pages, and DOC-004 with 14 pages. These counts sum to 69. There are no root-level Office, workbook, or CSV scientific sources in the direct-source inventory.

Every `source_coverage.md` row meets the profile's required numeric identities: reusable units are 0, fresh-required units equal total units, mapped units equal total units, and status is `COMPLETE`. The row-level identities are 11 = 11 for DOC-001, 37 = 37 for DOC-002, 7 = 7 for DOC-003, and 14 = 14 for DOC-004. The artifact explicitly defines mapped units as fresh structural page records rather than recovery of scientific content. That qualification is necessary and must remain prominent in the final report.

The SHA-256 values in `source_hashes_before.sha256` were independently recomputed during this audit with `sha256sum` and matched all four recorded values exactly. No source modification was detected at the audit point.

The current-run inventories and every mapper/checker provenance statement reviewed here consistently exclude legacy audit derivatives, web material, and external literature. No current-run scientific evidence path points to a legacy derivative. This supports the recorded evidence-chain boundary; the audit cannot independently reconstruct private agent read history beyond the durable provenance records.

Fresh tool-status records support the stated access limitation: `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, and `soffice` are not on the current PATH. `sha256sum` and `file` are available. No GPU use is recorded or required. The only fresh preprocessing derivative is `preprocessing/tool_and_page_status.md`, containing one structural status row for every page.

One bounded reproducibility omission remains in `evidence_asset_inventory.md`: it summarizes availability and the raw PDF page-tree fallback but does not record the exact commands, complete command outputs, or specific tool versions required by the review contract. In particular, the exact page-tree/Perl `Compress::Zlib` invocation used for page counts is absent, and `file` and `sha256sum` are recorded only as available rather than by version. The source hashes themselves are reproducible; the structural page-count procedure is described but not command-reproducible from the artifact as written.

The DOC-004 role description also goes beyond the accessible scientific evidence when it calls the file likely graphical/statistical output based on R producer metadata. Producer metadata can support a bounded statement about the generating software, but it does not establish the scientific content. The conservative role is supporting PDF with exact content indeterminate. This inference did not create an `N`, `S`, or `C` record.

## Coverage-manifest audit

`coverage_manifest.md` contains 21 data rows and includes every required stage: `source_inventory`, `evidence_assets`, `main_evidence_mapping`, `support_evidence_mapping`, `numeric_checks`, `statistics_pass_1`, `cross_source_checks`, `candidate_registration`, `evidence_recheck`, `statistics_pass_2`, `evidence_quality`, and `report_generation`.

Every coverage row contains exactly one undecorated POSIX-style relative artifact path. No artifact cell contains multiple paths, a Markdown link, prose, a comma-separated list, or a semicolon-separated list. Each shard identifier is unique. All 19 rows marked `COMPLETE` resolve to existing artifacts. At the audit snapshot, `evidence_quality` and `report_generation` remained `PLANNED`; this audit creates the former artifact, while the coordinator must change that row to `COMPLETE` and must create and complete the report row after report generation.

Main and support assignments are disjoint and cover DOC-001 pp. 1-11 and DOC-002 pp. 1-37, DOC-003 pp. 1-7, and DOC-004 pp. 1-14, respectively. The underlying mapping artifacts contain one row or explicit page enumeration for each of the 69 structural units. Canonical relationship inventories merge both mapper parts without an unlisted shard.

The candidate-stage scopes correctly state the complete empty `C` set rather than using an ID range. The two statistical-pass scopes correctly state the complete empty `S` set. Because the scientific contents of every page are unavailable, these rows document procedural coverage of the registered empty inventories; they cannot substantiate discovery coverage of unobserved printed relationships. No top-N, candidate cap, desired count, review queue, or early-stopping boundary appears in the reviewed discovery chain. The empty inventories arise from source-access failure, not a count boundary.

## Relationship and checker audit

The canonical numeric inventory and its two disjoint parts agree on 0 `N` IDs. `numeric_consistency.md` covers all required numeric check families for the empty registered set, separates direct observation from inference, emits 0 candidates, and names the missing evidence and exact human question.

The canonical statistical inventory and its two disjoint parts agree on 0 `S` IDs. Statistical pass 1 records `PASS_1_COMPLETE` for 0/0, covers every required check family as not mechanically applicable under source non-access, and emits 0 candidates. Statistical pass 2 records `PASS_2_COMPLETE` for 0/0 and explicitly revisits denominator, arithmetic, population, duplicate-value, label/scale, measure, rate/count, figure, cross-source, inferential-compatibility, and recheck implications. It emits 0 new candidates.

`cross_source_consistency.md` covers all four documents and 69 structural page units, records 0 matchable relationships, and emits 0 candidates. It does not infer agreement from the absence of readable evidence.

All four candidate-part artifacts agree: numeric candidates 0, cross-source candidates 0, statistical-pass-1 candidates 0, and statistical-pass-2 new candidates 0. The candidate ledger therefore has no duplicate relationship to merge and assigns no stable ID. The empty result did not involve deletion, ranking, suppression, or post-registration merging.

## Statistical execution and agent-manifest audit

At this audit snapshot, `agent_execution_manifest.md` contains 10 unique agent rows, including the coordinator exactly once and this evidence-quality auditor exactly once. Every current row has one primary artifact path. The manifested specialist roles cover fresh preprocessing, main mapping, support mapping, numeric review, cross-source review, both statistical passes, mechanical evidence recheck, and evidence-quality audit.

The two required statistical reviewers are distinct fresh agents:

| Pass | Agent ID | Model | Effort | Start mode | Inventory coverage |
|---|---|---|---|---|---|
| Statistical pass 1 | `/root/statistics_pass_1` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | 0/0 `S` IDs |
| Statistical pass 2 | `/root/statistics_pass_2` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | 0/0 `S` IDs plus 0/0 `C` recheck facts |

The IDs are non-placeholder and unequal. Neither statistical pass reused a mapper agent or a Terra/medium execution. Any report-generation or later repair agent spawned after this snapshot must be added exactly once to the manifest and token ledger; this audit cannot preconfirm future rows.

## Stable-ID, evidence-recheck, and card-field audit

No `## Cnnn` heading occurs in `candidate_ledger.md`, `verification/evidence_recheck.md`, or any checker candidate part. Their stable-ID sets are therefore identical empty sets. The recheck states both the required empty-set notice and 0/0 coverage, and it records the mechanical field meanings and the exact remaining human question without creating a scientific disposition.

There is no candidate card on which to test a printed value, comparator, arithmetic, pagination, duplicate relationship, alternative interpretation, conclusion-impact claim, downstream-impact claim, or candidate-specific source link. Counts of missing or defective candidate-card fields are therefore all 0 because the card set is empty, not because inaccessible paper contents were checked. No candidate-specific calculation is asserted. No false candidate pagination was found; all source-page references used in the mappings identify an existing structural page and end in `#page=N`, although page images were unavailable for visual confirmation.

No human-adjudication subfield is instantiated for a candidate. Consequently, there is no nonblank adjudication value and no violation of the required exact blank placeholder `__`. If any candidate is appended after this audit, every card must use `__` for Validity, Importance, Action, Initials, and Notes, and that ID must be added without renumbering and mechanically rechecked before report assembly.

No candidate is based on `P = 0`, `p = 0.000`, or equivalent display-zero notation. The statistical artifacts mention display zero only to apply the exclusion rule and state that no P-value display was accessible. There is no independent supplied-source contradiction and no display-zero candidate card requiring the conditional contradiction field.

## Scope, category, and communication audit

Because the stable set is empty, no primary category is assigned and there is no out-of-scope category assignment to repair. The reviewed checker and ledger language remains neutral quality control, distinguishes structural access from scientific findings, preserves `Pending Human Adjudication`, and does not assign severity, validity, acceptance, exclusion, or a scientific disposition. It makes no paper-level conclusion-impact claim and no unbounded claim that a defect propagated into a systematic review, meta-analysis, guideline, or other evidence product.

## Coordinator repair and finalization list

1. Preserve the explicit distinction between 69/69 structural source-unit mapping and unavailable scientific-content mapping throughout the final report. Do not describe 0 `N`, 0 `S`, or 0 `C` as proof of substantive consistency or complete relationship discovery.
2. If authoritative command history is available or the read-only checks can be rerun, add exact commands, tool versions, and outputs for `file`, `sha256sum`, executable discovery, root page-tree inspection, and the Perl `Compress::Zlib` fallback to the fresh evidence-asset record. Do not reconstruct an invocation from memory or fabricate output.
3. Replace or qualify the DOC-004 graphical/statistical-content inference in `source_inventory.md` and `checkers/cross_source_consistency.md`; R producer metadata establishes software provenance, not the file's scientific content.
4. Change the `evidence_quality` coverage row from `PLANNED` to `COMPLETE` now that this artifact exists. Create the final report, change `report_generation` to `COMPLETE`, and ensure the empty stable-set notice is explicit in the report.
5. Finalize the stale `run_state.md` stage and all pending timing fields immediately after Markdown report assembly. Append every subsequently spawned report or repair agent exactly once to `agent_execution_manifest.md` and to the authoritative token ledger.
6. Recompute all four source hashes at completion and preserve exact equality with `source_hashes_before.sha256`. Render and validate only after the Markdown, coverage, manifest, timing, and token artifacts are final.

## Audit limitation

The direct PDFs remain authoritative, but no permitted readable derivative could be produced in the current environment. This audit can confirm complete structural assignment, artifact-set identity, manifest form, exact hash continuity at the audit point, empty-set checker consistency, and neutral wording. It cannot confirm that all printed quantitative or statistical relationships were discovered, that result-level calculations reconcile, or that page citations identify the intended scientific text. Fresh page-addressable native/layout text or rendered-and-CPU-OCR evidence is required for those scientific-content confirmations.
