# Drafter B, round 3: the exploratory-tool framing, with the specified workflow as a core contribution

Pipeline numbers come from `run_meta.py` in this folder. No adjudication number is used.

## 0. The "no rigorous, replicable skill exists" gap: where it is in the notes

I could not find this statement in the notes. In the only transcript where Shiyin speaks (`previous_meeting_notes/meeting_notes/20260825-MeetingWithDrLinAndShiyin_原文.txt`, speaker 3), her relevant turns are: post the workflow on GitHub (l. 471–472), decoupled so users run it on their own tokens (l. 693–694); cross-check with a second model (l. 513–514); add save and CSV export for adjudication (l. 579–585); and frame the periods as pre- versus post-GPT (l. 681–682).

These support a reusable, released workflow. They do not state a literature gap. If she said it elsewhere, the user should supply the source. Otherwise the gap must rest on the literature:
- Zhang 2025 used a single prompt and lists multi-agent designs, supplements and propose-then-verify as future work.
- La 2026 used one identical prompt across models.
- Beyond those two: [citation needed: documented search showing no published, versioned LLM workflow specification for internal-consistency checking].

## 1. The story and what it must show

**Story.** We specified, released and exploratorily applied a reusable multi-agent workflow (a "skill") for checking internal consistency. It turns a randomized controlled trial (RCT) package into page-located candidates for a statistician to verify. The workflow is defined by:
- fixed agent roles;
- a review contract;
- an evidence-card schema;
- quality-control (QC) gates;
- a validator;
- pinned settings.

We applied it to 44 *JAMA* RCT packages, people verified the flags, and we report what it surfaced, how much people kept, what it cost, and where it broke. The two contributions are the specification and a descriptive account of using it, not a performance claim.

**Intended use** (Methods, repeated in Box 1).
- *Users:* statisticians, systematic reviewers and data extractors, and authors checking their own manuscript before submission.
- *Not for:* confidential manuscripts under review (Flanagin 2026), misconduct screening, or verdicts on whether a paper is correct.
- *What a flag means:* a discrepancy, reproduced at a cited page under a stated rule, that the workflow could not resolve from context.
- *What a flag does not mean:* an error or a severity grade.
- *What an absent flag means:* nothing, because recall is unknown.
- *Protocol_report flags:* they describe differences between plan and report, not violations.

**Essential even for an exploratory study.**
1. **Human verification of every non-protocol flag.** Without it the paper reports output volume, not usefulness, and LLM adjudication cannot substitute.
2. **Traceability.** Show one evidence card per domain: the page link, the reproduced calculation, the qualifying route, the alternatives considered, and the recheck state. The screening log keeps each rejected finding with a reason code (215 of 789), so users can audit what was dropped.
3. **Human-in-the-loop by construction.** Agents may not assign disposition or severity, or delete IDs, and error vocabulary is banned.
4. **Burden.**
   - Runs took a median of 66 minutes (range 35–131), with 12–43 agents each. 40 of 44 exceeded their planning target.
   - Reviewer minutes per paper and unconfirmed candidates per paper still need to be logged.
   - Tokens and cost were not recorded. Recover them from the Codex session logs, or state that they are missing.
5. **A failure-mode table:** garbled or missing plans, 3 runs that had to be completed, network-blocked tooling, annotated input PDFs, domain misassignment, recheck outcomes (4 transcription corrections, 1 not reproduced, 5 questioned by the auditor), reliance on reused derivatives (605 of 5,560 units fresh), and a validator that checks structure only.

## 2. What "rigorous and replicable" must mean, and what we can claim

Separate four levels and claim only what is shown.

| Level | Meaning | Status |
|---|---|---|
| **Specified** | Another team can run the identical procedure | **Shown.** Ten role presets, START_PROMPT, scope and contract, evidence-card schema (21 fixed fields), report spec, `settings.toml`, command allow-list, and pinned fallback tooling. The model is an exact ID, never a moving alias, and the coordinator stops instead of substituting. |
| **Traceable** | Each run can be audited after the fact | **Shown for all 44 runs.** Routing preflight, a manifest of every agent with runtime ID, model and reasoning effort, timing, tooling record, SHA-256 hashes of sources and reused assets before and after, the screening log, and validator PASS. |
| **Reproducible output** | A rerun returns the same candidates | **Not shown.** No repeated runs. No temperature or seed control in the settings. The provider may change a model behind a fixed ID. Each run reused derivatives left by earlier, year-specific pipeline versions, so a cold-start run follows a different input path. Compute device varied (one run requested GPU OCR). |
| **Portable** | It works with other models, agent frameworks or journals | **Not shown.** Codex CLI only, one model, *JAMA* RCTs only. |

**Claim:** "a fully specified and traceable workflow". Do not claim "replicable results" unless the minimum below is done.

**Minimum to claim run-to-run replicability (now essential, no longer optional):**
- On 3–4 packages stratified by period and size, run twice more with the frozen release.
- Make one of those runs a cold start with no reused assets.
- Match candidates by location and rule. Report per-paper overlap and the share of human-confirmed candidates found again. Adjudicate only the new flags.
- Record the Codex CLI version, the model ID and dates, and tokens.

This costs machine-hours plus a few hours of human time. If it is not done, the Discussion says output reproducibility is untested.

**Release requirements:**
- A tagged release with a DOI and hashes of every control file.
- A worked example on an openly licensed RCT package, so others can rerun end to end, since the *JAMA* PDFs cannot be shared. [Choose a CC-BY trial report; none chosen yet.]
- The human codebook and workbook builder ship as part of the template, because adjudication is half the procedure.

## 3. Future work vs essential

**Future work, stated as untested:** a held-out frozen cohort (the 44 papers remain the development set); planted errors (no sensitivity claim); a single-prompt baseline (no claim that the architecture adds value); ports to other models and frameworks.

**Essential:** dual human review; codebook and analysis plan frozen before review; Table S1 (departures from 0630); clean reruns of the 5 annotated packages (I now agree with A and C); a documented selection rule; a permissions statement; the errata check; the minimal stability rerun.

**Language to drop:** "sensitivity", "accuracy", "validated", "detects errors", "outperforms", and "PPV" (positive predictive value) used as a diagnostic-accuracy term. Say "share of candidates confirmed on human review", with paper-clustered intervals.

## 4. Outline changes

**Titles:**
1. A specified multi-agent large language model workflow for surfacing statistical reporting inconsistencies in randomized trial reports for human verification
2. A reusable, evidence-traced large language model workflow for internal-consistency checking of randomized trial reports: development and exploratory application to *JAMA* trials

**Abstract, in this order:** the problem; the specified workflow and its intended use; the application (44 *JAMA* RCT packages, 2018–2019 and 2024–2025); descriptive outputs (candidates per paper, share confirmed by domain with intervals, papers with at least one confirmed candidate, machine and reviewer time); one sentence on failure modes; "a screening aid; recall and [output reproducibility] not assessed."

**Methods:**
1. Intended use.
2. **The workflow specification.**
   - *Figure 1 (main text)* shows the procedure as a specification, not a cartoon: the stages, the artifact each stage must write, the gates (inclusion screen, recheck, statistical pass 2, auditor, validator), and what each gate enforces.
   - *Table 1 (main text, compact)* lists each component, its file, what it fixes, and how compliance is checked.
3. Candidate rules, presented as design choices.
4. Human verification protocol and codebook.
5. Release and reuse.
6. Application cohort.
7. Stability rerun.
8. Descriptive analysis.

**Supplement S1:** the full specification (scope, contract, report spec, settings, presets, validator conditions) in one file of 2 MB or less. The **repository** holds the release, the worked example and the run logs.

**Results:**
1. Runs and failures (Table 2 and the failure-mode table).
2. Figure 2: screening funnel through to human disposition.
3. Figure 3: one evidence card per domain.
4. Share confirmed by domain (pipeline-assigned denominator), substantive versus minor, determinability, and location.
5. Burden (Figure 4).
6. Stability.
7. Protocol–report differences, descriptive.
8. Per-period table (supplement).
9. Errata.

**Discussion:** what a user can expect; what the specification makes auditable and what it cannot guarantee (model drift, nondeterminism); untested design choices; limitations and future validation.
- **Box 1, "Using the workflow":** who runs it, the record to keep (release tag, model ID, dates, tokens), expected time, how to review a card (source first), how not to read absent flags or protocol_report flags, and the disclosure fields from Flanagin 2026.

**Article type:** AJE Practice of Epidemiology still fits ("AI/ML applications… implementation"). Fallbacks: *Research Synthesis Methods* or BMJ Open (Lin's original suggestion, Mentor会议总结 §二.4).

## 5. Disagreements with v3 that still stand

1. **Design label.** Call it "specification and exploratory application of a screening workflow", not "meta-epidemiological study with tool evaluation".
2. **Estimand table.** It reads as confirmatory. Keep θ₁ as the prespecified *main descriptive measure*, always paired with the share confirmed and θ₁ₛ. Report θ₂ descriptively. The errata row is "matches to published corrections", not recall.
3. **Period contrast.** Report per-period proportions with intervals in the supplement and fit no contrast model.
4. **v3 omits the tool core.** It needs the specification as a contribution (Figure 1 and Table 1 in the main text), the replicability levels, the stability rerun, the intended-use statement, the failure-mode table, cost recovery and Box 1.

**Conceded to v3:** the pipeline-assigned denominator, the clean reruns as a precondition, and the held-out cohort, planted errors and baseline as future work.
