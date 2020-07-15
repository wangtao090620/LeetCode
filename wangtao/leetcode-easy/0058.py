#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-15 23:56


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = count = 0
        for i in s[::-1]:
            if flag == 0 and i == ' ':
                continue
            if i != ' ':
                count += 1
                flag = 1
            else:
                break
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("hello i"))
