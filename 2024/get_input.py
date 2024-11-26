#!/usr/bin/python3
import argparse
import subprocess
import pathlib

input_file = "input.in"


def prepare(day) -> pathlib.Path:
    cwd = pathlib.Path().cwd()
    dir = cwd / f"day{day}"
    _input = dir / input_file
    print(f"Creating dir {dir=}")
    print(f"Creating file {_input=}")
    dir.mkdir()
    _input.write_text("")
    return _input


SESSION = "<FILL ME IN>"

useragent = (
    "https://github.com/oscarm3l1n/advent-of-code/blob/main/2024"
    "/get_input.py by oscarmelin1995@gmail.com"
)
parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("-y", "--year", type=int, default=2024)
parser.add_argument("-d", "--day", type=int, default=1)
args = parser.parse_args()

input_file = prepare(args.day)

cmd = (
    f"curl https://adventofcode.com/{args.year}/day/{args.day}/input"
    f'--cookie "session={SESSION}" -A "{useragent}"'
)
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
input_file.write_text(output)
print(output, end="")
