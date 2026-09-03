# Evidence-Quality Audit — Workflow 1.5.1

## Audit scope and result

This audit examined the complete current workflow artifacts for source inventory and coverage, reused-evidence provenance, main and support quantitative extraction, stable numeric/reporting relationships N001-N062, stable statistical relationships S001-S024, numeric review, cross-source review, both mandatory statistical passes, the stable candidate ledger, the mechanical evidence recheck, and the agent execution manifest. Direct supplied PDF pages were used to confirm the two candidate records; no legacy candidate, checker, disposition, queue, or report artifact was used as scientific evidence, and no external source was used.

The evidence chain supports two distinct quality-control candidates, C001 and C002, both of which remain **Pending Human Adjudication**. The audit does not assign validity, importance, severity, acceptance, exclusion, or a correction. C001 is a direct repeated-reporting mismatch. C002 is a directly reproducible count comparison whose relevance is explicitly conditional on a counting/overlap rule that the supplied aggregate display does not define. Neither candidate is based on a display-zero P value.

## Complete-coverage audit

### Source units and reusable/fresh closure

| Source | Total | Reusable | Fresh-required | Mapped | Audit observation |
|---|---:|---:|---:|---:|---|
| DOC-001 | 9 | 8 | 1 | 9 | `8 + 1 = 9`; all pages mapped. |
| DOC-002 | 26 | 0 | 26 | 26 | `0 + 26 = 26`; all pages mapped by direct rendered-page inspection. |
| DOC-003 | 24 | 0 | 24 | 24 | `0 + 24 = 24`; all pages mapped from the direct usable text layer. |
| DOC-004 | 11 | 9 | 2 | 11 | `9 + 2 = 11`; all pages mapped. |
| **Package** | **70** | **17** | **53** | **70** | `17 + 53 = 70`; mapped equals total. |

Every direct-source row in `source_coverage.md` therefore closes: reusable plus fresh-required equals total, mapped equals total, and status is `COMPLETE`. The main mapper accounts for DOC-001 pp. 1-9, including the freshly inspected reference-only p. 9. The support mapper accounts for all 61 pages of DOC-002 through DOC-004, including explicit page groups with no result display. The failed protocol OCR is a derivative limitation only; direct visual mapping closes the scientific coverage.

The four current direct-source SHA-256 values and all 51 reused-artifact SHA-256 values were mechanically rechecked against `source_hashes_before.sha256` and `reused_artifact_hashes_before.sha256`; every file matched at this audit point.

### Relationship and checker closure

- The mapper inventories contain 38 main numeric/reporting records and 24 support numeric/reporting records, normalized without loss as N001-N062. N038 is an explicit no-applicable-result record for DOC-001 p. 9 and appropriately remains in coverage.
- The mapper inventories contain 13 main and 11 support inferential/statistical records, normalized as S001-S024.
- `numeric_consistency.md` returns every N001-N062 relationship and records one provisional numeric candidate, later registered as C002.
- `statistical_pass_1.md` contains a relationship section and explicit `PASS_1_COMPLETE` marker for every S001-S024 relationship and emits SP1001.
- `cross_source_consistency.md` covers the full N001-N062 and S001-S024 union and emits XC001. SP1001 and XC001 concern the same printed any-stroke values, comparator, and consistency rule, so their pre-ID merge into C001 is a genuine duplicate merge.
- `statistical_pass_2.md` contains a relationship section and explicit `PASS_2_COMPLETE` marker for every S001-S024 relationship, revisits the complete C001/C002 ledger and mechanical recheck, and emits no additional distinct candidate.
- The stable ledger and mechanical recheck ID sets are both exactly C001 and C002. This artifact returns those same two IDs below.

No source or relationship unit is omitted because of a count target. The durable records expressly reject old selection boundaries, map all 70 pages, include all 62 N relationships and 24 S relationships, and register the actual two-candidate result without a queue, ranking, top-N list, or deferred-by-cap section. No artifact inspected in this audit indicates that a legacy candidate list controlled discovery.

### Coverage-manifest and execution-manifest audit

`coverage_manifest.md` has 14 data rows covering all 12 required stages; the two additional rows separately preserve the main and support relationship artifacts. Every Artifact cell contains exactly one undecorated POSIX-style relative path. Every row marked `COMPLETE` points to an existing artifact. The candidate registration and evidence-recheck rows enumerate C001 and C002. Both statistical rows enumerate all 24 S IDs rather than using an ID range. The evidence-quality row enumerates C001 and C002 and points to this artifact. At the audit point it is still marked `IN_PROGRESS`; the coordinator must change it to `COMPLETE` after accepting this artifact. The report-generation row is correctly still `PENDING`, and its one referenced artifact does not yet exist.

`agent_execution_manifest.md` contains the coordinator and every specialist active through this audit exactly once. Statistical pass 1 is `/root/statistical_pass_1` and statistical pass 2 is `/root/statistical_pass_2`; these are distinct fresh-spawn runtime IDs, each recorded as `gpt-5.6-terra` with `high` reasoning effort and a different canonical output artifact. No medium-effort mapper was repurposed as either statistical pass. Any later report generator or repair agent must be added exactly once when spawned.

## C001 — Conflicting confidence intervals for the matched any-stroke rate ratio

- **Candidate status boundary:** Pending Human Adjudication. This audit makes no scientific disposition.
- **Category audit:** `Cross-document numeric inconsistency` is one of the exact allowed primary categories and applies to a matched value differing between the abstract, results narrative, and figure.
- **Exact source support:** Direct DOC-001 inspection confirms [PDF p. 1](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1) prints any stroke as 69 (2.7%) versus 64 (2.5%), rate ratio 1.08, 95% CI 0.76-1.53. [PDF p. 5](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5) and Figure 4B on [PDF p. 7](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7) print the same counts, percentages, point estimate, and 2.5-year any-stroke context with 95% CI 0.77-1.51. All cited pages exist in the nine-page PDF, and each link resolves to the named source and page.
- **Direct observation:** The printed lower endpoints are 0.76 and 0.77; the printed upper endpoints are 1.53 and 1.51. The outcome, arms, follow-up, arm counts, percentages, and rate-ratio point estimate match across the cited locations. The detailed narrative and figure agree with each other.
- **Inference and rule:** Repeated reporting of the same matched result should preserve the same rounded CI endpoints unless a distinct estimand, analysis snapshot, or interval method is identified. The supplied locations identify no such distinction. The rule establishes a reporting mismatch but does not identify which interval is intended.
- **Calculation audit:** `0.77 - 0.76 = 0.01` and `1.53 - 1.51 = 0.02`. The crude displayed count ratio, `69 / 64 = 1.078125`, rounds to 1.08 but is not represented as a reconstruction of the time-to-event estimator. No incorrect interval-endpoint subtraction or unsupported reconstruction is used.
- **Necessary inputs and alternatives:** The package supplies the matched labels and printed values needed for the comparison. It does not supply event times, full risk sets, censoring by arm, O-E, V, unrounded endpoints, the exact interval construction, or an explanation for separate methods. A transcription/production difference, unsynchronized outputs, or separately generated intervals remain source-compatible possibilities; none establishes an intended correction.
- **Duplicate and provenance audit:** SP1001 and XC001 are genuine duplicates because they compare the same two interval displays under the same repeated-reporting rule. Their merge before stable assignment is supported. The ledger retains both checker provenances and relates the issue to S003, N006, and S013. C001 is not a duplicate of C002 because it concerns CI endpoints rather than subtype-count composition.
- **Mechanical recheck audit:** All required recheck fields are present: cited locations found, source and comparator matched, applicable rule, reproduced comparison, available and missing inputs, source-grounded alternative, observation/inference separation, and exact remaining human question.
- **Neutrality and impact audit:** The wording does not select an authoritative CI or infer a change to the paper-level conclusion. The downstream statement is bounded to the possibility that an extractor, systematic review, or meta-analysis could copy a nonauthoritative endpoint pair if the issue is confirmed.
- **Display-zero exclusion:** Not applicable; C001 does not involve a P-value display, so no conditional independent-contradiction field is required.
- **Evidence-card field repair for report assembly:** The ledger already supplies the candidate statement, category, locations, source evidence, reported-versus-comparator, reasoning, calculation, alternatives, relevance, bounded downstream impact, and human steps. The final report card must additionally summarize the completed mechanical evidence recheck under the exact `**Mechanical evidence recheck:**` label and include the exact blank adjudication template below. It should preserve the present page-specific PDF links and must not state which CI is correct.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Stroke subtype counts do not partition the displayed any-stroke count in the patch group

- **Candidate status boundary:** Pending Human Adjudication. This audit makes no scientific disposition.
- **Category audit:** `Numeric or arithmetic inconsistency` is an allowed primary category. Because the source does not establish mutual exclusivity or a common unit of counting, the card must retain the explicit conditional framing already present in the ledger and recheck; it must not present a required partition as a source fact.
- **Exact source support:** Direct inspection of Figure 4B on DOC-001 [PDF p. 7](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7) confirms column heading `No. of events (%)` and patch/usual-care values: presumed ischemic stroke 60 (2.4%)/58 (2.3%), hemorrhagic stroke 12 (0.5%)/6 (0.2%), and any stroke 69 (2.7%)/64 (2.5%). The caption gives the 2.5-year window and record sources and says presumed ischemic stroke includes unspecified types under its stated assumption. The page exists and the link resolves to the exact figure.
- **Direct observation:** The patch subtype cells sum to 72 while the patch any-stroke cell is 69. The usual-care subtype cells sum to 64 and its any-stroke cell is 64. The figure does not print an exclusivity, exhaustiveness, participant-level uniqueness, recurrence, overlap, or deduplication rule.
- **Inference and rule:** The component-sum identity is applicable only if the two subtype rows are mutually exclusive and exhaustive components counted under the same participant-level rule as `Any stroke`. Those conditions are not established by the figure. The candidate is therefore a counting-rule clarification attached to reproducible displayed arithmetic, not proof that 69, 60, or 12 is wrong.
- **Calculation audit:** Patch: `60 + 12 = 72` and `72 - 69 = 3`. Usual care: `58 + 6 = 64`. Patch percentages sum to 2.9% versus 2.7%, but integer counts—not percentage rounding—establish the comparison. The displayed percentages individually reproduce from denominator 2520: `60/2520 = 2.381%`, `12/2520 = 0.476%`, and `69/2520 = 2.738%`, rounding to 2.4%, 0.5%, and 2.7%. A three-person overlap follows only under additional set-union assumptions and is correctly labelled as an inference in the recheck.
- **Necessary inputs and alternatives:** The package lacks participant-level outcome records, a unit-of-count definition for each row, overlap counts, recurrence and reclassification rules, subtype exhaustiveness, and the `Any stroke` deduplication/first-event rule. Nonexclusive endpoint events or participant overlap could reconcile the display. The usual-care equality does not prove that the rows are exclusive.
- **Duplicate and provenance audit:** C002 derives from NC001 and N035, with S013 as related inferential context. It is distinct from C001 because it compares event-count composition under a conditional identity rather than repeated CI endpoints. No unsupported duplicate merge is needed.
- **Mechanical recheck audit:** All required recheck fields are present: cited location found, all six source/comparator values matched, conditional rule stated, arithmetic and denominator checks reproduced, available and missing inputs named, source-grounded nonexclusive-endpoint alternative, observation/inference separation, and an exact remaining human question.
- **Neutrality and impact audit:** The ledger and recheck appropriately distinguish the direct arithmetic from the unresolved counting convention. They do not claim a paper-level conclusion change. The downstream statement is bounded to what an evidence extractor or systematic review could sum or describe if the candidate is confirmed. In the final report, avoid shortening the statement to an unconditional claim that the subtype rows must partition `Any stroke`.
- **Display-zero exclusion:** Not applicable; C002 does not involve a P-value display, so no conditional independent-contradiction field is required.
- **Evidence-card field repair for report assembly:** The ledger already supplies the candidate statement, category, locations, source evidence, conditional comparator, reasoning, calculation, alternatives, relevance, bounded downstream impact, and human steps. The final report card must additionally summarize the completed mechanical evidence recheck under the exact `**Mechanical evidence recheck:**` label and include the exact blank adjudication template below. It must preserve the conditional counting-rule language and the page-specific source link.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Coordinator repair instructions and limitations

No source-grounded candidate content requires deletion, suppression, renumbering, ranking, or scientific disposition. The following workflow-completion actions remain:

1. Change only the `evidence_quality` coverage row from `IN_PROGRESS` to `COMPLETE` after accepting this canonical audit.
2. Generate the complete final report with both C001 and C002 cards. Each card must contain every exact label required by `report_spec.md`, the mechanical-recheck summary, and all five adjudication subfields with the exact `__` placeholders shown above. Preserve C002's conditional rule and both candidates' bounded downstream-impact wording.
3. After spawning the report generator, add its actual agent once to `agent_execution_manifest.md`, change the report-generation coverage row to `COMPLETE`, and include that agent in the token-usage ledger. Add any later repair agent in the same manner.
4. Finalize `run_state.md`, token accounting, hash-after records, HTML rendering, and mechanical validation after report assembly. These artifacts were not yet available at this audit point, so their final cross-artifact consistency cannot be confirmed here.

Evidence limitations are bounded. The protocol's reusable/native extraction was unusable and CPU OCR was empty, but direct rendered-page inspection mapped all protocol pages. Aggregate PDFs do not provide the analysis output or participant-level records needed to select the intended C001 interval or resolve the C002 overlap/counting convention. Those absences are the exact human-adjudication questions; they do not create an uncovered source unit.

Audit counts: 4/4 direct-source rows closed; 70/70 source pages mapped; 62/62 N relationships checked; 24/24 S relationships completed in each statistical pass; 14/14 coverage rows structurally audited; 10/10 currently manifested agents structurally audited; 2/2 stable IDs returned and mechanically rechecked.
