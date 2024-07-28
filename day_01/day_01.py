#!/usr/bin/env python
import argparse
import pathlib
import regex as re

import day_01

DEFAULT_DATA = pathlib.Path(day_01.__file__).parent.parent / "data"/ "day1.txt"


def load(filename: str | pathlib.Path) -> list[str]:
    with open(filename) as f:
        return f.readlines()


def solve_q1(data: list[str]) -> int:
    digits: list[int] = []
    digit_re = re.compile(r'\d')

    for text in data:
        first = digit_re.search(text).group()
        last  = digit_re.search(text[::-1]).group()
        digits.append(int(first + last))

    return sum(digits)


def solve_q2(data: list[str]) -> int:
    numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    mapping: dict[str, int] = {}
    for n, name in enumerate(numbers, start=1):
        mapping[name] = n
        mapping[str(n)] = n

    pattern = r'|'.join(numbers)
    digits_re = re.compile(rf'\d|{pattern}')
    digits = []
    for text in data:
        matches = digits_re.findall(text, overlapped=True)
        first = matches[0]
        last = matches[-1]

        digits.append(mapping[first] + mapping[last])

    return sum(digits)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default=DEFAULT_DATA)
    args = parser.parse_args()

    lines = load(args.input)
    print(f"Q1: {solve_q1(lines)}")
    print(f"Q2: {solve_q2(lines)}")


if __name__ == '__main__':
    main()
