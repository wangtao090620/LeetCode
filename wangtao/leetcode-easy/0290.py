#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 11:25


"""
和题目205一样

前一个字符串字符作为key，后一个字符作为value

"""


class Solution(object):
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(' ')
        if len(pattern) != len(str): return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if str[i] in dct.values():
                    return False
                dct[pattern[i]] = str[i]
            else:
                if dct[pattern[i]] != str[i]:
                    return False
        return True


if __name__ == '__main__':
    pass
