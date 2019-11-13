#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-13 18:19


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hash_map = dict()
        for i, x in enumerate(nums):  # 脚标和对应的值
            if (target - x) in hash_map:
                return [i, hash_map.get(target - x)]

            hash_map[x] = i  # 将新的值存储起来


if __name__ == '__main__':
    pass
