#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-28 11:12

# 思路：1、存储所有父节点，2、存储p的父节点，记录visited，3、判断q的父节点是否在visited中


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if root in (None, p, q): return root
    #     left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
    #     return root if left and right else left or right
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        visited = set()

        while p:
            visited.add(p)
            p = parent[p]
        while q not in visited:
            q = parent[q]
        return q


if __name__ == '__main__':
    d = {3: 5}
    print(d.keys())
