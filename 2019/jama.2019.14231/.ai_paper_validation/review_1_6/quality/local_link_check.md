# Local artifact link check

Pre-report coordinator check at 2026-10-11T01:36Z used Perl File::Find to read every current-run Markdown artifact and resolve each relative Markdown link from its containing directory. URL fragments were removed only for filesystem existence checks.

- Local links checked: 2323
- Missing targets: 0
- Scope: `.ai_paper_validation/review_1_6/**/*.md`

The final bundled validator separately checks the report's truthful source locations and local evidence links.
