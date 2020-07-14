#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-26 09:33

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List


# 摩尔投票法
# 如何理解摩尔投票法 https://www.zhihu.com/question/49973163/answer/235921864
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = nums[0], 1

        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                num = nums[i]
            elif nums[i] == num:
                count += 1
            else:
                count -= 1
        return num


if __name__ == '__main__':
    pass
