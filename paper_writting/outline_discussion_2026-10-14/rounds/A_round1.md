# Drafter A, round 1: storyline and outline (evidence-synthesis lens)

Paths are relative to `/home/juliz/ai-paper-val/paper_writting/` unless they start with `/`. Transcript times are speaker timestamps; `L` numbers are line numbers.

## 0. A correction to the brief

The notes show one faculty mentor, not two. **Lifeng Lin** is the meta-analysis methodologist and leads every meeting. **Shiyin Li** joins only on 08-25. She is a senior trainee who is graduating soon (08-25 transcript, 04:38 and 07:12), has systematic-review experience, and is designated second author and second reviewer (01:11:01). She contributes the AI-tooling suggestions. Most framework design comes from the student, Bulun Te.

Lin's concern is also not the AI's own extraction accuracy. It is **errors in published RCT packages that a meta-analyst would then extract**. I build the outline on that reading and explain below why AI extraction accuracy cannot be the primary endpoint.

## 1. Evidence drawn on

**Lin (meta-analysis methodologist)**
- **L1. Unsupervised audit, human verification of flags.** No planted-error or supervised design. Even about 10% of JAMA papers with a verifiable issue would be informative. Sources: 06-30 transcript, 01:10:12 to 01:13:35 (L424–433); 06-30 note, "unsupervised is enough / jama: 10% fault is enough".
- **L2. Focus on statistical results.** Wording disputes are not for us to decide. Sources: 08-25, 01:09:52; 08-14 transcript, L2399–2423.
- **L3. Supplements are the target.** Supplements get the least checking. Systematic reviewers retrieve data from them, so a typo can "contaminate the evidence flow". Sources: 08-25, 00:43:32; 08-14, L1190–1196 ("which result should I believe?").
- **L4. Severity is defined by extractability.** "P = 0" and a missing "<" are very minor. A count/percentage conflict where a reviewer cannot tell whether 50/100 or 5% is right is more serious, because the correct value cannot be imputed. Ignore very minor issues, but say so in the paper. Source: 08-25, 00:51:09 to 00:52:13.
- **L5. Constructive tone.** Do not imply that every issue changes conclusions. Lin backed away from AI major/minor grading ("you attack others, they attack you"). Sources: 08-14, L2440–2490; `2026-08-14_meeting_summary.tex`, AI section.
- **L6. Keep protocol–report differences.** Report them in a supplementary table plus a Results subsection, ranked below statistical reporting errors. Source: Gmail PDF p. 2, reply of 2026-09-05 22:49, point 1.
- **L7. Temporal comparison.** It is "interesting", around COVID-19 and LLM availability. It should be restricted to substantive statistical errors and internal inconsistencies. Check the assumptions of any parametric model; Lin favored a nonparametric bootstrap. Sources: same email, points 2–3; 08-25, 01:01:43 to 01:03:14, which describes shuffling the year labels, i.e. a permutation. Periods are balanced at 2018–2019 vs 2024–2025, with no causal claims (summary .tex). Earlier he doubted the comparison was worth it (`AI-validation-project_Mentor会议总结.md` §F, 07-24).
- **L8. Two reviewers, crossed over periods.** Each reviewer covers both periods so that assessor variability does not track period (08-14, L1145–1160). Bulun reviews first and Shiyin double-checks (08-25, 00:53:31).
- **L9. Target journal.** AJE "AI in Health" collection, deadline 30 October. Follow a meta-epidemiological methodology reporting guideline (Murad and colleagues; [citation needed: meta-epidemiological research reporting guideline]). Source: 08-25, 00:56:12 to 00:58:53.
- **L10. Make the reports public.** Post the per-paper reports (OSF or GitHub) for reviewers and readers (08-25, 00:45:12).
- **L11. 06-30 protocol.** Primary outcome: the proportion of packages with at least one human-confirmed issue. Secondary outcomes include the PPV of flags, issue types and locations, and review time. The comparison covers 2025 only (n = 30), no model comparison, and protocol/SAP deviations are out of scope (`method_design/AI_PaperVal_Protocol_0630.md`, L11–19, L51, L85, L113–123).

**Shiyin Li and Bulun Te (AI-framework concerns)**
- **S1–S3 (Shiyin, 08-25).** Release the workflow so users run it on their own tokens (01:04:12). Cross-check with a second model, at added cost (00:48:41). Build an HTML adjudication page with export (00:54:40).
- **B1 (Bulun, Gmail p. 1).** Retain protocol flags as candidates. Use a descriptive, exploratory framing. Fit a Bayesian count model or a cluster-robust GLM to the non-protocol subset.

**Disagreements**
- **Protocol flags.** Shiyin raised exclusion; Bulun proposed retention; Lin settled on retaining them, reported separately and treated as lower priority.
- **Temporal analysis.** Lin wants a formal comparison, possibly with a P value; Bulun frames it as exploratory; the protocol omits it altogether.
- **Severity grading.** Lin asked for it on 08-14 and then withdrew. Workflow 1.6.2 forbids grading, but the Codebook has substantive vs minor_presentation.
- **Need for cross-checking.** On 08-14 (L1169) Lin thought a cross-check was "probably not necessary"; on 08-25 he set up a two-reviewer double check. Bulun floated relying on AI to check flags (08-25, 00:48:00); Lin's position throughout is human verification.

## 2. Central question, storyline, venue

**Question.** In reports of RCTs published in *JAMA* in 2018–2019 and 2024–2025:
1. How often does the article package contain a statistical reporting inconsistency that an agentic LLM workflow flags and human reviewers confirm?
2. How often does that inconsistency leave ambiguous a value that a systematic reviewer would extract?
3. What proportion of the workflow's flags do reviewers confirm?

**Storyline (one sentence).** An agentic LLM audit of JAMA trial packages surfaces document-verifiable statistical reporting inconsistencies, concentrated in supplements, that human reviewers confirm; some leave the extractable effect estimate, interval or count ambiguous, which is an avoidable hazard for evidence synthesis that a routine prepublication check could remove.

**Why extraction relevance is the organizing construct but not the primary endpoint.**
- The workflow's own scope already defines inclusion route B3 as "could change … which value a data extractor would take" (`method_design/workflow1.6.2/QUALITY_CONTROL_SCOPE.md`, Inclusion threshold). The Codebook has a Downstream impact field J (direct/possible/unlikely/unknown).
- AI extraction accuracy as a primary endpoint would need three things we lack:
  - a reference extraction: dual independent human extraction of prespecified items;
  - a structured AI extraction to compare against (the pipeline writes free-text markdown evidence maps, e.g. `extraction/main_quantitative_evidence.md`);
  - a mentor request for it, and there is none.
- Xu et al. (BMJ 2022; Lin is a coauthor) quantified extraction errors made *by systematic reviewers*. This study is the upstream counterpart: inconsistencies *in the source* that make correct extraction impossible. That is the defensible bridge to the meta-analytic audience.

**Venue.** AJE, Practice of Epidemiology. The type explicitly covers "AI/ML applications" and validation (`AJE_specific/AJE_author_guideline.txt`, L316–318). Limits: 4,000 words and a 200-word unstructured abstract. The AI in Health call asks for work on bias, generalizability and interpretability (`AJE_special_crude_guideline.txt`), which suits an audit that is candid about its reference standard. AJE requires disclosure of AI use in the Methods (guideline L53). **The 30 October deadline is only "encouraged"; it is not worth submitting without human adjudication** (see §4).

## 3. Outline

### Abstract (200 words, unstructured)
Cover the question, the design (meta-epidemiological audit of 44 RCT packages), the reference standard (two human reviewers), the primary estimate with its interval, PPV with a paper-clustered interval, and an exploratory period contrast with its interval. State that sensitivity was not estimated.

### Introduction (about 500 words)
1. Results in RCT packages feed meta-analyses, and supplements receive little scrutiny (L3). Prior work documents extraction errors in syntheses (Xu et al. 2022).
2. LLMs are now used as consistency checkers. A planted-error design estimates sensitivity in a small sample (La et al. 2026, *Eye*). Reasoning LLMs have been used to screen papers for critical problems (Zhang et al. 2025). [Literature agent C to complete; cite only from `potential_paper_2_cite/`.]
3. Gap: no audit of naturally occurring, extraction-relevant inconsistencies in complete trial packages (main article, supplements, protocol, SAP) with human adjudication of every flag.
4. Objectives, stated in prespecified vs added order (see Methods §Protocol history).

### Methods (about 1,400 words)
- **Design and reporting.** Meta-epidemiological cross-sectional audit. Follow a meta-epidemiological methodology reporting guideline [citation needed] and Flanagin et al. 2026 for AI disclosure.
- **Protocol history.** State plainly:
  - The 06-30 protocol covered 2025 only and excluded protocol deviations.
  - The 2018–2019 vs 2024–2025 comparison and the protocol–report domain were added in July–August, after the 2024–2025 pilot.
  - Screening rules changed from workflow 1.6.1 to 1.6.2 after the 1.6.1 runs on 2018–2019 (`method_design/workflow1.6.2/README.md`, "Changes from 1.6.1").
  - The temporal analysis is therefore labeled exploratory. A dated SAP amendment must be frozen before human adjudication begins.
- **Eligibility and sampling.** Original primary reports of RCTs in *JAMA*, assigned to a year by online-first date (08-25, 01:05:45). This explains why jama.2017.21906 sits in 2018 and two 2024 DOIs sit in 2025. The observational paper jama.2019.14231 was excluded. Report the eligible count per year and the selection rule; see Gap 2.
- **Article package.** Main PDF, all supplements, protocol and SAP as supplied. Record which plans were missing or scanned (`/home/juliz/ai-paper-val/human_adjudication/human_adjudication_v_2_4_1/reviewer_runs/README.md`, "Missing plan documents").
- **Index test (workflow 1.6.2).** Describe:
  - the agent roles and the model with its version;
  - one run per package, all 44 run with 1.6.2 between 11 and 14 October 2026;
  - the four focus areas, the display-precision rule, inclusion routes A and B, and the screened-out reason codes;
  - "one candidate per issue";
  - no cap on candidates (the cap of 10 was removed after 08-14).

  Report runtime per package from `run_state.md`. A schematic goes in the supplement.
- **Reference standard.** Two human reviewers, Bulun and Shiyin. Each reviews from the PDFs before reading the card and is blinded to the other reviewer and to every LLM-adjudicator file. Allocation is crossed so that each reviewer covers both periods (L8). Use a calibration set first, then resolve disagreements by consensus with Lin as senior adjudicator. Use the v2.4.1 Codebook with two changes:
  1. make J (downstream impact) required for retained statistical_results rows;
  2. add one field: **"Can a reader determine the correct value from the package?"** (yes / no / not applicable). This field operationalizes Lin's 50/100-vs-5% criterion (L4).
- **Units and domains.**
  - The paper is the sampling unit and the candidate is the adjudication unit.
  - A candidate is not a count of affected numbers, because one candidate can list many locations.
  - The domains are statistical_results and report_internal_inconsistency (the "report domain"), plan_material, and protocol_report. protocol_report is analysed separately and carries no error verdict.
- **Outcomes and estimands.**
  - **Primary.** θ₁ is the proportion of packages with ≥1 report-domain candidate that is retained and has H = confirmed_issue (or K = substantive/minor inconsistency for report_internal_inconsistency rows). Its label is "workflow-detected, human-confirmed prevalence". This is a lower bound for true prevalence, because sensitivity is unknown.
  - **Key secondary (the extraction outcome).** θ₂ is the proportion of packages with ≥1 confirmed issue in which J = direct *and* the correct value is not determinable from the package.
  - **Other secondary outcomes:**
    - PPV, the confirmed share of report-domain candidates, estimated as a ratio over all candidates rather than a mean of per-paper PPVs;
    - the distribution by focus area (A/B/C), by location (main, supplement, or across documents) and by route;
    - θ₁ with probable_issue added, as a sensitivity analysis;
    - inter-reviewer agreement;
    - review time per paper (an objective in the 06-30 protocol).
  - **Descriptive.** Protocol–report differences by element (outcome, analysis, population, sample size, multiplicity), with Codebook field L and "disclosed" flags. No error rate is attached.
- **Statistical analysis.**
  - **Paper-level proportions.** Clopper–Pearson intervals.
  - **Candidate-level PPV and kappa.** Percentile intervals from a paper-level cluster bootstrap (2,000 resamples, seed stated).
  - **Exploratory period contrast.** For θ₁ and θ₂, the risk difference with a Newcombe interval. For confirmed report-domain issues per paper, a negative-binomial GLM with offset log(total package pages) gives a rate ratio. The GLM is fitted at the paper level, so no clustering correction is needed. A Bayesian version can be added, with priors stated (for example, Normal(0, 1) on the log rate ratio and Half-Normal(0, 1) on 1/dispersion). Lin's permutation of period labels goes in the supplement, and estimates with intervals lead.
  - **Covariates, descriptive only.** Package pages, number of supplements, protocol/SAP supplied, enrolment, and COVID-19 trial topic.
  - **Software.** R (stats, boot), with sessionInfo().
- **Sensitivity analyses.** Exclude the papers with annotated PDFs (Gap 4). Count probable_issue as confirmed. Exclude the online-first boundary papers.
- **Ethics and data use.** Published articles only. Include a text-and-data-mining statement (07-24 transcript, L730).

### Results (about 1,100 words)
- **Fig 1.** Flow: eligible reports by year → sampled → packages → workflow findings → screened out by reason code (from `screening/inclusion_screen*.md`) → candidates by domain → adjudication outcomes.
- **Table 1.** Package characteristics by period.
- **Table 2.** Candidate-level adjudication by domain:
  - disposition;
  - H × I (issue certainty by substantiveness);
  - J, and the "value determinable" field;
  - PPV with a 95% cluster-bootstrap interval.
- **Table 3.** Paper-level θ₁, θ₂ and the substantive-issue prevalence: overall, and by period (exploratory), with intervals.
- **Fig 2.** Paper-level dot plot, one row per paper, with counts by domain and by confirmed status. It shows clustering and the heavy right tail.
- **Table 4.** Confirmed issues by focus area × location (main vs supplement vs cross-document). This answers L3 directly.
- **Box 1.** Three or four worked examples showing the extraction consequence. Use neutral wording; full identification goes in the supplement.
- **Subsection: protocol–report differences.** Short and descriptive, with Supplementary Table S-PR (L6).
- **Supplement:**
  - per-paper ledger and links to the reports (L10);
  - screening logs;
  - runtime;
  - optionally, LLM-adjudicator vs human agreement, clearly labeled as such.

### Discussion (about 900 words)
Present detected-and-confirmed prevalence. Say which issue types make extraction indeterminate, and what to do about them: a prepublication check by authors or editors, and in reviews, extracting from both locations and querying authors. Contrast with planted-error studies, which estimate sensitivity but not naturally occurring prevalence. State the limitations directly:
- unknown sensitivity;
- a single model and a single run;
- selection of the 44 papers;
- overlap with the papers used for tuning;
- annotation exposure;
- reviewers who also built the tool;
- an underpowered, confounded period contrast.

Close with generalizability and release of the workflow (S1).

## 4. Data gaps and design decisions, ranked by how much they block

1. **There is no human adjudication.** This blocks every outcome. The R_A/R_Bulun workbooks are two Claude Opus 5.5 runs ("No person reviewed any candidate", reviewer_runs README). Their provisional pattern looks optimistic: about 4% excluded, `discuss` never used, and model errors that are likely correlated. To do:
   - two humans review all 440 candidates under the crossed allocation;
   - log time per paper;
   - keep reviewers away from `reviewer_runs/`.

   Bulun's estimate is 10 to 90 minutes per paper (08-25, 00:59:44), so roughly 7–66 hours per reviewer for 44 papers, nearer the top for a review that starts from the PDFs. Decide whether 30 October is realistic. My recommendation is to miss it rather than submit LLM-adjudicated results as the reference standard.
2. **The sampling frame is undocumented.** How were 9–15 papers per year chosen from all eligible JAMA RCTs? An earlier internal report says the packages "are not a random sample" (`/home/juliz/ai-paper-val/meta_report/previous/jama_audit_report_en.md`, L94). 2025 has 15 papers and 2019 has 9. Without the frame and selection rule, θ₁ describes these 44 papers only.
3. **Freeze an SAP amendment before adjudication.** It should fix:
   - the outcome tiers (θ₁, θ₂);
   - the J requirement and the new "value determinable" field;
   - the temporal contrast as exploratory, with its estimand and models;
   - how report_internal_inconsistency enters θ₁;
   - the sensitivity analyses.
4. **Contamination and development overlap.**
   - Earlier highlights by AltanGadasTbl that mark suspected errors appear only in **2024–2025-cohort** PDFs: 7 files in 5 papers (2024.2302, 2024.4183, 2025.4390, 2025.7710, 2025.11178; reviewer_runs README, "Annotated source PDFs"). The workflow read these files, so any bias would differ by period. Replace them with clean originals and rerun those 5 packages, or at minimum run a sensitivity analysis excluding them.
   - The 2024–2025 pilot papers shaped the prompt, and the 1.6.1 output on 2018–2019 shaped the 1.6.2 rules. Disclose both.
5. **Sensitivity is not estimable as designed.** Decide on one of:
   - (a) a full independent human audit of a random subsample, for example 2 papers per year, restricted to prespecified displays (abstract, primary-outcome table, flow diagram, baseline table);
   - (b) a planted-error substudy in the style of La et al.;
   - (c) a limitations statement plus descriptive reporting of the reviewers' out-of-set observations, which the LLM reviewers already logged and which show misses exist.

   (a) best fits the meta-analytic lens and remains feasible after submission.
6. **Optional extraction-fidelity substudy.** Compare the workflow's transcribed values for prespecified items (primary-outcome arm-level n/N or mean/SD, effect, CI, P) against dual human extraction, and tabulate `reproduced_after_transcription_correction` states from the evidence recheck. Label it secondary and skip it if time is short.
7. **Run-to-run reproducibility.** Rerun a subset (for example 5 packages) to estimate candidate-set overlap. Record the model string for every run; some `run_state.md` files omit it. Record token or cost use (S1, S2).
8. **Covariates for Table 1.** Collect them from the packages.

## 5. Claims the data cannot support

- **"Confirmed" or "human-verified" for any current number.** The current numbers come from LLM adjudication. Provisional pattern (R_Bulun run; my Python stdlib tabulation of the workbook XML, `scratchpad/tab.py`; non-human):
  - 422/440 candidates retained;
  - 214 retained protocol_report rows;
  - among 155 retained statistical_results rows, 139 coded confirmed_issue, of which 102 were minor_presentation.

  This suggests that the substantive and extraction-relevant tiers, not the headline counts, carry the story. It needs human confirmation.
- **Sensitivity, recall, or "the AI finds most errors".** Not estimated.
- **True prevalence of errors in JAMA.** Only detected-and-confirmed prevalence can be reported, conditional on one model, one run and the screening rules.
- **Candidate counts as error counts.** The grouping rule and screening thresholds determine counts. This is a reason to prefer paper-level binary outcomes over count models for the headline.
- **PPV as a portable property of "AI".** PPV depends on the screening rules, the prevalence and the reviewers.
- **Period differences attributed to LLM availability or COVID-19.** With 19 vs 25 papers, a risk difference near p = 0.5 has a 95% Wald half-width of about 0.30 (R: `qnorm(.975)*sqrt(.25/19+.25/25)` = 0.298). The comparison is confounded by plan availability, package length, trial topic, annotation exposure and tuning history. Any null or non-null result is descriptive. Lin's "either result tells a story" (08-25, 01:02:10) is a framing for the Discussion, not an inference.
- **Protocol–report differences as errors or as evidence of selective reporting.** Disclosure was not assessed systematically; this question is the user's to own.
- **AI extraction accuracy.** There is no reference extraction.
- **Inter-rater reliability from R_A vs R_Bulun.** Those are two runs of the same model.
