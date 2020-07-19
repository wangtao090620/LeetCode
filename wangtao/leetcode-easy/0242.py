#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 10:02

"""
统计每个字母出现的次数

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        return d1 == d2


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
