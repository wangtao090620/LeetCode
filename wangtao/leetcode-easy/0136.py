#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 23:04
from typing import List


"""

1 ^ 2 ^ 2 = 1

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 3, 2, 3]))
