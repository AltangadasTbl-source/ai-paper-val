# Evidence Quality Audit

## Audit scope and outcome

This audit covers the complete fresh Workflow 1.5.2 evidence chain available before report
generation: three direct PDFs and all 28 PDF pages; 69 numeric relationships (`N001`–`N069`);
38 inferential-statistical relationships (`S001`–`S038`); the numeric, cross-source, and both
statistical checker artifacts; the complete stable ledger and mechanical recheck for `C001`,
`C002`, `C003`, `C004`, `C005`, and `C006`; every source-coverage and coverage-manifest row; and
the agent-execution manifest. The audit used only the supplied direct PDFs and fresh Workflow 1.5.2
artifacts. It did not use an old audit derivative or an external source.

All six stable IDs are preserved below exactly once and remain **Pending Human Adjudication**. The
ledger, recheck, and this quality artifact have the identical stable-ID set. There was no count target,
top-N boundary, review queue, or early stopping rule. No mapped source contains a displayed-zero P
value, and no stable candidate has a display-zero P value as its basis.

One correctable arithmetic transcription was found and repaired through the coordinator without an
ID or status change: the `C004` count diagnostic in `candidate_ledger.md` and
`checkers/statistical_pass_1.md` now reports
`9/1147 − 7/1156 = .001791`, diagnostic `SE=.003463`, and diagnostic 95% interval approximately
`−.0050 to .0086`, matching the independently reproduced recheck. No genuinely new candidate is
supportable from this audit.

## Source, relationship, stage, and agent coverage

- `source_coverage.md` contains one row for each direct source. DOC-001 is 10/10 pages, DOC-002 is
  12/12 pages, and DOC-003 is 6/6 pages. For every row, reusable units are 0, fresh-required units
  equal total units, mapped units equal total units, and status is `COMPLETE` (28/28 pages overall).
- The current SHA-256 values of all three direct PDFs exactly match
  `source_hashes_before.sha256`. Fresh native and layout text cover all pages; result-relevant pages
  were rendered, and only DOC-003 p. 6 received targeted direct CPU Tesseract OCR because of heading
  glyph corruption. No source changed.
- The main map covers DOC-001 pp. 1–10. The support map covers DOC-002 pp. 1–12 and DOC-003
  pp. 1–6, explicitly recording reference/index-only pages with no applicable result unit. The
  canonical inventories individually enumerate all 69 `N` IDs and all 38 `S` IDs.
- The numeric checker has an explicit completion register and individual index covering 69/69 `N`
  IDs. Statistical pass 1 and statistical pass 2 each have an explicit record for 38/38 `S` IDs.
  The cross-source checker covers the union of 69 `N` and 38 `S` relationships. Pass 2 also revisits
  all six ledger IDs and all recheck facts. No relationship unit is deferred or suppressed.
- Every coverage-manifest data row contains exactly one plain relative artifact path. The source,
  mapping, numeric, both statistical, cross-source, candidate-registration, and recheck rows are
  complete and enumerate their full assigned ID sets. After this artifact is written, the coordinator
  must replace the pending `evidence_quality` scope with the explicit scope
  `C001; C002; C003; C004; C005; C006` and status `COMPLETE`. The analogous report-generation row
  must enumerate the same six IDs when the report exists; these are completion repairs, not discovery
  limits.
- `agent_execution_manifest.md` contains the coordinator and every agent used through this audit,
  each once with one primary artifact. Statistical pass 1 (`/root/statistics_pass_1`) and statistical
  pass 2 (`/root/statistics_pass_2`) are distinct fresh runtime IDs, both recorded as
  `gpt-5.6-terra`, `high`, and `FRESH_SPAWN`. Any later report-generation or repair agent must be
  appended once before token accounting.
- The final report did not yet exist at this audit stage. Its six cards must use the exact five blank
  human-adjudication subfields (`Validity`, `Importance`, `Action`, `Initials`, and `Notes`), each with
  the value `__`. This requirement cannot be confirmed until report assembly and remains a mandatory
  downstream validation gate.

## C001 — Table 2 placebo calcium `N=1994` exceeds the randomized placebo cohort

- **Evidence and pagination:** The cited cell is present in DOC-001
  [PDF p. 5](../../../jama_lappe_2017_oi_170019.pdf#page=5), Table 2, under the placebo “No. of
  Participants” column. The randomized placebo total `1147` is present on
  [PDF p. 1](../../../jama_lappe_2017_oi_170019.pdf#page=1) and in Figure 1 on
  [PDF p. 4](../../../jama_lappe_2017_oi_170019.pdf#page=4). All links resolve to the cited physical
  PDF pages.
- **Exact values and rule:** The table prints placebo calcium `N=1994`, placebo mean
  `512 (489 to 536)` mg/d, treatment `N=1099`, and treatment mean `500 (475 to 525)` mg/d. The
  adjacent placebo vitamin-D row prints `N=1094`. Under the printed participant-count header,
  `1994−1147=847`; a unique-participant count cannot exceed the randomized arm without a supplied
  different-unit definition. The independent mean calculation `500−512=−12.0` agrees with the row.
- **Observation and inference boundary:** The printed `1994`, header, and `1147` comparator are direct
  observations. A transposition to `1094` is only a plausible explanation based on the adjacent row;
  it is not a source-established correction.
- **Category, definitions, and duplication:** `Denominator, proportion, or total inconsistency` is an
  allowed primary category. The missing source-data count and intended counting unit are explicitly
  named. Numeric and statistical proposals were properly merged before stable IDs because they use
  the same cell, comparator, and rule. No other stable record duplicates this relationship.
- **Report-card readiness:** Locations, source evidence, comparator, arithmetic, alternatives, recheck
  facts, and the human question are available. The final card must add an explicit bounded
  quality-control relevance statement, bounded downstream extraction risk, human verification steps,
  and the five exact `__` adjudication blanks. It must not state that `1094` is the correction or that
  downstream propagation occurred.

## C002 — Protocol’s ≥70-year vitamin-D “limit” has the opposite inequality direction

- **Evidence and pagination:** DOC-002
  [PDF p. 7](../../../joi170019supp1_prod.pdf#page=7), section 5, prints the complete instruction and
  is the correct physical page.
- **Exact text and rule:** The same sentence governed by “limit” prints “no more than 400 IU/day” for
  age `<70` and “more than 600 IU/day” for age `≥70`. The first clause is an upper bound (`≤400`),
  while the second is a lower bound (`>600`), so the directions are not parallel upper-limit labels.
- **Observation and inference boundary:** The two inequality phrases are direct observations. An
  omitted “no,” or an intended `≤600 IU/day` instruction, is plausible but not established. A literal
  interpretation as a distinct recommended minimum for the older group remains source-grounded,
  although the source does not state that the coordinated clauses have different purposes.
- **Category, definitions, and duplication:** `Measure, label, or scale inconsistency` is appropriate
  for the directional label conflict. The intended maximum or explicitly different lower-bound
  purpose is missing and is named as the human question. `C002` and `C003` both map to `N057`, but
  they compare different printed statements under different rules and are not duplicates.
- **Report-card readiness:** Evidence, comparator, logical procedure, alternatives, recheck facts, and
  the human question are available. The final card must preserve the conditional wording, add bounded
  relevance and downstream extraction risk, give human verification steps, and use all five exact
  `__` adjudication blanks. It must not prescribe `≤600 IU/day` as a final correction.

## C003 — Protocol changes the calcium target unit from 1200 mg/day to 1200 g/day

- **Evidence and pagination:** DOC-002
  [PDF p. 7](../../../joi170019supp1_prod.pdf#page=7), section 5, contains the regimen and purported
  matching supplementation level on the same physical PDF page.
- **Exact values and rule:** The protocol prints calcium `1200 mg/d`, two `600 mg` caplets per day,
  and then `1,200 g/day` as the included supplementation level. Exact conversion gives
  `600 mg×2/day=1200 mg/day=1.2 g/day`; `1200 g/day=1,200,000 mg/day`, a 1000-fold conflict with
  the stated regimen.
- **Observation and inference boundary:** Both unit strings and the dose schedule are direct source
  observations. A substitution of `mg` for `g`, or `1.2 g/day`, is a plausible but unconfirmed
  production explanation.
- **Category, definitions, and duplication:** `Measure, label, or scale inconsistency` is an allowed
  category. The intended unit and production-source value are explicitly missing. This record is not
  a duplicate of the separate inequality-direction relationship in `C002`.
- **Report-card readiness:** Exact evidence, conversion, alternatives, recheck facts, and the human
  question are available. The final card must add bounded relevance and potential copying risk,
  human verification steps, and all five exact `__` adjudication blanks. It must not state a final
  replacement value without the production source.

## C004 — Death-difference confidence interval is discordant with the printed flow counts under a labelled diagnostic calculation

- **Evidence and pagination:** DOC-001 Figure 1 and adjacent narrative on
  [PDF p. 4](../../../jama_lappe_2017_oi_170019.pdf#page=4) print 7 treatment and 9 placebo deaths,
  randomized denominators 1156 and 1147, difference `.002`, and 95% CI `−.006 to .037`. The location
  and values match the direct PDF.
- **Exact calculation:** Placebo minus treatment is
  `9/1147−7/1156=.001791`, which rounds to `.002`. The explicitly diagnostic ordinary unpooled-Wald
  calculation gives `SE=.003463` and nominal 95% interval approximately `−.0050 to .0086`; the
  arithmetic repair in the ledger and pass 1 now matches the mechanical recheck.
- **Observation and inference boundary:** The printed counts, denominators, difference, and CI are
  direct observations. The discordance of `.037` is a reviewer diagnostic under an ordinary Wald
  construction. The package does not state that the reported interval used this construction, and it
  does not supply the implemented analysis population, variance rule, or contrast orientation.
- **Category, definitions, and supportability boundary:** `Statistical reporting inconsistency` is the
  applicable category for the conditional count/interval diagnostic. The unsupplied CI method is a
  material evidentiary boundary: the Wald calculation cannot establish a corrected endpoint or exact
  same-method contradiction. The record therefore must remain framed as a diagnostic quality-control
  question requiring the analysis/production source, without suppression or scientific disposition.
  No other stable record concerns this death interval.
- **Report-card readiness:** Printed evidence, point arithmetic, diagnostic procedure, recheck facts,
  alternative explanations, and missing definitions are available. The final card must label the
  Wald interval as diagnostic, avoid implying that `.0086` is the intended endpoint, bound downstream
  risk to possible copying of the printed CI, provide human recomputation steps, and use all five exact
  `__` adjudication blanks.

## C005 — Outside-study vitamin-D difference CI includes zero while printed P=.002

- **Evidence and pagination:** DOC-001 Table 2 on
  [PDF p. 5](../../../jama_lappe_2017_oi_170019.pdf#page=5) prints treatment `N=1099`,
  `740 (691 to 789)` IU/d; placebo `N=1094`, `869 (803 to 934)` IU/d; difference `−128.1`,
  95% CI `−209.5 to 46.6`; and `P=.002`. Direct visual and text checks confirm that no minus sign is
  printed before `46.6`.
- **Exact calculation and rule:** `740−869=−129`, compatible with `−128.1` at the available precision.
  The ordered printed interval contains the point estimate and zero. A corresponding same-contrast,
  two-sided 95% interval and two-sided null test would not pair null inclusion with `P=.002`.
  Replacing only the upper sign yields an approximately symmetric interval and a normal diagnostic
  near `.002`, but that is explanatory arithmetic, not a correction.
- **Observation and inference boundary:** The same-row CI and P value are direct observations. A lost
  minus sign is plausible, while correspondence of the interval and test procedures remains
  conditional because Table 2 does not name their exact variance/model mapping or sidedness.
- **Category, definitions, and duplication:** `Statistical reporting inconsistency` is appropriate.
  The exact CI/test methods and production endpoint are named missing inputs. This record shares
  `N028`/`S012` with `C001` but concerns a different row, values, comparator, and consistency rule;
  it is not a duplicate. No display-zero exclusion applies.
- **Report-card readiness:** Evidence, calculation, conditional inversion rule, alternatives, recheck
  facts, and the human question are available. The final card must preserve the conditional
  same-procedure premise, avoid prescribing `−46.6`, bound downstream risk to possible extraction of
  the CI/P pair, include verification steps, and use all five exact `__` adjudication blanks.

## C006 — Figure 1 discontinuation counts conflict with p.7 vitamin-D/placebo discontinuation total and percentages

- **Evidence and pagination:** DOC-001 Figure 1 on
  [PDF p. 4](../../../jama_lappe_2017_oi_170019.pdf#page=4) prints `238` and `246` under
  “Discontinued intervention.” The narrative on
  [PDF p. 7](../../../jama_lappe_2017_oi_170019.pdf#page=7) prints `304` participants, with 12.4% of
  treatment and 14.0% of placebo, stopping the vitamin-D or placebo supplement. Both links resolve to
  the correct physical PDF pages.
- **Exact calculation and rule:** Figure components reproduce `11+93+134=238` and
  `16+76+154=246`, totaling `484`. The narrative percentages are compatible with 143/1156 and
  161/1147 at one-decimal precision, and `143+161=304`. Rounding cannot reconcile 484 and 304.
- **Observation and inference boundary:** The two displays and their arithmetic are direct
  observations. Treating them as the same discontinuation construct is conditional: Figure 1 does
  not define whether its broader label includes either study component, another protocol-status
  category, a different time window, or another event rule.
- **Category, definitions, and duplication:** `Cross-document numeric inconsistency` is applicable to
  matched narrative-versus-figure locations within the supplied article. The exact figure event,
  component, time, and participant-counting definitions are missing and named. This is distinct from
  all other stable relationships and was not duplicated by the numeric or statistical lanes.
- **Report-card readiness:** Evidence, arithmetic, alternative constructs, recheck facts, and the
  exact human question are available. The final card must keep the construct match conditional,
  avoid claiming that either 304 or 484 is the correction, bound downstream risk to possible copying
  of a discontinuation count or definition, provide source-data verification steps, and use all five
  exact `__` adjudication blanks.

## Cross-candidate completeness, limitations, and required closeout

The six stable relationships are distinct under printed value, comparator, and consistency rule.
`C001` correctly preserves its pre-ID numeric/statistical duplicate merge; no post-ID deletion,
renumbering, merge, ranking, or suppression occurred. Every stable ID has a separate mechanical
recheck containing location match, source and comparator match, applicable rule, reproduced
calculation or logic, available and missing inputs, a source-grounded alternative, explicit
observation/inference separation, and an exact remaining human question.

The direct sources do not supply raw analysis data, the Table 2 CI/test/variance mapping, the
death-difference CI construction and implemented population, production files for the suspected
typographic values, or Figure 1's exact discontinuation construct. These bounded limitations are
retained and do not authorize suppression of an ID. Candidate wording remains neutral quality
control, does not assign severity or scientific disposition, does not claim a paper-level conclusion
change, and does not claim that downstream propagation occurred.

Coordinator closeout after this audit must (1) mark the full explicit `evidence_quality` coverage row
complete, (2) later enumerate all six IDs in the report-generation row, (3) ensure the final report
contains all six cards and all five `__` human-adjudication blanks per card, and (4) add any subsequent
agent to the execution manifest and token ledger. Subject to those downstream assembly actions, the
fresh evidence-quality scope is complete: 3/3 sources, 28/28 pages, 69/69 numeric relationships,
38/38 relationships in each statistical pass, and 6/6 stable candidates.
