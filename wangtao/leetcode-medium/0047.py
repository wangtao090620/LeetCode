#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 17:14
from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.visited = set()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backTrack(nums, [])
        return self.res

    def backTrack(self, nums, path):
        if len(nums) == len(path):
            self.res.append(path)
            return

        for i in range(len(nums)):
            if i in self.visited or (i > 0 and i - 1 not in self.visited and nums[i] == nums[i - 1]):
                continue
            self.visited.add(i)
            self.backTrack(nums, path + [nums[i]])
            self.visited.remove(i)


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
