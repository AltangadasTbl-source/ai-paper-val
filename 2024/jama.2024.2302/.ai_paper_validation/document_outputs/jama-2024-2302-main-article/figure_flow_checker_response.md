# Figure and participant-flow check

- **Document:** `jama_blakely_2024_oi_240020_1710443209.74411.pdf`
- **Scope:** Main-article Figure 1 (PDF p. 3; journal p. 1037), Figure 2 (PDF p. 6; journal p. 1040), and Figure 3 (PDF p. 8; journal p. 1042), compared only with nearby main-article text/tables and result-relevant Supplement 3 pp. 2-5.
- **Source inspected:** Retained 300-dpi source-page renders and page-linked normalized text.
- **Protocol/SAP:** Not opened.

## Local candidate 1

- **Category:** Presentation inconsistency (participant-flow/adherence labeling)
- **Exact location:** Main article PDF p. 3 (journal p. 1037), Figure 1, the early- and late-allocation boxes and footnotes d/e.
- **Visible source evidence:**
  - The early box states `163 Received treatment as randomized`, but its component counts include `5 Underwent inguinal hernia repair after discharge from neonatal intensive care unit`.
  - Figure 1 footnote d defines the randomized early strategy as planned `prior to discharge from the neonatal intensive care unit`.
  - The late box states `157 Received treatment as randomized`, but its component counts include `39 Underwent inguinal hernia repair prior to reaching postmenstrual age of 55 wk`.
  - Figure 1 footnote e defines the randomized late strategy as planned after NICU discharge **and** when the infant was older than 55 weeks' postmenstrual age.
  - The nearby Surgery Characteristics text confirms the same 5 and 39 timing departures (PDF pp. 5-6; journal pp. 1039-1040).
- **Logical basis:** The umbrella label `Received treatment as randomized` visibly contains infants whose reported repair timing does not meet the figure's own timing definition for the assigned strategy. The displayed branch arithmetic closes (`147 + 11 + 5 = 163`; `90 + 28 + 39 = 157`), so the candidate concerns the adherence label rather than the counts.
- **Uncertainty:** The authors may have intended `received treatment as randomized` to mean that the infants remained under their assigned treatment-policy strategy rather than literal timing adherence. Figure 1 does not define that phrase, however, and it separately uses `Did not undergo treatment as randomized` for the 9 postrandomization withdrawals in each arm.
- **Verification instruction:** On source PDF p. 3, read each allocation-box heading together with its timing subcategories and footnotes d/e; then confirm the 5 and 39 timing departures in the Surgery Characteristics text on PDF pp. 5-6. Ask whether the umbrella label should instead describe retention in the assigned group/strategy or explicitly distinguish timing crossovers.

## Local candidate 2

- **Category:** Participant flow inconsistency / Presentation inconsistency
- **Exact location:** Main article PDF p. 3 (journal p. 1037), Figure 1, transitions from randomized allocation to lost-to-follow-up and primary-analysis boxes; compare PDF p. 4 (journal p. 1038), Results—Patient Characteristics, and PDF p. 6 (journal p. 1040), Table 2 note a.
- **Visible source evidence:**
  - Early arm: `172 Randomized`; the allocation box lists `163 Received treatment as randomized` and `9 Did not undergo treatment as randomized`; the next displayed box is `4 Lost to follow-up`, followed by `159 Included in primary analysis`.
  - Late arm: `166 Randomized`; the allocation box lists `157 Received treatment as randomized` and `9 Did not undergo treatment as randomized`; the next displayed box is `8 Lost to follow-up`, followed by `149 Included in primary analysis`.
  - The nearby Results text and Table 2 note a explicitly say that 9 infants in each group were **withdrawn after randomization** and excluded, in addition to the 4 and 8 lost to follow-up.
- **Logical basis:** The analysis totals require subtraction of both the 9 withdrawals and the losses (`172 - 9 - 4 = 159`; `166 - 9 - 8 = 149`). Figure 1 labels the 9 only as not undergoing treatment as randomized and does not display a withdrawal/exclusion branch before the analysis boxes. Thus the figure alone can be read as showing only loss to follow-up as the exclusion between allocation and analysis, even though the nearby text/table identify a separate withdrawal exclusion.
- **Uncertainty:** The exact matching counts and the text inside each allocation box allow a careful reader to reconstruct the exclusions, so this is a flow-label/branch ambiguity rather than an arithmetic contradiction.
- **Verification instruction:** Trace both arrows from the allocation boxes to the primary-analysis boxes on source PDF p. 3 and reconcile them with the explicit withdrawal wording on PDF pp. 4 and 6. Confirm whether a separate `withdrew/excluded from analysis (n=9)` branch was intended.

## Checks passed

- **Figure 1 screening accounting:** `1514 - 1176 = 338`; `442 + 734 = 1176`; and `338 + 734 = 1072` eligible infants, agreeing with the Results text.
- **Figure 1 nonrandomized accounting:** `613 + 54 + 37 + 14 + 16 = 734`.
- **Eligibility-failure reasons:** The displayed reasons total 474 rather than 442, but Figure 1 note a explicitly states that an infant may have had more than 1 reason; no issue inferred.
- **Within-arm pathways:** Early `147 + 11 + 5 = 163`, with the 11-, 5-, and 9-infant reason lists each closing; late `90 + 28 + 39 = 157`, with the 28-, 39-, and 9-infant reason lists each closing.
- **Supplement 3 enrollment anchors:** On Supplement 3 pp. 2-4, the associated-factor rows total 51; parent/guardian refusal reasons total 613; physician refusal reasons total 37; and `other reasons` total 16. These agree with Figure 1 and nearby Results text.
- **Figure 2:** Axis labels, favor direction, median RR 0.68, 95% CrI 0.45-1.01, and the caption's 97% probability of benefit agree with Table 2 and the Primary Outcome text. The visible dot/interval and density curve do not show a document-verifiable contradiction.
- **Figure 3:** All printed event counts, subgroup denominators, risk differences, relative risks, credible intervals, favor direction, and favorable-outcome probabilities agree with the nearby subgroup text where explicitly repeated. The forest-plot points/intervals align with the printed RR columns. The overall row agrees with Table 2 after the different displayed precision is accounted for.
- **Supplement layout:** eTable 1 continuation pages and eTable 2 labels/cells were inspected; no additional scientific figure/flow candidate was identified.

