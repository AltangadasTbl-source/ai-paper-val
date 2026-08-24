# Numeric Consistency Review

## Scope, method, and outcome

This review covers the complete canonical numeric/reporting inventory `N001`--`N062` and the numeric, denominator, percentage, scale, rate/count, and repeated-value implications of statistical relationships `S001`--`S039`. Evidence was limited to the supplied PDFs and their fresh 1.5.2 native/layout text and rendered-page assets. Prior audit derivatives were not used.

For printed integer identities, the tolerance was exactly zero. For printed percentages, the accepted interval was the usual nearest-whole-percent interval: a count divided by its stated denominator may differ from the printed percentage by at most 0.5 percentage point (or by the displayed special `<1%` convention). For displayed decimal values, arithmetic was assessed at the printed precision; a difference no greater than one final displayed unit was treated as compatible with rounding. Rates per 100 person-years were never tested as proportions because their person-time denominators are not participant denominators.

**Completed relationships:** 62/62 N relationships, plus all 35 S relationships with applicable displayed numeric implications; S021-S023 and S039 were reviewed as prospective definition relationships without an additional observed count identity.

**Lane observations requiring later candidate merging:** 4.
**No-candidate checks:** all other relationships described below reconciled, were definitionally non-additive, or lacked a supplied denominator/model definition needed for a stronger mechanical test.

## Complete N-relationship register

| ID | Checks performed and result |
|---|---|
| N001 | **COMPLETE — PASS.** DOC-001 p1/p6: `370+333+289+320=1312`; abstract and Figure 1 agree. |
| N002 | **COMPLETE — PASS.** DOC-001 p6: `438+1494=1932`; `1932+1312=3244`. |
| N003 | **COMPLETE — PASS.** DOC-001 p1/p6: all four randomized cells (370/333/289/320) repeat as primary-analysis and adverse-event populations. |
| N004 | **COMPLETE — PASS.** DOC-001 p6: complete plus lost/dead is `260+110=370`, `236+97=333`, `212+77=289`, `226+94=320`. “No final blood” is an overlapping status including deaths, so it is not addable to loss/death. |
| N005 | **COMPLETE — PASS.** DOC-001 p6: complete-case plus exclusion identities are `259+111=370`, `236+97=333`, `211+78=289`, `226+94=320`; baseline-eGFR missing counts explain the specified exclusions. |
| N006 | **COMPLETE — PASS.** DOC-001 p4: 1090/1312=83.1%; 934/1312=71.2%; 934/1229 alive=76.0%; 1091/1312=83.2%; 945/1312=72.0%; 945/1229=76.9%. All reconcile under nearest-percent rounding. |
| N007 | **COMPLETE — PASS.** DOC-001 p4: 165/1312=12.58%→13%, 117/1312=8.92%→9%, and 24/1312=1.83%→2%. |
| N008 | **COMPLETE — PASS.** DOC-001 pp1,4,7-8: baseline eGFR 85.8 (SD 22.1) has matched value/unit across occurrences. |
| N009 | **COMPLETE — PASS.** DOC-001 pp1,2,4-5: 46% women and 31% minority are compatible with the displayed cell data/nonmissing definitions; no single common denominator is claimed for all Table 1 items. |
| N010 | **COMPLETE — PASS.** DOC-001 p5: Table 1 values use stated nonmissing-response percentages; category and unit labels agree with each row. |
| N011 | **COMPLETE — PASS.** DOC-001 p5: six race-category counts total 361, 327, 284, and 314 respectively. |
| N012 | **COMPLETE — PASS.** DOC-001 p5: diabetes-duration category totals are 369, 332, 288, and 319, exactly one below each randomized cell; stated nonmissing denominators explain this. |
| N013 | **COMPLETE — PASS.** DOC-001 p5: 25(OH)D category totals 355,317,274,311 are compatible with nonmissing-response denominators and their printed percentages. |
| N014 | **COMPLETE — PASS.** DOC-001 pp1-2: D3 2000 IU/d, omega-3 1 g/d (EPA 465 mg+DHA 375 mg), and nonstudy D3 <=800 IU/d retain coherent units; `465+375=840 mg` is compatible with a 1-g capsule containing other constituents. |
| N015 | **COMPLETE — PASS.** DOC-001 p3: N=1320, 80% power, 2.3 mL/min/1.73 m2, 80% return, and two-sided alpha .05 are a stated design calculation; no observed-result denominator is implied. |
| N016 | **COMPLETE — PASS.** DOC-001 p4: 85.8→73.5 gives displayed change about -12.3 using marginal means, whereas modelled full-population change is -12.7; the supplied mixed-model/imputation definition means these need not equal simple subtraction. Units and time ordering are coherent. |
| N017 | **COMPLETE — PASS.** DOC-001 p8 Table 2: D3 group Ns 701/607, 531/459, 496/438 and means/changes/differences are internally coherent to displayed rounding. Cross-display check is recorded separately at N020/N021. |
| N018 | **COMPLETE — PASS.** DOC-001 p8 Table 2: omega group Ns 657/651, 499/491, 472/462 and displayed means/changes/differences are coherent to displayed rounding. |
| N019 | **COMPLETE — PASS.** DOC-001 pp1,2,4,8: matched primary-results values (including 0.9 contrasts and CIs) agree after stated rounding. |
| N020 | **COMPLETE — PASS.** DOC-001 pp7-8: Figure 2 D3 eGFR counts 607/459/438 placebo and 701/531/496 active match Table 2. |
| N021 | **COMPLETE — OBSERVATION NUM-OBS-001.** Exact mismatch is documented below. |
| N022 | **COMPLETE — OBSERVATION NUM-OBS-002.** Exact mismatch is documented below. |
| N023 | **COMPLETE — PASS.** DOC-001 p4: adherence labels are percentages at distinct time points; biomarker values retain their stated ng/mL and percent units. No count denominator is printed for direct reconstruction. |
| N024 | **COMPLETE — PASS.** DOC-001 p4: 80+11+80=171 component occurrences versus 164 composite participants is explicitly compatible with overlapping components; it is not a failed total. |
| N025 | **COMPLETE — PASS.** DOC-001 p4: ACR 5.1 to 9.2 mg/g is about 1.80-fold between y2/y5; “approximately 3-fold” explicitly refers to baseline-to-y5, whose baseline value is not printed in that sentence. No incompatible same-time comparison. |
| N026 | **COMPLETE — PASS.** DOC-001 pp1,4: kidney stones `32+26=58`; GI bleeding `28+17=45`. |
| N027 | **COMPLETE — PASS.** DOC-001 p9: Table 3 D3 event counts, per-100-person-year rates, rate differences, and Cox HR columns have distinct labelled measures. Printed rate differences reconcile to displayed precision (2.5-2.7=-0.2; 1.6-1.7=-0.1; 4.4-3.3=1.1). |
| N028 | **COMPLETE — PASS.** DOC-001 p9: omega rate differences reconcile at displayed precision (2.7-2.5=0.2→0.3 with unrounded rates; 1.6-1.6=0.0; 4.0-3.7=0.3). Counts are not treated as rates. |
| N029 | **COMPLETE — PASS.** DOC-001 p9 footnote: eGFR outcome population excludes 4 baseline-eGFR missing and ACR population excludes 1 baseline-ACR missing; this is consistent with Figure 1 and denominators. |
| N030 | **COMPLETE — PASS.** DOC-001 p8 Figure 3: all subgroup Ns, signs, SDs, interaction labels, and factorial omega strata are coherent; subgroup categories are not mutually exhaustive where a missing category is possible. |
| N031 | **COMPLETE — PASS.** DOC-001 p9 Figure 4: all subgroup Ns, signs, SDs, interaction labels, and factorial D3 strata are coherent under the printed definitions. |
| N032 | **COMPLETE — PASS.** DOC-001 pp8-9 captions: adjusted active-minus-placebo change from baseline to y5, BMI kg/m2, and directions are consistently labelled. |
| N033 | **COMPLETE — PASS.** DOC-001 pp3,5,7: 0.75/year ×5=3.75/5y; all comparison quantities preserve mL/min/1.73 m2 and period labels. |
| N034 | **COMPLETE — PASS.** DOC-001 pp3-4,9: thresholds preserve units and logical criteria (ACR doubling plus final >=30 mg/g); post-hoc >=30% threshold is separately labelled. |
| N035 | **COMPLETE — PASS.** DOC-001 pp3-4: full M=20 imputed population and n=932 complete-case population are explicitly distinct, not competing denominators. |
| N036 | **COMPLETE — PASS.** DOC-002 pp11-16: planned factorial doses and target populations are internally unit-consistent; protocol plans are not compared as observed results. |
| N037 | **COMPLETE — PASS.** DOC-002 pp12-14: projected `40,000×50%=20,000`; blocks of 8 with two per factorial cell are arithmetically coherent. |
| N038 | **COMPLETE — PASS.** DOC-002 pp15-16: two 5-mL cryovials have 10-mL capacity and six 2-mL aliquot vials have 12-mL aggregate capacity; the text does not state every aliquot vial is filled to capacity (and precipitation is removed before aliquoting), so capacity is not an asserted volume total. Dose conversions are explicitly supplied. |
| N039 | **COMPLETE — PASS.** DOC-002 p17: formulae distinguish percent ACR change, absolute eGFR change, and composite thresholds; units/scales are coherent. |
| N040 | **COMPLETE — PASS.** DOC-002 pp19-20: each listed effect-power pair is a prospective calculation; monotonic power ordering (81→>99%, 71→97%) follows increasing effect size. |
| N041 | **COMPLETE — PASS.** DOC-002 pp32-33: addendum switches planned primary time contrast/definitions explicitly; 1058 is 80% of about 1323, compatible with the stated rounded 80% design figure and not an observed trial total. |
| N042 | **COMPLETE — PASS.** DOC-003 pp2-4: calibration multiplier is printed as 5.49/5.961, and the regression/units are calibration relations rather than participant outcomes. |
| N043 | **COMPLETE — PASS.** DOC-003 p6 eTable 1: each overall adherence numerator equals active+placebo: e.g., D3 642+566=1208, 573+506=1079, 378+331=709; omega 608+600=1208, 537+540=1077, 368+353=721. Percentages are among questionnaire responders, so they are not tested against randomized 1312. |
| N044 | **COMPLETE — PASS.** DOC-003 p7 eTable 2: for every displayed medication/time, the all-group count equals either factorial active+placebo partition (e.g., biguanides baseline 469+420=889 and 446+443=889) and percentages use stated nonmissing N=1312/988/916. Overlapping medication classes are not summed. |
| N045 | **COMPLETE — PASS.** DOC-003 p8 eTable 3: all-group counts equal the corresponding active+placebo partition (e.g., ACEi baseline 311+254=565 and 284+281=565); combination ACEi/ARB is not required to equal ACEi+ARB because overlap is possible. Denominators 1312/988/916 are stated. |
| N046 | **COMPLETE — PASS.** DOC-003 p9 eTable 4: complete-case D3 N495+437=932 and omega N470+462=932; y5 counts retain the complete-case definition. Mean-change values and `.87` active-placebo difference agree to rounding. |
| N047 | **COMPLETE — PASS.** DOC-003 p9 eTable 4: omega N470+462=932; y5 change -12.4 versus -12.4 and difference `.09` are modelled/rounded values, not an arithmetic contradiction. |
| N048 | **COMPLETE — PASS.** DOC-003 p10 eTable 5: adherent D3 baseline 544+485=1029 and y5 461+404=865; different time-point availability is labelled. Means/changes/difference `.89` agree to rounding. |
| N049 | **COMPLETE — PASS.** DOC-003 p10 eTable 5: adherent omega baseline 517+513=1030 (one differs from 1031 overall adherence count because this is a distinct eGFR-available population); y5 438+426=864. No incompatible common denominator is asserted. |
| N050 | **COMPLETE — PASS.** DOC-003 p11 eTable 6: D3 ACR N702+609=1311 at baseline, y5 505+440=945; ratios and active:placebo effect use geometric/adjusted scales and are not simple mean differences. |
| N051 | **COMPLETE — PASS.** DOC-003 p11 eTable 6: omega ACR baseline 658+653=1311 and y5 478+467=945; ratio labels/scales coherent. |
| N052 | **COMPLETE — PASS.** DOC-003 p12 eTable 7: available-case N504+440=944 (D3) and 477+467=944 (omega); 1311 baseline and 991 y5 samples do not need to equal the available-pair analysis population. |
| N053 | **COMPLETE — PASS.** DOC-003 p13 eTable 8: adherence-restricted ACR totals/attrition are explicitly time-specific; all effects retain ratio scale and mg/g unit. |
| N054 | **COMPLETE — PASS.** DOC-003 p14 eTable 9: UTI-visit exclusion yields separately defined time-specific Ns; effects remain ratios, not counts/rates. |
| N055 | **COMPLETE — PASS.** DOC-003 p15 eTable 10: D3 event counts, rates per 100 person-years, incidence-rate differences, and HRs are distinct columns; printed rate differences are compatible with unrounded rates. |
| N056 | **COMPLETE — PASS.** DOC-003 p15 eTable 10: same checks pass for omega outcomes; stated exclusions prevent using all 1312 as every outcome denominator. |
| N057 | **COMPLETE — PASS.** DOC-003 p16 eTable 11: for every safety row, D3 active+placebo equals omega active+placebo (e.g., hypercalcemia 9+10=14+5=19; stones 32+26=31+27=58; GI bleed 19+26=28+17=45). Counts are persons with >=1 report, not mutually exclusive outcome totals. |
| N058 | **COMPLETE — PASS.** DOC-003 p17: r=-.05 and r=-.02 have correct correlation scale and no supplied N/P/model for further reconstruction. |
| N059 | **COMPLETE — OBSERVATION NUM-OBS-003.** Exact participant-count-column identity mismatch is documented below. |
| N060 | **COMPLETE — OBSERVATION NUM-OBS-004.** Exact participant-count-column identity mismatch is documented below. |
| N061 | **COMPLETE — PASS.** DOC-004 p1 is an administrative data-sharing statement; no quantitative trial result requires reconciliation. |
| N062 | **COMPLETE — PASS.** DOC-002 p23: z=3 corresponds to two-sided P about .0027 under standard normal rounding; it is a planned monitoring rule. |

## S-relationship numeric implications

All listed S relationships were checked alongside their linked Ns. `S001-S020` and `S024-S038` have complete numeric implications; `S021-S023` and `S039` are prospective/statistical-definition relations with no additional observed count identity. The following cross-links were specifically completed: `S001/S002↔N017/N018/N019/N020/N021`; `S006-S012↔N027-N029`; `S025-S028↔N046-N049`; `S029-S033↔N050-N054`; `S034-S035↔N055-N056`; and `S037-S038↔N059-N060`.

The printed point estimates lie within their printed intervals, interval endpoints are ordered, and all null-crossing patterns match the non-significant P-value labels where a compatible model is supplied. No `P=0` or `p=.000` display occurs; therefore no display-zero record is applicable. Statistical inference beyond the source-supplied model is intentionally deferred to the statistical-review lanes.

## Lane observations for candidate merging (no C IDs)

### NUM-OBS-001 — Figure 2 omega eGFR participant counts conflict with Table 2

- **Exact evidence:** DOC-001 [Figure 2, PDF p7](../../../jama_de_boer_2019_oi_190122.pdf#page=7) prints omega-3 placebo `607/459/438` and omega-3 active `701/531/496` at baseline/year 2/year 5. DOC-001 [Table 2, PDF p8](../../../jama_de_boer_2019_oi_190122.pdf#page=8) prints omega placebo `651/491/462` and omega active `657/499/472` for the same outcome/time points.
- **Rule/calculation:** matched factorial omega comparison, outcome (eGFR), and time points require identical contributing-count sequences. They differ at every displayed time point; integer tolerance 0.
- **Direct observation vs inference:** direct observations are the two printed sequences. The inferred concern is a cross-display numeric inconsistency, not a calculation from unreported data.
- **Alternatives:** Figure 2 may have retained the vitamin-D count series, or a panel/table population definition may be unstated; the caption describes both as contributing participants and supplies no alternative population definition.
- **Quality-control relevance:** a reader could attach the plotted omega distributions to the wrong sample sizes.
- **Exact human question:** Which omega-3 eGFR contributing counts are intended for Figure 2, and should the figure panel be corrected or qualified against Table 2?

### NUM-OBS-002 — Figure 2 omega urine-ACR participant counts conflict with eTable 6

- **Exact evidence:** DOC-001 [Figure 2, PDF p7](../../../jama_de_boer_2019_oi_190122.pdf#page=7) prints omega placebo `609/463/440` and omega active `702/529/505` at baseline/year 2/year 5. DOC-003 [eTable 6, PDF p11](../../../joi190122supp2_prod.pdf#page=11) prints omega active `658/502/478` and placebo `653/490/467` for corresponding ACR time points; its arm totals are 1311/992/945.
- **Rule/calculation:** matched omega comparison, ACR outcome, and time points require the same arm-specific contributor counts unless a different analysis population is stated. The figure repeats the D3 ACR count sequences, whereas the table supplies different omega sequences; integer tolerance 0.
- **Direct observation vs inference:** direct observations are printed counts; inference is the unmatched-result identity. The figure caption supplies no distinct population definition.
- **Alternatives:** the panel could have a deliberate but unstated different set of contributors, or it may contain copied D3 counts.
- **Quality-control relevance:** incorrect arm/time denominators can affect interpretation of plotted ACR distributions.
- **Exact human question:** What omega-3 ACR contributor counts and population definition were intended for Figure 2, and are its printed counts copied from the vitamin-D panel?

### NUM-OBS-003 — eFigure 2 participant counts map to the opposite vitamin-D arms

- **Exact evidence:** DOC-003 [eFigure 2, PDF p18](../../../joi190122supp2_prod.pdf#page=18) labels columns `Placebo` N=703 and `Active intervention` N=609, with overall change ratios 3.02 and 2.97. DOC-003 [eTable 6, PDF p11](../../../joi190122supp2_prod.pdf#page=11) identifies vitamin-D active baseline N=702, y5 ratio 2.97 and placebo N=609, y5 ratio 3.02.
- **Rule/calculation:** randomized vitamin-D active totals `370+333=703` and placebo totals `289+320=609`; the figure places these Ns under the opposite headings. Separately, its `3.02` placebo and `2.97` active changes agree with eTable 6 under the printed headings.
- **Direct observation vs inference:** the direct observation is the overall and nested N-column mismatch. A transposition limited to participant counts is a plausible inference; reversal of headings, changes, or forest estimates is not established.
- **Alternatives:** only the N columns may be transposed. The active measured baseline N differs by one from randomized N=703 because eTable 6 excludes one baseline-ACR-missing participant.
- **Quality-control relevance:** an evidence extractor could attach subgroup participant counts to the wrong vitamin-D arm.
- **Exact human question:** Should only eFigure 2's N columns be exchanged, or do any subgroup changes or plotted estimates also require remapping?

### NUM-OBS-004 — eFigure 3 participant counts map to the opposite omega-3 arms

- **Exact evidence:** DOC-003 [eFigure 3, PDF p19](../../../joi190122supp2_prod.pdf#page=19) labels `Placebo` N=659 and `Active intervention` N=653, with overall ratios 3.05 and 2.94. DOC-003 [eTable 6, PDF p11](../../../joi190122supp2_prod.pdf#page=11) identifies omega active baseline N=658, y5 ratio 2.94 and placebo N=653, y5 ratio 3.05.
- **Rule/calculation:** randomized omega-3 active totals `370+289=659` and placebo totals `333+320=653`; the figure places these Ns under the opposite headings. Separately, its `3.05` placebo and `2.94` active changes agree with eTable 6 under the printed headings.
- **Direct observation vs inference:** the direct observation is the overall and nested N-column mismatch. A count-only transposition is plausible; reversal of headings, changes, or forest estimates is not established.
- **Alternatives:** only the N columns may be transposed. The one-person 659/658 difference is compatible with randomized versus measured baseline availability but does not resolve the N mapping.
- **Quality-control relevance:** an evidence extractor could attach subgroup participant counts to the wrong omega-3 arm.
- **Exact human question:** Should only eFigure 3's N columns be exchanged, or do any subgroup changes or plotted estimates also require remapping?

## Limitations

The source does not provide individual-level data, exact person-time totals, full unrounded estimates, every questionnaire-response denominator by arm/time, or all graphical forest-plot coordinates. Therefore rate/count checks used the supplied rate labels and printed precision; percentages with explicitly nonmissing/questionnaire denominators were not forced onto randomized N; and graphical results were checked only to the legible printed labels, Ns, ratios, and interaction P values. These limitations do not affect the four direct printed cross-display observations above.
