#!/usr/bin/env python

import sys


LEFT_IX = {"A": 0, "B": 1, "C": 2}
SHIFTS = {"X": -1, "Y": 0, "Z": 1}
SYMBOL_SCORES = [1, 2, 3]
RESULT_SCORES = [0, 3, 6]


def main():
    strategy = parse(sys.argv[1])
    score = 0
    for (elf, me) in strategy:
        symscore = SYMBOL_SCORES[(LEFT_IX[elf] + SHIFTS[me]) % 3]
        gamescore = RESULT_SCORES[SHIFTS[me] + 1]
        # print(elf, me, symscore, "+", gamescore)
        score += symscore + gamescore
    print(f"Final score: {score}")


def parse(file: str):
    with open(file, "r") as fin:
        strategy = []
        for line in fin:
            line = line.strip()
            fields = line.split()
            strategy.append((fields[0], fields[1]))
    return strategy


if __name__ == "__main__":
    main()
