#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 22:45

"""
树的left 和 right比较

递归或者栈

"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and \
               self.isMirror(t1.left, t2.right) and \
               self.isMirror(t1.right, t2.left)


if __name__ == '__main__':
    d = deque()
    d.append((1, 2))
    d.append((2, 3))
    d.popleft()
    print(d)

    q = []
    q.append((1, 2))
    q.append((2, 3))

    q.pop(0)
    print(q)
