#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 10:09
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.constructPath(root, '')

        return self.res

    def constructPath(self, root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                self.res.append(path)
            else:
                path += '->'
                self.constructPath(root.left, path)
                self.constructPath(root.right, path)


if __name__ == '__main__':
    pass
