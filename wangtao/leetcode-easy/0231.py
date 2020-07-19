#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 15:58

"""
n & (n - 1)

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(6))
