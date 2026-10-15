# Agent C, round 2: dispute of A_round1 and B_round1

All evidence comes from `C_litmap.md`. Where a claim depends on something outside the folder, I mark it [citation needed].

## 1. Agreed; do not reopen

Both drafts:
- keep LLM workbooks out of the findings;
- choose Practice of Epidemiology;
- keep protocol_report descriptive;
- disclose post hoc changes.

The annotated 2024–2025 PDFs need clean reruns before any period comparison is reported. A sensitivity analysis alone is not enough.

## 2. Drafter A

**Overclaim 1. The gap sentence is false as written.**
- A writes: "no audit of naturally occurring, extraction-relevant inconsistencies … with human adjudication of every flag."
- La et al. did manually adjudicate every additional flag in 40 published articles. These were naturally occurring inconsistencies: 337/355 judged genuine, 158 unique.
- What La lacks is complete RCT packages, extraction relevance, and any account of who adjudicated or how. The defensible gap is narrower, so drop "human adjudication of every flag" as the novelty.

**Overclaim 2. "Concentrated in supplements" and "a routine prepublication check could remove" assume the results.**
- *Supplements.* Supplements are longer than main texts, so more raw issues there means nothing without a rate per source unit or page. B's offset handles this; A's storyline asserts the conclusion before it has been measured.
- *Prepublication check.* Goh and Mazor both show that accurate AI output did not change downstream human or system outcomes. Flanagin bars entering confidential manuscripts into external AI tools during peer review. The only use we can defend is one by authors before submission, or by reviewers after publication. Our data test neither.

**The "prevalence lower bound" headline (θ₁) is defensible on paper but misleading in practice.**
1. **It will be trivially high.** In the provisional, non-human pattern A tabulated, 139 statistical rows are coded confirmed and 102 of them minor_presentation. La found 158 pre-existing inconsistencies in 40 articles, most of them rounding. If minor items count toward θ₁, it will probably lie close to 1. A headline saying "≥1 issue in nearly every JAMA trial" would be read as an error rate, whatever the label says. It also cuts against Lin's tone requirement (A's L5).
2. **It is a lower bound for a population we never sampled.** With an undocumented sampling frame (A's Gap 2), the bound applies to these 44 packages only. The word "prevalence" invites readers to generalize beyond them.
3. **The bound is one-sided only if confirmation is error-free.** Reviewers who built the tool, adjudicating with the AI card in front of them, can over-confirm (incorporation and anchoring bias). Over-confirmation breaks the "lower" in "lower bound".

**Proposal.** Demote θ₁ to a descriptive secondary. Promote A's θ₂ (the package does not let a reader determine the value a systematic reviewer would extract) to primary, reported as detected yield rather than prevalence.
- θ₂ is the construct that connects to Xu, which no folder paper measures.
- Condition 1: the "value determinable" field was created after the LLM runs were seen. It must be defined with an operational rule and worked examples, and frozen in the SAP amendment before any human adjudication.
- Condition 2: its agreement between the two reviewers must be reported, because it carries the whole storyline.

**The sensitivity substudy (Gap 5a) is the right idea at the wrong size.**
- Two papers per year is 8 clusters, restricted to selected displays. It estimates recall for those displays only, against humans who are themselves imperfect, and the interval will be very wide.
- Label it "display-restricted recall in an 8-paper audit" and do not let it stand in for sensitivity.
- §4 below proposes a cheaper anchor with known truth.

**Underclaim.** A treats extraction relevance as already established by citing Xu. Xu's reference standard assumes the trial report is correct: an extractor who matches either of two conflicting values "has no error". This blind spot is our strongest citable argument, and A should say it outright.

## 3. Drafter B

**PPV and yield are not novel enough to be the primary contribution.**
- Both competitors already report the quantity: La reports the proportion of extra flags judged genuine (94.9%), and Zhang reports AP@5 (best 35.2).
- An AJE reviewer will put our PPV next to La's 94.9% at once. Any difference will be blamed on the threshold, because La counts rounding and we screen it out.
- PPV is a property of our inclusion rules × our papers × our reviewers. B already concedes it is in-sample (apparent) because the rules were tuned on these papers. A headline that is non-portable and in-sample is weak.
- **Keep PPV and burden as secondary** (unconfirmed flags per paper, reviewer minutes). The burden measures are partly new: Zhang reports cost per paper, and La reports no burden.

**Overclaim. The gap statement misdescribes prior work.**
- B says "prior checkers are single-prompt, their output is not traced to sources …".
- Single-prompt is correct for both Zhang and La.
- "Not traced to sources" is wrong. La reports that all 98 detected planted errors were "exactly localised". Zhang's output schema requires a Location field.
- What is new is **independent reproduction of each finding plus a written inclusion screen before registration**, not localization.
- "Evaluated without plan documents" is correct for Zhang. For La, write "did not report using".

**What an AJE reviewer will attack first.**
- "This is a software description with an in-sample PPV, no comparator and no recall. What does the 12-gate multi-agent architecture add over the single prompt that La reports at 81.7% planted-error sensitivity?"
- B offers the design features as untested hypotheses, so the central contribution shows nothing.
- **Cheapest fix:** a single-prompt baseline (same model, Zhang/La-style prompt) on the same or a stratified subset of packages, comparing overlap, confirmed yield and θ₂ yield. Without it, the AI-framework framing does not hold.

**The held-out cohort is not clean.**
- `/home/juliz/ai-paper-val/ExtraPapers/` holds 10 papers: 6 in 2017 and 4 in the 2020 folder, one of which is jama.2019.20207.
- Every one already contains `.ai_paper_validation/` output from Workflow 1.5.1 or 1.5.2. They are held out only if nobody looked at those outputs while 1.5.3–1.6.2 were being designed. That has to be documented, not assumed.
- They also fall outside both period strata.
- Call them a "temporal-external check", not a validation cohort, unless the provenance is clean.

**Technical point.** In a hierarchical logit model, a logistic prior on the intercept is uniform for the *median-paper* PPV, not the mean PPV. State the prior on the parameter actually estimated. B's "feasible before publication" claim runs into the same Flanagin limit as A's.

## 4. Gaps neither draft addresses

1. **Reviewer independence.** Bulun built the workflow and Shiyin is a coauthor; both will adjudicate. An AJE reviewer will raise this.
   - Add an external statistician to adjudicate a random subset, blinded to the pipeline's reasoning text where possible, and report agreement with the consensus.
2. **A natural reference standard already exists: published corrections.**
   - JAMA posts corrections ("Error in …"). For the 2018–2019 papers, check every subsequent correction notice. The question is whether 1.6.2 flagged the issues JAMA later corrected.
   - This is a known-truth recall subset of *naturally occurring* errors, available before any human adjudication. Neither planted errors (La, kwag204) nor a small audit offers this.
   - Caveats: a post-correction PDF has already removed the error, so check the ingested version; and models may know the correction (contamination, as Zhang notes).
   - [citation needed: corrections/errata frequency in high-impact journals]
3. **Copyright and text-and-data mining.** JAMA PDFs reserve "text and data mining, AI training". Sending them to an external provider needs a stated legal and licence basis in the Methods, alongside the AJE disclosure of AI use.
4. **Literature search.** Our "prior work" is an 8-paper folder. "No study has compared reported analyses with the protocol/SAP using LLMs" needs a documented search before we write it; otherwise write "among studies we identified" and describe the search.

## 5. Introduction gap statement: what we can cite today

| Sentence | Support |
|---|---|
| Data extraction errors are frequent in systematic reviews of adverse events and can change pooled conclusions. | Xu 2022 ✓ (state the adverse-events and binary-outcome scope) |
| Xu attributes part of these errors to poor or ambiguous trial reporting, and its reference standard treats the trial report as correct. | Xu 2022 ✓ (Xu's interpretation; their definition of error) |
| Statistical reporting inconsistencies are common in published biomedical articles. | [citation needed]. La's 158 inconsistencies, detected by LLMs and mostly rounding, are weak support. |
| Supplementary materials receive less scrutiny than main texts. | [citation needed]. Lin's view is not citable. |
| Protocol/SAP–publication discrepancies in RCT outcomes and analyses are common. | [citation needed: outcome-switching / selective reporting] |
| Deterministic checkers exist for test statistics and granularity. | [citation needed: statcheck; GRIM] |
| LLMs detect planted internal inconsistencies with high sensitivity once given a manuscript. | La 2026 ✓ |
| LLMs recover authors' stated critical errors in about half of withdrawn preprints. | Zhang 2025 ✓ (workshop preprint; flag its status) |
| Prior evaluations used one prompt on the main document, and judged flags by LLM or by unspecified manual review. | Zhang ✓, La ✓ ("did not report" for La's supplements and adjudicators) |
| Journals require full disclosure of AI in research and bar external AI in confidential peer review. | Flanagin 2026 ✓ |
| No study has assessed whether source-report inconsistencies leave extractable values undetermined, or compared reported analyses with protocols using LLMs. | Needs a documented search; until then [citation needed / "among studies identified"] |

## 6. My version of the central question

**Question.** In complete JAMA RCT packages (article, supplements, protocol, SAP), how many human-confirmed reporting issues that leave a value a systematic reviewer would extract undetermined does an evidence-grounded multi-agent LLM workflow surface? And what does it cost the reviewer, compared with a single-prompt checker?

**One-sentence storyline (the drafters must answer each bracket).** Inconsistencies within a trial report are an upstream source of extraction error that existing extraction-validity work treats as ground truth. Applied to [44] JAMA RCT packages, an evidence-grounded LLM workflow surfaced [n] human-confirmed issues in [k] papers that leave an extractable value undetermined, at [m] unconfirmed flags per paper. That is [more/fewer] than a single-prompt checker, and it recovered [r of s] issues JAMA later corrected; recall otherwise remains unknown.

**Hierarchy implied:**
1. Primary: θ₂ yield.
2. Secondary:
   - PPV and burden;
   - θ₁;
   - single-prompt comparison;
   - recall against corrections.
3. Descriptive:
   - protocol_report;
   - stability.
4. Exploratory: the period comparison, only after clean reruns.

**Deadline.** Do not submit on 30 October with LLM adjudication. The only honest product by that date is a 1,500-word Research Letter with no confirmation claims, and it would spend the novelty.
