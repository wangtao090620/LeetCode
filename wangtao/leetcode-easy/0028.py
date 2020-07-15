#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 22:35

"""

子串问题，一般都会用滑动窗口

KMP算法后面了解

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or not haystack: return 0

        L, n = len(needle), len(haystack)

        for i in range(n - L + 1):
            if haystack[i:i + L] == needle:
                return i
        return -1


if __name__ == '__main__':
    pass
