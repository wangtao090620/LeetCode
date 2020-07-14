#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 09:32

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

"""

# 思路：对多进行2次交易
from sys import maxsize
from typing import List


class Solution:
    """
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = float('-inf'), float('-inf')
        release1, release2 = 0, 0

        for price in prices:
            release2 = max(release2, hold2 + price)
            hold2 = max(hold2, release1 - price)

            release1 = max(release1, hold1 + price)
            hold1 = max(hold1, - price)

        return release2
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # 天数，交易次数，当前持仓
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        dp[0][0][0], dp[0][0][1] = 0, -prices[0]
        dp[0][1][0], dp[0][1][1] = -maxsize, -maxsize  # maxsize == float('inf')
        dp[0][2][0], dp[0][2][1] = -maxsize, -maxsize

        print(dp)

        for i in range(1, len(prices)):
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])

            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])

            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])

        end = len(prices) - 1

        return max(dp[end][0][0], dp[end][1][0], dp[end][2][0])


if __name__ == '__main__':
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(4)]

    print(dp)
