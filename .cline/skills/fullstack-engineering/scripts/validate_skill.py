#!/usr/bin/env python3
"""Dependency-free structural validator for this Agent Skill package."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("name", "description")

def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must begin with YAML frontmatter (---).")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("YAML frontmatter closing delimiter not found.")
    raw = text[4:end]
    values = {}
    for line_no, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            raise ValueError(f"Nested YAML is not supported by this lightweight validator (line {line_no}).")
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line {line_no}: expected key: value.")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values, text[end + 4:].lstrip("\n")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail if SKILL.md exceeds 500 lines")
    args = parser.parse_args()
    skill = ROOT / "SKILL.md"
    errors, warnings = [], []
    try:
        metadata, body = parse_frontmatter(skill.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    for key in REQUIRED:
        if not metadata.get(key):
            errors.append(f"Missing required frontmatter field: {key}")
    name = metadata.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("name must use lowercase letters, numbers, and single hyphens.")
    if len(name) > 64:
        errors.append("name exceeds 64 characters.")
    if len(metadata.get("description", "")) > 1024:
        errors.append("description exceeds 1024 characters.")
    if name != ROOT.name:
        errors.append(f"name '{name}' does not match directory '{ROOT.name}'.")
    line_count = len(skill.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        (errors if args.strict else warnings).append(f"SKILL.md has {line_count} lines; recommended maximum is 500.")

    # Validate relative Markdown links and explicit relative file references.
    refs = set(re.findall(r"\]\((\.?/[^)#]+|references/[^)#]+|assets/[^)#]+|scripts/[^)#]+)\)", body))
    refs.update(re.findall(r"`((?:references|assets|scripts)/[^`]+)`", body))
    for ref in sorted(refs):
        candidate = (ROOT / ref).resolve()
        if not candidate.is_relative_to(ROOT.resolve()):
            errors.append(f"Reference escapes skill directory: {ref}")
        elif not candidate.exists():
            errors.append(f"Referenced path does not exist: {ref}")

    for directory in ("references", "scripts", "assets"):
        if not (ROOT / directory).is_dir():
            warnings.append(f"Optional directory missing: {directory}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if errors:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Validation passed: {name} | {line_count} SKILL.md lines | {len(refs)} local references checked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
