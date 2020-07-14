#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-14 23:07

'''
整数反转


'''


class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)  # 判断x是整数还是负数
        r = int(str(x * s)[::-1])
        return r * s * (r < 2 ** 31)  # 限定范围


if __name__ == '__main__':
    s = Solution()
    s.reverse(23)
