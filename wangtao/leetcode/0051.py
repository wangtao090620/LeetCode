#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-15 09:59

"""
N皇后问题

"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.result = []
        self.cols = set();self.pie = set();self.na = set()
        self.DFS(n, 0, [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in self.result]

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)


if __name__ == '__main__':
    pass
