# Workflow 1.5.3/1.5.4 OpenRouter Performance Profile

This document is normative for both OpenRouter workflow 1.5 profiles.

## Per-package planning target

Set the planning target separately for each paper package after inventory. Do not assume a fixed SAP
length, a fixed supplement length, or a fixed total page count. Count the actual supplied main article
and every support source in `source_coverage.md`, then consider:

- total source units;
- how many units require fresh direct-source mapping rather than reusable extraction;
- PDF, Office, workbook, or CSV complexity;
- OCR, conversion, and visual-table requirements;
- expected relationship volume and required agent waves.

Do not derive a target from page count alone and do not use universal `SMALL`, `MEDIUM`, or `LARGE`
bands. Record a bounded package-specific explanation in `Target basis` and a positive `MIN-MAX` minute
range in `Target elapsed minutes`.

The completed workflow 1.4.1 run is one calibration point only: that package contained five PDFs with
102 total pages across the main article and all support files, of which 81 pages initially lacked
reusable extraction. It finished in 49.4 minutes after a coverage repair and two statistical reruns.
A 35-50 minute target may be reasonable for a future package with comparable total scope, missing-
derivative burden, and review complexity. It is not a default for other packages and says nothing
about the expected length of an SAP.

Retain each clean workflow 1.5 observation as future calibration evidence. The target is not a hard
timeout and never permits omitted sources, relationships, statistical pass 2, candidates, evidence
rechecks, quality review, links, or report cards. Record bounded causes whenever the selected upper
bound is exceeded.

## Reasoning-effort allocation

| Role class | Model | Reasoning effort | Start requirement |
|---|---|---|---|
| Coordinator | `~openai/gpt-latest` | `high` | Current coordinator session |
| Statistical consistency pass 1 | `~openai/gpt-latest` | `high` | New specialist agent |
| Statistical consistency pass 2 | `~openai/gpt-latest` | `high` | Different new specialist agent |
| All other specialist roles | `~openai/gpt-latest` | `high` | New specialist when delegated |
| Mechanical evidence recheck | `~openai/gpt-latest` | `high` | New specialist when delegated |
| Final evidence-quality audit | `~openai/gpt-latest` | `high` | New specialist when delegated |

Every role uses `high` effort. Spawn each statistical pass as a fresh configured agent; when the named
preset is unavailable, omit the spawn-model override so the launcher-enforced
`~openai/gpt-latest`/`high` default applies. The two passes use distinct runtime agent IDs and read
durable artifacts rather than shared chat context. Record both executions in
`agent_execution_manifest.md`.

Do not lower a specialist below `high`. Repairs and fallback default agents use the same model/effort
contract.

## Latency rules

1. Run main/support mapping concurrently after one asset inventory and one coverage plan.
2. Run numeric, statistical pass 1, and cross-source review concurrently after mapping.
3. Reuse durable canonical artifacts; do not ask a later agent to reread unrelated source units.
4. Split only when the configured context bound would be exceeded, never to distribute a desired
   finding count.
5. Do not repeat OCR, Office conversion, extraction, a calculation, or a source-page confirmation when
   a current source-matched artifact already records it.
6. Generate report-card shards only when the candidate threshold is exceeded. Otherwise generate the
   complete report in one call and render HTML once after Markdown stabilizes.
7. Return compact agent statuses; complete evidence remains in artifacts rather than chat transcripts.

## Timing record

The coordinator records these exact fields in the versioned `run_state.md`:

```markdown
- **Target basis:** BOUNDED PACKAGE-SPECIFIC EXPLANATION
- **Total source units:** INTEGER
- **Fresh-source units:** INTEGER
- **Target elapsed minutes:** MIN-MAX
- **Started UTC:** YYYY-MM-DDTHH:MM:SSZ
- **Finished UTC:** YYYY-MM-DDTHH:MM:SSZ
- **Observed elapsed minutes:** NUMBER
- **Target status:** MET_TARGET or EXCEEDED_TARGET
- **Exceedance causes:** None, or a bounded semicolon-separated list
```

`Total source units` and `Fresh-source units` must equal the sums in `source_coverage.md`. The target
range must use positive whole minutes with the lower bound below the upper bound. `Finished UTC` and
`Observed elapsed minutes` are captured immediately after the complete Markdown report is assembled.
Copy all finalized fields into the report, render HTML once, and run the mechanical validator. Local
rendering and validation are excluded from observed review duration so timing does not require a
second report-generation wave.

Use `Finished UTC` as the model-usage accounting cutoff. The token ledger includes every coordinator
and specialist response inside the review window. The local token-cost calculation, HTML rendering,
and mechanical validation do not consume model tokens and remain outside that window. If a validation
repair requires a later model response, move `Finished UTC` forward and regenerate both timing and
token summaries.

Finish complete work even when elapsed time exceeds the selected upper bound. Never convert the
planning target into sampling, early stopping, a candidate cap, or incomplete coverage.
