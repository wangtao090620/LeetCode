#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-14 19:43

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21


class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)  # 保证和x的符号一致

        r = int(str(x * s)[::-1])  # 正数反转

        return r * s * (r < 2 ** 31)


if __name__ == '__main__':  # True 1，False 0

    clazz = Solution()
    print(clazz.reverse(-210))
