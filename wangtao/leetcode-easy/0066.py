#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 00:07
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        while digits and digits[-1] == 9:
            digits.pop()
            res.append(0)
        if not digits:  # 全部是9，例如：99，999
            return [1] + res
        else:
            digits[-1] += 1
            return digits + res


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0, 0, 9]))
