#!/usr/bin/env python

import sys
import numpy as np


class Patch:
    def __init__(self, patch: np.array):
        self.patch = patch
        self.visible = np.zeros_like(patch)

    def nrows(self) -> int:
        return self.patch.shape[0]

    def ncols(self) -> int:
        return self.patch.shape[1]

    def check_visible_left(self):
        for rix in range(self.nrows()):
            row_max = -1
            for cix in range(self.ncols()):
                self.visible[rix, cix] = (
                    self.visible[rix, cix] or self.patch[rix, cix] > row_max
                )
                row_max = max(row_max, self.patch[rix, cix])

    def check_visible_right(self):
        for rix in range(self.nrows()):
            row_max = -1
            for cix in reversed(range(self.ncols())):
                self.visible[rix, cix] = (
                    self.visible[rix, cix] or self.patch[rix, cix] > row_max
                )
                row_max = max(row_max, self.patch[rix, cix])

    def check_visible_bottom(self):
        for cix in range(self.ncols()):
            col_max = -1
            for rix in reversed(range(self.nrows())):
                self.visible[rix, cix] = (
                    self.visible[rix, cix] or self.patch[rix, cix] > col_max
                )
                col_max = max(col_max, self.patch[rix, cix])

    def check_visible_top(self):
        for cix in range(self.ncols()):
            col_max = -1
            for rix in range(self.nrows()):
                self.visible[rix, cix] = (
                    self.visible[rix, cix] or self.patch[rix, cix] > col_max
                )
                col_max = max(col_max, self.patch[rix, cix])

    def num_visibile(self) -> int:
        self.check_visible_bottom()
        self.check_visible_top()
        self.check_visible_left()
        self.check_visible_right()
        return np.sum(self.visible)


def main():
    patch = parse(sys.argv[1])
    print(f"Total visible: {patch.num_visibile()}")


def parse(file: str) -> Patch:
    res = []
    with open(file, "r") as fin:
        for line in fin:
            line = line.strip()
            res.append([int(c) for c in line])

    return Patch(np.array(res))


if __name__ == "__main__":
    main()
