#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 22:53
from typing import List

"""
二分查找
1、right = len(nums) - 1

2、while left <= right

3、mid = left + (right - left) // 2

4、
if mid > target:
    right = mid - 1
else:
    left = mid + 1
    


"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    pass
