#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-07 17:41


"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），

可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3

"""
from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:

    # nums.sort()
    #
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i - 1]:
    #         return nums[i]

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p1 = nums[0]
        p2 = slow

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1


if __name__ == '__main__':
    a = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(a))
