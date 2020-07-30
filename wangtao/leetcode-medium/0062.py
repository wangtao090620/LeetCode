#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-29 09:50

"""
每个位置的路径 = 该位置左边的路径 + 该位置上边的路径

"""


class Solution:
    # 滚动数组 自顶向下，从左往右
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for j in range(1, m):
            dp[j] = dp[j] + dp[j - 1]  # 只关系上一层的计算结果，当前位置的值
        return dp[-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[0 for _ in range(n)] for _ in range(m)]
    #
    #     for i in range(m):
    #         dp[i][0] = 1
    #
    #     for j in range(n):
    #         dp[0][j] = 1
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #     return dp[-1][-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[1 for _ in range(n)] for _ in range(m)]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #     return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))
