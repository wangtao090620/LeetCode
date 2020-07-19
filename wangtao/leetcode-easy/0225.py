#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 15:48


"""
用队列实现栈对应232用栈实现队列

deque



"""
import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.appendleft(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.d[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.d


if __name__ == '__main__':
    pass
