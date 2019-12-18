#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 19:51


"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        res = []

        return self.helper(res, root, 0)

    def helper(self, res, root, level):
        if len(res) == level:
            res.append([])

        res[level].append(root.val)

        if root.left:
            self.helper(res, root.left, level + 1)

        if root.right:
            self.helper(res, root.right, level + 1)

        return res


if __name__ == '__main__':
    pass
