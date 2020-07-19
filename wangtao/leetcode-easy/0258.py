#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 10:18

"""
数学归纳法：
k=x
k+1=x+1 当x=9时：k+1=1
k+2=x+2 或 2

显然 k%9可以推测，根据0-9调整表达式

f(x*10+y)=f(x*9+x+y)=f(x+y), 成立当f(x)= x%9

"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    print(Solution().addDigits(38))
