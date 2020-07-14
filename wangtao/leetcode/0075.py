#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-11 20:22

# 思路：荷兰三色国旗问题
# 三指针:
# 1、nums[curr]=0,curr和p0交换,p0向右移动
# 2、nums[curr]=2,curr和p2交换，p2向左移动
# 3、nums[curr]=1,curr向右移动


class Solution:
    def sortColors(self, nums):
        p0 = curr = 0

        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1


if __name__ == '__main__':
    pass
