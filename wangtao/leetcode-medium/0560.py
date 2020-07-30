#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-28 22:37
from typing import List

"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

前缀和

"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_v, res, count = 0, 0, {}
        count[0] = 1

        for num in nums:
            sum_v += num
            if (sum_v - k) in count:
                res += count[sum_v - k]
            count[sum_v] = count.get(sum_v, 0) + 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
