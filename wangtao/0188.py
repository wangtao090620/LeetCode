#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 09:33


"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

"""


class Solution:

    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0

        if k >= len(prices) // 2:
            return self.maxBirnaryProfit(prices)

        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices))]  # 天数、交易次数、有无股票
        profit = float("-inf")
        for i in range(k + 1):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            for j in range(k + 1):
                # 当j==0时 dp[i - 1][j][0]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i]) if j != 0 else dp[i - 1][0][0]
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])

        for i in range(k + 1):
            profit = max(profit, dp[len(prices) - 1][i][0])
        return profit

    def maxBirnaryProfit(self, prices):
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        return total


if __name__ == '__main__':
    k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    s = Solution()
    print(s.maxProfit(k, prices))
