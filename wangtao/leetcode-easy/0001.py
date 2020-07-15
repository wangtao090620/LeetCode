#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-14 22:53


"""

两数之和，考察hash值

hash k：值 value：脚标

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map.get(target - x)]
            hash_map[x] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
