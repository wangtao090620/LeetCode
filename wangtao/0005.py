#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-14 17:04

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。


class Solution:
    def longestPalindrome(self, s: str) -> str:

        size = len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = ""
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and (res == "" or j - i + 1 > len(res)):
                    res = s[i:j + 1]

        return res
#         if s is None:
#             return ""
#
#         res = ""
#         for i in range(len(s)):
#             res = max(self.check(s, i, i), self.check(s, i, i + 1), res, key=len)
#         return res
#
#     def check(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1;r += 1
#         return s[l + 1:r]





if __name__ == '__main__':
    clazz = Solution()

    print(clazz.longestPalindrome("babad"))
