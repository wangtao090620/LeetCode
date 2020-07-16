#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 10:08

"""
二分法

牛顿法：

cur =(cur + x / cur) // 2

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
