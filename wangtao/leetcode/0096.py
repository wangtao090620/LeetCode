#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 09:55

"""

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

[1,2,3,4,5,6,7]

i = 3

"""


# 思路：动态规划
# 给定一个有序序列 1 ... n，为了根据序列构建一棵二叉搜索树。
# 我们可以遍历每个数字 i，将该数字作为树根，1 ... (i-1) 序列将成为左子树，(i+1) ... n 序列将成为右子树。于是，我们可以递归地从子序列构建子树。
#
# G(n): 长度为n的序列的不同二叉搜索树个数。
# F(i,n): 以i为根的不同二叉搜索树个数(1<= i <= n)。
# F(i,n)=G(i−1)⋅G(n−i)

# 思路：

# Cn+1 = 2(2n+1)/n+2 * Cn


# class Solution:
#     def numTrees(self, n: int) -> int:
#         res = [0] * (n + 1)
#         res[0], res[1] = 1, 1
#         for i in range(2, n + 1):
#             for j in range(1, i + 1):
#                 res[i] += res[j - 1] * res[i - j]
#         return res[n]

class Solution:
    def numTrees(self, n):
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) // (i + 2)
        return c


if __name__ == '__main__':
    for i in range(2, 5):
        print(i)
