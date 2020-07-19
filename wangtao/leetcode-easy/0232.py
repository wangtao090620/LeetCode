#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 16:05

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_01 = []
        self.stack_02 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_01.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.helper()

        return self.stack_02.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        self.helper()

        return self.stack_02[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_01 and not self.stack_02

    def helper(self):
        if not self.stack_02:
            while self.stack_01:
                self.stack_02.append(self.stack_01.pop())


if __name__ == '__main__':
    pass