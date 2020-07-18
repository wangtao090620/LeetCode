#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 10:02
from typing import List

"""
买卖股票问题：最多只能完成一笔交易，最大利润，（只能买或者只能卖）



"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        print(dp)
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0  # 没有买入股票、买了一股、买了一股现在把卖了
        profile = 0
        for i in range(2, len(prices)):
            dp[i][0] = dp[i - 1][0]  # 前一天没有买入股票
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]  # 前一天买了一股，然后卖了
            profile = max(profile, dp[i][0], dp[i][1], dp[i][2])
        return profile


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
