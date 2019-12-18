#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-18 11:07


"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

"""


# 思路：


class Solution:
    def isInterleave(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)

        if r + c != l:
            return False

        dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]

        for i in range(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])

        return dp[-1][-1]


if __name__ == '__main__':
    pass
