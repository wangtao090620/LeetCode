#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 15:26

"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from sys import maxsize


class Solution:
    maxSum = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -maxsize

        self.maxPath(root)

        return self.maxSum

    def maxPath(self, root):
        if not root: return 0
        left = max(self.maxPath(root.left), 0)
        right = max(self.maxPath(root.right), 0)

        self.maxSum = max(self.maxSum, left + right + root.val)
        return max(left, right) + root.val


if __name__ == '__main__':
    pass
