#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 11:56
from typing import List

"""

双指针


"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 3):
            if nums[k] + nums[k + 1] * 3 > target: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            if nums[k] + nums[-1] * 3 < target: continue

            for i in range(k + 1, len(nums) - 2):
                if nums[k] + nums[i] + nums[i + 1] * 2 > target: break
                if nums[k] + nums[i] + nums[-1] * 2 < target: continue
                if i > k + 1 and nums[i] == nums[i - 1]: continue

                j, x = i + 1, len(nums) - 1

                while j < x:
                    s = nums[k] + nums[i] + nums[j] + nums[x]

                    if s > target:
                        x -= 1
                    elif s < target:
                        j += 1
                    else:
                        res.append([nums[k], nums[i], nums[j], nums[x]])
                        while j < x and nums[j] == nums[j + 1]: j += 1
                        while j < x and nums[x] == nums[x - 1]: x -= 1
                        j += 1
                        x -= 1

        return res


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
