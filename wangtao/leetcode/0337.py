#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-09 17:34

# 思路

"""
如果我们想从当前的二叉树（植根于root）中抢钱，我们肯定希望对它的左和右子树也能这样做。

因此，沿着这条线，让我们定义一个函数rob(root)，该函数将返回为根于root; 的二叉树可以抢走的最大金额。

现在的关键是，从解决方案解决原来的问题构建它的子问题，即，如何让rob(root)来自rob(root.left), rob(root.right), ...等等。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        visited = {}
        return self.helper(root, visited)

    def helper(self, root, visited):
        if root in visited:
            return visited[root]

        res = 0

        if not root:
            return 0

        if root.left:
            res += self.helper(root.left.left, visited) + self.helper(root.left.right, visited)

        if root.right:
            res += self.helper(root.right.left, visited) + self.helper(root.right.right, visited)

        res = max(res + root.val, self.helper(root.left, visited) + self.helper(root.right, visited))

        visited[root] = res
        return res


if __name__ == '__main__':
    d = {1: "aa"}
    print(1 in d)
