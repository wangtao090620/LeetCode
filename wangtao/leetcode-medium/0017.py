#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 11:43
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0: return []
        if len(digits) == 1: return list(m[digits])

        pre = self.letterCombinations(digits[:-1])
        final = self.letterCombinations(digits[-1])

        return [s + c for s in pre for c in final]


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
