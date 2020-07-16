#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 23:43
from typing import List
"""

dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

当前位置的数  = 上一行的该位置数 + 上一行该位置的前一个数

 
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * n for n in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.generate(4))
