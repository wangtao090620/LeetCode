#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-10 19:00


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.dfs(0, root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, cur, root, sum):
        if not root:
            return 0
        cur += root.val
        return (1 if cur == sum else 0) + self.dfs(cur, root.left, sum) + self.dfs(cur, root.right, sum)


if __name__ == '__main__':
    pass
