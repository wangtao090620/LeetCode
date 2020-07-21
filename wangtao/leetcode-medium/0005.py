#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-20 23:13

"""
中心扩散法

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        res = ""

        for i in range(len(s)):
            res = max(self.check(s, i, i), self.check(s, i, i + 1), res, key=len)

        return res

    def check(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
