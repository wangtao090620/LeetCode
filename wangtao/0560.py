#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-13 09:45

"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

"""

# sum[i, j] = sum[0, j] - sum[0, i - 1] --> sum[0, i - 1] = sum[0, j] - sum[i, j]
# k           sum         hashmap - key -->  hashmap - key = sum - k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum, res, d = 0, 0, {}

        d[0] = 1
        for num in nums:
            sum += num
            if (sum - k) in d:
                res += d[sum - k]
            d[sum] = d.get(sum, 0) + 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
