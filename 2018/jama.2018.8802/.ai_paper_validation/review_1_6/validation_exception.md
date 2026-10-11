# Authorized Current-Provider Exception

The user explicitly instructed the review to use the current provider even where Workflow1.6 defaults to OpenRouter. Provider inheritance was preserved without switching or changing credentials/configuration. The routing preflight records that authorized choice truthfully.

The preserved bundled validator's validate_routing_preflight function hardcodes `Provider: openrouter`. Reporting that literal provider without evidence of actual routing would misstate the run. The control script and original validation result are preserved without modification. The expected provider assertion is an authorized configuration exception, not a scientific coverage gap. The complete original result is in review_validation.json; its actual status and remaining-check results are recorded below after validation.

## Actual final validation result

- Original validator status: FAIL.
- Error count:1.
- Sole error: `Routing preflight must record Provider: openrouter.`
- Warnings:None.
- Authorized effective provider selection:inherited current session, per explicit user instruction; no provider switch or guessed identity.
- Complete source coverage:PASS,44mapped of44pages;0fresh-required extraction gaps.
- Source and all65reused-artifact integrity:PASS; after-hash files exactly match before-hash files.
- Mandatory agent routing:all required fresh distinct fixedgpt-6.1-sol stages recorded;12actual agents including coordinator and support numeric shard.
- Statistical relationships:104, each complete in two distinct freshhigh passes.
- Candidate ledger/recheck/audit/report:identical19IDs,allcompleteclassificationfields;17recorded_candidate and2record_input_error.
- Report cards:allrequiredfields;95exact__humanblankfields;allPDFevidencelinksresolve;standaloneHTML has embeddedCSS andtableofcontents.
- Temporary environment:NOT_NEEDED;none created;removecommandreturnedemptyremovedlist.
- Review duration:34.42minutes;25-40minute target MET_TARGET.

Every validator condition other than the authorized provider-default exception passed. The scientific review and deliverable assembly are complete. Strict Workflow1.6 PASS remains unattained because changing the truthful routing record to the hardcoded provider would conflict with the user's explicit override. No control file, original validation status or routing evidence was altered to hide this condition. All candidates remain Pending Human Adjudication.
