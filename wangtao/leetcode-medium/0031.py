#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 09:47
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:  # 从后往前找第一次前面数不小于后面数
            i -= 1
        if i == 0:  # 数组的倒序的
            nums.reverse()
            return
        print(i)
        k = i - 1
        while nums[j] <= nums[k]:  # 以第一次出现的位置为终点，从后往前找第二次前面数不小于后面的数
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]  # j位置的值肯定比i位置的值要小

        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        print(nums)


if __name__ == '__main__':
    print(Solution().nextPermutation([1, 3, 2]))
