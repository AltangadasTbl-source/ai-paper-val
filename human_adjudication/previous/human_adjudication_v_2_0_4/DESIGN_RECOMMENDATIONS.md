# Human adjudication v.2.0.4: design decisions

## Design aim

V.2.0.4 treats the adjudication interface as an exploratory decision aid. The final-report construction stage has already checked candidate presentation and resolved duplicate registrations. Human adjudication focuses on whether to retain a candidate, its relationship-consistent review domain, the small domain-specific assessment, optional clustering, and notes needed for discussion.

The tool does not try to make practitioner judgment reproducible through extra mandatory form fields. A final report should disclose the exploratory role of the tool and leave interpretation and adoption decisions to the practitioner.

## Direct base and data boundaries

The direct candidate base is the four frozen v.2.0.3 annual HTML payloads. Candidate keys, titles, evidence, source links, and the consolidated relationship vocabulary are inherited from that base.

The current meta-report results are a separate input with one narrow role: they supply editable AI starting values for relationship, domain, and disposition. The builder verifies exact 412-key agreement before joining them. It never extracts or replaces the candidate universe from a reclassification JSON.

Valid design provenance begins with v.2.0.1 and v.2.0.2 and continues through v.2.0.3. Every `v_1_0_*` build is excluded from methodological inheritance and migration.

## Reduced record schema

The universal human record contains candidate disposition, editable review domain, optional related-cluster ID, domain-specific fields, and optional notes.

The statistical domain uses statistical error status, substantiveness, and potential downstream impact. The internal/plan-material domain uses one assessment field. The protocol-report domain uses documentation, justification, and interpretation.

V.2.0.4 removes these v.2.0.3 fields:

- flag verification;
- duplicate status;
- exact duplicate of candidate key;
- general potential consequence;
- evidence personally checked; and
- primary assessment rationale.

`relatedClusterId` remains because it can group distinct but connected candidates without recreating a duplicate-resolution workflow. `downstreamImpact` remains only in the statistical module because it supports the intended analytical distinction.

## Domain labels and editable routing

The four domain labels include their associated relationship symbols: statistical results and internal nonstatistical show `(S_C / S_W)`, protocol-report shows `(P_R)`, and plan material shows `(P_P)`. The meta-report relationship determines the AI starting domain, but every candidate retains all four choices. A human reviewer may change the domain and the conditional assessment module changes with it.

## AI initial state

The meta report remains an AI-generated categorization rather than a human conclusion. Its relationship and domain appear in an expandable AI starting-assessment panel, and its disposition/domain values initialize a new primary record. Prior `recorded_candidate` and `repaired_residual` states map to `retain`, `not_reproduced` maps to `exclude`, and `record_input_error` maps to `discuss`. This is a carry-forward of the earlier result, not a new reproducibility task. Reviewers may edit the values. They do not mark a record complete.

The builder writes one compact initial-state JSON per year beside the HTML. These files document the exact starting values and meta-report digest without mixing them with a human reviewer identity.

## Two-stage records

A checker snapshot preserves three layers:

1. the locked primary record;
2. the checker status and comment; and
3. an editable proposed final record.

The checker sees the primary answer, so any agreement statistic describes process consistency rather than blinded inter-rater reliability. The 2018 HTML embeds a complete all-discussion primary record and exposes a one-click test entry. The same snapshot is also written as a separate JSON to test the ordinary import path.

## Derived outcomes

Derived labels no longer depend on a second reproduction judgment:

- Primary temporal outcome: completed and retained `S_C`/`S_W`; statistical domain; confirmed or probable statistical error; substantive.
- Secondary temporal outcome: completed and retained `S_C`/`S_W`; internal-nonstatistical domain; substantive internal inconsistency.
- Protocol descriptive outcome: completed and retained `P_R`.
- Plan-material descriptive outcome: completed and retained `P_P`.

All labels remain exploratory and should be interpreted alongside the final-report disclaimer and practitioner review.

## Portability

Every local link is relative to an HTML stored at `human_adjudication/human_adjudication_v_2_0_4/`. A linked file under a year directory therefore uses `../../2018/...`, `../../2019/...`, `../../2024/...`, or `../../2025/...`. Build validation rejects home-directory paths, `file://` URLs, legacy `ai-paper-results/` prefixes, and unexpected local prefixes.

## Versioning

V.2.0.4 uses schema 7 and a separate browser-storage namespace. Earlier snapshots are not automatically migrated because removed fields and changed completion rules could otherwise imply review work that was not performed under this schema.
