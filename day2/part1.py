#!/usr/bin/env python

import sys

DEFEATS = {
    # rock beats scissors
    "A": "Z",
    # paper beats rock
    "B": "X",
    # scissors beat paper
    "C": "Y",
}

EQUALS = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

SYMBOL_SCORES = {"X": 1, "Y": 2, "Z": 3}

SCORE_WIN = 6
SCORE_LOSE = 0
SCORE_DRAW = 3


def main():
    strategy = parse(sys.argv[1])
    score = 0
    for (elf, me) in strategy:
        symscore = SYMBOL_SCORES[me]
        if EQUALS[elf] == me:
            gamescore = SCORE_DRAW
        elif DEFEATS[elf] == me:
            gamescore = SCORE_LOSE
        else:
            gamescore = SCORE_WIN
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
