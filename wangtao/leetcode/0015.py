#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-16 16:07


# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# 目标c，遍历两边list 找出a和b，看c = -（a+b）满足


class Solution:
    def threeSum(self, nums: list):
        if len(nums) < 3:
            return []
        nums.sort()

        res = set()

        for i, v in enumerate(nums[:2]):  # 避免重复计算
            if i >= 1 and v == nums[i - 1]:  # 相邻的值相同
                continue
            d = {}

            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1  # 将值存储在map中，value可以是任意值，最终比较的key
                else:
                    res.add((v, -v - x, x))
        return map(list, res)


if __name__ == '__main__':

    a = [1, 2, 3, 4]



    for i, v in enumerate(a[:-2]):
        print(i)
