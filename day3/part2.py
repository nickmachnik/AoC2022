#!/usr/bin/env python

import sys


def main():
    backpacks = parse(sys.argv[1])
    score = 0
    for gix in range(0, len(backpacks), 3):
        common_item = (backpacks[gix] & backpacks[gix + 1] & backpacks[gix + 2]).pop()
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
            res.append(set(items))
    return res


if __name__ == "__main__":
    main()
