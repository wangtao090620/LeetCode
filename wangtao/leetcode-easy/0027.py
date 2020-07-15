#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 20:24

""""

删除数组相同元素

就地删除元素，当和目标元素相等时跳过，不等时，复制元素

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        new_tail = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_tail] = nums[i]
                new_tail += 1
        return new_tail


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
