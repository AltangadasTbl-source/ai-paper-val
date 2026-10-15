# v5 (final): a publicly released LLM screening workflow and its exploratory first application to JAMA RCT packages

Sources: v4, C_final.md and B_final.md. No flag has been verified by a person. Workbook figures come from two Claude Opus 5.5 runs and are used for planning only. Pipeline figures (789 findings, 215 screened out, 440 flags, runtimes, 14/44 runs with GPU OCR on request, Pandoc 3.7.0.2/3.1.11.1/3.1.3) were checked against the run records.

## 0. Framing and fixed wording rules

The core contribution is a **formalized, publicly released, human-in-the-loop multi-agent workflow** for flagging internal reporting inconsistencies in complete randomized trial packages. Its first application to 44 *JAMA* RCT packages is a **descriptive, exploratory characterization**, and the extraction-relevant yield is that application's payoff. The workflow is a **screening aid**: it is not a confirmatory detector and not a validated instrument. The design label is **"development and exploratory application of a screening workflow"**.

**Sentences the paper must carry** (substance fixed): **M1** every candidate needs human verification; an unverified one is not evidence of an inconsistency. **M2** only flagged candidates were reviewed, so misses were not assessed; no flag does not mean consistent. **M3** the share of packages with ≥1 confirmed issue is the yield of a human-verified screening process on 44 selected packages, not a prevalence. **M4** θ₁ and the confirmed share were prespecified (30 June 2026); all other outcomes, the protocol_report domain, the 2018–2019 cohorts, the outcome reordering and the vocabulary change came later (Table S1, dated). **M5** rules were revised after seeing 2018–2019 output, and earlier prompts were shaped by the 2024–2025 pilot, so results are in-sample. **M6** one reviewer developed the workflow; both saw its cards. **M7** a flag prompts resolving the value from report, registry or authors; it is not a corrected value. **M8** no single-prompt comparison; what the multi-agent design adds was not tested. **M9** model, version, dates; any LLM-run judgments labeled as two runs of one model.

**Terms the paper must not use.** N1 "detected errors", "error rate", "accuracy". N2 "useful", "effective", "reliable", "saves time" (permitted: "may help locate values that need checking; not evaluated"). N3 "validated", except "has not been validated". N4 any directional or causal reading of the period contrast. N5 "prevalence", including "lower bound". N6 editors running it on submitted manuscripts. N7 "exploratory" as grounds to omit intervals, present LLM-adjudicated numbers or add undated outcomes.

**"Replicable."** The paper may say "replicable" only if both conditions below hold. Otherwise it says **"formalized and publicly released"**.
1. *Procedural replicability* requires a successful second-operator run from the README plus published hashes of the control files.
2. *Output agreement* may be stated only as the measured overlap on k packages under one model ID and one Codex version.

## 1. Question, storyline, titles

**Questions.** A frozen multi-agent LLM workflow (1.6.2) is used as an exploratory screening aid on complete *JAMA* RCT packages (article, supplements, protocol, SAP). We ask:
1. What does it hand to human verifiers?
2. How much of it survives verification, and at what reviewer cost?
3. How often does a confirmed issue leave a value that a systematic reviewer would extract undeterminable from the package?

The aim of specifying the procedure is stated in the Introduction, P5.

**Storyline (one sentence).** We specify and publicly release a versioned, human-in-the-loop multi-agent LLM workflow for flagging internal reporting inconsistencies in randomized trial packages; used as a screening aid on 44 *JAMA* RCT packages, it raised [N] candidates, of which two reviewers confirmed [n] (about [1/p] flags reviewed per confirmed issue; [t] reviewer minutes per package), including confirmed issues in [k₂] packages that left a value a systematic reviewer would extract undeterminable from the package, while what it misses was not assessed.

Brackets: [N] is a pipeline count; [n], [1/p] and [k₂] need complete dual verification; [t] needs the logged minutes.

**Titles** (a subtitle is used only where it names the design):
1. A publicly released multi-agent large language model workflow for flagging internal reporting inconsistencies in randomized trial packages: development and exploratory application to trials in *JAMA*
2. Flagging extraction-relevant reporting inconsistencies in randomized trial packages with a human-in-the-loop large language model workflow: development and exploratory application

## 2. Outcomes (descriptive; prespecified vs added, dated)

**Definitions.**
- **Report-domain flag.** A flag the pipeline assigned to statistical_results (175) or report_internal_inconsistency (9), giving 184 in total. plan_material (37) and protocol_report (219) are reported separately.
- **Confirmed.** Retained at human consensus with H = confirmed_issue, or with K = substantive or minor inconsistency. A variant also counts probable_issue.
- **Substantive.** I = substantive or K = substantive_inconsistency. This is the nearest analogue of the protocol's "Major" category; the mapping is imperfect, and the paper says so.
- **Intervals.** All intervals are 95%. They describe uncertainty for packages like these 44 (selection undocumented), not for *JAMA* RCTs in general.

| Set | Measure | Unit / denominator | Interval |
|---|---|---|---|
| **A. Prespecified (0630)** | Share of report-domain flags confirmed (pipeline-assigned denominator); variant counting probable | Flag / 184 | Paper-cluster bootstrap (2,000 resamples, seed 20261030) |
| A | θ₁: packages with ≥1 confirmed report-domain issue, always shown with θ₁ₛ (≥1 substantive) and M3 | Package / 44 | Clopper–Pearson |
| A | Confirmed issues per package, by category, location and substantiveness; review minutes per package | Package / 44 | Median (IQR); cluster bootstrap |
| **B. Added (dated amendment, frozen before review)** | **θ₂, the extraction payoff:** packages with ≥1 confirmed issue whose value is determinable "only externally" or is "not determinable" (3-level field); distribution of that field | Package / 44; issue | Clopper–Pearson; κ |
| B | Flags reviewed per confirmed issue (1/share); unconfirmed flags per package | Flag; package | Inverted bootstrap interval; median (IQR) |
| B | Confirmed issues per 100 pages, main article vs results supplements | Role within package | Poisson GLMM rate ratio, log-pages offset |
| B | κ (calibration, then main review) for disposition, issue status and determinability | Flag | Paper-cluster bootstrap |
| B | Candidates matching published *JAMA* corrections ("r of s"); not recall | Erratum item | Counts |
| B | Execution: wall-clock time, agents per run, failure modes, tool versions, tokens/cost if recoverable | Run / 44 | Median (range) |
| B | Stability: Jaccard overlap of candidate sets; recovery of confirmed issues; rerun-only candidates reported as **unverified overlap** | Package / 8 | Median (range) |
| **C. Descriptive** | protocol_report flags by plan element, L field and disclosure; no verdict | Flag / 219 | Counts |
| C | Funnel (findings → reason codes → flags → dispositions); pipeline vs human domain | — | Counts |
| **D. Hypothesis-generating (supplement)** | Per-period θ₁, θ₁ₛ, θ₂; Newcombe risk difference. Reported **only if the 5 clean reruns are done**, in a table that also lists the confounders: annotation exposure, reused assets from year-specific pipeline versions, tuning history | Package / 19 vs 25 | Clopper–Pearson; Newcombe |

The abstract leads with the verification yield. Leading with the confirmed share reorders two outcomes that 0630 prespecified. It adds no outcome and happened before any human verification. M4 and Table S1 date the change.

## 3. IMRaD outline (AJE Practice of Epidemiology, ≤4,000 words)

### Abstract (200 words, unstructured)
1. Problem.
2. The workflow and its intended use.
3. The application: 44 packages, the years, plans included.
4. Candidates → confirmed → flags per confirmed issue; minutes per package.
5. θ₁/θ₁ₛ in M3 wording.
6. θ₂.
7. "Misses were not assessed; flags require human verification."

### Introduction (about 450 words)
- **P1, the user.**
  - Data extraction errors in adverse-event systematic reviews are frequent and can change pooled results; state the scope [Xu 2022].
  - Xu's definition of error treats the trial report as correct [Xu 2022].
  - Inconsistencies inside a package therefore sit upstream of extraction (our argument).
- **P2, the problem.** Statistical reporting inconsistencies occur; supplements and plans are long and receive little checking; deterministic checkers cover narrow, formalized patterns [citation needed for each: prevalence of inconsistencies; scrutiny of supplements; statcheck; GRIM/GRIMMER].
- **P3, LLM checkers so far.**
  - Single-prompt LLM checks of manuscripts have reported flags judged genuine, by unspecified manual review [La 2026] or by LLM judges [Zhang 2025].
  - La found most such genuine flags to be rounding discrepancies.
  - Zhang targets critical errors in withdrawn preprints and is a workshop preprint.
  - *JAMA* Network journals require AI use in research to be fully described, with authors responsible for accuracy [Flanagin 2026]. AJE requires AI use to be disclosed in the cover letter and in the Methods or Acknowledgments (AJE author guidelines).
- **P4, the gap** (pending a documented literature search):
  > "Among the studies we identified, large language model checks for internal inconsistencies or critical problems used a single prompt applied to the main manuscript, and only one published its prompts and code [Zhang 2025; La 2026]; we found none that released a multistage agentic workflow with written inclusion rules and source-anchored evidence for complete trial packages, including protocols and statistical analysis plans."

  We do not claim that no templates exist: Zhang publishes prompts and code, and Ruta 2025 a non-agentic prompt template.
- **P5, aim.**
  - Specify, as an inspectable procedure, a workflow for agentic checking of internal consistency, and release it.
  - Characterize its first exploratory application to *JAMA* RCT packages.
  - The extraction-relevant yield is the payoff.

### Methods (about 1,600 words; about half on the workflow)
1. **Intended use** (with M1, M2, M7).
   - Users: statisticians, systematic reviewers and data extractors, and authors checking their own work before submission.
   - Not for: confidential manuscripts under review, misconduct screening, or verdicts on papers (N6).
2. **Workflow specification** (Figure 1).
   - **Inputs and roles.** Document roles REPORT/PLAN; relationship codes P_R, P_P, S_C, S_W; four review domains.
   - **Stages:**
     1. inventory and source hashing;
     2. reuse-asset curator;
     3. main and support mappers;
     4. numeric, cross-source and statistical pass 1 checkers;
     5. inclusion screen;
     6. registration;
     7. evidence recheck;
     8. statistical pass 2;
     9. **second inclusion screen** whenever pass 2 emits findings;
     10. quality-control auditor;
     11. report;
     12. structural validator.
   - **Candidate rules,** presented as design choices:
     - route A: always-register categories;
     - route B: in focus, not resolved by context, and bearing on interpretation *or on which value an extractor would take* (this is where the design encodes the extraction priority);
     - display-precision rule;
     - one candidate per issue; no cap; vocabulary rules.
   - **Human-in-the-loop constraints.** Agents assign no disposition or severity and delete no IDs.
   - **Outputs.** Evidence cards; the screening log, which lets a user audit what was dropped; the ledger; the HTML report.
   - The agent-role table goes in the supplement.
3. **Implementation and release.**
   - Workflow 1.6.2 with one configurable model ID (`gpt-6.1-sol`) and reasoning effort set by role. It runs under the user's own Codex authentication and stores no credentials.
   - Rendering and OCR run on the CPU by default; GPU OCR runs on user request and is recorded per run (14/44).
   - Tool versions differed across runs (e.g., Pandoc 3.7.0.2 vs 3.1.11.1). They are listed per run in Table 1.
   - Control files were **verified post hoc** as byte-identical across all 44 packages and the release (AGENTS.md, scope, contract, settings, validator, a sample preset). These hashes are published; they were not recorded at run time.
   - The README carries M1, M2 and M7 and states that the results are specific to this model. A port to other agent frameworks or as a "skill" is untested.
4. **Human verification.**
   - The v2.4.1 Codebook, rebuilt with J (downstream impact) required and a 3-level determinability field.
   - Reviewers read the title and locations, then the source, then the card.
   - Calibration κ on 2 ExtraPapers packages before the main review, with a minimum agreed in advance.
   - Independent dual review of all 221 non-protocol flags.
   - protocol_report flags single-coded, crossed over periods, with a random 20% dual-coded.
   - Consensus with Lin; an external statistician if one is recruited.
   - A file-access check of `reviewer_runs/`. Minutes logged. M6 is stated.
5. **Stability and second operator.**
   - **Stability.** Two additional runs on *copies* of 8 packages (2 per year). Each stratum includes one cold start with no reused derivatives, since only 605 of 5,560 source units were extracted fresh. Candidate sets are matched by location and rule.
   - **Second operator.** Shiyin runs the release from the README alone on ExtraPapers packages, or on cohort packages only after her verification is complete, and logs procedural failures.
6. **Application cohort.**
   - Eligibility by online-first year, with the selection rule documented; the observational paper excluded.
   - Clean reruns of the 5 annotated packages.
   - Table S1 lists the departures (M4) and the in-sample status (M5).
7. **Analysis.** As in §2. R, with `sessionInfo()` reported. Scripts tested on mock data. No hypothesis tests.
8. **Ethics, permissions, AI disclosure.**
   - Text-and-data-mining basis (UA Libraries opinion) and the provider's data-use terms.
   - No PDFs redistributed.
   - Disclosure per the AJE guidelines and M9.

### Results (about 1,100 words)
1. **Runs** (Table 1; failure-mode table): wall-clock median 66 minutes (35–131), agents per run, tool versions; failures (scanned or missing plans, 3 stopped runs completed, network-blocked tooling, input annotations, domain misassignment, recheck outcomes, reliance on reused derivatives).
2. **Figure 2:** funnel. **Figure 3:** one annotated evidence card per domain (neutral; identifiers in the supplement).
3. **Table 2:** share confirmed by domain, flags per confirmed issue, substantiveness, rates per 100 pages, determinability.
4. **Extraction payoff:** θ₂ and the determinability distribution; Box 2 with 3–4 cases where an extractor could not tell which value to take.
5. **Package level:** θ₁/θ₁ₛ in M3 wording; Figure 4, confirmed and unconfirmed flags per package against pages.
6. Corrections matches; κ; stability and second-operator results (rerun-only candidates unverified); protocol–report differences (Table S-PR); per-period table in the supplement.

### Discussion (about 800 words)
1. **What this adds beyond a long prompt** (an explicit paragraph).
   - The contribution is an **auditable specification**:
     - written inclusion rules with a numeric precision cutoff;
     - document roles covering protocols and SAPs;
     - one candidate per issue;
     - a screening log of everything dropped, with reasons;
     - cards anchored to source pages;
     - a defined human-verification step.
   - It also contributes an **extraction-relevant yield measured on complete packages**, which prior single-prompt studies did not report.
   - We claim no superiority over a single prompt, deterministic checkers or human review (M8). Whether these features change what is found is untested.
   - *Checkpoint for the authors:* if this paragraph cannot be written without crediting the design with the yield, the single-prompt baseline is needed before submission.
2. **What a user can expect.**
   - The verification workload, and where confirmed issues sat.
   - For systematic reviewers, a flag prompts resolution of the value (M7). Using the workflow may help locate values that need checking; this was not evaluated (N2) [Goh 2024; Mazor 2025].
3. **Box 1, "Using the workflow":** who runs it and when; inputs; model and what to record (version, model ID, dates, tool versions); expected time; reviewing a card source-first; how *not* to read an absent flag (M2) or a protocol_report flag; disclosure (AJE's rule; Flanagin's fields for *JAMA* Network journals).
4. **Limitations:** misses not assessed (M2); in-sample rules (M5); selection; reviewers who developed the workflow, anchoring (M6); one model and Codex dependence; heterogeneous run environments; run-to-run variability characterized on at most 8 packages; reused assets; possible training-data exposure; an underpowered, confounded period table.
5. **Before any confirmatory use:** a held-out frozen set; known-truth items (planted, stratified by type and location; naturally corrected); comparators (single prompt, deterministic checkers, human-only review); cross-model stability; independent verifiers; cost; a study of whether use changes outcomes.

### Supplement (≤5 files, ≤2 MB each) and repository
- **S1.** Specification appendix (role table, rules, prompts, contract, control-file hashes) and Table S1.
- **S2.** Results tables: per package; Table S-PR; funnel by reason; sensitivity analyses; per-period table with confounders; corrections; stability.
- **S3.** Worked examples with page locators.
- **S4 (optional).** LLM-run judgments vs human consensus, labeled as two runs of one model.
- **Repository.** DOI, with an anonymized link for double-anonymized review. Contents: the release, human workbooks and R scripts. No PDFs.

## 4. Actions before 30 October (today is D−16)

| Date | Action |
|---|---|
| D−16 to D−15 | Freeze and commit the amendment: outcome sets A–D; θ₂ rule with hypothetical examples; abstract order; M/N lists; the calibration κ minimum. |
| D−15 | Rebuild the Codebook and blanks; run the validators; desktop-Excel smoke test. Document the selection rule. Send the text-and-data-mining (TDM) query. Recover tokens and the Codex version from session logs, or declare them missing. |
| D−15 to D−13 | Clean reruns of the 5 annotated packages. Stability reruns on copies of 8 packages (16 runs, about 18 machine-hours, cold start per stratum). |
| D−14 | Calibration on 2 ExtraPapers packages; check κ against the agreed minimum. If it falls short, revise the guide and recalibrate. |
| D−14 to D−5 | Independent dual verification of the 221 flags; protocol_report coding; minutes logged. |
| D−14 to D−6 | Corrections search. Package the release (README, hashes). Second-operator run on ExtraPapers. Methods specification. R scripts on mock data. |
| **D−4** | Consensus, then **go/no-go**. |
| D−4 to D−1 | Analysis, writing, Lin's review, disclosure. |

**Go/no-go conditions.** Submit only if all of the following hold. Otherwise wait until verification is complete; the paper does not wait for confirmatory add-ons, and never goes with partial verification (N7).
1. Calibration κ met the agreed minimum before the main review.
2. Dual verification and consensus are complete for all 221 non-protocol flags.
3. Commit history shows the amendment predates the first human judgment.
4. The selection rule is documented.
5. A permissions position is in hand.
6. The clean reruns are done. If they are not, the period table is dropped.

## 5. Decisions that still need the user, Lin or Shiyin
1. **Lin:** accept the design label "development and exploratory application" (meta-epidemiological items applied to the application part only); the abstract leading with verification yield rather than θ₁; and the period comparison as a supplementary, hypothesis-generating Newcombe risk difference.
2. **User and Lin:** the calibration κ minimum, agreed before 16 October (a go/no-go condition).
3. **Shiyin:** confirm the gap formulation attributed to her (transcript support is indirect: 08-25, 01:04:12; Lin 00:45:41), and do the second-operator run on ExtraPapers.
4. **Lin:** whether an external statistician can be recruited by 20 October; otherwise a limitation, with M6.
5. **User:** "replicable" only if the stability rerun and second-operator run both succeed; otherwise "publicly released".
6. **User:** run the single-prompt baseline now only if the "beyond a long prompt" paragraph cannot avoid crediting the design.
7. **User:** the text-and-data-mining (TDM) position, and whether per-package reports quoting source excerpts can be posted.
