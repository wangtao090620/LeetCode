#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-27 19:54

"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""

from typing import List


# 思路：dp[i][j]：正方形的长度
# dp = max()

class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row, col = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        res = 0

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                    res = max(dp[i][j], res)

        return res * res


if __name__ == '__main__':
    print(3 ** 3)
