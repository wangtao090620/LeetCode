#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-14 23:14


"""

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):  # 如果是负数或者个位数是0则不满足
            return False
        res = 0

        '''
        思路：将x反转
        '''
        while res < x:
            res = res * 10 + x % 10
            x = x // 10

        return x == res or x == res // 10  # 判断奇数情况：例如121 res = 12


if __name__ == '__main__':
    s = Solution()
    # print(s.isPalindrome(121))
    print(s.isPalindrome(21))
