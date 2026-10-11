# Statistical pass 1

Fresh runtime: 01a12959-b34f-7793-ae97-9dece6336e61. Model: gpt-6.1-sol. Reasoning effort: high. Scope: every S001–S123 and S301–S388, 211 statistical records, partitioned into 101 main-result and 110 methods/support records. Stable mapped S IDs are preserved. No previous candidate/checker/report conclusion was read. Scope and review contract were read completely. All observation decisions below were made by this agent against supplied source content and the scope threshold; there is no finding target. Ten findings and fifteen excluded observations. Every relationship has an explicit check outcome in the table appended below and in statistics/relationship_inventory.md.

Evidence: new complete main/support maps, source-linked immutable text/images, direct-source Poppler26.01.0 page extraction in preprocessing/statistics_pass_1/. CPU; no OCR/rendering needed. All17 confirmation derivatives are individually recorded in preprocessing/statistics_pass_1/engine_manifest.md; no fresh-required unit count is added. Detailed provenance and limitations are in statistics/pass_1_main_results.md and statistics/pass_1_methods_support.md. Images were read in bounded source batches, including every numeric annotation in DOC-005 pp.31–42. Diagnostic effect-measure arithmetic for every applicable main/PP/subgroup row is in statistics/effect_measure_diagnostics.md (57 count/effect rows, not sampled). The reference counts and roles come from supplied documents, not external evidence.

## Findings

### F-ST1-001

**Title:** Abstract hypoxemia interval includes zero while its P value is significant and the body prints a negative upper endpoint.

**Relationships:** S085. **Locations/roles:** REPORT [main article PDF p.1, abstract](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) and REPORT [main article PDF p.9, Table3 hypoxemia](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9). Direct source layout and visually read page confirm the positive abstract endpoint.

**Printed values:** Abstract 5.0% vs13.6%, RD−8.6%, 95%CI−11.1% to **+6.1%**, P<.001; Table3 49/989 vs134/987, RD−8.6%, CI−11.1% to **−6.1%**, P<.001.

**Rule/calculation:** The abstract's closed interval [−11.1,+6.1] contains the difference null0, whereas P<.001 is significant at the supplied two-sided .05 level. Table3 excludes0. Its upper-limit copy differs by12.2 percentage points; half-unit endpoint intervals [+6.05,+6.15] and [−6.15,−6.05] have gap12.10, relative discrepancy12.10/6.1=1.9836. Interval/test conflict itself is exempt from display-precision exclusion.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category1 (also category2).

**Affected result or extracted value:** Abstract hypoxemia RD95%CI and its significance reading. **Why context does not resolve it:** A category1 interval/test conflict must be registered; reconstructing the body reading does not remove a sign-changing printed limit.

**Alternatives/missing definition:** A missing minus sign is a source-grounded alternative because the body prints−6.1. Distinct analyses cannot explain the same matched abstract/body tuple without a stated mapping. No production mechanism is attributed. **Human question:** Which hypoxemia upper95%CI endpoint and corresponding analysis should be used for abstract extraction?

### F-ST1-002

**Title:** Three Table2 intervals print a null endpoint with significant P values.

**Relationships:** S002,S003,S016. **Locations/roles:** REPORT [main article PDF p.7, Table2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), tidal volume first/last hour and respiratory rate last hour.

**Printed values:** Tidal first hour RD0.1 (95%CI0–0.2), P=.007; tidal last hour RD0.1 (0–0.2), P=.008; respiratory last hour RD−0.4 (−0.7–0), P=.02. Confidence level95%; two-sided significance .05 in main methods p.4.

**Rule/calculation:** Each printed closed interval contains0; every P is below .05. Estimates lie inside ordered intervals, so the reproduced issue is specifically null-interval versus significance, consolidated as one zero-endpoint pattern. No asymptotic test, sample denominator or variance estimator is inferred. Display rounding intervals are not used to exclude routeA category1.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category1.

**Affected result or extracted value:** Significance and interval extraction for these three intraoperative comparisons. **Why context does not resolve it:** Category1 includes the reverse conflict (interval includes null with significant test), irrespective of a potential rounding explanation.

**Alternatives/missing definition:** Unrounded endpoints could exclude0, or interval and P could use different analyses. Neither exact endpoints nor separate interval/test methods are supplied in Table2. Both alternatives are recorded for adjudication, not assumed. **Human question:** What unrounded intervals and interval/test methods underlie these three significant comparisons whose displayed limits include0?

### F-ST1-003

**Title:** Table2 percentages and printed absolute differences imply different contrasts for monitoring and reversal.

**Relationships:** S038,S039. **Locations/roles:** REPORT [main article PDF p.8, Table2 neuromuscular monitoring/reversal](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8).

**Printed values:** Monitoring632/982(64.9%) vs651/984(67.7%), RD−1.8% (−6.0–2.4), P=.40. Reversal724/982(74.3%) vs723/984(75.2%), RD+0.2% (−3.6–4.1), P=.90.

**Rule/calculation:** High-minus-low percentages imply−2.8% and−0.9%. Allowing each displayed percentage ±.05 gives monitoring difference[−2.90,−2.70], while RD−1.8 gives[−1.85,−1.75], gap.85/1.8=.4722. Reversal gives[−1.00,−.80] versus RD[+.15,+.25], gap.95/.2=4.75 and reversed sign. By contrast, explicit fractions give−1.80008% and+.25148%, consistent with the printed RDs under half-unit input intervals. The high/low percentages almost reproduce denominators974/961 from the preceding neuromuscular-blockade row; that is a diagnostic alternative, not a denominator correction. Individual count-to-percentage relative discrepancies are small and are not independently registered.

**Focus areas:** A,B. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category2 (the extracted contrast changes sign/magnitude), also Route B.

**Affected result or extracted value:** Monitoring/reversal percentages and high-minus-low absolute differences. **Why context does not resolve it:** The row simultaneously supplies explicit fractions and a different percentage-based contrast; reconstruction of the fractions does not remove the sign-changing printed reading.

**Alternatives/missing definition:** Percentages may use the preceding blockade population while fractions/RD use available observations; the table does not say this. A population difference could explain calculations but needs explicit percentage and RD denominator mappings. **Human question:** Which denominator belongs to each percentage, and is the absolute-difference column a contrast of those displayed percentages or of the explicit fractions?

### F-ST1-004

**Title:** Repeated risk-ratio values follow a conditional allocation-risk pattern rather than the outcome-risk orientation of the displayed arms.

**Relationships:** All count/effect rows listed individually in statistics/effect_measure_diagnostics.md: S054,S055,S056,S057,S058,S059,S060,S061,S062,S063,S064,S065,S066,S067,S068,S069,S070,S071,S072,S073,S075,S077,S078,S079,S080,S082,S083,S085,S086,S087,S088,S089,S090; S092,S093,S094,S095,S096,S097,S098,S099,both S100 rows,S101; S344–S356. Corresponding component forest S373–S384 and repeated narrative/abstract occurrences are included in this one pattern. Near-equal rows are retained as diagnostic comparators, not asserted individually beyond precision.

**Locations/roles:** REPORT [main PDF p.4 binary effect methods](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [p.8 pleural/mild/primary narrative](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), [p.9 Table3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [p.10 Table3/notes/Figure2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), [p.1 primary abstract](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1); REPORT [results supplement p.29 eTable8](../../../joi190055supp4_prod_16092.pdf#page=29) and [p.42 eFigure12 component rows](../../../joi190055supp4_prod_16092.pdf#page=42). Main methods state effects on incidence reported as risk ratios, with site-adjusted mixed model explicitly separate as sensitivity. PP table header itself says Effect Estimate, so its effect identity remains an explicit mapping question rather than a substituted header.

**Printed values:** Main pleural43/989 vs21/987, RR1.35; hypoxemia49/989 vs134/987, RR.51; hypotension313/989 vs170/987, RR1.43; primary211/989 vs233/987, RR.93; all other exact tuples/locations are preserved in the diagnostic table and complete map. The pattern includes dozens of displayed rows, not just these examples.

**Rule/calculation:** For events a,b and arm totals H,L, outcome-risk orientation is R=(a/H)/(b/L). The diagnostic T=[a/(a+b)]/[(H−a)/(H+L−a−b)] instead compares probability of allocation to high PEEP among participants with versus without the outcome. It closely reproduces displayed values throughout both tables/forests: pleural T=1.35795, hypoxemia T=.51074, hypotension T=1.43123, primary T=.93579; near truncation/rounding accounts for last displayed digits. These are different conditional quantities. The arithmetic is a diagnostic of estimand orientation, not an inference of fitted model or production mechanism. The complete57-row table preserves R,T and all half-unit R intervals, including low-count rows where input intervals do not individually exceed the threshold. For example, hypoxemia R=.364932, R half-unit interval[.35950,.37041] versus printed [.505,.515], gap/printed value=.26390. Pleural R=2.04348, R interval[1.97075,2.11980], relative discrepancy=.45611; hypotension R=1.83745, interval[1.82729,1.84769], relative discrepancy=.27433. Both remain above the printed effect's half-unit interval by more than.05 relative.

**Focus areas:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W; repeated appearances in another REPORT corroborate the same internal pattern, rather than adding a conflicting cross-document copy. **Qualifying route:** Route B.

**Affected result or extracted value:** Outcome risk ratios and their estimand/reference orientation for pulmonary components, intraoperative outcomes, PP analyses and subgroups; largest contrasts include pleural effusion, hypoxemia and hypotension. Primary point-estimate gap alone is within the display rule and is not an independent qualifying discrepancy.

**Why context does not resolve it:** The result is labelled intervention effect on outcome incidence, but an alternative conditional allocation-risk quantity reproduces many supplied values. No stated adjustment, transformed estimand or denominator mapping explains that orientation. This is a reproduced effect-identity pattern grounded in labels and multiple rows, not merely a preference for crude estimates over an identified model.

**Alternatives/missing definition:** An unstated model-based estimand, adjustment or transformation could account for differences; that alternative requires the model/link, response variable, contrast and denominator orientation. Transposition is one diagnostic mathematical explanation, not an attributed mechanism. **Human question:** Which exact response, model, arm orientation and denominators produce the displayed risk ratios, and how do those values map to the stated high-versus-low effect on outcome incidence?

### F-ST1-005

**Title:** DIC risk-ratio interval excludes one with P>.99.

**Relationship:** S080. **Location/role:** REPORT [main PDF p.9, Table3 DIC](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), with REPORT [p.10 notes b/c](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Printed values:** High1(0.1%) versus low0; RD.1%(−.1–.3), RR2.00(95%CI1.91–2.09), P>.99. Interval Wald approximation; P chi-square; secondary two-sided .05.

**Rule/calculation:** 1<1.91<2.00<2.09 excludes the ratio null1, while P>.99 is nonsignificant at .05. RD interval includes0. The contradiction is independent of any finite-effect treatment of a zero control count and independent of the repeated effect-identity issue. RouteA category1 has no rounding exclusion.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category1.

**Affected result or extracted value:** DIC RR95%CI and significance reading. **Why context does not resolve it:** It is an always-register interval/test conflict even though interval and P are attributed to different analyses.

**Alternatives/missing definition:** Stated Wald-versus-chi-square distinction is retained; treatment of the zero cell and precise interval procedure are not supplied. **Human question:** What interval/zero-cell procedure yields1.91–2.09, and how should its exclusion of1 be reconciled with the stated P>.99?

### F-ST1-006

**Title:** In-hospital mortality interval does not reproduce the log-interval symmetry that reproduces neighboring risk-ratio rows.

**Relationship:** S088. **Location/role:** REPORT [main PDF p.9, Table3 mortality during hospital stay](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), with REPORT [p.10 note b interval method](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10). Comparator REPORT p.9 pleural effusion/hypoxemia/bradycardia and p.10 vasoactive rows.

**Printed values:** Mortality12/989 vs5/987, RR1.41(CI.95–1.81), P=.09. Comparators include pleural1.35(1.14–1.62), hypoxemia.51(.40–.65), bradycardia1.27(1.11–1.45), vasoactive1.10(1.01–1.21). One common Wald approximation is named for these rows.

**Rule/calculation:** A log-symmetric ratio interval has estimate²=lower×upper. This reproducing algebra holds within display precision for the neighboring rows; e.g. sqrt(1.14×1.62)=1.3590, sqrt(.40×.65)=.5099, sqrt(1.11×1.45)=1.2687. For mortality sqrt(.95×1.81)=1.3113, not1.41. Half-unit ratio1.405–1.415 and upper1.805–1.815 imply lower=ratio²/upper in[1.08762,1.10927]; printed lower is[.945,.955], gap≥.13262/.95=.13960. Thus more than .05 discrepancy remains without using any count or model variance. A diagnostic conditional-allocation log-Wald calculation additionally gives1.41538(1.03806–1.92984), but that diagnostic is not the reported analysis. No sidedness/covariance/denominator is inferred.

**Focus areas:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category4.

**Affected result or extracted value:** In-hospital mortality RR95%CI, particularly the lower limit. **Why context does not resolve it:** A reproducing same-display interval relation does not reproduce this row above display precision; the unstated interval convention becomes the question.

**Alternatives/missing definition:** A different asymmetric likelihood/interval procedure specifically for this row could explain it; the common footnote does not identify such an exception. No interval correction is proposed. **Human question:** What mortality-specific interval construction produces .95–1.81 around1.41, when the neighboring named-method intervals reproduce log symmetry?

### F-ST1-007

**Title:** PP cardiopulmonary-edema interval excludes one with P=.09.

**Relationship:** S355. **Location/role:** REPORT [results supplement PDF p.29, eTable8 cardiopulmonary edema](../../../joi190055supp4_prod_16092.pdf#page=29); REPORT [main p.4 primary/PP/binary methods](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4) supplies corresponding analysis context. The discrepancy itself is inside eTable8, not a comparison with the main ITT edema row.

**Printed values:** PP high15/917(1.6%) versus low7/912(.8%); effect1.36(95%CI1.02–1.82), P=.09. Table header is Effect Estimate95%CI rather than a substituted RR label; the matching main/SAP binary methods are ratio-based. Secondary two-sided .05 applies.

**Rule/calculation:** The ratio interval[1.02,1.82] excludes1, but .09>.05. The point estimate is contained in ordered endpoints. Null/test incompatibility uses the supplied ratio context, not an assumption about exact interval/test procedure. No display-precision exclusion applies.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_W / S_W. **Qualifying route:** Route A, category1.

**Affected result or extracted value:** PP cardiopulmonary-edema significance and95%CI. **Why context does not resolve it:** This is a category1 interval/test conflict; attributing CI and P to different analyses remains an alternative.

**Alternatives/missing definition:** Effect identity and exact PP interval/test mapping are not printed in the table; main binary RR/Wald and chi-square descriptions supply the strongest context. **Human question:** What effect measure and interval/test methods generated the PP edema tuple, and how is an interval entirely above1 reconciled with P=.09?

### F-ST1-008

**Title:** Planned clinical-severity-weighted primary-composite GEE has no identified reported result.

**Relationships:** S110,S123,S318 and comparison S357–S361/S373–S388. **Locations/roles:** PLAN [updated SAP PDF p.3, Clinical severity weight](../../../joi190055supp3_prod_16092.pdf#page=3); REPORT [main PDF p.4 sensitivity methods](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), [p.11 Additional Analysis](../../../jama_bluth_2019_oi_190055_16092.pdf#page=11); REPORT [results PDF p.30, eTable9](../../../joi190055supp4_prod_16092.pdf#page=30), [p.42 eFigure12](../../../joi190055supp4_prod_16092.pdf#page=42). Complete main14-page/results43-page mapping searched, not just selected displays.

**Printed statements:** SAP says each component will have an a posteriori clinical severity weight and a multivariate GEE will estimate common-effect OR while applying severity weights. Report identifies site-random, count/proportional odds, common-effect GEE, treatment-component interaction and average-relative-effect GEE; forest shows collapsed, count, common and average effects. Common-effect eTable9 footnote specifies one treatment effect across12 components and does not identify weights. Main says sensitivity analyses under alternative statistical assumptions were similar.

**Rule/logical comparison:** This is an expressly planned primary-outcome sensitivity analysis. The complete supplied report has no identified weighted model result or weights and no disclosure that the planned analysis was omitted/replaced. The supplied plan defines the weighted analysis separately from the common-effect and other analyses. The report does not explicitly map any result to that distinct planned analysis; absence of a reported identifiable counterpart is the reproduced observation, not a claim that the analysis was never performed.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type/all relationships:** P_R / P_R. **Qualifying route:** Route A, category5.

**Affected result or extracted value:** Planned clinical-severity-weighted primary-composite treatment OR and the main claim that alternate primary statistical analyses were similar. **Why context does not resolve it:** A planned primary analysis lacks an identifiable reported counterpart, an always-register category.

**Alternatives/missing definition:** The displayed common-effect GEE could actually be weighted, but neither table footnote nor forest identifies weights or maps that result to the planned weighted analysis. It could have been performed but unreported, or explicitly replaced outside the supplied package; neither is assumed. **Human question:** Which supplied result corresponds to the planned weighted GEE, what weights were used, or where is a disclosed amendment/omission recorded?

### F-ST1-009

**Title:** Same collapsed-composite tuple is labelled risk ratio in the main report and odds ratio in the sensitivity forest.

**Relationships:** S054,S101,S108,S385. **Locations/roles:** REPORT [main PDF p.1 abstract](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [p.9 Table3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [p.10 Figure2](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10); REPORT [results PDF p.42 eFigure12 global collapsed composite](../../../joi190055supp4_prod_16092.pdf#page=42).

**Printed values/labels:** Main RR.93(95%CI.83–1.04); forest global heading Odds Ratio(95%CI), collapsed row .93[.83,1.04]. Other global rows are explicitly OR-based count/GEE analyses and have their own tuples. This label is visually confirmed, not an OCR interpretation.

**Rule/logical comparison:** RR and OR are distinct effect measures with different extraction meaning. The exact matched collapsed-composite tuple is assigned both quantities without a separate model/estimand identification for that row. This finding concerns changing the named effect measure, not a recomputed crude versus adjusted comparison; numeric copies are identical, so no display discrepancy calculation applies.

**Focus areas:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_C / S_C. **Qualifying route:** Route B.

**Affected result or extracted value:** Effect-measure identity of .93(.83–1.04) for the primary collapsed composite in evidence synthesis. **Why context does not resolve it:** The forest's global OR heading is plausible for its neighboring models, while the same primary tuple is explicitly an RR in the main article; a reader cannot identify which label applies to this row from values alone.

**Alternatives/missing definition:** The OR heading may be intended only for the other global models, or the collapsed row could represent a distinct model result sharing displayed values. Neither row-specific exception nor model distinction is printed. **Human question:** Is the collapsed-composite forest row an RR or an OR, and does it reuse the main primary analysis or represent a different model?

### F-ST1-010

**Title:** Hypoxemia/hypotension counting definitions leave duration and pre-existing low-value handling unclear.

**Relationships:** S119 with S085/S086/S118. **Locations/roles:** REPORT [main PDF p.1 abstract hypoxemia](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [p.3 secondary definitions](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), [p.10 Table3 notes i/j](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), REPORT [results PDF p.21 secondary definitions](../../../joi190055supp4_prod_16092.pdf#page=21). PLAN definitions are corroborating context rather than an asserted report/plan discrepancy: original PLAN p.5 has durations, p.19 has the conditional drop rules.

**Printed statements:** Main hypoxemia SpO2≤92% for>1 minute (abstract and p.3); hypotension systolic<90mmHg for>2 minutes (p.3). Table notes instead say hypoxemia≤92% or decline>5% if previously<92%; hypotension<90mmHg or drop>10mmHg if previously<90. Results-supplement definitions simply≤92% and<90mmHg. They do not state which duration condition applies to the conditional declines or how a pre-existing below-threshold value is counted.

**Rule/logical comparison:** These are numeric outcome thresholds tied to49/989 versus134/987 hypoxemia events and313/989 versus170/987 hypotension events. The report supplies two counting-rule descriptions without explicitly mapping duration and the pre-existing-low branch to the analyzed events. A patient already below the threshold satisfies the unconditional low-value description but requires an additional decline under the conditional description; the source does not identify the intended branch priority. No patient-level recategorization or magnitude of change is inferred.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship type/all relationships:** S_C / S_C, S_W; cross-report definitions and within-main definitions contribute. **Qualifying route:** Route B.

**Affected result or extracted value:** Definitions attached to intraoperative hypoxemia (key secondary result in the abstract) and hypotension event counts and effect estimates. **Why context does not resolve it:** The numeric duration/conditional rules can identify different events, and none of the cited report descriptions expressly connects all branches to a single analyzed counting rule.

**Alternatives/missing definition:** Footnotes may abbreviate a duration rule that remains in force, and conditional decline rules may apply only to new recruitment-related deterioration in patients with pre-existing low values. The complete analyzed endpoint mapping is the missing definition, not a preferred definition proposed here. **Human question:** What exact duration and baseline-dependent decision rule was applied to count each hypoxemia/hypotension event, including patients already below threshold?

## Excluded observations

Only apparent observations not emitted appear here. Reconciled checks are in the relationship table, not this catalogue.

| Location | Observation | Reason code |
|---|---|---|
| Main p.7 Table2, heart-rate label S026–S028 | Heat rate is evident from beats/min and neighboring physiology; no numeric reading changes. | NOTATION_OR_TYPOGRAPHY |
| Main p.10 Figure2 waist-to-hip heading S100 | cm after the ratio heading resolves from dimensionless thresholds1.0; no numeric result changes. | NOTATION_OR_TYPOGRAPHY |
| Main p.4 vs SAP pp.1–2 S106/S311 | ITT versus modified ITT names share stated postrandomization exclusions and full flow; terminology alone adds no conflicting population value. | TERMINOLOGY_OR_WORDING |
| Main p.2 vs protocol p.13 S102/S303 | Permuted blocks4/6/8 versus6 and administrative risk-accounting detail are outside the specified statistical-result/planned-decision-rule focus in this package. | OUT_OF_FOCUS |
| Main p.4 vs original protocol p.23 S307/S308 | Original logistic/odds-ratio-relative-risk wording and SPSS are superseded by supplied explicitly finalized updated SAP; no separate current result is identified. | CONTEXT_RESOLVES |
| Main p.4/eFigure8 vs SAP p.2 S109/S313/S369 | Report does not explicitly name log-rank for P=.190; that value could be the planned test, so a planned primary test's nonreporting/replacement is not reproduced merely from absence of its label. | CONDITIONAL_OR_UNREPORTED |
| Main p.4/Table3 vs SAP p.2 S112/S314 | Additional zero-inflated-beta hospital-free-days confirmation has no identified result, but this is neither a planned primary nor an abstract/prespecified key secondary analysis; no displayed number conflicts. | CONDITIONAL_OR_UNREPORTED |
| Main Table3 p.9 S074/S121 | GI severity observed in49/46 of65/56 events does not claim completeness; unspecified missing severity alone is no inconsistency. | CONDITIONAL_OR_UNREPORTED |
| Main p.10 note d vs results p.20 S120 | Mild oxygen≤2L versus=2L is resolved from the adjacent moderate>2L partition; no identified numeric result depends on a competing meaning. | TERMINOLOGY_OR_WORDING |
| Results p.21 versus main pp.3/10 S091/S118/S310 | Broad secondary designation includes five-day mortality while main explicitly calls it post hoc; the supplement does not claim it prespecified, so nonprimary versus post hoc terms can coexist. | TERMINOLOGY_OR_WORDING |
| Results p.30 eTable9 S361/S388 | Log-Wald diagnostic for.99(.94–1.05) differs fromP=.98, but neither CI transformation nor average-effect test/variance mapping is given; significance/containment agrees and no defined test contradiction is reproduced. | CONDITIONAL_OR_UNREPORTED |
| Results pp.25–26 S321/S322 | Dopamine0 versus2, P1.00 is unlike ordinary chi-square/Fisher diagnostics, but this display does not identify its categorical test/available-case mapping; low-cell conventions are not inferred from neighboring nonsparse rows. | CONDITIONAL_OR_UNREPORTED |
| Results p.41 eFigure11 S372 | Caption says extra-pulmonary complications but title, axis,0.5%/0.3%, parenthetical five-day-mortality HR and main tuple identify mortality immediately. | CONTEXT_RESOLVES |
| Results pp.38–39 eFigures8/9 S370 | Identical per-time-point risk tables under primary/severe graphs are an apparent copy concern; these peripheral counts do not establish a primary/key-secondary analysis-size or decision-rule change and censoring mapping is not supplied. | PERIPHERAL_COMPARISON |
| Main p.9 Table3 versus results p.42 eFigure12 S375/S379/S382 | Repeated component point estimates differ .90/.91, .99/1.00 and1.35/1.36; half-unit printed-copy intervals touch, and any residual relative discrepancy is at most.05. Different95%/99.58% interval limits are distinct confidence levels. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations

Every assigned relationship was checked; no scientific scope remains uncovered. Exact latent mean values, available-case denominators for many Table2 continuous variables, distribution-specific procedural tests, subgroup GLM link, GEE covariance/variance details and East6.0 implementation settings are not supplied. Graphical mean/CI endpoints without scalar labels cannot be recovered precisely from a supplied figure and were assessed for order/containment/direction visually. These missing definitions limit exact diagnostic reproduction, not unit coverage. Original randomization assumptions, sample-size diagnostic, all stopping/multiplicity rules and every available printed interval/test were reviewed. No actual interim test results are supplied. Claims about treatment superiority were assessed against final primary .044 and secondary .05; all primary conclusions remain nonsignificant in the printed analyses. Distinct outcome definitions/estimands and repeated patterns remain separate from interval/test findings.

## Explicit outcome for every assigned S ID

The following rows are the canonical pass1 records, with individual outcomes; the underlying printed evidence is in the indexed maps and the two bounded statistical parts.

| S ID | Check outcome | Pass 1 |
|---|---|---|
| S001 | Tidal volume after intubation: ordered CI contains estimate and zero; .15 nonsignificant. Mean rounding can reconcile zero difference. | PASS_1_COMPLETE |
| S002 | Tidal volume first hour: CI 0–0.2 contains null with P .007; F-ST1-002. | PASS_1_COMPLETE |
| S003 | Tidal volume last hour: CI 0–0.2 contains null with P .008; F-ST1-002. Rounded means do not identify available-case contrast. | PASS_1_COMPLETE |
| S004 | Initial PEEP: positive ordered containing CI and P <.001 agree; intervention orientation agrees. | PASS_1_COMPLETE |
| S005 | First-hour PEEP: CI 7.9–8.0 contains 7.9, positive test agrees; means and narrative match with rounding. | PASS_1_COMPLETE |
| S006 | Last-hour PEEP: positive ordered containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S007 | Recruitment: percentage-point contrast, ordered CI and P <.001 agree; low rescue 11 patients matches text. | PASS_1_COMPLETE |
| S008 | Initial peak pressure: positive containing CI, P <.001 and narrative higher-high agree. | PASS_1_COMPLETE |
| S009 | First-hour peak pressure: positive containing CI, P <.001 and figure direction agree. | PASS_1_COMPLETE |
| S010 | Last-hour peak pressure: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S011 | Initial driving pressure: negative containing CI and P <.001 agree with high-minus-low. | PASS_1_COMPLETE |
| S012 | First-hour driving pressure: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S013 | Last-hour driving pressure: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S014 | Initial respiratory rate: negative CI excludes zero and P <.001 agrees. | PASS_1_COMPLETE |
| S015 | First-hour respiratory rate: CI includes zero and P .09 agrees. | PASS_1_COMPLETE |
| S016 | Last-hour respiratory rate: CI −0.7 to 0 includes null with P .02; F-ST1-002. | PASS_1_COMPLETE |
| S017 | Initial FIO2: CI includes zero and P .27 agrees; fractional unit distinct from supplement percent. | PASS_1_COMPLETE |
| S018 | First-hour FIO2: negative containing CI and P <.001 agree; rounded group means insufficient for precise difference. | PASS_1_COMPLETE |
| S019 | Last-hour FIO2: negative containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S020 | Initial SpO2: positive containing CI and P <.001 agree; rounded means can yield 0.7. | PASS_1_COMPLETE |
| S021 | First-hour SpO2: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S022 | Last-hour SpO2: positive containing CI and P <.001 agree. | PASS_1_COMPLETE |
| S023 | Initial end-tidal CO2: CI includes zero and P .09 agrees. | PASS_1_COMPLETE |
| S024 | First-hour end-tidal CO2: positive CI and P .01 agree. | PASS_1_COMPLETE |
| S025 | Last-hour end-tidal CO2: positive CI and P .004 agree. | PASS_1_COMPLETE |
| S026 | Initial heart rate: containing CI crosses zero and P .38 agrees; printed Heat wording excluded. | PASS_1_COMPLETE |
| S027 | First-hour heart rate: containing CI crosses zero and P .36 agrees. | PASS_1_COMPLETE |
| S028 | Last-hour heart rate: negative containing CI and P .02 agree. | PASS_1_COMPLETE |
| S029 | Initial mean arterial pressure: positive containing CI and P .03 agree. | PASS_1_COMPLETE |
| S030 | First-hour mean arterial pressure: containing CI crosses zero and P .87 agrees. | PASS_1_COMPLETE |
| S031 | Last-hour mean arterial pressure: containing CI crosses zero and P .81 agrees. | PASS_1_COMPLETE |
| S032 | Head-elevation partition: both categories exhaust 989/987; global P .70 is not a category-specific P. | PASS_1_COMPLETE |
| S033 | Noninvasive ventilation: counts/percentages and RD agree within precision; containing CI crosses zero and P .64 agrees. | PASS_1_COMPLETE |
| S034 | Anesthesia partition: totals 989/987; global P .51 and no interval; no separate-category test inferred. | PASS_1_COMPLETE |
| S035 | Epidural: count-based RD and printed CI/P .92 agree. | PASS_1_COMPLETE |
| S036 | Epidural location: denominators 80/81 and category totals agree; global P .81, no separate estimates. | PASS_1_COMPLETE |
| S037 | Neuromuscular blockade: CI crosses zero and P .08 agrees; count-based RD reconciles. | PASS_1_COMPLETE |
| S038 | Monitoring: fractions reproduce RD −1.8, but percentages imply −2.8; F-ST1-003. CI/P .40 agree about nonsignificance. | PASS_1_COMPLETE |
| S039 | Reversal: fractions reproduce positive RD about 0.25, but percentages imply −0.9; F-ST1-003. CI/P .90 agree about nonsignificance. | PASS_1_COMPLETE |
| S040 | Total fluids: CI contains .02 and zero; P .79 agrees. Median difference is not substituted for unspecified contrast. | PASS_1_COMPLETE |
| S041 | Crystalloids: CI contains zero estimate and null; P .97 agrees. | PASS_1_COMPLETE |
| S042 | Colloid volume: CI contains .05 and zero; P .50 agrees; supplement volume includes nonrecipients, not substituted for conditional median. | PASS_1_COMPLETE |
| S043 | Colloid receipt: count-based RD 1.8 and CI/P .09 agree within precision. | PASS_1_COMPLETE |
| S044 | Urine output: CI contains −.02 and zero; P .16 agrees; contrast is not assumed a difference of medians. | PASS_1_COMPLETE |
| S045 | Packed cells: count-based RD and containing CI/P .14 agree. | PASS_1_COMPLETE |
| S046 | Plasma: count-based RD and containing CI/P .58 agree. | PASS_1_COMPLETE |
| S047 | Platelets: equal counts, zero RD, containing CI and P >.99 agree. | PASS_1_COMPLETE |
| S048 | Albumin: RD agrees with counts; containing CI crosses zero and P .14 agrees. | PASS_1_COMPLETE |
| S049 | Blood loss: containing CI crosses zero and P .77 agrees; 5.2 compatible with integer-rounded group means. | PASS_1_COMPLETE |
| S050 | End-surgery temperature: estimate and CI touch zero, P .12 nonsignificant; rounded group means can reconcile contrast. | PASS_1_COMPLETE |
| S051 | Surgery duration: CI contains zero; P .62 agrees; median/IQR not used to infer contrast method. | PASS_1_COMPLETE |
| S052 | Anesthesia duration: CI contains zero; P .94 agrees. | PASS_1_COMPLETE |
| S053 | Narrative directional and nonsignificance claims agree with matched intervention/management rows; pain/dyspnea checked against eTable 7. | PASS_1_COMPLETE |
| S054 | Primary composite: all copies match; CI/test nonsignificant at .044, direction coherent; effect-orientation diagnostic joins F-ST1-004. | PASS_1_COMPLETE |
| S055 | Mild respiratory failure: all copies match and null CI/P .22 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S056 | Moderate respiratory failure: ordered containing intervals and P .10 agree about null; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S057 | Severe respiratory failure: null intervals and P .45 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S058 | Atelectasis: null intervals and P .25 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S059 | Pleural effusion: both intervals positive and P .005 agree; narrative higher-high agrees; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S060 | Infiltrates: null intervals/P .47 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S061 | Cardiopulmonary edema: main RR CI .99–1.74 includes null with P .12; pattern F-ST1-004, distinguished from PP S355 conflict. | PASS_1_COMPLETE |
| S062 | Bronchospasm: null intervals and P .67 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S063 | Pulmonary infection: equal event counts, null CI/P >.99 agree; near-one effect within precision. | PASS_1_COMPLETE |
| S064 | Aspiration: null intervals/P >.99 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S065 | ARDS: null intervals and P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S066 | Pneumothorax: null intervals and P .37 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S067 | Severe composite: interval/P .22 agree about null; component counts need not sum to union; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S068 | Extrapulmonary composite: null intervals/P .31 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S069 | SIRS: ordered null intervals/P .44 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S070 | Sepsis: ordered null intervals/P .60 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S071 | Severe sepsis: ordered null intervals/P .46 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S072 | Septic shock: ordered null intervals/P .79 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S073 | GI failure: ordered null intervals/P .40 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S074 | GI conditional severity: fractions/partition sums 49/46 agree; global P .64. Missing severity for some events is not itself a conflicting value. | PASS_1_COMPLETE |
| S075 | Kidney failure: null intervals/P .89 agree; near-one effect within precision. | PASS_1_COMPLETE |
| S076 | Kidney stage: fractions/partition totals 31/32 agree within precision; global P .97. | PASS_1_COMPLETE |
| S077 | Extrapulmonary infection: null intervals/P .40 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S078 | Hepatic failure: equal counts and null intervals/P >.99 agree. | PASS_1_COMPLETE |
| S079 | Coma: equal counts and null intervals/P >.99 agree. | PASS_1_COMPLETE |
| S080 | DIC: RR CI 1.91–2.09 excludes one with P >.99; F-ST1-005, separately from repeated effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S081 | MI: both zero, no effect/CI/P printed; no estimate is invented. | PASS_1_COMPLETE |
| S082 | Wound healing: null intervals/P .55 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S083 | ICU: null intervals/P .29 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S084 | Hospital-free days: mean-difference footnote resolves RR-column placement; negative .77 lies inside CI crossing zero, t P .27 agrees; rounded SD/sample-size diagnostic coherent. | PASS_1_COMPLETE |
| S085 | Hypoxemia: main Table 3 negative CI/P agree, abstract CI −11.1 to +6.1 includes null with P <.001; F-ST1-001. Effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S086 | Hypotension: positive intervals/P <.001 and narrative direction agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S087 | Bradycardia: positive intervals/P .001 and narrative direction agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S088 | In-hospital mortality: printed intervals/P .09 all nonsignificant; printed RR interval does not share reproducing log symmetry of other rows, F-ST1-006; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S089 | Rescue: negative RD, RR below one and P <.001 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S090 | Vasoactive need: positive intervals and P .02 agree; same counts/P as eTable 4; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S091 | Five-day mortality: HR explicitly Cox; containing CI crosses one and P .48 agrees, matched .484 in eFigure 11; broader supplement secondary designation does not contradict explicit main post hoc designation and is excluded as wording. | PASS_1_COMPLETE |
| S092 | Nonlaparoscopic: containing CI crosses one; graphical direction favors low; interaction .08 is separate contrast; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S093 | Laparoscopic: containing CI crosses one; graphical direction favors high; interaction .08 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S094 | BMI <40: containing CI crosses one; interaction .97 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S095 | BMI ≥40: containing CI crosses one; interaction .97 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S096 | SpO2 <96: containing CI crosses one; interaction .35 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S097 | SpO2 ≥96: containing CI crosses one; near-one allocation-risk diagnostic, no within-subgroup P supplied. | PASS_1_COMPLETE |
| S098 | Peripheral incision: containing CI crosses one; direction favors low; interaction .11 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S099 | Upper abdominal incision: containing CI crosses one; direction favors high; interaction .11 separate; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S100 | Both waist/hip categories: ordered containing intervals cross one; interaction .65 separate; missing waist measurements do not conflict with full-population totals. Effect pattern F-ST1-004; cm wording excluded. | PASS_1_COMPLETE |
| S101 | All-patient diamond: same primary counts/RR/CI as S054; containing null interval agrees with main .23; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S102 | Individual site-stratified 1:1 randomization coherent; PLAN block 6 vs REPORT blocks 4/6/8 is excluded as outside stated result/design focus. | PASS_1_COMPLETE |
| S103 | Original 40% vs 30%, two-sided .05/80% gives normal-approximation diagnostic about 356/group; 748 target consistent with printed 356 and 5% at display precision. | PASS_1_COMPLETE |
| S104 | Blinded pooled-rate re-estimation disclosed; 1912/.95=2012.63, target 2013 agrees. East group-sequential size cannot be independently regenerated without complete software specification. | PASS_1_COMPLETE |
| S105 | Final .044 agrees with Z 2.012; interim .006/.015/.044 and nonbinding futility rules agree with PLAN. Actual interim test values unreported; continuation alone is no conflict. | PASS_1_COMPLETE |
| S106 | Complete-case/modified ITT definition and flow exclusion explain analyzed 1976 after 8 losses; terminology ITT vs modified ITT excluded. No missing-data sensitivity trigger (>1%) reached by 8/1984. | PASS_1_COMPLETE |
| S107 | PP exclusions and sums reconcile 989−72=917 and 987−75=912; missing ventilation and specified PEEP exclusions sum. | PASS_1_COMPLETE |
| S108 | Primary binary model/test declarations match SAP; effect-orientation pattern F-ST1-004. Two-sided .044 consistently distinct from .05 secondary. | PASS_1_COMPLETE |
| S109 | KM/Cox primary HR matches eFigure 8; SAP log-rank test not explicitly named in report but .190 could be its P; absence alone excluded, not asserted replaced. | PASS_1_COMPLETE |
| S110 | Site-random GLMM sensitivity matches eTable 9. Planned severity-weighted primary GEE has no identified reported result; F-ST1-008. | PASS_1_COMPLETE |
| S111 | Binary outcome interval/P method declarations match Table 3; interval conflicts tracked independently F-ST1-005/F-ST1-007; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S112 | Hospital-free t-test/mean difference matches Table 3 note; no null/test conflict. Planned additional GAM confirmation unreported but not primary/key secondary; excluded. | PASS_1_COMPLETE |
| S113 | Five-day unadjusted Cox matches main note and eFigure 11 HR/CI/P, not substituted for in-hospital endpoint. | PASS_1_COMPLETE |
| S114 | Exploratory secondary analyses/no general adjustment consistent; Bonferroni component sensitivity is a distinct analysis. Primary .044 exception clear. | PASS_1_COMPLETE |
| S115 | All five subgroup dichotomies and interaction specification match SAP and Figure 2; no within-stratum P inferred from interaction. | PASS_1_COMPLETE |
| S116 | Complete-case statement coherent; rescue/vasoactive designated post hoc in all main occurrences; R version change alone excluded. | PASS_1_COMPLETE |
| S117 | Twelve-component first-five-day union matches SAP/PLAN; component sums not required to equal composite incidence. | PASS_1_COMPLETE |
| S118 | Nine reported prespecified secondary outcomes match updated SAP grouping; supplement includes post hoc five-day mortality under a broader secondary heading, excluded as wording rather than an explicit prespecification claim. Historical protocol supersession checked separately. | PASS_1_COMPLETE |
| S119 | Main duration/baseline-sensitive hypoxemia/hypotension definitions do not identify a single counting rule; F-ST1-010. Bradycardia definitions agree. | PASS_1_COMPLETE |
| S120 | Respiratory severity thresholds checked; mild ≤2 L in main vs =2 L supplement is compressed wording adjacent to moderate >2 L; excluded, no additional numeric effect asserted. | PASS_1_COMPLETE |
| S121 | GI severity subset 49/46 of 65/56 events is compatible with incomplete classification; conditional missing detail alone excluded. Stages/overall test coherent. | PASS_1_COMPLETE |
| S122 | Kidney risk/injury/failure/loss definitions and row counts reconcile; no stage-specific P inferred. | PASS_1_COMPLETE |
| S123 | PP primary CI/P, site-adjusted and alternate displayed models all support nonsignificance; clinical weighting lacks identified result F-ST1-008. Subgroup interaction claim matches .08. | PASS_1_COMPLETE |
| S301 | Original PLAN power inputs match report; diagnostic n≈356/group and target 748 within display rule. | PASS_1_COMPLETE |
| S302 | Revised inputs .20/.15, .05/80%, max1912 and dropout-inflated2013 internally coherent; full East reproduction unavailable, not a conflicting printed number. | PASS_1_COMPLETE |
| S303 | Allocation website/site balance and block6 compared with main site strata and blocks4/6/8; administrative block/stratum wording alone excluded. | PASS_1_COMPLETE |
| S304 | PLAN five-day collapsed 12-component primary matches main/SAP; union definition coherent. | PASS_1_COMPLETE |
| S305 | Original secondary lists and statuses compared with updated SAP and reports; disclosed updated SAP supersedes earlier list, not independent drift finding. | PASS_1_COMPLETE |
| S306 | Information fractions ×1912 give956/1434/1912; cumulative alpha/beta monotone to .05/.20; crossing sums .801/.200 within precision; Z-to-two-sided P companions reconcile. | PASS_1_COMPLETE |
| S307 | Older logistic/OR/RR hybrid wording compared with explicit updated SAP; no coherent choice challenged. No effect inferred from term alone. | PASS_1_COMPLETE |
| S308 | Older confirmatory-primary/exploratory-other designation matches updated main; updated SAP supplies modified ITT and R in place of earlier SPSS. | PASS_1_COMPLETE |
| S309 | Version-history deletion/reintroduction of interim analysis explicitly disclosed; old threshold not treated as current stopping rule. | PASS_1_COMPLETE |
| S310 | Updated SAP primary and seven grouped prespecified secondary items match nine main outcomes; broad report-supplement secondary wording does not assert five-day prespecification. | PASS_1_COMPLETE |
| S311 | Complete-case/trigger>1%/modified ITT coherent with 8 losses and final1976; absent imputation under <1% not a conflict. | PASS_1_COMPLETE |
| S312 | Distribution assessment, two-sided levels, no general adjustment and selected ventilation times coherent with reports; no normality result invented. | PASS_1_COMPLETE |
| S313 | Primary RR/Wald/chi-square and .044 match main; log-rank may supply unnamed eFigure 8 P, absent named test alone excluded. | PASS_1_COMPLETE |
| S314 | Secondary RR and hospital-free t match main; additional zero-inflated-beta mean-ratio result not identified, outside primary/key omission threshold and excluded. | PASS_1_COMPLETE |
| S315 | Five subgroup boundaries/interactions match all Figure 2 rows; not interpreted as ten main-effect tests. | PASS_1_COMPLETE |
| S316 | GLMM site random and component count/proportional odds with Mann–Whitney correspond exactly to eTable 9 footnotes. | PASS_1_COMPLETE |
| S317 | 1−.05/12=.995833..., printed99.58% agrees; component forest all intervals ordered/containing; common/distinct GEE specifications map to eTable 9. | PASS_1_COMPLETE |
| S318 | Treatment-by-component P .11 has identified reported result; clinical severity-weight GEE lacks identified counterpart; F-ST1-008. | PASS_1_COMPLETE |
| S319 | All ARISCAT operational OR/CI/coefficients and rounded coefficient×10 scores checked; estimates contained, limits ordered and score arithmetic coherent; historical model not trial treatment estimate. | PASS_1_COMPLETE |
| S320 | All fluid count/percent/volume/SD/P tuples checked; no CI conflicts; rounded means and unspecified distribution/sample detail prevent unsupported exact-test inference. Main median vs supplement overall mean not conflicting estimands. | PASS_1_COMPLETE |
| S321 | All six drug/count/dose tuples checked; need-for-vasoactive counts/P match main; dopamine sparse-count P raises diagnostic question but exact test unidentified, excluded. | PASS_1_COMPLETE |
| S322 | All 29 agent rows checked; counts within precision, overlapping drug classes not summed as partition; sparse-cell P differences cannot establish test without definition. | PASS_1_COMPLETE |
| S323 | All surgical-priority/position/wound partitions checked; small total differences reflect available observations, percentages within precision. Global P not interpreted per category; pressure no interval conflict. | PASS_1_COMPLETE |
| S324 | Dyspnea day1: equal rounded means, P .53; no CI, no contradiction under mean precision or a named test. | PASS_1_COMPLETE |
| S325 | Dyspnea day2: rounded mean ranges can yield small nonsignificant contrast/P .57; no exact test inferred. | PASS_1_COMPLETE |
| S326 | Dyspnea day3: rounded mean ranges can reconcile P .68; no CI. | PASS_1_COMPLETE |
| S327 | Dyspnea day4: equal rounded means and P .79 compatible; no CI. | PASS_1_COMPLETE |
| S328 | Dyspnea day5: equal rounded means and P .78 compatible; no CI. | PASS_1_COMPLETE |
| S329 | Thoracic day1: rounded mean ranges can reconcile P .52; no CI. | PASS_1_COMPLETE |
| S330 | Thoracic day2: SD3.9 retained, not normalized; P .34 does not establish numeric contradiction with rounded means. | PASS_1_COMPLETE |
| S331 | Thoracic day3: rounded equal means/P .94 compatible; no CI. | PASS_1_COMPLETE |
| S332 | Thoracic day4: rounded mean ranges include a difference yielding P .20; no test assumed. | PASS_1_COMPLETE |
| S333 | Thoracic day5: equal rounded means/P .16 can reconcile through precision; no CI. | PASS_1_COMPLETE |
| S334 | Abdominal rest day1: printed mean intervals allow .10 difference and nonsignificant P .10; no CI. | PASS_1_COMPLETE |
| S335 | Abdominal rest day2: equal rounded means/P .31 compatible; no CI. | PASS_1_COMPLETE |
| S336 | Abdominal rest day3: equal rounded means/P .94 compatible; no CI. | PASS_1_COMPLETE |
| S337 | Abdominal rest day4: equal rounded means/P .75 compatible; no CI. | PASS_1_COMPLETE |
| S338 | Abdominal rest day5: equal rounded means/P .83 compatible; no CI. | PASS_1_COMPLETE |
| S339 | Abdominal incident day1: equal rounded means/P .52 compatible; no CI. | PASS_1_COMPLETE |
| S340 | Abdominal incident day2: rounded mean ranges permit small contrast/P .51; no CI. | PASS_1_COMPLETE |
| S341 | Abdominal incident day3: equal rounded means/P .55 compatible; no CI. | PASS_1_COMPLETE |
| S342 | Abdominal incident day4: rounded mean ranges permit small contrast/P .69; no CI. | PASS_1_COMPLETE |
| S343 | Abdominal incident day5: equal rounded means/P .58 compatible; no CI. | PASS_1_COMPLETE |
| S344 | PP primary: counts/percentages and ordered containing null CI/P .17 agree; effect-orientation pattern F-ST1-004. | PASS_1_COMPLETE |
| S345 | PP mild: ordered containing null CI/P .15 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S346 | PP moderate: ordered containing null CI/P .15 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S347 | PP severe: ordered containing null CI/P .18 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S348 | PP ARDS: ordered containing null CI/P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S349 | PP bronchospasm: ordered containing null CI/P .84 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S350 | PP infiltrates: equal counts, ordered null CI/P .99 agree; near-one estimate within display precision. | PASS_1_COMPLETE |
| S351 | PP infection: ordered containing null CI/P .83 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S352 | PP aspiration: ordered containing null CI/P1.00 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S353 | PP pleural: CI excludes one and P .01 agrees; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S354 | PP atelectasis: containing null CI/P .18 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S355 | PP cardiopulmonary edema: CI1.02–1.82 excludes one with P .09; F-ST1-007; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S356 | PP pneumothorax: ordered containing null CI/P .62 agree; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S357 | Site-random OR.86(.68–1.08), P.19: ordered containing null CI/test agree; not compared with crude RR. | PASS_1_COMPLETE |
| S358 | Count OR.88(.72–1.09), P.25: ordered containing null CI/test agree despite expressly different OR and Wilcoxon analyses; mean count distinct from incidence. | PASS_1_COMPLETE |
| S359 | Common-effect GEE OR.93(.80–1.08), P.37: ordered containing null CI/test agree; no covariance inferred. | PASS_1_COMPLETE |
| S360 | Treatment-component interaction P .11: defined heterogeneity test, no estimate/CI given; no other row P substituted. | PASS_1_COMPLETE |
| S361 | Average-effect OR.99(.94–1.05), P.98: ordered containing null CI/test significance agree; log-Wald diagnostic differs but test/CI transform not specified, excluded. | PASS_1_COMPLETE |
| S362 | Sequential figure directions/boundaries/enrollment match PLAN; drawing is design boundary not observed Z, so continuation not inferred from it. | PASS_1_COMPLETE |
| S363 | Tidal graph: all five means inside their graphical CIs; unit/legend coherent; .081 is time×group, not main table within-time .007/.008. | PASS_1_COMPLETE |
| S364 | PEEP graph: all five means contained, high above low, P <.001 interaction distinct from high-low comparisons; no precise endpoint invented. | PASS_1_COMPLETE |
| S365 | Peak graph: all five means contained, high above low, interaction P <.001 and main direction agree. | PASS_1_COMPLETE |
| S366 | SpO2 graph: all five means contained, high above low, interaction P <.001; table/graphic direction agrees. | PASS_1_COMPLETE |
| S367 | Driving graph: all five means contained, high below low, interaction P <.001; pressure-minus-PEEP definition coherent. | PASS_1_COMPLETE |
| S368 | FIO2 graph: all five means contained, high lower after initial time, interaction P <.001; percent vs main fraction scale resolves immediately. | PASS_1_COMPLETE |
| S369 | Primary time-to-event HR.88(.73–1.06), P.190: containing null CI and direction agree; all annotations match caption; Schoenfeld .05 no reported contradictory decision. | PASS_1_COMPLETE |
| S370 | Severe time-to-event HR.85(.66–1.09), P.197: containing null CI and direction agree; Schoenfeld .28; duplicate primary risk table apparent issue excluded as peripheral. | PASS_1_COMPLETE |
| S371 | Extrapulmonary HR1.12(.89–1.39), P.314: containing null CI and direction agree; Schoenfeld .67; caption/annotation consistent. | PASS_1_COMPLETE |
| S372 | Five-day HR1.67(.40–6.97), P.484: containing null CI and direction agree; Schoenfeld .14; caption's extraneous outcome phrase resolves from title, scale and parenthesis and is excluded. | PASS_1_COMPLETE |
| S373 | Mild forest RR.92[.76,1.12]: containing ordered99.58% CI; no printed P; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S374 | Moderate forest RR.83[.59,1.17]: containing ordered99.58% CI; no P inferred; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S375 | Severe forest RR.91[.61,1.34]: containing ordered99.58% CI; effect pattern F-ST1-004; small .90/.91 copy gap within precision. | PASS_1_COMPLETE |
| S376 | Aspiration RR1.33[.41,4.30]: containing ordered99.58% CI/arrows coherent; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S377 | Bronchospasm RR1.09[.62,1.91]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S378 | ARDS RR1.50[.65,3.44]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S379 | Infection RR1.00[.52,1.90]: containing ordered99.58% CI; .99/1.00 display difference within precision. | PASS_1_COMPLETE |
| S380 | Atelectasis RR.88[.64,1.23]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S381 | Edema RR1.31[.87,1.98]: containing ordered99.58% CI; different multiplicity level not compared with95% PP conflict; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S382 | Pleural RR1.36[1.05,1.76]: containing ordered99.58% CI excludes one; no multiplicity-adjusted P printed; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S383 | Pneumothorax RR.50[.04,5.96]: containing ordered99.58% CI/arrows coherent; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S384 | Infiltrates RR.87[.49,1.55]: containing ordered99.58% CI; effect pattern F-ST1-004. | PASS_1_COMPLETE |
| S385 | Collapsed .93[.83,1.04] called OR while main same tuple called RR; quantity-label conflict F-ST1-009. Containment/order coherent. | PASS_1_COMPLETE |
| S386 | Count .88[.72,1.09]: OR label agrees with eTable 9, ordered containing null95% CI. | PASS_1_COMPLETE |
| S387 | Common GEE .93[.80,1.08]: OR label and tuple match eTable 9; containing null95% CI. | PASS_1_COMPLETE |
| S388 | Average GEE .99[.94,1.05]: OR label and tuple match eTable 9; containing null95% CI; diagnostic limitation tracked at S361. | PASS_1_COMPLETE |
