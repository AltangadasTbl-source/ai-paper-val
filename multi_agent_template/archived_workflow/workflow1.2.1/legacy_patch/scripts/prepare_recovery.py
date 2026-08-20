#!/usr/bin/env python3
"""Inventory immutable workflow-1.0 artifacts and enforce the patch profile."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".csv", ".tsv", ".html"}
SOURCE_SUFFIXES = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv"}
CANDIDATE_HINTS = {
    "candidate",
    "checker",
    "verification",
    "verifier",
    "critic",
    "final_report",
    "agent_response",
    "agent_output",
}
ENDDETAIL_MARKERS = (
    "Audit Method and Revision Status",
    "Candidate Disposition Summary",
    "Verified Scientific Findings",
    "Uncertain Candidates",
    "Rejected and Excluded Interpretations",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify(relative: Path) -> str:
    value = relative.as_posix().casefold()
    if "ocr" in value and relative.suffix.casefold() in {".txt", ".json"}:
        return "ocr_record"
    if any(part in value for part in ("rendered", "page_image")):
        return "rendered_page"
    if "normalized" in value or "extracted_text" in value:
        return "normalized_text"
    if "candidate" in value:
        return "candidate_record"
    if "checker" in value:
        return "checker_output"
    if "verif" in value:
        return "verifier_output"
    if "critic" in value:
        return "critic_output"
    if relative.name.casefold().startswith("final_report"):
        return "final_report"
    if "manifest" in value:
        return "manifest"
    if "document_outputs" in value:
        return "document_record"
    return "other"


def candidate_bearing(relative: Path) -> bool:
    if relative.suffix.casefold() not in TEXT_SUFFIXES:
        return False
    value = relative.as_posix().casefold()
    return any(hint in value for hint in CANDIDATE_HINTS)


def legacy_files(legacy: Path) -> list[Path]:
    files: list[Path] = []
    for path in legacy.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(legacy)
        first = relative.parts[0].casefold()
        if first.startswith("patch_1_"):
            continue
        if re.fullmatch(r"final_report_1_2_[012]\.(?:md|html)", relative.name, re.IGNORECASE):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(legacy).as_posix().casefold())


def detect_endetail(legacy: Path) -> tuple[bool, int, list[str]]:
    report = legacy / "final_report.md"
    if not report.is_file():
        return False, 0, []
    text = report.read_text(encoding="utf-8", errors="replace")
    found = [marker for marker in ENDDETAIL_MARKERS if marker.casefold() in text.casefold()]
    detected = len(found) >= 3 and "Candidate Disposition Summary" in found
    return detected, len(found), found


def direct_sources(package: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in package.iterdir()
            if path.is_file() and path.suffix.casefold() in SOURCE_SUFFIXES
        ),
        key=lambda item: item.name.casefold(),
    )


def reuse_existing_baseline(package: Path, legacy: Path, patch_dir: Path, profile: str) -> bool:
    inventory_path = patch_dir / "legacy_inventory.json"
    if not inventory_path.is_file():
        return False
    try:
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"EXISTING_BASELINE_INVALID: {error}") from error
    if not isinstance(inventory, dict) or inventory.get("profile") != profile:
        raise SystemExit("EXISTING_BASELINE_INVALID: inventory profile mismatch.")

    stored_legacy = inventory.get("legacy_files", [])
    stored_sources = inventory.get("direct_sources", [])
    if not isinstance(stored_legacy, list) or not isinstance(stored_sources, list):
        raise SystemExit("EXISTING_BASELINE_INVALID: inventory arrays are absent.")
    current_legacy = {path.relative_to(legacy).as_posix(): path for path in legacy_files(legacy)}
    expected_legacy = {
        str(entry.get("path", "")): entry for entry in stored_legacy if isinstance(entry, dict)
    }
    current_sources = {path.name: path for path in direct_sources(package)}
    expected_sources = {
        str(entry.get("path", "")): entry for entry in stored_sources if isinstance(entry, dict)
    }
    if set(current_legacy) != set(expected_legacy):
        raise SystemExit("LEGACY_ARTIFACT_SET_CHANGED: legacy files were added or removed after preflight.")
    if set(current_sources) != set(expected_sources):
        raise SystemExit("SOURCE_SET_CHANGED: direct sources were added or removed after preflight.")
    for label, current, expected in (
        ("LEGACY_ARTIFACT_INTEGRITY_FAILURE", current_legacy, expected_legacy),
        ("SOURCE_INTEGRITY_FAILURE", current_sources, expected_sources),
    ):
        for name, path in current.items():
            entry = expected[name]
            if path.stat().st_size != entry.get("bytes") or sha256(path) != entry.get("sha256"):
                raise SystemExit(f"{label}: {name} changed after the recovery baseline.")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=("1.2.1", "1.2.2"))
    parser.add_argument("--package", type=Path, default=Path("."))
    args = parser.parse_args()

    package = args.package.expanduser().resolve()
    legacy = package / ".ai_paper_validation"
    if not legacy.is_dir():
        raise SystemExit(f"Legacy directory is absent: {legacy}")

    detected, marker_score, markers = detect_endetail(legacy)
    expected = args.profile == "1.2.2"
    status = "ENDDETAIL_DETECTED" if detected else "NOT_DETAILED"
    if detected != expected:
        required = "1.2.2" if detected else "1.2.1"
        raise SystemExit(
            f"PROFILE_MISMATCH: detected {status}; apply workflow patch {required}, not {args.profile}."
        )

    patch_name = f"patch_{args.profile.replace('.', '_')}"
    patch_dir = legacy / patch_name
    patch_dir.mkdir(parents=True, exist_ok=True)

    if reuse_existing_baseline(package, legacy, patch_dir, args.profile):
        print(
            json.dumps(
                {
                    "status": "PASS",
                    "profile": args.profile,
                    "endetail_status": status,
                    "baseline": "REUSED_AND_VERIFIED",
                    "patch_dir": str(patch_dir),
                },
                ensure_ascii=False,
            )
        )
        return

    inventory_entries: list[dict[str, object]] = []
    for path in legacy_files(legacy):
        relative = path.relative_to(legacy)
        inventory_entries.append(
            {
                "path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "kind": classify(relative),
                "candidate_bearing": candidate_bearing(relative),
            }
        )

    source_entries = [
        {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
        for path in direct_sources(package)
    ]
    candidate_sources = [
        str(entry["path"]) for entry in inventory_entries if bool(entry["candidate_bearing"])
    ]
    kinds: dict[str, int] = {}
    for entry in inventory_entries:
        kind = str(entry["kind"])
        kinds[kind] = kinds.get(kind, 0) + 1

    created = dt.datetime.now(dt.timezone.utc).isoformat()
    payload = {
        "schema_version": 1,
        "profile": args.profile,
        "package": package.name,
        "created_at_utc": created,
        "legacy_root": ".ai_paper_validation",
        "endetail_detection": {
            "status": status,
            "marker_score": marker_score,
            "markers": markers,
        },
        "legacy_file_count": len(inventory_entries),
        "legacy_kind_counts": kinds,
        "candidate_sources": candidate_sources,
        "legacy_files": inventory_entries,
        "direct_sources": source_entries,
    }
    (patch_dir / "legacy_inventory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (patch_dir / "source_hashes_before.json").write_text(
        json.dumps({"schema_version": 1, "sources": source_entries}, indent=2) + "\n",
        encoding="utf-8",
    )
    (patch_dir / "run_state.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "profile": args.profile,
                "preflight_status": "PASS",
                "endetail_status": status,
                "started_at_utc": created,
                "cpu_only": True,
                "autonomous": True,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    rows = [
        f"# Legacy inventory for patch {args.profile}",
        "",
        f"- Preflight: `PASS`",
        f"- Endetail status: `{status}`",
        f"- Legacy files: {len(inventory_entries)}",
        f"- Candidate-bearing artifacts: {len(candidate_sources)}",
        f"- Direct source files: {len(source_entries)}",
        "- Runtime: Linux CPU-only; legacy OCR first",
        "",
        "## Artifact kind counts",
        "",
        "| Kind | Count |",
        "|---|---:|",
    ]
    rows.extend(f"| {kind} | {count} |" for kind, count in sorted(kinds.items()))
    rows.extend(
        [
            "",
            "## Candidate-bearing legacy artifacts",
            "",
            "Every path below must appear literally in `legacy_source_coverage.md`.",
            "",
        ]
    )
    rows.extend(f"- `{path}`" for path in candidate_sources)
    rows.extend(["", "## Direct sources", ""])
    rows.extend(f"- `{entry['path']}` — SHA-256 `{entry['sha256']}`" for entry in source_entries)
    (patch_dir / "legacy_inventory.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "profile": args.profile,
                "endetail_status": status,
                "legacy_files": len(inventory_entries),
                "candidate_sources": len(candidate_sources),
                "direct_sources": len(source_entries),
                "patch_dir": str(patch_dir),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
