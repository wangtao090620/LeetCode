#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-29 11:17
from typing import List

"""
     dp[0][j-1] + grid[0][j]
dp = dp[i-1][0] + grid[i][0]
     min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

   
"""


class Solution:

    # 滚动数组
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[0][j] = grid[0][j - 1] + grid[0][j]
                elif j == 0:
                    grid[i][0] = grid[i - 1][0] + grid[i][0]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #
    #     dp = [[0 for _ in range(n)] for _ in range(m)]
    #     dp[0][0] = grid[0][0]
    #     for i in range(1, m):
    #         dp[i][0] = dp[i - 1][0] + grid[i][0]
    #
    #     for j in range(1, n):
    #         dp[0][j] = dp[0][j - 1] + grid[0][j]
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    #
    #     return dp[-1][-1]


if __name__ == '__main__':
    # matrix = [[1, 3, 1],
    #           [1, 5, 1],
    #           [4, 2, 1]]

    matrix = [[1, 2, 5], [3, 2, 1]]
    print(Solution().minPathSum(matrix))
