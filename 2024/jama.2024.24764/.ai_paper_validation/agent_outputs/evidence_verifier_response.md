# Evidence Verifier Response

## Verification scope

- Verification stage: single evidence-verification stage, round 1 of a maximum of 2.
- Candidates reviewed: exactly V1-V5 supplied by the coordinator.
- Original PDFs and the retained page images were reopened. The narrowly authorized SAP comparison was limited to Supplement 1, PDF p. 28, section 9.9, "Planned subgroup analyses" (with its contents-page locator).
- No protocol section, web source, or external source was inspected. Source PDFs were not modified.

## Classification summary

| Candidate | Classification | Category |
|---|---|---|
| V1 / TAC-01 | **Verified** | Presentation inconsistency |
| V2 / merged FFC-1 and SCC-02 | **Rejected** | Candidate framing not supported |
| V3 / FFC-2 | **Verified** | Statistical reporting inconsistency |
| V4 / FFC-3 | **Verified** | Presentation inconsistency |
| V5 / SCC-01 | **Verified** | Statistical reporting inconsistency |

## V1 / TAC-01 - Surgeon-level categories exceed the participant denominators without a multiple-response note

**Classification: Verified**

- **Location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 7 (printed JAMA p. 859), Table 2, "Level of operating surgeon," "Level of surgeon closing fascia," and "Level of surgeon closing skin."
- **Source values/statements:** The table header is "No. of participants (%)" and states iNPWT `n = 411` and surgeon's preference `n = 410`. The rows show:
  - Operating surgeon: `319, 123, 4` and `318, 110, 1`.
  - Surgeon closing fascia: `201, 218, 26` and `193, 225, 15`.
  - Surgeon closing skin: `115, 214, 96` and `102, 241, 73`.
  - Footnote `f` defines international seniority equivalents only. It does not state that categories are non-mutually exclusive or that multiple surgeons can be counted for one participant.
- **Calculation/logical basis:**
  - Operating surgeon: `319 + 123 + 4 = 446`, exceeding 411 by 35; `318 + 110 + 1 = 429`, exceeding 410 by 19.
  - Closing fascia: `201 + 218 + 26 = 445`, exceeding 411 by 34; `193 + 225 + 15 = 433`, exceeding 410 by 23.
  - Closing skin: `115 + 214 + 96 = 425`, exceeding 411 by 14; `102 + 241 + 73 = 416`, exceeding 410 by 6.
  - The percentages also sum above 100% in every block. Multiple surgeons or levels may legitimately be recorded, but the participant-count heading and footnotes do not disclose that recording rule. The verified issue is ambiguity of presentation, not proof that the underlying counts are wrong.
- **Human verification instruction:** On Table 2, add each three-level surgeon block and read footnote `f`. Confirm from the source tabulation whether more than one surgeon/level could be recorded per operation; if so, add an explicit non-mutually-exclusive/multiple-response note, otherwise recheck the counts.

## V2 / merged FFC-1 and SCC-02 - Figure 2 allegedly adds incision length and omits a planned recruiting-center subgroup

**Classification: Rejected**

- **Main-article locations and exact statements:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF pp. 2-3 (printed pp. 854-855), Randomization, Blinding, and Minimization: minimization used degree of contamination, presence of a stoma, and recruiting center.
  - Same PDF, p. 4 (printed p. 856), Statistical Analysis: "Prespecified subgroup analyses" included "the minimization variables, such as operative contamination and presence of a stoma," plus operative procedure, skin preparation, BMI, country, assessment method, and pandemic date.
  - Same PDF, p. 9 (printed p. 861), Figure 2: a visible "Length of incision, cm" family has `<15` and `>=15` rows; no recruiting-center family appears.
- **Authorized comparison source:** `joi240145supp1_prod_1741627844.87412.pdf`, PDF p. 28, section 9.9, "Planned subgroup analyses." The SAP expressly limits planned primary-outcome subgroup analyses to degree of contamination, stoma, operative procedure, **"Size of wound"** (`<15 cm, >=15 cm`), skin preparation, country, BMI, assessment method, and the UK-only pandemic-date subgroup. Recruiting center is not in that planned list.
- **Logical basis:** Figure 2's incision-length family is the SAP-prespecified "Size of wound" analysis with the same 15-cm cutoff. The SAP does not plan recruiting center as a subgroup. Therefore, the supplied claim that Figure 2 added an unplanned incision-length analysis and omitted a planned recruiting-center analysis is not supported. The main article's abbreviated wording is imprecise, but it does not establish the candidate as framed once the expressly cited SAP is checked.
- **Human verification instruction:** Compare main Methods p. 4 and Figure 2 p. 9 with SAP section 9.9 on PDF p. 28. Match "Length of incision" to planned "Size of wound" and confirm that recruiting center is absent from the SAP's planned subgroup inventory.

## V3 / FFC-2 - The Methods omits the UK-only restriction for the pandemic subgroup

**Classification: Verified**

- **Locations:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 4 (printed p. 856), Statistical Analysis.
  - Same PDF, p. 9 (printed p. 861), Figure 2, "SARS-CoV-2 pandemic" rows and footnote `a`.
  - Confirmatory planned-analysis source: `joi240145supp1_prod_1741627844.87412.pdf`, PDF p. 28, SAP section 9.9.
- **Source/comparison statements and values:**
  - Main Methods describes a subgroup based on "the date the global pandemic was declared (patients randomized before or after March 11, 2020)" without a country restriction.
  - Figure 2 marks the pandemic subgroup with footnote `a`, "UK-based patients only."
  - The two pandemic rows report events `60` and `19` for iNPWT and `55` and `18` for surgeon's preference.
  - Figure 2's UK country row reports `79` and `73` events. The primary totals are `112` and `108`.
  - SAP section 9.9 explicitly plans "Date of COVID-19 as per World Health Organization (For UK patients only)."
- **Calculation/logical basis:** `60 + 19 = 79` and `55 + 18 = 73`, exactly the UK-row event totals, rather than the all-country primary totals of 112 and 108. Thus the figure and SAP use a UK-only estimand, while the main Methods description does not disclose that restriction. The local figure footnote does not cure the mismatch in the stated Methods population.
- **Human verification instruction:** Read the complete pandemic-subgroup sentence on main PDF p. 4, then Figure 2 footnote `a` and the two pandemic event rows on p. 9. Add the row counts and compare them with the UK row. Reconcile the Methods wording with the planned and displayed UK-only analysis.

## V4 / FFC-3 - Figure 2 omits category denominators and does not disclose missing subgroup classifications

**Classification: Verified**

- **Location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 9 (printed p. 861), Figure 2.
- **Source values/statements:** Figure 2 labels its numeric columns "No. of patients with SSI within 30 d of procedure" and gives only the overall group sizes `n = 394` and primary event totals `112` and `108`. It supplies event numerators and adjusted RRs for each category, but no category-specific denominators, missing/unknown categories, or complete-case subgroup footnote. The only figure footnote is the UK-only pandemic note.
- **Calculation/logical basis:**
  - BMI events: iNPWT `5 + 33 + 30 + 41 = 109`, leaving `112 - 109 = 3`; control `4 + 37 + 30 + 32 = 103`, leaving `108 - 103 = 5`.
  - Incision-length events: iNPWT `21 + 90 = 111`, leaving 1; control `22 + 81 = 103`, leaving 5.
  - Assessment-method events: iNPWT `77 + 15 + 9 = 101`, leaving 11; control `78 + 16 + 13 = 107`, leaving 1.
  - These shortfalls show that some primary-outcome events are absent from the displayed category rows. Missing subgroup data can explain this and do not by themselves invalidate the adjusted RRs, but the figure does not state the category denominators or quantify missing subgroup classifications. The verified issue is incomplete/ambiguous presentation, not a claim that the subgroup estimates are numerically wrong.
- **Human verification instruction:** For BMI, incision length, and assessment method, total the displayed event numerators against 112 and 108, then inspect the caption and footnote for missing-data disclosure. Request category denominators and missing/unknown counts, or an explicit complete-case subgroup-analysis note.

## V5 / SCC-01 - "No differences in quality of life" conflicts with the day-7 EuroQol contrast

**Classification: Verified**

- **Locations:**
  - `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 1 (printed p. 853), Abstract Results.
  - Same PDF, p. 6 (printed p. 858), Secondary Outcomes.
  - `joi240145supp3_prod_1741627844.89412.pdf`, PDF p. 4, Supplementary eTable 3, EQ5D-5L EuroQol score, Day 7.
- **Source/comparison statements and values:**
  - Abstract: of 7 secondary outcomes, 6 "showed no significant difference," explicitly including quality of life.
  - Main Results: "There were no differences in quality of life between the 2 groups (eTables 2-4 in Supplement 3)."
  - Supplementary eTable 3, day 7: `N = 292` vs `283`; means `0.44 (SD 0.32)` vs `0.49 (SD 0.30)`; adjusted mean difference `-0.057 (95% CI, -0.104 to -0.010)`, `P = .02`.
  - The eTable footnote says surgeon's preference is the reference and values greater than 0 favor iNPWT, so this negative estimate favors surgeon's preference.
  - The treatment-by-time interaction is `P = .10`.
- **Calculation/logical basis:** The day-7 95% CI is wholly below the null value 0 and the displayed time-specific P value is below .05. That inferential result does not correspond to the unqualified narrative that quality of life showed no difference. The nonsignificant interaction may be the intended global inferential basis and multiplicity may matter, but neither qualification is stated in the cited narrative. Verification is therefore limited to the reporting mismatch; it does not assert a significant overall longitudinal treatment effect.
- **Human verification instruction:** Compare the two unqualified main-article quality-of-life statements with eTable 3's day-7 estimate, CI, P value, and interaction P value. Clarify whether the conclusion rests on the global interaction or time-specific contrasts and qualify the narrative accordingly.

## Existing uncertain leads retained separately

### U1 - Wound-related readmission adjusted risk difference

**Status: Uncertain; not a verified candidate**

- **Location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 8 (printed p. 860), Table 3, "Hospital readmission for wound-related complications."
- **Values:** `11/399 (3%)` vs `11/398 (3%)`; adjusted RD `0.010 (95% CI, -0.014 to 0.034)`; adjusted RR `1.02 (95% CI, 0.45 to 2.31)`, `P = .96`.
- **Calculation/uncertainty basis:** The crude RD is `11/399 - 11/398 = -0.000069` (approximately zero), which is not close to 0.010. However, main PDF p. 4 states that adjusted RD and RR came from separate mixed-effects binomial models using identity and log links. The supplied documents do not provide fitted covariates or model outputs, so agreement between the crude RD, adjusted RD, and an RD derived from the adjusted RR is not a valid document-only requirement.
- **Human verification instruction:** Check the original model output/typesetting source to confirm whether adjusted RD `0.010` is intended.

### U2 - Figure 1 total deaths versus Table 3 30-day mortality

**Status: Uncertain; not a verified candidate**

- **Locations:** Main PDF p. 3 (printed p. 855), Figure 1 footnote `b`; main PDF p. 6 (printed p. 858), Safety Outcomes; main PDF p. 8 (printed p. 860), Table 3.
- **Values/statements:** Figure 1 says "A total of 25 deaths were reported" (`10` iNPWT, `15` surgeon's preference). The Safety Outcomes text and Table 3 report mortality "within 30 days" as `10/411` and `14/410`, totaling 24.
- **Logical basis for uncertainty:** The one-death difference is visible, but Figure 1 does not state that all 25 deaths occurred within 30 days. A control-group death after day 30 would reconcile the statements. The supplied results pages do not establish identical time windows.
- **Human verification instruction:** Confirm the time window for all 15 control-group deaths in Figure 1. Reconcile only if all 15 occurred within 30 days; otherwise make the time distinction explicit.

