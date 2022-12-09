#!/usr/bin/env python
from __future__ import annotations
import sys
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Position:
    row: int
    col: int

    def move(self, rel_pos: Position):
        self.row += rel_pos.row
        self.col += rel_pos.col

    def is_touching(self, other: Position):
        return abs(self.row - other.row) <= 1 and abs(self.col - other.col) <= 1

    def __hash__(self):
        return (self.row, self.col).__hash__()


class Rope:
    def __init__(self):
        self.head = Position(0, 0)
        self.tail = Position(0, 0)
        self.tail_positions = set()
        self.tail_positions.add(self.tail)

    def move(self, rel_pos: Position):
        old_head = Position(self.head.row, self.head.col)
        self.head.move(rel_pos)
        if not self.head.is_touching(self.tail):
            self.tail = old_head
            self.tail_positions.add(self.tail)

    def process_move_instr(self, instr: Tuple[str, int]):
        [direction, num_steps] = instr
        for _ in range(num_steps):
            match direction:
                case "R": self.move(Position(0, 1))
                case "L": self.move(Position(0, -1))
                case "U": self.move(Position(-1, 0))
                case "D": self.move(Position(1, 0))


def main():
    instructions = parse(sys.argv[1])
    rope = Rope()
    for instr in instructions:
        rope.process_move_instr(instr)

    print(f"Total tail positions: {len(rope.tail_positions)}")


def parse(file: str) -> List[Tuple[str, int]]:
    res = []
    with open(file, "r") as fin:
        for line in fin:
            line = line.strip()
            [direction, distance] = line.split()
            res.append((direction, int(distance)))

    return res


if __name__ == "__main__":
    main()
