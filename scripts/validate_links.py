#!/usr/bin/env python3
"""Validate repository-local Markdown links and heading fragments.

This script intentionally ignores external URLs and does not fetch the network.
It checks common Markdown link/image syntax and inline HTML href/src attributes.
"""
from pathlib import Path
import re
import sys
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)')
HTML_ATTR_RE = re.compile(r"(?:href|src)\s*=\s*[\"\']([^\"\']+)[\"\']", re.I)
HEADING_RE = re.compile(r'^#{1,6}\s+(.+?)\s*#*\s*$')


def slug(text: str) -> str:
    text = re.sub(r'[`*_~]', '', text)
    text = text.strip().lower()
    text = re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', '-', text)
    return text


def anchors_for(path: Path):
    anchors = set()
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        m = HEADING_RE.match(line)
        if m:
            a = slug(m.group(1))
            if a in anchors:
                suffix = 1
                while f'{a}-{suffix}' in anchors:
                    suffix += 1
                a = f'{a}-{suffix}'
            anchors.add(a)
    return anchors


def parse_target(raw: str):
    raw = raw.strip()
    if raw.startswith('<') and raw.endswith('>'):
        raw = raw[1:-1]
    # Markdown allows optional title after the destination; handle the simple form used here.
    if raw.startswith('"') or raw.startswith("'"):
        return None
    m = re.match(r'^(\S+?)(?:\s+["\'].*["\'])?$', raw)
    return m.group(1) if m else raw.split()[0] if raw.split() else ''

errors = []
checked = 0
for md in MARKDOWN:
    text = md.read_text(encoding='utf-8', errors='replace')
    # Markdown links and images
    candidates = []
    for m in LINK_RE.finditer(text):
        target = m.group(1) or m.group(2)
        target = parse_target(target or '')
        if target:
            candidates.append(target)
    candidates.extend(HTML_ATTR_RE.findall(text))
    for target in candidates:
        target = target.strip()
        if not target or target.startswith('#'):
            if target.startswith('#') and target[1:]:
                anchor = urllib.parse.unquote(target[1:])
                if anchor not in anchors_for(md):
                    errors.append(f'{md.relative_to(ROOT)}: missing local anchor #{anchor}')
            continue
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        if target.startswith('//'):
            continue
        decoded = urllib.parse.unquote(target)
        parsed = urllib.parse.urlsplit(decoded)
        path_part, fragment = parsed.path, parsed.fragment
        dest = (md.parent / path_part).resolve() if path_part else md.resolve()
        try:
            dest.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f'{md.relative_to(ROOT)}: link escapes repository: {target}')
            continue
        checked += 1
        if not dest.exists():
            errors.append(f'{md.relative_to(ROOT)}: missing target: {target}')
            continue
        if fragment and dest.suffix.lower() == '.md':
            anchor = urllib.parse.unquote(fragment)
            if anchor not in anchors_for(dest):
                errors.append(f'{md.relative_to(ROOT)}: missing anchor in {path_part}: #{anchor}')

if errors:
    print(f'FAILED: {len(errors)} issue(s); checked {checked} local path link(s).')
    for e in errors:
        print(' - ' + e)
    sys.exit(1)
print(f'OK: checked {checked} repository-local link(s) across {len(MARKDOWN)} Markdown files.')
