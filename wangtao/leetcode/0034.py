#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-04 19:15


class Solution:
    def searchRange(self, nums, target):

        lo = self.search(nums, target)

        return [lo, self.search(nums, target + 1) - 1] if target in nums[lo:lo + 1] else [-1, -1]

    def search(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    pass
