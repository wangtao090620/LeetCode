#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 22:38

"""
双指针问题

left，right 如果不是数字和字母则不向前移动

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1

            if left > right:
                break

            else:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
