# Current-provider validation override

The user explicitly requested the current provider by default. That instruction supersedes the bundled OpenRouter selection. The session and named specialist presets continue without changing any provider or authentication configuration.

The supplied validator requires a literal `Provider: openrouter` routing-preflight value. Reporting that value for an unverified current provider would be inaccurate. This directory holds a preserved copy of the supplied auxiliary validation helper with exactly one string changed: expected Provider becomes `CURRENT_SESSION_DEFAULT`. The diff and both hashes are recorded alongside it. All scientific, source-integrity, agent, coverage, classification, report, and timing checks remain unchanged. No original workflow file is modified.

At completion run the supplied command first, retain its output, and then execute this provider-adjusted copy with `--profile 1.6 --package .`. Distinguish the original validator's provider-only failure from the adjusted validation result in the report and completion message. This is an instruction-driven compatibility change to the permitted bundled validator helper; it introduces no scientific review orchestration or extraction code.
