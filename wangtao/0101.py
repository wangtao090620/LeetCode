#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 18:49


"""

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""


# 思路：
# 1、它们的两个根结点具有相同的值。
# 2、每个树的右子树都与另一个树的左子树镜像对称。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归：

class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and \
               self.isMirror(t1.right, t2.left) and \
               self.isMirror(t1.left, t2.right)
"""


# 栈
class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        stack = []

        stack.append((root.left, root.right))

        while stack:
            l, r = stack.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False

            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True


if __name__ == '__main__':
    queue = []

    queue.append((1, 2))
