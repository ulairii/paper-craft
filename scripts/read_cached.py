"""Read selected 1-based PDF pages from the scratch text cache."""
import argparse
import re
import subprocess

p = argparse.ArgumentParser()
p.add_argument('paper', choices=[f'P{i:02}' for i in range(1, 11)])
p.add_argument('pages', help='Comma-separated pages or inclusive ranges, e.g. 1-9,14-17')
a = p.parse_args()
raw = subprocess.check_output(['ssh', 'palmetto', f'cat /scratch/runw/paper-craft/cache/papers/{a.paper}.txt']).decode()
pages = raw.split('\f')
for part in a.pages.split(','):
    ends = list(map(int, part.split('-')))
    for number in range(ends[0], ends[-1] + 1):
        print(f'\n{a.paper} PDF PAGE {number}\n')
        print(re.sub(r'[ \t]+', ' ', pages[number - 1]))
