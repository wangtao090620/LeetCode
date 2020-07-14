#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-09 15:01


# 思路,数组排序，依次判断数组的第一个元素和最大集合的最后一个元素值的大小，例如：[1,3]、[2,6]
# i[0] = 2,out[-1][-1] = 3  ===> 2 < 3 ,out[-1][-1] = max(out[-1][-1],i[-1])


class Solution:
    def merge(self, intervals):
        out = []

        # intervals = sorted(intervals, key=lambda i: i[0])

        for i in sorted(intervals, key=lambda i: i[0]):  # 按照第一个元素排序

            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])  # 更改最后一个元素的值
            else:
                print(out)
                out += i,

        return out


if __name__ == '__main__':
    l1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # l2 = [[4, 5], [1, 4]]

    s = Solution()
    print(s.merge(l1))
