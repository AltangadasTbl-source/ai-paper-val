# Development maintenance only

Reviewers use the annual XLSX files and the Chinese PDF. Nothing here is a review, handoff, checking or export step.

build.mjs uses the frozen source catalog, codebook.json and @oai/artifact-tool to rebuild six workbooks. It writes to a new ADJ_OUTPUT directory and refuses an existing directory. test.mjs exercises workflow failure and completion scenarios; annual-test.mjs checks completed annual datasets. guide.mjs renders the Chinese guide with local Chrome. Use the supplied runtime Node dependencies (@oai/artifact-tool, jszip, playwright), without modifying dependency directories.

The generated workbooks use ordinary Excel formulas; no macro, script or runtime dependency is embedded. All cell styles are explicitly unlocked after export.
