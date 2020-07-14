#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-10 19:00


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.dfs(0, root, sum) +\
               self.pathSum(root.left, sum) +\
               self.pathSum(root.right, sum)

    def dfs(self, cur, root, sum):
        if not root:
            return 0
        cur += root.val
        return (1 if cur == sum else 0) + self.dfs(cur, root.left, sum) + self.dfs(cur, root.right, sum)

    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if self.dfs(i, j, 0, board, word, ):
                    return True
        return False

    def dfs(self, row, col, k, board, word):
        if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != word[k]:
            return False

        if k == len(board) - 1: return True

        temp, board[row][col] = board[row][col], '#'

        res = self.dfs(row + 1, col, k + 1, board, word) or \
              self.dfs(row - 1, col, k + 1, board, word) or \
              self.dfs(row, col + 1, k + 1, board, word) or \
              self.dfs(row, col - 1, k + 1, board, word)

        board[row][col] = temp
        return res


if __name__ == '__main__':
    pass
