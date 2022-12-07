#!/usr/bin/env python

import sys


def main():
    backpacks = parse(sys.argv[1])
    score = 0
    for b in backpacks:
        common_item = list(set(b[0]).intersection(set(b[1])))[0]
        score += prio(common_item)
    print(f"Final score: {score}")


def prio(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def parse(file: str):
    with open(file, "r") as fin:
        res = []
        for line in fin:
            line = line.strip()
            items = [e for e in line]
            midpoint = len(items) // 2
            res.append((items[:midpoint], items[midpoint:]))
    return res


if __name__ == "__main__":
    main()
