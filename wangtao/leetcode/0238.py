#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-07 10:15

"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        k = 1

        for i in range(n):
            res[i] = k
            k = k * nums[i]
        k = 1

        for i in range(n - 1, -1, -1):
            res[i] = res[i] * k
            k = k * nums[i]
        return res


if __name__ == '__main__':
    a1 = [1, 2, 3, 4]
    print(Solution().productExceptSelf(a1))
