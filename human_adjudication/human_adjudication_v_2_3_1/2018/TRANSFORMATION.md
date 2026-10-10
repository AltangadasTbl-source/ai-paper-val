# 2018 construction record — v.2.3.1

Only the 2018 v.2.1.5.3 primary-review format and rules were used. The annual cohort defines membership, including papers with 2017 in their DOI. The supplied and current baseline inventories match exactly. Source hashes are in source_hash_manifest.json; sources were read without modification.

The builder loads the actual annual workbook to retain source values, primary row order, navy headers, widths, wrapping, freeze panes and baseline H–L default formulas. It rebuilds the workflow and result sheets, removes Primary_snapshot and the old review handoff, clears M–Q and hides those narrow spacer columns, retains notes in R, removes stale validations and conditional formatting, and creates independent blank role files from the same source. Suggested E values are preserved and explicitly labeled editable AI suggestions. E and G are widened for readability. C_ tables become filterable A:R ranges so spacer headers can be truly empty. Source tables remain intact.

Candidates, Evidence, Links and Relations remain cell-for-cell equal to both the annual baseline and the 2018 subset of the source catalog. Original href text is unchanged; hyperlink metadata resolves the original repository file and uses a relative path from the output directory. Papers links to paper sheets; candidate keys link to embedded evidence. No Excel formula depends on those external source documents.

G validates identity (including spaces, tabs/newlines and nonbreaking-space-only input), key uniqueness and paper membership, disposition/domain, required and optional judgments, inactive stale values, and completion. Option codes are case-sensitive through EXACT, so invalid capitalization pasted around dropdowns is rejected. Blank completion means draft. A completed flag must be manually reset before editing.

Decisions uses candidate-key INDEX/MATCH lookups. Inactive effective fields normalize to not_applicable, while G blocks readiness for stale inputs. P_R/P_P descriptive relationship precedence is retained. Temporal outcomes require S_C/S_W and the baseline judgment eligibility. Baseline indeterminate/minor judgments that do not meet eligibility remain not_eligible; they are not converted into confirmed findings. The v.2.3.1 adaptations are a blank discuss outcome, a separate unresolved count, and paper outcome counts withheld until every row is ready and no row is discuss. This allows independent review completion without scientific resolution.

Protection is deliberately not enabled: protected ranges NONE. Rule_defaults displays the fixed applicability table but remains editable. All cells, unused-cell defaults, cell styles and named styles explicitly serialize locked=0 and hidden=0. No passwords or workbook structure lock exist. The baseline was also unprotected. Initial validation detected openpyxl omitting protection for style index zero; a narrowly scoped styles.xml serialization step now explicitly unlocks every cellXf/cellStyleXf, and final validation inspects the ZIP contents.

Tools: Python 3.12.3; local .venv; openpyxl 3.1.5 and et_xmlfile 2.0.0. No global packages changed. openpyxl writes OOXML but does not calculate formulas. Construction scratch is directed to .tmp inside this folder. The first development passes used the library's default transient scratch behavior before this was explicitly redirected; no source or other-year files were changed. Staging and test files are construction artifacts, never reviewer deliverables. Synthetic fixtures are labeled TEST ONLY. No automation was registered.

The construction-only formula probe parses and evaluates the actual emitted formulas for the supported function subset. It is a limited test harness, not Excel and not a certified compatible calculation engine. No cached values from openpyxl are treated as recalculation evidence. Desktop Excel visual and saved/reopened functional validation remains pending; see VALIDATION.md.

Construction commands, from this folder:

```
.venv/bin/python build_v_2_3_1.py --year 2018 --output-dir NEW_EMPTY_STAGING_DIRECTORY
.venv/bin/python validate_v_2_3_1.py --year 2018 --input-dir NEW_EMPTY_STAGING_DIRECTORY
```

The builder rejects other years, paths outside this folder, release output paths and existing workbook outputs. It never overwrites released workbooks. Do not run either script as part of review or delivery. Future corrections require a separately named version and explicit review of changes. The settled workbook, edited and saved in Excel, is the review authority.
