#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-11 12:23
"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:

数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。
"""


# 背包问题，dp[i][j]：数组中前i个元素组成和为j
# 状态转移方程 dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
from typing import List

"""
                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
                       
sum(P) = (target + sum(nums)) / 2

"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sumVal = sum(nums) + S

        if sumVal & 1 != 0 or sum(nums) < S:
            return 0

        v = sumVal // 2

        dp = [0] * (v + 1)
        dp[0] = 1

        for num in nums:
            i = v
            while i >= num:
                dp[i] = dp[i] + dp[i - num]
                i -= 1
        return dp[v]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(Solution().findTargetSumWays(nums, S))
