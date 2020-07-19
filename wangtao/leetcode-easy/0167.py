#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 23:36
from typing import List

"""
双指针 + 二分

脚标不是从0开始，所以每次都要加1

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    pass
