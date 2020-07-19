#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 11:01
from typing import List

"""
快慢指针，如果都是非0 index == i，如果是0，index永远存储的是0
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1

        print(nums)


if __name__ == '__main__':
    print(Solution().moveZeroes([5, 1, 2, 0, 4]))
