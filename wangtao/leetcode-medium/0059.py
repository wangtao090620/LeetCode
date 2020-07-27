#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-26 11:44
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, top, right, bottom = 0, 0, n - 1, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]

        num, tar = 1, n * n
        while num <= tar:
            # 从左到右
            for i in range(left, right + 1):
                mat[top][i] = num
                num += 1
            top += 1

            # 从上到下
            for i in range(top, bottom + 1):
                mat[i][right] = num
                num += 1
            right -= 1

            # 从右到左
            for i in range(right, left - 1, -1):
                mat[bottom][i] = num
                num += 1
            bottom -= 1

            # 从下到上
            for i in range(bottom, top - 1, -1):
                mat[i][left] = num
                num += 1
            left += 1

        return mat


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
