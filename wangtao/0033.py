#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-04 17:06


"""

class Solution:
    def search(self, nums, target):

        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid
                else:
                    return mid
            elif target < nums[0]:
                lo = mid + 1  # target在后半段
            else:
                hi = mid
        return -1
"""


class Solution:

    def search(self, nums, target):

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if lo == hi and nums[lo] == target else -1


if __name__ == '__main__':
    x = 2
    print(bin(x))

    print(x & -x)
