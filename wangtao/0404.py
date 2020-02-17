#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-17 14:24


"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, flag) -> int:
        if not root:
            return 0
        v = 0
        if flag and not root.left and not root.right:
            v = v + root.val
        l = self.sumOfLeftLeaves(root.left, True)
        r = self.sumOfLeftLeaves(root.right, False)

        return l + r + v


if __name__ == '__main__':
    pass
