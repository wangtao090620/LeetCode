#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-27 19:36


class Solution:
    def quickSort(self, nums):
        self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, start, end):
        if end < start:
            return 0
        flag = nums[start]
        left = start
        right = end
        while start < end:
            while nums[end] > flag and end > start:
                end -= 1
            while nums[start] <= flag and end > start:
                start += 1
            nums[end], nums[start] = nums[start], nums[end]
        nums[left], nums[end] = nums[end], nums[left]
        self.helper(nums, left, end - 1)
        self.helper(nums, end + 1, right)


if __name__ == '__main__':
    l = [10, 1, 3, 2, 1, 4, 6, 8, 4, 2]
    Solution().quickSort(l)
    print(l)
