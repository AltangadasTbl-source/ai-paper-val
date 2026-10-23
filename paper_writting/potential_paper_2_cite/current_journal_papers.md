# Title: 2022 - Chang Xu et al - validity of data extraction in evidence synthesis practice of adverse events: reproducibility study

## Problem:

To investigate the validity of data extraction in systematic reviews of adverse events the effect of data extraction errors on the results, and to develop a classification framework for data extraction errors to support further methodological research.

## Experiment design:
  - Data source : eligible systematic reviews published between 1 January 2015 and 1 January 2020. Metadata from the randomised controlled trials. The original data sources (eg, full text and ClinicalTrials.gov) were then referred to by the same authors to reproduce the data used in these meta analyses.
  - Inclusion and Exclusion criteria: RCT for healthcare interventions, report safety as exclusive outcome, at least one-pair of meta-analysis that included 5+ RCTs and with 2x2 table of data for event counts and sample sizes in intervention and control arms available for each trial in the meta-analysis.
  - 
  - AI Properties (None):
    - Skill based :
    - Agent based :
    - Open sourced : 
    - Reproducibility :

## Results:

The most common types of data extraction errors were numerical errors (49.2%, 867/1762) and ambiguous errors (29.9%, 526/1762), mainly caused by ambiguous definitions of the outcomes. These categories were followed by three others: zero assumption errors, misidentification, and mismatching errors. The impact of these errors were analysed on 288 meta-analyses. Data extraction errors led to 10 (3.5%) of 288 meta-analyses changing the direction of the effect and 19 (6.6%) of 288 meta-analyses changing the significance of the P value. Meta-analyses that had two or more different types of errors were more susceptible to these changes than those with only one type of error (for moderate changes, 11 (28.2%) of 39 v 26 (10.4%) 249, P=0.002; for large changes, 5 (12.8%) of 39 v 8 (3.2%) of 249, P=0.01). **`(Human data extraction errors are non-ignorable, which inducies the need to AI-assistance)`**

## Limitation:
  - data collection was divided into four portions, and each portion was conducted by a separate author. Although all authors undertook pilot training in advance, their judgments might still differ.
  - our study covered only systematic reviews published in the five year period from 2015 to 2020; therefore, the validity of the data extraction in earlier studies is unclear
  - a small proportion of studies could not have reproducibility checked, and these studies were treated as if no data extraction errors existed, which could lead to a slight underestimation of data extraction error overall
  - only focused on systematic reviews of randomised controlled trials and did not consider observational studies.


# Title:  2024 - Emily et al - Exploring the Limits of Artificial Intelligence for Refering Scientific Articles


## Problem: 
To evaluate the reliability of 3 chatbots in generating accurate references from exisiting obstetric literature.


## Experiment design: 
  - Data source:
  - Inclusion and exclusion criteria: RCTs were considered for inclusion if they were mentioned in a previous article that primarily evaluated RCTs published by the top medical and obstetrics and gynecology journals with the highest impact factors in 2020 as well as RCTs published in a new journal focused on publishing obstetric RCTs.
  
  - AI Properties :
    - Skill based : No, prompt based
    - Agent based : No
    - Open sourced : 
    - Reproducibility :

## Results: 
   - Among the 44 RCTs analyzed, Google Bard demonstrated the highest accuracy, correctly citing 13.6% of the requested RCTs, whereas ChatGPT and Chatsonic exhibited lower accuracy rates of 2.4 and 0%, respectively. Google Bard often substantially outperformed Chatsonic and ChatGPT in correctly citing the studied reference components. The majority of references from all AI models studied were noted to provide DOIs for unrelated studies or DOIs that do not exist. **`(The need for a multi-agentic framework for division of jobs and reproducing the extractions.)`**
   - To ensure the reliability of scientific information being disseminated, authors must exercise caution when utilizing AI for scientific writing and literature search

## Limitation: 
  - the study only evaluated three AI models,whichmay not represent the full capabilities of all AI chatbots available.
  - the findings and conclusions drawn fromthe study may have limited generalizability beyond the specific dataset utilized.
  - the outputs of the AI models varied significantly based on the wording of the prompt and the time at which the prompt was given


# Title: 2025 - Ruta et al - ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research


## Problem:
This study aimed to assess ChatGPT as a data analysis tool and provide researchers with a framework for applying ChatGPT to data management tasks, descriptive statistics, and inferential statistics. 


## Experiment design: 
  - Data source: The 2019 National Inpatient Sample data from the National Healthcare Cost and Utilization Project was selected to assess ChatGPT’s capabilities
  - Inclusion and exclusion criteria:
  
  - AI Properties : GPT-4
    - Skill based : no, prompt based
    - Agent based :
    - Open sourced : 
    - Reproducibility :

## Results: 


## Limitation: 


# Title: 2026 - Ethan La et al. - Large language models as internal consistency checkers for ophthalmic manuscripts

## Problem:

To evaluate whether large language models (LLMs) can detect, precisely locate, explain, and correct internal inconsistencies in ophthalmic manuscripts, and whether they can support manuscript quality control before submission.

## Experiment design:

- **Data source:** 40 published articles randomly selected from ophthalmic journals with an impact factor >3.0.
- **Inclusion and exclusion criteria:** Published ophthalmic articles meeting the journal impact-factor threshold. Detailed article-level eligibility criteria, publication dates, and exclusion criteria were not reported.
- **Experimental setup:**
  - One prespecified inconsistency was introduced into each of 30 articles: percentage/count inconsistencies (n=10), sample-size/subgrouping inconsistencies (n=10), and statistical reporting inconsistencies (n=10).
  - Ten articles remained unmodified.
  - Four models independently reviewed every article using an identical prompt: GPT-5.6 High Effort, Claude Sonnet 5 High Effort, Gemini 3.1 Pro, and GPT-5.5 Instant.
  - Outcomes included error detection, exact localisation, correct explanation, and the proposed replacement value. Additional errors flagged by models were manually adjudicated.
  - Detection rates were compared using Cochran’s Q test and pairwise McNemar tests with Holm correction.

- **AI Properties:**
  - **Skill based:** No reusable skill framework was described; the approach was prompt based.
  - **Agent based:** No agentic workflow was described. Models were evaluated independently, without collaboration or task delegation.
  - **Open sourced:** No open-source implementation or code release was reported.
  - **Reproducibility:** Partial. Model names, effort settings where applicable, and use of an identical prompt were reported. However, the exact prompt, detailed execution settings, and repeated-run results were not provided. Study datasets are available from the corresponding author upon reasonable request.

## Results:

- **Planted-error detection:** Across 120 assessments of manipulated manuscripts, models detected 98 planted errors (**81.7%**).

  | Model | Detection rate |
  |---|---:|
  | GPT-5.6 High Effort | 29/30 (96.7%) |
  | Claude Sonnet 5 High Effort | 27/30 (90.0%) |
  | Gemini 3.1 Pro | 23/30 (76.7%) |
  | GPT-5.5 Instant | 19/30 (63.3%) |

  GPT-5.6 and Claude Sonnet 5 significantly outperformed GPT-5.5 after Holm correction (p=0.012 and p=0.039, respectively).

- **Performance by error type:** Detection was highest for sample-size/subgrouping inconsistencies (**90.0%**), followed by percentage/count inconsistencies (**82.5%**) and statistical reporting inconsistencies (**72.5%**).

- **Localisation and correction:** All 98 detected planted errors were accurately localised; 97/98 (**99.0%**) were correctly explained and corrected. Complete detection–localisation–explanation–correction succeeded in **97/120 assessments (80.8%)**.

- **Additional inconsistencies:** Of 355 additional error flags, 337 (**94.9%**) were manually verified as genuine, representing **158 unique pre-existing inconsistencies** after deduplication across models. GPT-5.6 identified the most additional genuine inconsistencies, although 99/134 (**73.9%**) were rounding discrepancies.

- **Main implication:** **LLMs may provide a useful supplementary check before manuscript submission. Their principal weakness was missed errors rather than incorrect interpretation of detected errors. Human verification remains necessary.**

## Limitation:

*The following limitations are inferred from the reported design and reporting.*

- Only 40 ophthalmic articles from journals with impact factors >3.0 were included, limiting generalisability to other specialties, journals, and manuscript types.
- The planted-error experiment covered only three inconsistency categories, with one planted error per manipulated article; it does not establish performance on broader methodological flaws or more complex combinations of errors.
- No repeated-run evaluation was reported, leaving output stability and sensitivity to prompting uncertain.
- Model configurations differed, including High Effort and Instant settings, so comparisons do not isolate model capability from inference settings.
- Manual adjudication was reported without details about reviewer independence, blinding, or inter-rater agreement.
- The **94.9% verification rate applies to flagged additional problems**, not all existing errors. Without an exhaustive reference standard, sensitivity for pre-existing inconsistencies cannot be determined.
- Many additional findings were rounding discrepancies; their effects on study conclusions or clinical interpretation were not evaluated.
- The study did not directly compare LLM-assisted checking with human-only review or measure time savings.

:chatgpt-content-reference{index="0"}


# Title: 2026 - Jai Paris et al. - Can large language models accurately triage oculoplastic referrals?

## Problem:

To evaluate whether large language models (LLMs) can accurately assign urgency categories to oculoplastic referrals compared with specialist assessment, and identify referrals requiring expedited review.

## Experiment design:

- **Data source:** 100 hypothetical referral vignettes representing periocular, lacrimal, and orbital conditions of varying severity. Models were evaluated in May 2026.
- **Inclusion and exclusion criteria:** Vignettes were developed to represent conditions encountered in routine oculoplastic practice. Detailed eligibility criteria, case-selection procedures, and exclusion criteria were not reported.
- **Reference standard:** Two fellowship-trained oculoplastic surgeons independently reviewed each vignette and assigned a category:
  - Category 1: review within 2 days.
  - Category 2: within 30 days.
  - Category 3: within 90 days.
  - Category 4: within 365 days.
- **Experimental setup:** Five models received identical referral information and the same concise natural-language prompt: ChatGPT 5.4, ChatGPT 5.5, Claude Opus 4.8 Thinking, Claude Sonnet 4.6 Thinking, and Gemini 3.1 Pro Thinking.
- **Evaluation:** Exact agreement, quadratic weighted Cohen’s κ, mean absolute error (MAE), and under-/over-triage rates. A secondary analysis classified referrals as urgent (Categories 1–2) or non-urgent (Categories 3–4), evaluating sensitivity, specificity, predictive values, and F1 score.

- **AI Properties:**
  - **Skill based:** No reusable skill framework was described; the approach was prompt based.
  - **Agent based:** No agentic workflow was described. Models were evaluated independently without collaboration or task delegation.
  - **Open sourced:** No open-source implementation or code release was reported.
  - **Reproducibility:** Partial. Model names, evaluation month, and the use of a shared prompt were reported. The prompt is referenced in Supplementary Material 1, which was not included in the supplied PDF. Detailed execution settings and repeated-run results were not reported. Study data are available from the corresponding author upon reasonable request.

## Results:

- **Agreement with expert triage was limited:** Exact agreement ranged from **24–41%**, while weighted κ ranged from **0.47–0.61**. ChatGPT 5.5 had the highest agreement and lowest MAE.

  | Model | Exact agreement | Weighted κ | MAE | Under-triage | Over-triage |
  |---|---:|---:|---:|---:|---:|
  | ChatGPT 5.4 | 32% | 0.50 | 0.81 | 4% | 64% |
  | ChatGPT 5.5 | 41% | 0.61 | 0.67 | 8% | 51% |
  | Claude Opus 4.8 Thinking | 37% | 0.58 | 0.72 | 4% | 59% |
  | Claude Sonnet 4.6 Thinking | 31% | 0.49 | 0.82 | 5% | 64% |
  | Gemini 3.1 Pro Thinking | 24% | 0.47 | 0.89 | 2% | 74% |

- **Over-triage predominated in the four-category analysis:** Models assigned greater urgency than experts in **51–74%** of cases. ChatGPT 5.5 had the highest reported under-triage rate (**8%**) despite its stronger overall agreement.

- **Urgent-referral identification, as reported in Table 2:** Sensitivity ranged from **52.1–76.1%**, specificity from **89.7–96.6%**, and F1 scores from **0.68–0.85**. ChatGPT 5.5 achieved the highest sensitivity and F1 score; Gemini achieved the highest specificity but lowest sensitivity.

- **Main implication:** **The authors conclude that LLMs show moderate agreement with specialist triage, but require evaluation using real-world referrals before clinical integration. Better relative performance did not establish reliable autonomous triage.**

## Limitation:

*The authors explicitly identify the need for real-world evaluation. Additional limitations below are inferred from the study design and reporting.*

- **Hypothetical cases:** Performance on constructed vignettes may not reflect real referrals containing incomplete information, ambiguous descriptions, or inconsistent documentation.
- **Small, specialty-specific dataset:** Only 100 oculoplastic vignettes were evaluated, limiting generalisability to other specialties and referral systems.
- **Reference-standard reporting:** Although two specialists independently reviewed the cases, their inter-rater agreement and the procedure for resolving disagreements were not reported.
- **Uncertain output stability:** No repeated-run evaluation or prompt-sensitivity analysis was reported.
- **Limited statistical uncertainty reporting:** Confidence intervals and formal between-model comparisons were not provided; numerical rankings should not be interpreted as demonstrated statistical superiority.
- **Potential internal reporting inconsistency:** Tables 1 and 2 appear difficult to reconcile under the stated urgency definitions. For example, ChatGPT 5.5’s binary metrics are consistent with approximately 17 missed urgent cases among 100 referrals, exceeding the 8 under-triaged cases reported in Table 1. The positive-class coding or table labels require clarification before interpreting the direction of errors.
- **No clinical implementation outcomes:** The study did not measure patient outcomes, waiting times, resource use, or whether clinician–AI collaboration improves triage over clinician assessment alone.

:chatgpt-content-reference{index="0"}





---

# Title: 2025 - Charles J. Lovering et al. - On Finding Inconsistencies in Documents

**Source:** arXiv:2512.18601v1, 21 December 2025. [Paper PDF](<recent_ai_papers_2026-10-22/On Finding Inconsistencies in Documents/paper.pdf>). Page references below refer to this saved PDF version.

## Problem:

To evaluate whether language models can proactively identify internal inconsistencies in long professional documents, without being given a targeted question or the location of an error, and provide the original evidence and an explanation sufficient for human review.

The authors introduce FIND (Finding INconsistencies in Documents), which requires models to inspect complete documents rather than classify preselected sentence pairs. It covers numerical, conceptual/logical, and structural inconsistencies, such as incorrect totals, conflicting classifications, or references to tables with incompatible content. The task does not include correcting the inconsistency, deciding which conflicting statement is true, or systematically verifying facts against external sources. Some judgments still require general or domain knowledge. (§§1, 3–4, pp. 1–5.)

## Experiment design:

- **Data source:** FIND contains **500 document examples: 125 development examples and 375 test examples**, with one expert-inserted target inconsistency per example. The test set contains 75 documents from each of five sources: US Bureau of Labor Statistics reports (BLS), S&P bond presale reports (PRE), SEC 10-Q reports (SEC), municipal bond disclosures (EMM), and Project Gutenberg nonfiction books (PG). Experts created, annotated, and checked each inconsistency, with approximately two hours spent per example. The test set contains 204 numerical, 63 non-numerical, and 108 structural inconsistencies. Mean document length is approximately 63,000 tokens; the reported median is approximately 35,000, and 25% exceed 78,000 tokens. (§4; Tables 1–2.)

- **Inclusion and exclusion criteria:** Documents were selected for suitable licensing, professional quality, and variation in length, tables, and analytical content. Recent documents were preferred for several sources, and Gutenberg texts were screened against selected pretraining corpora to reduce contamination risk. This does not establish that all proprietary models had never encountered them. Documents were generally converted to Markdown; conversion failures were handled by replacing documents or manually preparing them. Some very long documents were reduced to relevant sections that retained the target inconsistency. BLS visual charts were removed, and all documents were in English. The complete sampling frame, random seed, document-level exclusion list, and a common minimum length were not reported. (Appendices G and H.)

- **Additional natural-error samples:** Separate analyses used **45 MFR financial reports** and **50 arXiv cs.CL papers**. The latter comprised 25 papers with a known inconsistency identified through a correction between adjacent versions (Idnt), and 25 papers selected without requiring a known error (Ctrl). Ctrl papers were not established to be error-free. These samples are separate from the 375-document FIND test set and are not representative random samples of all scientific disciplines. (§4.1; Table 2.)

- **Experimental setup:** Eleven models were evaluated: Gemma 3 12B/27B, gpt-oss 20B/120B, Claude Sonnet v4, GPT-5-mini, GPT-5, o3-mini, o3, and Gemini 2.5 Flash/Pro. Each model received a document and instructions to return inconsistencies, quoted evidence, and explanations using structured tags. No task-specific detector was trained. Inputs were limited to 105,000 tokens and outputs to 20,000 tokens. Depending on the tokenizer, up to 83/375 test documents were truncated; target evidence fell outside the retained text in two Gemma 3 cases. (§§3, 5; Appendix I.)

- **Evaluation:** For each document, the best-matching model suggestion was compared with its single annotated target. Evidence score ΛE measures alignment with supporting passages; description score Λδ uses BLEURT; task score ΛI uses GPT-4.1 to judge whether the suggestion identifies the same inconsistency. ΛI therefore approximates document-level recall of planted targets, rather than precision, overall accuracy, or recall of every natural error. The judge achieved Cohen’s κ=0.96 against human judgments on 200 sampled development-set outputs. Additional GPT-5 suggestions were manually assessed in 200 documents sampled across eight source/subset groups, including FIND, MFR, and both cs.CL subsets. These precision estimates and the main recall estimates use different samples and procedures. (§§3.3, 6–7.)

- **AI Properties:**
  - **Skill based:** No reusable skill library, skill retrieval, or skill-learning mechanism was described. The method was prompt based.
  - **Agent based:** No collaborative agent workflow or autonomous tool-use loop was evaluated. A single model inspected each document; GPT-4.1 served as an evaluator rather than a collaborating review agent.
  - **Open sourced:** This version provides links to data, terms of use, and annotation guidance. It states that code and a Hugging Face release would follow review; that statement is a release commitment in the saved version, not evidence of a completed release. Four evaluated models had open weights, while the others were accessed through hosted services. (Appendix C.)
  - **Reproducibility:** Partial. Prompts, evidence-scoring algorithms, preprocessing descriptions, and hardware details are provided. Open models used vLLM on eight A100 GPUs; hosted models were accessed through LiteLLM. Complete sampling settings, dated hosted-model snapshots, and repeated-run stability results were not provided. Reproduction also depends on licensing, preprocessing decisions, and model availability. (Appendices D, E, and I.)

## Results:

- **Planted-target detection:** GPT-5 achieved the highest task score, **64%**, followed by Gemini 2.5 Pro at **61%**. Results below are rounded scores reported for the 375-document FIND test set; exact hit counts should not be reconstructed from these rounded percentages. (Table 4, p. 7.)

  | Model | Task score ΛI (%) | Evidence score ΛE (×100) | Description score Λδ (×100) |
  |---|---:|---:|---:|
  | GPT-5 | 64 | 33 | 45 |
  | Gemini 2.5 Pro | 61 | 32 | 46 |
  | o3 | 53 | 24 | 40 |
  | GPT-5-mini | 51 | 23 | 41 |
  | Gemini 2.5 Flash | 43 | 21 | 42 |
  | Claude Sonnet v4 | 39 | 23 | 38 |
  | Gemma 3 27B | 23 | 7 | 37 |
  | Gemma 3 12B | 20 | 7 | 36 |
  | o3-mini | 19 | 6 | 27 |
  | gpt-oss-20B | 6 | 10 | 32 |
  | gpt-oss-120B | 6 | 13 | 37 |

- **Variation by source and length:** GPT-5 task scores were 87%, 67%, 73%, 43%, and 52% on BLS, PRE, SEC, EMM, and PG, respectively, with 75 documents per source. Even the strongest model missed approximately 36% of planted targets. For GPT-5 and Gemini 2.5 Pro, an additional 10,000 input tokens was associated with an approximately **2.6 percentage-point decrease** in task score after controlling for source and inconsistency type; this was an association, not a demonstrated causal effect. (§6; Figure 6; Table H.5.)

- **Quality of additional suggestions:** Across the five FIND sources, GPT-5’s mean source-level precision was **52.5%**, and **66.6%** of suggestions were considered useful, with an average of 2.6 suggestions per document. These are averages across sources, not pooled proportions across all suggestions. In the cs.CL Ctrl and Idnt subsets, precision was 72.1% and 70.1%, respectively; usefulness was 91.9% and 90.7%. (Table 5, p. 8.)

- **Scientific-paper findings:** Among the 50 cs.CL papers, **136/196 new suggestions (approximately 69.4%)** were judged to identify genuine inconsistencies. The 196 excludes 12 recovered known inconsistencies from 208 total predictions. Separately, GPT-5 recovered **12/25 known inconsistencies (48%)** in Idnt papers. The confirmation rate for new suggestions and recall of known targets have different denominators and should not be presented as the same measure. (Abstract; §7.2; Appendix A.11.)

- **Natural financial errors:** On the 45 MFR reports, GPT-5’s task score was only **7%**, while Claude Sonnet v4 achieved the highest score, **11%**. These rounded results suggest that natural errors and inserted targets can differ substantially in difficulty. (Table H.2.)

- **Main implication:** **LLMs can assist with evidence-supported document consistency checks, but substantial missed-error and false-positive rates remain. The 64% FIND result is not a scientific-paper recall estimate; the scientific-paper evidence comes from a separate, smaller case study.**

## Limitation:

- **Scope and generalisability:** The benchmark is entirely in English and mainly covers financial documents and nonfiction. It excludes visual chart interpretation, cross-document inconsistencies, and systematic external fact-checking. The scientific-paper analysis contains only 50 cs.CL papers.
- **Constructed targets:** Each FIND example contains one inserted target; insertion locations favour the first half of documents, with mean evidence position around 30% of document length. This differs from the distribution of naturally occurring problems.
- **Training contamination and selection:** Some cs.CL and MFR documents may have appeared in training data. Idnt papers are selected for errors that authors noticed and corrected, potentially favouring particular error types.
- **Uncertain adjudication:** Initial human agreement on additional suggestions was modest: κ=0.31 with 58.8% agreement for financial sources, and κ=0.38 with 67.8% agreement for cs.CL. Final labels followed discussion. The automated judge’s high agreement was demonstrated on development outputs, not every evaluation setting.
- **Incomplete reference standard:** Without an exhaustive list of natural errors, recall for all existing inconsistencies cannot be established. Reporting more candidates may improve planted-target recall while increasing human review costs.
- **Evidence localisation and impact:** Quoted evidence can be difficult to locate uniquely when passages repeat, and evidence boundaries are subjective. The task does not assess correction quality. The authors did not observe the cs.CL inconsistencies they found changing the papers’ conclusions.
- **Implications for system design:** The study motivates assisted consistency checking and evidence-based evaluation, but does not establish an advantage for multi-agent workflows or skill libraries over the tested single-model approach. (§9 and relevant evaluation sections.)

---

# Title: 2026 - Min Dong et al. - Potential and limitations of a large language model in the statistical review of comparative categorical data: an exploratory study of structured prompt-guided approach

**Source:** *Research Integrity and Peer Review*, 2026, 11:39; DOI: [10.1186/s41073-026-00231-0](https://doi.org/10.1186/s41073-026-00231-0). [Paper PDF](<recent_ai_papers_2026-10-22/Potential and limitations of a large language model in the statistical review of comparative categorical data - an exploratory study of structured prompt-guided approach/paper.pdf>). Page references below refer to the saved PDF’s printed page numbers.

## Problem:

To determine whether a structured prompt containing explicit statistical knowledge and procedural rules enables DeepSeekV3.2 to review comparative categorical data reliably, identify where failures arise, and assess whether the model can conduct statistical audits autonomously.

The study focuses on contingency-table analyses that can usually be checked using published frequencies rather than individual-level data. These include Pearson χ² and continuity-corrected tests for independent samples, and McNemar/McNemar–Bowker tests for paired data. It evaluates both the appropriateness of the reported method under predefined rules and the reproducibility of reported statistics and P values, rather than overall manuscript quality. (pp. 2–3.)

## Experiment design:

- **Data source:** **40 medical papers** were divided into a 20-paper development set and a 20-paper independent test set. Development papers mainly came from the authors’ publishing institution, supplemented to cover less common paired designs. Test papers were retrieved from DOAJ in November 2025 using `("SPSS" AND "Chi-square test") OR ("SPSS" AND "McNemar")`. The test set contained 15 independent-sample papers and five paired-design papers, with **43 tables and 181 analysis items**: 168 independent and 13 paired analyses. Eighty items used 2×2 tables and 101 used other table dimensions. (p. 3; Table 1.)

- **Inclusion criteria:** Independent-sample papers had to report original medical research, provide actual frequencies rather than percentages alone, use SPSS, explicitly mention χ² testing, and report at least five key results with χ² statistics and P values to three decimal places. Eligible designs included clinical trials, cohort studies, case–control studies, and cross-sectional studies. Paired studies had to meet the research-type, frequency-availability, and SPSS requirements, provide P values to at least two decimal places, and supply a complete paired contingency table or discordant-pair counts. (p. 3.)

- **Exclusion criteria:** Incomplete frequencies; analyses using only complex models such as logistic or Poisson regression without direct contingency-table testing; methods outside the prompt’s knowledge base, such as Cochran–Mantel–Haenszel or trend χ² tests; reviews, commentaries, case reports, meta-analyses, and conference abstracts; and tables with poor OCR or excessively complex merged/nested structures. Publication-date limits and complete screening counts were not reported.

- **Prompt development and workflow:** Dozens of development iterations produced a prompt specifying a statistical-expert role, four statistical modules, explicit formulas, mandatory constraints, and an ordered workflow: locate tables, extract counts, identify design and dimensions, match rules, select tests, calculate results, and compare them with the manuscript. Rules covered independent 2×2 and R×C tables, paired 2×2 tables, and paired square tables. For paired 2×2 analyses, the ordinary versus corrected McNemar formula depended on whether the number of discordant pairs reached 40. The prompt required identification of cells with expected counts below 5. (pp. 3–5; Appendix 2.)

- **Limits on calculation:** Early attempts to calculate Fisher’s exact test sometimes failed and led the model to copy the manuscript’s P value. The final prompt therefore required the model to identify and explain when an exact test was needed, while leaving calculation to humans and statistical software. Decisions requiring substantive context, such as whether ordinal data warranted a rank-based test, were also left to human reviewers. (p. 4.)

- **Execution and reference standard:** A trained researcher uploaded PDFs to the official DeepSeekV3.2 website, selected “Deep thinking,” supplied the full prompt, and recorded outputs and displayed thinking time. External statistical-program or code-execution use by the model was not reported. A senior statistician independently recalculated results in SPSS 26.0; paired 2×2 results were checked manually. Discrepancies were examined by a human, and reasonable alternative test choices were not automatically treated as errors. (pp. 3, 5, 7.)

- **Evaluation and denominators:** An actual error in the manuscript was the positive class. Measures included accuracy, sensitivity, specificity, positive and negative predictive values, F1, Cohen’s κ, and Wilson confidence intervals. An absolute numerical difference of **≤0.005** was accepted as agreement. After the Case 8 data correction, the test set contained 181 items; excluding all 33 items from repeatedly failing Case 17 left **148 items for method evaluation**. Excluding paired analyses and items requiring or already using Fisher’s exact test left **97 independent-sample items for numerical evaluation**. These are evaluable subsets, not all submitted tasks. (pp. 5–8; Tables 1–3.)

- **Repeatability and efficiency:** The first 12 test papers—10 independent-sample and two paired-design papers—were each processed five times, with ICC analysis for 83 items. Timing compared displayed model thinking time with manual data entry, method selection, and result generation, using a paired Wilcoxon test. Manual setup of the SPSS variable view was excluded. (pp. 6, 8.)

- **AI Properties:**
  - **Skill based:** No explicit skill library, skill retrieval, or skill-learning mechanism was described. Statistical rules were packaged as a reusable structured prompt.
  - **Agent based:** No multi-agent division of work, mutual review, or autonomous tool-use loop was described. One web-based model performed the task, with humans handling operation, verification, and exceptions.
  - **Open sourced:** The full prompt is published in Appendix 2 and saved locally as a [prompt text file](<recent_ai_papers_2026-10-22/Potential and limitations of a large language model in the statistical review of comparative categorical data - an exploratory study of structured prompt-guided approach/released_assets/prompts/appendix_2_prompt.txt>). Automated review code and the complete dataset were not reported as released. A public prompt alone does not make the full system or experimental data open source.
  - **Reproducibility:** Partial. The model name, mode, prompt, tolerance, reference software, and repeated-run design are reported. Exact web-backend versions, sampling settings, complete item-level inputs and outputs, and all extracted data are not fully available. Complete data are available from the corresponding author upon reasonable request. A degrees-of-freedom correction introduced after testing is not included in the published Appendix 2 formula, limiting reproduction of the corrected results. (Appendix 2; Data availability.)

## Results:

- **Error identification:** Table 2 reports high classification accuracy on the evaluable subsets. These measures assess whether the model correctly classified the manuscript’s result as erroneous or correct; they are not the proportion of model-generated numbers that exactly match the reference calculation. TN counts below are derived from the reported totals and TP/FN/FP counts. (pp. 7–8.)

  | Measure | Method selection (N=148) | χ² error classification (N=97) | P-value error classification (N=97) |
  |---|---:|---:|---:|
  | Manuscript errors in reference standard | 26 | 23 | 17 |
  | TP / FN / FP / TN | 25 / 1 / 0 / 122 | 21 / 2 / 3 / 71 | 15 / 2 / 1 / 79 |
  | Accuracy | 147/148 (99.3%) | 92/97 (94.8%) | 94/97 (96.9%) |
  | Sensitivity | 25/26 (96.2%) | 21/23 (91.3%) | 15/17 (88.2%) |
  | Specificity | 122/122 (100.0%) | 71/74 (95.9%) | 79/80 (98.8%) |
  | Positive predictive value | 100.0% | 87.5% | 93.8% |
  | Negative predictive value | 99.2% | 97.3% | 97.5% |
  | F1 | 98.0% | 89.3% | 90.9% |
  | Cohen’s κ | 0.976 | 0.859 | 0.891 |

  Accuracy 95% CIs were **96.3–99.9%, 88.5–97.8%, and 91.2–98.8%**, respectively. Sensitivity CIs were **81.2–99.4%, 73.1–97.5%, and 65.7–96.7%**. One case requiring Fisher’s exact test was missed. Error counts in Table 2 include discrepancies caused by inappropriate method selection; they are not directly interchangeable with Table 1’s 21 purely computational discrepancies.

- **Paired analyses and prompt correction:** All **six paired 2×2 analyses** agreed with manual calculations. However, **three of seven paired R×R analyses initially disagreed with SPSS** because the prompt did not adjust degrees of freedom when a symmetric pair of off-diagonal cells both contained zero. Adding this rule produced agreement with SPSS. This is a result after adapting the prompt, rather than 100% success from the original fixed prompt. (p. 8.)

- **Efficiency:** Median manual time was **374 seconds** (IQR 223–478), compared with **407 seconds** for the model (IQR 251–477); n=19, Z=−0.523, P=0.601. The study found no statistically significant time saving. A nonsignificant difference does not establish equivalence. (p. 8.)

- **Repeatability:** Across 83 items evaluated in five runs, χ² ICC was **0.912** (95% CI 0.880–0.938), and P-value ICC was **0.997** (0.996–0.998), both P<0.001. High aggregate agreement did not ensure complete task execution: Cases 2 and 10 each omitted some analyses in **two of five runs**. (pp. 6, 8.)

- **Failure patterns:** Case 17 exhibited inconsistent extraction across page boundaries and, during its 33 analyses, a shift from stepwise recalculation to copying reported χ²/P values and labelling them consistent. The authors described this as “laziness,” a behavioural description rather than evidence of intent. In Case 10, only one of 12 reported result pairs was correct, and the model also made multiple errors and omissions. The authors suggested anchoring on manuscript values, but did not test its causal effect using hidden or altered values. (pp. 8–10.)

- **Main implication:** **Explicit statistical rules can support accurate checking of selected categorical analyses, but extraction failures, omissions, and dependence on the values being checked prevent these results from establishing reliable autonomous statistical auditing. Human verification and independent recalculation remain necessary.**

## Limitation:

*The authors discuss the restricted scope, generalisability, anchoring, sample composition, and within-manuscript dependence. Further implications of the design and reporting are identified below.*

- **Restricted scope:** The study excludes one-sample tests, t tests, ANOVA, multiple-comparison adjustment, Bayesian methods, and broader methodological review. Results from one model and SPSS-using medical papers do not establish performance across models, software packages, or disciplines.
- **Small, uneven sample:** Only 20 papers formed the independent test set, with limited representation of complex paired tables and cross-page structures. Common, simple tasks may dominate aggregate results.
- **Conditional performance after exclusions:** Excluding Case 17 removes a substantive deployment failure. Accuracy among 148 or 97 evaluable items is not an end-to-end success rate for all submitted manuscripts, and the proportion of papers for which every task was completed correctly was not fully reported.
- **Dependence within manuscripts:** Analysis items from the same paper may share methods and error patterns, but were treated as independent. This can narrow confidence intervals and allow a few error-dense papers to dominate. The authors suggest GEE or mixed-effects models.
- **Independent calculation and prompt benefit were not isolated:** Manuscript values remained visible, and no systematic hidden-value or erroneous-anchor comparison was performed. Development iterations also do not replace a controlled comparison of ordinary and structured prompts on the independent test set.
- **Post-test adaptation and prompt availability:** The paired R×R correction was added after discrepancies were observed, so its success requires testing on new data. Appendix 2 still gives `df=R*(R−1)/2` without the zero-pair adjustment, and the complete enhanced prompt was not identified in the saved materials.
- **Reference standard and repeatability reporting:** Reasonable alternative tests may yield different results. Details of expert blinding, inter-rater agreement, the ICC model, and missing-value handling are insufficient to reconstruct every analytical decision. High ICC does not establish absence of individual errors or omissions.
- **Incomplete workflow costs:** Timing excludes prompt development, output review, and correction; manual timing also excludes some setup. The findings do not establish improved efficiency across the complete editorial workflow.
- **Implications for system design:** The study motivates structured checking with human oversight, but does not compare a skill library with ordinary prompting or test whether multi-agent review improves on a single model.

-----------------------------------------------------------------------------
# Title:  


## Problem: 


## Experiment design: 
  - Data source:
  - Inclusion and exclusion criteria:
  
  - AI Properties (None):
    - Skill based :
    - Agent based :
    - Open sourced : 
    - Reproducibility :

## Results: 


## Limitation: 
