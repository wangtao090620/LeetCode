#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-20 23:29
"""
Z子变换

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, flag = 0, -1
        res = [""] * numRows

        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag  # 在达到 ZZ 字形转折点时，执行反向
            i += flag
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().convert("LEETCODEISHIRING", 3))
