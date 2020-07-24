#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 16:49
from typing import List


class Solution:
    def __init__(self):
        self.res = []


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backTrack(nums, [])
        return self.res

    def backTrack(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            # 类似二叉树，左子树+右子树
            self.backTrack(nums[:i] + nums[i + 1:], path + [nums[i]])


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
