#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 23:15

from sys import maxsize


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        :type x: int
        :rtype: None
        """

        self.stack.append((x, min(self.getMin(), x)))

    def pop(self) -> None:
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self) -> int:
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        return maxsize


if __name__ == '__main__':
    l = []
    l.append((2, 3))
    print(l[-1][1])
    print(l[-1][0])
