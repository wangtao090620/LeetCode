#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-20 23:07


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_len = 0
        dct = {}

        for i in range(len(s)):
            if s[i] in dct and start <= dct[s[i]]:
                start = dct[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            dct[s[i]] = i

        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dfgyff"))
