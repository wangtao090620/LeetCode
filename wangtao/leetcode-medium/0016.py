#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 11:24
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for k in range(len(nums) - 1):
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == target:
                    return target
                if abs(s - target) < abs(res - target):
                    res = s
                if s - target < 0:
                    i += 1
                else:
                    j -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
