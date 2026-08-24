# Candidate Ledger

All candidates remain **Pending Human Adjudication**. Similar evidence from the two supplement figures is retained as one genuine duplicate because it concerns the same repeated caption phrase, the same active-versus-placebo comparator, and the same label-consistency rule.

## C001 — eFigure 2 and eFigure 3 comparator wording conflicts with the active-versus-placebo contrast

- **Status:** Pending Human Adjudication
- **Origin:** Statistical pass 1 proposal SP001; numeric and cross-source lanes emitted no duplicate proposal.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** DOC-003 (`joi190122supp2_prod.pdf`) PDF p.18, eFigure 2 title/caption; DOC-003 PDF p.19, eFigure 3 title/caption; comparator context at DOC-003 PDF p.11, eTable 6, and DOC-001 (`jama_de_boer_2019_oi_190122.pdf`) PDF p.4.
- **Direct source evidence:** eFigure 2 is titled “Effects of Vitamin D Versus Placebo …”; eFigure 3 is titled “Effects of Omega-3 Fatty Acids Versus Placebo …”. Each caption states that estimates compare “the active treatment assignment to year 5,” even though the same sentence already defines baseline to year 5 as the change window. eTable 6 labels the relevant contrast “Ratio of change from baseline, active to placebo,” and the main article describes active interventions versus placebo.
- **Reported-versus-comparator:** Printed comparator labels in both figure titles: active treatment versus placebo. Printed comparator phrase in both captions: active treatment assignment “to year 5,” which names a follow-up timepoint rather than a control group.
- **Consistency rule:** An effect estimate’s comparator label must identify the comparison group. A follow-up timepoint can define the outcome window but cannot replace the placebo comparator in figures explicitly titled active treatment versus placebo.
- **Calculation / logical comparison:** No arithmetic is required. The titles identify placebo as comparator; the captions use year 5 as the object of “comparing,” while baseline-to-year-5 already defines time. The two labels do not reconcile under the displayed active-versus-placebo contrast.
- **Direct observation versus inferred explanation:** The titles and caption phrases are direct observations from fresh page-addressable native text. It is an inference, not a final correction, that the intended comparator may have been placebo.
- **Alternative source-grounded interpretation:** The non-layout Acrobat extraction may have omitted or reordered a visual caption element. No permitted page renderer was available to confirm glyph placement. Alternatively, both figure captions may reproduce the same wording defect.
- **Necessary missing input:** Direct visual rendering of DOC-003 pp.18-19 is unavailable in this run; plotted estimates, intervals, and P values are also unavailable from native text.
- **Exact human question:** Do the rendered source pages actually print “comparing the active treatment assignment to year 5”; if so, should the comparator wording identify placebo while retaining baseline to year 5 as the change window?
- **Potential downstream evidence-chain relevance:** If confirmed, a data extractor could copy an ambiguous comparator label when recording these subgroup effects. The package does not establish that this has occurred or that any conclusion changes.

## C002 — Omega-3 eGFR panel repeats vitamin-D contributor counts instead of the omega-3 allocation counts

- **Status:** Pending Human Adjudication
- **Origin:** Final evidence-quality audit repair of N031; omitted by the initial numeric lane.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-001 (`jama_de_boer_2019_oi_190122.pdf`) PDF p.7, Figure 2 panels A and B; DOC-001 PDF p.8, Table 2 omega-3 rows.
- **Direct source evidence:** Figure 2 panel A (vitamin D versus placebo) gives active/placebo contributor counts 701/607 at baseline, 531/459 at year 2, and 496/438 at year 5. Panel B (omega-3 versus placebo) repeats exactly 701/607, 531/459, and 496/438. Table 2’s matched omega-3 active/placebo counts are 657/651, 499/491, and 472/462.
- **Reported-versus-comparator:** Omega-3 Figure 2 panel B: 701/607, 531/459, 496/438; matched omega-3 Table 2: 657/651, 499/491, 472/462. The repeated panel-B counts instead equal the vitamin-D panel-A/Table-2 grouping.
- **Consistency rule:** Contributor counts for the same omega-3 versus placebo eGFR panels, timepoints, and analysis display should use the omega-3 factorial regrouping, not the different vitamin-D regrouping. Equal overall totals do not make the active/placebo allocation counts interchangeable.
- **Calculation / logical comparison:** At baseline both groupings total 1308, but the allocations differ: 701−657=44 and 607−651=−44. At year 2, 531−499=32 and 459−491=−32. At year 5, 496−472=24 and 438−462=−24. Thus panel B preserves totals while shifting participants between the printed active/placebo groups.
- **Direct observation versus inferred explanation:** The two Figure 2 count sequences and the Table 2 omega-3 sequence are direct observations from fresh page-addressable native text. Copying from panel A is a possible production explanation, not an established cause or correction.
- **Alternative source-grounded interpretation:** Non-layout extraction might have reordered panel labels or count sequences; a rendered page could establish the exact visual association. However, the native sequence explicitly places the repeated values within panel B’s omega-3 section.
- **Necessary missing input:** Direct page rendering is unavailable; visual confirmation of panel placement remains necessary.
- **Exact human question:** Does rendered Figure 2 panel B associate the repeated 701/607, 531/459, and 496/438 values with omega-3 versus placebo, and if so, why do they differ from the matched omega-3 contributor counts in Table 2?
- **Potential downstream evidence-chain relevance:** If confirmed, a data extractor could copy incorrect arm-specific contributor denominators for omega-3 eGFR timepoints. The package does not show that this has happened or that estimates/conclusions change.

## C003 — Omega-3 urine-ACR panel repeats vitamin-D contributor counts instead of the omega-3 allocation counts

- **Status:** Pending Human Adjudication
- **Origin:** Final evidence-quality audit repair of N031; distinct endpoint/value set from C002.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-001 (`jama_de_boer_2019_oi_190122.pdf`) PDF p.7, Figure 2 panels C and D; DOC-003 (`joi190122supp2_prod.pdf`) PDF p.11, eTable 6 omega-3 rows.
- **Direct source evidence:** Figure 2 panel C (vitamin D versus placebo) gives active/placebo urine-ACR contributor counts 702/609 at baseline, 529/463 at year 2, and 505/440 at year 5. Panel D (omega-3 versus placebo) repeats exactly 702/609, 529/463, and 505/440. eTable 6’s matched omega-3 counts are 658/653, 502/490, and 478/467.
- **Reported-versus-comparator:** Omega-3 Figure 2 panel D: 702/609, 529/463, 505/440; matched omega-3 eTable 6: 658/653, 502/490, 478/467. The panel-D sequence instead equals the vitamin-D panel-C grouping.
- **Consistency rule:** Counts for the same omega-3 versus placebo urine-ACR timepoints must reflect the omega-3 factorial regrouping; equal totals do not authorize reuse of the vitamin-D arm split.
- **Calculation / logical comparison:** At baseline, panel D differs from eTable 6 by +44 active and −44 placebo; at year 2 by +27 and −27; at year 5 by +27 and −27. Overall totals reconcile (1311, 992, and 945), but the printed arm allocations do not.
- **Direct observation versus inferred explanation:** Figure and eTable sequences are directly observed in fresh native text. A copied-panel explanation is inferred and is not a final correction.
- **Alternative source-grounded interpretation:** Native text may have reordered visual elements, although the sequence places the repeated counts inside panel D’s omega-3 section. Rendering is needed to confirm the visual association.
- **Necessary missing input:** Direct page rendering and visual panel confirmation are unavailable.
- **Exact human question:** Does rendered Figure 2 panel D associate 702/609, 529/463, and 505/440 with omega-3 versus placebo, and if so, why do those arm counts differ from eTable 6’s matched omega-3 counts?
- **Potential downstream evidence-chain relevance:** If confirmed, a data extractor could copy incorrect arm-specific contributor denominators for omega-3 urine-ACR timepoints. No downstream use or conclusion change is established.

## C004 — eTable 7 reports 944 analyzed participants but its footnote states that 991 were included

- **Status:** Pending Human Adjudication
- **Origin:** Final evidence-quality audit repair of N059; omitted by the initial numeric lane.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-003 (`joi190122supp2_prod.pdf`) PDF p.12, eTable 7 title, active/placebo rows, and footnote marked `*`.
- **Direct source evidence:** The title states that participants with available baseline and year-5 measurements number `N = 944*`. The displayed factorial arm counts reconcile to 944 for both treatment dimensions: 504+440=944 and 477+467=944. The attached footnote states that 991 participants donated both baseline and year-5 urine samples and “were included in this analysis”; it also states that 320 baseline-only participants and 1 participant without baseline were excluded from 1312.
- **Reported-versus-comparator:** Title and displayed arm denominators: 944. Attached inclusion footnote: 991. Difference: 47 participants.
- **Consistency rule:** A footnote attached to the table’s analysis N and explicitly stating how many participants “were included in this analysis” should reconcile with the title and displayed analysis denominators, or name a further exclusion/population distinction.
- **Calculation / logical comparison:** 504+440=944; 477+467=944; 991−944=47. The footnote flow also gives 991+320+1=1312, so it does not name the additional 47-person reduction represented by the rows/title.
- **Direct observation versus inferred explanation:** The title, rows, footnote statement, and arithmetic are direct observations. It is inferred—but not established—that 991 may be the count donating samples while 944 is a paired complete-case analysis after an unreported additional rule.
- **Alternative source-grounded interpretation:** Some of the 991 urine donors may lack usable ACR measurements or another necessary covariate, but the supplied footnote says all 991 were included and does not state a 47-participant exclusion.
- **Necessary missing input:** A definition or flow explaining the 47-person difference is absent from the table text.
- **Exact human question:** Which count is the intended eTable 7 analysis population, 944 or 991, and what source-defined exclusion or denominator rule accounts for the 47-participant difference?
- **Potential downstream evidence-chain relevance:** If confirmed, an evidence extractor could record the wrong complete-case analysis denominator. The package does not establish propagation or impact on effect estimates.
