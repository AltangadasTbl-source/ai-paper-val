# Independent inclusion screen — statistical pass 2

Fresh runtime agent: `root/inclusion_pass2`; role `qc162_inclusion_screener`; model `gpt-6.1-sol`; reasoning effort `high`. Exact assigned finding scope: **F-ST2-601 only**, in `checkers/statistical_parts/pass2_plan_methods.md`, with the independent corroborating reconsideration in `checkers/statistical_parts/pass2_main.md`, prior-exclusion row 73. The current ledger and initial screen were used solely to assess duplication and current-run classification. No legacy scientific conclusions, external evidence, or web sources were consulted.

The scope document and review contract were read completely. This is an independent source-grounded decision, without a target count. The coordinator owns the canonical screening table and candidate IDs; the row below is ready to append there.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-601 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C019 |

**One-sentence justification:** F-ST2-601 is reproduced and qualifies by **Route B** because the supplied plans state different primary final-analysis decision branches after overall efficacy failure, the later SAP retains final subgroup-selection language without expressly reconciling that branch, and this changes the adaptive primary rejection rule a reader would extract even though the trial stopped before the final stage.

Counts: 1 finding screened; 1 included distinct issue; 0 screened-out findings; screened-out reason-code counts are all zero. Candidate status after coordinator registration remains **Pending Human Adjudication**.

## F-ST2-601 — Source-grounded independent assessment

### Exact locations and roles

Every compared document is **PLAN** by content: prospective primary statistical design and decision rules, with separately disclosed trial chronology in the SAP.

- PLAN [protocol p.48, final-analysis scenario 1, steps 2, 2.1 and 2.2](../../../joi240006supp2_prod_1708623114.99233.pdf#page=48): at final analysis after continued overall-population enrollment, failure to cross the overall efficacy bound leads to selecting and testing an optimal subgroup; crossing its efficacy bound permits declaring efficacy in that subgroup.
- PLAN [trial SAP p.10, final-stage paragraph and numbered conclusions](../../../joi240006supp3_prod_1708623114.99733.pdf#page=10): final testing is in either the overall population or a selected subgroup, following the two enrollment scenarios; failure to cross the efficacy boundary leads to a declaration of no superiority to standard medical management.
- PLAN [trial SAP p.9, subgroup-selection paragraph and section 7.2](../../../joi240006supp3_prod_1708623114.99733.pdf#page=9): selection of a most promising subgroup is still described at interim **or final** analysis; two planned interim looks are 200 and 380 completed participants, with a maximum 560.
- PLAN [protocol p.45](../../../joi240006supp2_prod_1708623114.99233.pdf#page=45), [p.46](../../../joi240006supp2_prod_1708623114.99233.pdf#page=46), [p.47](../../../joi240006supp2_prod_1708623114.99233.pdf#page=47), and [p.49](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49) establish the same primary 90-day mRS adaptive framework, subgroup-selection rationale, planned looks and simulation context. They do not provide a statement that the final rescue branch was removed.
- PLAN [protocol appendix p.81](../../../joi240006supp2_prod_1708623114.99233.pdf#page=81) and [trial SAP appendix p.40](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40) both state the final overall efficacy threshold and the same setting: maximum 560, interim 200/380, final boundary c = 2.772. This shared threshold does not itself specify what to do after its non-crossing.
- PLAN [protocol p.1](../../../joi240006supp2_prod_1708623114.99233.pdf#page=1) and repeated page headers identify August 4, 2021; [trial SAP p.2](../../../joi240006supp3_prod_1708623114.99733.pdf#page=2) identifies version 1.0.0 dated November 20, 2022 and says the plan was reviewed and approved before data lock.
- PLAN [trial SAP p.12, section 7.5](../../../joi240006supp3_prod_1708623114.99733.pdf#page=12) explicitly discloses a review after 300 completed 90-day outcomes, a decision to provide the data without altering the study design or adding interim analyses, and early stopping after the DSMB's efficacy recommendation. This is applicability and lineage context, not an observed final-stage result.

The principal protocol p.48 and SAP p.10 readings were confirmed visually against exact-source page images. Protocol pp.45–49 were also reread by fresh direct layout extraction from the supplied PDF; neither checker transcription was final authority.

### Reproduced discrete-rule comparison

Hold the printed scenario fixed: enrollment remains in the overall population, the final stage is reached, and the overall efficacy bound is not crossed.

| Decision-tree input or consequence | August 2021 protocol p.48 | November 2022 SAP p.10 |
|---|---|---|
| Population reaching final stage | Overall population in scenario 1 | Overall population in scenario 1 |
| Overall final efficacy boundary not crossed | Select optimal subgroup and test its null | Declare EVT not superior to standard medical management |
| New selected subgroup crosses its efficacy boundary | Declare efficacy in that subgroup | No subsequent rescue branch stated after the terminal non-superiority conclusion |
| Selected subgroup does not cross its efficacy boundary | Declare no benefit | The terminal non-superiority conclusion already applies to failed final testing |

The discrepancy is not the omission of an implementation detail alone: the protocol states a further test with a possible subgroup efficacy declaration, while the later SAP states a terminal conclusion for the matched failure branch. SAP p.9 additionally retains selection at final analysis, so its p.10 conclusion does not immediately show whether final rescue was removed or compressed into the preceding description.

**Display precision:** This is a categorical branch and conclusion comparison. Half-unit intervals and a relative numeric discrepancy are not applicable; none is fabricated. The shared numeric boundary 2.772 reconciles between appendices and is not registered as a numeric discrepancy. No observed Z, subgroup effect, final-stage P value, attained sample of 560, alpha inflation, or actual final inferential consequence is inferred.

### Comparison tiers and qualifying route

**Comparison tier:** A primary decision rule within supplied plan material is expressly a qualifying comparison in the scope. It is not a peripheral simulation-output comparison, a recruitment calendar, or an administrative plan detail. Its potential consequence is a different permitted primary efficacy conclusion for the same final branch.

**Route A:** No always-register category is needed or claimed. This is a plan-internal primary decision-rule discrepancy, rather than a paired interval/test conflict, count discrepancy, or a claim that an executed planned primary analysis was omitted.

**Route B:** All three criteria are met.

- **B1, in focus:** Focus area D, prospective primary adaptive statistical design and final decision rules; review domain `plan_material`.
- **B2, unresolved by immediate context:** A later approved SAP is a plausible amendment or superseding description, but its date and approval do not identify whether final subgroup rescue was intentionally removed, retained through shorthand, or subsumed in the stated selection/testing. The retained final-selection statement on SAP p.9 and the terminal statement on p.10 prevent identifying one coherent branch at once. Protocol p.48 and its own appendix p.81 also differ in explicitness about that branch. The supplied excerpts contain no operative mapping that reconciles these readings.
- **B3, interpretation/extraction:** The affected extracted value is the **final primary adaptive rejection-tree specification**, specifically whether final overall failure still permits a selected-subgroup efficacy declaration. This is a named part of the primary 90-day mRS design underlying the plans' adaptive decision framework and reported design description. The unexecuted branch limits its connection to an observed outcome; it does not turn a differing planned decision rule into a peripheral detail under the explicit scope tier.

### Context, alternatives and boundaries

1. The later SAP may deliberately replace the protocol's rescue branch. Its approval and later date support this as an alternative, not a confirmed amendment that identifies the branch change. The SAP retains final-selection terminology and describes providing the 300-outcome review without altering design; those printed facts do not state that final rescue was removed.
2. The SAP's concise final-stage paragraph may be intended to incorporate selection/testing before its two terminal conclusions, including the protocol's rescue branch. That reading requires a rule not made explicit in the matched scenario; it remains a human question.
3. The common appendix description may summarize only the overall rejection condition and leave the subgroup branch elsewhere. Absence from the appendix alone is not the finding; the explicit terminal declaration versus explicit rescue branch is the finding.
4. SAP p.12 discloses early stopping. The final branch was therefore not reached in the disclosed chronology. No actual disagreement between final observed decisions, or alteration of the reported early-stop estimate, is claimed. The included issue concerns extracting the planned primary adaptive rule.

### Classification recommendations

- **Review domain:** `plan_material`.
- **Relationship type:** `P_P`.
- **All relationships:** `P_P` only.
- **Compared document roles:** PLAN protocol p.48 versus PLAN trial SAP p.10, with PLAN SAP p.9 and the two PLAN appendices supplying internal context.
- **Classification rationale:** The conflict concerns primary prospective decision rules in plan materials. No REPORT location is a conflicting side and no `P_R` relationship is added merely because the design supports a report.
- **Classification ambiguity:** Differing dates and a later approved SAP may indicate an intentional change of rule; the supplied descriptions do not explicitly establish that lineage. Also, `plan_material` normally concerns an element the reported analysis relies on: here the supported connection is the named adaptive primary decision framework and its specification, not execution of this final branch. That applicability limit must stay visible in the eventual card.
- **Evidence state recommendation for subsequent recheck:** The independent screen reproduces the stated source comparison; the fresh mechanical rechecker retains responsibility for assigning the registered evidence state.

### Duplication check and remaining human question

This is distinct from **C014**, which asks how the disclosed 300-outcome efficacy stop maps to the retained planned 200/380 interim schedule. C014 is about the timing and boundary mapping of an executed interim review; F-ST2-601 is about whether an unexecuted final overall-failure branch permits new subgroup rescue. Their decision-tree conditions and needed definitions differ. It is also distinct from **C013**, which concerns the direction of the raw-score alternative probability, and from **C010**, which concerns outcome hierarchy. No current included issue describes this same final rescue/terminal branch pattern. The two pass-2 reviewers' descriptions refer to this one F-ST2-601 issue and need no separate registration.

**Exact remaining human question:** Which final primary rejection tree was operative after failure to cross the overall efficacy boundary—termination with no superiority, or selection and testing of an optimal subgroup—and which supplied amendment or explicit rule reconciles the protocol and SAP descriptions?

## Direct-source inspection and derivative provenance

Compute device: **CPU**. Recorded direct engine: **Poppler 26.01.0**. No OCR or fallback environment was required. No source or reused artifact was modified.

Fresh artifacts owned by this agent:

- `preprocessing/inclusion_pass2/protocol-p48.png`: protocol PDF p.48, Poppler `pdftoppm` 26.01.0, PNG at 120 dpi, CPU. Command: `pdftoppm -f 48 -l 48 -r 120 -singlefile -png joi240006supp2_prod_1708623114.99233.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_pass2/protocol-p48`.
- `preprocessing/inclusion_pass2/protocol-layout.txt`: complete supplied protocol PDF pp.1–82, direct Poppler `pdftotext` 26.01.0 layout extraction, CPU. Command: `pdftotext -layout joi240006supp2_prod_1708623114.99233.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_pass2/protocol-layout.txt`. Full extraction was used to locate version/amendment language; scientific comparison remains bounded to the cited primary-rule pages.

Direct transient commands also used: `pdftotext -layout -f 45 -l 49 joi240006supp2_prod_1708623114.99233.pdf -` and `pdftotext -layout -f 81 -l 81 joi240006supp2_prod_1708623114.99233.pdf -`.

Exact-source images inspected without modification: current-run `preprocessing/inclusion_initial/sap-p9.png`, `sap-p12.png`, `sap-p40.png`; current-run `preprocessing/support_protocol/page-81.png`; reusable `.ai_paper_validation/review_1_5_3/preprocessing/support_mapper_fresh/DOC-004/pages/page-10.png` and `page-02.png`. Current-run engine provenance remains in the evidence-asset inventory and producing artifacts; the reusable images' original engine version is not inferred. Document identity and page correspondence are grounded in the current source inventory and unchanged source/reused-asset hashes.

Scientific coverage limitations: None for the one assigned finding. The absence of an operative amendment/branch mapping and the unexecuted final stage are stated interpretive limits, not uninspected source locations.
