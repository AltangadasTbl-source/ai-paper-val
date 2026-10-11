# Workflow 1.4 Performance Profile

This document is normative for both workflow 1.4 profiles.

## Planning target

The target elapsed time for a typical single-paper package is 20–25 minutes. This is an operational
planning target, not a hard timeout and not permission to omit sources, relationships, statistical
pass 2, candidates, evidence rechecks, quality review, links, or report cards.

The target assumes a normal medical-paper package, usable local source files, no large-scale new OCR,
working local tools, and up to six independent specialist threads. Record the exact cause when the
target is exceeded, including document/page volume, missing or poor OCR, Office conversion, unusually
large relationship/candidate counts, tool failures, or repair waves.

## Reasoning-effort allocation

| Role class | Model | Reasoning effort |
|---|---|---|
| Coordinator | `gpt-5.6-sol` | `high` |
| Statistical consistency, both passes | `gpt-5.6-terra` | `high` |
| All other Terra roles | `gpt-5.6-terra` | `medium` |
| Mechanical evidence recheck | `gpt-5.6-sol` | `high` |
| Final evidence-quality audit | `gpt-5.6-sol` | `high` |

Do not silently raise a Terra role above this table. A one-off escalation requires a concrete failed
check or unresolved statistical relationship recorded in `run_state.md`; ordinary package length is
not sufficient.

## Latency rules

1. Run main/support mapping concurrently after one asset inventory and one coverage plan.
2. Run numeric, statistical pass 1, and cross-source review concurrently after mapping.
3. Reuse durable canonical artifacts; do not ask a later agent to reread unrelated source units.
4. Use the larger 1.4 shard thresholds to avoid unnecessary waves. Split only when the configured
   context bound would be exceeded, never to distribute a desired finding count.
5. Do not repeat OCR, Office conversion, extraction, a calculation, or a source-page confirmation when
   a current source-matched artifact already records it.
6. Generate report-card shards only when the candidate threshold is exceeded. Otherwise generate the
   complete report in one call and render HTML once after Markdown stabilizes.
7. Return compact agent statuses; complete evidence remains in artifacts rather than chat transcripts.

## Timing record

The coordinator records these exact fields in the versioned `run_state.md`:

```markdown
- **Target elapsed minutes:** 20-25
- **Started UTC:** YYYY-MM-DDTHH:MM:SSZ
- **Finished UTC:** YYYY-MM-DDTHH:MM:SSZ
- **Observed elapsed minutes:** NUMBER
- **Target status:** MET_TARGET or EXCEEDED_TARGET
- **Exceedance causes:** None, or a bounded semicolon-separated list
```

`Finished UTC` and `Observed elapsed minutes` are captured immediately after the complete Markdown
report is assembled. The coordinator then copies the finalized timing fields into the report, renders
HTML once, and runs the mechanical validator. These local finalization commands are expected to take
seconds and are excluded from the observed review duration so timing does not require a second report
generation wave.

Finish complete work even when elapsed time exceeds 25 minutes. Never convert the planning target into
sampling, early stopping, a candidate cap, or incomplete coverage.
