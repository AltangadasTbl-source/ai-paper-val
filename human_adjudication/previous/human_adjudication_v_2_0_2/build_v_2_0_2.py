#!/usr/bin/env python3
"""Build self-contained v.2.0.2 primary-review and checker HTML files."""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote


VERSION = "v.2.0.2"
SCHEMA_VERSION = 5
YEARS = ("2018", "2019", "2024", "2025")
EXPECTED_YEAR_COUNTS = {"2018": 119, "2019": 71, "2024": 91, "2025": 131}
EXPECTED_PRIMARY_COUNTS = {"P_R": 45, "P_P": 41, "P_O": 2, "P_B": 7, "S_C": 65, "S_W": 252}
STATISTICAL_ROUTING_CATEGORIES = {
    "Statistical reporting inconsistency",
    "Denominator, proportion, or total inconsistency",
    "Numeric or arithmetic inconsistency",
    "Rate-versus-count inconsistency",
    "Analysis-unit or population inconsistency",
}

OUT_DIR = Path(__file__).resolve().parent
ROOT = OUT_DIR.parents[1]
SOURCE = ROOT / "meta_report" / "consistency_reclassification_2026-09-04" / "reclassified_candidates.json"


def clean_markdown(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\((?:<[^>]+>|[^)]+)\)", r"\1", value)
    value = value.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", value).strip()


def body_field(body: str, name: str) -> str:
    match = re.search(
        rf"^\*\*{re.escape(name)}:\*\*\s*(.*?)(?=\n\n\*\*|\Z)",
        body,
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return clean_markdown(match.group(1)) if match else ""


def repo_href(source_href: str) -> str:
    if re.match(r"^[a-z]+://", source_href, flags=re.IGNORECASE):
        return source_href
    marker = "ai-paper-results/"
    if marker in source_href:
        return "../../" + source_href.split(marker, 1)[1]
    return source_href


def suggested_domain(row: dict[str, object]) -> str:
    relationship = str(row["primary"])
    if relationship == "P_R":
        return "protocol_report"
    if relationship == "P_P":
        return "protocol_internal"
    if relationship == "P_O":
        return "protocol_operational"
    if relationship == "P_B":
        return "protocol_background"
    if str(row.get("category", "")) in STATISTICAL_ROUTING_CATEGORIES:
        return "statistical_results"
    return "internal_nonstatistical"


def compact_row(row: dict[str, object]) -> dict[str, object]:
    body = str(row.get("body", ""))
    evidence_names = (
        "Source evidence",
        "Reported-versus-comparator",
        "Calculation",
        "Alternative source-grounded interpretations",
        "Mechanical evidence recheck",
        "Human verification steps",
    )
    evidence = {name: body_field(body, name) for name in evidence_names}
    evidence = {key: value for key, value in evidence.items() if value}
    report_path = str(row["reportPath"])
    return {
        "key": row["key"],
        "year": row["year"],
        "package": row["package"],
        "id": row["id"],
        "sourceId": row.get("sourceId", row["id"]),
        "title": row["title"],
        "statement": row.get("statement", ""),
        "category": row.get("category", ""),
        "sourceStatus": row.get("sourceStatus", ""),
        "locations": row.get("locations", ""),
        "sourceLinks": [
            {"label": link.get("label", "Source"), "href": repo_href(str(link.get("href", "")))}
            for link in row.get("sourceLinks", [])
        ],
        "reportHref": "../../" + str(row.get("reportHref", report_path)).split("ai-paper-results/", 1)[-1],
        "reportPath": report_path,
        "primary": row["primary"],
        "relations": row.get("relations", []),
        "rationale": row.get("rationale", ""),
        "evidencePaths": [
            {"label": path, "href": "../../" + str(path)} for path in row.get("evidence_paths", [])
        ],
        "ambiguity": row.get("ambiguity", ""),
        "duplicateOfCoding": row.get("duplicate_of", ""),
        "subtype": row.get("subtype", ""),
        "evidenceState": row.get("evidence_state", "recorded_candidate"),
        "planMechanism": row.get("plan_discrepancy_mechanism", ""),
        "additionalSensitivityExclude": bool(row.get("additional_sensitivity_exclude", False)),
        "broadPlanInvolved": bool(row.get("broad_plan_involved", False)),
        "submissionInvolved": bool(row.get("submission_involved", False)),
        "currentReportCrossDocument": bool(row.get("current_report_cross_document", False)),
        "originalCrossDocument": bool(row.get("original_cross_document", False)),
        "suggestedDomain": suggested_domain(row),
        "evidence": evidence,
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__YEAR__ Two-Stage Flag Review — v.2.0.2</title>
  <style>
    :root { --ink:#17212b; --muted:#617080; --line:#d9e1e6; --paper:#fff; --wash:#f4f7f8; --accent:#176b87; --accent2:#0e536b; --soft:#e7f4f7; --ok:#28764c; --warn:#996300; --bad:#a33e35; --purple:#5d54a4; --shadow:0 5px 20px rgba(24,48,62,.08); }
    * { box-sizing:border-box; } html { scroll-behavior:smooth; } body { margin:0; color:var(--ink); background:var(--wash); font:14px/1.48 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
    button,input,select,textarea { font:inherit; } a { color:var(--accent2); } code { font-size:.92em; }
    .page { width:min(1380px,calc(100% - 30px)); margin:0 auto; }
    header { padding:28px 0 24px; color:#fff; background:linear-gradient(125deg,#103f52,#176b87 60%,#25869b); }
    header h1 { margin:0 0 7px; font:700 clamp(24px,4vw,38px)/1.15 Georgia,serif; } header p { max-width:1000px; margin:0; color:#e5f4f7; }
    .provenance { margin-top:11px; color:#cce6ec; font-size:12px; }
    .reviewer-bar { position:sticky; top:0; z-index:20; padding:10px 0; border-bottom:1px solid var(--line); background:rgba(244,247,248,.97); backdrop-filter:blur(8px); }
    .reviewer-grid { display:grid; grid-template-columns:minmax(130px,.45fr) minmax(180px,.8fr) auto 1fr; gap:8px; align-items:center; }
    .control,.btn { min-height:39px; padding:8px 10px; border:1px solid #b9c6ce; border-radius:8px; color:var(--ink); background:#fff; }
    .btn { cursor:pointer; font-weight:700; } .btn:hover { border-color:var(--accent); color:var(--accent); } .btn.primary { color:#fff; border-color:var(--accent); background:var(--accent); }
    .active-reviewer { color:var(--muted); font-size:12px; text-align:right; }
    .toolbar { display:grid; grid-template-columns:1.5fr repeat(4,minmax(145px,.55fr)) auto; gap:8px; margin:14px 0 10px; }
    .actions { position:relative; } .actions>summary { list-style:none; } .actions>summary::-webkit-details-marker { display:none; }
    .menu { position:absolute; right:0; top:44px; z-index:15; width:270px; padding:8px; border:1px solid var(--line); border-radius:10px; background:#fff; box-shadow:var(--shadow); }
    .menu .btn,.menu label { display:block; width:100%; margin:3px 0; text-align:left; } .menu input[type=file] { display:none; }
    .stats { display:grid; grid-template-columns:repeat(7,1fr); gap:8px; margin:10px 0 14px; }
    .stat { padding:11px 12px; border:1px solid var(--line); border-radius:9px; background:#fff; box-shadow:0 2px 7px rgba(30,50,60,.03); }
    .stat b { display:block; font-size:21px; line-height:1.1; } .stat span { color:var(--muted); font-size:11px; }
    .notice { display:flex; gap:10px; align-items:flex-start; margin:0 0 13px; padding:11px 13px; border-left:4px solid var(--accent); border-radius:4px 8px 8px 4px; background:var(--soft); }
    .notice strong { white-space:nowrap; } #save-status { margin-left:auto; color:var(--muted); font-size:12px; white-space:nowrap; }
    details.group { margin:10px 0; overflow:clip; border:1px solid var(--line); border-radius:10px; background:#fff; box-shadow:0 3px 12px rgba(30,50,60,.04); }
    details.group>summary { padding:13px 15px; cursor:pointer; font-weight:750; background:#f9fbfb; } details.paper { margin:9px 12px 12px; box-shadow:none; }
    .group-count { margin-left:7px; color:var(--muted); font-size:12px; font-weight:550; }
    .candidate-list { margin:0; padding:2px 15px 14px 40px; } .candidate-list>li { margin:7px 0; padding-left:2px; }
    details.candidate { overflow:hidden; border:1px solid var(--line); border-radius:8px; background:#fff; } details.candidate[open] { border-color:#b7cdd5; box-shadow:0 3px 12px rgba(30,50,60,.06); }
    details.candidate>summary { display:flex; gap:8px; align-items:flex-start; padding:10px 11px; cursor:pointer; list-style:none; } details.candidate>summary::-webkit-details-marker { display:none; }
    details.candidate>summary::before { content:"›"; color:var(--accent); font-size:21px; line-height:18px; transition:transform .12s; } details.candidate[open]>summary::before { transform:rotate(90deg); }
    .candidate-id { flex:0 0 auto; color:var(--accent); font-weight:800; } .candidate-title { flex:1 1 auto; font-weight:650; }
    .badge,.analysis-pill,.chip { display:inline-block; border-radius:999px; padding:2px 8px; font-size:11px; font-weight:700; }
    .badge { flex:0 0 auto; color:#fff; background:#687480; } .badge.progress { background:var(--warn); } .badge.complete { background:var(--ok); }
    .analysis-pill { color:#fff; background:#687480; } .analysis-pill.primary { background:var(--purple); } .analysis-pill.secondary { background:var(--accent); } .analysis-pill.protocol { background:#735a2a; }
    .candidate-body { padding:0 13px 14px 40px; border-top:1px solid #edf1f3; }
    .metadata { display:flex; flex-wrap:wrap; gap:6px; padding:11px 0 3px; } .chip { border:1px solid var(--line); color:var(--muted); background:#fafbfb; font-weight:600; }
    .chip.relationship { color:#174f62; border-color:#b8d0d8; background:#eff8fa; } .chip.warning { color:#7d3d12; border-color:#e1c3ad; background:#fff6ef; }
    .statement { max-width:1100px; margin:8px 0; } .source-row { display:flex; flex-wrap:wrap; gap:6px; align-items:center; margin:8px 0 11px; color:var(--muted); font-size:12px; }
    .source-link { display:inline-block; padding:3px 7px; border:1px solid #b8cdd5; border-radius:6px; text-decoration:none; background:#f5fbfc; }
    .evidence-box,.coding-box { margin:8px 0 12px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfcfc; }
    .evidence-box h4 { margin:8px 0 2px; color:#3f505c; font-size:12px; } .evidence-box p { margin:0 0 7px; } .coding-box summary { cursor:pointer; font-weight:700; }
    .coding-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px 14px; margin-top:9px; } .coding-grid p { margin:0; }
    .review-panel { padding:12px; border-radius:9px; background:#f4f7f8; } .review-panel.locked { opacity:.58; pointer-events:none; }
    .section-title { margin:0 0 8px; color:#2d4653; font-size:14px; }
    .review-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; margin-bottom:10px; }
    .field { display:flex; flex-direction:column; gap:4px; } .field.wide { grid-column:span 2; } .field.full { grid-column:1/-1; }
    .field label { color:#3e4e59; font-size:12px; font-weight:750; } .field select,.field input,.field textarea { width:100%; padding:7px 8px; border:1px solid #bac7cf; border-radius:7px; background:#fff; }
    .field textarea { min-height:68px; resize:vertical; } .hint { color:var(--muted); font-size:11px; }
    .module { margin-top:10px; padding:10px; border:1px solid #d4e1e5; border-radius:8px; background:#fbfdfd; } .module[hidden] { display:none; }
    .primary-readonly { margin:10px 0; padding:11px 12px; border:1px solid #c8d7dd; border-radius:8px; background:#eef5f7; }
    .primary-readonly h3 { margin:0 0 7px; font-size:14px; color:#244b59; }
    .primary-readonly dl { display:grid; grid-template-columns:minmax(150px,.35fr) 1fr; gap:4px 12px; margin:0; }
    .primary-readonly dt { color:var(--muted); font-size:12px; font-weight:700; }
    .primary-readonly dd { margin:0; white-space:pre-wrap; overflow-wrap:anywhere; }
    .checker-box { margin-top:11px; padding:11px; border:2px solid #b9d5dd; border-radius:9px; background:#f7fcfd; }
    .completion { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-top:10px; padding-top:10px; border-top:1px solid var(--line); }
    .validation { color:var(--bad); font-size:12px; } .empty { padding:40px 0; text-align:center; color:var(--muted); }
    footer { padding:25px 0 42px; color:var(--muted); font-size:12px; }
    @media(max-width:1050px) { .toolbar { grid-template-columns:repeat(3,1fr); } .toolbar input[type=search] { grid-column:1/-1; } .stats { grid-template-columns:repeat(3,1fr); } .review-grid { grid-template-columns:repeat(2,1fr); } }
    @media(max-width:700px) { .reviewer-grid,.toolbar,.review-grid,.coding-grid { grid-template-columns:1fr; } .active-reviewer { text-align:left; } .field.wide,.field.full { grid-column:auto; } .stats { grid-template-columns:repeat(2,1fr); } .candidate-body { padding-left:12px; } }
    @media print { .reviewer-bar,.toolbar,.notice,.menu,footer { display:none!important; } body { background:#fff; font-size:10pt; } .page { width:100%; } header { color:#000; background:#fff; padding:0 0 10px; } header p,.provenance { color:#333; } details { break-inside:avoid; } details.group,details.candidate { box-shadow:none; } }
  </style>
</head>
<body>
  <header><div class="page">
    <h1>__YEAR__ Two-Stage Candidate-Flag Review</h1>
    <p>Version v.2.0.2 supports a primary adjudication followed by a visible-answer second-person check. It preserves the primary record, the checker response, and the checker-proposed final assessment separately.</p>
    <div class="provenance">Generated __GENERATED__ · __PACKAGES__ papers · __TOTAL__ candidates · source digest <code>__DIGEST_SHORT__</code></div>
  </div></header>

  <div class="reviewer-bar"><div class="page reviewer-grid">
    <input id="reviewer-id" class="control" placeholder="Reviewer ID (required)" aria-label="Reviewer ID">
    <input id="reviewer-name" class="control" placeholder="Display name (optional)" aria-label="Reviewer name">
    <button id="activate-reviewer" class="btn primary">Create / load primary reviewer</button>
    <div id="active-reviewer" class="active-reviewer">No active reviewer; review fields are locked.</div>
  </div></div>

  <main class="page">
    <div class="toolbar">
      <input id="search" class="control" type="search" placeholder="Search paper, ID, title, category, subtype, or rationale…">
      <select id="progress-filter" class="control"><option value="all">All progress</option><option value="pending">Pending</option><option value="progress">In progress</option><option value="complete">Complete</option></select>
      <select id="relationship-filter" class="control"><option value="all">All relationships</option><option value="S_W">S_W · one report</option><option value="S_C">S_C · report cross-file</option><option value="P_R">P_R · report vs plan</option><option value="P_P">P_P · plan internal</option><option value="P_O">P_O · plan vs operations</option><option value="P_B">P_B · plan background</option></select>
      <select id="domain-filter" class="control"><option value="all">All review domains</option><option value="statistical_results">Statistical results</option><option value="internal_nonstatistical">Internal nonstatistical</option><option value="protocol_report">Protocol–report</option><option value="other_plan">Other plan material</option><option value="other">Other</option></select>
      <select id="analysis-filter" class="control"><option value="all">All analysis labels</option><option value="primary">Primary temporal eligible</option><option value="secondary">Secondary temporal eligible</option><option value="protocol">Protocol–report descriptive</option><option value="plan">Other plan descriptive</option><option value="not_eligible">Not temporal eligible</option><option value="undetermined">Eligibility undetermined</option></select>
      <details class="actions"><summary class="btn primary">Review actions ▾</summary><div class="menu">
        <button id="next-incomplete" class="btn">Next incomplete item</button><button id="expand-visible" class="btn">Expand visible</button><button id="collapse-all" class="btn">Collapse all</button>
        <button id="export-json" class="btn">Export reviewer snapshot (JSON)</button><button id="export-csv" class="btn">Export review table (CSV)</button><button id="download-html" class="btn">Download annotated HTML</button>
        <label class="btn" for="import-json">Resume from v.2.0.2 snapshot</label><input id="import-json" type="file" accept="application/json,.json">
        <label class="btn" for="start-checker-json">Start checker stage from primary JSON</label><input id="start-checker-json" type="file" accept="application/json,.json"><button id="print" class="btn">Print / Save PDF</button>
      </div></details>
    </div>

    <section class="stats" aria-label="Review progress">
      <div class="stat"><b id="stat-total">0</b><span>Total candidates</span></div><div class="stat"><b id="stat-complete">0</b><span id="stat-complete-label">Primary reviews complete</span></div>
      <div class="stat"><b id="stat-progress">0</b><span>In progress</span></div><div class="stat"><b id="stat-reproduced">0</b><span>Reproduced or partial</span></div>
      <div class="stat"><b id="stat-primary">0</b><span>Primary temporal eligible</span></div><div class="stat"><b id="stat-secondary">0</b><span>Secondary temporal eligible</span></div>
      <div class="stat"><b id="stat-protocol">0</b><span>Retained P_R descriptive</span></div>
    </section>

    <div class="notice"><strong id="stage-label">Primary stage:</strong><span id="stage-help">Complete and export the primary review before another reviewer starts the visible-answer checker stage. Document-role coding is context, not adjudication.</span><span id="save-status">Waiting for reviewer</span></div>
    <div id="candidate-groups"></div><div id="empty" class="empty" hidden>No candidates match the current filters.</div>
  </main>
  <footer class="page">V.2.0.2 · Candidate keys are year / package / candidate ID. Primary, checker, and proposed-final records remain separate. Temporal labels use the completed primary record or the completed checker-proposed final record.</footer>

  <div id="embedded-review-state" data-state="" hidden></div>
  <script id="candidate-data" type="application/json">__DATA_JSON__</script>
  <script>
  (() => {
    'use strict';
    const dataset = JSON.parse(document.getElementById('candidate-data').textContent);
    const candidates = dataset.candidates;
    const VERSION = 'v.2.0.2', SCHEMA = 5;
    const STORAGE_PREFIX = `human-adjudication-${VERSION}-${dataset.years[0]}`;
    let state = null, saveTimer = null;
    const embedded = decodeState(document.getElementById('embedded-review-state').dataset.state);
    const el = id => document.getElementById(id);
    const esc = value => String(value ?? '').replace(/[&<>\"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[ch]));
    const relationLabels = {S_W:'Within one main/non-plan supplement',S_C:'Main vs non-plan supplement / two non-plan supplements',P_R:'Report/results supplement vs protocol/SAP',P_P:'Protocol/SAP internal or versions',P_O:'Protocol/SAP vs operational document',P_B:'Historical/background result in protocol/SAP'};
    const domainLabels = {statistical_results:'Statistical results',internal_nonstatistical:'Internal nonstatistical inconsistency',protocol_report:'Protocol–report discrepancy',protocol_internal:'Protocol/SAP internal',protocol_operational:'Protocol vs operational document',protocol_background:'Protocol background data',other:'Other'};
    const opts = {
      verification:[['pending','Select…'],['reproduced','Reproduced'],['partly_reproduced','Partly reproduced'],['not_reproduced','Not reproduced'],['unable','Unable to determine']],
      disposition:[['pending','Select…'],['retain','Retain candidate flag'],['exclude','Exclude unsupported candidate'],['out_of_scope','Outside the prespecified review scope'],['discuss','Needs discussion']],
      domain:Object.entries(domainLabels), duplicateStatus:[['pending','Select…'],['distinct','Distinct candidate'],['exact_duplicate','Exact duplicate'],['uncertain','Uncertain']],
      statisticalErrorStatus:[['pending','Select…'],['confirmed_error','Confirmed statistical reporting error'],['probable_error','Probable statistical reporting error'],['not_error','Not a statistical error'],['indeterminate','Indeterminate']],
      substantiveStatus:[['pending','Select…'],['substantive','Substantive'],['minor_presentation','Minor / presentation-only'],['indeterminate','Indeterminate']],
      downstreamImpact:[['pending','Select…'],['direct','Direct extraction/analysis impact'],['possible','Possible downstream impact'],['unlikely','Unlikely downstream impact'],['unknown','Unable to assess']],
      internalStatus:[['pending','Select…'],['substantive_inconsistency','Substantive inconsistency'],['minor_presentation','Minor / presentation-only inconsistency'],['wording_only','Wording-only difference'],['not_inconsistency','Not an inconsistency'],['indeterminate','Indeterminate']],
      potentialConsequence:[['pending','Select…'],['data_extraction','Could affect data extraction'],['interpretation','Could affect interpretation'],['administrative','Administrative/procedural only'],['none','No material consequence identified'],['unknown','Unable to assess']],
      documentationStatus:[['pending','Select…'],['explicit','Change explicitly documented'],['partial','Partial or implicit documentation'],['none_located','No documentation located in reviewed materials'],['cannot_assess','Cannot assess'],['not_applicable','Not applicable']],
      justificationStatus:[['pending','Select…'],['explicit','Explicit justification located'],['none_located','No justification located in reviewed materials'],['cannot_assess','Cannot assess'],['not_applicable','Not applicable']],
      protocolInterpretation:[['pending','Select…'],['documented_justified','Documented and justified change'],['documented_no_justification','Documented; no justification located'],['undocumented_change_candidate','Possible undocumented change'],['wording_only','Wording-only / no substantive difference'],['version_timing','Version or timing ambiguity'],['not_reproduced','Discrepancy not reproduced'],['indeterminate','Indeterminate']],
      checkStatus:[['pending','Select…'],['agree','Agree with primary assessment'],['agree_clarification','Agree with clarification'],['disagree','Disagree; proposed final assessment edited below'],['unable','Unable to resolve / refer for discussion']]
    };
    function defaultRecord(c) { return {verification:'pending',disposition:'pending',domain:c.suggestedDomain,duplicateStatus:'pending',duplicateOf:'',relatedClusterId:'',evidenceChecked:'',decisionRationale:'',statisticalErrorStatus:'pending',substantiveStatus:'pending',downstreamImpact:'pending',internalStatus:'pending',potentialConsequence:'pending',documentationStatus:'pending',justificationStatus:'pending',protocolInterpretation:'pending',notes:'',reviewComplete:false,updatedAt:''}; }
    function cloneRecord(record,c) { return {...defaultRecord(c),...(record||{})}; }
    function stage() { return state?.stage||'primary'; }
    function primaryRecordFor(c) { return cloneRecord(stage()==='checker'?state?.primary?.reviews?.[c.key]:state?.reviews?.[c.key],c); }
    function checkFor(c) { return state?.checks?.[c.key]||null; }
    function recordFor(c) { return stage()==='checker'?cloneRecord(checkFor(c)?.finalRecord||primaryRecordFor(c),c):primaryRecordFor(c); }
    function normalizeId(value) { return value.trim().replace(/\s+/g,'_'); }
    function stateKey(value) { if(!value)return ''; return value.stage==='checker'?`${STORAGE_PREFIX}::checker::${encodeURIComponent(value.primary.reviewer.id)}::${encodeURIComponent(value.checker.id)}`:`${STORAGE_PREFIX}::primary::${encodeURIComponent(value.reviewer.id)}`; }
    function decodeState(encoded) { if (!encoded) return null; try { const binary=atob(encoded), bytes=new Uint8Array(binary.length); for(let i=0;i<binary.length;i++) bytes[i]=binary.charCodeAt(i); return JSON.parse(new TextDecoder().decode(bytes)); } catch (_) { return null; } }
    function encodeState(value) { const bytes=new TextEncoder().encode(JSON.stringify(value)); let binary=''; for(const byte of bytes) binary+=String.fromCharCode(byte); return btoa(binary); }
    function validBase(value) { return value && value.schemaVersion===SCHEMA && value.reviewVersion===VERSION && value.year===dataset.years[0] && value.sourceDigest===dataset.sourceDigest; }
    function validPrimary(value) { return validBase(value) && (value.stage||'primary')==='primary' && value.reviewer && value.reviews && typeof value.reviews==='object'; }
    function validChecker(value) { return validBase(value) && value.stage==='checker' && value.primary?.reviewer && value.primary?.reviews && value.checker && value.checks && typeof value.checks==='object'; }
    function validSnapshot(value) { return validPrimary(value)||validChecker(value); }
    function primaryComplete(value) { return validPrimary(value) && dataset.keySet.every(key=>{const c=candidates.find(candidate=>candidate.key===key),r=cloneRecord(value.reviews[key],c);return value.reviews[key]?.reviewComplete===true&&validate(c,r).length===0;}); }
    function mergePrimary(base,incoming) { if(!validPrimary(incoming)) return base; for(const [key,record] of Object.entries(incoming.reviews)){ if(!dataset.keySet.includes(key)) continue; const old=base.reviews[key]; if(!old || String(record.updatedAt||'')>=String(old.updatedAt||'')) base.reviews[key]=record; } if(incoming.reviewer.name) base.reviewer.name=incoming.reviewer.name; return base; }
    function activateReviewer(id,name,fromImport=null) {
      id=normalizeId(id); if(!id) return alert('Enter a reviewer ID.');
      let fresh={schemaVersion:SCHEMA,reviewVersion:VERSION,sourceDigest:dataset.sourceDigest,year:dataset.years[0],stage:'primary',reviewer:{id,name:name.trim()},reviews:{}};
      try { const local=JSON.parse(localStorage.getItem(stateKey(fresh))||'null'); if(validPrimary(local) && local.reviewer.id===id) fresh=mergePrimary(fresh,local); } catch (_) {}
      if(validPrimary(embedded) && embedded.reviewer.id===id) fresh=mergePrimary(fresh,embedded);
      if(validPrimary(fromImport)) fresh=mergePrimary(fresh,fromImport);
      if(name.trim()) fresh.reviewer.name=name.trim(); state=fresh;
      try { localStorage.setItem(`${STORAGE_PREFIX}::last-state-key`,stateKey(state)); } catch (_) {}
      el('reviewer-id').value=id; el('reviewer-name').value=state.reviewer.name||'';
      el('active-reviewer').textContent=`Active primary reviewer: ${id}${state.reviewer.name?' · '+state.reviewer.name:''}`;
      renderGroups(); updateAll(); saveState();
    }
    function activateChecker(primary,id,name,fromImport=null) {
      id=normalizeId(id); if(!id) return alert('Enter the checker ID before selecting the primary JSON.');
      if(!primaryComplete(primary)) return alert('The primary snapshot is incomplete. Complete all candidates and export it again.');
      if(id===primary.reviewer.id) return alert('The checker ID must differ from the primary reviewer ID.');
      let fresh={schemaVersion:SCHEMA,reviewVersion:VERSION,sourceDigest:dataset.sourceDigest,year:dataset.years[0],stage:'checker',primary:{reviewer:primary.reviewer,reviews:primary.reviews,exportedAt:primary.exportedAt||''},checker:{id,name:name.trim()},checks:{}};
      if(validChecker(fromImport)) fresh=fromImport;
      state=fresh; try { localStorage.setItem(`${STORAGE_PREFIX}::last-state-key`,stateKey(state)); } catch (_) {}
      el('reviewer-id').value=state.checker.id;el('reviewer-name').value=state.checker.name||'';el('active-reviewer').textContent=`Active checker: ${state.checker.id}${state.checker.name?' · '+state.checker.name:''} · primary: ${state.primary.reviewer.id}`;
      renderGroups();updateAll();saveState();
    }
    function saveState() { if(!state) return; clearTimeout(saveTimer); el('save-status').textContent='Saving…'; saveTimer=setTimeout(()=>{ try { const key=stateKey(state);localStorage.setItem(key,JSON.stringify(state));localStorage.setItem(`${STORAGE_PREFIX}::last-state-key`,key);el('save-status').textContent='Saved in browser; export JSON for archival'; } catch (_) { el('save-status').textContent='Browser storage unavailable; export JSON now'; } },160); }
    function progressFor(c) { if(stage()==='checker'){const check=checkFor(c);if(check?.checkComplete)return 'complete';if(check)return 'progress';return 'pending';} const stored=state?.reviews?.[c.key];if(stored?.reviewComplete)return 'complete';if(stored&&Object.keys(stored).some(k=>!['domain','reviewComplete','updatedAt'].includes(k)&&stored[k]&&stored[k]!=='pending'))return 'progress';return 'pending'; }
    function assessmentComplete(c) { return stage()==='checker'?Boolean(checkFor(c)?.checkComplete):Boolean(state?.reviews?.[c.key]?.reviewComplete); }
    function sameAssessment(c) { const primary=primaryRecordFor(c),final=recordFor(c),keys=Object.keys(defaultRecord(c)).filter(key=>!['reviewComplete','updatedAt'].includes(key));return keys.every(key=>String(primary[key]??'')===String(final[key]??'')); }
    function analysisFor(c,r) {
      if(!assessmentComplete(c)) return 'undetermined';
      const reproduced=['reproduced','partly_reproduced'].includes(r.verification), retained=r.disposition==='retain';
      if(c.primary==='P_R') return reproduced&&retained?'protocol':'not_eligible';
      if(['P_P','P_O','P_B'].includes(c.primary)) return reproduced&&retained?'plan':'not_eligible';
      if(!['S_C','S_W'].includes(c.primary) || !reproduced || !retained) return 'not_eligible';
      if(r.domain==='statistical_results' && ['confirmed_error','probable_error'].includes(r.statisticalErrorStatus) && r.substantiveStatus==='substantive') return 'primary';
      if(r.domain==='internal_nonstatistical' && r.internalStatus==='substantive_inconsistency') return 'secondary';
      return 'not_eligible';
    }
    function analysisLabel(value) { return {primary:'Primary temporal eligible',secondary:'Secondary temporal eligible',protocol:'Protocol–report descriptive',plan:'Other plan-material descriptive',not_eligible:'Not temporal eligible',undetermined:'Eligibility undetermined'}[value]; }
    function selectField(key,field,label,values,current,hint='') { return `<div class="field"><label>${esc(label)}</label><select data-key="${esc(key)}" data-field="${field}">${values.map(([v,l])=>`<option value="${esc(v)}" ${current===v?'selected':''}>${esc(l)}</option>`).join('')}</select>${hint?`<span class="hint">${esc(hint)}</span>`:''}</div>`; }
    function checkSelectField(key,field,label,values,current,hint='') { return `<div class="field"><label>${esc(label)}</label><select data-key="${esc(key)}" data-check-field="${field}">${values.map(([v,l])=>`<option value="${esc(v)}" ${current===v?'selected':''}>${esc(l)}</option>`).join('')}</select>${hint?`<span class="hint">${esc(hint)}</span>`:''}</div>`; }
    function inputField(key,field,label,current,placeholder='',wide='') { return `<div class="field ${wide}"><label>${esc(label)}</label><input data-key="${esc(key)}" data-field="${field}" value="${esc(current)}" placeholder="${esc(placeholder)}"></div>`; }
    function areaField(key,field,label,current,placeholder='',wide='full') { return `<div class="field ${wide}"><label>${esc(label)}</label><textarea data-key="${esc(key)}" data-field="${field}" placeholder="${esc(placeholder)}">${esc(current)}</textarea></div>`; }
    function checkAreaField(key,field,label,current,placeholder='',wide='full') { return `<div class="field ${wide}"><label>${esc(label)}</label><textarea data-key="${esc(key)}" data-check-field="${field}" placeholder="${esc(placeholder)}">${esc(current)}</textarea></div>`; }
    function primarySummary(c) { const r=primaryRecordFor(c), fields=[['Reviewer',state.primary.reviewer.id],['Verification',r.verification],['Disposition',r.disposition],['Domain',r.domain],['Duplicate status',r.duplicateStatus],['Statistical error status',r.statisticalErrorStatus],['Substantiveness',r.substantiveStatus],['Internal assessment',r.internalStatus],['Potential consequence',r.potentialConsequence],['Protocol documentation',r.documentationStatus],['Protocol justification',r.justificationStatus],['Protocol interpretation',r.protocolInterpretation],['Evidence checked',r.evidenceChecked],['Rationale',r.decisionRationale],['Notes',r.notes]].filter(([,v])=>v&&v!=='pending');return `<div class="primary-readonly"><h3>Locked primary assessment · ${esc(state.primary.reviewer.id)}</h3><dl>${fields.map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl></div>`; }
    function candidateHtml(c) {
      const r=recordFor(c), progress=progressFor(c), analysis=analysisFor(c,r);
      const check=stage()==='checker'?(checkFor(c)||{}):null;
      const evidence=Object.entries(c.evidence).map(([name,value])=>`<h4>${esc(name)}</h4><p>${esc(value)}</p>`).join('');
      const direct=c.sourceLinks.map(link=>`<a class="source-link" href="${esc(link.href)}" target="_blank">${esc(link.label)}</a>`).join('');
      const deeper=c.evidencePaths.map(link=>`<a class="source-link" href="${esc(link.href)}" target="_blank">${esc(link.label.split('/').slice(-2).join('/'))}</a>`).join('');
      const warnings=[c.evidenceState!=='recorded_candidate'?`Evidence state: ${c.evidenceState}`:'',c.additionalSensitivityExclude?'Additional sensitivity exclusion':''].filter(Boolean);
      return `<li data-candidate-key="${esc(c.key)}"><details class="candidate" data-search="${esc([c.year,c.package,c.id,c.sourceId,c.title,c.statement,c.category,c.subtype,c.rationale,c.primary].join(' ').toLowerCase())}">
        <summary><span class="candidate-id">${esc(c.id)}</span><span class="candidate-title">${esc(c.title)}</span><span class="analysis-pill ${analysis}" data-analysis-badge>${esc(analysisLabel(analysis))}</span><span class="badge ${progress}" data-progress-badge>${progress==='complete'?'Complete':progress==='progress'?'In progress':'Pending'}</span></summary>
        <div class="candidate-body">
          <div class="metadata"><span class="chip">${esc(c.year)} / ${esc(c.package)} / ${esc(c.id)}</span><span class="chip relationship">${esc(c.primary)} · ${esc(relationLabels[c.primary]||c.primary)}</span><span class="chip">Original category: ${esc(c.category||'not stated')}</span><span class="chip">Subtype: ${esc(c.subtype||'not coded')}</span>${warnings.map(w=>`<span class="chip warning">${esc(w)}</span>`).join('')}</div>
          ${c.statement?`<p class="statement"><strong>Candidate statement:</strong> ${esc(c.statement)}</p>`:''}
          <div class="source-row"><a class="source-link" href="${esc(c.reportHref)}" target="_blank">Open full source report</a>${direct}${c.locations&&!direct?`<span>${esc(c.locations)}</span>`:''}</div>
          ${evidence?`<details class="evidence-box"><summary><strong>Candidate evidence and verification guidance</strong></summary>${evidence}</details>`:''}
          <details class="coding-box"><summary>Post-hoc document-role coding — context only, not adjudication</summary><div class="coding-grid"><p><strong>Suggested review domain:</strong> ${esc(domainLabels[c.suggestedDomain])}</p><p><strong>Relations:</strong> ${esc(c.relations.join(', '))}</p><p class="full"><strong>Rationale:</strong> ${esc(c.rationale)}</p>${c.ambiguity?`<p class="full"><strong>Ambiguity:</strong> ${esc(c.ambiguity)}</p>`:''}${c.planMechanism?`<p><strong>Protocol mechanism:</strong> ${esc(c.planMechanism)}</p>`:''}<p><strong>Evidence state:</strong> ${esc(c.evidenceState)}</p><div class="source-row">${deeper}</div></div></details>
          ${stage()==='checker'?primarySummary(c):''}
          <div class="review-panel ${state?'':'locked'}" data-review-panel>
            <h3 class="section-title">${stage()==='checker'?'Checker-proposed final assessment':'Primary reviewer assessment'}</h3>
            <div class="review-grid">
              ${selectField(c.key,'verification','Flag verification',opts.verification,r.verification)}
              ${selectField(c.key,'disposition','Candidate disposition',opts.disposition,r.disposition)}
              ${selectField(c.key,'domain','Review domain',opts.domain,r.domain,'Initial value is routing guidance and may be changed.')}
              ${selectField(c.key,'duplicateStatus','Duplicate status',opts.duplicateStatus,r.duplicateStatus)}
              ${inputField(c.key,'duplicateOf','Exact duplicate of candidate key',r.duplicateOf,'Required only for exact duplicate')}
              ${inputField(c.key,'relatedClusterId','Related issue cluster ID',r.relatedClusterId,'Optional; distinct flags may share a cluster')}
            </div>
            <div class="module" data-module="statistical" ${r.domain==='statistical_results'?'':'hidden'}><h3 class="section-title">Statistical-results assessment</h3><div class="review-grid">
              ${selectField(c.key,'statisticalErrorStatus','Statistical error status',opts.statisticalErrorStatus,r.statisticalErrorStatus)}
              ${selectField(c.key,'substantiveStatus','Substantiveness',opts.substantiveStatus,r.substantiveStatus)}
              ${selectField(c.key,'downstreamImpact','Potential downstream impact',opts.downstreamImpact,r.downstreamImpact)}
            </div></div>
            <div class="module" data-module="protocol" ${r.domain==='protocol_report'?'':'hidden'}><h3 class="section-title">Protocol–report discrepancy assessment</h3><div class="review-grid">
              ${selectField(c.key,'documentationStatus','Change documentation',opts.documentationStatus,r.documentationStatus)}
              ${selectField(c.key,'justificationStatus','Change justification',opts.justificationStatus,r.justificationStatus)}
              ${selectField(c.key,'protocolInterpretation','Interpretation',opts.protocolInterpretation,r.protocolInterpretation)}
              ${selectField(c.key,'potentialConsequence','Potential consequence',opts.potentialConsequence,r.potentialConsequence)}
            </div></div>
            <div class="module" data-module="nonstat" ${['statistical_results','protocol_report'].includes(r.domain)?'hidden':''}><h3 class="section-title">Non-error inconsistency/discrepancy assessment</h3><div class="review-grid">
              ${selectField(c.key,'internalStatus','Assessment',opts.internalStatus,r.internalStatus)}
              ${selectField(c.key,'potentialConsequence','Potential consequence',opts.potentialConsequence,r.potentialConsequence)}
            </div></div>
            <div class="review-grid">${areaField(c.key,'evidenceChecked',stage()==='checker'?'Evidence checked by primary/checker':'Evidence personally checked',r.evidenceChecked,'Sources/pages/calculations checked')}${areaField(c.key,'decisionRationale',stage()==='checker'?'Proposed final rationale':'Primary assessment rationale',r.decisionRationale,'Explain the verification, disposition, and domain-specific judgment')}${areaField(c.key,'notes','Additional notes',r.notes,'Uncertainty or points for discussion')}</div>
            ${stage()==='checker'?`<div class="checker-box"><h3 class="section-title">Second-person check</h3><div class="review-grid">${checkSelectField(c.key,'checkStatus','Check result',opts.checkStatus,check.checkStatus||'pending')}${checkAreaField(c.key,'checkerComment','Checker comment',check.checkerComment||'','Required for clarification, disagreement, or unresolved cases','wide')}</div><button class="btn" data-action="reset-primary" data-key="${esc(c.key)}">Reset proposed final to primary</button></div>`:''}
            <div class="completion"><button class="btn primary" data-action="complete" data-key="${esc(c.key)}">${stage()==='checker'?'Mark second-person check complete':'Mark primary review complete'}</button><button class="btn" data-action="reopen" data-key="${esc(c.key)}" ${progress==='complete'?'':'hidden'}>Reopen</button><span class="analysis-pill ${analysis}" data-analysis-text>${esc(analysisLabel(analysis))}</span><span class="validation" data-validation></span></div>
          </div>
        </div></details></li>`;
    }
    function renderGroups() {
      const packages=[...new Set(candidates.map(c=>c.package))];
      el('candidate-groups').innerHTML=`<details class="group year" open><summary>${dataset.years[0]} <span class="group-count">${packages.length} papers · ${candidates.length} candidates</span></summary>${packages.map(pkg=>{const items=candidates.filter(c=>c.package===pkg); return `<details class="group paper" data-package="${esc(pkg)}"><summary>${esc(pkg)} <span class="group-count">${items.length} candidates</span></summary><ul class="candidate-list">${items.map(candidateHtml).join('')}</ul></details>`;}).join('')}</details>`;
    }
    function validate(c,r) {
      const missing=[]; if(r.verification==='pending') missing.push('flag verification'); if(r.disposition==='pending') missing.push('candidate disposition'); if(!r.domain) missing.push('review domain');
      if(r.duplicateStatus==='pending') missing.push('duplicate status'); if(r.duplicateStatus==='exact_duplicate'&&!r.duplicateOf.trim()) missing.push('duplicate candidate key'); if(!r.evidenceChecked.trim()) missing.push('evidence checked'); if(!r.decisionRationale.trim()) missing.push('assessment rationale');
      const active=['reproduced','partly_reproduced'].includes(r.verification) && r.disposition==='retain';
      if(active&&r.domain==='statistical_results'){ if(r.statisticalErrorStatus==='pending') missing.push('statistical error status'); if(r.substantiveStatus==='pending') missing.push('substantiveness'); if(r.downstreamImpact==='pending') missing.push('downstream impact'); }
      else if(active&&r.domain==='protocol_report'){ if(r.documentationStatus==='pending') missing.push('change documentation'); if(r.justificationStatus==='pending') missing.push('change justification'); if(r.protocolInterpretation==='pending') missing.push('protocol interpretation'); if(r.potentialConsequence==='pending') missing.push('potential consequence'); }
      else if(active){ if(r.internalStatus==='pending') missing.push('non-error assessment'); if(r.potentialConsequence==='pending') missing.push('potential consequence'); }
      return missing;
    }
    function updateRecord(key,field,value) { if(!state)return;const c=candidates.find(x=>x.key===key),now=new Date().toISOString();if(stage()==='checker'){const old=checkFor(c)||{checkStatus:'pending',checkerComment:'',finalRecord:primaryRecordFor(c),checkComplete:false};state.checks[key]={...old,finalRecord:{...recordFor(c),[field]:value,reviewComplete:true,updatedAt:now},checkComplete:false,updatedAt:now};}else{state.reviews[key]={...recordFor(c),[field]:value,reviewComplete:false,updatedAt:now};}if(field==='domain')updateModules(key,value);updateItem(key);saveState();updateStats();applyFilters(); }
    function updateCheckField(key,field,value) { if(stage()!=='checker')return;const c=candidates.find(x=>x.key===key),old=checkFor(c)||{checkStatus:'pending',checkerComment:'',finalRecord:primaryRecordFor(c),checkComplete:false};state.checks[key]={...old,[field]:value,checkComplete:false,updatedAt:new Date().toISOString()};updateItem(key);saveState();updateStats();applyFilters(); }
    function updateModules(key,domain) { const item=document.querySelector(`[data-candidate-key="${CSS.escape(key)}"]`); if(!item) return; item.querySelector('[data-module="statistical"]').hidden=domain!=='statistical_results'; item.querySelector('[data-module="protocol"]').hidden=domain!=='protocol_report'; item.querySelector('[data-module="nonstat"]').hidden=['statistical_results','protocol_report'].includes(domain); }
    function updateItem(key) { const c=candidates.find(x=>x.key===key),r=recordFor(c),item=document.querySelector(`[data-candidate-key="${CSS.escape(key)}"]`);if(!item)return;const progress=progressFor(c),analysis=analysisFor(c,r),badge=item.querySelector('[data-progress-badge]');badge.className=`badge ${progress}`;badge.textContent=progress==='complete'?'Complete':progress==='progress'?'In progress':'Pending';for(const node of item.querySelectorAll('[data-analysis-badge],[data-analysis-text]')){node.className=`analysis-pill ${analysis}`;node.textContent=analysisLabel(analysis);}const reopen=item.querySelector('[data-action="reopen"]');reopen.hidden=progress!=='complete'; }
    function completeReview(key) { if(!state)return alert('Create or load a reviewer first.');const c=candidates.find(x=>x.key===key),r=recordFor(c),missing=validate(c,r),item=document.querySelector(`[data-candidate-key="${CSS.escape(key)}"]`),message=item.querySelector('[data-validation]');if(stage()==='checker'){const check=checkFor(c)||{};if(!check.checkStatus||check.checkStatus==='pending')missing.push('check result');if(check.checkStatus&&check.checkStatus!=='agree'&&!String(check.checkerComment||'').trim())missing.push('checker comment');if(check.checkStatus==='agree'&&!sameAssessment(c))missing.push('use “Agree with clarification”/“Disagree,” or reset the proposed final to primary');}if(missing.length){message.textContent=`Complete: ${missing.join(', ')}.`;return;}const now=new Date().toISOString();if(stage()==='checker'){const old=checkFor(c)||{};state.checks[key]={...old,finalRecord:{...r,reviewComplete:true,updatedAt:now},checkComplete:true,updatedAt:now};message.textContent='Second-person check marked complete.';}else{state.reviews[key]={...r,reviewComplete:true,updatedAt:now};message.textContent='Primary review marked complete.';}updateItem(key);saveState();updateStats();applyFilters(); }
    function reopenReview(key) { if(!state)return;const c=candidates.find(x=>x.key===key),now=new Date().toISOString();if(stage()==='checker'){const old=checkFor(c)||{checkStatus:'pending',checkerComment:'',finalRecord:primaryRecordFor(c)};state.checks[key]={...old,checkComplete:false,updatedAt:now};}else{state.reviews[key]={...recordFor(c),reviewComplete:false,updatedAt:now};}updateItem(key);saveState();updateStats();applyFilters(); }
    function resetToPrimary(key) { if(stage()!=='checker')return;const c=candidates.find(x=>x.key===key),old=checkFor(c)||{checkStatus:'pending',checkerComment:''};state.checks[key]={...old,finalRecord:{...primaryRecordFor(c),reviewComplete:true},checkComplete:false,updatedAt:new Date().toISOString()};renderGroups();updateAll();saveState(); }
    function domainFilterMatch(domain,filter) { if(filter==='all') return true; if(filter==='other_plan') return ['protocol_internal','protocol_operational','protocol_background'].includes(domain); return domain===filter; }
    function applyFilters() { const query=el('search').value.trim().toLowerCase(),progress=el('progress-filter').value,relationship=el('relationship-filter').value,domain=el('domain-filter').value,analysis=el('analysis-filter').value;let visible=0;
      document.querySelectorAll('[data-candidate-key]').forEach(item=>{const c=candidates.find(x=>x.key===item.dataset.candidateKey),r=recordFor(c),p=progressFor(c),a=analysisFor(c,r),details=item.querySelector('details.candidate');const show=(!query||details.dataset.search.includes(query))&&(progress==='all'||p===progress)&&(relationship==='all'||c.primary===relationship)&&domainFilterMatch(r.domain,domain)&&(analysis==='all'||a===analysis);item.hidden=!show;if(show)visible++;});
      document.querySelectorAll('details.paper').forEach(p=>{const show=[...p.querySelectorAll('[data-candidate-key]')].some(i=>!i.hidden);p.hidden=!show;if(show&&(query||progress!=='all'||relationship!=='all'||domain!=='all'||analysis!=='all'))p.open=true;});el('empty').hidden=visible!==0;
    }
    function updateStats() { const counts={complete:0,progress:0,reproduced:0,primary:0,secondary:0,protocol:0}; for(const c of candidates){const r=recordFor(c),p=progressFor(c),a=analysisFor(c,r);if(p==='complete')counts.complete++;if(p==='progress')counts.progress++;if(['reproduced','partly_reproduced'].includes(r.verification))counts.reproduced++;if(a==='primary')counts.primary++;if(a==='secondary')counts.secondary++;if(a==='protocol')counts.protocol++;} el('stat-total').textContent=candidates.length;for(const key of ['complete','progress','reproduced','primary','secondary','protocol'])el(`stat-${key}`).textContent=counts[key]; }
    function updateAll(){const checker=stage()==='checker';el('stage-label').textContent=checker?'Checker stage:':'Primary stage:';el('stage-help').textContent=checker?'Review the locked primary assessment, verify the evidence, and record agreement or a proposed final revision. Primary answers are never overwritten.':'Complete and export the primary review before another reviewer starts the visible-answer checker stage. Document-role coding is context, not adjudication.';el('stat-complete-label').textContent=checker?'Second-person checks complete':'Primary reviews complete';updateStats();applyFilters();}
    function snapshot(){return {...state,exportedAt:new Date().toISOString()};}
    function download(name,content,type){const url=URL.createObjectURL(new Blob([content],{type})),link=document.createElement('a');link.href=url;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
    function requireReviewer(){if(!state){alert('Create or load a reviewer first.');return false;}return true;}
    function csvCell(value){const s=String(value??'');return /[\",\n]/.test(s)?`\"${s.replaceAll('\"','\"\"')}\"`:s;}
    el('activate-reviewer').addEventListener('click',()=>activateReviewer(el('reviewer-id').value,el('reviewer-name').value));
    el('reviewer-name').addEventListener('change',()=>{if(!state)return;const name=el('reviewer-name').value.trim();if(stage()==='checker'){state.checker.name=name;el('active-reviewer').textContent=`Active checker: ${state.checker.id}${name?' · '+name:''} · primary: ${state.primary.reviewer.id}`;}else{state.reviewer.name=name;el('active-reviewer').textContent=`Active primary reviewer: ${state.reviewer.id}${name?' · '+name:''}`;}saveState();});
    document.addEventListener('input',event=>{const t=event.target;if(t.dataset?.field)updateRecord(t.dataset.key,t.dataset.field,t.value);});
    document.addEventListener('change',event=>{const t=event.target;if(t.dataset?.field)updateRecord(t.dataset.key,t.dataset.field,t.value);});
    document.addEventListener('input',event=>{const t=event.target;if(t.dataset?.checkField)updateCheckField(t.dataset.key,t.dataset.checkField,t.value);});
    document.addEventListener('change',event=>{const t=event.target;if(t.dataset?.checkField)updateCheckField(t.dataset.key,t.dataset.checkField,t.value);});
    document.addEventListener('click',event=>{const b=event.target.closest('[data-action]');if(!b)return;if(b.dataset.action==='complete')completeReview(b.dataset.key);if(b.dataset.action==='reopen')reopenReview(b.dataset.key);if(b.dataset.action==='reset-primary')resetToPrimary(b.dataset.key);});
    for(const id of ['search','progress-filter','relationship-filter','domain-filter','analysis-filter'])el(id).addEventListener(id==='search'?'input':'change',applyFilters);
    el('expand-visible').addEventListener('click',()=>document.querySelectorAll('details:not([hidden])').forEach(d=>d.open=true)); el('collapse-all').addEventListener('click',()=>document.querySelectorAll('details.group,details.candidate').forEach(d=>d.open=false));
    el('next-incomplete').addEventListener('click',()=>{const item=[...document.querySelectorAll('[data-candidate-key]')].find(i=>!i.hidden&&progressFor(candidates.find(c=>c.key===i.dataset.candidateKey))!=='complete');if(!item)return alert('No visible incomplete candidates.');let p=item.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}item.querySelector('details.candidate').open=true;item.scrollIntoView({behavior:'smooth',block:'center'});});
    function identity(){return stage()==='checker'?`${state.primary.reviewer.id}-checked-by-${state.checker.id}`:state.reviewer.id;}
    el('export-json').addEventListener('click',()=>{if(!requireReviewer())return;download(`flag-review-${VERSION}-${dataset.years[0]}-${identity()}-${new Date().toISOString().slice(0,10)}.json`,JSON.stringify(snapshot(),null,2),'application/json');});
    el('export-csv').addEventListener('click',()=>{if(!requireReviewer())return;const fields=Object.keys(defaultRecord(candidates[0])),base=['year','package','candidate_id','candidate_key','primary_relationship','relations','original_category','subtype','evidence_state','suggested_domain'];let headers,rows;if(stage()==='checker'){headers=[...base,'primary_reviewer_id','checker_id','check_status','checker_comment','check_complete',...fields.map(f=>`primary_${f}`),...fields.map(f=>`final_${f}`),'derived_analysis_label'];rows=candidates.map(c=>{const p=primaryRecordFor(c),r=recordFor(c),ch=checkFor(c)||{};return [c.year,c.package,c.id,c.key,c.primary,c.relations.join('|'),c.category,c.subtype,c.evidenceState,c.suggestedDomain,state.primary.reviewer.id,state.checker.id,ch.checkStatus||'pending',ch.checkerComment||'',Boolean(ch.checkComplete),...fields.map(f=>p[f]),...fields.map(f=>r[f]),analysisFor(c,r)].map(csvCell).join(',');});}else{headers=[...base,'reviewer_id','reviewer_name',...fields,'derived_analysis_label'];rows=candidates.map(c=>{const r=recordFor(c);return [c.year,c.package,c.id,c.key,c.primary,c.relations.join('|'),c.category,c.subtype,c.evidenceState,c.suggestedDomain,state.reviewer.id,state.reviewer.name,...fields.map(f=>r[f]),analysisFor(c,r)].map(csvCell).join(',');});}download(`flag-review-${VERSION}-${dataset.years[0]}-${identity()}.csv`,[headers.join(','),...rows].join('\n'),'text/csv;charset=utf-8');});
    el('download-html').addEventListener('click',()=>{if(!requireReviewer())return;const clone=document.documentElement.cloneNode(true),target=clone.querySelector('#embedded-review-state');target.dataset.state=encodeState(snapshot());download(`candidate-flag-review-${VERSION}-${dataset.years[0]}-${identity()}-annotated.html`,'<!doctype html>\n'+clone.outerHTML,'text/html;charset=utf-8');});
    function primaryFromChecker(value){return {schemaVersion:SCHEMA,reviewVersion:VERSION,sourceDigest:dataset.sourceDigest,year:dataset.years[0],stage:'primary',reviewer:value.primary.reviewer,reviews:value.primary.reviews,exportedAt:value.primary.exportedAt||''};}
    el('import-json').addEventListener('change',async event=>{const file=event.target.files[0];if(!file)return;try{const incoming=JSON.parse(await file.text());if(validPrimary(incoming))activateReviewer(incoming.reviewer.id,incoming.reviewer.name||'',incoming);else if(validChecker(incoming))activateChecker(primaryFromChecker(incoming),incoming.checker.id,incoming.checker.name||'',incoming);else throw new Error('Snapshot version, year, digest, or schema does not match this HTML.');}catch(error){alert(`Could not import snapshot: ${error.message}`);}finally{event.target.value='';}});
    el('start-checker-json').addEventListener('change',async event=>{const file=event.target.files[0];if(!file)return;try{const primary=JSON.parse(await file.text());if(!validPrimary(primary))throw new Error('Select a matching completed v.2.0.2 primary snapshot.');activateChecker(primary,el('reviewer-id').value,el('reviewer-name').value);}catch(error){alert(`Could not start checker stage: ${error.message}`);}finally{event.target.value='';}});
    el('print').addEventListener('click',()=>{document.querySelectorAll('details.group,details.candidate,.evidence-box,.coding-box').forEach(d=>d.open=true);window.print();});
    renderGroups(); updateAll();
    let initial=null;if(validSnapshot(embedded))initial=embedded;else{try{const key=localStorage.getItem(`${STORAGE_PREFIX}::last-state-key`);if(key){const local=JSON.parse(localStorage.getItem(key)||'null');if(validSnapshot(local))initial=local;}}catch(_){}}
    if(validPrimary(initial))activateReviewer(initial.reviewer.id,initial.reviewer.name||'',initial);else if(validChecker(initial))activateChecker(primaryFromChecker(initial),initial.checker.id,initial.checker.name||'',initial);
  })();
  </script>
</body></html>'''


def validate_source(rows: list[dict[str, object]]) -> None:
    if len(rows) != 412:
        raise RuntimeError(f"Expected 412 candidates, found {len(rows)}")
    keys = [str(row["key"]) for row in rows]
    if len(keys) != len(set(keys)):
        raise RuntimeError("Candidate keys are not unique")
    year_counts = Counter(str(row["year"]) for row in rows)
    if dict(year_counts) != EXPECTED_YEAR_COUNTS:
        raise RuntimeError(f"Unexpected year counts: {dict(year_counts)}")
    primary_counts = Counter(str(row["primary"]) for row in rows)
    if dict(primary_counts) != EXPECTED_PRIMARY_COUNTS:
        raise RuntimeError(f"Unexpected primary counts: {dict(primary_counts)}")
    missing = [str(row["reportPath"]) for row in rows if not (ROOT / str(row["reportPath"])).is_file()]
    if missing:
        raise RuntimeError(f"Missing report paths: {missing[:5]}")


def validate_local_links(rows: list[dict[str, object]]) -> int:
    checked = 0
    missing: list[str] = []
    for row in rows:
        links = [str(row["reportHref"])]
        links.extend(str(link["href"]) for link in row["sourceLinks"])
        links.extend(str(link["href"]) for link in row["evidencePaths"])
        for href in links:
            if not href or re.match(r"^[a-z]+://", href, flags=re.IGNORECASE):
                continue
            target = (OUT_DIR / unquote(href.split("#", 1)[0])).resolve()
            checked += 1
            if not target.is_file():
                missing.append(f"{row['key']}: {href}")
    if missing:
        raise RuntimeError("Missing local link targets:\n" + "\n".join(missing[:20]))
    return checked


def main() -> None:
    rows = json.loads(SOURCE.read_text(encoding="utf-8"))
    validate_source(rows)
    built_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    source_digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    validation_lines = [
        "# V.2.0.2 build validation",
        "",
        f"- Build time: {built_at}",
        f"- Source: `{SOURCE.relative_to(ROOT)}`",
        f"- Source SHA256: `{source_digest}`",
        "- Candidate keys: 412 unique keys",
        "- Relationship counts: " + ", ".join(f"{k}={v}" for k, v in EXPECTED_PRIMARY_COUNTS.items()),
        "- Referenced final-report paths: all present",
        "- Embedded candidate JSON: parsed and reconciled for every output",
        "- Two-stage workflow markers: primary, checker, locked primary, proposed final, and reset action present",
        "- Review schema: 5 (v.2.0.2 snapshots only; no automatic v.2.0.1 migration)",
        "",
        "| Year | Papers | Candidates | Output |",
        "|---|---:|---:|---|",
    ]
    checked_links = 0
    for year in YEARS:
        year_rows = [compact_row(row) for row in rows if str(row["year"]) == year]
        checked_links += validate_local_links(year_rows)
        digest = hashlib.sha256(json.dumps(year_rows, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        payload = {"schemaVersion": SCHEMA_VERSION, "reviewVersion": VERSION, "sourceDigest": digest, "classificationSourceDigest": source_digest, "years": [year], "keySet": [row["key"] for row in year_rows], "candidates": year_rows}
        data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        package_count = len({str(row["package"]) for row in year_rows})
        rendered = (HTML_TEMPLATE.replace("__YEAR__", year).replace("__GENERATED__", built_at).replace("__PACKAGES__", str(package_count)).replace("__TOTAL__", str(len(year_rows))).replace("__DIGEST_SHORT__", digest[:12]).replace("__DATA_JSON__", data_json))
        output = OUT_DIR / f"candidate_flag_review_v_2_0_2_{year}.html"
        output.write_text(rendered, encoding="utf-8")
        check = output.read_text(encoding="utf-8")
        required_markers = [
            "Version v.2.0.2",
            f'"sourceDigest":"{digest}"',
            "Start checker stage from primary JSON",
            "Locked primary assessment",
            "Checker-proposed final assessment",
            "Reset proposed final to primary",
            "checkStatus",
            "out_of_scope",
            "const VERSION = 'v.2.0.2', SCHEMA = 5",
        ]
        missing_markers = [marker for marker in required_markers if marker not in check]
        if missing_markers:
            raise RuntimeError(f"Generated marker validation failed for {output}: {missing_markers}")
        embedded_match = re.search(
            r'<script id="candidate-data" type="application/json">(.*?)</script>',
            check,
            flags=re.DOTALL,
        )
        if not embedded_match:
            raise RuntimeError(f"Embedded candidate JSON not found: {output}")
        embedded_payload = json.loads(embedded_match.group(1))
        if embedded_payload["keySet"] != [row["key"] for row in year_rows]:
            raise RuntimeError(f"Embedded candidate keys do not reconcile: {output}")
        validation_lines.append(f"| {year} | {package_count} | {len(year_rows)} | `{output.name}` |")
        print(f"Wrote {output.relative_to(ROOT)}: {package_count} papers, {len(year_rows)} candidates, {digest[:12]}")
    validation_lines.extend(["", f"Local report/evidence/source links checked: {checked_links}", "", "Result: **PASS**", ""])
    (OUT_DIR / "VALIDATION.md").write_text("\n".join(validation_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
