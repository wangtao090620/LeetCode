#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-29 10:01
from typing import List

"""


"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:  # 第一个位置是障碍物
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:  # 有障碍物
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    a = obstacleGrid[i - 1][j] if i != 0 else 0  # 上面
                    b = obstacleGrid[i][j - 1] if j != 0 else 0  # 左边
                    obstacleGrid[i][j] = a + b

        return obstacleGrid[-1][-1]

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0] == 1:  # 第一个位置是障碍物
    #         return 0
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #
    #     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    #
    #     dp[1][1] = 1  # 当迈出第一步的时候才会有第一种方法
    #
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if i == 1 and j == 1:  # 跳过dp[1][1]
    #                 continue
    #             if obstacleGrid[i - 1][j - 1] == 0:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #             else:
    #                 dp[i][j] = 0
    #     return dp[-1][-1]

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0] == 1:  # 第一个位置是障碍物
    #         return 0
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0 for _ in range(n)] for _ in range(m)]
    #     dp[0][0] = 1
    #     for i in range(1, m):  # 第一行
    #         if dp[i][0] == 0:
    #             dp[i][0] = 1
    #         else:  # 遇到障碍物后面的都是0
    #             break
    #
    #     for j in range(1, n):  # 第一列
    #         if dp[0][j] == 0:
    #             dp[0][j] = 1
    #         else:  # 遇到障碍物后面的都是0
    #             break
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if obstacleGrid[i][j] == 0:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #             else:
    #                 dp[i][j] = 0
    #     return dp[-1][-1]


if __name__ == '__main__':
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print(Solution().uniquePathsWithObstacles(matrix))
