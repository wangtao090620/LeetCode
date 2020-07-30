#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-26 13:16
import math

"""
n = 3,k = 3

  "123" 
  "132" 
  "213" 
  "231" 
  "312" 
  "321" 
  
3 - 1 = 2, 2! = 2
3/2 向上取整 2
  
[1,2,3]
  

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [str(i) for i in range(1, n + 1)]  # [1, n]
        res = ""
        n -= 1  # 每个不同的数开头，有(n-1)!种排列
        while n > -1:
            t = math.factorial(n)  # 阶乘
            loc = math.ceil(k / t) - 1  # 得到数组的索引
            print(loc)
            res += num[loc]  # 将确定的数添加到res中
            num.pop(loc)  # 去除得到的索引
            k %= t  # 更新k
            n -= 1
        return res


if __name__ == '__main__':
    a = math.factorial(3)
    # print(math.ceil(11 / 3))
    Solution().getPermutation(3, 3)
