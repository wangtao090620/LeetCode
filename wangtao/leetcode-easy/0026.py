#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 10:00

"""
给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

解决办法：双指针

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_tail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]
        return new_tail + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0]))
