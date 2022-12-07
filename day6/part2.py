#!/usr/bin/env python

import sys
from dataclasses import dataclass

START_OF_PKT_MARKER_LEN = 4
START_OF_MSG_MARKER_LEN = 14


class Device:
    def __init__(self):
        pass

    def start_of_packet(self, msg: str) -> int:
        for ix in range(START_OF_PKT_MARKER_LEN, len(msg) + 1):
            if len(set(msg[ix - START_OF_PKT_MARKER_LEN: ix])) == START_OF_PKT_MARKER_LEN:
                return ix

    def start_of_message(self, msg: str) -> int:
        for ix in range(START_OF_MSG_MARKER_LEN, len(msg) + 1):
            if len(set(msg[ix - START_OF_MSG_MARKER_LEN: ix])) == START_OF_MSG_MARKER_LEN:
                return ix


def main():
    with open(sys.argv[1], 'r') as fin:
        msg = fin.read()

    print(f"Marker ix: {Device().start_of_message(msg)}")


if __name__ == "__main__":
    main()
