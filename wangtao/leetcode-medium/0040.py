#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 15:22
from typing import List



class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, nums, target, index, path):

        if target == 0:
            self.res.append(path)
            return

        if target < 0:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:  # 去重
                continue
            temp = target - nums[i]

            # 剪枝
            if temp < 0:
                return
            else:
                # 不能重复，下一层开始
                self.dfs(nums, temp, i + 1, path + [nums[i]])


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
