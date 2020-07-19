#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 14:34

"""
输入: s = "egg", t = "add"
输出: true

将出现的字符用[]存起来计数

"""


class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     d1, d2 = {}, {}
    #
    #     for i, v in enumerate(s):
    #         d1[v] = d1.get(v, []) + [i]
    #     for i, v in enumerate(t):
    #         d2[v] = d2.get(v, []) + [i]
    #     print(d1)
    #     print(d2)
    #     return sorted(d1.values()) == sorted(d2.values())

    """
        分别遍历s和t，用字典和列表保存每个字符的编号。（编号从1开始，同字符的编号相同）
        返回s和t的编号列表是否相同。
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:

                if t[i] in dct.values():  # 排除ab，aa情况
                    return False

                dct[s[i]] = t[i]
            else:
                if dct[s[i]] != t[i]:
                    return False

        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic('ab', 'aa'))
