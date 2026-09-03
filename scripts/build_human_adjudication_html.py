#!/usr/bin/env python3
"""Build year-specific, self-contained human-adjudication HTML files.

The source reports remain authoritative. This script extracts only concise
identification fields from the current package-level final report in each
2018, 2019, 2024, and 2025 package.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "human_adjudication"
YEARS = ("2018", "2019", "2024", "2025")


def output_for(year: str) -> Path:
    return OUTPUT_DIR / f"candidate_error_adjudication_{year}.html"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
CANDIDATE_RE = re.compile(
    r"^(?P<label>(?:C\s*-?\s*\d{1,3}|V\s*-?\s*\d{1,3}|\d{1,3}))\s*[—–-]\s*(?P<title>.+?)\s*$",
    re.IGNORECASE,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:<([^>]+)>|([^)]+))\)")


def select_report(package: Path) -> Path:
    report_dir = package / ".ai_paper_validation"
    versioned = sorted(report_dir.glob("final_report_1_*.md"))
    if versioned:
        return versioned[-1]
    fallback = report_dir / "final_report.md"
    if fallback.is_file():
        return fallback
    raise FileNotFoundError(f"No final Markdown report found in {package.relative_to(ROOT)}")


def normalize_label(label: str) -> tuple[str, int]:
    compact = re.sub(r"\s+", "", label).upper()
    match = re.search(r"(\d+)", compact)
    if not match:
        raise ValueError(f"Cannot normalize candidate label: {label}")
    number = int(match.group(1))
    prefix = "V" if compact.startswith("V") else "C"
    return f"{prefix}{number:03d}", number


def clean_inline_markdown(value: str) -> str:
    value = MD_LINK_RE.sub(lambda m: m.group(1), value)
    value = value.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", value).strip()


def field_value(body: str, names: tuple[str, ...]) -> str:
    for name in names:
        pattern = re.compile(rf"^\*\*{re.escape(name)}:\*\*\s*(.*)$", re.MULTILINE | re.IGNORECASE)
        match = pattern.search(body)
        if match:
            value = match.group(1).strip()
            if value:
                return clean_inline_markdown(value)
    return ""


def location_block(body: str) -> str:
    inline = re.search(
        r"^\*\*Exact source locations?:\*\*\s*(.+)$",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    if inline:
        return inline.group(1).strip()

    lines = body.splitlines()
    for index, line in enumerate(lines):
        heading = HEADING_RE.match(line)
        if heading and re.fullmatch(r"Exact source locations?", heading.group(2), re.IGNORECASE):
            collected: list[str] = []
            for following in lines[index + 1 :]:
                if HEADING_RE.match(following):
                    break
                if not following.strip() and collected:
                    break
                if following.strip():
                    collected.append(following.strip())
            return " ".join(collected)
    return ""


def resolve_href(report: Path, target: str) -> str:
    target = target.strip().strip("<>")
    if re.match(r"^[a-z]+://", target, re.IGNORECASE):
        return target
    path_part, separator, fragment = target.partition("#")
    resolved = (report.parent / path_part).resolve()
    try:
        relative = resolved.relative_to(ROOT)
    except ValueError:
        return target
    href = "../" + relative.as_posix()
    if separator:
        href += "#" + fragment
    return href


def source_links(report: Path, block: str) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for match in MD_LINK_RE.finditer(block):
        label = clean_inline_markdown(match.group(1))
        target = match.group(2) or match.group(3) or ""
        href = resolve_href(report, target)
        item = (label, href)
        if item not in seen:
            seen.add(item)
            links.append({"label": label, "href": href})
    return links


def contextual_status(section: str, versioned: bool) -> str:
    lower = section.lower()
    if "verified scientific" in lower or lower == "scientific findings":
        return "Reported as verified"
    if "uncertain candidate" in lower:
        return "Reported as uncertain"
    if "rejected" in lower or "excluded interpretation" in lower:
        return "Reported as rejected/excluded"
    if versioned:
        return "Pending Human Adjudication"
    return "Source status not stated"


def parse_report(year: str, package: Path, report: Path) -> list[dict[str, object]]:
    text = report.read_text(encoding="utf-8")
    lines = text.splitlines()
    versioned = report.name.startswith("final_report_1_")
    candidates: list[dict[str, object]] = []
    current_section = ""

    for index, line in enumerate(lines):
        heading = HEADING_RE.match(line)
        if not heading:
            continue
        level = len(heading.group(1))
        heading_text = heading.group(2).strip()

        match = CANDIDATE_RE.match(heading_text)
        if not match:
            if level <= 2:
                current_section = re.sub(r"^\d+\.\s*", "", heading_text).strip()
            continue

        raw_label = match.group("label").strip()
        # Bare numeric headings are candidates only inside the formal finding sections.
        if raw_label.isdigit() and not any(
            marker in current_section.lower()
            for marker in ("verified scientific", "uncertain candidate", "rejected")
        ):
            continue

        title = clean_inline_markdown(match.group("title"))
        if "unused candidate slot" in title.lower():
            continue

        end = len(lines)
        for next_index in range(index + 1, len(lines)):
            next_heading = HEADING_RE.match(lines[next_index])
            if next_heading and len(next_heading.group(1)) <= level:
                end = next_index
                break
        body = "\n".join(lines[index + 1 : end])
        normalized, number = normalize_label(raw_label)
        location = location_block(body)
        report_html = report.with_suffix(".html")
        report_target = report_html if report_html.is_file() else report

        candidates.append(
            {
                "key": f"{year}::{package.name}::{normalized}",
                "year": year,
                "package": package.name,
                "id": normalized,
                "sourceId": re.sub(r"\s+", "", raw_label).upper(),
                "number": number,
                "title": title,
                "statement": field_value(body, ("Candidate statement", "Finding statement", "Issue statement")),
                "category": field_value(body, ("Category",)),
                "sourceStatus": contextual_status(current_section, versioned),
                "locations": clean_inline_markdown(location),
                "sourceLinks": source_links(report, location),
                "reportHref": "../" + report_target.relative_to(ROOT).as_posix(),
                "reportPath": report.relative_to(ROOT).as_posix(),
            }
        )
    return candidates


def collect() -> tuple[list[dict[str, object]], list[Path]]:
    candidates: list[dict[str, object]] = []
    reports: list[Path] = []
    packages: list[tuple[str, Path]] = []
    for year in YEARS:
        for package in sorted(path for path in (ROOT / year).iterdir() if path.is_dir()):
            packages.append((year, package))

    if len(packages) != 45:
        raise RuntimeError(f"Expected 45 paper packages, found {len(packages)}")

    for year, package in packages:
        report = select_report(package)
        parsed = parse_report(year, package, report)
        if not parsed:
            raise RuntimeError(f"No formal candidates parsed from {report.relative_to(ROOT)}")
        reports.append(report)
        candidates.extend(parsed)

    keys = [str(item["key"]) for item in candidates]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise RuntimeError(f"Duplicate combined candidate keys: {duplicates}")

    candidates.sort(key=lambda item: (YEARS.index(str(item["year"])), str(item["package"]), int(item["number"])))
    return candidates, reports


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__YEAR__ Human Adjudication — Cxxx Candidate Errors</title>
  <style>
    :root {
      --ink: #17212b; --muted: #617080; --line: #dce3e8; --paper: #ffffff;
      --wash: #f5f7f8; --accent: #176b87; --accent-soft: #e5f3f7;
      --accept: #227a4b; --reject: #a53c32; --minor: #5b56a5; --discuss: #9b650a; --pending: #66717d;
      --shadow: 0 7px 24px rgba(25, 44, 56, .08);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; color: var(--ink); background: var(--wash); font: 15px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    button, input, select, textarea { font: inherit; }
    a { color: var(--accent); }
    .page { width: min(1260px, calc(100% - 32px)); margin: 0 auto; }
    header { color: white; background: linear-gradient(125deg, #103f52, #176b87 58%, #23849b); padding: 34px 0 28px; }
    header h1 { margin: 0 0 8px; font: 700 clamp(24px, 4vw, 39px)/1.12 Georgia, serif; letter-spacing: -.02em; }
    header p { max-width: 850px; margin: 0; color: #e7f4f7; }
    .provenance { margin-top: 13px; font-size: 12px; color: #cce5ec; }
    .toolbar-wrap { position: sticky; top: 0; z-index: 10; padding: 12px 0; background: rgba(245,247,248,.96); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
    .toolbar { display: grid; grid-template-columns: minmax(220px, 1.7fr) minmax(155px, .65fr) auto; gap: 9px; align-items: center; }
    .control, .btn { min-height: 40px; border: 1px solid #bdc9d1; border-radius: 8px; background: white; color: var(--ink); padding: 8px 11px; }
    .control:focus, textarea:focus, select:focus, input:focus { outline: 3px solid rgba(23,107,135,.17); border-color: var(--accent); }
    .btn { cursor: pointer; font-weight: 650; white-space: nowrap; }
    .btn:hover { border-color: var(--accent); color: var(--accent); }
    .btn.primary { color: white; border-color: var(--accent); background: var(--accent); }
    .more-actions { position: relative; }
    .more-actions > summary { list-style: none; }
    .more-actions > summary::-webkit-details-marker { display: none; }
    .menu { position: absolute; right: 0; top: 46px; width: 245px; padding: 8px; border: 1px solid var(--line); border-radius: 10px; background: white; box-shadow: var(--shadow); }
    .menu button, .menu label { display: block; width: 100%; margin: 2px 0; text-align: left; }
    .menu input[type=file] { display: none; }
    .stats { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin: 18px 0; }
    .stat { padding: 13px 15px; border: 1px solid var(--line); border-radius: 10px; background: var(--paper); box-shadow: 0 2px 7px rgba(30,50,60,.03); }
    .stat b { display: block; font-size: 23px; line-height: 1.1; }
    .stat span { color: var(--muted); font-size: 12px; }
    .notice { display: flex; gap: 10px; align-items: flex-start; margin: 0 0 18px; padding: 12px 14px; border-left: 4px solid var(--accent); background: var(--accent-soft); border-radius: 4px 8px 8px 4px; }
    .notice strong { white-space: nowrap; }
    #save-status { margin-left: auto; font-size: 12px; color: var(--muted); white-space: nowrap; }
    details.group { margin: 11px 0; border: 1px solid var(--line); border-radius: 11px; background: var(--paper); box-shadow: 0 3px 12px rgba(30,50,60,.04); overflow: clip; }
    details.group > summary { cursor: pointer; padding: 14px 16px; font-weight: 750; list-style-position: inside; background: #fbfcfc; }
    details.year > summary { font-size: 18px; background: #eef5f7; }
    details.paper { margin: 9px 12px 12px; box-shadow: none; }
    .group-count { color: var(--muted); font-size: 12px; font-weight: 550; margin-left: 8px; }
    .candidate-list { margin: 0; padding: 2px 16px 14px 42px; }
    .candidate-list > li { padding-left: 3px; margin: 7px 0; }
    details.candidate { border: 1px solid var(--line); border-radius: 8px; background: white; overflow: hidden; }
    details.candidate[open] { border-color: #b9ced6; box-shadow: 0 3px 12px rgba(30,50,60,.06); }
    details.candidate > summary { display: flex; align-items: flex-start; gap: 9px; padding: 11px 12px; cursor: pointer; list-style: none; }
    details.candidate > summary::-webkit-details-marker { display: none; }
    details.candidate > summary::before { content: "›"; color: var(--accent); font-size: 22px; line-height: 18px; transition: transform .12s ease; }
    details.candidate[open] > summary::before { transform: rotate(90deg); }
    .candidate-id { flex: 0 0 auto; color: var(--accent); font-weight: 800; }
    .candidate-title { flex: 1 1 auto; font-weight: 650; }
    .badge { flex: 0 0 auto; border-radius: 999px; padding: 2px 8px; color: white; font-size: 11px; font-weight: 750; background: var(--pending); }
    .badge.accept { background: var(--accept); } .badge.reject { background: var(--reject); } .badge.minor { background: var(--minor); } .badge.discuss { background: var(--discuss); }
    .candidate-body { padding: 0 14px 15px 42px; border-top: 1px solid #edf0f2; }
    .metadata { display: flex; flex-wrap: wrap; gap: 7px; padding: 12px 0 4px; }
    .chip { border: 1px solid var(--line); border-radius: 999px; padding: 2px 8px; color: var(--muted); background: #fafbfb; font-size: 11px; }
    .statement { max-width: 1000px; margin: 8px 0; }
    .source-row { display: flex; flex-wrap: wrap; gap: 7px; align-items: center; margin: 8px 0 14px; color: var(--muted); font-size: 12px; }
    .source-link { display: inline-block; border: 1px solid #b9ced6; border-radius: 6px; padding: 3px 7px; text-decoration: none; background: #f6fbfc; }
    .review-grid { display: grid; grid-template-columns: minmax(175px, .65fr) minmax(220px, 1fr) minmax(280px, 1.5fr); gap: 12px; padding: 13px; border-radius: 9px; background: #f6f8f9; }
    .field { display: flex; flex-direction: column; gap: 5px; }
    .field label { color: #3d4c58; font-size: 12px; font-weight: 750; }
    .field textarea, .field input, .field select { width: 100%; border: 1px solid #bbc7cf; border-radius: 7px; background: white; padding: 8px 9px; }
    .field textarea { min-height: 78px; resize: vertical; }
    .field.reason { grid-column: span 2; }
    .field.notes { grid-column: 1 / -1; }
    .field.invalid textarea { border: 2px solid var(--reject); background: #fff8f7; }
    .required-note { display: none; color: var(--reject); font-size: 11px; }
    .field.invalid .required-note { display: block; }
    .empty { padding: 40px 0; text-align: center; color: var(--muted); }
    footer { padding: 28px 0 44px; color: var(--muted); font-size: 12px; }
    @media (max-width: 850px) {
      .toolbar { grid-template-columns: 1fr 1fr; }
      .toolbar input[type=search] { grid-column: 1 / -1; }
      .stats { grid-template-columns: repeat(2, 1fr); }
      .review-grid { grid-template-columns: 1fr; }
      .field.reason, .field.notes { grid-column: auto; }
      .candidate-body { padding-left: 14px; }
    }
    @media print {
      .toolbar-wrap, .notice, .menu, footer { display: none !important; }
      body { background: white; font-size: 10pt; }
      .page { width: 100%; }
      header { color: black; background: white; padding: 0 0 12px; }
      header p, .provenance { color: #333; }
      details { break-inside: avoid; }
      details.group, details.candidate { box-shadow: none; }
    }
  </style>
</head>
<body>
  <header>
    <div class="page">
      <h1>__YEAR__ Human Adjudication</h1>
      <p>Cxxx-style quantitative quality-control candidates from the __YEAR__ paper packages. Open a folded item, decide whether to retain, classify as minor, or reject it, and record a rejection reason.</p>
      <div class="provenance">Generated __GENERATED__ · __PACKAGES__ paper packages · <span id="header-total">__TOTAL__</span> candidates · source digest <code>__DIGEST_SHORT__</code></div>
    </div>
  </header>

  <div class="toolbar-wrap">
    <div class="page toolbar">
      <input id="search" class="control" type="search" placeholder="Search year, package, Cxxx ID, or description…" aria-label="Search candidates">
      <select id="decision-filter" class="control" aria-label="Filter by decision">
        <option value="all">All decisions</option><option value="pending">Pending</option><option value="accept">Retain as error</option><option value="minor">Minor error</option><option value="reject">Reject error</option><option value="discuss">Needs discussion</option><option value="missing-reason">Rejected: reason missing</option>
      </select>
      <details class="more-actions">
        <summary class="btn primary">Review actions ▾</summary>
        <div class="menu">
          <button id="next-pending" class="btn">Next pending item</button>
          <button id="expand-visible" class="btn">Expand visible</button>
          <button id="collapse-all" class="btn">Collapse all</button>
          <button id="download-html" class="btn">Download annotated HTML</button>
          <button id="export-json" class="btn">Export snapshot (JSON)</button>
          <button id="export-csv" class="btn">Export decisions (CSV)</button>
          <label class="btn" for="import-json">Import snapshot (JSON)</label>
          <input id="import-json" type="file" accept="application/json,.json">
          <button id="print" class="btn">Print / Save PDF</button>
        </div>
      </details>
    </div>
  </div>

  <main class="page">
    <section class="stats" aria-label="Adjudication progress">
      <div class="stat"><b id="stat-total">0</b><span>Total candidates</span></div>
      <div class="stat"><b id="stat-pending">0</b><span>Pending</span></div>
      <div class="stat"><b id="stat-accept">0</b><span>Retained as errors</span></div>
      <div class="stat"><b id="stat-minor">0</b><span>Minor errors</span></div>
      <div class="stat"><b id="stat-reject">0</b><span>Rejected</span></div>
      <div class="stat"><b id="stat-missing">0</b><span>Rejections missing reason</span></div>
    </section>

    <div class="notice">
      <strong>Working safely:</strong>
      <span>Edits auto-save in this browser. For handoff to your colleague, use <em>Download annotated HTML</em> (state travels inside the copy) or export/import a JSON snapshot. The original paper reports are never modified.</span>
      <span id="save-status">Loading…</span>
    </div>

    <div id="candidate-groups"></div>
    <div id="empty" class="empty" hidden>No candidates match the current filters.</div>
  </main>

  <footer class="page">Keys use <code>year / package / candidate ID</code>, because candidate numbering restarts in every paper. Source-report dispositions are context only; the joint decision is recorded independently.</footer>

  <div id="embedded-review-state" data-state="" hidden></div>
  <script id="candidate-data" type="application/json">__DATA_JSON__</script>
  <script>
  (() => {
    'use strict';
    const dataset = JSON.parse(document.getElementById('candidate-data').textContent);
    const candidates = dataset.candidates;
    const STORAGE_KEY = '__STORAGE_KEY__';
    const labels = { pending: 'Pending', accept: 'Retain as error', minor: 'Minor error', reject: 'Reject error', discuss: 'Needs discussion' };
    let state = { schemaVersion: 3, sourceDigest: dataset.sourceDigest, decisions: {} };

    const el = id => document.getElementById(id);
    const escapeHtml = value => String(value ?? '').replace(/[&<>"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]));

    function decodeState(encoded) {
      if (!encoded) return null;
      try {
        const binary = atob(encoded); const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
        return JSON.parse(new TextDecoder().decode(bytes));
      } catch (_) { return null; }
    }
    function encodeState(value) {
      const bytes = new TextEncoder().encode(JSON.stringify(value)); let binary = '';
      for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
      return btoa(binary);
    }
    function validRecord(record) {
      return record && ['pending','accept','minor','reject','discuss'].includes(record.decision);
    }
    function mergeStates(base, incoming) {
      if (!incoming || typeof incoming !== 'object' || typeof incoming.decisions !== 'object') return base;
      for (const [key, record] of Object.entries(incoming.decisions)) {
        if (!validRecord(record) || !dataset.keySet.includes(key)) continue;
        const existing = base.decisions[key];
        if (!existing || String(record.updatedAt || '') >= String(existing.updatedAt || '')) base.decisions[key] = record;
      }
      return base;
    }
    function loadState() {
      const embedded = decodeState(el('embedded-review-state').dataset.state);
      state = mergeStates(state, embedded);
      try { state = mergeStates(state, JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null')); }
      catch (_) { el('save-status').textContent = 'Browser storage unavailable'; }
    }
    function recordFor(key) {
      return state.decisions[key] || { decision: 'pending', reason: '', notes: '', reviewers: '', updatedAt: '' };
    }
    let saveTimer;
    function saveState() {
      clearTimeout(saveTimer);
      el('save-status').textContent = 'Saving…';
      saveTimer = setTimeout(() => {
        try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); el('save-status').textContent = 'Saved in browser'; }
        catch (_) { el('save-status').textContent = 'Use Download annotated HTML to save'; }
      }, 180);
    }

    function fieldHtml(candidate) {
      const r = recordFor(candidate.key);
      const statement = candidate.statement && candidate.statement.toLowerCase() !== candidate.title.toLowerCase()
        ? `<p class="statement"><strong>Identification:</strong> ${escapeHtml(candidate.statement)}</p>` : '';
      const sourceLabel = candidate.sourceId !== candidate.id ? `<span class="chip">Source label: ${escapeHtml(candidate.sourceId)}</span>` : '';
      const metadata = sourceLabel + [candidate.category, candidate.sourceStatus].filter(Boolean).map(value => `<span class="chip">${escapeHtml(value)}</span>`).join('');
      const directLinks = candidate.sourceLinks.map(link => `<a class="source-link" href="${escapeHtml(link.href)}" target="_blank">${escapeHtml(link.label)}</a>`).join('');
      const locations = candidate.locations ? `<span>${escapeHtml(candidate.locations)}</span>` : '';
      return `
        <div class="candidate-body">
          <div class="metadata"><span class="chip">${escapeHtml(candidate.year)} / ${escapeHtml(candidate.package)} / ${escapeHtml(candidate.id)}</span>${metadata}</div>
          ${statement}
          <div class="source-row"><a class="source-link" href="${escapeHtml(candidate.reportHref)}" target="_blank">Open full source report</a>${directLinks}${locations && !directLinks ? locations : ''}</div>
          <div class="review-grid">
            <div class="field"><label>Joint decision</label><select data-field="decision" data-key="${escapeHtml(candidate.key)}">
              ${Object.entries(labels).map(([value,label]) => `<option value="${value}" ${r.decision === value ? 'selected' : ''}>${label}</option>`).join('')}
            </select></div>
            <div class="field"><label>Reviewer initials / names</label><input data-field="reviewers" data-key="${escapeHtml(candidate.key)}" value="${escapeHtml(r.reviewers)}" placeholder="e.g., JZ / AB"></div>
            <div class="field reason ${r.decision === 'reject' && !r.reason.trim() ? 'invalid' : ''}"><label>Reason for rejection</label><textarea data-field="reason" data-key="${escapeHtml(candidate.key)}" placeholder="Required when rejecting this candidate">${escapeHtml(r.reason)}</textarea><span class="required-note">Please record why this candidate is rejected.</span></div>
            <div class="field notes"><label>General adjudication notes</label><textarea data-field="notes" data-key="${escapeHtml(candidate.key)}" placeholder="Optional evidence checks, disagreements, or follow-up needed">${escapeHtml(r.notes)}</textarea></div>
          </div>
        </div>`;
    }

    function candidateHtml(candidate) {
      const r = recordFor(candidate.key);
      return `<li data-candidate-key="${escapeHtml(candidate.key)}" data-year="${escapeHtml(candidate.year)}"><details class="candidate" data-search="${escapeHtml([candidate.year,candidate.package,candidate.id,candidate.sourceId,candidate.title,candidate.statement,candidate.category].join(' ').toLowerCase())}">
        <summary><span class="candidate-id">${escapeHtml(candidate.id)}</span><span class="candidate-title">${escapeHtml(candidate.title)}</span><span class="badge ${r.decision}" data-badge>${labels[r.decision]}</span></summary>
        ${fieldHtml(candidate)}
      </details></li>`;
    }

    function renderGroups() {
      const years = [...new Set(candidates.map(c => c.year))];
      el('candidate-groups').innerHTML = years.map((year, yearIndex) => {
        const yearItems = candidates.filter(c => c.year === year);
        const packages = [...new Set(yearItems.map(c => c.package))];
        const papers = packages.map(pkg => {
          const items = yearItems.filter(c => c.package === pkg);
          return `<details class="group paper" data-package="${escapeHtml(pkg)}"><summary>${escapeHtml(pkg)} <span class="group-count">${items.length} candidates</span></summary><ul class="candidate-list">${items.map(candidateHtml).join('')}</ul></details>`;
        }).join('');
        return `<details class="group year" data-year="${year}" ${yearIndex === 0 ? 'open' : ''}><summary>${year} <span class="group-count">${packages.length} papers · ${yearItems.length} candidates</span></summary>${papers}</details>`;
      }).join('');
    }

    function updateRecord(key, field, value) {
      const record = { ...recordFor(key), [field]: value, updatedAt: new Date().toISOString() };
      state.decisions[key] = record;
      const item = document.querySelector(`[data-candidate-key="${CSS.escape(key)}"]`);
      if (item) {
        const badge = item.querySelector('[data-badge]');
        badge.className = `badge ${record.decision}`; badge.textContent = labels[record.decision];
        const reasonField = item.querySelector('.field.reason');
        reasonField.classList.toggle('invalid', record.decision === 'reject' && !record.reason.trim());
      }
      saveState(); updateStats(); applyFilters();
    }

    function updateStats() {
      const counts = { pending: 0, accept: 0, minor: 0, reject: 0, discuss: 0, missing: 0 };
      candidates.forEach(c => { const r = recordFor(c.key); counts[r.decision]++; if (r.decision === 'reject' && !r.reason.trim()) counts.missing++; });
      el('stat-total').textContent = candidates.length; el('stat-pending').textContent = counts.pending;
      el('stat-accept').textContent = counts.accept; el('stat-minor').textContent = counts.minor;
      el('stat-reject').textContent = counts.reject; el('stat-missing').textContent = counts.missing;
    }

    function applyFilters() {
      const query = el('search').value.trim().toLowerCase(); const decision = el('decision-filter').value;
      let visibleTotal = 0;
      document.querySelectorAll('[data-candidate-key]').forEach(item => {
        const details = item.querySelector('details.candidate'); const key = item.dataset.candidateKey; const r = recordFor(key);
        const decisionMatch = decision === 'all' || r.decision === decision || (decision === 'missing-reason' && r.decision === 'reject' && !r.reason.trim());
        const visible = (!query || details.dataset.search.includes(query)) && decisionMatch;
        item.hidden = !visible; if (visible) visibleTotal++;
      });
      document.querySelectorAll('details.paper').forEach(paper => {
        const visible = [...paper.querySelectorAll('[data-candidate-key]')].some(item => !item.hidden); paper.hidden = !visible;
        if (visible && (query || decision !== 'all')) paper.open = true;
      });
      document.querySelectorAll('details.year').forEach(group => {
        const visible = [...group.querySelectorAll('details.paper')].some(paper => !paper.hidden);
        group.hidden = !visible; if (visible && (query || decision !== 'all')) group.open = true;
      });
      el('empty').hidden = visibleTotal !== 0;
    }

    function download(name, content, type) {
      const url = URL.createObjectURL(new Blob([content], {type})); const link = document.createElement('a');
      link.href = url; link.download = name; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    }
    function snapshot() { return { schemaVersion: 3, sourceDigest: dataset.sourceDigest, exportedAt: new Date().toISOString(), decisions: state.decisions }; }
    function csvCell(value) { const text = String(value ?? ''); return /[",\n]/.test(text) ? `"${text.replaceAll('"','""')}"` : text; }

    document.addEventListener('input', event => {
      const target = event.target; if (target.dataset && target.dataset.field) updateRecord(target.dataset.key, target.dataset.field, target.value);
    });
    document.addEventListener('change', event => {
      const target = event.target; if (target.dataset && target.dataset.field) updateRecord(target.dataset.key, target.dataset.field, target.value);
    });
    ['search','decision-filter'].forEach(id => el(id).addEventListener(id === 'search' ? 'input' : 'change', applyFilters));
    el('expand-visible').addEventListener('click', () => document.querySelectorAll('details:not([hidden])').forEach(d => d.open = true));
    el('collapse-all').addEventListener('click', () => document.querySelectorAll('details.group, details.candidate').forEach(d => d.open = false));
    el('next-pending').addEventListener('click', () => {
      const item = [...document.querySelectorAll('[data-candidate-key]')].find(node => !node.hidden && recordFor(node.dataset.candidateKey).decision === 'pending');
      if (!item) return alert('No visible pending candidates.');
      let parent = item.parentElement; while (parent) { if (parent.tagName === 'DETAILS') parent.open = true; parent = parent.parentElement; }
      item.querySelector('details.candidate').open = true; item.scrollIntoView({behavior:'smooth', block:'center'});
    });
    el('export-json').addEventListener('click', () => download(`adjudication-${dataset.years[0]}-snapshot-${new Date().toISOString().slice(0,10)}.json`, JSON.stringify(snapshot(), null, 2), 'application/json'));
    el('export-csv').addEventListener('click', () => {
      const headers = ['year','package','candidate_id','source_id','title','source_report_status','joint_decision','rejection_reason','reviewers','notes','updated_at'];
      const rows = candidates.map(c => { const r = recordFor(c.key); return [c.year,c.package,c.id,c.sourceId,c.title,c.sourceStatus,labels[r.decision],r.reason,r.reviewers,r.notes,r.updatedAt].map(csvCell).join(','); });
      download(`adjudication-${dataset.years[0]}-decisions-${new Date().toISOString().slice(0,10)}.csv`, [headers.join(','),...rows].join('\n'), 'text/csv;charset=utf-8');
    });
    el('download-html').addEventListener('click', () => {
      const clone = document.documentElement.cloneNode(true); const embedded = clone.querySelector('#embedded-review-state');
      embedded.dataset.state = encodeState(snapshot());
      download(`candidate-error-adjudication-${dataset.years[0]}-annotated-${new Date().toISOString().slice(0,10)}.html`, '<!doctype html>\n' + clone.outerHTML, 'text/html;charset=utf-8');
    });
    el('import-json').addEventListener('change', async event => {
      const file = event.target.files[0]; if (!file) return;
      try {
        const imported = JSON.parse(await file.text());
        if (!imported || typeof imported.decisions !== 'object') throw new Error('Snapshot has no decisions object.');
        if (!confirm('Merge this snapshot? Imported records overwrite matching local records when they are newer.')) return;
        state = mergeStates(state, imported); localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        el('candidate-groups').innerHTML = ''; renderGroups(); updateStats(); applyFilters();
      } catch (error) { alert(`Could not import snapshot: ${error.message}`); }
      finally { event.target.value = ''; }
    });
    el('print').addEventListener('click', () => { document.querySelectorAll('details.group, details.candidate').forEach(d => d.open = true); window.print(); });

    loadState(); renderGroups(); updateStats(); applyFilters(); el('save-status').textContent = 'Ready; edits auto-save';
  })();
  </script>
</body>
</html>
'''


def main() -> None:
    candidates, reports = collect()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for year in YEARS:
        year_candidates = [item for item in candidates if item["year"] == year]
        year_reports = [report for report in reports if report.relative_to(ROOT).parts[0] == year]
        digest = hashlib.sha256()
        for report in year_reports:
            digest.update(report.relative_to(ROOT).as_posix().encode("utf-8"))
            digest.update(report.read_bytes())
        source_digest = digest.hexdigest()
        payload = {
            "schemaVersion": 3,
            "sourceDigest": source_digest,
            "years": [year],
            "keySet": [item["key"] for item in year_candidates],
            "candidates": year_candidates,
        }
        data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        package_count = len({str(item["package"]) for item in year_candidates})
        html = (
            HTML_TEMPLATE.replace("__GENERATED__", generated)
            .replace("__TOTAL__", str(len(year_candidates)))
            .replace("__PACKAGES__", str(package_count))
            .replace("__DIGEST_SHORT__", source_digest[:12])
            .replace("__STORAGE_KEY__", f"human-adjudication-{year}-v3")
            .replace("__YEAR__", year)
            .replace("__DATA_JSON__", data_json)
        )
        output = output_for(year)
        output.write_text(html, encoding="utf-8")
        print(
            f"Wrote {output.relative_to(ROOT)}: "
            f"{package_count} reports, {len(year_candidates)} candidates, digest {source_digest[:12]}"
        )


if __name__ == "__main__":
    main()
