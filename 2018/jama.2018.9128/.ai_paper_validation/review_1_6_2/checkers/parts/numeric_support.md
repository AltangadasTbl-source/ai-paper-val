# Numeric consistency support shard

Runtime: root/numeric_support_checker; gpt-6.1-sol; medium; FRESH_SPAWN. Scope and all calculations are recorded in relationships/parts/numeric_support.md. Seventy-four relationships N201–N274 checked, one finding, two excluded observations. No cross-document comparison or interval-versus-P compatibility is duplicated. Supplied source PDFs are authoritative.

### F-NUM-201

**Title:** Original protocol cohort-size and regional-size counts do not reconcile with its own allocation arithmetic.

**Compared locations and document roles:** PLAN [DOC-002 physical p36 lines1255–1258, Study Design](../../../../joi180075supp1_prod.pdf#page=36), continuing PLAN [physical p37 line1259](../../../../joi180075supp1_prod.pdf#page=37); PLAN [physical p13 lines468–473, cohort allocation](../../../../joi180075supp1_prod.pdf#page=13); PLAN [physical p39 lines1343–1349, clustering inputs](../../../../joi180075supp1_prod.pdf#page=39). All are in the original protocol, not a comparison between amended versions.

**Relationship:** N201; P_P; all relationships P_P. **Focus area:** D (planned sample size and population allocation), also A (cohort counts). **Proposed review domain:** plan_material.

**Printed inputs:** p36 says “600 dyads per cohort (300 per region/site)” and p37 completes “a total sample size of 600.” p13 states three cohorts, 200 dyads each, 100 randomized per arm and 50 per intervention or control facility per cohort. p39 independently states three waves of 200, 100 per arm, 50 per community recreation center per wave.

**Rule and calculation:** A cohort containing two arms of100 has200 dyads, not600. Two regions each containing50 intervention plus50 control dyads have100 per region/cohort, not300. Across three cohorts the total is600. Direct displayed copies of the cohort count have intervals600±.5=[599.5,600.5] and200±.5=[199.5,200.5];gap399;relative discrepancy399/600=.665. For regional count, (50±.5)+(50±.5) gives[99,101], while300±.5 gives[299.5,300.5];gap198.5;relative discrepancy198.5/300=.661667. Both exceed.05. These differences concern the units to which printed counts apply, rather than the approximate17-family sessions.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Planned dyads per cohort and per region/site, inputs used to understand allocation, clustering and the target trial population.

**Why context does not resolve it:** Route A category2 applies to the changed reading of the printed600-per-cohort and300-per-region counts. The adjacent total600 and downstream allocation make the probable intended total reconstructable, but the displayed per-cohort quantity remains three times the cohort count printed elsewhere and could be taken into design extraction. Reconstruction of a likely intended value does not remove a reproduced printed count discrepancy.

**Alternatives and missing definition:** “Per cohort” may have been intended to refer to the whole three-cohort trial, with300 per region across the entire trial; this preserves the600 total and the200-per-cohort allocation. Alternatively, the Study Design passage might describe a distinct cohort convention, but no such alternative definition is supplied in that passage. The observation is the conflicting printed count attribution; its production mechanism is not inferred.

**Exact human question:** In the original protocol Study Design statement on pp36–37, do600 dyads and300 per region/site refer to the whole trial rather than each of the three200-dyad cohorts, and which cohort/regional counts should be extracted as the planned design?

**Source confirmation:** Direct pdftotext-layout extraction from supplied DOC-002 pp36–44 and pp9–15; visual source-derived image of p36 freshly rendered using Poppler25.03.0 on CPU at preprocessing/numeric_support/DOC002-p036.png; source-matched reusable p37/p39 images inspected. Source numerals and their attribution were preserved without normalization.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-002 PLAN pp37 and91, six-occasion Study Design passages, alongside fullT1–T6 schedule on pp15,63–64/78 | The abbreviated prose lists baseline,3,9,12,36 months while saying six occasions; the full schedule supplies24 months. This is an incomplete enumeration, not a changed printed participant count or a changed outcome/decision rule. The complete schedule and six-occasion designation establish the intended measurement list; no actual planned analysis contrast relies on omitting24 months. | CONTEXT_RESOLVES |
| DOC-003 REPORT p2 eTable1, all five rows | Descriptive mean differences (.1,0,-.1,0,0) are not identical to adjusted model differences(-.01,-.04,-.05,-.03,.05). Footnoteb explicitly identifies longitudinal mixed-effects regression estimates; no claim these are crude differences. Printed-input half-unit crude intervals are [-.00,.20],[-.10,.10],[-.20,.00],[-.10,.10],[-.10,.10],respectively. | MODEL_VERSUS_CRUDE |

## Completion and limitations

All74 assigned support numeric relationships were checked explicitly. All5 eTable1 rows, all38 eTable2 coefficient/CI identities and all6 sample-validity footnotes, all6 eFigure1 panels, eFigure2 and all3 eFigure3 panels are covered. Plan sample/retention/exposure/randomization arithmetic and all9 power-table cells are covered. No scientific coverage gap. Exact power replication needs the numerical OD residual/random-effect default settings; no contradictory arithmetic was found in those printed inputs. Graphs lack exact numeric curve coordinates; visual checking is limited to labels, scales, direction and containment. Inferential compatibility and amended primary-model power implications are assigned to statistical specialists.

New derivative provenance: Poppler25.03.0 pdftoppm, CPU, supplied joi180075supp1_prod.pdf physical p36, command recorded in numeric inventory. Existing rendered images were read unchanged. No candidate IDs or adjudications assigned.

