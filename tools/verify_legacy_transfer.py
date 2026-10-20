#!/usr/bin/env python3
"""Contrôle de consolidation legacy : copies exactes + reconstitutions identifiées.

Ne promet jamais que des fichiers recréés sont des copies de leurs originaux.
Commande : python tools/verify_legacy_transfer.py
L'ancienne option --update-manifest reste acceptée sans modifier la provenance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_CANDIDATES = [
    ROOT / "legacy" / "pega-legacy-source-map.json",
    ROOT / "legacy" / "dynatrace-crc-source-map.json",
]


def git_blob_sha(content: bytes) -> str:
    prefix = b"blob " + str(len(content)).encode("ascii") + b"\0"
    return hashlib.sha1(prefix + content).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-manifest", action="store_true",
                        help="Ancienne option : sans effet, la provenance est figée dans le manifeste")
    args = parser.parse_args()

    found = [p for p in MANIFEST_CANDIDATES if p.is_file()]
    if len(found) != 1:
        print("ERROR: exactly one legacy source map expected", file=sys.stderr)
        return 2

    manifest = json.loads(found[0].read_text(encoding="utf-8"))
    groups = manifest.get("sources") or [manifest]
    entries = [entry for group in groups for entry in group["files"]]
    errors = []
    copied = 0
    reconstructed = 0

    for item in entries:
        relative = item["destination"]
        destination = (ROOT / relative).resolve()
        if not destination.is_relative_to(ROOT.resolve()):
            errors.append(f"INVALID_PATH: {relative}")
            continue
        if not destination.is_file():
            errors.append(f"MISSING: {relative}")
            continue

        original = item["sha"]
        replacement = item.get("reconstructed_sha")
        if replacement is not None:
            if item.get("preserved") is not False or not item.get("reconstruction"):
                errors.append(f"INVALID_RECONSTRUCTION_METADATA: {relative}")
                continue
            expected = replacement
            category = "reconstructed"
            if replacement == original:
                errors.append(f"RECONSTRUCTION_UNEXPECTEDLY_IDENTICAL: {relative}")
                continue
        else:
            if item.get("preserved") is not True:
                errors.append(f"UNCOVERED_ORIGINAL: {relative}")
                continue
            expected = original
            category = "copied"

        actual = git_blob_sha(destination.read_bytes())
        if actual != expected:
            errors.append(f"SHA_MISMATCH: {relative}; expected {expected}; actual {actual}")
        elif category == "copied":
            copied += 1
        else:
            reconstructed += 1

    for error in errors:
        print(error)
    print(f"EXACT_SOURCE_BLOBS: {copied}")
    print(f"INDEPENDENT_RECONSTRUCTIONS: {reconstructed}")
    print(f"CONTENT_VERIFIED: {copied + reconstructed}/{len(entries)}")

    if errors:
        print("LEGACY_CONTENT_CHECK_FAILED: keep original repositories")
        return 1

    if args.update_manifest:
        print("INFO: --update-manifest is deprecated; manifest provenance remains unchanged.")

    print("CONTENT_COVERAGE_PASS_WITH_RECONSTRUCTION")
    print("WARNING: reconstructed files differ from original Git blobs.")
    print("WARNING: full original Git histories, settings and issues are not preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
