#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 11:40
from typing import List

"""
1、中间元素和右边界比较，使用右中位数；
2、中间元素和右边界比较，使用左中位数；
3、中间元素和左边界比较，使用右中位数；
4、中间元素和左边界比较，使用左中位数；
5、中间元素和左边界比较，使用左中位数（使用最原始的二分查找法模板）。

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:  # 中间元素不小于左边元素
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:  # 中间元素不小于右边元素
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
