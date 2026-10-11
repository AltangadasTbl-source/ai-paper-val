# Numeric consistency checker — Workflow 1.6.2

Scope completed: DOC-001 REPORT pp.1–10, DOC-002 PLAN pp.1–25 and DOC-003 REPORT pp.1–9; all 44 mapped pages and **150 N relationships** in [numeric relationship inventory](../relationships/numeric_relationship_inventory.md). Count and percentage arithmetic was checked cell by cell, including all 51 baseline Table 1 count-percentage cells. Flow, randomized/treated/analyzed/followed-up populations, complete row/column partitions, vascular-event counts, outcome denominators, repeated numeric copies, risk trajectories and effect-measure identity were checked. Result-relevant means, medians, SDs/IQRs, scales and units are retained. Statistical test and plan/report checks have their parallel specialist inventories; the numerical interval/P observation below is emitted because route A requires registration whenever observed.

Source authority: supplied PDFs. The current maps and reusable source-linked layout text were locators; fresh direct Poppler pdftotext -layout exact-page readings confirmed main pp.4–8, protocol pp.16–19 and supplement pp.5–9. No source/reused asset changed, no legacy candidate/report conclusions read and no external evidence used. No OCR or rendering required. Device: CPU.

## Findings

### F-NUM-001

**Title:** Primary-analysis participant counts differ between Figure 1 and the results/primary-outcome table.

**Relationship IDs:** N001, N004, N005, N006 and the Table 2 all-or-none relationship.

**Compared locations and document roles:**
- REPORT [main article PDF p.4, Results opening paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4): 4800 patients were enrolled prospectively and included in the primary analysis, with Figure 1 cited.
- REPORT [main article PDF p.5, Figure 1 lower analysis boxes](../../../jama_wang_2018_oi_180070.pdf#page=5): intervention 2003 patients and control 1977 patients included in primary analysis. The immediately preceding twelve-month follow-up boxes show 397 and 423 patients lost, respectively.
- REPORT [main article PDF p.7, Table 2 all-or-none row](../../../jama_wang_2018_oi_180070.pdf#page=7): 1290/2400 and 1147/2400, respectively, for a co-primary outcome.
- REPORT [main article PDF p.1, abstract Results](../../../jama_wang_2018_oi_180070.pdf#page=1) and p.4 later Results paragraph: 3980 patients completed twelve-month follow-up; arm completion 2003 and 1977.

**Printed inputs:** 4800 in the primary analysis in p.4; Figure 1 primary analysis I=2003 and C=1977; randomized/received I=C=2400; losses 397/423; co-primary Table 2 denominators I=C=2400.

**Rule and calculation:** A specific primary-analysis population must have reconcilable counts across its report locations after matching analysis status. Figure 1 gives 2003+1977=3980; p.4 gives 4800. These same Figure 1 values also equal 2400−397 and 2400−423 and the p.4 twelve-month completers, while Table 2 uses all 2400 participants per arm. For display precision, input half-unit sum interval is [3979,3981]; p.4 reference interval is [4799.5,4800.5]. The interval gap is 818.5 participants; relative discrepancy 818.5/4800=0.1705208 (>0.05). Arm discrepancies similarly have interval gaps 396/2400=0.165 and 422/2400=0.1758333. Counts therefore remain discrepant under the required display rule.

**Focus area:** A (counts and analysis denominators).

**Proposed review domain:** report_internal_inconsistency.

**Provisional relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Number of participants included in the co-primary composite/all-or-none analyses, and the analysis-population size extracted from Figure 1.

**Why context does not resolve it:** B1: this concerns the primary-analysis population rather than a peripheral per-time-point contributor count. B2: the follow-up labels identify where the smaller numbers arose, but both p.4 and the figure explicitly attribute different populations to the primary analysis, and Table 2 supplies the larger denominator; a reader cannot take both analysis labels literally. B3: extracting the figure's primary-analysis boxes changes the reported primary-analysis total from 4800 to 3980 and changes its interpretation as a follow-up-completer analysis.

**Source-grounded alternatives and missing definition:** Figure 1 may intend twelve-month completers rather than the inpatient co-primary analysis set; alternatively its primary-analysis boxes may designate a different analysis from Table 2. The report does not distinguish those analysis labels in the figure. The source observations establish an attribution/count discrepancy; they do not establish an actual computational exclusion or propose a preferred analysis.

**Exact human question:** Which participant population do the Figure 1 primary-analysis boxes describe, and how should their 2003/1977 counts be reconciled with the stated 4800 primary-analysis participants and Table 2 denominators of 2400 per arm?

### F-NUM-002

**Title:** In-hospital death absolute-difference confidence interval and P value do not reconcile.

**Relationship ID:** N064; the parallel statistical relationship is Table 3 in-hospital death absolute difference.

**Compared locations and document roles:**
- REPORT [main article PDF p.8, Table 3 Death / In hospital, absolute difference and its P column](../../../jama_wang_2018_oi_180070.pdf#page=8): −0.7% (95% CI, −1.1% to +0.2%), P=.009.
- REPORT [main article PDF p.4, Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4): P<.05 considered statistically significant; all tests two-sided; comparative absolute differences presented with adjusted 95% CIs.
- REPORT [main article PDF p.5, Clinical Events paragraph](../../../jama_wang_2018_oi_180070.pdf#page=5): no significant total mortality difference in hospital or at 3/6/12 months. This is contextual corroboration, not an additional relationship; its intended test could be the separate HR test.

**Printed inputs:** Difference −0.7 percentage points; 95% CI [−1.1,+0.2]; paired P=.009; significance threshold .05. The distinct HR is .96 (.90–1.02), P=.14, with a separate column; that HR result must not be substituted for the difference's P.

**Rule and calculation:** Zero belongs to [−1.1,+0.2], so that interval does not exclude the null. The paired P=.009 is below .05. This is interval-versus-P incompatibility under the reported two-sided 95%/.05 levels. Half-unit endpoint ranges [−1.15,−1.05] and [.15,.25] continue to straddle zero, and P range [.0085,.0095] remains below .05. Route A category 1 is never screened as rounding; a relative-gap calculation is not the applicable test. The point estimate itself is contained and the endpoints are ordered.

**Focus area:** B (estimate and test logic).

**Proposed review domain:** statistical_results.

**Provisional relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The in-hospital mortality adjusted absolute-difference interval and P value, and whether that particular estimate is read as statistically distinguishable from zero.

**Why context does not resolve it:** Route A category 1 always requires inclusion for a reproduced interval-versus-P conflict. The separate nonsignificant HR/P and narrative cannot determine which absolute-difference interval/P pairing the reader should extract.

**Source-grounded alternatives and missing definition:** The printed interval or P may describe different inferential procedures, or one printed value may be intended differently. No source identifies a distinct procedure for this row's absolute-difference CI and P. Even if distinct analyses were intended, that is an alternative interpretation requiring human clarification, not a basis for excluding the observation.

**Exact human question:** What analyses produced the in-hospital mortality absolute-difference CI −1.1% to +0.2% and its paired P=.009, and how should their differing null-exclusion readings be interpreted?

## Excluded observations

Only apparent issues self-screened out are listed here. Reconciled arithmetic checks appear in the N inventory and are not listed as exclusions.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [main p.6 Table 1 CAD/previous MI, intervention](../../../jama_wang_2018_oi_180070.pdf#page=6) | 311/2400=12.9583% versus printed13.05%. Input interval[12.9348,12.9819]%, printed[13.045,13.055]%; gap.0631/13.05=.004837≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [supplement p.8 eTable4 control percentages](../../../joi180070supp2_prod.pdf#page=8) | Discharge antithrombotics2141/2400=89.2083 versus89.3: recomputed[89.1689,89.2478], printed[89.25,89.35], gap ratio.000025≤.05. AF39/174=22.4138 versus22.5, lipid1439/1586=90.7314 versus90.8 and diabetes557/688=80.9593 versus81.1 have overlapping input/printed intervals under the same rule. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main p.6 dyslipidemia](../../../jama_wang_2018_oi_180070.pdf#page=6) versus REPORT [supplement p.5 eTable2 dyslipidemia](../../../joi180070supp2_prod.pdf#page=5) | Baseline history totals596 versus347 differ across descriptive copies, while every count/denominator/percentage within each display reconciles; no primary/key secondary result or analysis-population size changes. | PERIPHERAL_COMPARISON |
| REPORT [main p.6 NIHSS](../../../jama_wang_2018_oi_180070.pdf#page=6) versus REPORT [supplement p.5 eTable2 NIHSS](../../../joi180070supp2_prod.pdf#page=5) | Admission median4 in each treatment arm versus3 in each availability stratum; these are copies of descriptive baseline summaries, not outcome/analysis-population quantities. | PERIPHERAL_COMPARISON |
| REPORT [main p.6 baseline801](../../../jama_wang_2018_oi_180070.pdf#page=6) versus REPORT [supplement p.2 twenty-per-cluster survey description](../../../joi180070supp2_prod.pdf#page=2) | 20×40 nominal target800 versus baseline801. Even exact arithmetic gives1/801=.001248; prescribed half-unit input intervals overlap the801 interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main Tables2/3 pp.7–8](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT [supplement eTables3/4 pp.6/8](../../../joi180070supp2_prod.pdf#page=6) | Adjusted absolute differences and modeled OR/HR values can differ from crude printed-proportion contrasts, including mortality. Each effect is explicitly adjusted/model-based; no effect is stated crude/unadjusted. | MODEL_VERSUS_CRUDE |
| PLAN [p.17 sample-size cycle description](../../../joi180070supp1_prod.pdf#page=17) and PLAN [p.13 Figure4](../../../joi180070supp1_prod.pdf#page=13) | Three30-patient improvement cycles can appear to give90 instead of120; linkedFigure4 explicitly has four30-patient collection batches with three intervening feedback/improvement loops, totaling120. The diagram resolves the batch/loop distinction. | CONTEXT_RESOLVES |
| REPORT [main p.4 opportunity example](../../../jama_wang_2018_oi_180070.pdf#page=4), PLAN [p.19 matching example](../../../joi180070supp1_prod.pdf#page=19) versus nine-measure definitions | Hypothetical eligibility for5of7 measures is illustrative, and3ones+2zeroes=5; not a printed realized denominator or a change to the enumeratednine trial measures. | CONTEXT_RESOLVES |
| REPORT [main p.4 sample size](../../../jama_wang_2018_oi_180070.pdf#page=4), PLAN [p.17 sample size](../../../joi180070supp1_prod.pdf#page=17) | Independent composite sample-size reproduction lacks variance/SD, exact equation and size-imbalance assumptions; no stated same-display method supplies these inputs. Missing specification alone is not a printed reproduced conflict. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

**Relationships:** 150. **Findings:** 2. **Excluded-observation rows:** 9. All findings were self-screened against both routes, and no reproduced route A category was excluded. Repeated occurrences are consolidated in their finding or exclusion row. No C IDs, adjudications or suggested corrections are assigned.

The numerical displays were completely reviewed. Independent model estimation requires unavailable patient/opportunity-level records, censoring histories, cluster counts and covariance matrices; counts and displayed arithmetic do not require those data. Historical reusable renderer/extractor versions are unrecorded; direct supplied-PDF readings confirmed the finding inputs. Both paired effect columns remain separate; no crude ratio was substituted for a modeled effect. No numeric scientific coverage gap remains.


## Bounded numeric-tail handoff

N001–N120 and N121–N150 are partitioned in relationships/parts/numeric_001_120.md and numeric_121_150.md. The fresh root/numeric_tail reviewer independently completed all 30 tail relationships; zero new findings and eight excluded observations appear in checkers/parts/numeric_tail.md and remain part of screening/pass-2/audit scope. Source-location refinements from that handoff were applied to N134 (plan p.16) and N148 (main p.6); no numerical input changed.
