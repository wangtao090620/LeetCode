#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-10 12:48

# 思路：动态规划的问题,状态方程：
# dp[i][j]存储的第i行第j列的路径数
# dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]  # m：行，n：列

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    dp = Solution().uniquePaths(3, 3)
    print(dp)
