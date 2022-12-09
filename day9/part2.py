#!/usr/bin/env python
from __future__ import annotations
import sys
from dataclasses import dataclass
from typing import List, Tuple
from numpy import sign


@dataclass
class Position:
    row: int
    col: int

    def move(self, dest: Position):
        self.row = dest.row
        self.col = dest.col

    def is_touching(self, other: Position):
        return abs(self.row - other.row) <= 1 and abs(self.col - other.col) <= 1

    def move_towards(self, other: Position):
        self.move(
            Position(self.row + sign(other.row - self.row),
                     self.col + sign(other.col - self.col)))

    def __hash__(self):
        return (self.row, self.col).__hash__()


class Rope:
    def __init__(self):
        self.rope = [Position(0, 0) for _ in range(10)]
        self.tail_positions = set()
        self.tail_positions.add(Position(0, 0))

    def vis(self, min_r, max_r, min_c, max_c):
        for rix in range(min_r, max_r):
            chars = []
            for cix in range(min_c, max_c):
                chars.append('.')
                for kix in reversed(range(10)):
                    knot = self.rope[kix]
                    if (knot.row, knot.col) == (rix, cix):
                        chars[-1] = f"{kix}"
            print(" ".join(chars))
        print()

    def vis_tail_trace(self, min_r, max_r, min_c, max_c):
        for rix in range(min_r, max_r):
            chars = []
            for cix in range(min_c, max_c):
                chars.append(' ')
                if Position(rix, cix) in self.tail_positions:
                    chars[-1] = '#'
            print("".join(chars))
        print()

    def move(self, rel_pos: Position):
        head = self.head()
        head.move(self.new_head_position(rel_pos))
        prev_knot = head

        for knot_ix in range(1, 10):
            knot = self.rope[knot_ix]
            if prev_knot.is_touching(knot):
                break
            else:
                knot.move_towards(prev_knot)
                prev_knot = knot

        # self.vis(-15, 5, -15, 5)
        self.tail_positions.add(Position(self.tail().row, self.tail().col))

    def tail(self) -> Position:
        return self.rope[9]

    def head(self) -> Position:
        return self.rope[0]

    def new_head_position(self, rel_pos: Position) -> Position:
        head = self.head()
        return Position(head.row + rel_pos.row, head.col + rel_pos.col)

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
    rope.vis_tail_trace(-140, 50, -120, 150)

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
