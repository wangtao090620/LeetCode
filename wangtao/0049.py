#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-06 09:39


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))  # 保证key一致
            d[key] = d.get(key, []) + [w]
        return d.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    g = Solution().groupAnagrams(strs)
