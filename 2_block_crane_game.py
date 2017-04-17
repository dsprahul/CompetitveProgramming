# coding=utf-8
from __future__ import print_function
import sys


class Crane:
    """ A class based on Crane driver's perspective """
    def __init__(self, W, H, arrangement):
        """ State vals """
        self.floor = arrangement
        self.limit = H
        self.width = W
        self.holding = False
        self.position = 0

    def move_left(self):
        """ Move left if you can """
        if self.position != 0:
            self.position -= 1

    def move_right(self):
        """ Move right if you can """
        if self.position != self.width-1:
            self.position += 1

    def pick(self):
        """ Pick if you can """
        if not self.holding and self.floor[self.position] > 0:
            self.floor[self.position] -= 1
            self.holding = True

    def drop(self):
        """ Drop if you can """
        if self.holding and self.floor[self.position] < self.limit:
            self.floor[self.position] += 1
            self.holding = False


if __name__ == '__main__':
    # Main implementation...
    W, H = map(int, raw_input().split())
    crane = Crane(W=W, H=H, arrangement=map(int, raw_input().split()))
    for command in map(int, raw_input().split()):
        if command == 1:
            crane.move_left()
        elif command == 2:
            crane.move_right()
        elif command == 3:
            crane.pick()
        elif command == 4:
            crane.drop()
        else:
            for item in crane.floor:
                print(item, end=' ')
            sys.exit(0)

