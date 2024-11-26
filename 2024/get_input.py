#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

SESSION = '<FILL_ME_IN>'

useragent = 'https://github.com/oscarm3l1n/advent-of-code/blob/master/get_input.py by oscar.a.melin@outlook.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2024)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A \'{useragent}\''
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
