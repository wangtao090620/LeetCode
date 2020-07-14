#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-02-11 11:21


"""

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false


"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #
    #     if not p and not q:
    #         return True
    #     if not p or not q:
    #         return False
    #
    #     if p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        d = deque()

        d.append((p, q))

        while d:
            p, q = d.popleft()

            if not self.check(p, q):
                return False
            if p:
                d.append((p.left, q.left))
                d.append((p.right, q.right))

        return True

    def check(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val:
            return True
        return False


if __name__ == '__main__':
    pass
