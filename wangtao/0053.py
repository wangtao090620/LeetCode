#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-06 10:21

"""思路：

动态规划问题

dp[i]:表示以a[i]为结束的子序列的最大和

前面的a[i-1]结束的某个子序列已经取得的最大和，如果为正数，才有继续下去的必要，否咋从下一个元素从新计算

dp[0] = nums[0]
dp[i] = dp[i - 1] + nums[i]

"""


class Solution:

    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += + nums[i - 1]

        return max(nums)

    # def maxSubArray(self, nums):
    #     for i in range(1, len(nums)):
    #         nums[i] = max(nums[i], nums[i - 1] + nums[i])
    #
    #     return max(nums)


if __name__ == '__main__':
    pass
