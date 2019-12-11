#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-05 10:46

#

class Solution:
    # def rotate(self, matrix):
    #     matrix.revrese()
    #     for i in range(len(matrix)):
    #         for j in range(i):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # def rotate(self, matrix):
    #     matrix[:] = map(list, zip(*matrix[::-1]))

    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = zip(a, b)

    zip(*a[::-1])
    print()
    #
    # print(list(c))
    # print(list(d))
