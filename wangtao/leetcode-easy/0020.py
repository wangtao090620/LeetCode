#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 09:42


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or mapping[c] != stack.pop():
                return False
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(][]{}"))
