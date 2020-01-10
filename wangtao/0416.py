#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-10 11:03


"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumVal = sum(nums)

        if sumVal & 1 == 1:
            return False

        target = sumVal // 2

        # dp = [False for _ in range(target + 1)]
        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:
            for j in range(target, -1, -1):
                if j >= num:
                    dp[j] = dp[j] or dp[j - num]
                else:
                    break
        return dp[target]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
