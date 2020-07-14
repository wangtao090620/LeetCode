#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-10 10:20

"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
"""

解题思路：先排序再插入

1.排序规则：按照先H高度降序，K个数升序排序
2.遍历排序后的数组，根据K插入到K的位置上

高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求

"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = {}  # {7: [[7, 0], [7, 1]], 4: [[4, 4]], 5: [[5, 0], [5, 2]], 6: [[6, 1]]}

        for h, k in people:

            if h not in d:
                d[h] = [[h, k]]
            else:
                d[h].append([h, k])
        res = []

        print(d)
        for h in sorted(d.keys(), reverse=True):
            group = sorted(d[h])
            print(res)
            if not res:
                res += group
            else:
                for h, k in group:
                    res.insert(k, [h, k])

        return res


if __name__ == '__main__':
    Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
