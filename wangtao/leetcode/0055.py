#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-06 16:59

# 思路：贪心算法

# 尽可能达到最远的位置，如果能达到某一个位置那一定能达到前面所有的位置

class Solution:
    def canJump(self, nums):
        m = 0

        for i, n in enumerate(nums):
            if i > m:
                return False

            m = max(m, n + i)
        return True


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]

    b = Solution().canJump(l)

    print(b)
