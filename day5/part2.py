#!/usr/bin/env python

import sys
from dataclasses import dataclass


@dataclass
class MoveInstruction:
    num: int
    from_ix: int
    to_ix: int


class Stacks:
    def __init__(self):
        self.stacks = []

    def add_crates(self, crates):
        self.adjust_num_stacks(len(crates))
        for stack_ix, crate in enumerate(crates):
            if crate is not None:
                self.add_crate(stack_ix, crate)

    def adjust_num_stacks(self, num_stacks):
        for _ in range(num_stacks - self.num_stacks()):
            self.add_stack()

    def num_stacks(self) -> int:
        return len(self.stacks)

    def add_crate(self, stack_ix, crate):
        self.stacks[stack_ix].append(crate)

    def add_stack(self):
        self.stacks.append([])

    def move(self, n: int, from_ix: int, to_ix: int):
        self.stacks[to_ix].extend(self.stacks[from_ix][-n:])
        for _ in range(n):
            self.stacks[from_ix].pop()

    def tops(self) -> str:
        return "".join([stack[-1] for stack in self.stacks])

    def invert(self):
        for stack in self.stacks:
            stack.reverse()


def main():
    stacks = Stacks()
    with open(sys.argv[1], 'r') as fin:
        line = next(fin)
        while is_stack_line(line):
            stacks.add_crates(parse_stack_line(line))
            line = next(fin)
        stacks.invert()
        # skip next empty line
        next(fin)
        # do all the moving
        for line in fin:
            instr = parse_move_line(line)
            stacks.move(instr.num, instr.from_ix, instr.to_ix)

    print(f"Tops: {stacks.tops()}")


def parse_move_line(line: str):
    line = line.strip()
    fields = line.split()
    return MoveInstruction(int(fields[1]), int(fields[3]) - 1, int(fields[5]) - 1)


def parse_stack_line(line: str):
    crates = []
    num_chars = len(line)
    # the box symbols are at positions 1, 5, 9, 13, 17
    num_stacks_in_line = (num_chars + 1) // 4
    for stack_ix in range(num_stacks_in_line):
        sym = line[stack_ix * 4 + 1]
        if sym == ' ':
            crates.append(None)
        else:
            crates.append(sym)
    return crates


def is_stack_line(line: str):
    for s in line:
        if s == ' ':
            continue
        elif s == '[':
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()
