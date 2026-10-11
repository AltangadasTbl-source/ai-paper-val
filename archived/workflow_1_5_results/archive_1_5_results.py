#!/usr/bin/env python3
"""Move workflow 1.5.x (and earlier) results and controls out of the paper packages.

Keeps raw extraction assets (text, OCR, renders, page manifests, document records,
extractor outputs) in place for workflow 1.6 reuse. Archived files keep their
package-relative paths under archived/workflow_1_5_results/<year>/<paper>/.

Usage: python3 archive_1_5_results.py [--execute]   (default: dry run)
"""
import argparse, csv, hashlib, re, shutil, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ARCH = Path(__file__).resolve().parent
YEARS = ("2018", "2019", "2024", "2025")

ROOT_CONTROL_FILES = {"AGENTS.md", "README.md", "START_PROMPT.md", "USAGE.md", "PERFORMANCE_PROFILE.md",
                      "QUALITY_CONTROL_SCOPE.md", "OPENROUTER_SETUP.md"}
ROOT_NON_SOURCE = {"Detailed_Errors_On_C1_C3_C5.docx"}          # earlier error annotation, not a paper source
AIPV_RESULT_DIRS = {"agent_outputs", "checker_outputs", "checks", "coordinator", "critique", "final",
                    "verification", "archive"}
AIPV_RESULT_FILE = re.compile(
    r"^(final_report|human_adjudication|ai_paper_validation_detailed|candidate_|selected_candidates|critic|"
    r"evidence_verifier|figure_flow_checker|statistical_consistency_checker|table_arithmetic_checker|"
    r"report_generator|workflow_(audit|completion|status|trace)|source_integrity)", re.I)
DOCOUT_TOP_RESULT = re.compile(r"^(critic|evidence_verification|table_arithmetic|verified_findings)", re.I)
DOC_RESULT_FILE = re.compile(r"(checker|candidate|critic|verifier|report_generator|agent_response|"
                             r"workflow_agent_responses)", re.I)
DOC_RESULT_DIRS = {"agent_responses", "agent_outputs"}
CURRENT_RUN = re.compile(r"^review_1_5_[0-9]$")
ANY_RUN = re.compile(r"^review_1_5_[0-9]")


def classify(rel: Path) -> str:
    """Return 'archive' or 'keep' for a package-relative file path."""
    parts = rel.parts
    if len(parts) == 1:
        name = parts[0]
        if name in ROOT_CONTROL_FILES or name in ROOT_NON_SOURCE or name.startswith("~$"):
            return "archive"
        return "keep"
    if parts[0].startswith("workflow_1_5_"):
        return "archive"
    if parts[0] == ".codex":
        name = parts[-1]
        if name.startswith("qc15-") or name == "config.toml" or re.match(r"workflow-1-5-\d\.rules$", name):
            return "archive"
        return "keep"
    if parts[0] != ".ai_paper_validation":
        return "keep"
    p = parts[1:]
    if ANY_RUN.match(p[0]):
        return "keep" if CURRENT_RUN.match(p[0]) and len(p) > 2 and p[1] == "preprocessing" else "archive"
    if p[0] in AIPV_RESULT_DIRS:
        return "archive"
    if len(p) == 1:
        return "archive" if AIPV_RESULT_FILE.match(p[0]) else "keep"
    if p[0] == "document_outputs":
        if len(p) == 2:
            return "archive" if DOCOUT_TOP_RESULT.match(p[1]) else "keep"
        if p[1] == "shared_agent_responses":
            return "archive"
        if len(p) >= 4 and p[2] in DOC_RESULT_DIRS:
            return "archive"
        if len(p) == 3 and DOC_RESULT_FILE.search(p[2]):
            return "archive"
    return "keep"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()
    rows, flagged = [], []
    cand_rx = re.compile(r"^#{1,4}\s*C\d{3}\b|Pending Human Adjudication", re.M)
    for year in YEARS:
        for pkg in sorted((REPO / year).glob("jama.*")):
            for f in sorted(x for x in pkg.rglob("*") if x.is_file()):
                rel = f.relative_to(pkg)
                action = classify(rel)
                if action == "keep" and rel.parts[0] == ".ai_paper_validation" and f.suffix in {".md", ".txt", ".json", ".yaml", ".html"}:
                    try:
                        if cand_rx.search(f.read_text(encoding="utf-8", errors="ignore")):
                            flagged.append(f"{year}/{pkg.name}/{rel}")
                    except OSError:
                        pass
                rows.append((year, pkg.name, rel.as_posix(), action, f.stat().st_size))
    arch = [r for r in rows if r[3] == "archive"]
    print(f"files scanned={len(rows)} archive={len(arch)} keep={len(rows)-len(arch)}")
    print(f"kept files that look like candidate/result material: {len(flagged)}")
    for x in flagged[:60]:
        print("  FLAG", x)
    if not args.execute:
        return
    if flagged:
        sys.exit("refusing to execute while kept files are flagged; refine rules first")
    manifest = ARCH / "archive_manifest.csv"
    if manifest.exists():
        sys.exit(f"{manifest} exists; refusing to overwrite an earlier archive run")
    with manifest.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["year", "paper", "package_relative_path", "archive_path", "bytes", "sha256"])
        for year, paper, rel, _, size in arch:
            src = REPO / year / paper / rel
            dst = ARCH / year / paper / rel
            if dst.exists():
                sys.exit(f"archive target exists: {dst}")
            digest = sha(src)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            if sha(dst) != digest:
                sys.exit(f"hash mismatch after move: {dst}")
            w.writerow([year, paper, rel, dst.relative_to(REPO).as_posix(), size, digest])
    # remove directories left empty by the moves (never removes files)
    for year in YEARS:
        for pkg in (REPO / year).glob("jama.*"):
            for d in sorted((x for x in pkg.rglob("*") if x.is_dir()), key=lambda x: len(x.parts), reverse=True):
                if not any(d.iterdir()):
                    d.rmdir()
    print(f"moved {len(arch)} files; manifest at {manifest.relative_to(REPO)}")


if __name__ == "__main__":
    main()
