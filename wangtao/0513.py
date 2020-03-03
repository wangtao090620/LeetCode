#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-19 23:54


import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = [root]

        while res:
            root = res.pop()

            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)

        return root.val

if __name__ == '__main__':
    pass