#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-14 10:44

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 滑动窗口问题


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_char[s[i]] = i
        return max_length


if __name__ == '__main__':
    clazz = Solution()
    size = clazz.lengthOfLongestSubstring("pwwkew")
    print(size)

    # print("pwwkew".__contains__("wke"))
