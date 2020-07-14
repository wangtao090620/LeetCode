#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-11 10:27


"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            k = abs(nums[i]) - 1
            nums[k] = -abs(nums[k])

        return [i + 1 for i, num in enumerate(nums) if num > 0]
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     map = {}
    #
    #     for num in nums:
    #         map[num] = 1
    #     res = []
    #
    #     for i in range(1, len(nums) + 1):
    #         if i not in map:
    #             res.append(i)
    #     return res


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
