#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-27 19:51


class Solution:

    def mergeSort(self, array):
        if len(array) < 2:
            return array
        else:
            mid = int(len(array) / 2)
            left = self.mergeSort(array[:mid])
            right = self.mergeSort(array[mid:])
            return self.merge(left, right)

    def merge(self, left, right):  # 并两个已排序好的列表，产生一个新的已排序好的列表
        result = []  # 新的已排序好的列表
        i = 0  # 下标
        j = 0
        # 对两个列表中的元素 两两对比
        # 将最小的元素，放到result中，并对当前列表下标加1
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 此时left或者right其中一个已经添加完毕，剩下的就全部加到result后面即可
        result += left[i:]
        result += right[j:]
        return result


if __name__ == '__main__':
    pass
