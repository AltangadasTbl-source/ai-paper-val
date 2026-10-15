# Workflow 1.6.1 Quantitative Quality-Control Scope

This document is normative for workflow 1.6.1.

## Review objective

Identify reporting issues in the supplied paper package that a statistically literate reader could
not resolve at once and that could change how a reported result is interpreted or which value is
taken into data extraction or evidence synthesis. Prepare each one for human adjudication. The
workflow is a quality-control aid for publication and evidence-synthesis use. It does not judge
authors or declare a paper invalid.

The packages are randomized trials from many clinical fields. Reviewers and readers are specialists
in their own fields, and field-specific wording that such a reader understands immediately is not a
reporting issue for this workflow.

## Vocabulary

Call every registered item a `candidate` or a `reporting issue`, and describe the observation as an
`inconsistency`, a `discrepancy`, an `unclear` or `incomplete` statement, or a result that `does not
reconcile` under a stated rule. Never describe a candidate, a value, or the authors' work with the
words error, mistake, defect, erroneous, wrong, or incorrect. Established statistical and clinical
terms that contain one of these words (for example standard error, type I error, measurement error,
refractive error, medication error, septal defect) keep their usual names.

## The four review domains

Every candidate belongs to exactly one of four review domains. The domain is the candidate's
category; there is no other category system.

| Review domain | Relationship types | What belongs here |
|---|---|---|
| `statistical_results` | `S_C`, `S_W` | Counts and denominators, estimates and intervals, test logic, and statistical method logic in the report materials (focus areas A, B and C below). |
| `report_internal_inconsistency` | `S_C`, `S_W` | Report materials conflict about which outcome, time point, analysis set, or comparison a reported number belongs to, so that a reader cannot tell which result applies. Wording or labeling differences alone do not belong here. |
| `protocol_report` | `P_R` | The report differs from the protocol or statistical analysis plan (SAP) in a statistical design or analysis element (focus area D). |
| `plan_material` | `P_P` | The protocol or SAP is internally inconsistent in a statistical design element that the reported analysis relies on (focus area D). |

### Focus areas

A. **Counts and denominators.** Participant flow numbers, randomized, treated, analyzed and
   followed-up totals, event counts, numerator/denominator pairs, row and column totals, and the
   same count reported differently in two places, when the difference exceeds display precision and
   leaves the value a reader or data extractor should use unclear.

B. **Estimate and test logic.** A point estimate outside its interval; interval limits in the wrong
   order; an estimate, interval, P value, or test statistic that cannot belong to the same stated
   analysis; a direction of effect that conflicts between estimate, label, narrative and figure; a
   superiority, noninferiority, or equivalence conclusion that does not follow from the reported
   interval and the stated margin; a reported multiplicity, interim, or stopping decision that does
   not follow from the stated rule.

C. **Statistical method logic.** A reported analysis whose method, as described in the supplied
   materials, has a logical gap (a step needed to obtain the reported result is missing or
   contradicted), is unclear in a way that prevents a reader from knowing which analysis produced a
   reported number, or appears inconsistent with the stated design or data structure. Examples: a
   sample size that does not reproduce from the stated inputs; a test for independent samples
   applied to data the paper describes as paired; a model the text says accounts for clustering or
   stratification while the reported analysis description omits it; an effect measure labeled as one
   quantity but computed as another. Ground every such candidate in the supplied text. Do not propose
   a preferred method, and do not question a choice that is stated and internally coherent.

D. **Planned versus reported statistical design.** Primary or key secondary outcome definition or
   time point, primary analysis model and covariates, analysis population, handling of missing data,
   noninferiority or equivalence margin and hypothesis direction, sample size and power assumptions,
   interim, stopping and multiplicity rules, and a prespecified primary or key secondary analysis that
   is replaced or not reported. Inside plan material, the same elements stated inconsistently.

## Cross-document and cross-location comparisons

Comparisons across documents (main article, supplements, protocol, SAP) and across locations in one
document (abstract, Key Points, text, tables, figures) remain in scope, but what is compared decides
whether a difference can matter. Apply this scope rule before the inclusion threshold. It is not a
severity grade. A key secondary outcome is one reported in the abstract or prespecified as key
secondary.

Comparisons that can meet the inclusion threshold:

- a primary or key secondary outcome result (effect estimate, interval, P value, event count,
  denominator, or outcome distribution) that differs beyond display precision between locations or
  documents, or whose direction or reference group conflicts;
- a result attributed in one location to a different outcome, population, analysis set, or time point
  than in another (for example an all-cause death percentage described as cause-specific deaths);
- a label that changes the quantity a value represents (for example a monthly rate versus a change
  over 24 weeks) when the values do not show which applies;
- report versus protocol or SAP: the analysis specification (model, covariates, priors, imputation,
  matching, prespecified subgroup or sensitivity analyses, analysis population), the endpoint
  definition, threshold, window, or hierarchy, or the dose or duration of the randomized intervention;
- within plan material: sample size or power inputs, the primary endpoint, the primary analysis, a
  margin, or a decision rule stated inconsistently.

Comparisons screened out as `PERIPHERAL_COMPARISON`, unless the difference changes a primary or key
secondary result, the size of an analysis population, or a planned decision rule:

- descriptive baseline characteristics (means, standard deviations, counts, percentages) that differ
  between the main baseline table and a supplementary table;
- observation or contributor counts at individual time points, or values in secondary or exploratory
  displays;
- footnotes, cross-references, table or figure pointers, and panel or heading labels;
- numbers of sites or centers, recruitment dates and calendars, and other administrative details,
  within the report or between report and plan;
- other inconsistencies inside plan material, including background or historical data presented in a
  protocol or SAP.

## Inclusion threshold

Register a candidate only when all of the following hold:

1. **Reproduced.** The cited values or statements are read correctly from the exact supplied source
   location, and the inconsistency remains under the stated arithmetic, statistical, or logical rule.
2. **In focus.** It falls under focus area A, B, C, or D, fits one of the four review domains, and
   is not a peripheral comparison as defined above.
3. **Not resolved by context.** A statistically literate reader in the relevant clinical field could
   not identify the intended value or meaning at once from common sense or the immediate context (the
   same sentence, paragraph, table, figure, or caption).
4. **Bears on interpretation or extraction.** It could plausibly change how a specific reported
   result is interpreted, or which value a data extractor would take for a systematic review or
   meta-analysis. Name that result or value.

The threshold is an inclusion criterion, not a severity grade. Do not rank, grade, or label
candidates as major or minor. A finding that fails any criterion is screened out with one reason code
below; it is recorded in the screening log and does not receive a `C` ID.

## Screened-out observations

Screen out, with exactly one of these reason codes, every observation that falls under one of the
following descriptions, even when it is real:

| Reason code | Observations screened out |
|---|---|
| `NOT_REPRODUCED` | The cited values, read correctly, reconcile; or the apparent inconsistency arose from the reviewing agent's own transcription, page assignment, or alignment of non-matching results. |
| `ROUNDING_OR_DISPLAY_PRECISION` | Differences within display precision: a recomputed percentage, difference, ratio, or mean that matches when each displayed input is allowed its half-unit rounding interval; percentages that sum to slightly more or less than 100 because each was rounded; different numbers of decimal places for the same value; a very small P value displayed as `P = 0`, `P = .000`, or equivalent. |
| `NOTATION_OR_TYPOGRAPHY` | A missing, duplicated, or substituted symbol or character whose intended reading is obvious (for example `P 0.05` or `P = .05` where `P < .05` is evidently meant from the interval or text), a misplaced or missing unit or percent sign where the values make the unit obvious, dash or minus glyphs, spacing, duplicated words, axis tick or caption formatting, and any other typographic slip. |
| `TERMINOLOGY_OR_WORDING` | Inconsistent names or descriptions of groups, populations, outcomes, scales, instruments, procedures, or definitions across the text that a reader in the field resolves at once (for example "patients" and "participants", two names for the same analysis set, or an abbreviated and an expanded outcome name), unless they make it impossible to tell which reported number applies. |
| `MODEL_VERSUS_CRUDE` | An adjusted, modeled, stratified, or otherwise model-based estimate that differs from a crude ratio or difference recomputed from printed counts, unless the source states that the estimate is crude or unadjusted. |
| `CONTEXT_RESOLVES` | Any other observation whose intended value or meaning is identifiable at once from common sense or the immediate context and that cannot change the interpretation of any result or the value a data extractor would take. |
| `CONDITIONAL_OR_UNREPORTED` | An observation that holds only under an assumption the package does not establish, or that consists only of a detail the paper does not report. |
| `PERIPHERAL_COMPARISON` | A cross-document or cross-location difference of a kind listed as peripheral in the section above, when it does not change a primary or key secondary result, the size of an analysis population, or a planned decision rule. |
| `OUT_OF_FOCUS` | Differences outside focus areas A to D (for example staff roles or procedural descriptions), general design or clinical critique, and preferences for a different analysis. |
| `DUPLICATE_OF_INCLUDED` | The same issue as a finding already included, including another occurrence of an included pattern. |

When in doubt whether a reader in the field would resolve an observation at once, screen it out under
`CONTEXT_RESOLVES` or `TERMINOLOGY_OR_WORDING` rather than registering it.

## One candidate per issue

Register one candidate per distinct issue. When the same rule fails for the same evident reason in
several rows, subgroups, outcomes, figures, time points, or documents (for example one denominator
applied to a whole column, or one mislabeled effect measure repeated across a table), register one
candidate and list every affected location in it. Register separate candidates only for different
rules or independent causes.

## No expected count

There is no expected, typical, minimum, maximum, or target number of candidates. Do not calibrate the
screening to a number, to other papers, or to earlier runs; decide each finding on the criteria alone.
Zero candidates is a valid result after complete coverage.

## Document-role classification

The review domain is constrained by the documents in conflict. Assign each compared location one role
by content, never by file name or supplement number:

- `REPORT`: the main article, or a non-plan results supplement (eTables, eFigures, eAppendix results,
  structured result files);
- `PLAN`: a protocol, SAP, protocol amendment or plan version, or a prospective operational document
  such as a manual of procedures.

A protocol/SAP bundle that is physically supplied as a supplement is still `PLAN`. Inconsistencies
inside one bound plan bundle remain plan-internal even if the bundle contains several plan versions.

### Relationship types

| Code | Meaning |
|---|---|
| `P_R` | `REPORT` content differs from `PLAN` content. It does not imply a protocol violation. |
| `P_P` | An inconsistency solely within `PLAN` material, inside one plan document or between plan documents or versions. |
| `S_C` | An inconsistency between two different `REPORT` documents: main article versus a non-plan supplement, or two non-plan supplements. |
| `S_W` | An inconsistency within one `REPORT` document. |

Record every relationship the candidate involves in `All relationships`. When a candidate involves
more than one, choose the primary relationship type by precedence `P_R` > `P_P` > `S_C` > `S_W`. A
document that only corroborates one side of an inconsistency is not a relationship: a protocol that
merely confirms the intended value of an internal report inconsistency does not make that candidate
`P_R`. Record any uncertain role assignment or possible disclosed amendment in `Classification
ambiguity`.

The review domain must agree with the relationship type: `P_R` → `protocol_report`; `P_P` →
`plan_material`; `S_C` or `S_W` → `statistical_results` or `report_internal_inconsistency`, chosen by
content as defined above. Use `statistical_results` whenever the issue concerns counts, estimates,
intervals, tests, or statistical methods.

### Evidence state

The mechanical evidence recheck assigns exactly one evidence state:

| Evidence state | Use when |
|---|---|
| `reproduced` | The recheck finds the cited values or statements and reproduces the registered inconsistency. |
| `reproduced_after_transcription_correction` | A transcribed value or location in the registration was corrected, and the corrected source values still show the registered inconsistency. |
| `not_reproduced` | The direct-source recheck shows that the cited values, read correctly, reconcile. |

A `not_reproduced` candidate keeps its stable ID and card, because IDs are never deleted after
registration. The evidence state is an evidence-record distinction, not a validity judgment. No
disposition is suggested; the human reviewer decides every disposition.

## Tone

Use neutral phrases such as `candidate reporting issue`, `the printed values do not reconcile under
the stated rule`, `the stated method does not specify`, and `requires human adjudication`. Avoid
sensational or prosecutorial language. Keep paper-level conclusion impact separate from potential
downstream evidence reuse, and claim neither without package evidence.
