#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 14:20
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate("", n, n, [])

    def generate(self, p, l, r, param):
        if l:
            self.generate(p + '(', l - 1, r, param)
        if l < r:
            self.generate(p + ')', l, r - 1, param)
        if not r:
            param += p
        return param


if __name__ == '__main__':
    pass
