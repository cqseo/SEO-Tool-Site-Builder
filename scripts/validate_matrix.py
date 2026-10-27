#!/usr/bin/env python3
"""Check a proposed SEO page matrix for duplicates and missing independent value."""
import csv
import pathlib
import sys
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print("Usage: python validate_matrix.py path/to/matrix.csv")
    raise SystemExit(2)
path = pathlib.Path(sys.argv[1])
allowed = {"ship", "merge", "experiment", "noindex", "drop"}
required = {"keyword", "intent", "candidate_url", "unique_value", "index_decision", "evidence_source"}
problems = []
try:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        if missing := (required - fields):
            problems.append("Missing columns: " + ", ".join(sorted(missing)))
        rows = list(reader)
except OSError as e:
    print(f"Cannot open matrix: {e}")
    raise SystemExit(2)

seen = {}  # deliberate: multiple keywords can map to one URL if merged
for row_i, row in enumerate(rows, start=2):
    if not required.issubset(fields):
        break
    decision = (row.get("index_decision") or "").strip().lower()
    url = (row.get("candidate_url") or "").strip()
    keyword = (row.get("keyword") or "").strip()
    value = (row.get("unique_value") or "").strip()
    evidence = (row.get("evidence_source") or "").strip()
    if decision not in allowed:
        problems.append(f"Row {row_i}: unknown index_decision {decision!r}")
    if not keyword or not url:
        problems.append(f"Row {row_i}: keyword and candidate_url are required")
    if url and not url.startswith("/") and not urlparse(url).scheme in ("https", "http"):
        problems.append(f"Row {row_i}: URL must be a path or absolute HTTP(S) URL")
    if decision in {"ship", "experiment"} and (len(value) < 12 or not evidence or evidence.lower() in {"none", "unknown", "tbd"}):
        problems.append(f"Row {row_i}: publishing candidate lacks unique_value or evidence_source")
    if decision == "ship" and url in seen:
        problems.append(f"Row {row_i}: duplicate ship URL {url} (row {seen[url]})")
    if decision == "ship":
        seen[url] = row_i
if problems:
    print("FAILED:\n" + "\n".join("- " + p for p in problems))
    raise SystemExit(1)
print(f"PASS: {len(rows)} matrix rows checked; {len(seen)} distinct ship URLs")
