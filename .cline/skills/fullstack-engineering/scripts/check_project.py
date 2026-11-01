#!/usr/bin/env python3
"""Read-only project reconnaissance; reports common manifests and risk markers."""
from __future__ import annotations
import argparse
from pathlib import Path

MANIFESTS = [
    "package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json",
    "pyproject.toml", "requirements.txt", "Cargo.toml", "go.mod",
    "composer.json", "Gemfile", " pom.xml", "build.gradle",
]
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "vendor", ".venv", "__pycache__"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", default=".", help="project directory (default: current directory)")
    args = parser.parse_args()
    root = Path(args.project).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    print(f"Project: {root}")
    print("\nRoot manifests/configuration:")
    found = False
    for name in MANIFESTS:
        path = root / name.strip()
        if path.exists():
            print(f"  - {path.name}")
            found = True
    if not found:
        print("  (none of the common manifests found)")
    print("\nTop-level entries:")
    for item in sorted(root.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
        if item.name not in SKIP_DIRS:
            print(f"  {'[dir] ' if item.is_dir() else '[file]'} {item.name}")
    print("\nPotentially sensitive filenames (names only; file contents are not read):")
    sensitive = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.name.startswith(".env") or path.name in {"id_rsa", "id_ed25519", "credentials.json"}):
            sensitive.append(path.relative_to(root))
    if sensitive:
        for path in sensitive[:50]:
            print(f"  - {path}")
        print("  Review access and ensure secrets are not committed. Values were not inspected.")
    else:
        print("  No common secret filenames found.")
    print("\nRead-only scan complete. This script does not install, modify, or execute project code.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
