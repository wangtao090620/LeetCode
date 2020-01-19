#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-19 10:36


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.pie = set();self.na = set();self.cols = set();self.result = []
        self.DFS(n,0,[])
        return len(self.result)

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
