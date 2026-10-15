# Consolidated draft v3 (Drafter A; integrates B round 2, C dispute 1, and the user's exploratory-tool framing)

**Status, 14 October 2026.** No human verification of any flag exists yet. Every workbook number below comes from two Claude Opus 5.5 runs (R_A, R_Bulun), is provisional, and is used only for planning. **Correction:** R_Bulun retained 413/440 candidates (27 excluded), not 422 (B is right; `tab.py`: 107+76+107+123).

## 0. How the exploratory-tool framing changed this draft

The workflow is now an **exploratory screening aid** that surfaces candidates for human verification, not a confirmatory error detector or validated instrument; the study is **exploratory and descriptive**. Changes:
1. **Outcomes:** the primary/secondary hierarchy becomes labeled sets: prespecified descriptive outcomes from protocol 0630 (30 June) and later-added outcomes, each dated and marked as added before or after outputs were seen (§2).
2. **θ₁ vs θ₂:** the formal switching problem eases, the headline-emphasis problem sharpens, and a reporting rule handles both (§2).
3. **Vocabulary (Table 0):** "PPV" becomes the **confirmation proportion** (the PPV analogue against human verification, for these reviewers and rules only); "reference standard/index test" become **human verification/workflow**; errata become a **correspondence description**, not recall.
4. **Further work sorted:** held-out cohort, planted errors, single-prompt baseline, recall and stability move to an agenda for *future confirmatory work*; the paper keeps what an honest description of the aid needs (§3).
5. **New Discussion section on intended use:** who runs the aid, when, and what a flag does and does not license.
6. **Unchanged:** human verification of every non-protocol flag; an exploratory tool paper must still report the share of flags humans confirmed.

**Table 0. Language check** (applies to the manuscript, figure labels and the repository README)

| Avoid | Use instead |
|---|---|
| detect, detection, detector | surface, flag |
| validate / validation (of the tool or of papers); "AI paper validation" | human verification of flags; do not use the project name in the manuscript |
| accuracy, performance, sensitivity, recall, specificity | confirmation proportion, yield, reviewer burden; recall **not assessed** |
| audit (of papers or journals) | screening of reports; review |
| reference standard, index test, gold standard | human verification; workflow |
| error, mistake (for a flag) | candidate; confirmed inconsistency |
| "the tool found errors in X% of JAMA trials" | "human reviewers confirmed ≥1 flagged inconsistency in k of 44 packages" |

Protocol 0630 itself is titled "AI-Assisted *Detection* … : A Pilot Cross-Sectional *Study*" and calls the design an *audit*. Table S1 records this change of vocabulary as a departure.

## 1. Central question, storyline, title

**Question.** Used as an exploratory screening aid on complete *JAMA* RCT packages (article, supplements, protocol, SAP), what does a frozen multi-agent LLM workflow (1.6.2) surface; what share of its flags do two human reviewers confirm, and in how many packages; how often does a confirmed inconsistency leave an extractable value undeterminable from the package; and what does verification cost reviewers?

**Storyline (one sentence).** Extraction-validity studies treat the trial report as correct; run as an exploratory screening aid on 44 *JAMA* RCT packages, a multi-agent LLM workflow surfaced [n] candidates per package, of which human reviewers confirmed [c]% (in [k₁]/44 packages, [k₁ₛ] substantive), with [k₂]/44 packages containing a confirmed inconsistency that left an extractable value undeterminable from the package, at about [t] reviewer minutes per package, while whether it misses inconsistencies was not assessed.

**Title options** (a subtitle is used only where it names the design):
1. Screening randomized trial reports in *JAMA* for extraction-relevant reporting inconsistencies with a multi-agent large language model workflow, 2018–2019 and 2024–2025: an exploratory meta-epidemiological study
2. Human-verified reporting inconsistencies surfaced by a large language model screening aid in randomized trial reports in *JAMA*, 2018–2019 and 2024–2025

## 2. Outcomes (exploratory and descriptive)

**Definitions.**
- *Report-domain flag.* A flag the pipeline assigned to statistical_results (175) or report_internal_inconsistency (9): **184** in total. The remaining 256 are plan_material (37) and protocol_report (219) (v2.4.1 build table).
- *Confirmed.* Retained at human consensus with H = confirmed_issue, or K ∈ {substantive_inconsistency, minor_presentation}. A variant also counts probable_issue.
- *Substantive.* I = substantive or K = substantive_inconsistency. This is the nearest Codebook analogue of 0630's "Confirmed Major Issue". The mapping is imperfect and is stated as such.

**Intervals.** 95% intervals throughout. With an undocumented selection of 44 packages, they describe stochastic uncertainty for packages like these, not inference to *JAMA* RCTs generally; the Methods say so.

| Set | Outcome | Unit | Denominator | Interval |
|---|---|---|---|---|
| **A. Prespecified descriptive (0630)** | θ₁: packages with ≥1 confirmed report-domain inconsistency, always shown with θ₁ₛ (≥1 substantive; 0630 Major/Minor, L95–105) | Package | 44 | Clopper–Pearson |
| A | Confirmed inconsistencies per package; distribution by category, location and substantiveness (0630 secondary) | Package / flag | 44 / confirmed set | Median (IQR); cluster bootstrap for means |
| A | Confirmation proportion: report-domain flags confirmed in either report domain (0630's "PPV of LLM flags"); variant counting probable | Flag | 184 (pipeline-assigned) | Paper-cluster percentile bootstrap (2,000 resamples, seed 20261030); GEE check |
| A | Review time per package (0630 feasibility objective) | Package | 44 | Median (IQR) |
| **B. Added later (dated amendment, frozen before human verification)** | θ₂: packages with ≥1 confirmed inconsistency whose value is "only determinable externally" or "not determinable" (3-level field). *Conceived after LLM-run outputs were seen.* | Package | 44 | Clopper–Pearson; κ for the field |
| B | Unconfirmed flags per package (reviewer burden) | Package | 44 | Median (IQR) |
| B | Confirmed inconsistencies per 100 pages, main article vs results supplements | Document role within package | Pages | Poisson GLMM rate ratio (paper intercept, log-pages offset) |
| B | Inter-reviewer κ (disposition, issue status, determinability); external statistician vs consensus, if recruited | Flag | Dual-reviewed set | Paper-cluster bootstrap |
| B | Correspondence with published *JAMA* corrections: which corrected items in the ingested versions had been flagged. Descriptive only; **not recall** | Erratum item | s (likely small) | Counts; Clopper–Pearson if s permits |
| **C. Descriptive** | protocol_report flags by plan element, the optional L field, and disclosure. No verdict and no confirmation proportion | Flag | 219 pipeline-assigned; human-final also given | Counts |
| C | Screening funnel (789 → 215 screened out → 440); pipeline vs human domain; runtime | Finding / package | — | Counts; proportions with bootstrap |
| **D. Exploratory contrast (added July–August)** | 2018–2019 vs 2024–2025 for θ₁, θ₁ₛ, θ₂ and confirmed counts per package. Reported only after clean reruns | Package | 19 vs 25 | Newcombe RD; NB rate ratio with log-pages offset; permutation P in the supplement only |

**θ₁ vs θ₂ under the exploratory framing.**
- *What eases.* No single outcome carries a confirmatory inference, so adding θ₂ is not switching a primary endpoint. In exploratory work it is defensible if it is labeled "added", dated, and defined before any person verifies a flag.
- *What sharpens.* Without a hierarchy, the *headline* becomes the place where selective emphasis happens. θ₂ was conceived after the LLM runs showed θ₁ near its ceiling: in the non-human R_Bulun run, 38/44 packages had ≥1 confirmed statistical row (`tab.py`). Leading with θ₂ alone would be selection by appearance.
- *Rule.* The abstract and first Results paragraph report θ₁ with θ₁ₛ and θ₂ **together**, each labeled (prespecified / added). The Discussion may center θ₂. The Methods give the date θ₂ was added and why.

This removes most of the disagreement with C (§5.1).

**Bayesian option (supplement).** Hierarchical logit, μ ~ Logistic(0, 1) (median-package logit), τ ~ Half-Normal(0, 1); marginal mean from posterior draws; 95% credible intervals.

## 3. IMRaD outline (AJE Practice of Epidemiology, ≤4,000 words, 200-word unstructured abstract)

**Abstract.**
- Years, journal and design: exploratory meta-epidemiological study.
- The workflow, described as a screening aid.
- Human verification.
- θ₁/θ₁ₛ and θ₂, labeled.
- The confirmation proportion and the burden.
- "Missed inconsistencies were not assessed."

**Introduction (≈500 words).**
- **P1.**
  - Extraction errors are frequent in adverse-event systematic reviews and can change pooled results; state the scope [Xu 2022].
  - Xu's error definition treats the trial report as correct and attributes some ambiguity to poor reporting [Xu 2022].
  - Inconsistencies inside a report therefore sit upstream of extraction (our argument).
- **P2.**
  - Statistical reporting inconsistencies are common [citation needed].
  - Supplements receive less scrutiny [citation needed; Lin's view is not citable].
  - Protocol/SAP–publication discrepancies are common [citation needed: outcome switching].
  - Deterministic checkers exist [citation needed: statcheck; GRIM].
- **P3.**
  - LLMs flag planted inconsistencies, and a manual check of their other flags on natural text judged most genuine, largely rounding [La 2026].
  - Reasoning LLMs recover stated critical errors in about half of withdrawn preprints (workshop preprint; LLM-judged) [Zhang 2025].
  - Both used a single prompt on the main document [La 2026; Zhang 2025].
  - The gap is *not* "first to verify every flag".
- **P4.**
  - Among studies identified [documented search still to be done], none applied an LLM screening aid to complete RCT packages including plans, or asked whether confirmed inconsistencies leave extractable values undeterminable.
  - Aim: to describe, exploratorily, what such an aid surfaces and what human verification of its flags shows.

**Methods (≈1,500 words).**
1. **Design.** Exploratory, descriptive meta-epidemiological study [citation needed: the reporting guideline Lin cited]. Table S1 dates each departure from 0630 (years, protocol_report domain, cap, workflow versions, removal of 14231, Codebook, set-B outcomes, vocabulary), before or after outputs were seen.
2. **Eligibility and selection.**
   - *JAMA* primary RCT reports by online-first year.
   - The selection rule (the gap still to be filled).
   - Observational paper excluded.
   - Figure 1A.
3. **Packages.**
   - Documents supplied; missing or post-dated plans; unusable text layers.
   - Annotated PDFs replaced and rerun.
   - Pages by role.
4. **The screening aid** (Figure 2 in the main text; role table in the supplement).
   - Frozen 1.6.2 with hashes; `gpt-6.1-sol`; effort by role; run dates; one run per package.
   - Inclusion rule: routes A and B, the display-precision rule, reason codes, one candidate per issue, no cap.
   - Year-specific provenance of the reused assets.
   - The validator checks structure, not correctness.
   - The tool's design history: the 44 packages informed its development, so they are not an independent test set.
5. **Human verification.**
   - Bulun and Shiyin each independently verify all 221 non-protocol flags.
   - protocol_report flags are coded by one reviewer, crossed over periods, with a random 20% double-coded.
   - Calibration on 2 ExtraPapers packages, which are not analysed.
   - Order of work: title and locations, then source, then card. Anchoring is disclosed.
   - Consensus with Lin.
   - An external statistician reviews 5 random packages if one is recruited.
   - A file-access check confirms no reviewer opened `reviewer_runs/`.
   - Minutes are logged.
   - The rebuilt Codebook makes J required and adds the determinability field.
6. **Correspondence with corrections.** Search *JAMA* correction notices, check whether each ingested PDF predates its correction, and match items to flags.
7. **Analysis.**
   - As in §2. R with `sessionInfo()` and stated seeds.
   - Scripts tested on mock data before unblinding.
   - Sensitivity analyses: probable counted as confirmed; reviewer-final denominator; boundary papers (jama.2017.21906, jama.2024.24764, jama.2024.27643); annotated vs clean runs.
8. **Ethics, permissions, AI disclosure.** No human participants; text-and-data-mining basis (UA Libraries opinion) and provider data-use terms; no PDF redistributed; AI use disclosed as AJE requires and Flanagin 2026 describes.

**Results (≈1,200 words).**
- **Figure 1.** A) Paper flow. B) Funnel from findings, through screened-out reasons and flags by domain, to human dispositions.
- **Table 1.** Packages by period.
- **Table 2.** Report-domain flags: disposition, H × I, K, determinability and J, and the confirmation proportion with its interval. plan_material is shown separately.
- **Table 3.** θ₁/θ₁ₛ and θ₂ (labeled prespecified or added), overall, and exploratory by period.
- **Table 4.** Confirmed inconsistencies by focus area × location, as rates per 100 pages.
- **Figure 3.** Package-level dot plot of confirmed and unconfirmed flags against pages.
- **Box 1.** 3–4 neutral examples of undeterminable values.
- **Short subsections:**
  - correspondence with corrections;
  - protocol–report differences (descriptive; Table S-PR);
  - agreement between reviewers.

**Discussion (≈800 words).**
1. **Principal findings** in screening-aid terms: what was surfaced and what humans confirmed, θ₂ emphasized, with no performance claim.
2. **Intended use (new).**
   - *Who and when:*
     - authors, on their own final manuscript and supplements before submission;
     - systematic reviewers and data extractors, on included trial reports at the extraction stage.
     - Editorial use on confidential submissions is outside what we tested and is constrained by Flanagin's confidentiality rule, unless the model is deployed under terms that allow it.
   - *What a flag licenses:* a pointer to a location and a stated rule that did not reconcile, prompting a person to check the source.
   - *What a flag does not license:*
     - it does not establish an error, author fault or any effect on conclusions;
     - a protocol_report flag does not establish a protocol violation or selective reporting;
     - **an absence of flags is not evidence of consistency**, because misses were not assessed;
     - flag counts must not be used to rank papers, authors or journals.
   - In practice, a person resolves each flag against the source and, for extraction, records conflicting values and queries authors.
   - No claim that using the aid changes outcomes [Goh 2024; Mazor 2025].
3. **Relation to prior work.** The confirmation proportion is not comparable with La's "genuine" share (La counts rounding; our rules screen it out). What the multi-agent design adds is not assessed.
4. **Limitations.** Misses not assessed; rules tuned on these papers; selection; verifiers who are also developers, anchoring; one model, one run; year-specific reused assets; possible training-data exposure; an underpowered, confounded period contrast (half-width ≈0.30 for a risk difference near 0.5; R `qnorm(.975)*sqrt(.25/19+.25/25)`).
5. **Before any confirmatory use (new).** A confirmatory study would need: a frozen workflow and model with a prespecified endpoint and sample size; held-out packages; known-truth recall (planted inconsistencies stratified by type and location, plus natural corrected errors); comparators (single-prompt LLM, deterministic checkers, human-only review); run and cross-model stability; verifiers independent of development; recorded cost; and eventually a user study of whether use changes outcomes.

**Sorting the disputed items under this framing.**

| Item | Exploratory paper? | Reason |
|---|---|---|
| Human verification of all 221 non-protocol flags, with κ | **Required** | The confirmation proportion is the minimum honest description of a screening aid |
| Documented selection rule; clean reruns of the annotated packages | **Required** (reruns only if the period contrast is kept) | Describing what was screened; differential contamination by period |
| Correspondence with corrections | Include, as description | Cheap; shows overlap with known issues, not recall |
| Small stability rerun (2 extra runs on about 6 packages) | Desirable, if time allows | Users of an aid need to know whether flags recur. It is not a performance claim |
| Planted-error substudy; held-out cohort; single-prompt baseline; recall | **Future confirmatory work** | Each supports a performance or comparative claim that this paper does not make |

**Supplement (≤5 files, ≤2 MB each) and repository.** S1 Methods appendix (Table S1, amendment, Codebook and guide, role table and rules, run metadata, asset provenance); S2 Results tables (per-package results, Table S-PR, funnel by reason, sensitivity analyses, corrections, examples with locators); optional S3 (LLM-run judgments vs human consensus, labeled as two runs of one model). Repository (OSF or Zenodo DOI; anonymized link for review): frozen 1.6.2 code and configuration with hashes, a README stating intended use and the "absence of flags" warning, per-package reports (excerpts as permissions allow), human workbooks, R scripts; no PDFs.

## 4. Pre-review actions (D = 30 October; today D−16)

| Date | Action | Owner |
|---|---|---|
| D−16–D−15 | Freeze and commit the amendment: set A/B/C/D outcomes, the θ₂ rule with hypothetical examples, the reporting rule for the headline, analyses, and Table 0 vocabulary. Done before any person opens a flag. | Bulun; Lin approves |
| D−15 | Rebuild the Codebook and blanks (J required, 3-level field); run the validators; Excel smoke test | Bulun |
| D−15 | Document the selection rule; TDM query to UA Libraries; Lin asks the editors about late submission and approaches an external statistician | Bulun; Lin |
| D−15–D−13 | Clean reruns of 2024.2302, 2024.4183, 2025.4390, 2025.7710 and 2025.11178; rebuild their blanks. Verification starts on the other 39 | Bulun |
| D−14 | Calibration on 2 ExtraPapers packages | Bulun, Shiyin |
| D−14–D−5 | Independent dual verification of the 221 non-protocol flags; protocol_report coding with 20% overlap; minutes logged | Bulun, Shiyin |
| D−14–D−10 | Corrections search and version check; optional stability reruns | Bulun or agent |
| D−12–D−6 | R scripts on mock data; draft the Introduction and Methods | Bulun |
| **D−4** | **Consensus with Lin; go/no-go** | All |
| D−4–D−1 | Analysis; Results and Discussion; Lin's review; AI disclosure | All |

**Go/no-go (26 October).** Submit only if all of the following hold:
1. dual verification and consensus are complete for all non-protocol flags;
2. the commit history shows the amendment predates the first human judgment;
3. the selection rule is documented;
4. a permissions position exists;
5. either the clean reruns are done or the period contrast is dropped.

Otherwise, ask for a late slot, or submit to the regular track as soon as verification is complete. Under the exploratory framing, that later version does **not** wait for planted errors, a held-out set or a baseline. LLM-run judgments are never presented as human verification. Workload (my extrapolation): about 20–40 hours per reviewer.

## 5. Unresolved disagreements
1. **Headline (A vs C; mostly resolved).** C: θ₂ should lead; θ₁ near 1 reads as an error rate. A: θ₂ may be featured, but reported with θ₁/θ₁ₛ and labeled "added"; leading with it alone is selective emphasis.
2. **Confirmation-proportion denominator (A vs B).** B: the human-final domain is the truth. A: a reviewer-set denominator depends on the outcome; use the pipeline domain, with confirmation in either report domain, and put B's version in the sensitivity analyses.
3. **Held-out set and planted errors (A vs B).** B: a seeded held-out set gives category sensitivity cheaply. A: that supports a performance claim this paper does not make, so it is future confirmatory work; ExtraPapers (1.5.x outputs, two human reports) is at best a temporal-external check.
4. **Single-prompt baseline (A vs C).** C: AJE will attack its absence first. A: the paper claims nothing about the architecture and says so; the baseline belongs in confirmatory work. C may still judge the reviewer risk too high.
5. **Corrections (A vs C).** C: they give natural known-truth recall. A: corrected PDFs hide the errors and the items are few, so report correspondence only.
6. **Timing (A, B vs C).** C: do not count on 30 October. A and B: a full exploratory article is honest if go/no-go holds; otherwise wait for verification only, not for confirmatory add-ons.
7. **Period contrast (B vs A, C).** B: excluding annotated papers suffices. A and C: clean reruns are a precondition, or the contrast is dropped.
8. **External statistician (C vs A).** C: needed for independence. A: desirable; if none by 20 October, a limitation rather than a blocker.
