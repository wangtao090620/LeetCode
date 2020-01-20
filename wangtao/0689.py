#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-20 16:07


"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 
注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

"""

"""
递归 + dfs

target = sum(nums) // k 凑的值


"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums and len(nums) < k:
            return False

        self.avg, self.mod = divmod(sum(nums), k)

        if self.mod:
            return False

        nums.sort(reverse=True)
        if nums[0] > self.avg:
            return False
        self.visited = set()

        return self.dfs(k, nums)

    def dfs(self, k, nums, start=0, tmp=0):
        if tmp == self.avg:
            return self.dfs(k - 1, nums, 0, 0)

        if k == 1:
            return True

        for i in range(start, len(nums)):
            if i not in self.visited and nums[i] + tmp <= self.avg:
                self.visited.add(i)
                if self.dfs(k, nums, i + 1, nums[i] + tmp):
                    return True
                self.visited.remove(i)

        return False



if __name__ == '__main__':
    pass
