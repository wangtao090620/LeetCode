#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 22:53

"""
二叉树的最小深度


深度是从上到下（水井），高度是从下到上（尺子量身高一般都从脚量到头）

返回Math.min(左子树的深度，右子树的深度)+1，看起来很有道理，但有一个问题，

如果左右子树都不为空或者都为空是没问题的。但如果左右子树一个为空一个不为空，就会有问题了，

因为为空的那个子节点的深度是0，我们不能用它，所以这里要有个判断。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
如果left和right都为0，我们返回1即可，
如果left和right只有一个为0，说明他只有一个子结点，我们只需要返回它另一个子节点的最小深度+1即可。
如果left和right都不为0，说明他有两个子节点，我们只需要返回最小深度的+1即可。
"""



class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0 or r == 0:
            return l + r + 1
        return min(l, r) + 1


if __name__ == '__main__':
    pass
