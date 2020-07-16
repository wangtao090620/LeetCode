#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-16 13:27
from typing import List

"""
双指针，从后向前遍历，每次和nums1相比较，谁大就移动谁，如果最后nums2中还有元素，将其全部赋值到nums1中

nums1的空间大小大于等于 m + n
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            print(m + n - 1)
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]  # 最后一个元素的脚标 m+n-1
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    print(s.merge([1, 3, 4, 5, 0, 0, 0, 0], 4, [1, 2, 3, 4], 4))
