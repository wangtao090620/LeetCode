#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 10:54
from typing import List

"""
奇数和偶数和的最大值
"""


class Solution:

    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for i in range(len(nums)):
            if i & 1:
                a = max(a + nums[i], b)
            else:
                b = max(b + nums[i], a)
        return max(a, b)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
