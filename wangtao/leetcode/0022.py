#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-18 11:31

# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n: int):
        return self.generate("", n, n, [])

    def generate(self, p, left, right, param: list):

        if left:
            self.generate(p + '(', left - 1, right, param)
        if left < right:
            self.generate(p + ')', left, right - 1, param)

        if not right:
            param += p,
        return param


if __name__ == '__main__':
    a = []

    a += ''
    print(a)
