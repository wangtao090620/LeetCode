#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-19 09:20

"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

"""

思路：

展开其实就是前序遍历，但是用前序遍历 1->2->3 ,每遍历一个节点，就将上一个节点的右指针更新为当前节点

1的右节点5丢失了，所以我们采用逆序

我们依次遍历 6 5 4 3 2 1 , 然后每遍历一个节点就将当前节点的右指针更新为上一个节点,

遍历到 5，把 5 的右指针指向 6。6 <- 5 4 3 2 1。

遍历到 4，把 4 的右指针指向 5。6 <- 5 <- 4 3 2 1。

6<-5<-4<-3<-2<-1  右子树->左子树->根节点，

"""


# Definition for a binary tree node.

# 解法1：


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
class Solution:

    def __init__(self) -> None:
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
       
        # Do not return anything, modify root in-place instead.
        

        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
"""

# 解法2：

"""
思路：

将左子树插入到右子树的地方
将原来的右子树接到左子树的最右边节点
考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 nul
"""


class Solution:

    def flatten(self, root: TreeNode) -> None:
        while root:
            if not root.left:
                root = root.right
            else:
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 原来的右子树接到左子树的右边
                pre.right = root.right
                # 左子树插入到右子树
                root.right = root.left
                root.left = None
                # 下一个节点
                root = root.right


if __name__ == '__main__':
    pass
