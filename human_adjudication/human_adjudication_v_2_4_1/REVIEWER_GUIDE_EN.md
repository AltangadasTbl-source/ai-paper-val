# v.2.4.1 Reviewer Guide (Excel independent primary review)

Applies to: v.2.4.1 primary-review workbooks for 2018, 2019, 2024 and 2025.
Date: 2026-10-11. Field and option definitions are governed by the `Codebook` sheet in each workbook. Where this guide and the `Codebook` differ, follow the `Codebook`.

This guide is the English counterpart of [REVIEWER_GUIDE_CN.md](REVIEWER_GUIDE_CN.md). The two versions have the same content and section numbering.

---

## 1. Task

The AI pipeline (workflow 1.6.2) checked each JAMA paper package for consistency in numerical and statistical reporting and raised a set of candidates. A candidate is a possible problem flagged by the AI. **It is not a confirmed error.**

Your task is an **independent primary review** of the workbook for the year assigned to you:

1. For each candidate, check the original PDFs and decide independently whether to `retain`, `exclude` or `discuss` it.
2. Confirm or change the review domain suggested by the AI, and answer the judgments that domain requires.
3. Use the workbook's built-in checks to confirm that your entries are complete, then return the workbook.

Each year has two reviewers (`R_A` and `R_B`) who review the same candidates independently. **Do not consult the other reviewer.** The coordinator resolves disagreements after both workbooks are returned.

### Review load in this version

| Year | Papers | Candidates per reviewer | statistical_results | report_internal_inconsistency | plan_material | protocol_report |
|---|---:|---:|---:|---:|---:|---:|
| 2018 | 10 | 115 | 49 | 4 | 7 | 55 |
| 2019 | 10 | 87 | 30 | 0 | 4 | 53 |
| 2024 | 10 | 113 | 51 | 2 | 15 | 45 |
| 2025 | 15 (13 with 1.6.2 output) | 109 | 33 | 3 | 11 | 62 |

The domain counts are AI suggestions, not human judgments. About half of the candidates are `protocol_report`; Section 6.4 explains why.

---

## 2. Before you start

### 2.1 Files

| Item | Location |
|---|---|
| Your blank workbook | `human_adjudication/human_adjudication_v_2_4_1/<year>/human_adjudication_v_2_4_1_<year>_<R_A or R_B>.xlsx` (use only the file the coordinator assigned to you) |
| Paper packages | `<year>/<paper-id>/` at the repository root, for example `2019/jama.2019.10517/` |
| AI final report | `<year>/<paper-id>/.ai_paper_validation/final_report_1_6_2.html` (or `.md`) |
| Pipeline definitions of domains and relationship codes (reference) | `QUALITY_CONTROL_SCOPE.md` at the root of each package, sections "The four review domains" and "Relationship types" |

### 2.2 Tools

- Desktop Excel. The dropdowns, formulas and conditional formatting require Excel.
- A PDF reader that can jump to a page.
- R or a calculator for recalculation (Section 9).

### 2.3 Independence rules (mandatory)

1. **Open only the workbook assigned to you.** Do not open the other role's file.
2. **Do not open locations that contain earlier answers or AI judgments:**
   - every workbook under `human_adjudication/human_adjudication_v_2_3_1/`, especially `ai_reviewer_runs/` and `Bulun_version/`. Some candidates overlap with this version, and those folders contain completed judgments;
   - `human_adjudication/previous/`;
   - `review_<year>.md`, `spot_review_*.md` and `reclassified_candidates.*` under `meta_report/`;
   - `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`.
3. **Use only the 1.6.2 reports.** The `review_1_5_*` and `review_1_6_1` folders in a package, and any older `final_report*.md` without `1_6_2` in its name, come from earlier versions of the pipeline. Do not rely on them.
4. **Judge first, then read the AI's reasoning.** Form your judgment from the original PDFs, then consult the final report card if needed (Section 4). If the card changes your judgment, say so in column R.
5. Do not write anything in the final report, and do not modify any file in a paper package. Files such as `AGENTS.md` and `START_PROMPT.md` at a package root are pipeline run instructions and have no bearing on human review.

---

## 3. Workbook structure

### 3.1 Sheets

| Sheet | Purpose |
|---|---|
| `Setup` | B2: your reviewer ID or name (required). B3: full name (optional). B4 (role) and B5 (year) are preset; **do not change them**. |
| `Checks` | Summary: total candidates, `PRIMARY READY` rows, `discuss` rows, unfinished rows and `Workflow status`. |
| `Papers` | List of papers and their candidate counts. The links in the `Review worksheet` column jump to the matching `C_` sheet. |
| `C_<paper-id>` | One sheet per paper and one row per candidate. This is the main work area. |
| `Codebook` | English definitions of every field and option. |

The workbook has no evidence sheet and no results summary. The evidence is in the original PDFs and the final report cards; the coordinator compiles the results.

**2025 note:** `jama.2025.11178` and `jama.2025.15185` do not yet have workflow 1.6.2 results. Their `C_` sheets contain only the header and a one-line note, `Papers` shows 0 for them, and `Checks` leaves them out; nothing needs to be done there. The 2025 cohort also includes two papers with `jama.2024.*` IDs (`jama.2024.24764` and `jama.2024.27643`), stored under the repository's `2025/` folder. The workbook, not the ID, determines the year.

### 3.2 Columns of a `C_` sheet

| Column | Name | What to do |
|---|---|---|
| A | Candidate key | Read only. Format `<year>::<paper-id>::Cxxx`. **Do not edit.** `Cxxx` matches the card number in the final report. |
| B | Candidate title | Read only. Same as the card title in the final report. |
| C | Source location | Read only. Original file name and PDF page. Where the report omitted the file name, it was added as `<file name> — <location>`. |
| D | Disposition | Required: `retain`, `exclude` or `discuss`. Blank at the start. |
| E | Review domain | Prefilled with the AI suggestion; editable. |
| F | Complete | `no` while drafting; change to `primary_done` after your manual review. |
| G | Validation hint | Formula; read only. |
| H | Statistical_or_numerical issue | Depends on the domain. |
| I | Substantiveness | Depends on the domain. |
| J | Downstream impact | Optional. |
| K | Report-internal or planning-material inconsistency | Depends on the domain. |
| L | Protocol interpretation | Optional. |
| M–Q | Hidden blank columns | Not used. |
| R | Notes (optional) | Optional. Record in **English** the locations checked, recalculations and reasoning. |

### 3.3 Default formulas in H–L

Unfilled cells in H–L hold formulas. If the field may apply (D is blank or `retain`, and E is the matching domain), the cell shows blank. Otherwise it shows `not_applicable` and is shaded as inactive.

- Choosing an answer from the dropdown **overwrites** the formula. This is expected.
- If you later change D or E, **answers already entered are not cleared automatically**. Delete answers that no longer apply (leaving the cell blank is enough); otherwise G shows `CLEAR INACTIVE VALUES`.
- Do not choose `not_applicable` for an applicable field. It means "does not apply", not "no problem" or "uncertain".

---

## 4. Final report cards (supporting material)

In each paper's `final_report_1_6_2.html`, every candidate has a card under `Candidate Evidence Cards`, titled `Cxxx — <title>`. Useful fields:

| Field | Use |
|---|---|
| Candidate statement | One-sentence statement of the discrepancy; fuller than the title in column B |
| Exact source locations / Source evidence | Source locations with page links, and quoted excerpts |
| Reported-versus-comparator, Calculation | The comparison made and the AI's recalculation |
| Relationship type / All relationships / Compared document roles | Which documents are involved (Section 5) |
| Qualifying route | Why the AI included the candidate: `Route A, category N` (a category that is always registered) or `Route B` (general criteria) |
| Alternative source-grounded interpretations | Alternative explanations the AI considered |
| Classification rationale / ambiguity | The AI's reasons for the domain, and its uncertainty |
| Affected result or extracted value | The result or extractable value that may be affected |

"reproduced" and "CONFIRMED" on a card describe only the AI's own recheck and inclusion audit. **They are not human conclusions**, and they do not mean you should choose `confirmed_issue`.

Known limitations: column C for `2018::jama.2018.18020::C022` has no file or page, because the report only says "see the table below". Use the source-evidence table in that card. Some column C entries are long, because lists or tables were joined into one paragraph separated by `; `.

The original PDF always governs. The pipeline's text extraction or OCR can lose minus signs, decimal points, superscripts and subscripts, or merge adjacent rows.

---

## 5. Relationship codes and the four domains

| Code | What is compared | Matching domain |
|---|---|---|
| `S_W` | Within one report document (within the main article, or within one non-plan supplement) | `statistical_results` or `report_internal_inconsistency` |
| `S_C` | Between two report documents (main article and a non-plan supplement, or two supplements) | `statistical_results` or `report_internal_inconsistency` |
| `P_R` | Between the report (main article or results supplement) and the plan (protocol, SAP) | `protocol_report` |
| `P_P` | Within plan material only, or between plan documents or versions | `plan_material` |

When a candidate involves several relationships, the pipeline chooses the primary one by precedence `P_R` > `P_P` > `S_C` > `S_W`. A document that only corroborates one side is not a relationship. For example, if a protocol merely confirms the correct value in an inconsistency inside the report, the candidate remains a report-internal problem.

The relationship code is not shown in the workbook, and changing E does not change it. Choose E by **the materials you actually compare and the nature of the problem** (Section 6).

---

## 6. The four review domains: meaning and typical examples

> Note: all examples below are **invented for illustration**. None is taken from a candidate in this review, so that they do not influence your independent judgment. Each table lists common patterns and the usual line of reasoning; your actual judgment follows the source documents and the `Codebook`.

### 6.1 `statistical_results`

**Meaning:** whether numbers, estimates, confidence intervals, denominators, tests or statistical method logic in the report materials are wrong, judged by recalculation or statistical definitions. The pipeline puts every problem about counts, estimates, intervals, tests or statistical methods here, even when it spans two report documents.

**Required:** H (is there an issue) and I (is it substantive). J is optional.

**Typical patterns:**

| Pattern | Invented example | Line of reasoning |
|---|---|---|
| Count, denominator and percentage do not agree | A table prints "27/180 (21.0%)", but 27/180 = 15.0% | First rule out a different denominator (e.g., participants with complete data). If the mismatch remains, usually `confirmed_issue`; if the value would be extracted, I is usually `substantive` |
| Interval and P value incompatible | "HR 0.82 (95% CI 0.70–0.96); P = .21" | The interval implies P of about .01, which conflicts with .21. First check whether both come from the same model; if so, usually `confirmed_issue` |
| Point estimate outside its interval, or limits in the wrong order | "RD 4.6 (95% CI 5.1 to 9.8)" | Usually a typographic or transcription error. Whether it is `substantive` depends on whether it changes significance or an extracted value |
| Abstract and body disagree | Abstract "OR 1.45", body table "OR 1.54" | A difference beyond rounding. Usually `substantive` if a reader cannot tell which value to take |
| Calculation does not reproduce | Every other row of a table reproduces with the Wald method, but one row's CI is too narrow | Establish the method first. If it remains unclear, use `probable_issue` or `indeterminate` and state in column R what information is missing |
| Gap in method logic | The text describes a paired design, but the table footnote names an independent-samples t test | Judge whether the report contradicts itself, not which method you prefer |

**Common pitfalls:** rounding (first check how many decimals the source keeps); adjusted versus unadjusted estimates; ITT versus per-protocol; continuity correction or none; categories of multiple-choice items or competing risks need not sum to the total. If a difference is due to rounding alone, choose `exclude`, or `retain` with `not_issue` (see Section 7, Step 3).

### 6.2 `report_internal_inconsistency`

**Meaning (per the `Codebook`):** an inconsistency within the main paper, within the updated supplement, or between the two. It is not restricted to nonstatistical content, but if you are specifically judging a numerical or statistical reporting error, use `statistical_results` instead.

The pipeline's inclusion rule is narrower: only conflicts between report locations about which outcome, time point, analysis set or comparison a number belongs to, such that a reader cannot tell which result applies. Differences in wording or labels alone are not included. As a result, this domain is rare in this version (4 in 2018, 0 in 2019, 2 in 2024).

**Required:** K.

**Typical patterns:**

| Pattern | Invented example | Line of reasoning |
|---|---|---|
| One result tied to different time origins | The abstract defines the outcome as "90 days from randomization"; the supplement footnote for the same result says "90 days from discharge" | The two origins change what the result means; usually `substantive_inconsistency` |
| Subgroup or population labels cannot be matched to values | A forest plot is labeled "≤6 h / >6 h", but the table has only one set of values and does not say which group they belong to | `substantive_inconsistency` or `indeterminate`, depending on whether a reader can tell |
| Outcome hierarchy inconsistent within the report | The methods call an outcome tertiary; the discussion lists it among secondary outcomes | `substantive_inconsistency` or `minor_presentation`, depending on whether it affects understanding |
| Different wording, same meaning | "participants" and "enrolled patients" refer to the same group | `non_inconsistency`; usually change to `exclude` |

### 6.3 `plan_material`

**Meaning:** an inconsistency within the protocol or SAP, or between plan documents or versions, in a statistical design element that the reported analysis relies on. Only plan material is compared; the report is not involved.

**Required:** K.

**Typical patterns:**

| Pattern | Invented example | Line of reasoning |
|---|---|---|
| Numeric slip within the plan | The body assumes an event rate of 0.08%, while the sample-size appendix uses 0.8% | Determine which value was actually used for the sample size. If it affects how the design is understood, usually `substantive_inconsistency` |
| Sample size or power does not reproduce from the stated inputs | The SAP claims "80% power to detect a 15% difference", but its stated proportions and sample size give about 60% | First look for unstated assumptions (one-sided test, dropout, continuity correction). If it cannot be resolved, `indeterminate` |
| Conflicting interim, stopping or noninferiority rules | The body gives a noninferiority margin of −0.10; the signed copy of the same SAP gives +0.10 | A conflict of sign or direction changes the decision region; usually `substantive_inconsistency` |
| Definitions differ between plan versions | The protocol times the outcome from "start of surgery"; the SAP uses "start of anesthesia" | Judge whether the difference affects the reported analysis. A wording difference can be `minor_presentation` |
| Content that is not a design element | Results of earlier studies quoted in the protocol's background section are themselves inconsistent | Does not affect this trial's design or analysis; usually `exclude` |

If a `plan_material` candidate actually compares the plan with the report, change it to `protocol_report`, and vice versa.

### 6.4 `protocol_report`

**Meaning:** the report differs from the protocol or SAP in a statistical design or analysis element. This **describes a difference**. It does not establish a protocol violation or an improper change. The `Codebook` states that no search for change records or reasons is required.

**Required:** nothing beyond D and a valid E. L is optional.

**Why there are so many:** workflow 1.6.2 registers three situations as soon as they are reproduced, without screening for context or wording:
- a change in an outcome's status (primary, secondary, safety, etc.) or in a composite definition;
- an analysis the report calls prespecified that the supplied plan does not contain;
- a planned primary or key secondary analysis that is not reported.

In addition, protocols and SAPs are often long and come in several versions. Every specific commitment in them is a point of comparison, and a journal article has limited space.

**Typical patterns:**

| Pattern | Invented example | Line of reasoning |
|---|---|---|
| Planned analysis or result not found in the report | The SAP specifies a complete-case sensitivity analysis of the primary outcome; neither the article nor the supplements report it | First **search every supplied report document** (main article and all results supplements). If you find it, the AI missed it: `exclude`. If it is truly absent: `retain` |
| Analysis method or model changed | The plan specifies a Cox model; the report uses a log-binomial model. Covariate sets differ. The number of imputations differs | If the methods truly differ, `retain`; L is usually `substantive_difference` |
| Outcome definition, time window or measurement changed | The planned primary outcome is assessed at 12 months; the report uses 6 months | A typical `substantive_difference` (this is the `Codebook`'s own example) |
| Population, eligibility, randomization strata or subgroup cutpoints changed | The plan enrolls age ≥65; the report says ≥60. A subgroup cutpoint changes from the median to a fixed value | Judge whether the analysis population or subgroup membership changes |
| Outcome hierarchy changed, or "prespecified" claim without a plan basis | A planned secondary outcome is reported as post hoc; the report calls a subgroup "prespecified" but the plan does not contain it | First check all plan versions. If an earlier or later version contains it, consider `version_timing` |
| Equivalent wording | The plan says "week 12"; the report says "12 weeks after baseline" | `non_inconsistency`; usually `exclude` |

**Notes on L:**

- A change the report itself discloses (for example, labeled post hoc, or GEE used after the planned model failed to converge) is still a difference between plan and report. Disclosure does not remove the difference. Note "disclosed in report, p. x" in column R.
- If the difference may reflect comparison of different protocol or SAP versions, and the materials do not show which came first, choose `version_timing`.
- Leaving L blank does not block completion. Blank means "not described", not "no difference".

---

## 7. Step-by-step procedure

### Step 1: Make a working copy and enter your identity

1. Open your assigned workbook in Excel and **Save As** a working copy, for example `human_adjudication_v_2_4_1_<year>_<role>_<your ID>.xlsx`.
2. Enter your ID or name in `Setup` B2 (not `R_A`/`R_B`). B3 is optional.
3. Column G should change from `CHECK REVIEWER ID` to `PRIMARY DRAFT` or another field message.

### Step 2: Check each candidate, paper by paper

Work through the papers in `Papers` order, starting each paper at C001:

1. Read the title in column B and the locations in column C. The title is short; for the full statement, see the card's Candidate statement.
2. **Open the original PDF at the stated page.** Confirm that the cited text, table or figure exists and that the values match the AI's description.
3. Find the comparator (other rows of the same table, the body text, the abstract, a supplement, the protocol or SAP). Confirm that both refer to **the same outcome, population, time point, definition and model**.
4. For numerical candidates, **recalculate yourself** (Section 9).
5. Consider alternative explanations: rounding, a different denominator or analysis set, a different test, adjusted versus unadjusted estimates, a disclosed approximation or amendment.
6. After forming your judgment, you may open the card to compare the AI's calculation and alternative interpretations, and to check whether you missed evidence.

### Step 3: Choose D (Disposition)

| Option | When to use |
|---|---|
| `retain` | After checking, keep the candidate as a finding: an issue is confirmed, or there is a difference worth recording. Then answer the fields for its domain. Retaining a protocol difference does not confirm an error. |
| `exclude` | Checked, and should not be kept: the apparent inconsistency has a satisfactory explanation, the AI misread the source, the comparison is not like with like, or the planned result is in fact reported. |
| `discuss` | Checked carefully, but the disposition cannot be settled from the available material and needs later discussion. This defers the decision; it is not an untouched row. State in column R where you are stuck. |

A blank D means untouched. It is not `discuss`.

`exclude` versus "`retain` with no issue": if you confirm there is no problem at all (for example, the difference is fully explained by different definitions), usually choose `exclude`. If the candidate is worth keeping on record but your judgment of whether it is a problem is negative or uncertain, choose `retain` and then `not_issue`, `non_inconsistency` or `indeterminate` in H or K.

### Step 4: Confirm or change E (Review domain)

E is prefilled with the AI suggestion. **It is not a human judgment.** Choose according to Sections 5 and 6:

| Domain | Required | Optional | Not applicable |
|---|---|---|---|
| `statistical_results` | H, I | J | K, L |
| `report_internal_inconsistency` | K | — | H, I, J, L |
| `plan_material` | K | — | H, I, J, L |
| `protocol_report` | — | L | H, I, J, K |

When D is `exclude` or `discuss`, none of H–L applies (leave them blank or `not_applicable`), but D and a valid E are still required. After changing E, delete old answers in fields that no longer apply.

### Step 5: Answer H–L

**H: Statistical_or_numerical issue** (required for `statistical_results`): does a statistical or numerical reporting issue exist? This records certainty only; importance goes in I.

| Option | Meaning |
|---|---|
| `confirmed_issue` | The evidence establishes a reporting issue or contradiction, even if the correct value is unknown |
| `probable_issue` | The evidence favors an issue, but an unresolved limitation or plausible alternative remains |
| `not_issue` | The apparent discrepancy is explained by a valid calculation, definition, method or context |
| `indeterminate` | The evidence does not allow a decision |

**I: Substantiveness** (required for `statistical_results`): could the issue meaningfully affect interpretation or data use? An issue can be both `confirmed_issue` and `minor_presentation`.

| Option | Meaning |
|---|---|
| `substantive` | Could change interpretation, data extraction or downstream analysis |
| `minor_presentation` | The intended meaning is clear; a small formatting, labeling or typographic problem |
| `indeterminate` | Not enough information to decide |

**J: Downstream impact** (optional for `statistical_results`): blank means not assessed, not `unlikely`. `direct`: the affected value itself may be extracted or used in later analysis (describes potential impact, not harm already done); `possible`: an indirect or uncertain route to affecting later use exists; `unlikely`: the result remains clear and usable; `unknown`: the materials are insufficient to judge.

**K: Report-internal or planning-material inconsistency** (required for `report_internal_inconsistency` or `plan_material`):

| Option | Meaning |
|---|---|
| `substantive_inconsistency` | The conflict could materially change how the study, population, procedures or results are understood |
| `minor_presentation` | A real discrepancy that mainly affects presentation; the intended meaning is clear |
| `non_inconsistency` | Not contradictory once definitions, populations, time points or context are considered |
| `indeterminate` | Insufficient material to establish whether there is a conflict or how much it matters |

**L: Protocol interpretation** (optional for `protocol_report`):

| Option | Meaning |
|---|---|
| `substantive_difference` | Plan and report meaningfully differ in an outcome, population, procedure or analysis (describes the difference only) |
| `minor_presentation` | A small wording or labeling problem; the meaning remains clear |
| `version_timing` | The difference may reflect which version or date is compared; the materials cannot resolve the sequence |
| `non_inconsistency` | Compatible after checking (usually change D to `exclude`) |
| `indeterminate` | The evidence does not support a more specific description |

### Step 6: Write a note in column R (recommended, in English)

For every `retain` or `discuss` row, and every row where you changed E, write a one-sentence note: the files and pages checked, recalculation results (for example `27/180 = 15.0%; printed 21.0%`), and the key reason or how you differ from the AI. Do not record participant-level data.

### Step 7: Mark complete and check G

1. When a row is filled in and correct, change F to `primary_done`.
2. G should show `PRIMARY READY`; otherwise see Section 8.
3. Mark `primary_done` only after you have actually completed the manual review.

### Step 8: Editing a completed row

Change F back to `no` first. Then revise D, E or the judgments and delete answers that no longer apply. After reviewing the row again, mark it `primary_done`. The formulas do not undo a completion flag automatically.

### Step 9: Delivery

1. In `Checks`, confirm that `Workflow status` is `PRIMARY READY` and `Unfinished rows` is 0.
2. `discuss` rows can be `PRIMARY READY` but remain unresolved; `Checks` counts them separately.
3. Save, send **your own workbook** to the coordinator, and keep a backup. Do not merge or forward the other reviewer's file.

---

## 8. Column G (Validation hint) messages

All three years use the same formulas, so the messages are identical:

| Message | Meaning | Action |
|---|---|---|
| `CHECK REVIEWER ID` | `Setup` B2 is empty or contains only spaces | Enter your ID in B2 |
| `CHECK KEY` | The key in column A is empty, duplicated or belongs to another paper | Undo the edit to column A. When sorting, move whole rows (A:R, including hidden columns) |
| `CLEAR INACTIVE VALUES` | An old answer remains in a field that does not apply under the current D/E | Delete those cell contents |
| `CHECK FIELDS` | D or E is empty or invalid, a required judgment is missing, or an applicable field has an invalid value (including pasted values or a wrongly chosen `not_applicable`) | Reselect from the dropdown and fill the required fields |
| `CHECK COMPLETE` | F is neither `no` nor `primary_done` | Reselect from the dropdown |
| `PRIMARY DRAFT` | The fields are valid, but F is not yet `primary_done` | Change F to `primary_done` when the review is done |
| `PRIMARY READY` | The entry is complete, valid and marked complete | Nothing to do |
| `CHECK INPUT / KEY` | The formula met unexpected input | Look for pasted abnormal values or an edited key |

G checks only **whether entries are complete and valid**. It does not check whether a scientific judgment is correct.

---

## 9. Common recalculations (R)

These are standard formulas. Compare the results against the method the source used. If the source used model-adjusted estimates, the bootstrap or another method, rough calculations are for reference only.

```r
# Proportion and risk difference (percentage points) with Wald 95% CI
rd <- function(a, n1, c, n2, level = 0.95) {
  p1 <- a / n1; p2 <- c / n2; z <- qnorm(1 - (1 - level) / 2)
  d <- p1 - p2; se <- sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
  round(100 * c(p1 = p1, p2 = p2, rd = d, lower = d - z * se, upper = d + z * se), 2)
}

# Risk ratio with log-scale Wald 95% CI
rr <- function(a, n1, c, n2, level = 0.95) {
  z <- qnorm(1 - (1 - level) / 2)
  est <- (a / n1) / (c / n2); se <- sqrt(1 / a - 1 / n1 + 1 / c - 1 / n2)
  round(c(rr = est, lower = exp(log(est) - z * se), upper = exp(log(est) + z * se)), 3)
}

# Odds ratio with log-scale Wald 95% CI (a, b = events/non-events in group 1; c, d in group 2)
or <- function(a, b, c, d, level = 0.95) {
  z <- qnorm(1 - (1 - level) / 2)
  est <- (a * d) / (b * c); se <- sqrt(1 / a + 1 / b + 1 / c + 1 / d)
  round(c(or = est, lower = exp(log(est) - z * se), upper = exp(log(est) + z * se)), 3)
}

# Approximate two-sided P value implied by an estimate and its 95% CI
# ratio = TRUE for RR/OR/HR (log scale); FALSE for differences
p_from_ci <- function(est, lower, upper, ratio = TRUE) {
  if (ratio) { est <- log(est); lower <- log(lower); upper <- log(upper) }
  se <- (upper - lower) / (2 * qnorm(0.975))
  2 * pnorm(-abs(est / se))
}

# Chi-square test on a 2x2 table, with and without continuity correction
chisq_both <- function(a, n1, c, n2) {
  m <- matrix(c(a, n1 - a, c, n2 - c), nrow = 2, byrow = TRUE)
  c(yates = chisq.test(m, correct = TRUE)$p.value,
    no_correction = chisq.test(m, correct = FALSE)$p.value)
}

# Two-sample power for proportions (compare with a plan's stated power)
# power.prop.test(n = 150, p1 = 0.42, p2 = 0.27, sig.level = 0.05)

# Display-precision check: does a printed value fit the interval implied by
# rounding each displayed input to its last shown digit?
half_unit <- function(x, digits) c(x - 0.5 * 10^-digits, x + 0.5 * 10^-digits)

sessionInfo()
```

---

## 10. Frequently asked questions

**Must I keep the prefilled domain in E?** No. Decide for yourself following Sections 5 and 6, and clear old answers in fields that no longer apply.

**The card says "reproduced" or "CONFIRMED". Must I choose `confirmed_issue`?** No. That is only the AI's internal recheck status.

**The report already explains the reason for a `protocol_report` change. Should I still `retain` it?** The difference still exists, so usually `retain` it and note in column R that it was disclosed. The `Codebook` does not ask you to judge whether the change was justified.

**A planned analysis is flagged as "not reported", but I found it in a supplement.** Choose `exclude` and give the location in column R.

**Can I sort the rows?** Yes, but select whole rows A:R (including hidden columns M–Q) when sorting.

**Is the workbook protected?** No. Do not edit columns A–C, the formulas in G–L (except by answering through the dropdowns), or `Setup` B4–B5. If you change one by mistake, undo or restore from your backup.

**A page is scanned and the text cannot be searched.** Read the page image directly. The OCR text under `.ai_paper_validation/` can help you locate content, but always confirm values against the PDF.

**I found a suspected error outside the candidates.** Do not add a row. Record it briefly in column R of a related row, or tell the coordinator separately.
