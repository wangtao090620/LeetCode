#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-28 12:25


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row, col = 0, len(matrix[0]) - 1

        while col >= 0 and row <= len(matrix) - 1:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:  # 前一列
                col -= 1
            elif target > matrix[row][col]:  # 下一行
                row += 1
        return False


if __name__ == '__main__':
    pass
