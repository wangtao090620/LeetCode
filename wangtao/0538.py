#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-12 15:10

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 反向的有序遍历 右->根->左
class Solution:
    sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return None
        self.helper(root.right)
        root.val += self.sum
        self.sum = root.val
        self.helper(root.left)



if __name__ == '__main__':
    pass
