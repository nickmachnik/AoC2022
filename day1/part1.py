#!/usr/bin/env python

import sys
import numpy as np


def main():
    infile = sys.argv[1]
    elf2cal = parse(infile)
    print(
        f"Elf with max cal: Elf #{np.argmax(elf2cal) + 1} with {np.max(elf2cal)} cals")


def parse(file: str):
    elf2cal = [0]
    with open(file, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line == "":
                elf2cal.append(0)
            else:
                elf2cal[-1] += int(line)
    return elf2cal


if __name__ == "__main__":
    main()
