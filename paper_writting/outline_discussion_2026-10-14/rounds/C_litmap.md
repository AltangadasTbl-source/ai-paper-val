# Agent C literature map (round 1)

Sources read: full text of all 8 PDFs in `potential_paper_2_cite/` (all have a text layer; extracted with PyMuPDF because poppler `pdftotext` is not installed), the two AJE examples (kwag195, kwag204), and both AJE guideline files. I skimmed the README, QUALITY_CONTROL_SCOPE and protocol 0630 for orientation only. Numbers below are as printed. "Not printed" means the PDF does not give the item. "No intervals printed" means the paper reports the proportion without a CI.

---

## 1. Paper-by-paper map

### 1.1 Xu et al. 2022 (anchor for extraction accuracy)

**Bibliographic details (as printed).** Xu C, Yu T, Furuya-Kanamori L, Lin L, Zorzela L, Zhou X, Dai H, Loke Y, Vohra S. Validity of data extraction in evidence synthesis practice of adverse events: reproducibility study. *BMJ* 2022;377:e069155. doi:10.1136/bmj-2021-069155. Accepted 10 April 2022; first published 10 May 2022. The byline as extracted assigns no author to affiliation 8, so check the PDF before citing. Lifeng Lin is a coauthor (Florida State University at the time). If he is on our paper, this citation is a self-citation.

**Design.** Reproducibility study of 201 systematic reviews of adverse events (PubMed, 2015 to 2020) containing 829 pairwise meta-analyses (each with 5 or more trials and 2×2 data) and 10 386 RCTs. Four authors re-extracted the data from the original sources (full text, supplements, ClinicalTrials.gov, company websites), followed by further rounds of double checking.

**Reference standard.** The original trial sources. A "data extraction error" is defined as trial data used in a meta-analysis that are "not the same as had been reported from one of its original sources".

**Main results.**
- Not reproducible: 1762 (17.0%) of 10 386 trials (extractor-adjusted 15.8%).
- Meta-analyses with at least one error: 554 (66.8%) of 829 (adjusted 65.5%).
- Systematic reviews with at least one such meta-analysis: 171 (85.1%) of 201.
- Taxonomy, as a share of the 1762:
  - numerical, 867 (49.2%)
  - ambiguous, 526 (29.9%), "mainly caused by ambiguous definitions of the outcomes"
  - zero assumption, 221 (12.5%)
  - misidentification, 115 (6.5%)
  - mismatching, 33 (1.9%)
- Impact, in the 288 meta-analyses without ambiguous errors:
  - 37 (12.8%) had a change of 20% or more and 13 (4.5%) a change of 50% or more.
  - 10 (3.5%) changed direction and 19 (6.6%) changed "significance".
  - Mixed versus single error types: moderate changes 28.2% vs 10.4% (P = 0.002) and large changes 12.8% vs 3.2% (P = 0.01).
- No intervals are printed for the headline proportions. Duplicate extraction was not associated with errors: odds ratio 0.9 (95% CI 0.3 to 2.5).

**Stated limitations.** Different extractors had different portions of the work (handled with a mixed model). Coverage is limited to 2015 to 2020. The 3.1% of trials whose sources were unavailable were treated as error-free (slight underestimate). RCTs only. Poor reporting of the extraction process limited the analysis of associations.

**Relation to our paper.** Xu supplies the motivation for our work, and its reference standard leaves a gap we can name.
- Xu treats the trial report as ground truth. When the report itself carries two values for one quantity, an extractor who takes either is not counted as in error. Xu attributes part of the "ambiguous" category to poor trial reporting ("varying terminology, poorly defined categories, and diverse data sources").
- Our candidates sit upstream, in the source. That is a defensible bridge: source-side inconsistencies are one mechanism behind the ambiguous and numerical extraction-error categories.
- We have not measured that mechanism. Xu's impact figures (3.5% direction change, 6.6% significance change) describe extraction errors in meta-analyses of adverse events, not our candidates, and must not be transferred to them.
- Caution on design claims. Xu's taxonomy was built after the data were seen ("on the basis of consensus after summarising"). Ours is not cleanly prespecified either. The 1.6.2 screening rules were revised after the 1.6.1 runs on the 2018 and 2019 packages (README, "Changes from 1.6.1"). For those cohorts the rules are post hoc, and we must say so.

### 1.2 Zhang and Abernethy 2025 (closest competitor 1)

**Bibliographic details (as printed).** Zhang TM, Abernethy NF. Reviewing Scientific Papers for Critical Problems With Reasoning LLMs: Baseline Approaches and Automatic Evaluation. 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: AI for Science. arXiv:2505.23824v3 [cs.CL], 1 Apr 2026. This is a workshop paper and preprint; no journal, volume or pages are printed.

**Design.** Benchmark built from WITHDRARXIV.
- Papers withdrawn from arXiv for "critical errors" were filtered, partly with an LLM, to 1,225 cases (WITHDRARXIV-CHECK).
- The test set is 245 papers: 52% math, 29% physics, 15% computer science.
- Five reasoning LLMs each listed up to k = 5 "most critical" problems from the PDF or the LaTeX source.
- The prompt was simple and single-pass. Models had no tools, no supplements and one run each.

**Reference standard.**
- Hits: the authors' own retraction comment.
- Precision: no gold standard ("there is no gold standard for precision evaluation"). Two LLM judges (Gemini 2.5 Pro and o3) both had to agree that a flag was a "true problem".

**Main results** (no intervals printed).
- HR@5 with PDF input: o3 48.2, Gemini 2.5 Pro 39.2, Gemini 2.5 Flash 38.4, o4-mini 38.0, Claude 3.7 Sonnet 11.0.
- With LaTeX input, o3 reached 50.6.
- AP@5 with PDF input: Gemini 2.5 Pro 35.2, o3 29.5, Claude 36.4.
- Claude found no problem in 64.9% of PDFs. o3 cost $0.064 per paper.
- The metric depends on the judge. For the same o3 checker, the Gemini judge gave a hit rate of 80.4 and the o3 judge 50.2. For the Gemini 2.5 Pro checker, the two judges gave 68.2 and 41.2.

**Stated limitations.** Closed models only; ambiguous retraction comments; single runs; a corpus heavy in math and physics. Evaluation was automatic and "without human involvement", which the authors call "circular evaluation of LLMs using LLMs"; they could not recruit domain experts. They also raise possible training-data contamination and call copyright "a key challenge".

**How we differ.**
- Domain and corpus. Ours is biomedical: RCT reports in one general medical journal (JAMA), with the main article, supplements, and protocol or statistical analysis plan (SAP). Theirs is mainly math and physics preprints, PDF or LaTeX only.
- Error class. They target "critical errors … that would invalidate the conclusions", with a reference standard drawn from retractions. We target reporting inconsistencies that bear on interpretation or extraction, in papers that were not retracted. We cannot claim to detect invalidating errors.
- Architecture. They name "propose-then-verify", "including supplementary materials", tools and "multi-agent collaboration" as untested future work. Our multi-agent pipeline (separate mapping, checking, an independent inclusion screen, evidence rechecking and an auditor) does all of these. This is our cleanest claim of novelty against them.
- Scale and denominator. They test on 245 papers but count at most 5 problems per paper. We have about 40 papers and 440 candidates, with no cap on candidates.
- Shared weakness. Our current "adjudication" consists of two Claude Opus runs. That is the same LLM-judges-LLM circularity they disclose. We must disclose it just as plainly and not present it as validation.

### 1.3 La et al. 2026 (closest competitor 2)

**Bibliographic details (as printed).** La E, Paris J, Agarwal A, Chan WO, Selva D. Large language models as internal consistency checkers for ophthalmic manuscripts. *Eye*; 2026. https://doi.org/10.1038/s41433-026-04965-5. Brief Communication, open access. Received 7 September 2026; revised 14 September 2026; accepted 23 September 2026. Volume, issue and pages are not printed.

**Design.**
- Sample: 40 published articles, "randomly selected from ophthalmic journals with an impact factor of > 3.0". Study designs are not stated.
- Planted errors: one prespecified inconsistency was planted in each of 30 articles, 10 for each type (percentage/count, sample size/subgrouping, statistical reporting). Ten articles were left unmodified. The text reads "introduced … without altering the manuscript", which is contradictory as printed.
- Models (names as printed): Claude Sonnet 5 High Effort, GPT-5.6 High Effort, GPT-5.5 Instant and Gemini 3.1 Pro. All used one identical prompt.
- Comparisons: Cochran Q test, then McNemar tests with Holm correction.

**Reference standard.**
- Planted errors: known by construction, so sensitivity can be estimated.
- Additional flags: "manually adjudicated as either genuine or non-genuine". The paper does not say who adjudicated, how many people did so, whether they were blinded, or what the agreement was.

**Main results** (no intervals printed).
- Planted-error detection: 98/120 (81.7%) overall; GPT-5.6 29/30 (96.7%), Claude Sonnet 5 27/30 (90.0%), Gemini 23/30 (76.7%), GPT-5.5 19/30 (63.3%); Cochran Q = 16.86, p < 0.001.
- Detection by type: sample size/subgrouping 36/40, percentage/count 33/40, statistical reporting 29/40.
- Once detected, all 98 were localized and 97/98 (99.0%) were explained and corrected. End-to-end success was 97/120 (80.8%).
- Additional flags judged genuine: 337/355 (94.9%), which collapse to 158 unique pre-existing inconsistencies. In unmodified manuscripts, 115/118 (97.5%) were genuine.
- Of GPT-5.6's genuine extras, 99/134 (73.9%) were rounding discrepancies.

**Stated limitations.** The paper has no formal limitations section. It says that "failure of systematic detection remains the principal limitation" and frames LLMs as "complementary".

**How we differ.**
- Corpus. We use natural issues in RCT packages from one high-scrutiny journal across 4 cohorts. La uses ophthalmic articles of unstated design, with planted errors whose location in each manuscript is not described.
- Scope. We add supplements and the protocol and SAP. Planned-versus-reported statistical design is a separate domain in our scope; La has nothing comparable.
- Inclusion rule. We use an explicit, written relevance screen. A display-precision rule (relative discrepancy > 0.05 after half-unit interval arithmetic) removes rounding differences. Most of La's "genuine" extras are rounding. Their 94.9% "genuine" rate is therefore not comparable with any positive predictive value we report, and we should say why.
- What La can claim that we cannot. La estimates sensitivity against a known reference and compares models. We have no planted errors, no model comparison and, so far, no human adjudicators. On sensitivity, La is ahead of us, and a reviewer will ask for it.

### 1.4 Flanagin et al. 2026 (policy framing)

**Bibliographic details (as printed).** Flanagin A, Perlis RH, Bibbins-Domingo K. Updated Guidance for Author Use of AI in Medical Publication. *JAMA*. September 15, 2026;336(11):926-928. Published online August 10, 2026. doi:10.1001/jama.2026.16613. Editorial Opinion.

**Content.**
- AI in research is acceptable if it is fully described in the Methods and the authors take full responsibility.
- Using AI to generate or format references is "discouraged" because frontier models produce realistic but nonexistent references.
- For peer review, "Entering an author's manuscript … into an external AI tool or LLM is a violation of confidentiality."
- Disclosure must give the tool name, version, manufacturer, dates of use and a description of use.

**Relation to our paper.** Flanagin frames the issue; it is not evidence for our method.
1. The confidentiality prohibition applies to manuscripts under review. Our pipeline runs on published packages. That points to a post-publication, author-side (before submission) or evidence-synthesis use. We should not pitch the pipeline as an editorial peer-review tool for JAMA without addressing this point.
2. The JAMA PDFs we process carry "All rights reserved, including those for text and data mining, AI training, and similar technologies". The pipeline sends them to an external model provider. The package folders already contain `ai_training_restriction_record.md`, so the team is aware. The paper still needs a stated legal and permission position. Zhang raises the same issue.
3. Our own manuscript must disclose the use of Codex/GPT agents in the pipeline, the Claude Opus reviewer runs and any AI-assisted drafting. AJE requires this as well (see Section 3).

### 1.5–1.8 Peripheral papers (background only)

**Graf EM, McKinney JA, Dye AB, Lin L, Sanchez-Ramos L.** Exploring the Limits of Artificial Intelligence for Referencing Scientific Articles. *Am J Perinatol* 2024;41(15):2072–2081. DOI 10.1055/s-0044-1786033. Lin L is listed at UA Epidemiology and Biostatistics, so this is likely a self-citation.
- Design and reference: cross-sectional study of ChatGPT (GPT-3.5), Bard and Chatsonic, which were asked for the citations of 44 obstetric RCTs from 2020. Answers were checked against PubMed and Google Scholar.
- Results: fully correct 7/132 (5.3%); Bard 6/44 (13.6%); ChatGPT 1/44 (printed as 2.4%; the table gives 2.3); Chatsonic 0. Permutation tests; no intervals printed.
- Stated limitations: 3 models; GPT-3.5 only; outputs varied with prompt and time.
- Relation: background on fabrication. It supports the rule that every candidate must be grounded in located source text.

**Goh E, Gallo R, Hom J, Strong E, Weng Y, Kerman H, Cool JA, Kanjee Z, Parsons AS, Ahuja N, Horvitz E, Yang D, Milstein A, Olson APJ, Rodman A, Chen JH.** Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial. *JAMA Netw Open*. 2024;7(10):e2440969. doi:10.1001/jamanetworkopen.2024.40969.
- Design: single-blind RCT, 50 physicians, GPT-4 versus conventional resources. Blinded rubric grading; weighted κ 0.66.
- Results: difference 2 percentage points (95% CI −4 to 8; P = .60). The LLM alone scored 16 percentage points higher (95% CI 2 to 30).
- Stated limitations: one LLM; no prompt training; 6 cases.
- Relation: the AI alone does not equal the human working with the AI. A human adjudication step needs its own evaluation, and grading should be blinded with κ reported.

**Ruta MR, Gaidici T, Irwin C, Lifshitz J.** ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research. *J Med Internet Res* 2025;27:e63550. doi:10.2196/63550.
- Design: 10 repeated trials per task with GPT-4; the reference was Python, SAS and R output within a 1% tolerance.
- Results: statistical values correct 26/80 (32.5%), 65/80 (81.3%) and 74/80 (92.5%) for Basic, Intermediate and Advanced prompts. Thirteen coding errors all came from the default Yates correction. No intervals printed.
- Stated limitations: univariate tests only; small dataset.
- Relation: a precedent for a computed reference standard and an explicit tolerance, comparable to our "reproduced" requirement and display-precision rule. It also shows silent failures caused by software defaults.

**Mazor T, Farhat KS, Trukhanov P, Lindsay J, Galvin M, Mallaber E, Paul MA, Hassett MJ, Schrag D, Cerami E, Kehl KL.** Clinical Trial Notifications Triggered by Artificial Intelligence–Detected Cancer Progression: A Randomized Trial. *JAMA Netw Open*. 2025;8(4):e252013. doi:10.1001/jamanetworkopen.2025.2013.
- Design: RCT, n = 20 707, allocated 2:1.
- Results: the AI model's AUROC was 0.95, yet enrollment did not differ: 2.20% vs 2.03%; difference 0.18 percentage points (95% CI −0.25 to 0.58).
- Stated limitations: one barrier targeted among many; single center.
- Relation: indirect. Detection accuracy did not translate into downstream impact, so we must not imply that our candidate yield affects evidence synthesis. It also shows protocol–report elements of our kind: retrospective registration "at the request of the journal" and an amendment that extended the end date.

### 1.9 Incidental observations (handle with care)

I noticed the following while reading and checked them by hand computation (Wald intervals). They are exactly the route-A issue types, and they appear in papers we plan to cite. That is a vivid motivating point. None has been adjudicated by a person, and two of the papers involve people close to the group. **Do not use them in the manuscript without a human check and a deliberate decision.**

- **Goh, Table 2.** The attending subgroup is printed as "0.5 (−9 to 1); P = .92". The point estimate sits near the upper limit. A Wald P from that interval is about .85 for an estimate of 0.5 and about .12 for the interval midpoint.
- **Goh, time per case.** P is printed as .20 in the text and .15 in the table. The interval (−195 to 31) implies about .155.
- **Mazor, exploratory 8277-patient analysis.** The arm rates are 5.45% vs 5.14%, but the difference is printed as "−0.31 [95% CI −0.73 to 1.31]". The arithmetic and the interval midpoint (0.29) suggest +0.31. Figure 1 also reads "Randomized 1:2" while the text gives 2:1.
- **Graf, Table 2.** "3.5%" for Chatsonic's lead author does not equal k/44 for any integer k.

---

## 2. Synthesis

### (a) Established

1. Errors in data extraction for systematic reviews are common and can change meta-analytic conclusions in a minority of cases (Xu). Earlier studies by Jones et al. and Gøtzsche et al. are cited inside Xu and need to be obtained and verified.
2. Current LLMs, given a short manuscript and a single prompt, detect most planted numeric inconsistencies and localize and explain them almost perfectly once found. The weak point is discovery, not interpretation (La).
3. Reasoning LLMs recover the authors' own stated critical error in about half of withdrawn arXiv papers at k = 5 (Zhang).
4. LLMs fabricate plausible references and fail silently on statistical computation that depends on software defaults or prompt specificity (Graf; Ruta; Flanagin's editorial experience).
5. Standalone AI performance does not translate automatically into better human or system outcomes (Goh; Mazor).
6. JAMA policy requires full disclosure of AI used in research and bars AI from confidential peer review (Flanagin).

### (b) Contested or unresolved

1. **What "precision" means without people as the reference.** Zhang's LLM-as-judge estimates depend strongly on the judge, and La gives no details of its adjudicators. Our Claude Opus runs share the same problem.
2. **What counts as a genuine issue.** La counts rounding discrepancies; our workflow screens them out. The literature has no shared severity or relevance threshold, so yield and PPV are not comparable across studies.
3. **Whether source-side inconsistencies matter for evidence synthesis.** This is plausible through Xu's "ambiguous" and "numerical" mechanisms but has not been shown by any paper in the folder.
4. **Where the tool belongs.** The candidates are pre-submission author checks (La), initial editorial screening (Zhang), post-publication or synthesis QC, or none of these, given the confidentiality rule (Flanagin).
5. **Planted versus natural errors.** Planted errors give known sensitivity but may be easier than natural ones; natural errors are realistic but have no complete reference.

### (c) Gaps our design can credibly claim

1. **Full RCT packages.** The first LLM-based review, among the papers we hold, of complete published RCT packages (main article, supplements, protocol and SAP) from one general medical journal across four annual cohorts (2018, 2019, 2024, 2025). La covers main texts only; Zhang covers preprints only.
2. **Planned versus reported design as its own domain.** No folder paper does this with LLMs. Our scope also goes beyond our own protocol 0630, which says protocol/SAP deviations would not be assessed (see (d)).
3. **An explicit, written inclusion rule** (for which cohorts, if any, it was fixed before outputs were seen still needs documenting; see (d)9) tied to interpretation and extraction relevance. This includes a numeric display-precision cutoff, always-register categories, and an asymmetric rule for doubt. It answers La's rounding-dominated "genuine" counts and Zhang's open-ended "critical problems".
4. **A described multi-agent, evidence-grounded architecture** (independent reproduction, inclusion screen, rechecker, auditor). Zhang names this explicitly as untested future work.
5. **A conceptual bridge from source-report quality to extraction validity**, linking our domains to Xu's taxonomy. It must be stated as a hypothesis or framework, not as a measured effect.
6. **A descriptive yield and workload profile:** candidates per paper and by domain, location and document type, with paper-clustered intervals. This matches the feasibility aims of protocol 0630.

### (d) Gaps we must NOT claim

1. **Sensitivity, recall or false-negative rate.** No exhaustive independent review exists and no errors were planted. Only flagged items are being adjudicated, which is partial verification. Without a human-reviewed random sample of unflagged material, or a planted-error substudy like La's or kwag204's, recall is not estimable.
2. **PPV or "confirmed" proportions against a human reference.** The completed workbooks are two Claude Opus 5.5 runs. In the README's own words, R_A versus R_Bulun agreement is "agreement between two runs of the same model … not inter-rater reliability". Reporting it as validation would repeat the circularity Zhang names. If the paper goes ahead before human adjudication, the most it can claim is model-run agreement, labeled as such.
3. **Effects on meta-analyses or clinical conclusions.** Not measured. Xu's impact percentages belong to a different object.
4. **Comparative claims** (better than other LLMs, better than human reviewers, better than statcheck-type tools). There is no comparator arm.
5. **Generalization** beyond JAMA RCTs. About 10 papers per year is not a probability sample of RCTs.
6. **Time trends between 2018 and 2025.** Small clusters, plus differences in package composition and model version, confound any comparison. At most this is descriptive and exploratory.
7. **Words such as "error", misconduct or invalidity.** Our own scope document forbids this vocabulary, and the evidence would not support it.
8. **Fidelity to protocol 0630 without disclosure.** Protocol 0630 planned 30 JAMA 2025 RCTs, a single prompt and model, "human-confirmed" issues as the primary outcome, and no protocol/SAP comparison. The current study differs on all four counts. These are post hoc changes and must be reported as such.
9. **Prespecified screening rules.** Workflow 1.6.2 changed the inclusion rules after the 1.6.1 output for 2018 and 2019 had been seen. Applied to those two cohorts, the rules are post hoc.
10. **Freedom from contamination.** The 2018 and 2019 papers, and any corrections to them, may be in the models' training data (Zhang raises this). Corrections and errata that have since been published are a related problem: do we check whether flagged items were already corrected?

---

## 3. Venue check (AJE)

- **Special collection.** AJE does look intended. The special collection on AI in health has a submission deadline of **October 30, 2026**, 16 days away. The call stresses bias, generalizability, interpretability, reproducibility and AI "as a complementary tool". Fit is a judgment call; our paper would be meta-research in support of evidence synthesis.
- **Article type.**
  - The best fit is **Practice of Epidemiology** (4,000 words; covers "AI/ML applications … validation of instruments").
  - **Novel Methodology** is the alternative (4,000 words; needs a real-world application).
  - **Research Letter** (1,500 words, no abstract, 1 figure and 1 short table, "preliminary findings") is the honest fallback if there is still no human adjudication at submission.
- **Format.**
  - Abstract: 200 words or fewer, unstructured, no citations, and it must give study years, location and population.
  - Unnumbered IMRD headings; double-anonymous review.
  - At most 5 supplementary files, each 2 MB or smaller.
  - P values to at most 2 digits; avoid "effect" for associations.
  - AI use disclosed in the cover letter **and** the Methods or Acknowledgments.
  - A graphical abstract is encouraged.
- **Examples.**
  - kwag195 (Practice of Epidemiology) follows a plain IMRD structure.
  - kwag204 (Novel Methodology) validates a flagging pipeline for implausible dietary values with **injected artificial outliers**, reporting "> 77% sensitivity, 97% specificity, and 88% precision". It is the nearest AJE template. It signals that reviewers will expect a known-truth component, which we lack.

## 4. Citations needed (not in the folder; none invented)

"In X" means the item appears in a folder paper's reference list. Verify the original before citing.

- [citation needed: statcheck and automated statistical-consistency checking]. Nuijten & Polanin 2020 is in Zhang.
- [citation needed: GRIM/GRIMMER granularity tests]
- [citation needed: prevalence of statistical reporting inconsistencies in medical journals]
- [citation needed: outcome switching and protocol/registry-versus-publication discrepancies in RCTs]
- [citation needed: current CONSORT and SPIRIT, and SAP reporting]
- [citation needed: earlier extraction-error studies]. Jones et al. and Gøtzsche et al. are in Xu, as is the Cochrane Handbook.
- [citation needed: LLM-assisted data extraction for systematic reviews]
- [citation needed: reliability of LLMs as judges]
- [citation needed: partial verification bias and reference-standard design (STARD literature)]
- [citation needed: reporting guideline for LLM evaluation studies, e.g., TRIPOD-LLM]. Verify existence and version.
- [citation needed: automation bias]
- [citation needed: errata and corrections in high-impact journals]
- [citation needed: SPOT benchmark]. Son et al. 2025 is in Zhang.
- [citation needed: AI in peer review]. Perlis et al. 2025, Flanagin et al. 2024 and the January 2026 ICMJE update are all in Flanagin 2026.
- [citation needed: intervals for clustered proportions; agreement statistics]
- [citation needed: copyright and text-and-data-mining policy for sending PDFs to external LLMs]
