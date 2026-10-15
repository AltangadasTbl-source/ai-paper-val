# Drafter B, round 2

The counts below are computed with `reconcile.py`, `run_meta.py` and `parse_xlsx.py` in this folder. Every workbook number is LLM-adjudicated and provisional.

## 1. Critique of Drafter A

**A1. Primary estimand: I concede the order, with a relabel.** A is right that the 06-30 protocol prespecified the paper-level proportion with at least one human-confirmed issue as the primary outcome, with PPV secondary. Keeping that order turns one post hoc change into a retained prespecified outcome, and that is worth more than my preference.

My condition is the label. θ₁ is the **per-paper yield of the human–AI workflow**: the probability that one frozen run plus human adjudication surfaces at least one confirmed issue. It is not prevalence: it combines true prevalence, unknown sensitivity, and the selection of 44 papers that were also used for tuning. "Lower bound on prevalence" may appear once in the Discussion, with those caveats.

PPV and false candidates per paper are **co-reported in the abstract**. A reader deciding whether to adopt the tool needs the yield and the cost together.

**A2. The extraction-impact field: adopt, but define it more tightly.** It belongs in my framing as well. Route B3 already selects candidates on "which value a data extractor would take", so this field is the human test of the pipeline's own inclusion claim.

Make it three-level, not yes/no:
1. determinable within the package;
2. determinable only from an external source (registry, erratum, author);
3. not determinable.

It applies to retained statistical_results and report_internal_inconsistency rows (167 in the provisional data), at roughly a minute per row. The Codebook must be rebuilt before any human review starts. The blanks have not yet gone to people, so the change costs nothing now and is impossible later.

Reviewers will see the AI card's "Affected result or extracted value" text. The field therefore carries an anchoring risk, which goes in the limitations.

**A3. The exhaustive-audit option for sensitivity: reject.** At 2 papers per year (8 papers), restricted to the abstract, primary table, flow diagram and baseline table:
- The number of true issues found is likely in single digits, so the sensitivity interval would span most of [0, 1].
- It excludes supplements, which are Lin's main concern.
- The human auditor is an imperfect reference with unknown sensitivity of its own.

See §2 (c) for the alternative.

**A4. Blinding to the card is not literally possible.** The card defines what the candidate claims. The reviewer-run README's "judged from the PDFs before reading each card" means: read the title and locations, check the source, then read the card. Describe it that way.

**A5. Agreements.**
- A's crossed allocation of reviewers across periods is better than my version, so I adopt it.
- I adopt A's point that candidate counts depend on the grouping rule, so paper-level binary outcomes should lead.
- A's page offset is the same as my source-unit offset for PDFs.
- A's Newcombe risk difference with a half-width near 0.30 is exactly why the period contrast must stay exploratory.

**A6. The architecture figure belongs in the main text, not the supplement.** The AI-in-Health call asks for reproducibility and interpretability. Without Figure 1 the PPV has no object. The agent-role table can go to the supplement.

**A7. Drop the extraction-fidelity substudy.** The evidence maps are free text, so it would need structured re-extraction.

**A8. Corrections to A's numbers.**
- R_Bulun retained **413/440**, not 422. That means 27 were excluded (6.1%), not "about 4%".
- A's other figures check out: 214 retained protocol_report rows; 155 retained statistical_results rows; 139 confirmed_issue, of which 102 are minor_presentation.

## 2. Reconciliations and responses to C

**(d) The protocol_report counts are four different quantities.**

| Count | Definition | Source |
|---|---|---|
| 219 | Pipeline-assigned domain P_R (the AI suggestion in workbook column E as built) | `review_validation.json` ×44; v2.4.1 README table |
| 216 | Domain = protocol_report after the R_Bulun run edited E | `wb_*.json` column E |
| 214 | The same rows, retained (disposition = retain) | R_Bulun D = retain and E = protocol_report |
| 209 / 180 / 163 | Retained as protocol_report by **both** R_A and R_Bulun / identical L / both coded substantive_difference | `reviewer_runs/README.md`, `compare_roles.py` |

The paper should define the protocol_report denominator as **the human-final domain**, and report the pipeline's domain-assignment agreement against it as a classification-accuracy result. That result is a legitimate framework outcome. The 221 candidates outside protocol_report are counted by pipeline domain, so the human-final number will differ.

**C1. Recall and prevalence.** Agreed. See A1 for the relabel and (c) for the substudy.

**C2. The 1.6.2 rules are post hoc for 2018–2019.** This is worse than C states. The 2024–2025 pilot shaped the prompt and the 1.6.1 runs on 2018–2019 shaped 1.6.2, so **all 44 papers are a development cohort**. The remedy is a frozen evaluation on held-out packages: the 10 papers in `/home/juliz/ai-paper-val/ExtraPapers/` (2017; 2020, which is a COVID-period year), plus newly sampled JAMA RCTs if time allows. The held-out run also hosts the planted-error substudy below.

**C3. Departure from protocol 0630.** Supplementary Table S1 lists each departure with its date and whether it came before or after outputs were seen. Restoring the prespecified primary outcome (A1) shrinks the list.

**C4. Zhang 2025 future work as our differentiation.** Use it, but with a narrow claim: our pipeline **implements** propose-then-verify, supplements, tools and multi-agent checking. With no comparator we cannot say these help.

The cheap remedy is an exploratory ablation on the held-out set. Run the same model, single prompt and same packages without the screener, recheck or auditor, and compare candidate counts and the share of screened-out-equivalent flags. Only the added flags need human review. If this is skipped, the Discussion says the architecture's contribution is untested.

**(c) Planted errors versus an exhaustive audit: planted errors are cheaper and more convincing for this framework.**

*Design:*
- About 20 held-out packages (the 10 ExtraPapers plus about 10 more if they can be obtained).
- 1–3 errors seeded into each of about 15 packages, with about 5 clean controls.
- Errors drawn from the route A categories: a count/percentage pair that does not reconcile, an interval vs P conflict, a sign or digit slip, an abstract vs body mismatch, and a planned vs reported outcome-status change.
- Locations prespecified and stratified main vs supplement.

*Estimand:* sensitivity per category, with paper-clustered intervals.

*Cost:* about 20 runs × ~66 min of wall-clock time, which can run in parallel. Human time is only the check of each seed, about 10 hours.

*Technical risk:* the edits must leave no visual or text-layer tells such as font substitution or misaligned glyphs. The pipeline reads both the native text and the rendered pages. Pilot two packages first, and have a person confirm that each seeded page is visually indistinguishable.

*What it claims:* sensitivity for seeded inconsistencies of known types, not natural ones, which may be harder. It matches the La and kwag204 precedent and stays secondary to Lin's unsupervised design.

**C5. Flanagin and JAMA copyright/TDM.** Frame the use case as an author-side check before submission and as post-publication or evidence-synthesis quality control, not as confidential peer review.

The Methods state:
- the account type and data-use terms under which packages went to the model provider;
- that no PDF is redistributed;
- a permissions position on publishing reports that quote source excerpts, checked with UA library or counsel.

Each package's `ai_training_restriction_record.md` documents the screen.

**C6. Research Letter fallback: no, if it reports LLM adjudication.** That reproduces the Zhang circularity in a venue with no room to qualify it, and it uses up the main paper's novelty. An unadjudicated Research Letter, giving yield, screening funnel and architecture only, is honest but weak. I would still rather wait.

**C7 (C §2(d)10). Errata.** This is a cheap, independent partial reference, and I adopt it. Search JAMA correction notices for the 44 papers. Report the share of candidates that a published correction later addressed, and flag those papers for training-data contamination. A candidate that matches an erratum is externally corroborated.

**(e) Deadline.** It is 14 October. Doing everything by 30 October is impossible. The held-out run, the seeding and the ablation alone take more than a week of preparation.

*Decision rule:* submit to the collection only if independent dual human review of the 221 non-protocol candidates plus a protocol_report sample is complete, with consensus, by about 26 October. At Bulun's 10–90 minutes per package, and covering only non-protocol rows, that is about 30–60 person-hours. It is feasible only if both reviewers start now with the rebuilt Codebook.

Otherwise:
- Lin asks the collection editors whether a late submission is accepted. The call says submissions are "encouraged before" the date.
- Without that, target the AJE regular Practice of Epidemiology track 6–8 weeks later, with the held-out planted-error substudy included.
- Under no scenario is LLM adjudication submitted as the reference standard.

## 3. Revised question, storyline and outline

Changes from round 1 are marked **[NEW]**, **[CHANGED]** or **[DROPPED]**.

**Central question [CHANGED].** When a frozen multi-agent LLM workflow reads complete JAMA RCT packages (main article, supplements, protocol, SAP):
- in what share of papers does it surface at least one human-confirmed statistical or report-internal inconsistency;
- in what share of those papers is the correct value not determinable by an extractor;
- what proportion of its candidates do humans confirm, and at what reviewer burden;
- how often does it detect seeded inconsistencies in held-out packages?

**Storyline [CHANGED].** A frozen, page-traced multi-agent workflow surfaced human-confirmed statistical reporting inconsistencies in [X/44] JAMA RCT packages. Some of these left an extractable value undeterminable, and most were in supplements. It did so at a PPV of [Y] with [Z] unconfirmed candidates per paper, and on held-out packages it detected [S] of seeded inconsistencies. Natural-error recall remains unknown.

**Venue.** AJE Practice of Epidemiology. AI-in-Health collection only under the decision rule in (e).

### Introduction
No change, except the novelty sentence, which is now restricted to "implements" (C4) **[CHANGED]**.

### Methods
- **Design** **[CHANGED]**:
  - a development cohort (44 papers) and a held-out evaluation cohort (about 20) **[NEW]**;
  - Table S1 lists departures from the protocol;
  - the 0630 primary outcome is retained.
- **Sample.** Online-first dating; a flow diagram; the documented selection rule (gap).
- **Workflow (Figure 1, main text) [CHANGED]**:
  - role table moved to the supplement;
  - inclusion rules and validator scope as in round 1;
  - versioning, and reuse of assets from earlier runs, by year.
- **Reference standard [CHANGED].** Two humans, crossed across periods (from A), working independently before consensus, with Lin as senior adjudicator. The Codebook is rebuilt before review with:
  - J required;
  - the three-level determinability field **[NEW]**.
  - Review order: title and locations, then source, then card. Minutes are logged.
- **External corroboration [NEW].** JAMA errata matched to candidates.
- **Estimands.**
  - Primary **[CHANGED]**: θ₁, the per-paper workflow yield of confirmed statistical_results or report_internal_inconsistency issues. "Probable" is counted in a sensitivity analysis.
  - Key secondary **[NEW]**: θ₂, the share of papers with at least one confirmed issue whose value is not determinable.
  - Co-reported: PPV by domain, and unconfirmed candidates per paper.
  - Domain-classification agreement between pipeline and human **[NEW]**.
  - Protocol_report described against the human-final domain, with no error verdict.
  - Screening funnel and execution metrics.
- **Held-out substudies [NEW]**:
  - planted-error sensitivity by category;
  - PPV and θ₁ on natural candidates from the frozen run;
  - stability (2 extra runs on about 8 packages);
  - optional single-prompt ablation (exploratory).
- **Analysis.**
  - Paper-level proportions: Clopper–Pearson or Wilson intervals.
  - PPV and sensitivity: cluster bootstrap (2,000 resamples, stated seed) or GEE.
  - Bayesian hierarchical sensitivity analysis with stated priors (Beta(1, 1)-equivalent on the mean; half-normal(0, 1) on the between-paper SD).
  - Counts: negative binomial with a size offset.
  - Period contrast **[CHANGED]**, exploratory only: Newcombe risk difference plus rate ratio, with a permutation check. Sensitivity analysis excluding the 5 annotated papers, or a rerun on clean files.

### Results
1. Cohorts and packages.
2. Execution and funnel (Figure 2).
3. Development-cohort adjudication (Table 3): PPV, θ₁, θ₂, burden.
4. Determinability and worked examples **[NEW emphasis]**.
5. Held-out cohort: seeded sensitivity (Table 4), natural PPV, stability **[NEW]**.
6. Protocol–report differences, descriptive (Supplementary Table S3).
7. Exploratory period contrast.

### Discussion
- Yield vs burden.
- Seeded vs natural recall.
- Architecture untested without the ablation.
- Model dependence.
- Use cases within Flanagin's confidentiality rule **[NEW]**.
- Limitations: development overlap, annotations, anchoring, reviewers who built the tool, one model.

**[DROPPED]** The LLM-as-second-reader comparison moves to the supplement and runs only if time allows. The extraction-fidelity substudy is not adopted.

**Blocking order:**
1. Rebuild the Codebook, then begin dual human review.
2. Obtain and freeze the held-out packages.
3. Pilot the seeding.
4. Rerun the annotated packages on clean files.
5. Document the selection rule.
6. Search for errata.
7. Recover cost (tokens) and the Codex version.
