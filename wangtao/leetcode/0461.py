#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-11 12:12


"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        i = x ^ y
        count = 0
        for _ in range(32):
            count += i & 1
            i = i >> 1
        return count
        # return bin(x ^ y).count('1')


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))
