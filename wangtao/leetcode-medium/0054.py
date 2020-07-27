# !/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-25 16:18
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        res = []
        while left <= right and top <= bottom:
            # 从左到右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            if top > bottom:
                break

            # 从上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right:
                break

            # 从右到左
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # 从下到上
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res



if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(4, 0, -1):
        print(i)
    print(Solution().spiralOrder(matrix))
