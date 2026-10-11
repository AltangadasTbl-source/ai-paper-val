# Mechanical evidence recheck — Workflow 1.6.2

Runtime agent: `/root/evidence_recheck`; fresh `qc162_evidence_rechecker`; run model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Assigned stable IDs: C001–C015. Status: COMPLETE. This artifact records evidence facts and classification only. Every ID remains Pending Human Adjudication.

The complete current ledger and independent initial screening log were read, together with the cited current numeric, cross-source, bounded cross-source-repair and statistical-pass-1 findings as provenance. The normative scope and mechanical recheck/classification contract govern this record. Earlier review conclusions and external evidence were not used. The screen contains 25 findings, 15 included anchors and 10 screened observations; the screened missingness, population, lung-subgroup and AIS-completeness branches do not become candidate bases in this recheck.

## Source authority, roles, locations and tooling

Locations below are PDF page numbers, counted from the first supplied PDF page. Every comparison was read anew from the exact supplied PDF using direct native layout extraction with preserved page boundaries. Fresh source renders were inspected for all disputed numeric display cells and the governing protocol/SAP analysis paragraphs. Existing extraction was a locator only. New derivatives are confined to `preprocessing/recheck/`; no source, reused artifact, ledger or screen was modified.

| Source | Role by content | New native derivative | Exact engine and command |
|---|---|---|---|
| `jama_arleth_2024_oi_240147_1738701765.27201.pdf` | REPORT: completed trial methods, results, figures and tables | `preprocessing/recheck/main.txt` | Poppler 26.01.0, CPU; `pdftotext -layout SOURCE OUTPUT` |
| `joi240147supp1_prod_1738701765.28701.pdf` | PLAN: original/final protocols, amendment log and prospective SAP | `preprocessing/recheck/plan.txt` | Poppler 26.01.0, CPU; `pdftotext -layout SOURCE OUTPUT` |
| `joi240147supp2_prod_1738701765.29201.pdf` | REPORT: completed-trial eMethods and result tables | `preprocessing/recheck/results.txt` | Poppler 26.01.0, CPU; `pdftotext -layout SOURCE OUTPUT` |

Fresh visually inspected renders: main pp.1,2,3,5,6,8; results pp.14,15,18,20,24; plan pp.26,62,84,85,88,89,101. Each has path `preprocessing/recheck/<main|results|plan>-N.png`. Engine: Poppler 26.01.0; device: CPU; command for each page: `pdftoppm -f N -l N -singlefile -r 110 -png SOURCE OUTPUT_PREFIX`. No OCR, fallback environment or GPU was required. Additional cited text/context pages were read directly from their supplied native PDF pages, including every ledger location listed in the cards below. Text pages and source renders agree on the disputed readings.

For percentage calculations, the conservative input intervals allow ±0.5 per printed integer count/denominator, truncate negative numerator bounds at zero, and allow ±0.05 for one-decimal percentages or ±0.5 for integer percentages. The recomputed lower limit uses the lowest numerator and highest denominator; the upper limit uses the converse. The gap between that interval and the printed percentage interval is divided by the absolute printed percentage. Printed-copy comparisons use both half-unit intervals. Categorical model, status and predicate comparisons have no rounding interval. Route A category 1 is never screened by relative rounding gaps. Arithmetic below was independently evaluated from source inputs.

## Classification and evidence-state summary

| ID | Review domain | Relationship type | All relationships | Evidence state | Recheck classification fact |
|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | reproduced | Numeric population attribution within the main report |
| C002 | protocol_report | P_R | P_R, P_P, S_W | reproduced | Add S_W: main p.5 contains both dropout-inclusive and evaluable target descriptions |
| C003 | protocol_report | P_R | P_R, P_P | reproduced | Protocol/SAP hierarchy differs; reports implement SAP hierarchy |
| C004 | protocol_report | P_R | P_R, P_P | reproduced | Primary covariate specifications differ across protocol, SAP and report |
| C005 | protocol_report | P_R | P_R | reproduced | SAP primary subgroup has no reported counterpart |
| C006 | protocol_report | P_R | P_R | reproduced | Governing SAP retains trauma clock while report labels randomization status |
| C007 | protocol_report | P_R | P_R, P_P | reproduced | Named categorical secondary tests differ from SAP/report models |
| C008 | statistical_results | S_C | S_C, S_W | reproduced | Main RD/OR nominal readings differ; supplementary OR tests extend comparison |
| C009 | protocol_report | P_R | P_R | reproduced | SSI planned and reported event predicates differ |
| C010 | statistical_results | S_C | S_C, S_W | reproduced | ICU count/membership mapping differs within supplement and across reports |
| C011 | statistical_results | S_C | S_C, S_W | reproduced | Supplement count/percentage pair and main percentage counterpart differ |
| C012 | statistical_results | S_W | S_W | reproduced | Both Bern count/percentage pairs fail within one result table |
| C013 | statistical_results | S_W | S_W | reproduced | Walk-in count/percentage pair fails within one result table |
| C014 | statistical_results | S_W | S_W | reproduced | Vascular-surgery count/percentage pair fails within one result table |
| C015 | statistical_results | S_W | S_W | reproduced | All four exclusion count/percentage pairs use discordant denominators |

Precedence is P_R > P_P > S_C > S_W. Compared plan paragraphs are PLAN by prospective content despite their supplement packaging. All main and results-supplement locations are REPORT by their completed-trial content. No role or primary-type/domain replacement is needed. The sole relationship expansion is C002's additional S_W. Context-only plan pages in C008/C010 do not create P_R. Classification and prose clarifications are not transcription changes: 15 evidence states are `reproduced`, zero are `reproduced_after_transcription_correction`, and zero are `not_reproduced`.

## C001 — Population attribution of randomized counts

**Location found / source matched:** REPORT [main p.1, Abstract Interventions and Results](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=1) gives randomly assigned restrictive n=733/liberal n=724 and separately 1979 randomized/1508 completed. REPORT [p.2, Key Points Findings](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=2) says “Among 1508 randomized adult trauma patients.” Both affected short-section readings are confirmed visually.

**Comparator matched:** REPORT [p.3, Figure 1](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3) prints 1979 randomized, 2 lost envelopes, allocations 983/994, received strategy 750/758 and primary analysis 733/724. REPORT [p.5, Trial Population](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) repeats 1979 randomized, 1508 completed and 1457 primary-available, 733/724 by arm. Every registered location is found.

**Rule / calculation / precision:** Focus A and route B: compare the population quantity attached to the printed counts. Integer-copy intervals are [732.5,733.5] versus [982.5,983.5], gap 249/983=0.253306; [723.5,724.5] versus [993.5,994.5], gap 269/994=0.270624; and [1507.5,1508.5] versus [1978.5,1979.5], gap 470/1979=0.237494. All exceed 0.05. The observed primary denominators themselves reconcile across locations.

**Inputs / missing definitions:** All printed counts and their flow identities are available. Missing: intended population qualification for the abstract intervention n values and the Key Points count. No raw data are needed to reproduce the attribution discrepancy.

**Alternative / direct versus inferred:** Direct: the sections attach different numeric sets to randomization. Alternative: “randomized” describes membership in a retained randomized cohort, while the n values intentionally identify completed/analyzed participants. This interpretation is supported by the body but remains an interpretation of the short-section labels. No clinical or allocation-process conclusion is inferred.

**Classification:** Compared roles REPORT main short sections versus REPORT main flow/body; relationship type S_W; all relationships S_W; review domain statistical_results. Numeric counts require this domain even though the source discrepancy includes a population label. No PLAN comparison is involved.

**Evidence state:** reproduced. Determining fact: all three copy interval gaps remain above 0.05 under the printed allocation/retained/analyzed identities.

**Exact remaining human question:** Do abstract n=733/724 and Key Points 1508 denote allocation-stage randomized patients, completed participants or analyzed participants, and which counts should be extracted as randomized sample sizes?

## C002 — Accrual maximum and target populations

**Location found / source matched:** PLAN [original synopsis p.13](../../../joi240147supp1_prod_1738701765.28701.pdf#page=13) and [final synopsis p.49](../../../joi240147supp1_prod_1738701765.28701.pdf#page=49) state inclusion up to 1600 and ending with 710 per arm with 30-day follow-up, total 1420. PLAN [original statistics p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26) and [final statistics p.62](../../../joi240147supp1_prod_1738701765.28701.pdf#page=62) repeat 1420 evaluable and maximum 1600 while follow-up matures. All four repeated plan locations match.

**Comparator matched:** PLAN [SAP p.85, Sample size calculation](../../../joi240147supp1_prod_1738701765.28701.pdf#page=85) gives 710 per arm, 1420 total including 3.5% dropout. REPORT [main p.5, Statistical Analysis](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) gives the same dropout-inclusive total, then separately says the trial was planned to end 30 days after inclusion of 1420 evaluable patients. REPORT [p.3 flow](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3) and p.5 population give 1979 randomized, 1508 completed and 1457 primary-available. PLAN [SAP p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84) directly establishes prospective preparation, approval on 11 January 2023 and precedence for all primary/secondary analyses.

**Rule / calculation / precision:** Focus D/route B concerns the population meaning of the accrual rule. If the maximum refers to all randomized patients, [1978.5,1979.5] versus [1599.5,1600.5] gives gap 378/1600=0.23625. This conditional diagnostic is reproduced, but a realized stopping-boundary breach is not established because “trial participants” is not explicitly mapped to randomization versus retention. “1420 evaluable” and “1420 including dropout” are different population qualifications rather than counts to subtract; rounding cannot identify their meaning.

**Inputs / missing definitions:** Available: repeated planned maxima, target descriptions, SAP precedence and realized population totals. Missing: definition of the population counted toward maximum 1600 and target 1420; operational recruitment-ending rule; any specific target-population mapping or further supplied amendment. These are needed to infer compliance with a numeric maximum, not to observe the unclear specification.

**Alternative / direct versus inferred:** Applying the maximum to 1508 retained participants could explain it. Approved SAP refinement could explain target meaning. These source-grounded possibilities are not asserted as realized rules. The supplied SAP approval and governance must not be described as absent.

**Classification:** PLAN protocols versus PLAN SAP gives P_P; PLAN protocol accrual rule versus REPORT realized/target populations gives P_R. REPORT p.5 itself repeats both dropout-inclusive and evaluable target meanings, adding S_W. Relationship type P_R; all relationships P_R, P_P, S_W; review domain protocol_report. This expands only All relationships from the ledger; highest precedence and domain remain unchanged.

**Evidence state:** reproduced. Determining fact: repeated protocol maximum/target language and dropout-inclusive SAP/report wording are found; no explicit population mapping reconciles all of them.

**Exact remaining human question:** Which recruitment or evaluable population counted toward maximum 1600 and target 1420, and which operational accrual rule determined termination at 1979 randomized/1508 completed/1457 primary-available?

## C003 — Outcome hierarchy

**Location found / source matched:** PLAN [original synopsis p.13](../../../joi240147supp1_prod_1738701765.28701.pdf#page=13), [original outcomes p.23](../../../joi240147supp1_prod_1738701765.28701.pdf#page=23), [data collection p.24](../../../joi240147supp1_prod_1738701765.28701.pdf#page=24), [final synopsis p.49](../../../joi240147supp1_prod_1738701765.28701.pdf#page=49), [final outcomes p.59](../../../joi240147supp1_prod_1738701765.28701.pdf#page=59) and [continuation p.60](../../../joi240147supp1_prod_1738701765.28701.pdf#page=60) reproduce the secondary-outcome list and associated collection context.

**Comparator matched:** PLAN [SAP title p.80](../../../joi240147supp1_prod_1738701765.28701.pdf#page=80), [approval p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84), [timing p.85](../../../joi240147supp1_prod_1738701765.28701.pdf#page=85), [multiplicity p.86](../../../joi240147supp1_prod_1738701765.28701.pdf#page=86), [outcomes p.88](../../../joi240147supp1_prod_1738701765.28701.pdf#page=88), [methods p.89](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89), [Table 3 p.100](../../../joi240147supp1_prod_1738701765.28701.pdf#page=100) and [Table 4 p.101](../../../joi240147supp1_prod_1738701765.28701.pdf#page=101) establish key/exploratory hierarchy and BH/FDR 5%. REPORT [main p.5 outcomes/statistics](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5), [p.6 Figure 2/narrative](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=6), [eTable 4 p.17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17), [eTable 5 p.18](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18) and [eTable 6 p.19](../../../joi240147supp2_prod_1738701765.29201.pdf#page=19) implement that hierarchy. PLAN [p.92](../../../joi240147supp1_prod_1738701765.28701.pdf#page=92) and REPORT [results p.10](../../../joi240147supp2_prod_1738701765.29201.pdf#page=10) explicitly defer long-term follow-up; every registered contextual location is found.

**Rule / reproduced comparison / precision:** Route A category 5 compares matched outcome status. Thirty-day mortality and major respiratory complications change from protocol secondary to SAP/report key secondary. Hospital LOS, ICU LOS, days alive outside ICU, mechanical-ventilation time, ventilator-free days, postdischarge pneumonia, intervention hypoxemia and SSI change from secondary to exploratory secondary. Protocol number of reintubations is matched to the SAP exploratory intubation/reintubation registrations; this preserves its status comparison without assuming those two counts have identical definitions or alleging an omitted key result. This is one hierarchy pattern. Numerical rounding is inapplicable to categorical status. Six/twelve-month EQ-5D-5L/GOSE and twelve-month mortality are contextual deferred outcomes, not additional qualifying absent primary/key analyses.

**Inputs / missing definitions:** All identities, status headings, windows and multiplicity rules are available. Missing: an itemized explanation of how the approved SAP refines each protocol status for extraction; no unprinted outcome result is inferred.

**Alternative / direct versus inferred:** Direct: protocol secondary labels and later key/exploratory labels. The SAP is prospectively approved and explicitly governs analyses; intentional hierarchy refinement is supported. That context does not remove the observed route-A status change, nor establish an unapproved change.

**Classification:** PLAN original/final protocols versus PLAN SAP gives P_P; protocol versus REPORT status gives P_R. Main and results supplement agree and add no S comparison. Relationship type P_R; all relationships P_R, P_P; review domain protocol_report; roles and domain confirmed.

**Evidence state:** reproduced. Determining fact: each matched protocol secondary-outcome family has the later key/exploratory status stated above.

**Exact remaining human question:** How should the prospectively approved SAP hierarchy refinement be documented item by item for protocol status, report status and nominal-versus-FDR interpretation in extraction?

## C004 — Primary covariate specification

**Location found / source matched:** PLAN [original statistics p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26) and [final statistics p.62](../../../joi240147supp1_prod_1738701765.28701.pdf#page=62) both specify primary logistic adjustment for age, sex, centre, intubation at randomization and known pneumonia on admission under treatment. PLAN [change log p.78](../../../joi240147supp1_prod_1738701765.28701.pdf#page=78), [p.79](../../../joi240147supp1_prod_1738701765.28701.pdf#page=79), [SAP title p.80](../../../joi240147supp1_prod_1738701765.28701.pdf#page=80), [approval p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84), [primary methods p.88](../../../joi240147supp1_prod_1738701765.28701.pdf#page=88) and [related methods p.89](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89) are found and read; the SAP explicitly governs all primary/secondary analyses.

**Comparator matched:** REPORT [main p.5, Statistical Analysis](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) specifies stratification-variable adjustment, additional age/sex/ISS/first-GCS adjustment, GEE site clustering and IPW. REPORT [results eMethods p.11](../../../joi240147supp2_prod_1738701765.29201.pdf#page=11) and [p.12](../../../joi240147supp2_prod_1738701765.29201.pdf#page=12) give population/weighting context. REPORT [eTable 4 p.17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17) gives primary OR 1.01(0.75–1.37), additional OR 0.98(0.68–1.41) and smoking model OR 1.05(0.73–1.49); [eTable 8 p.22](../../../joi240147supp2_prod_1738701765.29201.pdf#page=22) gives the three per-protocol model columns. No described reported primary model contains the protocol pneumonia covariate.

**Rule / reproduced comparison / precision:** Route A category 5: a specifically planned primary covariate model is replaced/not reported. Item matching retains centre/intubation, moves age/sex to additional adjustment, and omits known pneumonia on admission under treatment from the described primary model set. ISS/GCS/smoking are separate covariates. Categorical model-set comparison has no display-precision interval; the cited ORs are result anchors, not numerical predictions from covariate names. No model is reconstructed from aggregate counts.

**Inputs / missing definitions:** Available: both planned covariate lists, governing SAP model, report methods and all primary-model columns. Missing: itemized model-replacement record beyond the approved governing SAP, or originally specified pneumonia-adjusted output. Participant-level covariates/model coefficients are absent and prevent numerical model re-estimation, which is not needed for this specification comparison.

**Alternative / direct versus inferred:** Direct: differing named covariates and no displayed original-model output. The approved prospective SAP may intentionally replace the protocol model; approval/precedence are supplied facts. This is not a statement that replacement was unauthorized. Missingness/population branches were screened independently; categorical key-secondary methods belong to C007.

**Classification:** PLAN protocol versus PLAN SAP P_P; PLAN protocol versus REPORT primary models P_R; no report/report conflict because report implements SAP. Relationship type P_R; all relationships P_R, P_P; review domain protocol_report; confirmed.

**Evidence state:** reproduced. Determining fact: the pneumonia-under-treatment covariate appears in both protocol primary-model specifications and in none of the described reported primary-model sets.

**Exact remaining human question:** Does the approved governing SAP constitute replacement of the protocol's specified pneumonia-adjusted primary model, and is the original model result or an itemized replacement explanation supplied?

## C005 — Planned primary hypoxemia subgroup

**Location found / source matched:** PLAN [original subgroup paragraph p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26), [final paragraph p.62](../../../joi240147supp1_prod_1738701765.28701.pdf#page=62), [SAP approval p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84) and [SAP p.89 primary-subgroup bullets](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89) are found. The SAP explicitly assigns seven subgroup families to the primary outcome, including intervention SpO2<90%.

**Comparator matched:** REPORT [main p.5 subgroup methods](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) and [complete Figure 4 p.8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) give six families: initial intubation, ICU, TBI, lung disease, inclusion site and ISS. REPORT entire eTable 7 [p.20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) and [p.21](../../../joi240147supp2_prod_1738701765.29201.pdf#page=21) give those same families. Other result tables were read at [p.17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17), [p.18](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18), [p.19](../../../joi240147supp2_prod_1738701765.29201.pdf#page=19), [p.22](../../../joi240147supp2_prod_1738701765.29201.pdf#page=22), [p.23](../../../joi240147supp2_prod_1738701765.29201.pdf#page=23), [p.24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24) and [p.25](../../../joi240147supp2_prod_1738701765.29201.pdf#page=25). Hypoxemia 44/737 versus 28/737 in eTable 5 is an incidence endpoint, not primary-composite effect stratified by hypoxemia. Full-source text search found no additional primary hypoxemia subgroup output.

**Rule / reproduced comparison / precision:** Route A category 5. Match every SAP subgroup family to report display headings; six have counterparts and intervention hypoxemia has none. A planned primary analysis is not supplied by a differently targeted exploratory endpoint. Half-unit arithmetic is inapplicable to presence/absence of a specified analysis; no subgroup number is imputed.

**Inputs / missing definitions:** The explicit planned target and complete reported result displays are available. Missing: hypoxemia-stratified primary-composite treatment effects/interaction or a documented removal/deferment of this analysis. Participant-level hypoxemia/primary cross-tabulation is absent and no effect can be reconstructed.

**Alternative / direct versus inferred:** Direct: planned primary-target bullet and absence of its counterpart from complete supplied displays. Alternative: intentional removal, deferral or reporting elsewhere outside the supplied package. Such a disposition is not established by these sources. No omitted-effect magnitude is inferred.

**Classification:** PLAN SAP versus REPORT main/supplement yields P_R only; the protocols corroborate the subgroup's prior presence, and agreeing report displays add no S relationship. Relationship type P_R; all relationships P_R; review domain protocol_report; confirmed.

**Evidence state:** reproduced. Determining fact: the SAP's explicit primary hypoxemia subgroup has no matched report output, while the printed hypoxemia incidence is a different analysis target.

**Exact remaining human question:** Where is the prespecified primary-composite subgroup analysis by intervention SpO2<90%, or its documented removal/deferment?

## C006 — Intubation clock

**Location found / source matched:** PLAN [original p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26), [final p.62](../../../joi240147supp1_prod_1738701765.28701.pdf#page=62) and [SAP p.89](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89) specify initially intubated within one hour of accident/after trauma. PLAN [p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84) confirms approved SAP precedence, but that SAP retains the trauma-based criterion.

**Comparator matched:** REPORT [main p.5 subgroup paragraph](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) names initial intubation; REPORT [Figure 4 p.8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) and [eTable 7 p.20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) explicitly say intubated at randomization. No: 56/558 versus 50/543, OR 1.12(0.75–1.67); Yes: 62/175 versus 71/181, OR 0.90(0.57–1.41); interaction P=.48 in Figure 4. REPORT [eTable 3 p.16](../../../joi240147supp2_prod_1738701765.29201.pdf#page=16) gives trauma-to-randomization medians(IQR) 54(35–79)/52(33–78) minutes. REPORT [eTable 7 continuation p.21](../../../joi240147supp2_prod_1738701765.29201.pdf#page=21) provides no alternative intubation clock.

**Rule / reproduced comparison / precision:** Focus D/route B: compare membership at a fixed trauma-origin one-hour window with membership at randomization. These are different clock definitions without an equivalence mapping. Rounding is inapplicable to the predicates. Median/IQR time summaries corroborate distinct time origins; they do not prove that any particular participant changes subgroup membership.

**Inputs / missing definitions:** Available: both explicit predicates and associated reported effects. Missing: operational intubation time/window used for subgroup coding, patient-level cross-classification between predicates, or a clock-specific amendment. These missing inputs prevent a realized membership-difference count.

**Alternative / direct versus inferred:** Status may coincide across clocks for all participants, or the display may abbreviate the fixed trauma-clock definition. Neither is asserted. Direct observation is the differing clock statement; an individual subgroup reassignment is not inferred. Lung-disease membership is outside this candidate's included scope.

**Classification:** PLAN protocols/SAP versus REPORT intubation label yields P_R only; protocols and SAP agree on the trauma clock, reports agree on randomization label. Relationship type P_R; all relationships P_R; review domain protocol_report; confirmed.

**Evidence state:** reproduced. Determining fact: governing SAP says within one hour after trauma whereas both report subgroup displays say at randomization, without a supplied mapping.

**Exact remaining human question:** Was subgroup membership determined by intubation within one hour after trauma or intubation status at randomization, and how do the printed subgroup ORs map to the SAP criterion?

## C007 — Categorical key-secondary tests

**Location found / source matched:** PLAN [original outcomes p.23](../../../joi240147supp1_prod_1738701765.28701.pdf#page=23) and [final outcomes p.59](../../../joi240147supp1_prod_1738701765.28701.pdf#page=59) explicitly list 30-day mortality and major respiratory complications as secondary outcomes. PLAN [original methods p.26](../../../joi240147supp1_prod_1738701765.28701.pdf#page=26) and [final methods p.62](../../../joi240147supp1_prod_1738701765.28701.pdf#page=62) assign Fisher's exact/chi-square tests to categorical secondary data. PLAN [change log p.78](../../../joi240147supp1_prod_1738701765.28701.pdf#page=78), [p.79](../../../joi240147supp1_prod_1738701765.28701.pdf#page=79), [SAP title p.80](../../../joi240147supp1_prod_1738701765.28701.pdf#page=80), [approval p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84), [primary/key outcome p.88](../../../joi240147supp1_prod_1738701765.28701.pdf#page=88) and [key-secondary methods p.89](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89) are matched; key outcomes receive the primary logistic/GEE/IPW framework under the approved governing SAP.

**Comparator matched:** REPORT [main p.5 methods](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5), [Figure 2/narrative p.6](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=6) and [eTable 4 p.17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17) implement logistic/GEE/IPW. Death first/additional/smoking ORs are 1.28(0.85–1.92), P=.23; 1.37(0.80–2.38), P=.25; 1.37(0.80–2.33), P=.26. Respiratory ORs are 0.84(0.59–1.19), P=.33; 0.84(0.57–1.23), P=.38; 0.90(0.61–1.32), P=.58. None is identified as the originally planned categorical test result.

**Rule / reproduced comparison / precision:** Route A category 5: explicitly named categorical secondary analyses are replaced/not reported for the two subsequently key outcomes. Match outcome and categorical status before method comparison. The protocol's continuous competing-risk sentence is not compared to binary logistic outcomes. No crude or preferred test is recomputed; numerical rounding cannot reconcile named method families.

**Inputs / missing definitions:** All outcome names, method assignments and reported model outputs are available. Missing: categorical-test output under the original protocol or an itemized replacement explanation beyond the approved SAP. Model covariance and raw counts at the modeled weighting level are unnecessary for the method-name comparison and are not supplied.

**Alternative / direct versus inferred:** Prospective SAP approval may intentionally supersede generic protocol categorical tests. This is supported by explicit all-analysis precedence; no unapproved change is inferred. Direct facts are the original assignment and reported model implementation. This rule is separate from C004's primary covariate model and C003's status hierarchy.

**Classification:** PLAN protocols versus PLAN SAP gives P_P; protocols versus REPORT key-secondary implementation gives P_R. Reports agree. Relationship type P_R; all relationships P_R, P_P; review domain protocol_report; confirmed.

**Evidence state:** reproduced. Determining fact: planned categorical tests explicitly apply to named secondary death/respiratory outcomes while supplied results identify model-based analyses and no original test outputs.

**Exact remaining human question:** Does SAP approval establish replacement of the originally planned Fisher/chi-square comparisons for 30-day death and respiratory outcomes, or are those planned test results supplied?

## C008 — SSI nominal interval/test readings

**Location found / source matched:** REPORT [main p.6, Figure 2 SSI row](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=6) prints RD −3.04 percentage points, 95% CI −6.87 to 0.79 and OR 0.50(0.25–0.99), all visually confirmed. REPORT [main p.5 significance paragraph](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) distinguishes nominal 95% intervals/5% primary/key inference from exploratory FDR 5% testing. PLAN [SAP p.86](../../../joi240147supp1_prod_1738701765.28701.pdf#page=86) corroborates the nominal confidence/test and exploratory BH framework; it does not conflict with the report.

**Comparator matched:** REPORT [results p.18, eTable 5 SSI row](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18) gives first OR 0.50(0.25–0.99), P=.05; additionally adjusted OR 0.49(0.26–0.93), P=.03; smoking-adjusted OR 0.51(0.27–0.96), P=.04. The counts are 23/736 versus 32/724 in both displays. Supplement footnote and main narrative say no exploratory outcomes were significant after multiplicity adjustment; those statements are coherent with the stated FDR framework.

**Rule / reproduced comparison / precision:** Route A category 1 compares nominal interval-versus-test readings, preserving any different-analysis explanation. RD limits remain respectively below/above zero: [−6.875,−6.865] and [0.785,0.795]. OR upper-limit ranges [0.985,0.995], [0.925,0.935] and [0.955,0.965] remain below one. Adjusted P=.03/.04 give intervals [0.025,0.035]/[0.035,0.045], both below .05. The first P=.05 range [0.045,0.055] straddles .05 and is unnecessary to reproduce this candidate. Relative-gap rounding exclusion does not apply to category 1. No assertion of an FDR discovery or common variance method is made.

**Inputs / missing definitions:** Available: nominal 95% intervals, explicit model adjustment, P values and multiplicity statements. Missing: RD estimand, standardization/weighting and confidence-interval construction, and the precise test paired with the RD. Those inputs are needed to determine why distinct analyses might legitimately give these nominal readings.

**Alternative / direct versus inferred:** Direct: printed RD includes zero while OR intervals and adjusted nominal P values exclude their null. Alternative: different estimands, modeled contrasts, variances or analysis sets. The OR is explicitly stratification-adjusted; RD method is not defined in the caption. This alternative does not remove a category-1 candidate. FDR explains report-level exploratory decisions separately and does not map the RD to a nominal test.

**Classification:** Within main Figure 2 RD/OR comparison gives S_W; main RD versus supplementary OR/test results gives S_C. PLAN p.86 only corroborates inferential context and creates no P_R. Relationship type S_C; all relationships S_C, S_W; review domain statistical_results; confirmed.

**Evidence state:** reproduced. Determining fact: the source RD's upper limit stays positive while source OR upper limits and adjusted nominal P intervals stay on the nominal significant side, even after allowed display intervals.

**Exact remaining human question:** Which RD/95% CI procedure produced −3.04(−6.87 to 0.79), which nominal test maps to it, and how should its null-inclusive reading be understood alongside the printed OR intervals/P=.03/.04?

## C009 — SSI event predicate

**Location found / source matched:** PLAN [SAP p.101, Table 4 SSI row](../../../joi240147supp1_prod_1738701765.28701.pdf#page=101) requires at least one of purulent drainage; positive microbiologic testing from surgical site/wound and signs of infection; surgeon diagnosis. PLAN [p.84](../../../joi240147supp1_prod_1738701765.28701.pdf#page=84) establishes prospective SAP approval and precedence.

**Comparator matched:** REPORT [results p.9, section 3.3.2 SSI row](../../../joi240147supp2_prod_1738701765.29201.pdf#page=9) lists at least one of purulent drainage; positive microbiologic testing; deliberate opening by surgeon AND signs; surgeon diagnosis. Its introductory text explicitly calls these further elaborations. REPORT [results p.18, SSI results](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18) and [main p.6, Figure 2](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=6) attach 23/736 versus 32/724 and OR 0.50(0.25–0.99) to SSI within 30 days. Every cited location is found; window agrees.

**Rule / reproduced comparison / precision:** Focus D/route B: compare event-classification logical predicates. Drainage and diagnosis paths match. SAP positivity requires infection signs; the report positivity bullet does not. Report deliberate opening plus signs is an additional pathway absent from the SAP list. This changes the printed criterion a data extractor should use. Half-unit interval checks are inapplicable to Boolean predicates; no realized case-count difference is computed.

**Inputs / missing definitions:** Available: complete printed lists, shared window and linked events/results. Missing: applied operational item-level SSI classification; whether microbiology-positive cases had to have signs; whether report-only opening cases also satisfied the SAP list; patient-level criteria needed for realized reclassification counts.

**Alternative / direct versus inferred:** The report explicitly offers fuller elaboration of a shortened dictionary, supporting an intended operational expansion. It does not establish that every report-only path satisfies the SAP conjunction. Direct observation is differing written paths; realized event reassignment is not inferred. This is independent of C008's nominal uncertainty reading.

**Classification:** PLAN SAP predicate versus REPORT supplementary predicate gives P_R; main/supplement result counts agree and provide anchors only. Relationship type P_R; all relationships P_R; review domain protocol_report; confirmed.

**Evidence state:** reproduced. Determining fact: positivity-with-signs in SAP and independent positivity/deliberate-opening paths in report remain different when read directly.

**Exact remaining human question:** Which item-level SSI predicate classified the events, could microbiologic positivity alone qualify, and how were the report's opening-plus-signs cases mapped to the SAP dictionary?

## C010 — ICU population/window mapping

**Location found / source matched:** REPORT [results p.18, eTable 5 ICU admission](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18) prints restrictive 374/738(50.7%) and liberal 359/736(48.8%). REPORT [results p.20, eTable 7 ICU rows](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) and [main p.8, Figure 4 ICU rows](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) print No 42/458 versus 50/481, OR 0.98(0.64–1.49), and Yes 74/271 versus 68/238, OR 0.96(0.63–1.49). All duplicated subgroup locations match visually.

**Comparator/context matched:** REPORT [main p.4, destination after resuscitation](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=4) gives immediate ICU 276/741 versus 242/739. REPORT [main p.5, population/subgroups](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5) gives allocation cohorts 750/758 and primary-available 733/724 and unqualified ICU subgroup name. REPORT [results p.9](../../../joi240147supp2_prod_1738701765.29201.pdf#page=9) and [p.10](../../../joi240147supp2_prod_1738701765.29201.pdf#page=10) outcome elaborations define ICU day-counting but do not distinguish an admission window for subgroup membership. PLAN [SAP p.89](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89) similarly names ICU admission, corroborating only the unqualified name.

**Rule / calculation / precision:** Focus A/C and route B. If both displays mean the same ICU membership in a common allocation universe, admissions among subgroup-classified participants must be at least known admissions plus classified total minus allocation total. Restrictive point lower bound 374+271+458−750=353 versus Yes 271; liberal 359+238+481−758=320 versus Yes 238. Conservative half-unit lower bounds: 373.5+270.5+457.5−750.5=351 versus Yes upper 271.5; and 358.5+237.5+480.5−758.5=318 versus upper 238.5. Both gaps are 79.5; relative gaps 79.5/271=0.293358 and 79.5/238=0.334034. These allow every unclassified participant to be admitted; missingness alone cannot reconcile identical membership. Immediate-destination counts are contextual alternatives, not asserted numerically equal to subgroup denominators.

**Inputs / missing definitions:** Available: both sets of counts, full allocation universes, all duplicated subgroup outputs and immediate-destination comparator. Missing: ICU subgroup admission window/eligibility rule, linkage between admission outcome and subgroup, and participant-level cross-tabulation. Such inputs could explain the different populations.

**Alternative / direct versus inferred:** Direct: larger ICU admission counts cannot map into the subgroup Yes counts under the common-membership assumption even with maximal missing classification. Alternative: subgroup means immediate destination after resuscitation, while outcome means any later admission; another timing/eligibility restriction could also explain it. The source does not explicitly define the latter as a 30-day ICU-admission window, so no exact unprinted window is assigned. No participant reassignment is inferred.

**Classification:** REPORT eTable 5 versus eTable 7 gives S_W; eTable 5 versus main Figure 4 gives S_C. PLAN SAP is corroboration only, so no P_R. Relationship type S_C; all relationships S_C, S_W; review domain statistical_results; confirmed. Main p.4 is a distinctly labeled immediate-destination context rather than a separate conflicting copy.

**Evidence state:** reproduced. Determining fact: both source-grounded common-set bounds leave minimum gaps 79.5, and no printed window maps the named populations.

**Exact remaining human question:** Does the primary subgroup's ICU admission mean immediate destination, any admission during the hospital stay or another window, and which membership rule generated 271/238 versus the reported 374/359 admissions?

## C011 — Liberal AIS<3 count/percentage and repeated copy

**Location found / source matched:** REPORT [results p.20, eTable 7 AIS<3 liberal cell](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) directly and visually reads 48/473(9.2%). REPORT [p.21, eTable 7 footnote](../../../joi240147supp2_prod_1738701765.29201.pdf#page=21) identifies selected head AIS codes; it does not provide a different percentage denominator.

**Comparator matched:** REPORT [main p.8, Figure 4 AIS<3 liberal cell](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) directly and visually reads 48/473(10.1%). Count pair and subgroup identity agree across reports. The 675-versus-724 AIS completeness observation is outside this included candidate.

**Rule / calculation / precision:** Route A category 3. Count-derived point percentage is 10.147992%; conservative recomputed interval [10.031679,10.264550]% versus printed supplement [9.15,9.25]% gives gap 0.781679 percentage points and relative 0.0849651. Printed-copy intervals [9.15,9.25]% versus [10.05,10.15]% give gap 0.8/reference 10.1=0.0792079. Both exceed 0.05. Main's own count/percentage interval overlaps and is not a within-main arithmetic discrepancy.

**Inputs / missing definitions:** All printed numerator, denominator and percentage copies are available. Missing: denominator used to generate 9.2%, or identification of which component belongs with the cell. Participant-level AIS availability is not needed for this pair calculation and does not reconcile its printed percentage.

**Alternative / direct versus inferred:** Another population denominator could yield 9.2% (approximately 522 for numerator 48), but no such denominator is printed for this cell. This is a diagnostic possibility, not a replacement value. No complete-AIS-ascertainment claim or 49-patient effect is inferred.

**Classification:** Supplement pair gives S_W; main/supplement percentage copies give S_C. Both documents are REPORT. Relationship type S_C; all relationships S_C, S_W; review domain statistical_results; confirmed.

**Evidence state:** reproduced. Determining fact: the supplement visibly prints 9.2% beside 48/473, whose recomputed interval and main counterpart each remain beyond 0.05 relative gap.

**Exact remaining human question:** Which percentage and denominator should accompany the liberal AIS<3 primary-outcome subgroup result, and what produced the printed 9.2%?

## C012 — Bern receiving-center row, both arms

**Location found / source matched:** REPORT [results p.14, eTable 1 Receiving trauma center, University Hospital Bern row](../../../joi240147supp2_prod_1738701765.29201.pdf#page=14) visibly prints restrictive 50/750(7.2%) and liberal 47/758(6.7%). These are receiving-center cells, distinct from the earlier enrollment-location Bern row 25/750(3.3%) and 26/758(3.4%).

**Comparator matched:** Same REPORT row's printed numerator/denominator pairs and the N=750/N=758 column headers. Receiving-center numerators total 750/758, supporting the printed allocation denominators. Both affected arm cells are rechecked separately.

**Rule / calculation / precision:** Route A category 3. Restrictive point 6.666667%, recomputed [6.595603,6.737825]% versus printed [7.15,7.25]%, gap 0.412175, relative 0.0572465. Liberal point 6.200528%, recomputed [6.130521,6.270627]% versus printed [6.65,6.75]%, gap 0.379373, relative 0.0566228. Both exceed 0.05 after half-unit allowances. Other receiving-center rows' small discrepancies are not added to this registered pattern.

**Inputs / missing definitions:** Complete pairs, headings and row identity are available. Missing: another undisclosed numerator/denominator or population generating 7.2%/6.7%, or confirmation of intended cells. No raw data are needed to reproduce both same-display mismatches.

**Alternative / direct versus inferred:** Printed percentage may use another denominator or one component may belong elsewhere; no row-specific alternative denominator is supplied. Direct observations are both printed pairs and computed interval gaps. A production mechanism is not inferred.

**Classification:** REPORT pair versus REPORT percentage within eTable 1; relationship type S_W; all relationships S_W; review domain statistical_results; confirmed. This within-display baseline arithmetic falls under focus A rather than a peripheral baseline-copy comparison.

**Evidence state:** reproduced. Determining fact: both Bern receiving-center arm cells retain relative gaps greater than 0.05.

**Exact remaining human question:** Which receiving-center numerator, denominator and percentage should be extracted for Bern in each arm, and what generated 7.2% and 6.7%?

## C013 — Liberal walk-in row

**Location found / source matched:** REPORT [results p.15, eTable 2 Type of transport to trauma center, Walk-in liberal cell](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15) visibly reads 4/743(5.3%).

**Comparator matched:** Same REPORT cell's numerator/denominator and the no./total no.(%) heading. Liberal transport-category numerators sum to 743, consistent with the printed denominator; the adjacent restrictive cell is 9/747(1.2%) and is not an affected occurrence.

**Rule / calculation / precision:** Route A category 3. Point recomputation 0.538358%; interval [0.470746,0.606061]% versus printed [5.25,5.35]% gives gap 4.643939 percentage points, relative 0.876215. This exceeds 0.05 by the prescribed conservative interval check.

**Inputs / missing definitions:** Printed pair and row/column labels are available. Missing: intended component if 5.3% uses a different numerator or denominator, or a value placed in another cell. No method or raw-data assumption is needed for the arithmetic.

**Alternative / direct versus inferred:** Decimal placement or another cell/population may explain the display; these remain possible mechanisms only. Direct observation is 4/743 next to 5.3%, not a chosen replacement.

**Classification:** REPORT within eTable 2; relationship type S_W; all relationships S_W; review domain statistical_results; confirmed. No cross-document comparator is needed.

**Evidence state:** reproduced. Determining fact: direct source pair produces at most 0.606061% under rounding, below printed percentage interval's lower limit 5.25%.

**Exact remaining human question:** Which liberal walk-in count, denominator and percentage are intended for extraction?

## C014 — Liberal vascular-surgery row

**Location found / source matched:** REPORT [results p.15, eTable 2 Surgery in trauma resuscitation room, Vascular surgery liberal cell](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15) visibly reads 0/747(1.1%).

**Comparator matched:** Same REPORT cell's numerator/denominator and no./total no.(%) heading. Other liberal surgery rows use denominator 747, and restrictive vascular surgery is 1/744(0.1%); no second affected arm cell is registered.

**Rule / calculation / precision:** Route A category 3. Zero-numerator point percentage is 0. Permitting integer half-unit interval [0,0.5] and denominator [746.5,747.5] gives [0,0.066979]% versus printed [1.05,1.15]%. Gap 0.983021 percentage points, relative 0.893655. Count lower bound is truncated at zero; positive percentage remains far beyond 0.05 relative gap.

**Inputs / missing definitions:** Complete printed pair and heading are available. Missing: whether intended numerator is positive, whether percentage belongs to a different row, or an alternate disclosed population. No event count is inferred from the percentage.

**Alternative / direct versus inferred:** A displaced count or percentage could explain the presentation. The source supplies no mechanism. Direct observation is zero numerator adjacent to positive prevalence and the conservative interval gap.

**Classification:** REPORT within eTable 2; relationship type S_W; all relationships S_W; review domain statistical_results; confirmed. This is separate from C013 because source cells do not establish a shared production cause.

**Evidence state:** reproduced. Determining fact: count-derived maximum 0.066979% remains below printed interval lower limit 1.05%.

**Exact remaining human question:** Was any liberal-group vascular surgery recorded, and which numerator, denominator and percentage should be extracted from this cell?

## C015 — Exclusion denominator pattern, all four cells

**Location found / source matched:** REPORT [results p.24, eTable 10 both exclusion rows and both allocation columns](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24) visibly gives exclusion after randomization 55/750(45%) and 67/758(55%), row N=130; secondary exclusion 174/750(51%) and 165/758(49%), row N=341. Headers are restrictive N=750 and liberal N=758. All four affected cells are rechecked.

**Comparator matched:** Same REPORT displayed numerator/denominator pairs versus their adjacent percentages. Title calls the table a distribution among postrandomization excluded patients. Footnote states two secondary-exclusion patients lack randomized intervention data, explaining 174+165+2=341. It supplies no convention that adjacent percentages use denominators different from the printed slash pairs.

**Rule / calculation / precision:** Route A category 3. Conservative intervals and gaps are:

| Cell | Recomputed interval, % | Printed interval, % | Gap, percentage points | Relative gap |
|---|---|---|---|---|
| After randomization, restrictive 55/750(45) | [7.261825,7.404937] | [44.5,45.5] | 37.095063 | 0.824335 |
| After randomization, liberal 67/758(55) | [8.767304,8.910891] | [54.5,55.5] | 45.589109 | 0.828893 |
| Secondary, restrictive 174/750(51) | [23.117921,23.282188] | [50.5,51.5] | 27.217812 | 0.533683 |
| Secondary, liberal 165/758(49) | [21.687541,21.848185] | [48.5,49.5] | 26.651815 | 0.543915 |

All exceed 0.05. Distribution percentages using 55/(55+67)=45.081967%, 67/122=54.918033%, 174/(174+165)=51.327434% and 165/339=48.672566% match the integer percentages, supporting the alternate quantity suggested by the title. The different explicit slash denominators remain the observable mismatch. N=130 versus 122 is not a separate included basis: sum interval [121,123] versus total [129.5,130.5] has gap 6.5/130=0.05 exactly. The two missing secondary allocations reconcile its N=341 and are context only.

**Inputs / missing definitions:** All four pairs, integer percentages, title and footnote are available. Missing: explicit denominator convention separating allocation-group prevalence from distribution among excluded participants; participant-level exclusion allocation details needed to infer any alternate counts. No such alternate count is assigned.

**Alternative / direct versus inferred:** Title and cross-arm sums support intended distribution percentages while slash pairs may show allocation denominators. This plausible dual-quantity display does not make a single count/denominator/percentage pair numerically reconcile. A production mechanism or replacement is not inferred.

**Classification:** REPORT four paired cells within eTable 10; relationship type S_W; all relationships S_W; review domain statistical_results; confirmed. No PLAN or cross-report conflict is needed.

**Evidence state:** reproduced. Determining fact: each of the four printed pairs retains a relative gap above 0.05, although percentages can be reproduced from different cross-arm denominators.

**Exact remaining human question:** Do the percentages describe allocation-group prevalence or allocation distribution among excluded participants, and which denominator convention should accompany each count for extraction?

## Bounded factual and prose handoff

No source value or page anchor required a transcription change; all registered readings remain source-matched. Suggested coordinator-only updates are factual clarifications, not final replacements of source values:

- C002: add S_W to All relationships because main p.5 itself contains both dropout-inclusive and evaluable target descriptions. Keep P_R primary and protocol_report domain. Preserve the qualification that numeric maximum comparison depends on the recruitment population; do not infer a stopping-boundary breach.
- C003: preserve SAP prospective approval and explicit all-analysis precedence. Distinguish status comparison for intubation/reintubation registrations from an assertion that every exploratory registration requires a separate reported result. Do not conflate protocol number of reintubations with SAP total intubations as identical count definitions.
- C004: source-accurate covariate phrase is known pneumonia on admission under treatment. The registered shorthand admission pneumonia should be expanded to this meaning. Keep the candidate's basis solely primary covariates, with separate C007 secondary methods and independently screened missingness/population branches.
- C006: state that clock definitions differ; time summaries do not prove discordant realized membership. Preserve intubation-only scope and supplied governing SAP.
- C008: state nominal RD-versus-OR/test readings; retain distinct-analysis alternatives and separately coherent FDR decision. Printed first-model P=.05 alone does not settle significance because its display interval crosses .05.
- C010: retain both main and supplementary subgroup locations, immediate-destination context and all available count inputs. Do not assign a 30-day ICU-admission window that the source does not specify for this row. SAP corroboration does not create P_R.
- C011: keep within-cell percentage and cross-report percentage comparison as the bases; do not add conditional complete-AIS-partition assumptions.
- C015: retain the title-supported distribution interpretation and explicit-denominator discrepancy together, without adding the screened N=130 versus122 observation.

## Unresolved items and complete scope

All 15 IDs and every registered affected occurrence were rechecked. No supplied PDF page was unavailable, no disputed numeric cell remained unreadable, and no tooling limit prevented exact-source confirmation. Remaining human questions are item-specific and printed above: intended population labels/targets; itemized SAP hierarchy/model replacement meaning; unavailable primary hypoxemia subgroup disposition; intubation and ICU membership mappings; SSI operational predicate and RD/test procedure; intended percentage denominators for AIS, Bern, walk-in, vascular surgery and exclusions. Missing participant-level cross-tabulations, model coefficients and RD definitions limit explanatory reconstruction, not observation of the supplied statements.

Counts: 15 covered stable IDs; 15 reproduced; 0 reproduced_after_transcription_correction; 0 not_reproduced; 1 All-relationships expansion; 0 role/primary-type/domain replacements. Final artifact: `verification/evidence_recheck.md`. Runtime ID: `/root/evidence_recheck`.
