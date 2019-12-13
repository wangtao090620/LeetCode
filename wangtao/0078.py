#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-13 08:58

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        res = [[]]

        for i in nums:
            res = res + [[i] + num for num in res]
        return res


if __name__ == '__main__':
    s = Solution()

    s.subsets([1, 2, 3])

    res = [[]]

    source = [[1], [2], [3]]

    # t = res + [[0] + [4]]

    t = res + [[0] + num for num in source]
    print(t)



    print(t)
