#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-05-30 15:58
from typing import List


# 单调栈，栈存储的是脚标，单调递增栈顶的元素是最大的
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]  # 左右加0保证如果只有一个元素的时候栈不为空，如果是最后一个是0，弹出所有栈内元素

        res = 0
        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                print(stack)
                tmp = stack.pop()
                # print(i - stack[-1] - 1)
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


if __name__ == '__main__':
    arr = [2, 1, 5, 6, 2, 3]
    Solution().largestRectangleArea(arr)
