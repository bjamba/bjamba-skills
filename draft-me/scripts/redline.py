#!/usr/bin/env python3
"""
Produce a markdown redline between two git revisions of a file.

Output uses markdown strikethrough for removed text and bold for added text,
so the user can see the edit inline in the chat without switching to git.

Usage:
    python redline.py <file-path> <old-rev> <new-rev>

Example:
    python redline.py _drafts/zillow.md HEAD~1 HEAD
"""

import argparse
import re
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path


def git_show(repo_root: Path, revision: str, path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git show failed for {revision}:{path}\n{result.stderr.strip()}"
        )
    return result.stdout


def find_repo_root(path: Path) -> Path:
    cwd = path.parent if path.is_file() else path
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Not inside a git repo (checked from {cwd})")
    return Path(result.stdout.strip())


def tokenize(text: str) -> list[str]:
    """Split into words and whitespace runs — both preserved as tokens."""
    return re.findall(r"\S+|\s+", text)


def split_ws(text: str) -> tuple[str, str, str]:
    """Return (leading_ws, core, trailing_ws). If text is all whitespace, core is ''."""
    stripped = text.strip()
    if not stripped:
        return text, "", ""
    start = text.find(stripped)
    end = start + len(stripped)
    return text[:start], text[start:end], text[end:]


def wrap(text: str, marker: str) -> str:
    """Wrap the non-whitespace core of `text` in `marker` (e.g. '**' or '~~')."""
    if not text:
        return ""
    lead, core, trail = split_ws(text)
    if not core:
        # All whitespace — leave alone. Marking whitespace reads as noise.
        return text
    return f"{lead}{marker}{core}{marker}{trail}"


def render_redline(old: str, new: str) -> str:
    old_tokens = tokenize(old)
    new_tokens = tokenize(new)
    matcher = SequenceMatcher(a=old_tokens, b=new_tokens, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            out.append("".join(old_tokens[i1:i2]))
        elif tag == "delete":
            out.append(wrap("".join(old_tokens[i1:i2]), "~~"))
        elif tag == "insert":
            out.append(wrap("".join(new_tokens[j1:j2]), "**"))
        elif tag == "replace":
            out.append(wrap("".join(old_tokens[i1:i2]), "~~"))
            out.append(wrap("".join(new_tokens[j1:j2]), "**"))
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a markdown redline between two git revisions of a file",
    )
    parser.add_argument("file", help="Path to the file (e.g., _drafts/zillow.md)")
    parser.add_argument("old_rev", help="Older revision (e.g., HEAD~1)")
    parser.add_argument("new_rev", help="Newer revision (e.g., HEAD)")
    args = parser.parse_args()

    file_path = Path(args.file).resolve()

    try:
        repo_root = find_repo_root(file_path)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    try:
        rel_path = file_path.relative_to(repo_root)
    except ValueError:
        print(
            f"Error: {file_path} is not inside repo {repo_root}",
            file=sys.stderr,
        )
        return 1

    try:
        old = git_show(repo_root, args.old_rev, str(rel_path))
        new = git_show(repo_root, args.new_rev, str(rel_path))
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(render_redline(old, new))
    return 0


if __name__ == "__main__":
    sys.exit(main())
