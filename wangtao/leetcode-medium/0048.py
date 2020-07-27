#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 17:40
from typing import List

"""
上 matrix[pos1][pos1 + add]
右 matrix[pos1 + add][pos2]
下 matrix[pos2][pos2 - add]
左 matrix[pos2 - add][pos1]


左上角：matrix[pos1][pos1] => matrix[pos1][pos1+add]

右上角：matrix[pos1][pos2] => matrix[pos1+add][pos2] 

左下角：matrix[pos2][pos1] => matrix[pos2-add][pos1]

右下角：matrix[pos2][pos2] => matrix[pos2][pos2-add]


"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.


        """
        pos1, pos2 = 0, len(matrix) - 1
        while pos1 < pos2:
            add = 0  # 偏移量
            while add < pos2 - pos1:
                temp = matrix[pos2 - add][pos1]
                matrix[pos2 - add][pos1] = matrix[pos2][pos2 - add]
                matrix[pos2][pos2 - add] = matrix[pos1 + add][pos2]
                matrix[pos1 + add][pos2] = matrix[pos1][pos1 + add]
                matrix[pos1][pos1 + add] = temp

                add += 1
            pos1 += 1
            pos2 -= 1


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print(Solution().rotate(matrix))
    print(matrix)
