#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-13 09:37

# 最长路径 =

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    maxVal = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maxVal

    def helper(self, root):
        if not root:
            return 0

        leftVal = self.helper(root.left)
        rightVal = self.helper(root.right)

        self.maxVal = max(self.maxVal, leftVal + rightVal)

        return max(leftVal, rightVal) + 1


if __name__ == '__main__':
    pass
