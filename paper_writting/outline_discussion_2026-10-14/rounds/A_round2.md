# Drafter A, round 2

Counts come from `recon.py` and `tab.py` in this scratchpad, which parse the R_A and R_Bulun workbooks with the stdlib. They are LLM-adjudicated, not human, results and are used here only to reconcile definitions.

## 1. Critique of Drafter B

**Where I agree, and what I adopt**
- **Not prevalence.** B is right that a prevalence estimand is not supportable: the sample is non-random, recall is unknown, and the rules were tuned on these papers. I drop the word "prevalence" and relabel my θ₁ (see §3).
- **The 44 are a development cohort.** Accepted (see (c)).
- **Departures table (S1), dated, before or after outputs were seen.** This answers C's protocol challenge directly. Adopted.
- **Reused assets, by year.** My round 1 missed this. The earlier pipeline versions that produced the reused text and OCR assets differ by year (2018: 1.5.2/1.6.1; 2024: 1.5.3; …). Together with the annotated PDFs, this is a second exposure that differs by period. It belongs in the confounder list for the temporal contrast.
- **Dual review limited to the 221 non-protocol candidates, plus a random sample of protocol_report rows.** This is better than my all-440 plan and is what makes 30 October conceivable. Adopted, with *independent* dual review rather than Lin's initiate-then-check, so that reliability can be estimated.
- **Also adopted:** anchoring and incorporation-bias disclosure; "validator PASS is not accuracy"; reviewer burden as an outcome; a stability rerun; no cost-effectiveness claim; evidence cards in a DOI repository (AJE allows 5 supplementary files of ≤2 MB).

**Where I disagree**
1. **PPV should not be primary.** PPV is the quantity the tuning optimized. The screening rules (route B, the display-precision cutoff, "screen out when in doubt about wording") exist to keep reviewers from seeing false positives. In-sample, PPV is the most optimistically biased number we have. It also inherits incorporation bias from reviewers who read the AI card. Leading with it puts the weakest number first. The paper-level proportion with at least one human-confirmed issue is the primary outcome *prespecified in protocol 0630* (L113). Keeping it means one fewer post hoc departure, and C's challenge 3 is about exactly that kind of departure.
2. **The PPV denominator must be fixed by the index test, not the reviewer.** B defines PPV within statistical_results. Reviewers move candidates between domains (5 domain-only disagreements; the "E changed" column is nonzero in every year except 2018). A denominator defined by the reviewer's domain therefore depends on the outcome. Define the denominator by the **pipeline-assigned domain** (219 protocol_report and 221 other, from the v2.4.1 build table) and treat a reviewer's move between domains as a secondary outcome.
3. **The prior is mis-stated.** "Beta(1,1)-equivalent" is ambiguous in a hierarchical logit model. A uniform prior on expit(μ) means μ ~ Logistic(0, 1). State the prior placed on μ and on τ (half-normal(0, 1), logit scale).
4. **Offset.** Use total package pages, not "source units". Source units are produced by the pipeline's own segmentation, so they are part of the index test. Pages are not.
5. **Title.** "for detecting" implies sensitivity. Use "flagging" or "screening for".
6. **Too much space for the workflow.** A 12-gate figure plus a per-role table would cost about 800 of 4,000 words for an epidemiology readership. Keep one schematic and one paragraph of rules; move roles and versioning to the supplement and repository.
7. **LLM as second reader.** Agreed, but only with an audit showing the human reviewers never opened `reviewer_runs/`.

## 2. Responses to C

1. **Recall and prevalence.** Conceded. No recall, no prevalence. "Lower bound" appears only qualitatively in the Discussion.
2. **The 1.6.2 rules are post hoc for 2018–2019.** Conceded, and the problem is broader:
   - the 2024–2025 papers shaped earlier prompts through the pilot;
   - the 2018–2019 papers shaped the 1.6.2 screening rules.

   The tuning exposure therefore differs by period. That is a further reason the temporal contrast is descriptive only.
3. **Departure from protocol 0630.** Conceded. Use Table S1 (from B), and keep 0630's primary outcome (see §1, point 1).
4. **Xu 2022's impact figures.** Conceded. Xu is cited for motivation and for the conceptual bridge: inconsistencies in the source are one plausible mechanism behind Xu's "numerical" and "ambiguous" extraction-error categories. This is stated as a hypothesis. No impact percentages are transferred.
5. **kwag204's injected errors set an expectation of a known-truth component.** Partly accepted. A planted-error substudy cannot be done properly by 30 October:
   - the errors have to be planted in PDFs by someone blind to the runs;
   - rerunning takes 35–131 minutes per package;
   - planted main-text errors may be easier to find than natural ones (La).

   For now, state the absence in the abstract-level limitations and in the Discussion, and say why the designs differ: natural prevalence and PPV here, sensitivity there. Design the planted-error arm for the follow-up held-out study (§3, Future work). Do not offer the LLM-run agreement as a substitute.
6. **Flanagin 2026 and TDM.**
   - Flanagin bars AI on manuscripts *under review*. Position the workflow for author-side checks before submission and for evidence synthesizers after publication, not as a confidential peer-review tool.
   - The JAMA PDFs reserve text and data mining and AI training. Lin's analogy to systematic-review extraction (07-24 transcript, L730) is not a legal opinion. Before submission, ask the UA Libraries copyright office, record the provider's no-training terms, and post only page locators and minimal excerpts.
7. **Further points from C.**
   - Adopt an **errata check** for all 44 papers: cheap, a partial external reference, and it exposes a period confounder (2018–2019 papers have had six or more years to accumulate corrections).
   - C's incidental observations in Goh, Mazor and Graf must not be used. They are unadjudicated, and Graf includes Lin as an author.
   - A Research Letter with LLM adjudication would misrepresent the results just as much as a full article would.

## 3. Revised question, storyline and outline (changes marked ⟳)

### Reconciliations requested

**(a) Primary estimand.** One paper can carry both, in this order:
- **Primary:** per-paper confirmed yield, θ₁ ⟳. This is the proportion of the 44 packages in which the workflow raised ≥1 report-domain candidate that human reviewers confirmed. It is the 0630 primary, relabeled as a property of the tool on this development cohort.
- **Key secondary:** PPV, with the denominator fixed by the pipeline-assigned domain, and the reviewer burden (unconfirmed candidates per paper).
- **Extraction tier:** θ₂, below.

The abstract reports θ₁ and PPV in the same sentence.

**(b) The new field "Can the correct value be determined from the package?" (yes/no).** Cheap for reviewers, who already open the source to judge H; the cost is rebuilding and revalidating the workbook. For the 30 October path ⟳, drop the column:
- make the existing J (downstream impact) **required** for retained statistical_results rows;
- record undeterminable values with a fixed token in R (`VALUE_UNDETERMINABLE`), defined in the SAP amendment before review starts.

θ₂ is then the proportion of papers with ≥1 confirmed issue with J = direct, with the token as a further subset. On the full timeline, promote the token to a proper column.

**(c) Development versus held-out.** The 44 papers are a **development cohort** ⟳, and all estimates are apparent (in-sample). `ExtraPapers/` is **not** a clean held-out set. Its 10 packages were already run under workflows 1.5.1/1.5.2, two have human-adjudication reports (jama.2019.20207, jama.2020.8556), several still lack the main PDF (`MAIN_PAPER_TO_DOWNLOAD.txt`), and its years (2017, 2020) fall outside both periods. A genuinely held-out set would be JAMA RCTs published online first after the 1.6.2 freeze (11 October 2026), run once with the frozen workflow. That set is also free of training-data contamination. It is follow-up work and is not needed by 30 October.

**(d) protocol_report counts.** Each figure answers a different question:

| Definition | n |
|---|---:|
| Pipeline-assigned domain = protocol_report, all candidates (v2.4.1 build table: 55+49+45+70) | **219** (B's figure) |
| R_Bulun final domain = protocol_report, any disposition | 216 |
| R_Bulun retained as protocol_report | **214** (my figure) |
| R_A retained as protocol_report | 209 |
| Retained as protocol_report by both runs | 209 (README); L identical for 180; both substantive_difference for 163 |
| Retained by either run | 214 |

Report 219 as the index-test count, plus the human-retained counts by reviewer and by consensus, with no "error" label. The README's 209/180/163 describe the two LLM runs and stay out of the paper.

**(e) The 30 October deadline.** No human adjudication exists, and the deadline is only "encouraged".
- **Plan A (submit about 30 October):**
  - freeze an SAP amendment on 15–16 October;
  - Bulun and Shiyin independently review the 221 non-protocol candidates (about 5 papers a day each until about 26 October);
  - one reviewer codes the protocol_report rows descriptively, with a 20% random sample double-coded;
  - run the consensus meeting with Lin;
  - submit with the development-cohort framing, no held-out set, no stability rerun, and those analyses listed as limitations and planned work.
- **Go/no-go on 24 October.** If dual review of the 221 is not complete, skip the collection and submit to regular AJE Practice of Epidemiology later. That version can add the held-out post-freeze set, the stability rerun and a small planted-error arm.
- **Under no plan** is LLM adjudication submitted as the reference standard, or as a Research Letter.

### Central question ⟳
When a frozen multi-agent LLM workflow reads complete *JAMA* RCT packages (2018–2019 and 2024–2025), how often does it raise at least one statistical reporting inconsistency that human reviewers confirm? What share of its flags hold up? How many of the confirmed issues affect a value a systematic reviewer would extract?

### Storyline ⟳
Run once per package with page-anchored evidence, the workflow raised a human-confirmed statistical reporting inconsistency in [θ₁] of 44 *JAMA* trial packages, mostly in supplements, at a PPV of [ ]. Some of these issues bear directly on extractable effect estimates or counts. Routine checking before submission or before extraction is therefore feasible. Recall, and performance outside this development cohort, remain unknown.

### Outline (AJE Practice of Epidemiology, ≤4,000 words)

**Title ⟳.** "Flagging statistical reporting inconsistencies in randomized trial reports in *JAMA* with a multi-agent large language model workflow, 2018–2019 and 2024–2025."

**Introduction.**
1. Supplements feed evidence synthesis and receive little scrutiny.
2. Xu is cited for motivation only ⟳.
3. Prior checkers: La's planted errors and Zhang's arXiv benchmark, both with LLM-judged precision. Note that La's "genuine" rate is dominated by rounding, which our rules screen out ⟳.
4. Gap: complete packages including plans, explicit inclusion rules, and human adjudication.

**Methods.**
- Design: meta-epidemiological, tool evaluation on a development cohort ⟳.
- Table S1: departures from 0630 ⟳.
- Eligibility, with online-first dating.
- A sampling-frame statement (still a gap).
- Workflow: one schematic and the inclusion rules; the role table goes to the repository ⟳.
- Run metadata: model, dates, reused-asset provenance by year ⟳.
- Reference standard: independent dual review of the 221 non-protocol candidates, with protocol_report rows coded by one reviewer plus a 20% dual-coded sample ⟳.
  - Reviewers judge from the PDFs before reading the card.
  - Disclose anchoring.
  - Run an audit confirming that no reviewer opened `reviewer_runs/` ⟳.
- Estimands:
  - θ₁ (primary);
  - PPV, with the index-test denominator ⟳, and its sensitivity analysis counting probable as confirmed;
  - reviewer burden ⟳;
  - θ₂, via J = direct plus the token ⟳;
  - location and focus area;
  - κ;
  - reviewer minutes;
  - protocol_report described by element, with no verdict.
- Statistical analysis:
  - Clopper–Pearson intervals for θ₁ and θ₂;
  - paper-cluster bootstrap (2,000 resamples, stated seed) or GEE for PPV and κ;
  - an optional Bayesian hierarchical logit with priors stated on μ and τ ⟳.
- Exploratory period contrast:
  - risk difference (Newcombe interval) and negative binomial with a page offset;
  - permutation in the supplement;
  - confounders listed: plan availability, package length, reused assets, annotations, tuning exposure and time available for errata ⟳.
- Sensitivity analyses: exclude the 5 annotated papers; exclude the online-first boundary papers.
- Errata check ⟳.
- Ethics: TDM and permissions statement ⟳.
- AI disclosure as required by AJE and Flanagin.

**Results.**
- Fig 1: the funnel (789 checker findings [B's `run_meta.py`] → 215 screened out by reason → 440 candidates by pipeline domain → human dispositions) ⟳.
- Table 1: packages by period.
- Table 2: candidate-level adjudication with PPV and burden.
- Table 3: θ₁, θ₂ and the substantive tier, overall and exploratory by period.
- Table 4: focus area × location.
- Fig 2: paper-level dot plot.
- Box: 3–4 examples showing the extraction consequence.
- Protocol–report subsection with Table S-PR.
- Supplement: errata and κ ⟳.

**Discussion.**
- Yield and PPV on a development cohort, with recall unknown.
- What these issues mean for extractors.
- Why this design and planted-error designs answer different questions ⟳.
- Where the tool fits under Flanagin's confidentiality rule ⟳.
- Limitations.
- Future work: a frozen held-out set from after 11 October, a stability rerun and a planted-error arm ⟳.
