#!/usr/bin/env python3
"""Verify a legacy GitHub source content migration via exact Git blob SHA-1.

Run from any directory:
    python tools/verify_legacy_transfer.py
    python tools/verify_legacy_transfer.py --update-manifest

The second form changes the manifest *only when all original files are present
and exact*. It does not delete or download repositories.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PEGA_MANIFEST = ROOT / "legacy" / "pega-legacy-source-map.json"
DYNATRACE_MANIFEST = ROOT / "legacy" / "dynatrace-crc-source-map.json"


def git_sha1(blob: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(blob)).encode("ascii") + b"\0" + blob).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-manifest",
        action="store_true",
        help="When ALL files match, mark every record preserved=true and update status",
    )
    args = parser.parse_args()
    manifests = [x for x in (PEGA_MANIFEST, DYNATRACE_MANIFEST) if x.is_file()]
    if len(manifests) != 1:
        print("ERROR: expected exactly one Pega or Dynatrace manifest", file=sys.stderr)
        return 2
    manifest_path = manifests[0]
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = data.get("sources")
    if not sources:
        sources = [{"repo": data.get("source_repo"), "files": data["files"]}]

    checked = 0
    errors = []
    for source in sources:
        for entry in source["files"]:
            rel = entry["destination"]
            candidate = (ROOT / rel).resolve()
            if not candidate.is_relative_to(ROOT.resolve()):
                errors.append(f"INVALID PATH: {rel}")
                continue
            if not candidate.is_file():
                errors.append(f"MISSING: {rel}")
                continue
            actual = git_sha1(candidate.read_bytes())
            if actual != entry["sha"]:
                errors.append(f"SHA MISMATCH: {rel} expected {entry['sha']}, got {actual}")
            else:
                checked += 1
    total = sum(len(source["files"]) for source in sources)
    for error in errors:
        print(error)
    print(f"SHA_MATCH: {checked}/{total}")
    if errors:
        print("SOURCE_DELETE_BLOCKED: retain original repositories")
        return 1

    if args.update_manifest:
        for source in sources:
            for entry in source["files"]:
                entry["preserved"] = True
        data["decision"] = "SOURCE_CONTENT_COMPLETE_GIT_SHA_VERIFIED"
        manifest_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Manifest updated: {manifest_path.relative_to(ROOT)}")
    print("LEGACY_CONTENT_VERIFIED: all source files present with exact Git blob SHA")
    print("NOTE: Git history, issues and repository settings are not preserved by this check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
