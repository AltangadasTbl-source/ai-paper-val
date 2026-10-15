# Agent C, round 3: challenge under the exploratory screening-aid framing

Sources: `C_litmap.md` and v3. Framing: an exploratory screening aid whose candidates need human verification; descriptive study.

## 1. How the literature positions a screening aid

- **Zhang 2025 and La 2026.** Zhang casts LLMs as "manuscript quality checkers" with "human experts … at the center"; La calls them "complementary". Both still report performance metrics.
- **kwag204.** Its framework "emphasizes identification and exploration … rather than automatic exclusion". AJE published it as a triage tool **with** sensitivity, specificity and precision against injected outliers, and with code on GitHub.
- **Flanagin 2026.** Fits the framing: authors "check for accuracy and take full responsibility". Use by authors, or after publication, avoids the confidentiality bar on manuscripts under review.

**Net effect.**
- *Strength.* We no longer compete with La on sensitivity or with Zhang on a benchmark.
- *Weakness.* Every precedent, including AJE's own triage tool, evaluated its aid. Without verified output, an AJE reviewer will see a software description.

**Minimum evaluation even for an exploratory aid:**
1. Two-reviewer human verification of all candidates outside protocol_report, with κ.
2. The confirmed share of flags with paper-clustered intervals, also expressed as flags reviewed per confirmed issue (1/PPV).
3. Reviewer minutes per package.
4. The screening funnel with reason codes.
5. "Recall unknown", with the errata anchor if s > 0.
6. A frozen, hashed version with run metadata.

## 2. Where "exploratory" could become a shield

**The paper must contain:**
- M1. "The workflow is a screening aid: each candidate requires human verification, and an unverified candidate is not evidence of an inconsistency."
- M2. "Because only flagged candidates were reviewed, we could not estimate how many inconsistencies were missed; the absence of a flag does not indicate a consistent report."
- M3. "The proportion of packages with ≥1 confirmed issue describes the yield of a human-verified screening process in 44 selected packages, not the prevalence of inconsistencies in *JAMA* or in randomized trials."
- M4. "[θ₁] was prespecified in the protocol dated 30 June 2026; [θ₂, protocol_report, the 2018–2019 cohorts …] were added afterward (Table S1)."
- M5. "The screening rules were revised after output on the 2018–2019 packages had been seen."
- M6. "One reviewer developed the workflow, and both reviewers saw its evidence cards."
- M7. "A flag is a prompt to resolve the value from the report, registry or authors, not a corrected value."
- M8. "We did not compare the workflow with a single-prompt approach."

**The paper must not contain:**
- N1. "detected N errors", "error rate", "accuracy".
- N2. "useful", "effective", "reliable" or "saves time". Permitted: "may help locate values needing checks; not evaluated" (see Goh, Mazor).
- N3. "validated", except in "has not been validated". Title verb: "flagging", not "detecting".
- N4. Any reading of the period contrast as a change in reporting quality, or any link to LLMs or COVID-19. It stays out of the abstract.
- N5. "prevalence", including "lower bound of prevalence".
- N6. Any suggestion that editors screen submitted manuscripts with it, or that it replaces peer review.
- N7. Exploratory status used to omit intervals, present LLM-adjudicated numbers, or add undated outcomes.

v3's "meta-epidemiological" label (title option 3, Methods 1) contradicts M3. Replace it with "exploratory descriptive evaluation of a large language model screening workflow".

## 3. Shiyin's gap claim: "no formalized, rigorous, replicable agentic skills or templates for internal-consistency checking"

**What the folder papers publish:**
- **Zhang.** The most replicable as printed:
  - the checker and judge prompts verbatim (Appendix A);
  - model snapshots with dates (e.g., o3 2025-04-16) and parameters (Appendix B);
  - dataset, code and model outputs on GitHub.
  - Limits: one run per paper; a single prompt; no agent design. Zhang lists "propose-then-verify" and "multi-agent collaboration" as future work.
- **La.** Not replicable as printed:
  - The "identical prompt" is not given, and models are named without snapshots or settings.
  - The planted manuscripts are not released; data are "available … on reasonable request".
  - There is no agent design.
- **Ruta.** Publishes its prompts (Multimedia Appendices 1–3), a best-practice textbox and 10 repeats per task. A prompt template, but neither agentic nor about consistency checking.

**Verdict.** "No templates" is false as a blanket claim: Zhang and Ruta publish templates. "No agentic workflow for this task" is supported only among the papers we hold. Existing deterministic consistency tools are formalized and replicable by construction, so a reviewer will cite them against us.
- [citation needed: statcheck; GRIM/GRIMMER]. Nuijten & Polanin 2020 is in Zhang's reference list.
- [citation needed: Black Spatula Project outputs]. The URL is in Zhang. We have not checked whether it publishes prompts.

**What we can cite now, and what we cannot:**
- Citable now:
  - Flanagin's disclosure minimum (tool, version, manufacturer, dates, description of use);
  - Zhang on output variability and contamination;
  - Graf and Ruta on prompt and time dependence.
- [citation needed]:
  - a reporting guideline for LLM-based research tools (TRIPOD-LLM or equivalent; verify it exists);
  - reproducibility of agentic or LLM workflows;
  - Flanagin et al. 2024, the JAMA AI reporting guidance (in Flanagin 2026's reference list).

**Evidence a reviewer needs before accepting "rigorous and replicable."** Distinguish *procedural* replicability (anyone can re-execute the same frozen procedure) from *output* replicability (re-execution yields the same candidates). Today we can support only part of the first.
1. **Pinning.** Model identifier and snapshot, Codex version, role presets and hashes. Some `run_state.md` files omit the model string.
2. **Public repository.** A DOI with the frozen 1.6.2 workflow, the prompts and the validator.
3. **Stability rerun.** At least about 8 packages, with candidate overlap (Jaccard) and recovery of confirmed issues. Without it, "replicable" output cannot be claimed.
4. **Second operator.** Shiyin runs it from the README alone on a few packages, and procedural failures are reported.
5. **Model dependence.** One proprietary model. Say that results do not transfer.

If items 3–4 are missing, the sentence becomes "formalized and publicly released", not "replicable".

**Coherence.** "A formalized, reusable exploratory skill plus a descriptive first application" is coherent only if **the skill is the object and the JAMA application is its first characterization**. Two consequences:
- θ₁ and the period contrast are audit-type estimands. They fit poorly and should sit below the §1 minimum. This reopens θ₁-as-primary, and A must reconcile it with the 0630 primary through M4.
- The center of gravity moves toward **Novel Methodology** (kwag204's type: an open framework with real-world application). That type brings kwag204's bar of a known-truth component. Under Practice of Epidemiology, the skill is the method of an evaluation.

Choose one. Writing half an audit and half a software release splits the paper.

**Proposed gap sentence (defensible as printed, after a documented search):**
> "Among the studies we identified, large language model checks of internal consistency used a single prompt applied to the main manuscript, and only one published its prompts and code [Zhang; La]; we found none that released a multistage agentic workflow with written inclusion rules and source-anchored evidence for complete trial packages, including protocols and statistical analysis plans."

## 4. Updated positions on v3's disputes

1. **θ₁ vs θ₂.** I concede to A on outcome switching: θ₁ stays the prespecified primary, paired with θ₁ₛ and M3. Conditions:
   - The abstract leads with the verification yield.
   - θ₂ is frozen before review.
   - If the skill framing in §3 is adopted, revisit the ranking openly with M4.
2. **Single-prompt baseline.** Not required if M8 is printed. It becomes required if the paper credits design features (the independent screener, reproduction, always-register rules) with better output, or calls the skill "rigorous" by comparison.
3. **30 October.** The framing does not lower the floor; human verification is what defines the aid. I accept v3's go/no-go rule and withdraw the Research Letter fallback. Add calibration κ before the main review.
4. **Period contrast.** Move it to the supplement in every scenario.
5. **Remaining disputes.** Pipeline-assigned PPV denominator; errata reported as "r of s corrected issues among candidates"; the external statistician may become a limitation, with M6.

## 5. Revised central question and storyline

**Question.** As an exploratory screening aid, what does a frozen, publicly released multi-agent LLM workflow hand to human verifiers when applied to complete *JAMA* RCT packages (article, supplements, protocol, SAP)?
- How many candidates?
- How many hold up, and at what review cost?
- In how many packages does a confirmed issue leave an extractable value undeterminable?

**Storyline.** We release a frozen multi-agent workflow for flagging reporting inconsistencies in trial packages. Applied to 44 *JAMA* RCT packages, it raised [N] candidates, of which reviewers confirmed [c] (about [1/p] flags per confirmed issue, [t] minutes per package), including issues in [k₂] packages that left an extractable value undeterminable. This justifies formal evaluation of such aids for evidence synthesis, but does not show what they miss or let them replace reading the source.

**Challenge.** Beat it with no N1–N6 word, with every bracket computable from human-verified data by 26 October, and with a choice of Practice of Epidemiology or Novel Methodology. If your sentence includes "replicable", name the rerun that supports it.
