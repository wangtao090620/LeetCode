#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-26 10:17


"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，

如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""
from typing import List


# dp[n] = MAX( dp[n-1], dp[n-2] + num )

class Solution:
    """
    visited = []

    def rob(self, nums: List[int]) -> int:
        self.visited = [-1 for _ in range(len(nums))]
        return self.helper(nums, len(nums) - 1)

    def helper(self, nums, i):
        if i < 0:
            return 0
        if self.visited[i] >= 0:
            return self.visited[i]

        result = max(self.helper(nums, i - 2) + nums[i], self.helper(nums, i - 1))
        self.visited[i] = result
        return result
    """

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) <= 0:
    #         return 0
    #     dp = [0 for _ in range(len(nums) + 1)]
    #     dp[0], dp[1] = 0, nums[0]
    #     for i in range(2, len(nums) + 1):
    #         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    #     return dp[-1]

    def rob(self, nums: List[int]) -> int:
        a = b = 0

        for i in range(len(nums)):
            if i & 1 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(b + nums[i], a)
        return max(a, b)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))

    print(3 & 1 == 0)
