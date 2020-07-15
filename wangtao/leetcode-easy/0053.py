#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 23:31
from typing import List

"""
动态规划

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            print(nums[i - 1] + nums[i])
            print(nums[i])
            print("========")
            nums[i] = max(nums[i - 1] + nums[i], nums[i])

        print(nums)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
