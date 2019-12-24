#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-13 09:41


"""

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""


# 思路：
#
# 方法1：递归：根 -> 左 -> 右 时间复杂度O(n),空间复杂度O(log(n))
# 方法2：


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(res, root)
        return res

    def helper(self, res, root):
        if root:
            if root.left:
                self.helper(res, root.left)
            res.append(root.val)
            if root.right:
                self.helper(res, root.right)
"""


class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not root:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.left


if __name__ == '__main__':
    pass