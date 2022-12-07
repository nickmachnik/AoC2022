#!/usr/bin/env python

import sys
from dataclasses import dataclass


@dataclass
class Section:
    start: int
    stop: int

    def contains(self, other):
        return self.start <= other.start and self.stop >= other.stop


def main():
    pairs = parse(sys.argv[1])
    score = 0
    for a, b in pairs:
        if a.contains(b) or b.contains(a):
            print(a, b)
            score += 1
    print(f"Final score: {score}")


def parse(file: str):
    with open(file, "r") as fin:
        res = []
        for line in fin:
            line = line.strip()
            sections = []
            for s in line.split(","):
                [start, stop] = s.split("-")
                sections.append(Section(int(start), int(stop)))
            res.append(sections)
    return res


if __name__ == "__main__":
    main()
