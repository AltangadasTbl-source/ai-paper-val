# Construction-only synthetic fixtures

Every TEST workbook contains synthetic data or was saved for validation. Never distribute these as review templates or include their answers/counts in research data.

- TEST_blank.xlsx: blank role-A copy for initial formula evaluation.
- TEST_independence_R_A.xlsx: editing A leaves the clean B file unchanged.
- TEST_all_complete.xlsx: all 131 rows completed with synthetic substantive answers.
- TEST_all_complete_recalculated.xlsx: same synthetic workbook with evaluator-generated formula caches, saved and reopened. Formulas are retained; this was not a desktop Excel round trip.
- TEST_primary_cases.xlsx: valid/invalid entry and outcome scenarios; see cases.json for expected results.
- TEST_sorted_and_discuss.xlsx: complete records reordered, with one unresolved discuss in the actual one-candidate paper. Annual entry is complete; the affected paper's outcome counts are withheld.

Run construction validation only from this year's local directory. Reviewers use the release workbooks directly in Excel and do not run these scripts.
