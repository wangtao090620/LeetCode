#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-15 14:37

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2

        return (self.kth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.kth(nums1, 0, n - 1, nums2, 0, m - 1,
                                                                            right)) / 2

    def kth(self, num1, start1, end1, num2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        if len1 > len2: return self.kth(num2, start2, end2, num1, start1, end1, k)
        if len1 == 0: return num2[start2 + k - 1]


        if k == 1: return min(num1[start1], num2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if num1[i] > num2[j]:  # 删除小的部分
            return self.kth(num1, start1, end1, num2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.kth(num1, i + 1, end1, num2, start2, end2, k - (i - start1 + 1))


if __name__ == '__main__':
    clazz = Solution()
    l1 = [1, 2, 3, 4]

    print(l1[0:])

    print(3 / 2)

    l2 = []

    clazz.findMedianSortedArrays(l1, l2)
