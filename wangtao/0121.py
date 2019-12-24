#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 09:30

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""


# 思路：只能买卖一次股票问题，求最大值和最低值


class Solution:
    # def maxProfit(self, prices):
    #     low, profit = float("inf"), 0
    #
    #     for i in prices:
    #         profit = max(profit, i - low)
    #         low = min(low, i)
    #     return profit

    def maxProfit(self, prices):
        if not prices:
            return 0

        profit = 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0  # 没有股票，买入了股票，买入卖出

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
            profit = max(profit, dp[i][0], dp[i][1], dp[i][2])
        return profit


if __name__ == '__main__':
    pass
