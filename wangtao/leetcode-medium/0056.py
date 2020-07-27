#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-26 11:24
from typing import List

"""
[1,4] [2,3]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()  # 首位排序，左边界确定了
        res = [intervals[0]]
        for x, y in intervals[1:]:  # 遍历
            if res[-1][1] < x:  # 没有交集直接添加进res
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)  # 有交接，取右边界的最大值 例如：取4
        return res


if __name__ == '__main__':
    a = [[1, 3], [5, 6]]

    print(Solution().merge(a))
