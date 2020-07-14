#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-14 23:26


'''
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        n = len(s)

        for i in range(n - 1):
            if mapping[s[i]] < mapping[s[i + 1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]
        print(res)
        return res + mapping[s[-1]]


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
