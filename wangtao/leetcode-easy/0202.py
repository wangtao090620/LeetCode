#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 11:03

"""
思路判断是否有环

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        mapping = set()

        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))

            if n in mapping:
                return False
            else:
                mapping.add(n)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
