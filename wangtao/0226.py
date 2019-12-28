#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-28 10:01


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


if __name__ == '__main__':
    pass
