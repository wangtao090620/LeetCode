#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 23:48


"""
0的来源 2 * 5 所以一对2和5即可产生一个0,所以0的个数即为min(阶乘中5的个数和2的个数)
又因为是2的倍数的数一定比是5的倍数的数多 所以2的个数一定>=5的个数 所以只需要统计 5 的个数了



"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        nums = 0
        while n > 0:
            nums += n // 5
            n = n // 5

        return nums


if __name__ == '__main__':
    s = Solution()


