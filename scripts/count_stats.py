#!/usr/bin/env python3
"""统计仓库的文件数、行数，供 README 引用。

README 里的数字一律由本脚本生成，不要再手工数——手工数过的数据
一次写死后就会和实际脱节（本次即如此：README 写 66,086 行 Markdown，
实际 66,109；写 1,315 行代码，实际 1,258）。

用法：
    python scripts/count_stats.py            # 打印表格
    python scripts/count_stats.py --markdown # 输出可直接贴进 README 的表格

口径：
  - 只统计仓库内文件，跳过 .git / .venv / venv / __pycache__ / node_modules
  - Markdown = *.md
  - 代码 = *.py *.html *.css *.js *.ts *.sql *.sh *.ps1
  - "行" 按换行符计，末尾无换行的最后一行也计入
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SKIP_DIRS = {
    '.git', '.venv', 'venv', 'env', '__pycache__', 'node_modules',
    '.idea', '.vscode', '.mypy_cache', '.pytest_cache', 'dist', 'build',
}

# 测试产物与本地数据库不是仓库内容，计入会让数字随「跑没跑过测试」漂移。
SKIP_FILES = {'db.sqlite3'}
SKIP_SUFFIXES = {'.pyc', '.pyo', '.log', '.sqlite3'}

MD_SUFFIXES = {'.md'}
CODE_SUFFIXES = {'.py', '.html', '.css', '.js', '.ts', '.sql', '.sh', '.ps1'}

REPO_ROOT = Path(__file__).resolve().parent.parent


def count_lines(path: Path) -> int:
    data = path.read_bytes()
    if not data:
        return 0
    return data.count(b'\n') + (0 if data.endswith(b'\n') else 1)


def walk(root: Path):
    for path in sorted(root.rglob('*')):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.name in SKIP_FILES or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        yield path


def collect(root: Path) -> dict:
    stats = {
        'total_files': 0,
        'md_files': 0, 'md_lines': 0,
        'code_files': 0, 'code_lines': 0,
        'other_files': 0, 'other_lines': 0,
        'per_file': [],
    }
    for path in walk(root):
        lines = count_lines(path)
        suffix = path.suffix.lower()
        stats['total_files'] += 1
        if suffix in MD_SUFFIXES:
            stats['md_files'] += 1
            stats['md_lines'] += lines
            kind = 'markdown'
        elif suffix in CODE_SUFFIXES:
            stats['code_files'] += 1
            stats['code_lines'] += lines
            kind = 'code'
        else:
            stats['other_files'] += 1
            stats['other_lines'] += lines
            kind = 'other'
        stats['per_file'].append((path.relative_to(root).as_posix(), kind, lines))
    stats['total_lines'] = stats['md_lines'] + stats['code_lines'] + stats['other_lines']
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description='统计 learning-hub 的文件数与行数')
    parser.add_argument('--markdown', action='store_true', help='输出 README 表格')
    parser.add_argument('--root', default=str(REPO_ROOT), help='仓库根目录')
    parser.add_argument('--verbose', action='store_true', help='逐文件明细')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f'目录不存在: {root}', file=sys.stderr)
        return 1

    stats = collect(root)

    if args.verbose:
        for name, kind, lines in stats['per_file']:
            print(f'{lines:>7}  {kind:<8}  {name}')
        print('-' * 60)

    if args.markdown:
        print('| 指标 | 实测值 |')
        print('|------|--------|')
        print(f'| 文件总数 | {stats["total_files"]} 个（{stats["md_files"]} 个 Markdown + {stats["code_files"]} 个代码文件 + {stats["other_files"]} 个其他） |')
        print(f'| Markdown 行数 | {stats["md_lines"]:,} |')
        print(f'| 代码行数 | {stats["code_lines"]:,} |')
        print(f'| 其他文件行数 | {stats["other_lines"]:,} |')
        print(f'| 总行数 | {stats["total_lines"]:,} |')
    else:
        print(f'root          = {root}')
        print(f'total_files   = {stats["total_files"]}')
        print(f'markdown      = {stats["md_files"]} files / {stats["md_lines"]:,} lines')
        print(f'code          = {stats["code_files"]} files / {stats["code_lines"]:,} lines')
        print(f'other         = {stats["other_files"]} files / {stats["other_lines"]:,} lines')
        print(f'total_lines   = {stats["total_lines"]:,}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
