#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 10:20

"""
要检索整数 n 中最右边的位，可以应用模运算（即 n%2）或与运算（即 n & 1）



"""


class Solution:
    def reverseBits(self, n: int) -> int:
        powre = 31
        res = 0
        while n:
            res += (n & 1) << powre
            n = n >> 1
            powre -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(3 & 1)  # 100 001
    print(3 % 2)
    print(3 >> 1)  # 011
