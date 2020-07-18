#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 22:32
from typing import List

"""
dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i]） i-1天没有股票，当天不做操作；i-1天有股票，当天卖掉一股
dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])  i-1天有股票，当天不做操作；i-1天没有股票，当天买了一股
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


if __name__ == '__main__':
    pass
