#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-10 11:02


"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n == 0:
            return []
        return self.generateTree(1, n)

    def generateTree(self, start, end):
        if start > end:
            return [None, ]

        res = []

        for index in range(start, end + 1):
            lefts = self.generateTree(start, index - 1)
            rights = self.generateTree(index + 1, end)

            for left in lefts:
                for right in rights:
                    root = TreeNode(index)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res


if __name__ == '__main__':
    pass
