#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-04 14:10


class Solution:
    def longestValidParentheses(self, s):

        dp, stack = [0] * (len(s) + 1), []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1  # [0,0,2,0,0,2,6]
        return max(dp)


if __name__ == '__main__':
    s = "()(())"
    # s = ")"

    solution = Solution()

    i = solution.longestValidParentheses(s)

    print(i)
