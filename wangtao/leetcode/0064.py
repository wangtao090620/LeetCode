#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-10 13:17

# 思路：动态规划问题， grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

# grid[i][j]表示到达第i行第j列元素路径最小和，等于上一次的最小与第i-1行和j-1列路径的最小值的和

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]  # 初始化第一列

        print(grid)

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]  # 初始化第1行

        print(grid)

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    aar = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    Solution().minPathSum(aar)
