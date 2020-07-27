#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-25 15:46
"""

奇数：
多一个 res * x


偶数：
n >> 1 除以2，n // 2


例如：
x^4  = x ^2 * x^2
x^3 = x^2 * res * x (res = 1)

7 = x ^ 2 * x^2 x^2 * x

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    # print(7 & 1)
    print(Solution().myPow(2, 4))
