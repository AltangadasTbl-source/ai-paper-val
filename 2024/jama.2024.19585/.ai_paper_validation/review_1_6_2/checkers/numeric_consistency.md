# Numeric consistency review

Runtime agent: 01a129b5-e322-7ff1-a198-947ffd0e507e. Model/effort:gpt-6.1-sol/medium; fresh mandatory numeric reviewer. Complete scope: N001–N096 and N201–N216 (112 numeric families); every constituent count/percentage in main Tables1–3, Figure1, supplement eTables3–5,8–12, missingness displays and related narrative. S-attached supplementary count matrices cover270 fraction cells. Full results: [numeric inventory](../relationships/numeric_relationship_inventory.md). Scope and review contract were read completely. No old checker/report/candidate conclusions or external source were used.

Counts, flow partitions, percentages and matched analysis populations reconcile. Three inferential observations encountered during numeric review qualify under the always-register rule and are emitted here even where a statistical checker may independently report them. Independent screening determines consolidation. Findings:3; excluded apparent observations:5. No scientific coverage gap.

## Findings

### F-NUM-001

Title: significant P values accompany null-containing intervals in two zero-control-event symptom-specific rows.

- **Exact source locations and roles:** REPORT [DOC-003 p.14, eTable10, symptom-specific intervention, SSPedi≥1, tingly/numb and hunger rows](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14); REPORT [DOC-003 p.15, footnote b](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15); REPORT [DOC-003 p.22, eMethods binary analyses](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22). Corroborating main narrative:N085/N086 at DOC-001 pp5–6. Inventory relationships:S116,S123,N085,N086.
- **Printed inputs:** neuropathy6/57(10.5%) vs0/70(0%), effect17.8,95%CI(0.98,323.1),P=.007; hunger6/111(5.4%) vs0/130(0%), effect16.08,95%CI(0.9,288.74),P=.009. Footnote b says P values from mixed/fixed logistic regression; eMethods names ORs, with mixed-model fallback to fixed treatment-only logistic regression.
- **Rule and reproduced calculation:** the95%CI contains OR null1 in both rows (0.98<1<323.1;0.9<1<288.74), while both printed P values are<.05. Numerator percentages separately reconcile (6/57=10.5263%;6/111=5.4054%). Point estimates lie inside intervals. The two conflicts follow the same rule in zero-control-event rows and are consolidated as one pattern.
- **Recomputed interval/relative discrepancy:** numerical interval propagation is not the decision rule for Route A category1; no estimate is recomputed from an assumed model. Printed P half-unit intervals [.0065,.0075] and[.0085,.0095] remain below.05; lower-limit half-unit intervals [.975,.985] and[.85,.95] remain below1. Relative discrepancy:not applicable to categorical CI/P compatibility.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type / all relationships:** S_W / S_W.
- **Qualifying route:** Route A, category1.
- **Affected result or extracted value:** whether symptom-specific intervention differs for symptomatic neuropathy and hunger, and the corresponding95%CIs/P values taken into extraction.
- **Why context does not resolve it:** Route A category1 applies even if inferential procedures differ. The display supplies95%CIs and P values for the same printed contrasts; it does not identify a row-specific distinction accounting for null containment.
- **Alternatives:** interval and P may use distinct small-sample/sparse-event procedures, or distinct model fits; this is a source-grounded possibility from the mixed/fixed fallback, not an assumed explanation. Counts alone cannot choose the intended interval or test.
- **Exact human question:** Which models and inferential procedures generated the95%CIs and P values for these two rows, and should each null-containing interval and significant P value be read as coming from the same analysis?

### F-NUM-002

Title: sadness any-intervention interval excludes the null with printed P=.05.

- **Exact source locations and roles:** REPORT [DOC-003 p.13, eTable10, Any Intervention, sad/disappointed, All Participants](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13); REPORT [DOC-001 p.4, Statistical Analysis significance rule](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4); REPORT [DOC-001 p.5, corresponding result narrative](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5). Relationships:S115,S035,N078.
- **Printed inputs:**52/220(23.6%) vs82/224(36.6%),effect0.51,95%CI0.26–0.99,P=.05. Main text calls this significantly more common at usual-care sites; Statistical Analysis defines P<.05 as significant.
- **Rule and reproduced calculation:**0.26≤0.51≤0.99<1, hence the95%CI excludes OR null1, whereas the printed P=.05 does not meet the stated P<.05 rule. Percentages separately reconcile:52/220=23.6364%,82/224=36.6071%.
- **Recomputed interval/relative discrepancy:** no model estimate is recomputed; category1 excludes the numeric display-precision screen. The upper CI rounding interval[.985,.995] remains below1. P rounding interval[.045,.055] straddles.05 and is recorded as an alternative, not grounds to suppress a reproduced printed CI/P conflict. Relative discrepancy:not applicable.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type / all relationships:** S_W / S_W. Main text corroborates the clinical comparison and threshold, rather than establishing a separate conflicting report-to-report relationship.
- **Qualifying route:** Route A, category1.
- **Affected result or extracted value:** significance reading for any intervention for sadness, and its interval/P value extracted from eTable10.
- **Why context does not resolve it:** Route A category1 requires registration of the printed interval/P reading. Narrative implies significance but does not disclose an unrounded P or a distinct test.
- **Alternatives:** unrounded P could be just below.05 and print as.05; CI and P could use different procedures. Neither alternative supplies the exact value in the source.
- **Exact human question:** What is the unrounded P value and CI/test procedure for the all-participant sadness any-intervention contrast, and how should its printed P=.05 be read with the upper95%CI limit0.99 and stated P<.05 rule?

### F-NUM-003

Title: emergency-department absolute-effect credible interval contains zero alongside significant adjusted P.

- **Exact source locations and roles:** REPORT [DOC-001 p.9, Table3 emergency-department row and footnote b](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=9); REPORT [DOC-001 p.1, ED result](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=1). Relationships:N091,S027,S036.
- **Printed inputs:** mean.77(1.12) vs.45(.81),rates9.6 vs5.6 per100patient-weeks; absolute rate difference3.38(95%CrI−0.57,7.94);RR1.72(95%CI1.03,2.87),adjustedP=.04. Footnote b distinguishes marginalization over treatment+site model for absolute differences from treatment+site+two-strata model for RR.
- **Rule and reproduced calculation:** absolute-effect95%interval contains null0, while printed adjustedP=.04 is below.05. RR interval excludes1 and agrees with the P. Direction of both estimates is positive; no arithmetic claim equates3.38 with9.6−5.6.
- **Recomputed interval/relative discrepancy:** no assumed-model effect is recomputed; category1 categorical compatibility applies. Absolute lower-limit interval[−.575,−.565] is negative and upper interval[7.935,7.945]positive. P half-unit interval[.035,.045] remains significant. Relative discrepancy:not applicable.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type / all relationships:** S_W / S_W.
- **Qualifying route:** Route A, category1.
- **Affected result or extracted value:** interval/test significance reading for emergency-department encounter effects, especially absolute rate difference versus adjusted rate ratio.
- **Why context does not resolve it:** Route A category1 expressly requires registration even when the interval and P are attributed to different analyses; the supplied footnote is therefore preserved as an alternative. It does establish the model distinction and must accompany human review.
- **Alternatives:** the absolute credible interval and frequentist adjusted P address different fitted models and inferential conventions, as directly stated in footnote b. That disclosed distinction could explain the readings; no preferred analysis is proposed.
- **Exact human question:** Should the adjusted P be read exclusively with the adjusted RR, and how should the null-containing absolute-rate-difference credible interval be interpreted alongside the significant RR result?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p2 pathway adaptation vs REPORT DOC-003 p6 eTable3 | Main reject6.4% vs142/1350=10.5185%; keep551/1350=40.8148% and adapt657/1350=48.6667% match. Half-unit rejection inputs across10sites give[137/1355,147/1345]×100=[10.1107,10.9294]%; printed6.4±.05 leaves gap3.6607 points,relative.5720. This comparison of implementation descriptive adaptation choices changes no primary/key-secondary result, analysis population or decision rule. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 pp13–15 eTable10 heading vs REPORT DOC-003 p22 eMethods | Generic heading “Difference” accompanies logistic estimates; eMethods explicitly identifies odds ratios. For pain-specific severe7/11 vs1/11, crude OR(7×10)/(4×1)=17.5 matches17.50 whereas risk difference54.545 percentage points does not. Logistic/positive-ratio interval context makes the measure immediately identifiable. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p8 Figure2 caption vs REPORT DOC-001 p7 baseline columns | Caption lists198/209 without separate baseline Ns, while baseline table reports216/213. Caption counts are exact week8 counts; per-time contributor/caption comparison changes no primary result or analysis population, and bars lack exact printed segments. | PERIPHERAL_COMPARISON |
| REPORT DOC-003 p11 eTable8 vs REPORT DOC-001 p7 Table2 | Crude severe symptom risk differences can differ from mixed-model absolute differences (e.g.taste11/198−25/209=−6.4069percentage points vs model−5.7). eTable8 expressly estimates mixed-model effects; “unadjusted” is not a statement that effects are crude margins. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p7 Table2 individual-symptom rows | Recomputing binary severe-symptom ORs from score3–4 counts can differ from ordinal ORs using all0–4 categories. Source methods and footnotes expressly distinguish these quantities. | MODEL_VERSUS_CRUDE |

All other reconciled checks are in the numeric inventory, not exclusions. No always-register interval/P observation encountered here is placed in the excluded table.

## Evidence and limitations

Direct fresh layout confirmation: DOC-003 pp13–15 (eTable10-direct.txt),pp6–8(eTables3-5-direct.txt),DOC-001 p9(Table3-direct.txt),under preprocessing/numeric_check/,using Poppler pdftotext26.01.0 CPU. No rendering/OCR or fallback was needed. Source files and reused assets were preserved. All112 numeric families and supplementary count cells were checked. Exact Figure2 segment percentages and unique encounter totals/SDs from open-ended upper bins are unavailable by display design; no scientific scope omitted. Models cannot be numerically regenerated without raw data, and their stated identities were respected.
