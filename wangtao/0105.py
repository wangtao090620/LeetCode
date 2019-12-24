#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 23:01


"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive(递归)

# preorder 中的第一个元素一定是树的根，
#
# 这个根又将 inorder 序列分成了左右两棵子树。现在我们只需要将先序遍历的数组中删除根元素，然后重复上面的过程处理左右两棵子树。

# 中序遍历的特性，根下标mid，mid左边为左子树，mid右边右子树
# 前遍历的特性，第一个是根节点


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))  # 根节点位置
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


if __name__ == '__main__':
    pass
