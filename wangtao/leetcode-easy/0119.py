#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 23:49
from typing import List


class Solution:
    """
    从倒数第二个元素开始往前更新 它等于原来这个位置的数 + 前一个位置的数
    行[i] = 行[i] + 行[i-1]
    """
    def getRow(self, rowIndex):
        dp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j - 1]
        return dp

    """
    修改上面
    
    """

    def getRow1(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i - j] = dp[i - j - 1] + dp[i - j]
        return dp

    """
    首位插入0   
    """
    def getRow2(self,rowIndex):
        # j行的数据, 应该由j - 1行的数据计算出来.
        # 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
        # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r




if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
