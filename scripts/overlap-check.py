#!/usr/bin/env python3
"""Flag phrases in this repo that match a reference corpus too closely.

Use it to make sure rewritten content does not reproduce source text. The reference
corpus is never stored in this repository; you pass its path on the command line.

    python3 scripts/overlap-check.py --source /path/to/reference/notes
    python3 scripts/overlap-check.py --source DIR --n 8 --terms "acme,acme.io"

Checks:
  1. Any run of N or more identical words (default 8) shared with the corpus,
     after lowercasing and stripping punctuation and markdown symbols.
  2. Optional forbidden terms (--terms), matched as whole words, case-insensitive.
  3. Multi-word titles (first line of each corpus file, 2-4 words) reused verbatim.

Exit code is 1 when anything is found, 0 otherwise.
"""

import argparse
import re
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".html", ".mdc", ".json"}
SKIP_DIRS = {".git", "node_modules", "references", ".render"}
SKIP_FILES = {"LICENSE", "LICENSE-CONTENT"}
WORD = re.compile(r"[a-z0-9]+(?:['.\-][a-z0-9]+)*")
URL = re.compile(r"https?://\S+")
SVG_LINE = re.compile(r"<(svg|path|symbol|use|circle|rect|line|polyline)\b", re.I)


def words(text):
    """Lowercased word tokens. URLs are dropped: font and CDN links are shared boilerplate, not prose."""
    return WORD.findall(URL.sub(" ", text.lower()))


def iter_files(root, suffixes):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.name in SKIP_FILES:
            continue
        yield path


def build_ngrams(source, n):
    grams = set()
    titles = set()
    for path in iter_files(source, {".md", ".txt", ".ts", ".js"}):
        text = path.read_text(errors="ignore")
        w = words(text)
        grams.update(tuple(w[i:i + n]) for i in range(len(w) - n + 1))
        first = next((ln.strip("# ").strip() for ln in text.splitlines() if ln.strip()), "")
        if 2 <= len(first.split()) <= 4 and len(first) < 40:
            titles.add(first.lower())
    return grams, titles


def scan_file(path, grams, n):
    """Return merged spans (line_no, phrase) of words that sit inside a shared n-gram."""
    lines = path.read_text(errors="ignore").splitlines()
    tokens = []  # (word, line_no)
    for i, line in enumerate(lines, 1):
        if SVG_LINE.search(line):
            continue  # icon path data is code, not prose
        tokens.extend((w, i) for w in words(line))
    hit = [False] * len(tokens)
    seq = [t[0] for t in tokens]
    for i in range(len(seq) - n + 1):
        if tuple(seq[i:i + n]) in grams:
            for j in range(i, i + n):
                hit[j] = True
    spans, start = [], None
    for i, flag in enumerate(hit + [False]):
        if flag and start is None:
            start = i
        elif not flag and start is not None:
            spans.append((tokens[start][1], " ".join(seq[start:i])))
            start = None
    return spans


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path, help="reference corpus directory")
    ap.add_argument("--target", type=Path, default=Path(__file__).resolve().parent.parent,
                    help="directory to scan (default: repo root)")
    ap.add_argument("--n", type=int, default=8, help="minimum shared run length in words (default 8)")
    ap.add_argument("--terms", default="", help="comma-separated forbidden terms")
    args = ap.parse_args()

    if not args.source.is_dir():
        sys.exit(f"source not found: {args.source}")

    grams, titles = build_ngrams(args.source, args.n)
    terms = [t.strip().lower() for t in args.terms.split(",") if t.strip()]
    found = 0

    for path in iter_files(args.target, TEXT_SUFFIXES):
        rel = path.relative_to(args.target)
        text = path.read_text(errors="ignore")
        for line_no, phrase in scan_file(path, grams, args.n):
            found += 1
            print(f"OVERLAP {rel}:{line_no}: {phrase}")
        low = text.lower()
        for i, line in enumerate(low.splitlines(), 1):
            for term in terms:
                if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", line):
                    found += 1
                    print(f"TERM    {rel}:{i}: '{term}'")
            for title in titles:
                if title in line:
                    found += 1
                    print(f"TITLE   {rel}:{i}: '{title}'")

    print(f"\n{found} finding(s). Corpus: {len(grams)} {args.n}-grams, {len(titles)} titles.")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
