# Support B statistical relationships

| ID | Statistical relationship / source | Status for later statistical passes |
|---|---|---|
| BS001 | SAP pp. 120-121: non-inferiority BVM-TI margin -0.01; H0 <=-0.01, H1 >=-0.01; two-sided alpha .05. | Defined; compare published primary CI to this rule. |
| BS002 | SAP p. 124: primary analysis 95% two-sided CI of BVM-TI; lower bound >-0.01 accepts non-inferiority; exact CI if necessary; ITT, PP and AT. | Defined; main published one-sided 97.5% form is mathematically corresponding to the one-sided decision boundary. |
| BS003 | SAP pp. 120, 123: planned interim analyses cancelled due to rapid enrolment; only final analysis and no multiplicity adjustment; primary missing=worst-case no success, secondary no imputation. | Defined; no directly conflicting result in shard. |
| BS004 | SAP pp. 123-124: categorical values as absolute/relative frequency based on nonmissing values, one-decimal rounding; secondary proportions chi-square with 95% CIs for OR/difference; t test/Mann-Whitney for quantitative criteria. | Defined. |
| BS005 | SAP p. 124: safety analysis ITT and AT; dichotomous endpoints chi-square or Fisher exact; quantitative outcomes t test/Mann-Whitney. | Defined; supports interpretation of main Table 3 footnote. |
| BS006 | DOC-003 p. 3 post-hoc ECMO/donation-excluded result: P=.63; difference 0.4; 95% CI [-2.2,1.3]. | CI includes zero; P is coherent at displayed precision. |
| BS007 | DOC-003 p. 3 post-hoc reclassification result: P=.31; difference 0.9; 95% CI [-0.9,2.7]. | CI includes zero; P is coherent at displayed precision. |
| BS008 | SAP p. 122 safety endpoint list predates protocol-v2 additions of aspiration pneumonia/BVM failure (pp. 114-116). | VERSIONED_DEFINITION_DIFFERENCE; not a statistical inconsistency without evidence of the final analysis set/definition. |
| BS009 | DOC-002 rendered p.103 IDS bands: 0<IDS<=5 slight; IDS>5 moderate-major; IDS=infinity impossible. Main Table 3 calls >5 difficult. | The scale definitions agree and explicitly categorize score 5 as slight difficulty; no candidate. |

All BS relationships are mapped for statistical pass 1 and pass 2. No display-zero P value appears in this shard, and no `DISPLAY_ZERO_NOT_CANDIDATE` record is needed.
