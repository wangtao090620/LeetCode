#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-05 08:42


# DFS 剪枝 做搜索回溯的套路是画图

class Solution:
    def combinationSum(self, condidates, target):
        res = []
        condidates.sort()
        self.dfs(condidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return

        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


if __name__ == '__main__':
   pass
