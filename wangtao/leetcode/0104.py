#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 22:31


"""

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
"""
class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            return max(left_h, right_h) + 1       
"""

"""
class Solution:
    def maxDepth(self, root: TreeNode):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
        
"""


class Solution:
    def maxDepth(self, root: TreeNode):
        stack = []
        if root:
            stack.append((1, root))

        depth = 0

        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth


if __name__ == '__main__':
    pass
