#!/usr/bin/env python3
"""
Scaffold a draft-me corpus in a folder.

Creates the user-owned folders (format-samples/, voice-samples/, about-me/),
the skill-managed folders (_drafts/, _finals/, _meta/, _meta/sessions/),
and writes .draft-me.json with the corpus config. If the folder is a git
repo, makes an initial commit.

Usage:
    python init.py <path> [--corpus-type "cover letters"]
                          [--format-samples letters]
                          [--voice-samples writings]
                          [--about-me me]
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_FOLDERS = {
    "format_samples": "format-samples",
    "voice_samples": "voice-samples",
    "about_me": "about-me",
    "drafts": "_drafts",
    "finals": "_finals",
    "meta": "_meta",
}


def is_git_repo(path: Path) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=path,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and result.stdout.strip() == "true"


def git_commit(path: Path, message: str, files: list[str]) -> tuple[bool, str]:
    add = subprocess.run(["git", "add", *files], cwd=path, capture_output=True, text=True)
    if add.returncode != 0:
        return False, add.stderr
    commit = subprocess.run(
        ["git", "commit", "-m", message], cwd=path, capture_output=True, text=True
    )
    if commit.returncode != 0:
        return False, commit.stderr
    return True, commit.stdout


def scaffold(
    root: Path,
    corpus_type: str | None,
    folder_overrides: dict[str, str],
) -> dict:
    folders = {**DEFAULT_FOLDERS, **folder_overrides}

    created = []
    for folder_name in folders.values():
        folder = root / folder_name
        folder.mkdir(parents=True, exist_ok=True)
        created.append(folder_name)

    sessions_dir = root / folders["meta"] / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)

    # Placeholder .gitkeep files so empty folders are tracked in git.
    for folder_name in folders.values():
        keep = root / folder_name / ".gitkeep"
        if not any((root / folder_name).iterdir()):
            keep.touch()
    (sessions_dir / ".gitkeep").touch(exist_ok=True)

    config = {
        "version": "1.0",
        "corpus_type": corpus_type or "unspecified",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "folders": folders,
    }

    config_path = root / ".draft-me.json"
    with config_path.open("w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")

    return {
        "created_folders": created,
        "config_path": str(config_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a draft-me corpus")
    parser.add_argument(
        "path", nargs="?", default=".", help="Folder to initialize (default: cwd)"
    )
    parser.add_argument(
        "--corpus-type", default=None, help='E.g., "cover letters", "blog posts"'
    )
    parser.add_argument("--format-samples", default=None, help="Override folder name")
    parser.add_argument("--voice-samples", default=None, help="Override folder name")
    parser.add_argument("--about-me", default=None, help="Override folder name")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists():
        print(f"Error: {root} does not exist", file=sys.stderr)
        return 1
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        return 1

    config_path = root / ".draft-me.json"
    if config_path.exists():
        print(f"Already initialized: {config_path} exists. Nothing to do.")
        return 0

    overrides = {}
    if args.format_samples:
        overrides["format_samples"] = args.format_samples
    if args.voice_samples:
        overrides["voice_samples"] = args.voice_samples
    if args.about_me:
        overrides["about_me"] = args.about_me

    result = scaffold(root, args.corpus_type, overrides)

    print(f"draft-me is set up at: {root}")
    print(f"  Config: {result['config_path']}")
    print(f"  Folders: {', '.join(result['created_folders'])}")

    if is_git_repo(root):
        ok, output = git_commit(
            root,
            "Set up draft-me",
            [".draft-me.json"] + result["created_folders"],
        )
        if ok:
            print("  Git: initial commit created")
        else:
            print(f"  Git: commit failed — {output.strip()}", file=sys.stderr)
    else:
        print("  Git: not a git repo — skipping commit (run `git init` to enable history)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
