# Workflow 1.6 Run State

- **Target basis:** Four PDFs contain 63 pages: 10 article pages, 42 protocol/data analytic and pharmacotherapy-plan pages, 10 results-supplement pages including nine vector plots, and one operational data-sharing page. All 63 pages have usable reusable evidence; zero pages require fresh extraction. The review still requires new complete mapping of article tables, historical and prospective plan quantities, and graphical results, with parallel main/support mapping, three parallel checking lanes, distinct two-pass statistical review, exact-source recheck, quality audit, and report generation. Allow 30-45 minutes for these agent waves and targeted visual confirmation; this target is based on reusable coverage and relationship complexity as well as source-unit count.
- **Total source units:** 63
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T00:35:03Z
- **Finished UTC:** 2026-10-11T01:14:01Z
- **Observed elapsed minutes:** 38.967
- **Target status:** MET_TARGET
- **Exceedance causes:** None

- **Workflow profile:** 1.6
- **Current phase:** COMPLETE: source coverage, mandatory specialist stages, reports, integrity and authorized-provider validation finalized.
- **Provider deviation:** User authorized the current openai provider instead of the workflow's openrouter provider; fixed model/effort routing is retained. See routing_preflight.md.
- **Direct sources:** 4 PDFs; no DOC, DOCX, XLS, XLSX, or CSV.
- **Source integrity:** PASS, four before/after SHA-256 entries unchanged.
- **Reused-artifact integrity:** PASS, all187 before/after SHA-256 entries unchanged.
- **Scientific coverage:** All 63 reusable-backed pages mapped; zero fresh-required units; all source rows COMPLETE.
- **Candidate discovery:** Restarted from supplied source evidence; old candidate, verifier, critic, classification, endetail, and report records excluded from discovery input.
- **Statistical pass 1:** COMPLETE, S001 through S108 in 108 explicit relationship rows.
- **Statistical pass 2:** COMPLETE, all108 relationships individually reviewed after full ledger and recheck; zero newly appended candidates.
- **Evidence recheck:** COMPLETE, all fifteen stable IDs; fourteen recorded_candidate and one record_input_error.
- **Quality audit:** COMPLETE, all fifteen IDs, all coverage rows and both statistical passes; derivative repairs confirmed; no new candidates.
- **Report assembly:** COMPLETE, fifteen cards and75 exact human placeholders.
- **Validation:** PASS under the user-authorized openai provider exception; zero errors and warnings. The unmodified original validator reports only its expected openrouter-provider mismatch, preserved in validation/original_review_validation.json.
- **Tooling:** Direct local tools available; no temporary fallback environment created.
- **Limitations:** Figure points lack exact printed numerical labels; mappers must preserve graphical approximation and avoid claiming exact coordinates. Legacy record exclusions do not limit this review. DOC-004 PLAN role is the best-supported prospective operational classification and is available for location-level recheck.

Finish time and observed duration were recorded immediately after complete Markdown assembly and advanced after the report agent repaired source-link spacing. Local integrity, rendering and validation operations are excluded from observed review duration.

## User-authorized validation adjustment

The user authorized current-provider execution. The unmodified bundled validator expects openrouter and will be run first, with its output preserved. The run-local copy validation/validate_review.py changes only that expected provider to openai; all other checks are identical. This is a copied supplied auxiliary helper, used solely to apply the authorized routing exception, never to perform scientific reasoning or extraction. Sole diff and validation basis are documented in validation/provider_exception.md. Bundled validator SHA-256:14f69039abc17511265ab9e647fb9d432cc46fafc228fdd0b7b3902fe6ddc695; local copy SHA-256:179d9c2c81d6d9ea08235ae868ceac953551e9c9978834375f9e2315da2776d5. Report both original and user-amended outcomes.
