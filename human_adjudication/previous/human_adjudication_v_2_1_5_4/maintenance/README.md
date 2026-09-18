# Development maintenance only

Reviewers use the annual XLSX files and the Chinese PDF. Nothing here is a review, handoff, checking or export step.

build.mjs uses the frozen source catalog, codebook.json and @oai/artifact-tool to rebuild six workbooks. It writes to a new ADJ_OUTPUT directory and refuses an existing directory. test.mjs exercises workflow failure and completion scenarios; annual-test.mjs checks completed annual datasets. guide.mjs renders the Chinese guide with local Chrome. Use the supplied runtime Node dependencies (@oai/artifact-tool, jszip, xml-js, playwright), without modifying dependency directories.

The generated workbooks use ordinary Excel formulas; no macro, script or runtime dependency is embedded. All cell styles are explicitly unlocked after export.

Compatibility regression: test-compat.mjs verifies the unlock normalizer keeps protection before extLst, preserves extensions and is idempotent. Native Excel opening is a required release check; an artifact-tool re-import alone is insufficient.
