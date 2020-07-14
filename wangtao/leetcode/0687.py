#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-20 15:52

# 最长同值路径

"""
考察递归：

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_len = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.getMaxLen(root, root.val)
        return self.max_len

    def getMaxLen(self, root, val):
        if not root:
            return 0
        left = self.getMaxLen(root.left, root.val)
        right = self.getMaxLen(root.right, root.val)
        self.max_len = max(self.max_len, left + right)

        if val == root.val:
            return max(left, right) + 1
        return 0


if __name__ == '__main__':
    pass
