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


# 背包问题  dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]] dp[i][j]:表示第i个元素的和是j

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumVal = sum(nums)

        if sumVal & 1 == 1:
            return False

        target = sumVal // 2

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[len(nums) - 1][target]

        # 逆序 二维优化成了一维度
        # def canPartition(self, nums: List[int]) -> bool:
        #     sumVal = sum(nums)
        #
        #     if sumVal & 1 == 1:
        #         return False
        #
        #     target = sumVal // 2
        #
        #     dp = [False] * (target + 1)
        #
        #     dp[0] = True
        #
        #     for num in nums:
        #         for j in range(target, -1, -1):
        #             if j >= num:
        #                 dp[j] = dp[j] or dp[j - num]
        #             else:
        #                 break
        #     return dp[target]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 12, 5]))
