#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-15 09:41


"""

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        return self.helper(root,levels,0)
    def helper(self,root,levels,level):
        if not root:
            return
        if len(levels) == level:
            levels.insert(0,[])
        if root.left:
            self.helper(root.left,levels,level + 1)
        if root.right:
            self.helper(root.right,levels,level + 1)
        levels[len(levels) - 1 - level].append(root.val)
        return levels


if __name__ == '__main__':
    pass
