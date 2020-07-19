#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 00:14
from typing import List

"""
三次反转

1、首先把数组分段 k = len(nums) % k
2、[0, n-k-1],[n-k,n-1],[0，n-1]

例如：
[1,2,3,4,5,6,7] k = 3

反转第一段，[4,3,2,1,5,6,7]
反转第二段，[4,3,2,1,7,6,5]
反转整体，[5,6,7,1,2,3,4]

"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.swap(0, n - k - 1, nums)
        self.swap(n - k, n - 1, nums)
        self.swap(0, n - 1, nums)

        print(nums)

    def swap(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
