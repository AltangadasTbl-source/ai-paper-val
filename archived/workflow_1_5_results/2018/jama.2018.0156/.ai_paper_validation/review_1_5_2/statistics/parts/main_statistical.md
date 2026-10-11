# Main-Paper Statistical Relationship Inventory (Shard-local IDs)

Source: DOC-001 `jama_jabre_2018_oi_180004.pdf`, PDF pp. 1-9. IDs are shard-local (`MS`), not canonical IDs and not candidate IDs. No conclusion or candidate judgment is made here.

| ID | Location(s) | Statistical relationship / matching context | Reproducible check for later passes |
|---|---|---|---|
| MS001 | pp. 1, 3-4 | Primary ITT: BMV-ETI=0.11%, one-sided 97.5% CI -1.64% to infinity; margin -1%; P(noninferiority)=.11. | Confirm the reported lower limit (-1.64%) is not > -1%, hence printed noninferiority interpretation follows stated criterion; retain one-sided/97.5% convention. |
| MS002 | p. 4 | Hierarchical model with center random effect: difference 0.05%, one-sided 97.5% CI -1.70% to infinity. | Check endpoint, ITT context, model label, CI sidedness, and margin interpretation separately from unadjusted primary result. |
| MS003 | p. 4 | PP primary: 4.3% vs 4.2%, difference .08%, one-sided 97.5% CI -1.74% to infinity, P(noninferiority)=.12. | Apply same stated noninferiority rule; retain PP population. |
| MS004 | pp. 1, 4, 6 Table 2 | ITT survival at 28 days: difference .1%, 95% CI -1.8 to 2.1, P=.90. | Check point estimate lies within ordered CI; match ITT/day-28 outcome and two-sided secondary-outcome convention. |
| MS005 | pp. 1, 4, 6 Table 2 | ITT hospital admission: difference -3.7%, 95% CI -7.7 to .3, P=.07. | CI containment/direction and matching narrative/table check. |
| MS006 | pp. 4, 6 Table 2 | ITT ROSC: difference -4.7%, 95% CI -8.8 to -.5, P=.03. | CI containment/direction, test label, population/time match. |
| MS007 | p. 6 Table 2 | ITT CPC distribution P=.68; five ordered category counts and primary success defined as CPC 1+2. | Verify P attaches to CPC distribution (not a single category) and primary-success definition matches counts. |
| MS008 | p. 6 Table 2 | PP survival: difference .1%, CI -10 to 9.7, P=.99; hospital admission -4.0%, CI -7.6 to .6, P=.055; ROSC -5.6%, CI -9.9 to -1.3, P=.01. | Check each point estimate/CI direction and preserve PP population. |
| MS009 | p. 6 Table 2 | PP CPC distribution P=.76. | Verify attachment to CPC distribution and population label. |
| MS010 | pp. 1, 4, 6 Table 3 | Difficulty: difference 4.7%, 95% CI 1.5-7.9, P=.004. | CI containment/direction and safety-population, row-specific denominator matching. |
| MS011 | pp. 1, 4, 6 Table 3 | Failure: difference 4.6%, 95% CI 2.8-6.4, P<.001. | CI containment/direction; record threshold display, not as a display-zero issue. |
| MS012 | pp. 1, 4, 6 Table 3 | Gastric regurgitation: difference 7.7%, 95% CI 4.9-10.4, P<.001. | CI containment/direction; record threshold display, not as a display-zero issue. |
| MS013 | p. 6 Table 3 footnote | P values for Table 3 calculated with chi-square or Fisher exact test. | Test-type applicability depends on row; do not infer which exact test was used without more source evidence. |
| MS014 | p. 3 | Secondary rates: chi-square and corresponding 95% CIs for odds ratios and differences; quantitative endpoints t test/Mann-Whitney by distribution; two-sided P=.05, no multiplicity adjustment. | Apply only after matching endpoint type and stated analysis family; distinguish CIs for differences from unspecified OR CIs. |
| MS015 | p. 4 | Post-hoc CCF: BMV 86%, ETI 87%, difference -1%, 95% CI -4% to 2%, P=.70. | Check direction/CI containment and group order BMV minus ETI. |
| MS016 | p. 4 | Post-hoc pauses >2 sec: BMV 27 vs ETI 16, difference 11 seconds, 95% CI 7-15, P<.001. | Check units (reported difference in seconds), direction, interval containment; no test model is explicitly named for this quantitative endpoint. |
| MS017 | pp. 3, 7-8 | Noninferiority design and interpretation: planned 80% power, sample 956/group under 3%/2% assumptions, 1% absolute margin; discussion states close observed 4.3%/4.2% estimates may have contributed to underpowering. | Keep planned assumptions separate from observed analysis; assess interpretation only under stated noninferiority rule. |

## Statistical coverage notes

- All P values in the main article are represented above, including P=.11, .12, .90, .07, .03, .68, .99, .76, .055, .01, .004, <.001, and .70.
- No `P = 0` or `p = 0.000` display occurs in DOC-001; no `DISPLAY_ZERO_NOT_CANDIDATE` record is needed for this source.
- Table 1 presents baseline descriptive statistics without P values; it is covered as numeric relationships (MN014-MN019).
