#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 22:37


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        d = deque()

        d.append((p, q))
        while d:
            p, q = d.popleft()

            if not self.check(p, q):
                return False
            if p:
                d.append((p.left, q.left))
                d.append((p.right, q.right))
        return True

    def check(self, p, q):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if p.val == q.val:
            return True

        return False


if __name__ == '__main__':
    a = deque()
    a.append((1, 3))
    # print(a.popleft())

    l, r = a.popleft()
    print(l)
    print(r)
