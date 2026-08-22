# Stable Candidate Ledger

All entries are **Pending Human Adjudication**. The ledger contains every distinct candidate emitted by the numeric, statistical-pass-1, and cross-source lanes after merging only genuine duplicates. No candidate-count limit was used.

## C001 — Table 2 footnote duplicates the supplements-without-therapy label

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Numeric consistency NC-01; cross-source consistency candidate 1; mapped numeric relationship N032 in the main evidence map.
- **Exact source locations:** [DOC-001 Table 2 — PDF p. 6](<../../jama_bot_2019_oi_190007.pdf#page=6>); [DOC-001 Figure 1 — PDF p. 3](<../../jama_bot_2019_oi_190007.pdf#page=3>); [DOC-001 Results — PDF p. 7](<../../jama_bot_2019_oi_190007.pdf#page=7>).
- **Printed evidence and rule:** Footnote d assigns both `32/256 (12.5%)` and `22/256 (8.6%)` to supplements without therapy. Figure 1, footnote f, and Results identify `22/256 (8.6%)` as supplements with therapy. The mutually exclusive 2x2 cells must have distinct therapy-stratum labels; `32+22=54` and `256+256=512` confirm that the numerical supplements total is intact.
- **Direct observation versus inference:** The repeated phrase is directly printed. The proposed intended label follows the other source locations and remains an inference for human review.
- **Alternative source-grounded interpretation:** Counts, percentages, OR, interval, and P value remain coherent; the issue may be confined to one footnote label.
- **Remaining human question:** Should footnote d's second `without therapy` read `with therapy`, and was the duplicated label reused downstream?

## C002 — Supplement-adherence cutoff changes from inclusive to strict wording

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Numeric consistency NC-02; cross-source consistency candidate 2.
- **Exact source locations:** [DOC-001 Methods — PDF p. 4](<../../jama_bot_2019_oi_190007.pdf#page=4>); [DOC-001 Results — PDF p. 6](<../../jama_bot_2019_oi_190007.pdf#page=6>); [DOC-004 eAppendix 8 — PDF p. 16](<../../joi190007supp3_prod.pdf#page=16>); [DOC-004 eAppendix 12 — PDF p. 22](<../../joi190007supp3_prod.pdf#page=22>).
- **Printed evidence and rule:** Methods and both supplement locations use `>=70%`; Results says `more than 70%`. Inclusive and strict inequalities differ at exactly 70%. The eAppendix 8 multinutrient pill-weight counts total `515/666=77.3%`, compatible with the rounded 77% in Results, but the number exactly at the boundary is not supplied.
- **Direct observation versus inference:** The wording difference is direct. Whether any participant classification changes is unknown without individual data.
- **Alternative source-grounded interpretation:** The narrative may use `more than 70%` informally for the predefined inclusive rule, with no numerical consequence.
- **Remaining human question:** Which cutoff produced the reported numerator, and were observations exactly at 70% included?

## C003 — eAppendix 8 footnote markers point to unrelated adherence rows

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Cross-source consistency candidate 3; numeric relationships N037-N044 in the unified inventory.
- **Exact source location:** [DOC-004 eAppendix 8 — PDF p. 16](<../../joi190007supp3_prod.pdf#page=16>).
- **Printed evidence and rule:** Four `>=70%` adherence rows carry `*`, while the single-asterisk note defines how the average Morisky score was calculated and the Morisky row has no visible marker. A separate `**` note reports kappa values but no visible row carries `**`. A footnote marker should identify the row or statistic qualified by its note.
- **Direct observation versus inference:** Marker placement and note text are directly printed. The intended reassignment of markers cannot be determined from the PDF.
- **Alternative source-grounded interpretation:** Markers may have shifted during table production; the adherence-row marks may have been intended for the kappa note and the Morisky mark may have been omitted.
- **Remaining human question:** Which rows were intended to carry the Morisky and kappa notes in the production source?

## C004 — eAppendix 10 prints a literal P value of zero

- **Category:** Statistical reporting inconsistency
- **Checker provenance:** Statistical consistency pass 1; relationship S023.
- **Exact source location:** [DOC-004 eAppendix 10B — PDF p. 19](<../../joi190007supp3_prod.pdf#page=19>).
- **Printed evidence and rule:** The baseline GAD-7 row prints `B=0.464`, 95% CI `0.409 to 0.52`, and `p=0`. A probability cannot be literally zero. The positive interval supports a very small P value, but the page supplies no unrounded value, test statistic, degrees of freedom, or rounding convention.
- **Direct observation versus inference:** `p=0` is directly printed. A replacement such as `P<.001` would be an inference unless confirmed from the analysis output.
- **Alternative source-grounded interpretation:** The software output may have rounded a very small positive P value to three decimals rather than using threshold notation.
- **Remaining human question:** What was the unrounded P value, and what journal-compliant display should replace or explain `0`?

## C005 — Main-article sample-size total conflicts with four stated cell counts

- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** Numeric consistency NC-03; cross-source consistency candidate 4; unified numeric relationship N005.
- **Exact source location:** [DOC-001 Sample Size — PDF p. 4](<../../jama_bot_2019_oi_190007.pdf#page=4>).
- **Printed evidence and rule:** The article states `392 participants (196 in each of the 4 possible intervention combinations)` were needed. Four combinations at 196 each require `4 x 196 = 784`, not 392. The following attrition statement gives 250 per combination, which consistently implies 1000.
- **Direct observation versus inference:** The total and parenthetical cell count are printed; their arithmetic incompatibility is direct. Which number or label was intended is not supplied.
- **Alternative source-grounded interpretation:** The 392 may have meant 196 participants in each side of a two-level factorial main-effect contrast, but the sentence says each of four combinations.
- **Remaining human question:** What sample-size unit did the power calculation use, and which printed quantity or phrase requires clarification?

## C006 — Protocol calls a 30% versus 15% contrast a 25% difference

- **Category:** Numeric or arithmetic inconsistency
- **Checker provenance:** Numeric consistency NC-04; cross-source consistency candidate 5.
- **Exact source location:** [DOC-002 Sample Size — PDF p. 16](<../../joi190007supp1_prod.pdf#page=16>).
- **Printed evidence and rule:** The protocol says it is powered to detect `a difference of 25%`, then specifies 30% control and 15% intervention incidence. The absolute difference is 15 percentage points and the relative reduction is 50%; neither equals 25% under those usual metrics.
- **Direct observation versus inference:** All three percentages are printed. The intended metric for 25% is not defined.
- **Alternative source-grounded interpretation:** The 25% may describe an unstated power-calculation parameter or a drafting carryover rather than either displayed incidence contrast.
- **Remaining human question:** What quantity was intended by `difference of 25%`, and what inputs generated the protocol calculation?

## C007 — Protocol and publication state different sample-size assumptions

- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Numeric consistency NC-05; cross-source consistency candidate 6.
- **Exact source locations:** [DOC-001 Sample Size — PDF p. 4](<../../jama_bot_2019_oi_190007.pdf#page=4>); [DOC-002 Sample Size — PDF pp. 16-17](<../../joi190007supp1_prod.pdf#page=16>).
- **Printed evidence and rule:** The publication states 30% control versus 20% active incidence and 22% attrition; the protocol states 30% control versus 15% intervention incidence and 20% dropout. Both address enrollment planning for the same one-year factorial trial and reach a 250-per-combination target, but the displayed effect and attrition inputs differ.
- **Direct observation versus inference:** The different inputs are printed. Whether they reflect a documented amendment is unresolved.
- **Alternative source-grounded interpretation:** Protocol version 7 may record a later amendment or a different planning stage; a legitimate revision could reconcile the documents.
- **Remaining human question:** Which assumptions governed final enrollment, and where is any dated amendment or recalculation documented?

## C008 — Protocol uses incompatible DSM editions for the primary endpoint

- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** Numeric consistency NC-06; cross-source consistency candidate 7.
- **Exact source locations:** [DOC-002 endpoint summary — PDF p. 8](<../../joi190007supp1_prod.pdf#page=8>); [DOC-002 outcome methods — PDF p. 28](<../../joi190007supp1_prod.pdf#page=28>); [DOC-001 primary outcome — PDF p. 4](<../../jama_bot_2019_oi_190007.pdf#page=4>).
- **Printed evidence and rule:** Protocol p. 8 labels the MINI-assessed MDD endpoint according to DSM-IV; p. 28 labels the same schedule and MINI V5.01 endpoint according to DSM-5. The article identifies DSM-IV. A single endpoint should use one edition label or explain a version transition.
- **Direct observation versus inference:** DSM-IV and DSM-5 are directly printed. Whether the underlying MINI assessment changed cannot be inferred.
- **Alternative source-grounded interpretation:** One protocol section may be unrevised drafting text, while the instrument and applied algorithm may have remained unchanged.
- **Remaining human question:** Which diagnostic edition governed endpoint assessment, and did the edition label reflect any operational difference?

## C009 — Analysis-plan significance threshold lacks a comparison operator

- **Category:** Statistical reporting inconsistency
- **Checker provenance:** Statistical consistency pass 1 and pass 2; relationship S049.
- **Exact source location:** [DOC-003 statistical analysis plan — PDF p. 3](<../../joi190007supp2_prod.pdf#page=3>).
- **Printed evidence and rule:** The sentence states `the 2-sided significance threshold will be set at p 0.05`, with no `<`, `<=`, `=`, or other operator between `p` and `0.05`. A threshold requires a comparison relation to identify which P values meet it.
- **Direct observation versus inference:** Direct PDF rendering confirms the missing operator. The likely intended convention is not a source fact.
- **Alternative source-grounded interpretation:** A less-than glyph may have been lost during document production, although it is absent from both native text and direct rendering.
- **Remaining human question:** Was the intended rule `P<.05`, `P<=.05`, or another explicitly defined convention?

## Registration Completion

Stable candidate set: `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`, `C009`. Every checker observation is represented. Cross-lane duplicates were merged before stable ID assignment while preserving all checker provenance; the five repair-stage candidates were appended without renumbering C001-C004.
