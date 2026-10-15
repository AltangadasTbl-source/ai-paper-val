# v4 (Drafter A): a formalized exploratory workflow, first applied to JAMA RCT packages

Inputs: v3_consolidated.md, B_round3_exploratory.md, C_dispute2.md, and the user's two framing notes. No flag has been verified by a person yet. Workbook figures are from two Claude Opus 5.5 runs and appear only where they bear on planning. Pipeline figures (789 findings, 215 screened out, runtimes) come from B's `run_meta.py`.

## 0. What changed from v3, and why

1. **The core contribution is now the workflow itself.** It is a formalized, versioned, reusable procedure for agentic internal-consistency checking. The descriptive first application to 44 *JAMA* RCT packages is the demonstration, and the extraction-relevant outcomes are its payoff.
   - *Provenance caveat.* The user attributes this gap to Shiyin Li. The transcripts support it only indirectly: Shiyin proposed a public release that runs on users' own keys (08-25, 01:04:12), and Lin praised that "the whole thing can be reproduced" (08-25, 00:45:41, L478). Before the gap is written in her terms, confirm the wording with her.
2. **Design label.** "Meta-epidemiological study" is dropped as the design label. It implies we estimate properties of the trial literature, which contradicts C's M3. The new label is **"development and exploratory application of a screening workflow"**.
   - Lin asked for meta-epidemiological reporting items (08-25, 00:57:34). They can still be applied to the application part. Lin must agree to this.
3. **Methods weight.** About half of the Methods now specifies the workflow (§3).
4. **Abstract and storyline.** These now lead with what the workflow hands a verifier: candidates, then confirmed, then flags reviewed per confirmed issue. θ₁ and θ₁ₛ follow, worded as in C's M3, and θ₂ comes last as the payoff (C's §3.1, accepted).
   - θ₁ remains the **prespecified main descriptive measure** (B's term), not a confirmatory primary outcome.
   - *Reconciling with 0630 (C's challenge).* 0630 prespecified both θ₁ (primary) and the confirmed share of flags ("PPV of LLM flags", secondary). Leading with the confirmed share therefore reorders two prespecified outcomes; it adds no new one. The reordering follows the mentor's reframing and happens before any human verification. It is dated in Table S1 and stated in M4.
5. **"Replicable" is split in two.**
   - The *procedure* is re-executable: versioned, hashed, with a fixed model ID.
   - Whether its *output* is reproducible across runs is uncharacterized unless a small stability rerun is done.

   Under a skill framing, that rerun moves from "desirable" to **strongly recommended** (§4). Following C, procedural replicability also needs a **second operator**: Shiyin runs the release from the README alone on 2–3 packages. Without the rerun and the second operator, the paper says "formalized and publicly released", not "replicable".
6. **Adopted from C:** must-include sentences M1–M9, must-avoid terms N1–N7, calibration κ before the main review, and "flags reviewed per confirmed issue".
7. **Adopted from B:** the intended-use statement, the failure-mode table, the reuse and packaging subsection, cost recovery, and Box 1, "Using the workflow".
8. **Guardrail against crediting the architecture (C's trigger).** The workflow's features may be *described* as specification. They may not be *credited* with the yield. Once a feature is credited, a single-prompt baseline becomes required.

## 1. Central question, storyline, titles

**Question.** Can agentic LLM checking of internal reporting consistency be specified as a reusable, inspectable procedure? When that procedure is used as an exploratory screening aid on complete *JAMA* RCT packages (article, supplements, protocol, SAP), we ask:
- what it hands to human verifiers;
- how much of it survives verification, and at what cost;
- how often a confirmed issue leaves a value that a systematic reviewer would extract undeterminable from the package.

**Storyline (one sentence; answers C's three tests).** We specify a versioned, human-in-the-loop multi-agent LLM workflow for flagging internal reporting inconsistencies in randomized trial packages; used as a screening aid on 44 *JAMA* RCT packages, it raised [N] candidates, of which two reviewers confirmed [n] (about [1/p] flags reviewed per confirmed issue; [t] reviewer minutes per package), including confirmed issues in [k₂] packages that left a value a systematic reviewer would extract undeterminable from the package, while what it misses was not assessed.
- Test 1: no N1–N6 terms.
- Test 2: every bracket comes from human-verified data or logged minutes by 26 October.
- Test 3: no implication about the *JAMA* literature.

**Titles** (a subtitle appears only where it names the design):
1. A reusable multi-agent large language model workflow for flagging internal reporting inconsistencies in randomized trial packages: development and exploratory application to trials in *JAMA*
2. Flagging extraction-relevant reporting inconsistencies in randomized trial packages with a human-in-the-loop large language model workflow: development and exploratory application
3. Specifying agentic large language model checks of internal consistency in randomized trial reports, with an exploratory application to *JAMA*, 2018–2019 and 2024–2025

## 2. Outcomes (all descriptive; prespecified vs added, dated)

**Definitions** (unchanged from v3).
- *Report-domain flag:* pipeline-assigned statistical_results (175) or report_internal_inconsistency (9), 184 in total. plan_material (37) and protocol_report (219) are reported separately.
- *Confirmed:* human consensus retains the flag with H = confirmed_issue, or with K a substantive or minor inconsistency. A variant also counts probable_issue.
- *Substantive:* I = substantive, or K = substantive_inconsistency.

**Intervals.** All intervals are 95%. They describe uncertainty for packages like these 44 (selection undocumented), not for *JAMA* RCTs.

| Set | Measure | Unit / denominator | Interval |
|---|---|---|---|
| **A. Prespecified (0630, 30 June)** | Share of report-domain flags confirmed, with denominator = pipeline-assigned domain (B and C now agree). Variant counting probable | Flag / 184 | Paper-cluster bootstrap (2,000 resamples, seed 20261030) |
| A | θ₁ (packages with ≥1 confirmed report-domain issue), always with θ₁ₛ (≥1 substantive) and the M3 sentence | Package / 44 | Clopper–Pearson |
| A | Confirmed issues per package, by category, location and substantiveness | Package / 44 | Median (IQR); cluster bootstrap |
| A | Review minutes per package | Package / 44 | Median (IQR) |
| **B. Added (dated amendment, frozen before human review)** | **θ₂ (the extraction payoff):** packages with ≥1 confirmed issue whose value is determinable "only externally" or is "not determinable" (3-level field), plus the distribution of the field over confirmed issues | Package / 44; issue | Clopper–Pearson; κ for the field |
| B | Flags reviewed per confirmed issue (1/share confirmed); unconfirmed flags per package | Flag; package | Inverted bootstrap interval; median (IQR) |
| B | Confirmed issues per 100 pages, main article vs results supplements | Role within package | Poisson GLMM rate ratio, log-pages offset |
| B | κ (calibration, then main review), for disposition, issue status and determinability | Flag | Paper-cluster bootstrap |
| B | Candidates matching published *JAMA* corrections ("r of s"); no recall label | Erratum item | Counts |
| B | Workflow execution: wall-clock time, agents per run, failures (failure-mode table), tokens or cost if recoverable | Run / 44 | Median (range) |
| **C. Descriptive** | protocol_report flags by plan element, L field and disclosure; no verdict | Flag / 219 | Counts |
| C | Funnel from findings through reason codes to flags to dispositions; pipeline vs human domain | — | Counts |
| **D. Hypothesis-generating (supplement only)** | Per-period θ₁, θ₁ₛ, θ₂ with intervals; risk difference with Newcombe interval; no count model, no P value | Package / 19 vs 25 | Clopper–Pearson; Newcombe |

The θ₁ vs θ₂ question is settled (C conceded in round 3):
- θ₁ keeps its prespecified status.
- θ₂ is the added payoff, defined before review.
- Both are reported together and labeled.

## 3. IMRaD outline (AJE Practice of Epidemiology, ≤4,000 words)

**Abstract (200 words), in this order:**
1. The problem.
2. The workflow and its intended use.
3. The application (44 packages, years, plans included).
4. Candidates → confirmed → flags per confirmed issue; minutes per package.
5. θ₁/θ₁ₛ, worded as M3.
6. θ₂.
7. "Recall was not assessed; flags require human verification."

**Introduction (about 450 words).**
- **P1 (the user).**
  - Extraction errors in adverse-event systematic reviews are frequent and can change pooled results [Xu 2022].
  - Xu's error definition treats the report as correct [Xu 2022].
  - Inconsistencies inside a package therefore sit upstream of extraction. This is our argument and Lin's priority.
- **P2 (the problem).**
  - Reporting inconsistencies occur [citation needed].
  - Supplements and plans are long and receive little checking [citation needed].
  - Deterministic checkers cover narrow patterns [citation needed: statcheck; GRIM].
- **P3 (LLM checkers so far).**
  - Single-prompt checks on the main document report useful flags, with human or LLM judgment of flags [La 2026; Zhang 2025].
  - Journals require AI use to be fully described and author-verified [Flanagin 2026].
- **P4 (gap, in the skill framing).**
  - C's sentence, adopted pending a documented search: "Among the studies we identified, large language model checks of internal consistency used a single prompt applied to the main manuscript, and only one published its prompts and code [Zhang 2025; La 2026]; we found none that released a multistage agentic workflow with written inclusion rules and source-anchored evidence for complete trial packages, including protocols and statistical analysis plans."
  - Ruta 2025 publishes a prompt template for a different task; Zhang publishes prompts, model snapshots and code. "No templates exist" is therefore **not** claimed.
  - Deterministic consistency tools are formalized by construction and must be acknowledged [citation needed: statcheck; GRIM/GRIMMER].
- **P5 (aim).**
  - Specify such a workflow.
  - Describe its first exploratory application to *JAMA* RCT packages, with the extraction-relevant yield as the payoff.

**Methods (about 1,600 words; roughly half on the workflow).**
1. **Intended use** (B, with M1, M2 and M7).
   - Users: statisticians, systematic reviewers and data extractors, and authors checking their own work before submission.
   - Not for: confidential manuscripts under review, misconduct screening, or verdicts on papers (N6).
2. **Workflow specification** (Figure 1: architecture).
   - Inputs and document roles (REPORT/PLAN), relationship codes, and the four review domains.
   - Stages: inventory and hashing; mapping; three checkers; an independent inclusion screen; registration; evidence recheck; statistical pass 2; auditor; report; structural validator.
   - Candidate rules, as design choices:
     - route A (always-register categories);
     - route B (in focus, unresolved by context, bearing on interpretation *or which value an extractor would take*), which is where the workflow's own design encodes Lin's extraction priority;
     - the display-precision rule;
     - one candidate per issue; no cap; vocabulary rules.
   - Human-in-the-loop constraints: agents assign no disposition or severity and delete no IDs.
   - Outputs: evidence cards, the screening log as a user-auditable record of what was dropped, the ledger, and the HTML report.
   - The agent-role table goes in the supplement.
3. **Implementation and reuse.**
   - Workflow 1.6.2 is frozen with hashes. The exact model ID (`gpt-6.1-sol`) is configurable, with reasoning effort set per role.
   - Requirements: Codex CLI, CPU-only operation, pinned fallback tooling. Expected time per package.
   - Release under the user's own provider account (Shiyin's request), with the README carrying M1, M2 and M7 and stating that results are specific to this model.
   - A port to other agent frameworks or "skills" is untested.
4. **Human verification protocol.**
   - The v2.4.1 Codebook, rebuilt with J required and the 3-level determinability field.
   - Order of review: title and locations, then source, then card.
   - Calibration κ on 2 ExtraPapers packages before the main review (C).
   - Independent dual review of all 221 non-protocol flags.
   - protocol_report flags single-coded, crossed over periods, with a random 20% dual-coded.
   - Consensus with Lin. An optional external statistician.
   - A file-access check of `reviewer_runs/`. Minutes logged. M6 stated.
5. **Application cohort.**
   - Eligibility and online-first dating, with the selection rule documented.
   - 14231 excluded.
   - Clean reruns of the 5 annotated packages.
   - Table S1 lists the departures from 0630 (M4) and the in-sample status (M5).
6. **Analysis.** As in §2. R with `sessionInfo()`. Scripts tested on mock data. No hypothesis tests.
7. **Ethics, permissions, AI disclosure.**
   - The text-and-data-mining basis.
   - No PDFs redistributed.
   - M9.

**Results (about 1,100 words).**
1. **Runs** (Table 1 and the failure-mode table). Packages by period; wall-clock time (median 66 minutes, range 35–131; B); agents per run; failures and their handling.
2. **Figure 2.** The funnel.
3. **Figure 3.** One annotated evidence card per domain, showing what a user receives (neutral tone; identifiers in the supplement).
4. **Table 2.** Share of flags confirmed by domain, flags per confirmed issue, substantiveness, location (per 100 pages), and determinability.
5. **The extraction payoff.**
   - θ₂ and the determinability distribution.
   - Box 2: 3–4 examples in which an extractor could not tell which value to take.
6. **Package level.** θ₁/θ₁ₛ with M3. Figure 4: dot plot of confirmed and unconfirmed flags against pages, showing burden.
7. Matches with published corrections; κ.
8. Protocol–report differences, descriptive (Table S-PR).
9. Stability rerun, if done. Per-period table in the supplement.

**Discussion (about 800 words).**
1. **What the procedure contributes.** A rerunnable specification with an inspectable trail. The yield is not credited to its design (M8).
2. **What a user can expect.**
   - The verification workload.
   - Where confirmed issues sat.
   - The extraction payoff: for systematic reviewers, a flag is a prompt to resolve the value from the report, registry or authors (M7). It may help locate values that need checking, but this was not evaluated (N2).
3. **Box 1, "Using the workflow"** (B):
   - who runs it and when;
   - inputs;
   - which model, and what to record;
   - expected time;
   - how to review a card;
   - how *not* to read an absent flag (M2) or a protocol_report flag;
   - how to disclose use (Flanagin).
4. **Limitations.**
   - Recall not assessed.
   - In-sample rules (M5).
   - Selection.
   - Reviewers who developed the workflow, and anchoring (M6).
   - One model; Codex dependence.
   - Run-to-run variability uncharacterized unless the stability rerun is done.
   - Assets reused from earlier versions.
   - Training-data exposure.
5. **Before any confirmatory use.** A frozen held-out set; planted and naturally corrected known-truth items; comparators (single prompt, deterministic checkers, human-only review); cross-model stability; independent verifiers; cost; and a user study [Goh 2024; Mazor 2025].

**Supplement (at most 5 files) and repository.**
- **S1:** specification appendix (role table, rules, prompts, contract) and Table S1.
- **S2:** results tables (per package; Table S-PR; funnel by reason; sensitivity analyses; per-period table; corrections).
- **S3:** worked examples with page locators.
- **S4 (optional):** LLM-run judgments vs human consensus, labeled as such.
- **Repository** (DOI; anonymized link for review): the frozen release, the human workbooks and the R scripts. No PDFs.

## 4. Actions before 30 October (today is D−16)

| Date | Action |
|---|---|
| D−16 to D−15 | Freeze and commit the amendment: set A–D measures, the θ₂ rule and hypothetical examples, the abstract order, and the M/N lists. Lin signs off on the design label and on demoting the period contrast. |
| D−15 | Rebuild the Codebook and blanks; run the validators; Excel smoke test. Document the selection rule. Send the TDM query. Recover token and cost data and the Codex version from the session logs. |
| D−15 to D−13 | Clean reruns of the 5 annotated packages. **Stability rerun:** 2 additional runs on 8 packages (2 per year; C's size), compared with the original by location and rule (Jaccard overlap; recovery of confirmed issues once verification ends). This is machine time plus one person checking the matches. **Second operator:** Shiyin runs the release from the README on 2–3 packages and logs procedural failures. |
| D−14 | Calibration and κ on 2 ExtraPapers packages; revise the guide if κ is poor. |
| D−14 to D−5 | Independent dual verification of the 221 flags; protocol_report coding; minutes logged. |
| D−14 to D−6 | Corrections search. Package the release (README with M1, M2 and M7; hashes). Write the Methods specification. Write the R scripts on mock data. |
| **D−4** | Consensus, then **go/no-go**: complete dual verification; amendment predates the first human judgment; selection documented; permissions position; clean reruns done. |
| D−4 to D−1 | Analysis, writing, Lin's review, disclosure. |

Without verification, the paper does not go. "Exploratory" never justifies partial verification (N7).

## 5. Points to reconcile with B, C and Lin

1. **Design label (with Lin).** "Development and exploratory application" (A, B, C) vs Lin's wish to follow a meta-epidemiological guideline. Proposal: keep the meta-epidemiological items for the application part only.
2. **Period contrast (B vs A; Lin).**
   - B wants no contrast estimate at all.
   - A wants a Newcombe risk difference with its interval in the supplement, labeled hypothesis-generating, because Lin asked for the comparison (email of 5 September; 08-25) and the group's rule is an estimate with an interval rather than a bare table.
   - C wants it in the supplement only.
   - Lin must agree to demote it from the main text.
3. **Abstract lead.** C's verification-yield-first order is adopted here. B agrees. Check that Lin accepts θ₁ not being the first number.
4. **Stability rerun.** B: optional. A: strongly recommended under a "reusable skill" claim. If it is not done, the word "replicable" applies only to the procedure.
5. **Architecture credit (C's trigger).** Every author has to accept that the Discussion credits no feature of the design with the yield. Otherwise the single-prompt baseline returns as a requirement.
6. **Gap wording (with Shiyin and C).** Adopt C's sentence: Zhang released prompts and code; La did not; Ruta has a non-agentic template. Confirm Shiyin's formulation with her and run the documented search before submission.
7. **Article type (C: choose one).** A: **Practice of Epidemiology**. The workflow is the method of an exploratory evaluation, and Novel Methodology would bring kwag204's bar of a known-truth component, which this paper lacks. Revisit Novel Methodology after a confirmatory study. C asks the group to commit; B agreed with Practice of Epidemiology in round 3.
8. **"Replicable" in the title or abstract.** Only if the stability rerun and the second-operator run are both completed and reported; otherwise "formalized and publicly released".
9. **"Skill" portability.** B: Codex-only, port untested. Agreed. Do not call it a "skill" in the title unless it is packaged as one.
10. **External statistician.** C accepts treating it as a limitation if M6 is stated. A agrees. Still open: whether Lin can recruit one by 20 October.
11. **Determinability field.** B's 3-level version is adopted. C wants the rule frozen beforehand; it is in the amendment.
