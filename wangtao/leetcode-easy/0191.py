#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 10:36

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            if n & 1:
                res += 1
            n = n >> 1

        return res

if __name__ == '__main__':
    s = Solution
