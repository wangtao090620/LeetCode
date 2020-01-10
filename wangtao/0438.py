#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-10 19:11

"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

"""
from collections import Counter
from typing import List


class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    # res = []
    # pCounter = Counter(p)
    # sCounter = Counter(s[:len(p) - 1])
    # for i in range(len(p) - 1, len(s)):
    #     sCounter[s[i]] += 1
    #
    #     if sCounter == pCounter:
    #         sCounter[s[i - len(p) + 1]] -= 1
    #
    #     if sCounter[s[i - len(p) + 1]] == 0:
    #         del sCounter[s[i - len(p) + 1]]
    # return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}
        needs = {}
        for c in p:
            needs[c] = needs.get(c, 0) + 1

        length, limit = len(p), len(s)
        left = right = 0

        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1
                if right - left + 1 == length:
                    if window == needs: res.append(left)
                    window[s[left]] -= 1
                    left += 1

                right += 1
        return res


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
