# Final Evidence-Quality Audit

## Audit scope and outcome

This audit covers every current stable candidate (`C001`, `C002`, `C003`, `C004`, and `C005`), all 16 current coverage-manifest rows, all four direct-source coverage rows and 80 source units, the fresh source/evidence inventories and hashes, both 63-record canonical relationship inventories, all numeric/cross-source/statistical checker outputs, both statistical passes, the candidate ledger, the mechanical evidence recheck, and all 10 agents manifested at audit time. No candidate count was suppressed.

The scientific coverage available at audit time is complete: 80/80 direct-source units are mapped; 63/63 canonical numeric relationships have numeric checks; 63/63 canonical statistical relationships have explicit pass-1 and pass-2 records; the cross-source checker covers all 126 canonical relationships; and ledger/recheck/this quality artifact each contain exactly `C001` through `C005`. All candidates remain **Pending Human Adjudication**.

Three supportable coordinator repairs are required before report assembly:

1. In `checkers/cross_source_consistency.md`, CP-01 labels and links the matched Results narrative as PDF p. 6. Direct page extraction confirms that the `6.25% [4.10%-8.10%]` sentence is on main-article PDF p. 7. The canonical ledger, statistical pass 1, and recheck correctly use PDF p. 7. Repair the CP-01 location and link to `#page=7`.
2. Reframe the C003 title from “names the wrong comparison groups” to neutral source-grounded wording such as “difference footnote conflicts with the displayed comparison groups.” The printed contradiction and arithmetic remain unchanged.
3. Narrow C004's rule and report wording. The article does directly define the four-component reported composite and explicitly says the predefined statin data were not collected. The supported observation is that the supplied SAP and article use the same outcome name for different printed component sets, with no supplied amendment or change-control record. Do not state that the article failed to disclose the revised definition or imply that relabeling is necessarily required. Also preserve cross-source CP-04 provenance and link the reported result to `N026`, `N027`, and `S032` when the report card is assembled; the ledger currently has no canonical relationship ID for C004.

These are provenance and wording repairs. They do not authorize deletion, merging, ranking, suppression, scientific disposition, or renumbering of any stable ID.

## Source, integrity, and evidence-asset audit

| Source | PDF pages | Reusable | Fresh-required | Mapped | Audit result |
|---|---:|---:|---:|---:|---|
| DOC-001 `jama_huffman_2018_oi_170166.pdf` | 12 | 0 | 12 | 12 | COMPLETE |
| DOC-002 `joi170166supp1_prod.pdf` | 32 | 0 | 32 | 32 | COMPLETE |
| DOC-003 `joi170166supp2_prod.pdf` | 9 | 0 | 9 | 9 | COMPLETE |
| DOC-004 `joi170166supp3_prod.pdf` | 27 | 0 | 27 | 27 | COMPLETE |
| **Total** | **80** | **0** | **80** | **80** | **COMPLETE** |

- The package root contains four direct scientific source files, all PDFs; their recorded sizes and page counts match the inventory. No direct Office, workbook, or CSV source was omitted.
- The four current SHA-256 values exactly reproduce the four nonblank records in `source_hashes_before.sha256`: `11311a6b...aaca5f5`, `0e13bdfc...ab9004a`, `d49019c3...6bb1c6`, and `511f4a90...93f3ec` for DOC-001 through DOC-004 respectively. No source-hash change was found at audit time.
- `preprocessing/source_page_classification.md` has one row for every page: 12 DOC-001 rows, 32 DOC-002 rows, 9 DOC-003 rows, and 27 DOC-004 rows. Fresh native and layout extraction exists for all four PDFs; targeted fresh renders cover result-relevant visual pages.
- No old candidate set, prior audit conclusion, old checker output, old final report, or old discovery boundary was used as evidence. The sole pre-existing derivative used was the user-authorized, source-hash-matched OCR aid for image-only DOC-004 pp. 3-16. It was used for toolkit-page coverage and qualitative definitions; no exact OCR graph value was treated as a trial-outcome value, and no new CPU or GPU OCR was run.
- Fresh PDF page extraction independently reproduced the candidate-bearing printed values. The supplied PDFs remain authoritative; extracted text and renders are locators and inspection aids.

## Relationship, checker, and discovery audit

| Lane | Canonical units | Completed checker units | Coverage result |
|---|---:|---:|---|
| Numeric/reporting | 63 (`N001`-`N035`, `N501`-`N528`) | 63/63 | COMPLETE |
| Statistical pass 1 | 63 (`S001`-`S050`, `S501`-`S513`) | 63/63 `PASS_1_COMPLETE` | COMPLETE |
| Statistical pass 2 | Same 63 S IDs | 63/63 `PASS_2_COMPLETE` | COMPLETE |
| Cross-source | 126 N/S relationships | 126/126 | COMPLETE |

- Numeric checking produced two proposals, statistical pass 1 produced four proposals, and cross-source checking produced five proposals. The duplicate-merge record preserves their provenance and merges only same-values/comparator/rule duplicates into five stable IDs.
- Statistical pass 2 revisited the complete S inventory, the complete stable ledger, and all recheck facts; it represented all five stable IDs and found no additional distinct proposal.
- No target, minimum, maximum, top-N selection, review queue, or early-stopping boundary controlled discovery. The relationship enumerations and completed-record counts show full-lane coverage rather than a finding-count cutoff.
- No supplied P value is displayed as `P = 0`, `p = 0.000`, or equivalent. Both statistical passes explicitly record zero applicable display-zero relationships. None of `C001`-`C005` is based on a display-zero P value, so no independent-contradiction field is required for these candidates.
- Candidate categories follow `QUALITY_CONTROL_SCOPE.md`: C001-C002 use `Cross-document numeric inconsistency`; C003-C005 use `Measure, label, or scale inconsistency`. No broad study-design, clinical, misconduct, novelty, or raw-data finding was registered.

## Coverage-manifest and agent-execution audit

- The coverage manifest has 16 rows at audit time: 15 `COMPLETE` rows and the `evidence_quality` row marked `IN_PROGRESS` while this artifact was being written. Every row has exactly one undecorated POSIX-style relative artifact path, every shard ID is unique, and every referenced artifact exists after this audit file is written.
- Existing candidate-stage scopes enumerate `C001`, `C002`, `C003`, `C004`, and `C005` individually. Both statistical scopes enumerate all 63 S IDs individually. Main and support mapping scopes are disjoint and together cover DOC-001 through DOC-004.
- Coordinator action remains necessary after this artifact stabilizes: change `evidence_quality` to `COMPLETE`. The required `report_generation` stage is not yet present because the report generator has not run; add that row with all five IDs and exactly one report artifact path when the report is assembled.
- The execution manifest has 10 unique rows at audit time: one coordinator and nine fresh specialists covering preprocessing, both mappers, numeric checking, cross-source checking, statistical passes 1 and 2, evidence recheck, and this audit. Every row has one primary artifact path.
- Statistical pass 1 (`/root/statistics_pass_1`) and statistical pass 2 (`/root/statistics_pass_2`) are distinct fresh runtime agent IDs. Both are recorded as `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, with distinct canonical artifacts. No mapper or medium-effort agent was repurposed for either pass.
- A report-generator agent and any later repair agents are not yet manifested. The coordinator must add every later actual agent exactly once and include all manifested agents in the token ledger before completion.

## Candidate identity, link, and card-readiness audit

The candidate ledger and evidence recheck each contain exactly one heading for every ID `C001`-`C005`, with no extra stable ID. Every cited PDF exists locally, every cited page is within its source page count, and every canonical ledger/recheck PDF link ends in `#page=N`. Direct source checks reproduced the comparisons at main PDF pp. 3, 6, 7, and 9; SAP PDF pp. 5 and 7; and Supplement 3 PDF p. 17.

The final report did not exist at audit time. For each candidate below, the ledger plus recheck supply the substantive inputs needed for all required report-card fields. Report assembly must still emit the exact labels from `report_spec.md`, including candidate statement, source evidence, reported-versus-comparator, reasoning procedure, calculation, mechanical evidence recheck, quality-control relevance, bounded downstream impact, human verification steps, and the exact blank adjudication template. Potential impact must be conditional on confirmation and limited to what a later extractor or evidence product could copy; no propagation or paper-level conclusion change is established by the supplied package.

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint mismatch

- **Evidence-quality checks:** Exact locations and printed values are present and directly reproduced at [Table 2 — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6) and [Results narrative — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7). The table prints `6.25 (4.10 to 8.40)` and the narrative prints `6.25% [4.10%-8.10%]`; `8.40-8.10=0.30` percentage points. The point estimate, lower endpoint, OR `1.46`, OR interval `1.29-1.65`, population, contrast, and adjusted-result context match.
- **Assumptions and alternatives:** No unsupported model equivalence beyond the printed match is needed. A transcription/typesetting error or an unstated distinct analysis remains possible; neither location identifies a distinct analysis. The authoritative endpoint requires finalized model output.
- **Pagination and duplicate audit:** Canonical ledger and recheck pagination is correct. Cross-source CP-01's page-6 narrative link is the repairable false pagination recorded above. NCP-001, CP-01, and P1-S008-01 are genuine duplicates of this same printed relationship, not omitted separate candidates.
- **Missing card fields at audit time:** No substantive evidence input is missing from the ledger/recheck. Exact final-report card labels and the blank human-adjudication block remain pending report assembly.
- **Bounded relevance:** If confirmed, an extractor could copy either `8.40%` or `8.10%` as the same upper confidence endpoint. The package does not show that downstream reuse or conclusion change occurred.
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Discharge beta-blocker adjusted point estimates mismatch

- **Evidence-quality checks:** Exact locations and printed values are directly reproduced at [Table 2 — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6) and [Results narrative — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7). Risk-difference point estimates differ by `6.69-6.63=0.06` percentage points and OR point estimates by `1.48-1.47=0.01`; both corresponding intervals are identical. The rounded crude percentages do not explain the adjusted-estimate mismatch.
- **Assumptions and alternatives:** The matched population, contrast, adjusted-result description, and interval endpoints support comparison. Transcription, different internal rounding, or distinct analysis runs remain possible but unestablished. Finalized model output is missing.
- **Pagination and duplicate audit:** All canonical links and pages are correct. CP-02 and P1-S021-01 are genuine duplicates of the same matched-result relationship.
- **Missing card fields at audit time:** No substantive evidence input is missing from the ledger/recheck. Exact final-report card labels and the blank human-adjudication block remain pending report assembly.
- **Bounded relevance:** If confirmed, an extractor could copy nonmatching RD or OR point estimates for the same reported analysis. No downstream reuse or conclusion change is established.
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 1 difference footnote conflicts with the displayed comparison groups

- **Evidence-quality checks:** The source at [Supplement 3 eTable 1 — PDF p. 17](../../../joi170166supp3_prod.pdf#page=17) prints complete-follow-up and missing-follow-up columns but defines the difference as intervention minus control. The arithmetic reproducibly follows missing minus complete: `60.0-60.6=-0.6`, `71.2-75.8=-4.6`, and `42.4-30.8=11.6`. [Main article — PDF p. 6](../../../jama_huffman_2018_oi_170166.pdf#page=6) independently confirms the complete/missing group totals `21,079` and `295`.
- **Assumptions and alternatives:** The label conflict is directly observed. A copied footnote is plausible but inferred; an incorrect title/header is a less-supported alternative. Analysis code is unavailable for CI reconstruction, but no such code is needed to observe the group-label conflict.
- **Pagination and duplicate audit:** All canonical links and pages are correct. NCP-002, CP-03, and P1-S507-01 are genuine duplicates of this relationship. Reword the title to neutral “conflicts with” language; “wrong” reads as a disposition rather than a candidate observation.
- **Missing card fields at audit time:** No substantive evidence input is missing from the ledger/recheck. Exact final-report card labels and the blank human-adjudication block remain pending report assembly.
- **Bounded relevance:** If confirmed, an extractor could assign the displayed differences to intervention-control rather than missing-complete groups. No actual propagation or paper-level conclusion change is established.
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — SAP and article use different component sets under the same outcome name

- **Evidence-quality checks:** [SAP — PDF p. 5](../../../joi170166supp2_prod.pdf#page=5) defines the named composite with aspirin, ADP-receptor antagonist, heparin, statin, and beta blocker. [Main article Methods — PDF p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3) uses the same outcome name for aspirin, ADP-receptor antagonist, anticoagulant, and beta blocker and explicitly says predefined statin data were not collected. [Table 3 — PDF p. 7](../../../jama_huffman_2018_oi_170166.pdf#page=7) reports `3122 (31.7)` and `3878 (35.8)` for the four-component version.
- **Assumptions and alternatives:** The printed component sets differ and the supplied package has no amendment record; that comparison is reproducible. The existing ledger rule overstates an omission because the article directly defines and discloses the revised component set. Whether the disclosure is sufficient, whether a formal amendment exists, and whether `heparin` and `anticoagulant` were operationally coextensive remain human questions.
- **Pagination and duplicate audit:** All links and pages are correct. CP-04 is a distinct source-definition relationship. Pass 2 links it to S032. Preserve CP-04 and explicitly cross-reference N026/N027/S032 in the report; do not manufacture a second candidate from those links.
- **Missing card fields at audit time:** No printed comparator is missing, but the authoritative amendment/change-control record and statin observations are absent. Exact final-report card labels and the blank human-adjudication block remain pending report assembly. The candidate statement/reasoning must receive the narrowing repair recorded above.
- **Bounded relevance:** If confirmed, an extractor could combine a five-component planned composite and a four-component reported composite under one label. The package does not establish actual propagation or a conclusion change.
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Published prespecified age strata do not match the supplied SAP

- **Evidence-quality checks:** [SAP — PDF p. 7](../../../joi170166supp2_prod.pdf#page=7) prints `<65 years and >65 years`. [Main Methods — PDF p. 3](../../../jama_huffman_2018_oi_170166.pdf#page=3) and [Figure 3 — PDF p. 9](../../../jama_huffman_2018_oi_170166.pdf#page=9) call age a prespecified subgroup and display `<50`, `50-69`, and `≥70`. The two-category and three-category schemes do not map one-to-one; `50-69` spans the SAP's 65-year boundary, and the SAP's literal wording does not assign age 65.
- **Assumptions and alternatives:** The printed definition mismatch is direct. A later amendment, another prespecification record, or use of “prespecified” for the variable rather than exact cutpoints is possible but not supplied. No conclusion about intent or validity is made.
- **Pagination and duplicate audit:** All links and pages are correct. CP-05 and P1-S505-01, linked to S505 and S037-S039, are genuine duplicates of one category-definition relationship.
- **Missing card fields at audit time:** No substantive evidence input is missing apart from any nonsupplied amendment/prespecification record. Exact final-report card labels and the blank human-adjudication block remain pending report assembly.
- **Bounded relevance:** If confirmed, an extractor could record the 50/70-year strata as matching the supplied prespecified categories. No actual propagation or conclusion change is established.
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Final completion conditions and bounded limitations

- **Stable-ID identity:** Candidate ledger = evidence recheck = this quality audit = `C001`, `C002`, `C003`, `C004`, `C005`. Final-report identity remains pending because the report has not yet been generated.
- **Human fields:** Every adjudication subfield in this artifact uses the exact blank placeholder `__`. No validity, importance, action, severity, acceptance, rejection, verification disposition, or correction has been assigned.
- **Evidence limitations:** The package lacks raw data, finalized model exports, unrounded estimates, detailed test/variance inputs, analysis code, and amendment/change-control records. Exact graphical values were not inferred where figures lack printed point labels.
- **Runtime limitations:** The base environment lacked Poppler on `PATH`; the fresh preprocessing record documents the locally extracted Poppler runtime. The audit used that direct local runtime for source-page and pagination confirmation. No web or external literature was used.
- **Run remains open:** Report generation, finalized timing, token accounting, source hashes after completion, HTML rendering, link validation, and mechanical validator `PASS` occur after this quality stage. The coordinator must repair the three items above, mark this coverage row complete, add and manifest all later agents, assemble all five report cards without count suppression, and preserve exact ledger/recheck/quality/report ID identity.
