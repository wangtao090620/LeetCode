#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 14:50
from typing import List

"""

回溯

"""


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backTrack(candidates, target, 0, [])
        return self.res

    def backTrack(self, nums, target, index, path):
        if target < 0:
            return
        if target == 0:
            self.res.append(path)
            return

        for i in range(index, len(nums)):
            temp = target - nums[i]
            if temp < 0:
                return
            else:
                # 因为可以重复，所以可以从当前层开始
                self.backTrack(nums, target - nums[i], i, path + [nums[i]])


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
