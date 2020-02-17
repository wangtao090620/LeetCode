#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-15 17:50


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: return False
        return self.helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)


if __name__ == '__main__':
    pass
