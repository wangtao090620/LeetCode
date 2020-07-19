#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 15:40
from typing import List

"""

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct and dct[nums[i]] >= i - k:
                return True
            dct[nums[i]] = i
        return False



if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
