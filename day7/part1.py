#!/usr/bin/env python

import sys
from typing import Tuple, List
from dataclasses import dataclass

TOTAL_DISC_SPACE = 70000000


@dataclass
class File:
    name: str
    size: int


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []
        self.size = None

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir):
        self.dirs.append(dir)

    def list_dir_sizes(self, l: List[int]):
        for dir in self.dirs:
            dir.list_dir_sizes(l)
        l.append(self.get_size())

    def get_size(self):
        if self.size is None:
            self.size = 0
            for file in self.files:
                self.size += file.size
            for dir in self.dirs:
                self.size += dir.get_size()

        return self.size

    def capped_size(self, cap: int) -> int:
        if self.get_size() <= cap:
            return self.get_size()
        return 0

    def sum_of_capped_sizes(self, cap: int) -> int:
        res = self.capped_size(cap)
        for dir in self.dirs:
            res += dir.sum_of_capped_sizes(cap)
        return res

    def __repr__(self):
        return self.name


@dataclass
class FS:
    root: Dir

    def sum_of_capped_sizes(self, cap=100000) -> int:
        return self.root.sum_of_capped_sizes(cap)

    def sizes(self) -> List[int]:
        res = []
        self.root.list_dir_sizes(res)
        return res

    def free_space(self) -> int:
        return TOTAL_DISC_SPACE - self.root.get_size()

    def size_of_smallest_dir_to_delete_to_get_free_space(self, space_needed: int) -> int:
        sizes = self.sizes()
        min_to_free = space_needed - self.free_space()
        sizes.sort()
        for s in sizes:
            if s >= min_to_free:
                return s


def main():
    fs = tree_from_terminal_output(sys.argv[1])

    print(f"Total capped sum: {fs.sum_of_capped_sizes()}")
    # print(
    # f"p2 answer: {fs.size_of_smallest_dir_to_delete_to_get_free_space(30000000)}")


def process_ls(dir: Dir, buffer: List[str]):
    for line in buffer:
        if line.startswith("dir"):
            # I add dirs when cd'ing into them
            continue
        else:
            fields = line.split()
            dir.add_file(File(fields[1], int(fields[0])))
    buffer.clear()


def tree_from_terminal_output(file: str):
    fs = FS(Dir("/", None))

    with open(file, 'r') as fin:
        # first line always goes to root
        next(fin)
        curr_dir = fs.root
        ls_buffer = []
        for line in fin:
            line = line.strip()
            if line.startswith("$"):
                process_ls(curr_dir, ls_buffer)
                if line.startswith("$ cd"):
                    match line.split()[-1]:
                        case "/":
                            curr_dir = fs.root
                        case "..":
                            curr_dir = curr_dir.parent
                        case child:
                            nxt_dir = Dir(child, curr_dir)
                            curr_dir.add_dir(nxt_dir)
                            curr_dir = nxt_dir
                elif line.startswith("$ ls"):
                    continue
            else:
                ls_buffer.append(line)

        process_ls(curr_dir, ls_buffer)

    return fs


if __name__ == "__main__":
    main()
