# Independent Statistical Consistency Pass 1

**Explicit PASS_1_COMPLETE relationship register:** S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S300 S301 S302 S303 S304 S305 S306 S307 S308 S309 S310 S311.

**Scope complete:** S001-S053 and S300-S311 (65 of 65 relationships).  
**Source basis:** supplied DOC-001 through DOC-004 PDFs and current fresh evidence assets only.  
**Status:** every relationship was checked; each remains **Pending Human Adjudication** if it generated a provisional candidate. No severity, validity, correction, acceptance, or exclusion determination is made here.

## Checks completed

- Point-estimate containment and CI endpoint ordering were checked for every reported RD, OR, beta, and displayed CI in Table 2, Table 3, Figure 3, eTables 1-2 and 5-7, and the mapped narrative repetitions. All printed intervals were ordered and contained their associated printed estimate.
- Sign/direction and effect-measure labels were checked only within a matched model/contrast. OR direction and intervention-minus-control marginal-difference labels are internally coherent where defined. Crude percentages and medians were not used to reject adjusted estimates.
- Cross-location repetitions were compared after matching outcome, model, contrast, and precision. The exact discrepancies below were retained rather than resolved.
- No relationship supplied all inputs required for a new test-statistic, SE, P-value, or multiplicity calculation beyond stated O'Brien-Fleming threshold pairs. No unsupported inferential reconstruction was performed.
- No literal display-zero P value occurs in the assigned relationships; no display-zero candidate was emitted.

## Provisional candidates for coordinator registration

### SP1-001 — In-hospital beta-blocker adjusted-risk-difference CI differs between Table 2 and narrative

**Category:** Statistical reporting inconsistency  
**Exact source locations:** DOC-001, `jama_huffman_2018_oi_170166.pdf` PDF p.6, Table 2 and results narrative on the same page.  
**Direct observation:** Table 2 reports adjusted risk difference 6.25% (95% CI, 4.10% to 8.40%) and OR 1.46 (1.29-1.65). The narrative describes the same comparison as 6.25% (95% CI, 4.10%-8.10%) and OR 1.46 (1.29-1.65).  
**Consistency rule:** Same outcome, contrast, adjusted model, point estimate, and lower CI endpoint should retain the same upper CI endpoint across a table and its narrative repetition.  
**Calculation:** Printed upper endpoints are 8.40% versus 8.10%, a 0.30-percentage-point difference.  
**Alternative source-grounded interpretation:** One occurrence could be a transcription/rounding error; the supplied source does not identify a controlling version.  
**Human question:** Which upper endpoint is supported by the final analysis output?  
**Status:** Pending Human Adjudication.

### SP1-002 — Discharge beta-blocker adjusted estimates differ between Table 2 and narrative

**Category:** Cross-document numeric inconsistency  
**Exact source locations:** DOC-001 PDF p.6, Table 2; DOC-001 PDF p.7, results narrative.  
**Direct observation:** Table 2 gives adjusted risk difference 6.69% (95% CI, 4.43%-8.95%) and OR 1.48 (1.30-1.68). The narrative gives 6.63% with the same CI and OR 1.47 with the same CI for discharge beta-blocker use.  
**Consistency rule:** A narrative repetition of the same outcome, contrast, CI, and adjusted model should reproduce its point estimates at the displayed precision or identify a different analysis.  
**Calculation:** RD differs by 0.06 percentage points and OR by 0.01; both CIs are identical as printed.  
**Alternative source-grounded interpretation:** Both narrative values may be unreported higher-precision values rounded differently, although the identical displayed CIs and lack of a distinct model label leave that unresolved.  
**Human question:** Were the narrative and Table 2 values derived from different precision/model outputs, or is one a reporting transcription?  
**Status:** Pending Human Adjudication.

### SP1-003 — eTable 1 comparator footnote conflicts with its displayed follow-up-status columns

**Category:** Measure, label, or scale inconsistency  
**Exact source locations:** DOC-004, `joi170166supp3_prod.pdf` PDF p.17, eTable 1 header and footnote a.  
**Direct observation:** The columns are “Complete Follow Up” (n=21,079) and “Missing Follow Up” (n=295), while footnote a says “Difference = intervention minus control.” The tabulated age difference -0.6 matches 60.0 minus 60.6 (missing minus complete), illustrating the displayed column comparison rather than the stated intervention/control labels.  
**Consistency rule:** A difference-label footnote must name the groups displayed in the associated comparison columns.  
**Calculation:** For age, 60.0 - 60.6 = -0.6, matching the printed difference; intervention/control group labels are absent from this table.  
**Alternative source-grounded interpretation:** The footnote may have been carried over from eTable 2; the source does not state whether every eTable 1 difference is defined as missing minus complete.  
**Human question:** What comparator and sign convention were used for each eTable 1 difference?  
**Status:** Pending Human Adjudication.

### SP1-004 — Reported prespecified age-subgroup cut points differ from the supplied SAP

**Category:** Cross-document numeric inconsistency  
**Exact source locations:** DOC-003, `joi170166supp2_prod.pdf` PDF p.7, section 7.5.2; DOC-001 PDF p.3 (states results reported by prespecified subgroups) and PDF p.9, Figure 3.  
**Direct observation:** The SAP lists age “<65 years and >65 years” as an a-priori participant-level subgroup. Figure 3 reports three age strata: <50, 50-69, and >=70, within results described as prespecified subgroups.  
**Consistency rule:** When final results describe a subgroup analysis as prespecified, its displayed numeric cut points should match the supplied prespecification or the source should identify an amendment/redefinition.  
**Calculation:** The supplied boundaries differ: 65 versus 50 and 70 years, with a two-group planned division versus a three-group reported division.  
**Alternative source-grounded interpretation:** An unprovided amendment or a broader prespecified plan could authorize the final categories; the supplied package does not provide either.  
**Human question:** Were the Figure 3 age categories prespecified in an amendment or separate analysis plan, and if so where?  
**Status:** Pending Human Adjudication.

### SP1-005 — “Optimal in-hospital medication” uses non-identical component labels across final tables

**Category:** Measure, label, or scale inconsistency  
**Exact source locations:** DOC-001 PDF p.3 and p.7 Table 3 footnote c; DOC-004 PDF p.21 eTable 5 footnote c; DOC-004 PDF p.22 eTable 6 footnote b.  
**Direct observation:** DOC-001/Table 3 and DOC-004/eTable 5 define the named composite with aspirin, an ADP-receptor antagonist, anticoagulant, and beta-blocker. DOC-004/eTable 6 labels the same named composite with aspirin, an ADP-receptor antagonist, heparin, and beta-blocker.  
**Consistency rule:** Repeated use of the same named composite outcome across final-result tables should retain an identical component definition or explicitly distinguish a narrower/different construct.  
**Calculation:** “Heparin” replaces the broader displayed term “anticoagulant”; no source statement establishes that the eTable 6 interaction outcome is restricted to heparin or otherwise identical.  
**Alternative source-grounded interpretation:** Heparin may have been the only anticoagulant used in the analyzed data, making the terms extensionally equivalent; that fact is not supplied.  
**Human question:** Does eTable 6 analyze the same in-hospital medication composite as Table 3/eTable 5, and what exact anticoagulant component was used?  
**Status:** Pending Human Adjudication.

## Limitations

The package does not state all model details needed to derive independent P values, SEs, test statistics, or interval transformations. Diagnostic arithmetic was limited to direct label/value comparisons. The observed discrepancies require mechanical evidence recheck before stable C-ID registration.
