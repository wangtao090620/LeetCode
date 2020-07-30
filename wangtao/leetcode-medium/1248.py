#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-28 22:50
from typing import List

"""

给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_dict, odd_num, res = {}, 0, 0
        odd_dict[0] = 1
        for num in nums:
            if num % 2 == 1:
                odd_num += 1
            if (odd_num - k) in odd_dict:
                res += odd_dict[odd_num - k]
            odd_dict[odd_num] = odd_dict.get(odd_num, 0) + 1

        return res


if __name__ == '__main__':
    print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
