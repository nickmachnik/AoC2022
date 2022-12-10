#!/usr/bin/env python
from __future__ import annotations
import sys
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Instr:
    cmd: str
    args: List[int]

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6

class DeviceScreen:
    def __init__(self):
        self.rix = 0
        self.cix = 0
        self.bitmap = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    def draw(self, sprite_midpoint: int):
        if abs(sprite_midpoint - self.cix) < 2:
            self.bitmap[self.rix][self.cix] = "@"
        else:
            self.bitmap[self.rix][self.cix] = " "
        self.incr_draw_position()

    def incr_draw_position(self):
            self.cix += 1
            if self.cix >= SCREEN_WIDTH:
                self.cix = 0
                self.rix += 1
            if self.rix >= SCREEN_HEIGHT:
                self.rix = 0

    def __repr__(self):
        return "".join(["".join(row) + "\n" for row in self.bitmap])

class Device:
    def __init__(self):
        self.sprite_midpoint = 1
        self.cycle = 0
        self.screen = DeviceScreen()

    def process_instruction(self, instr: Instr):
        match instr.cmd:
            case "noop":
                self.incr_cycle(1)
            case "addx": 
                self.incr_cycle(2)
                self.incr_sprite_midpoint(instr.args[0])

    def incr_sprite_midpoint(self, val: int):
        self.sprite_midpoint += val

    def incr_cycle(self, num: int):
        for _ in range(num):
            self.cycle += 1
            self.screen.draw(self.sprite_midpoint)

    def __repr__(self):
        return f"{self.sprite_midpoint}, {self.cycle}, {self.signal_strengths}"

def main():
    dev = Device()
    for instr in parse(sys.argv[1]):
        dev.process_instruction(instr)
    print(dev.screen)


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
