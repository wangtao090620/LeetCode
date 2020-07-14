#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 00:02
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]
        for i in range(1, len(strs)):
            res = self.find(res, strs[i])
        return res

    def find(self, s1, s2):
        if not s1 or not s2: return ""

        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]: break
            i += 1
        return s1[:i]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
