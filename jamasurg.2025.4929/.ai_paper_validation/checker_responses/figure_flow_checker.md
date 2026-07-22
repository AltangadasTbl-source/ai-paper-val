# Figure and Participant-Flow Check

## Scope and sources

- Main article: DOC-001, `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`, PDF pages 1-9 only. PDF page 10 was not inspected.
- Results supplement: DOC-003, `soi250075supp2_prod_1767031598.05318.pdf`, PDF page 3 used only for visible cross-check anchors.
- Protocol DOC-002 was not inspected.
- Canonical evidence: source-PDF page images retained by preprocessing, plus nearby normalized native text and the main-text extractor response. OCR was not treated as canonical.

## Local candidate issues

### FF-01 - Postrandomization refusal label makes enrollment timing internally unclear

- **Category:** Presentation inconsistency
- **Severity:** Low
- **Location:** DOC-001, PDF p. 3 (journal p. 11), Figure, "Consolidated Standards for Reporting Trials (CONSORT) Diagram"; compare DOC-001, PDF p. 4 (journal p. 12), "Statistical Analysis" and "Study Flow and Analysis Population."
- **Visible/source evidence:** The top figure box describes all 240 participants as "willing to sign informed consent form," and all 240 then enter the "Randomized" node. After randomization, the LDG exclusion branch lists 3 "Refused trial enrollment" and the ODG branch lists 2 "Refused trial enrollment." Nearby prose instead describes the excluded population as patients who "refused or withdrew" and confirms that 16 patients were excluded from each group following randomization.
- **Logical basis:** The branch geometry unambiguously places the 5 refusals after randomization, but "refused trial enrollment" suggests they had not enrolled, while the nearby prose allows the distinct postrandomization event of withdrawal. The reported counts are consistent; the candidate concerns the visible disposition label and timing, not the exclusion arithmetic.
- **Verification instruction:** Inspect the source figure and participant-level disposition coding to determine whether these 5 patients withdrew consent/enrollment after randomization or refused a later procedure. If so, relabel the two boxes to state the actual postrandomization disposition consistently with the Results prose.

### FF-02 - Group-column spanner says "No. (%)" above continuous summaries

- **Category:** Presentation inconsistency
- **Severity:** Low
- **Location:** DOC-001: PDF p. 4 Table 1, p. 5 Table 2, p. 6 Table 3, and p. 7 Table 4 (journal pp. 12-15), visible group-column headers.
- **Visible/source evidence:** Each table places the spanner "No. (%)" above the LDG and ODG columns, although those columns also contain explicitly labeled continuous summaries. Examples include age as mean (SD) in Table 1; operating time as mean (SD) and blood loss as median (IQR) in Table 2; tumor size as mean (SD) and lymph-node count as median (IQR) in Table 3; and hospital stay as mean (SD) and time to adjuvant chemotherapy as median (IQR) in Table 4.
- **Logical basis:** "No. (%)" does not describe mean (SD) or median (IQR) cells. Row labels recover the intended statistics, so this is a header-presentation defect rather than an ambiguity in the underlying values.
- **Verification instruction:** Verify the group-column spanner in the source layout on all four table pages; replace it with a neutral heading (for example, "Value") or make the statistic-specific row labels/header structure govern without a categorical-only spanner.

### FF-03 - Supplementary table uses two visibly inconsistent treatment labels

- **Category:** Presentation inconsistency
- **Severity:** Very low
- **Location:** DOC-003, PDF p. 3, eTable 2, "Univariate and Multivariate Analysis for Predicting Postoperative Morbidity"; compare DOC-001, PDF p. 5, Table 2 and surrounding Surgical Outcomes prose.
- **Visible/source evidence:** eTable 2 prints "Aproach" and "Rouxx-En-Y." DOC-001 consistently prints "Approach" in the morbidity-model prose and "Roux-en-Y" in Table 2 and the Surgical Outcomes prose.
- **Logical basis:** These are visible typographical inconsistencies in labels for the same concepts across the article package. They do not alter denominators or effect estimates.
- **Verification instruction:** Compare the source renderings and correct the supplementary labels to "Approach" and "Roux-en-Y."

## No-issue checks

1. **CONSORT arithmetic:** 120 LDG + 120 ODG = 240 randomized. LDG exclusions total 7 + 6 + 3 = 16; ODG exclusions total 9 + 5 + 2 = 16. Each arm therefore retains 120 - 16 = 104, and 104 + 104 = 208. The merged "208 Included in full analysis" and "208 Short-term outcomes analysis" nodes reconcile exactly.
2. **Branch geometry:** Both exclusion boxes visibly branch from their assigned treatment arm before the merged analysis node. The 104 actual-treatment boxes are visibly linked to the 208 short-term-analysis node; no clipped arrow or misplaced count was identified.
3. **Nearby prose cross-reference:** DOC-001 PDF p. 4 states 240 randomized, 16 excluded per group, no pre-resection crossover, and 208 analyzed as 104 per group. These values agree with the Figure.
4. **Main-table denominators:** Tables 1-4 visibly label both treatment columns `n = 104`, consistent with the Figure and Results prose.
5. **Supplementary anchor:** DOC-003 PDF p. 3 eTable 2 shows approach denominators LDG 23/104 and ODG 22/104; these agree with DOC-001 Table 4 overall-morbidity cells and do not introduce a participant-flow mismatch.
6. **Figure caption and legend:** The Figure caption is present and legible, and LDG/ODG are defined next to the diagram. No axis or scale applies to this flow diagram.
7. **Scope exclusions:** DOC-001 PDF p. 10 and all protocol pages in DOC-002 were not used.

## Disposition

Three local presentation candidates are returned. No participant-count inconsistency was found.
