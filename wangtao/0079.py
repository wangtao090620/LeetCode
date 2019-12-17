#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-13 10:42

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""

# 思路：dfs,关键做一个访问过的标记


"""
class Solution:
    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        temp, board[i][j] = board[i][j], "#"

        # 网格上下左右是否满足
        res = self.dfs(board, i + 1, j, word[1:] or self.dfs(board, i - 1, j, word[1:]) \
                       or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:]))

        board[i][j] = temp

        return res
"""

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class Solution:
    def exist(self, board, word):
        if not board:
            return False
        m, n = len(board), len(board[0])
        temp = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j, temp, m, n):
                    return True

        return False

    def dfs(self, board, word, index, i, j, temp, m, n):
        if index == len(word) - 1:
            return board[i][j] == word[index]

        if board[i][j] == word[index]:
            temp[i][j] = True
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and not temp[new_i][new_j] and \
                        self.dfs(board, word, index + 1, new_i, new_j, temp, m, n):
                    return True
            temp[i][j] = False
        return False


if __name__ == '__main__':
    pass
