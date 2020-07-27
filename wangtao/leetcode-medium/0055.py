#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-25 17:35
from typing import List

"""
如果能到达某个位置，那么一定能到之前所有位置
如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if i > k: return False  # 当前位置到达不了
            if k >= len(nums) - 1:  # 提前跳出
                return True
            k = max(k, i + nums[i])  # 不断更新最远距离
        return True


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
