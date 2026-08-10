# Workflow Agent Responses — DOC-001

## Package inventory

Classified `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` as DOC-001, an 11-page main article and scientific audit target. Native text was available.

## AI use restriction checker

Status: **Explicit AI Training Restriction**. Exact language appears in the footer on PDF pp. 1–11: “© 2024 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” Human Compliance Review was required and treated as approved under the user's instruction to assume all permissions were given. The full rights record is in `ai_training_restriction_record.md`.

## PDF preprocessor

Native text was extracted for PDF pp. 1–11. Pages 5–9 were rendered for result tables and figures. No OCR was required. Page-level provenance is in `page_manifest.csv`; the preprocessor response is in `agent_response.md`.

## Main-text extractor

The extractor mapped the primary and secondary results, participant flow, denominators, estimates, confidence intervals, and P values. Key anchors included:

- Primary week-8 SSPedi: 7.9 (7.2), n=198, versus 11.4 (8.7), n=209; adjusted mean difference −3.8 (95% CI, −6.4 to −1.2), `P=.007` (Results p. 4; Table 2 p. 7).
- Baseline SSPedi denominators 216/213 and week-8 denominators 198/209 (Table 2 p. 7).
- Participant flow reconciled to 221/224 randomized and 198/209 in the primary analysis (Figure 1 p. 5).
- Table 2 symptom odds ratios and PedsQL estimates matched DOC-003 eFigures 2 and 3.
- Table 3 encounter results matched DOC-003 eTable 12.

## Table arithmetic checker

No DOC-001 table-arithmetic candidate was returned.

## Figure and flow checker

One candidate was returned: Figure 2 on PDF p. 8 has baseline and week-8 panels but an unqualified caption giving only n=198/209, which matches week 8 and not the baseline counts of 216/213. No participant-flow inconsistency was found.

## Statistical consistency checker

One DOC-001-linked candidate was returned: the Results called the sadness intervention comparison significant while displaying `P=.05` despite a declared `P<.05` threshold. This was later classified **Uncertain** because the unrounded P value was unavailable.

## Evidence verifier

The Figure 2 caption candidate was **Verified** as a caption-scope ambiguity, not as evidence that the plotted baseline bars were wrong. The significance candidate was **Uncertain**. A supplement sparse-data candidate was rejected.

## Critic

The Figure 2 finding was retained as a **Minor Presentation inconsistency**. The uncertain significance candidate was excluded.

## Report generator

The retained finding and separate DOC-001 AI Training Restriction Record were included in `.ai_paper_validation/human_adjudication_report.md`.

Processing status: **Audited; submitted for Human Adjudication.**

