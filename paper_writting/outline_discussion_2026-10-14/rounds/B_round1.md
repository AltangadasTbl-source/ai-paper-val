# Drafter B, round 1: storyline and outline from the AI-framework perspective

Paths are relative to `/home/juliz/ai-paper-val/paper_writting/` unless they start with `/`. The scripts that produced the numbers sit in the scratchpad (`/tmp/claude-1000/-home-juliz-ai-paper-val-paper-writting/f4104a5a-d4ba-4dcf-9152-ad91d8638ce5/scratchpad/`):
- `run_meta.py` gives the pipeline-side numbers, read from the 44 `review_validation.json` and `run_state.md` files;
- `parse_xlsx.py` and `paper_level.py` tabulate the workbooks.

No adjudication number is used here as a result.

## 1. Evidence: what the mentors asked for

**Who the voices are.** The notes contain one faculty mentor, Lifeng Lin. He is the evidence-synthesis methodologist, and he is also the source of most of the framework requirements. The second recurring voice is Shiyin Li. She is a co-author and the planned second reviewer, and her comments concern tooling (08-25 transcript, speaker 3). She is not called a mentor anywhere. The "AI-framework" position I take here therefore draws on both of them. The authors should not describe a second mentor.

Lin on extraction:
- Supplements matter most, because reviewers rarely check them and errors there "contaminate" later evidence synthesis (`previous_meeting_notes/meeting_notes/20260825-MeetingWithDrLinAndShiyin_原文.txt` l. 453; 08-14 transcript l. 2479–2490).
- Severity depends on whether an extractor can recover the intended value. "50/100 (5%)" cannot be resolved, while P = 0 or a missing "<" can. Very minor items may be set aside if the paper says so (08-25 l. 537–546).
- Keep the focus on numerical and statistical issues (08-14 transcript l. 2404; 08-25 l. 768).

Lin on protocol–report candidates and on the period comparison:
- Keep protocol–report discrepancies in a supplementary table and their own Results subsection, and treat them as less important than statistical errors (`Gmail - Guidance on Flag Adjudication and Temporal Analysis.pdf`, p. 2).
- Restrict the temporal comparison to statistical issues (same email).
- Either a bootstrap or a parametric count model is acceptable once its assumptions are checked (same email).

Lin on the framework:
- Use an unsupervised design: AI flags and humans verify. There is no ground truth, so sensitivity cannot be estimated (`MeetingWithDrLin-06-30-2026_原文.txt` ~l. 420–440; `AI-validation-project_Mentor会议总结.md` §三.A, §六).
- Remove the 10-flag cap (`2026-08-14_meeting_summary.tex` l. 41, 70).
- State exactly which model was run, because subscription interfaces may not reproduce a prompt (08-14 transcript l. 1627–1645).
- Showing that a cost-effective model works is more persuasive than relying on the most expensive one (`MeetingWithDrLin-07-24-2026_Transcript.txt` l. 658).
- Post the linked HTML reports on OSF or GitHub, so that "the whole thing can be reproduced" (08-25 l. 465–477).
- Write quickly, because models change fast (Mentor会议总结 §二.4).

Lin on venue and design:
- Venue: the AJE "Artificial Intelligence in Health" collection, deadline 30 October 2026, framed as meta-epidemiological methodological research that follows a collaborator's reporting guideline (08-25 l. 609–630).
- Periods: 2018–2019 vs 2024–2025, with no causal claims (summary .tex l. 43).
- Either result of the period comparison can be reported (08-25 l. 684–690).
- Papers are dated by online-first date (l. 723).

Shiyin:
- A cross-model check, such as Codex plus Claude (08-25 l. 513).
- An adjudication interface with save and CSV export (l. 579).
- A public release that runs on users' own API keys (l. 693).

**Disagreements or shifts:**
- *Model comparison.* The protocol excludes it. Lin wants the cost-effectiveness message, and Shiyin proposes a cross-model check.
- *Severity grades.* Lin asked for minor, moderate and major levels (08-14 l. 2428), then cautioned about tone (l. 2479).
- *Temporal comparison.* Lin was doubtful on 07-24 and supportive by 08-25.
- *Second review.* Lin proposed that one reviewer initiates and the other double-checks. Shiyin asked whether both should review everything (08-25 l. 564–576).
- *Protocol flags.* Shiyin questioned retaining them; Lin and Bulun kept them as a separate domain (email).

## 2. Central question, storyline, venue

**What the data can support.** A prevalence study of errors in JAMA randomized clinical trials (RCTs) is not supportable:
- recall is unknown;
- the 44 papers are not a defined random sample;
- the rules were tuned on these same papers (§4).

What the data can support is a study that describes a frozen, fully traced multi-agent workflow and measures what it delivers to a human reviewer: how many flags it raises, the share that hold up, of what type, at what reviewer burden, and how reproducibly. The paper-level count of confirmed issues remains Lin's headline, but stated as a lower bound conditional on detection. That is honest as a tool estimand and would be misleading as a prevalence estimand.

**Central question.** When a fixed multi-agent large language model (LLM) workflow reads a JAMA RCT report together with its supplements and plan documents, how many statistical-reporting candidates does it raise per paper? What proportion do human statisticians confirm, and at what cost in reviewer time?

**Storyline.** Run once per paper with complete source coverage and evidence traced to the page, the workflow surfaced human-confirmed statistical reporting issues in [X of 44] JAMA RCT reports, mostly in supplements. The positive predictive value (PPV) was [Y], and reviewers faced [Z] unconfirmed candidates per paper. Routine AI-assisted checking before publication or data extraction is therefore feasible, but its recall is unknown.

**Venue.** AJE, Practice of Epidemiology. The guidelines list "AI/ML applications… validation of instruments" under this type (`AJE_specific/AJE_author_guideline.txt` ~l. 316). The limits are 4,000 words and a 200-word unstructured abstract. The article can go to the AI-in-Health collection. Novel Methodology, the type of the kwag204 framework paper, would oversell the work, since we propose no new statistical method. kwag204 is still a useful structural template.

Format consequences:
- Supplementary material is limited to five files of at most 2 MB each (l. 509). The 440 evidence cards, the workflow, and the run artifacts must therefore go to an archived repository with a DOI.
- AI use must be disclosed in the Methods (l. 53).

**Title.** "A multi-agent large language model workflow for detecting statistical reporting inconsistencies in randomized trial reports in *JAMA*, 2018–2019 and 2024–2025."

## 3. Outline

### Introduction (~500 words)
1. Numerical inconsistencies, especially in supplements, escape peer review and propagate into systematic reviews. Cite Xu 2022 on the validity of data extraction.
2. Prior LLM checkers: Zhang 2025 and La 2026 from `potential_paper_2_cite/`, plus Flanagin 2026 on author AI use. Agent C should confirm what each reports. Also [citation needed: statcheck/GRIM-type deterministic checkers].
3. The gap: prior checkers are single-prompt, their output is not traced to sources, and they are evaluated without plan documents or reviewer-burden measures.
4. Aims:
   - describe the workflow;
   - estimate per-domain PPV and per-paper yield against human adjudication;
   - describe protocol–report differences separately;
   - an exploratory comparison of the two periods.

### Methods (~1,700 words)

**Design.**
- A cross-sectional methodological study with a tool-evaluation component.
- Reporting guideline: [citation needed: the meta-epidemiological reporting guideline Lin named on 08-25; and an LLM-evaluation checklist, if C finds one that applies].
- Supplementary Table S1 gives each departure from the 30 June protocol (`method_design/AI_PaperVal_Protocol_0630.md`). The protocol planned 2025 only (n = 30), a single GPT model run once per package, exclusion of protocol/SAP deviations, and four human categories. Each departure gets its date and whether it was made before or after seeing outputs:
  - the cap removed;
  - two periods instead of one year;
  - the protocol_report domain added;
  - the move from 1.5.x and 1.6.1 to 1.6.2;
  - jama.2019.14231 dropped;
  - the Codebook in place of the four categories.

**Sample.**
- Eligibility: JAMA RCT reports, dated by online-first date.
- Flow diagram.
- 44 papers: 10 from 2018, 9 from 2019, 10 from 2024 and 15 from 2025. The observational paper jama.2019.14231 is excluded, with the reason stated.
- Packages contain the main article, supplements, protocol, and statistical analysis plan (SAP).

**Workflow (the core section).**
- *Figure 1* shows the architecture as a sequence of gates:
  1. inventory and SHA-256 hashing;
  2. asset curation;
  3. parallel main and support mappers;
  4. three parallel checkers (numeric, cross-source, statistical pass 1);
  5. independent inclusion screener;
  6. candidate registration;
  7. mechanical evidence recheck;
  8. statistical pass 2, which rereads the checkers' exclusions;
  9. second screen;
  10. quality-control auditor;
  11. report generator;
  12. structural validator.
- *Table 1* has one row per agent role: what it reads, what it writes, its reasoning effort, and what it is barred from doing (no severity, no disposition, no deletion of candidate IDs, no "error" vocabulary).
- The text defines the rules that decide what becomes a candidate:
  - the inclusion threshold, with route A (always-register categories) and route B (in focus, unresolved by context, and bearing on interpretation or extraction);
  - the display-precision rule (half-unit interval arithmetic with a relative-discrepancy cutoff of 0.05);
  - the four review domains and the relationship codes P_R, P_P, S_C and S_W;
  - the evidence state;
  - page-anchored links to the sources;
  - fresh, distinct agents for each mandatory stage.
- State that the validator checks structure, coverage, matching ID sets, hashes and wording, not scientific correctness (`workflow_1_6_2/scripts/validate_review.py`).

**Versioning.**
- Workflow 1.6.2 was frozen. One model, `gpt-6.1-sol`, served all roles, with reasoning effort varying by role. The runs were made in the Codex CLI (version needed) on 11–14 October 2026, one run per package.
- *Supplementary Table S2* gives the development history from 1.0 to 1.6.1 (`/home/juliz/ai-paper-val/multi_agent_template/archived_workflow/`): what each version changed and which papers informed the change.
- Disclose that 1.6.2 reused text and OCR assets from earlier runs. Only 605 of 5,560 source units were extracted fresh. The earlier runs differ by year (2018: 1.5.2/1.6.1; 2019: 1.5.1/1.5.2/1.6.1; 2024: 1.5.3; 2025: 1.5.1/1.5.3). Tabulate asset provenance from each `evidence_asset_inventory.md`.

**Reference standard.**
- Two statisticians independently review the source PDFs using the v2.4.1 Codebook, which records:
  - disposition;
  - domain;
  - for statistical_results, issue status and substantiveness;
  - for report-internal and plan-material candidates, inconsistency status;
  - for protocol_report, an optional interpretation.
- Disagreements go to consensus, with Lin as senior adjudicator.
- Disclose that reviewers see the AI card and the pre-filled domain, which risks anchoring and incorporation bias.
- Record reviewer minutes per paper.
- The Claude Opus 5.5 "R_A/R_Bulun" runs are not the reference standard (§4).

**Estimands.**
- *Primary:* PPV within statistical_results, defined as the proportion of candidates retained with issue = confirmed. A sensitivity analysis counts confirmed or probable as positive.
- *Secondary:*
  - PPV for report_internal_inconsistency and for plan_material;
  - the proportion of papers with at least one confirmed issue, and with at least one substantive issue;
  - confirmed issues per paper;
  - unconfirmed candidates per paper (the reviewer burden);
  - location (main article vs supplement);
  - extraction relevance (field J);
  - reviewer minutes and pipeline wall-clock minutes per paper.
- *Descriptive only:* protocol_report candidates by element and by the optional interpretation. These get no error verdict and no PPV. This is the supplementary table Lin asked for.
- *Process, from pipeline logs:*
  - 789 checker findings;
  - 215 of them screened out (146 as duplicates; 16 terminology, 15 context, 10 peripheral, 9 not reproduced, 9 conditional, 4 rounding, 3 out of focus and 3 notation);
  - the remainder consolidated into 440 candidates;
  - evidence state reproduced for 435 candidates, and 5 questioned by the auditor.

**Analysis.**
- *PPV.* Candidates are clustered within papers (1–22 per paper). Use a logistic generalized estimating equation (GEE) with exchangeable working correlation, or a paper-level cluster bootstrap with 2,000 resamples and a stated seed.
- *Bayesian sensitivity analysis.* A hierarchical logit model with a Beta(1, 1)-equivalent prior on the mean PPV and a half-normal(0, 1) prior on the between-paper SD, reporting the SD with its credible interval.
- *Paper-level proportions.* Wilson intervals.
- *Counts per paper.* Negative binomial regression with an offset of log source units, because the opportunity to flag scales with package size (40–404 units).
- *Agreement between the two human reviewers.* Kappa with paper-bootstrap intervals.
- *Exploratory analyses:*
  - a period rate ratio for confirmed statistical issues, with permutation intervals as Lin suggested;
  - a stability rerun;
  - LLM-as-second-reader agreement with the human consensus.
- Analyses in R, with `sessionInfo()` reported.

**Stability (new data).** Rerun the frozen 1.6.2 workflow twice more on about 8 papers, stratified by period and by candidate count. Match candidates across runs by location and rule. Report the Jaccard overlap per paper and the share of human-confirmed issues that the reruns find again.

### Results (~1,300 words)
1. **Cohort (Table 2, by period).** Source units, availability of plans, unusable text layers, and annotated inputs.
2. **Execution.**
   - All 44 runs passed the validator.
   - Agents per run: median 15.5 (range 12–43).
   - Wall-clock time: median 66 minutes (range 35–131); 40 of 44 runs exceeded their planning target.
   - Failure modes: 3 runs needed completion after a stop; tooling bootstrap was blocked by network restrictions; some plan documents had unusable text layers.
   - *Figure 2* shows the funnel from findings to screened-out reasons, candidates and human disposition, by domain.
3. **Statistical results (Table 3).**
   - For each period and overall: candidates, retained, confirmed and probable, PPV with 95% CI, substantive versus minor, and extraction relevance.
   - Three or four worked examples in which the extractable value is ambiguous (Lin's test).
4. **Yield and burden (Table 4, Figure 3).** Confirmed and unconfirmed candidates per paper against source units, and reviewer minutes.
5. **Protocol–report differences.** Descriptive only, with Supplementary Table S3.
6. **Stability, and the exploratory period comparison.**

### Discussion (~800 words)
- Findings framed as yield and PPV, with recall unknown.
- Design features that plausibly support the PPV, presented as hypotheses since no ablation was run: the independent screener, the always-register rules, the reread of each source location, and one candidate per pattern.
- Comparison with prior LLM checkers.
- Implications for editors and data extractors.
- Dependence on one proprietary model that may be retired.
- Generalizability beyond JAMA RCTs.
- Limitations: the rules were tuned on the same papers; recall is unknown; reviewers may anchor on the AI cards; some inputs were annotated; assets were reused from earlier versions; cost was not measured.

**Data availability.** Workflow, configuration and per-paper reports go to an archived repository. The JAMA PDFs cannot be redistributed. Check whether reports that quote the source text can be posted, given the AI-training-restriction notices.

## 4. Data gaps and decisions, ranked by how much they block the paper

1. **No human adjudication exists.** This blocks everything.
   - The 880 judgments are Claude Opus 5.5 sessions (`/home/juliz/ai-paper-val/human_adjudication/human_adjudication_v_2_4_1/reviewer_runs/README.md`), so their agreement is concordance between runs of one model, whose errors are likely correlated.
   - *Decision:* Bulun and Shiyin each review independently at least the 221 candidates outside protocol_report, plus a random sample of protocol_report candidates, then reach consensus.
   - Lin's initiate-then-check scheme yields a verified reference standard but no reliability estimate.
   - At Bulun's 10–90 minutes per package (08-25 l. 667), full adjudication is tens of person-hours. That collides with 30 October. I advise against submitting with partial adjudication.
   - The LLM runs may appear only as a labeled secondary analysis.
2. **Development and evaluation overlap.** This blocks an unbiased PPV.
   - The rules were revised after the authors saw outputs on these papers. The 1.6.2 README cites the 1.6.1 runs on 2018–2019 as the reason for its changes.
   - The PPV on these 44 papers is therefore an in-sample (apparent) value.
   - *Remedy:* run the frozen 1.6.2 on held-out packages (the 10 in `/home/juliz/ai-paper-val/ExtraPapers/`, or new JAMA RCTs) and adjudicate them. Otherwise, label the 44 papers as a development cohort.
3. **Sampling frame.** How the 44 papers were chosen from the eligible JAMA RCTs is not documented.
4. **Contamination of inputs that differs by period.** Highlight annotations by the project account, some marking suspected errors, are in PDFs the pipeline read for five 2024–2025 papers (2024.2302, 2024.4183, 2025.4390, 2025.7710, 2025.11178). Two other files carry other annotations. No 2018–2019 file is affected.
   - *Remedy:* rerun on clean originals, or report a sensitivity analysis that excludes these papers. Without one or the other, the period comparison cannot be interpreted.
5. **Cost and stability.** Token use was not logged and no replicate runs exist.
   - Recover usage from the Codex session logs if possible, and run the stability subset.
   - Without these data, any cost-effectiveness claim is unsupported.
6. **Run metadata.** Missing: the Codex version, the model snapshot date, and the OCR hardware.
7. **Plan documents.** Some are missing or post-dated (for example, the 4183 protocol is dated after the trial ended).
8. **Permission to share** the reports that quote source text.

## 5. Risks: claims the data cannot support

- A prevalence or error rate "in JAMA RCTs". At most, the data give a lower bound for detected and confirmed issues in a non-random sample.
- Sensitivity, recall or "misses X%". Seeded errors or a second model give only partial and biased proxies.
- R_A/R_Bulun agreement presented as inter-rater reliability, or numbers adjudicated by the LLM presented as findings. This includes the provisional pattern in the workbooks: most papers have a retained statistical row, and most rows are coded minor_presentation.
- Retained protocol_report rows read as errors, violations or selective reporting.
- A period difference attributed to COVID-19 or to LLM availability. Even the association is fragile:
  - the samples are small (19 vs 25 papers);
  - input contamination differs by period;
  - the reused assets come from different pipeline versions by year;
  - supplements have probably lengthened.
- Validator "PASS" read as accuracy.
- "Cost-effective" or "works with cheap models": only one model was run and cost was not recorded.
- Generalization to other journals, to observational designs, or to other or later models.
- Wording in the authors' voice that implies misconduct.
