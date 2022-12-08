#!/usr/bin/env python

import sys
import numpy as np

MAX_TREE_HEIGHT = 9


class Patch:
    def __init__(self, patch: np.array):
        self.patch = patch
        self.scenic_scores = np.ones_like(patch)

    def nrows(self) -> int:
        return self.patch.shape[0]

    def ncols(self) -> int:
        return self.patch.shape[1]

    def sc_left(self):
        for rix in range(self.nrows()):
            closest_tree_of_height = {h: None for h in range(MAX_TREE_HEIGHT + 1)}
            for cix in range(self.ncols()):
                trees_visible = cix
                for h in range(self.patch[rix, cix], MAX_TREE_HEIGHT + 1):
                    loc = closest_tree_of_height[h]
                    if loc is not None:
                        trees_visible = min(trees_visible, cix - loc)
                closest_tree_of_height[self.patch[rix, cix]] = cix
                self.scenic_scores[rix, cix] *= trees_visible

    def sc_right(self):
        nc = self.ncols()
        for rix in range(self.nrows()):
            closest_tree_of_height = {h: None for h in range(MAX_TREE_HEIGHT + 1)}
            for cix in reversed(range(nc)):
                trees_visible = nc - cix - 1
                for h in range(self.patch[rix, cix], MAX_TREE_HEIGHT + 1):
                    loc = closest_tree_of_height[h]
                    if loc is not None:
                        trees_visible = min(trees_visible, loc - cix)
                closest_tree_of_height[self.patch[rix, cix]] = cix
                self.scenic_scores[rix, cix] *= trees_visible

    def sc_top(self):
        for cix in range(self.ncols()):
            closest_tree_of_height = {h: None for h in range(MAX_TREE_HEIGHT + 1)}
            for rix in range(self.nrows()):
                trees_visible = rix
                for h in range(self.patch[rix, cix], MAX_TREE_HEIGHT + 1):
                    loc = closest_tree_of_height[h]
                    if loc is not None:
                        trees_visible = min(trees_visible, rix - loc)
                closest_tree_of_height[self.patch[rix, cix]] = rix
                self.scenic_scores[rix, cix] *= trees_visible

    def sc_bottom(self):
        nr = self.nrows()
        for cix in range(self.ncols()):
            closest_tree_of_height = {h: None for h in range(MAX_TREE_HEIGHT + 1)}
            for rix in reversed(range(nr)):
                trees_visible = nr - rix - 1
                for h in range(self.patch[rix, cix], MAX_TREE_HEIGHT + 1):
                    loc = closest_tree_of_height[h]
                    if loc is not None:
                        trees_visible = min(trees_visible, loc - rix)
                closest_tree_of_height[self.patch[rix, cix]] = rix
                self.scenic_scores[rix, cix] *= trees_visible

    def max_scenic_score(self) -> int:
        self.sc_bottom()
        self.sc_top()
        self.sc_left()
        self.sc_right()
        return np.max(self.scenic_scores)


def main():
    patch = parse(sys.argv[1])
    print(f"Max scenic score: {patch.max_scenic_score()}")


def parse(file: str) -> Patch:
    res = []
    with open(file, "r") as fin:
        for line in fin:
            line = line.strip()
            res.append([int(c) for c in line])

    return Patch(np.array(res))


if __name__ == "__main__":
    main()
