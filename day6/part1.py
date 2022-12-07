#!/usr/bin/env python

import sys
from dataclasses import dataclass

START_OF_PKT_MARKER_LEN = 4


class Device:
    def __init__(self):
        pass

    def start_of_packet(self, msg: str) -> int:
        for ix in range(START_OF_PKT_MARKER_LEN, len(msg) + 1):
            if len(set(msg[ix - START_OF_PKT_MARKER_LEN: ix])) == 4:
                return ix


def main():
    with open(sys.argv[1], 'r') as fin:
        msg = fin.read()

    print(f"Marker ix: {Device().start_of_packet(msg)}")


if __name__ == "__main__":
    main()
