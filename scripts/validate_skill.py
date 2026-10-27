#!/usr/bin/env python3
"""Validate Agent Skill package metadata, references, stages and execution safeguards."""
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
MANIFEST = ROOT / "SKILL.md"
errors = []
if not MANIFEST.is_file():
    errors.append("SKILL.md missing")
else:
    text = MANIFEST.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        errors.append("Missing YAML frontmatter")
    else:
        frontmatter = match.group(1)
        name = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.M)
        desc = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
        version = re.search(r'^\s*version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)', frontmatter, re.M)
        if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)) or len(name.group(1)) > 64:
            errors.append("Invalid skill name")
        if not desc or len(desc.group(1).strip()) > 1024:
            errors.append("description is missing or too long")
        if not version:
            errors.append("metadata.version missing")
    for path in sorted(set(re.findall(r"(?:references|templates|scripts|examples)/[a-zA-Z0-9._-]+(?:/[a-zA-Z0-9._-]+)*", text))):
        if not (ROOT / path).is_file():
            errors.append(f"Missing referenced file: {path}")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds the recommended 500-line maximum")
    for pattern in [r"^## G1", r"^## G2", r"^## G3"]:
        if not re.search(pattern, text, re.M):
            errors.append(f"Missing stage heading: {pattern}")
    for label, pattern in {
        "execution/evidence protocol": r"execution-and-evidence\.md",
        "truthfulness boundary": r"构建成功.*部署成功",
        "user deployment preference": r"GitHub Actions",
        "test evidence statuses": r"PASS / FAIL / NOT RUN / BLOCKED",
    }.items():
        if not re.search(pattern, text, re.S):
            errors.append(f"Missing required safeguard: {label}")
    optional_meta = ROOT / "agents/openai.yaml"
    if optional_meta.exists() and "interface:" not in optional_meta.read_text(encoding="utf-8"):
        errors.append("agents/openai.yaml lacks interface")

if errors:
    print("FAILED:\n" + "\n".join("- " + e for e in errors))
    sys.exit(1)
print(f"PASS: {ROOT.name}; metadata, G1/G2/G3, local references and execution safeguards present")
