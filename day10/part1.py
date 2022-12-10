#!/usr/bin/env python
from __future__ import annotations
import sys
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Instr:
    cmd: str
    args: List[int]

MAGIC_CYCLE_IXS = [20, 60, 100, 140, 180, 220]

class Device:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal_strengths = []

    def process_instruction(self, instr: Instr):
        match instr.cmd:
            case "noop":
                self.incr_cycle(1)
            case "addx": 
                self.incr_cycle(2)
                self.incr_x(instr.args[0])

    def incr_x(self, val: int):
        self.x += val

    def incr_cycle(self, num: int):
        for _ in range(num):
            self.cycle += 1
            if self.cycle in MAGIC_CYCLE_IXS:
                self.signal_strengths.append(self.cycle * self.x)

    def __repr__(self):
        return f"{self.x}, {self.cycle}, {self.signal_strengths}"

def main():
    dev = Device()
    for instr in parse(sys.argv[1]):
        # print(instr)
        dev.process_instruction(instr)
        # print(dev)

    print(f"Sum of signal strengths: {sum(dev.signal_strengths)}")


def parse(file: str) -> List[Tuple[str, int]]:
    instructions = []
    with open(file, "r") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split()
            instructions.append(Instr(fields[0], [int(e) for e in fields[1:]]))

    return instructions


if __name__ == "__main__":
    main()
