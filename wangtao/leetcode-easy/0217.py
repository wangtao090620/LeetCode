#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 15:35
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = dict()

        for i in nums:
            if i in dct:
                return True
            dct[i] = i
        return False


if __name__ == '__main__':
    pass
