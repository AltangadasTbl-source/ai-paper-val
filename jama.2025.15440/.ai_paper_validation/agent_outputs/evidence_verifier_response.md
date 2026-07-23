# Evidence Verifier Response

- Verification scope: coordinator-supplied candidates C-01 and C-02 only.
- Source reopened: `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`.
- Verification rounds used: 1 of 2. Round 2 was not necessary.
- External sources, protocol, and SAP: not used.

## C-01 - Verified

- **Category:** Statistical reporting inconsistency.
- **Exact locations and source statements:**
  - PDF p. 1, structured abstract, Results: stroke occurred in **69 participants (2.7%)** in the intervention group and **64 (2.5%)** in the control group; rate ratio **1.08 (95% CI, 0.76-1.53)**.
  - PDF p. 5, Results, final paragraph: stroke occurred in **69 participants (2.7%)** in the intervention group and **64 (2.5%)** in the control group; event RR **1.08 (95% CI, 0.77-1.51)**.
  - PDF p. 7, Figure 4B, row **"Any stroke"**: patch group **69 (2.7%)** of 2520 and usual-care group **64 (2.5%)** of 2520; rate ratio **1.08 (95% CI, 0.77-1.51)**. The Figure 4 caption identifies panel B as rate ratios from time-to-event analyses of events from randomization through 2.5 years.
- **Comparison and logical basis:** All three locations report the same any-stroke result: 69 versus 64 events, the same group sizes of 2520, the same displayed percentages, and the same point estimate of 1.08. No location identifies a different outcome definition, population, follow-up horizon, or analysis for the abstract value. The abstract lower limit differs from the body and figure by **0.01** (0.76 versus 0.77), and the upper limit differs by **0.02** (1.53 versus 1.51). This is a repeated-value inconsistency, independent of any attempt to reconstruct the model-based CI.
- **Human verification instruction:** On PDF p. 1, read the last sentence of the structured-abstract Results; compare it with the last Results paragraph on p. 5 and the "Any stroke" row of Figure 4B on p. 7. Confirm the repeated 69 versus 64 events and rate ratio 1.08, then determine whether **0.76-1.53** or **0.77-1.51** is intended.

## C-02 - Rejected

- **Category considered:** Participant flow inconsistency.
- **Exact location and source statements:** PDF p. 4 (journal p. 1352), Figure 1, **"Flow of Participants in a Trial of Remote Patch-Based Electrocardiogram (ECG) Monitoring for Atrial Fibrillation Diagnosis."** The figure shows:
  - **368,000** individuals assessed for eligibility, with a footnote that the total is estimated;
  - **22,044** invited to participate;
  - **1,186** excluded because the GP practice participated in another trial;
  - **20,858** included;
  - **5,116** replies received;
  - **76** excluded after reply, comprising 72 negative replies and 4 positive replies with incomplete consent and no response to further contact;
  - **5,040** randomized.
- **Calculations:** The displayed formal transitions reconcile: **22,044 - 1,186 = 20,858** and **5,116 - 76 = 5,040**. The stage differences identified by the candidate are **368,000 - 22,044 = 345,956** not invited and **20,858 - 5,116 = 15,742** without a received reply.
- **Logical basis for rejection:** The unshown differences are inferable, but their omission does not create an internal contradiction. The boxes are labeled as different recruitment stages ("assessed," "invited," "included," and "replies received"), and the first count is explicitly estimated. Figure 1 does not state that every person who did not advance between these screening and response stages is an exclusion requiring a separate node. In contrast, the two explicit exclusion boxes are enough to reconcile the adjacent included and randomized totals exactly. On the supplied page alone, the absent "not invited" and "no reply" boxes may affect the level of process detail, but they do not make the reported participant flow arithmetically or logically inconsistent. Treating the omission as an error would require an external reporting requirement, which is outside this verification scope.
- **Human verification instruction:** Trace Figure 1 on PDF p. 4 and recalculate the two exact displayed transitions, 22,044 to 20,858 and 5,116 to 5,040. Note that the intervening labels are recruitment-stage subsets and that 368,000 is estimated; confirm that the figure makes no claim that all noninvited individuals or nonresponders are separately enumerated.

