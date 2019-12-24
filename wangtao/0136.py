#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 18:19


"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    l = [4, 1, 2, 1, 2]
    res = Solution().singleNumber(l)
