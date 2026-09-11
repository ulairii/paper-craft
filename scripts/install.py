#!/usr/bin/env python3
"""Install the entry point and all specialists together using only the standard library."""
import argparse
from pathlib import Path
import shutil
import sys


def install(source, destination):
    source = source.resolve()
    destination = destination.expanduser().resolve()
    folders = sorted(p for p in source.iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())
    if not folders or not (source / 'paper-craft' / 'SKILL.md').is_file():
        raise ValueError('The source must contain the paper-craft entry point and skill folders.')
    if destination == source or source in destination.parents:
        raise ValueError('Choose a destination outside the source skills directory.')
    conflicts = [destination / p.name for p in folders if (destination / p.name).exists() or (destination / p.name).is_symlink()]
    if conflicts:
        raise FileExistsError('Existing skills would be overwritten. Choose another destination:\n' + '\n'.join(map(str, conflicts)))
    destination.mkdir(parents=True, exist_ok=True)
    copied = []
    try:
        for folder in folders:
            target = destination / folder.name
            # Reserve the directory first; never merge into an existing installation.
            target.mkdir()
            copied.append(target)
            shutil.copytree(folder, target, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    except Exception:
        for target in reversed(copied):
            shutil.rmtree(target)
        raise
    return len(folders), destination / 'paper-craft' / 'SKILL.md'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path('~/.local/share/paper-craft/skills'), help='Destination for all sibling skill folders (default: %(default)s). Existing skills are never overwritten.')
    args = parser.parse_args()
    try:
        count, entry = install(Path(__file__).resolve().parents[1] / 'skills', args.dest)
    except (OSError, ValueError) as error:
        print(f'Installation failed: {error}', file=sys.stderr)
        return 1
    print(f'Installed {count} skill folders. Give your assistant this instruction:\n\nRead {entry}\n\nThen supply your target conference, method, and results.\nFor automatic discovery, use --dest with your assistant’s configured skills directory.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
