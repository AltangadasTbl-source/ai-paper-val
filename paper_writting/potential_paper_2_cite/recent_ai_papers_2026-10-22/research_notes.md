# Recent AI papers: reading map and verification notes

Collection date: 2026-10-22. Ten new papers; first public dates fall within 2024-10-22–2026-10-22. All ten PDFs downloaded and validated; the existing eight PDFs were preserved.

## Reading map

| Theme | Papers | Suggested order |
| --- | --- | --- |
| Internal consistency and scientific error detection (6) | FIND, PRISMM-Bench, categorical statistical review, To Err Is Human, FLAWS, SPOT | Start with FIND/PRISMM and the clinical study; then error-detection limits |
| Single versus multi-agent context/cost comparisons (3) | BenchAgent, Scaling Agent Systems, Single-Agent with Skills | BenchAgent gives the clearest measured cumulative-token comparison |
| Generated reusable skills (1) | SkillRL | Inspect the three released SkillBank JSON files |

## How to interpret context and reproducibility claims

These studies compare agent controllers or compiled reasoning pipelines, not ordinary untooled chat. Cumulative tokens sum model inputs and outputs over calls; repeated history can be counted repeatedly. Peak context occupancy is the largest live prompt/history at a call. Splitting agents can lower each local context while increasing cumulative usage. These quantities must not be equated. BenchAgent measures the former; the selected papers do not establish a universal peak-context saving.

Scaling Agent Systems v3 contains a reporting ambiguity: its coordination-overhead formula uses turn counts, while nearby prose describes ratios as token budgets and Table 5 reports matched reasoning tokens. Its tool-heavy interaction is not significant (p=.211). Use it for architecture/task dependence, not a clean numerical token-overhead ratio. SAS-with-skills is preliminary and SkillRL is a memory/skill-compression comparison, not MAS-versus-single evidence.

The statistical paper tests repeatability as well as manuscript numerical agreement. Released prompts and source support procedural reproducibility, but their availability alone does not show successful independent reproduction.

## Papers and saved artifacts

### 1. When AI Co-Scientists Fail: SPOT-a Benchmark for Automated Verification of Scientific Research

[Paper PDF](<When AI Co-Scientists Fail - SPOT-a Benchmark for Automated Verification of Scientific Research/paper.pdf>) · [Primary source](https://arxiv.org/abs/2505.11855v1) · first public 2025-05-17; saved version 2025-05-17.

Scientific-manuscript verification using 83 papers with 91 author/annotator-checked errors associated with errata or retraction.

**Evidence:** Best tested recall 21.1% and precision 6.1%; repeat runs often miss the same real errors.

**Limits:** Broad scientific verification, not purely internal numerical contradictions; selected serious errors are harder than routine clerical audits.

**Assets:** [released_assets](<When AI Co-Scientists Fail - SPOT-a Benchmark for Automated Verification of Scientific Research/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: no repository license declared. No LICENSE file or explicit repository license found; publicly accessible prompts are not thereby licensed as open source.

### 2. PRISMM-Bench: A Benchmark of Peer-Review Grounded Multimodal Inconsistencies

[Paper PDF](<PRISMM-Bench - A Benchmark of Peer-Review Grounded Multimodal Inconsistencies/paper.pdf>) · [Primary source](https://arxiv.org/abs/2510.16505v3) · first public 2025-10-18; saved version 2026-02-15.

Direct text/figure/table/equation inconsistency identification, remedy and conflicting-pair matching.

**Evidence:** Latest v3 contains 384 inconsistencies from 353 papers; evaluates 21 multimodal models.

**Limits:** Reviewer-mined, question-based benchmark; scores are not exhaustive free-form audit precision/recall. Earlier versions have different counts.

**Assets:** [released_assets](<PRISMM-Bench - A Benchmark of Peer-Review Grounded Multimodal Inconsistencies/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: Apache-2.0. 

### 3. FLAWS: A Benchmark for Error Identification and Localization in Scientific Papers

[Paper PDF](<FLAWS - A Benchmark for Error Identification and Localization in Scientific Papers/paper.pdf>) · [Primary source](https://arxiv.org/abs/2511.21843v1) · first public 2025-11-26; saved version 2025-11-26.

Identifies and localizes claim-invalidating errors inserted into peer-reviewed papers.

**Evidence:** 713 paper-error pairs; GPT-5 identifies 39.1% when allowed ten ranked candidate error spans.

**Limits:** Synthetic LLM-inserted errors and automated judging; top-ten identification is not ordinary audit accuracy.

**Assets:** [released_assets](<FLAWS - A Benchmark for Error Identification and Localization in Scientific Papers/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: MIT. 

### 4. On Finding Inconsistencies in Documents

[Paper PDF](<On Finding Inconsistencies in Documents/paper.pdf>) · [Primary source](https://arxiv.org/abs/2512.18601v1) · first public 2025-12-21; saved version 2025-12-21.

Direct within-document contradiction detection, including numeric/text discrepancies and scientific-paper case studies.

**Evidence:** Expert-inserted document benchmark plus 50 arXiv-paper audit; 136 of 196 GPT-5 suggestions on those papers judged legitimate.

**Limits:** Main benchmark primarily financial documents/nonfiction; paper-audit analysis is a separate case study. Reported 64% recall is not scientific-paper recall.

**Assets:** No official separate skill library located; published examples/prompts remain in the PDF. See skills_search_status.txt.

### 5. To Err Is Human: Systematic Quantification of Errors in Published AI Papers via LLM Analysis

[Paper PDF](<To Err Is Human - Systematic Quantification of Errors in Published AI Papers via LLM Analysis/paper.pdf>) · [Primary source](https://arxiv.org/abs/2512.05925v1) · first public 2025-12-05; saved version 2025-12-05.

GPT-5 Paper Correctness Checker detects objective formula, derivation, calculation, figure and table errors in published AI papers.

**Evidence:** Human experts confirmed 263/316 flagged mistakes (83.2% precision).

**Limits:** Precision on reviewed flags does not establish recall or exhaustive correctness; most errors were relatively minor.

**Assets:** [released_assets](<To Err Is Human - Systematic Quantification of Errors in Published AI Papers via LLM Analysis/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: MIT. 

### 6. Potential and limitations of a large language model in the statistical review of comparative categorical data: an exploratory study of structured prompt-guided approach

[Paper PDF](<Potential and limitations of a large language model in the statistical review of comparative categorical data - an exploratory study of structured prompt-guided approach/paper.pdf>) · [Primary source](https://doi.org/10.1186/s41073-026-00231-0) · first public 2026-07-01; saved version 2026-07-01.

Structured DeepSeek-V3.2 prompt audits categorical statistical methods and manuscript calculations against statistician recomputation; includes repeatability tests.

**Evidence:** 20 independent test manuscripts; chi-square consistency 92/97 and P-value consistency 94/97.

**Limits:** Small specialized study; unstable extraction, scope neglect and anchoring persisted. Does not justify autonomous statistical audit.

**Assets:** [released_assets](<Potential and limitations of a large language model in the statistical review of comparative categorical data - an exploratory study of structured prompt-guided approach/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: CC BY 4.0. 

### 7. Towards a Science of Scaling Agent Systems

[Paper PDF](<Towards a Science of Scaling Agent Systems/paper.pdf>) · [Primary source](https://arxiv.org/abs/2512.08296v3) · first public 2025-12-09; saved version 2026-04-08.

Controlled comparison of single-agent and four multi-agent architectures with standardized tools/prompts/compute across six benchmarks and 260 configurations in v3.

**Evidence:** Useful architecture/task study; tool-heavy interaction is non-significant in v3 (p=.211).

**Limits:** Overhead metric uses turn counts, while some prose calls ratios token budgets and Table 5 reports matched reasoning tokens; do not treat overhead percentages as unambiguous measured token ratios or context occupancy.

**Assets:** [released_assets](<Towards a Science of Scaling Agent Systems/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: MIT. 

### 8. Do More Agents Help? Evaluating Accuracy and Cost in LLM Multi-Agent Workflows

[Paper PDF](<Do More Agents Help - Evaluating Accuracy and Cost in LLM Multi-Agent Workflows/paper.pdf>) · [Primary source](https://arxiv.org/abs/2606.05670v2) · first public 2026-06-04; saved version 2026-10-09.

Direct controlled workflow comparison: common GPT-4.1 backend, tools and scoring across ten reasoning/coding/tool-use benchmarks; six MAS versus one task-level controller.

**Evidence:** v2: ChatEval uses 4.34x Core tokens, LLM-Debate 1.39x; EvoAgent pooled accuracy 79.70% versus Core 76.65%.

**Limits:** Recorded cumulative input/output tokens, not peak context occupancy. Nine broad-suite tasks only expose Python; HotpotQA and separate GAIA checks use expanded tools. Core can delegate search; single agent means one task controller. Missing usage not imputed; external-runtime case study budgets not matched.

**Assets:** [released_assets](<Do More Agents Help - Evaluating Accuracy and Cost in LLM Multi-Agent Workflows/released_assets/>). Reusable prompts and/or supporting source; not an installable skill package. License: MIT. Pinned BenchAgent experiment branch has no LICENSE file. GitHub repository metadata identifies MIT; official default-main LICENSE is archived separately as LICENSE_repository_main with Git blob SHA. Do not treat it as a file from the pinned experiment branch.

### 9. When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail

[Paper PDF](<When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail/paper.pdf>) · [Primary source](https://arxiv.org/abs/2601.04748v2) · first public 2026-01-08; saved version 2026-01-14.

Compiles multi-agent roles into prompt skills within a single LLM call, linking reusable skills to coordination/context repetition costs.

**Evidence:** Table 3: average 53.7% token and 49.5% latency reductions across GSM8K, HumanEval and HotpotQA; three/four calls collapse to one.

**Limits:** Preliminary reasoning benchmarks and synthetic skill-selection libraries; not a long-horizon realistic tool-workflow comparison. Token accounting less explicit than BenchAgent; no measured peak-context trace.

**Assets:** No official separate skill library located; published examples/prompts remain in the PDF. See skills_search_status.txt.

### 10. SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

[Paper PDF](<SkillRL - Evolving Agents via Recursive Skill-Augmented Reinforcement Learning/paper.pdf>) · [Primary source](https://arxiv.org/abs/2602.08234v2) · first public 2026-02-09; saved version 2026-10-07.

Automatically distills and recursively improves a hierarchical SkillBank from successful/failed trajectories with reinforcement learning.

**Evidence:** Official MIT repository releases three JSON skill libraries plus generation, retrieval and updating implementations.

**Limits:** Research skill-library JSON, not SKILL.md packages. Skill/memory compression is not a single-versus-multi-agent comparison or direct context-window occupancy measurement.

**Assets:** [released_assets](<SkillRL - Evolving Agents via Recursive Skill-Augmented Reinforcement Learning/released_assets/>). Three real research SkillBank JSON libraries, generation/retrieval/update source; no SKILL.md package. License: MIT. 

## Exclusions and collection checks

- Excluded the existing Zhang and ophthalmic consistency papers; the remaining six existing titles were also checked for overlap.
- Excluded Smurfs because its first preprint is outside the window despite 2025 proceedings.
- Other relevant skill papers were not added after reaching the ten-paper cap.
- Each PDF has SHA-256, byte count, source/version metadata and pdfinfo validation in manifest.json. Asset provenance records pin repository commits and classify prompts, research skill libraries and ordinary supporting code separately.
- No downloaded research code was executed. SPOT has no explicit repository license; BenchAgent experiment branch lacks a license file; the repository main-branch MIT license is archived separately with that distinction.

Full machine-readable records: [manifest.json](manifest.json). Citation records: [references.bib](references.bib).
