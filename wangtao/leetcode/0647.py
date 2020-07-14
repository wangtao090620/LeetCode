#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-14 15:30


"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
"""


class Solution:
    count = 0

    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)

        return self.count

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            self.count += 1


if __name__ == '__main__':
    print(Solution().countSubstrings("aaa"))
