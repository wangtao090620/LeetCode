#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-11-15 17:02


# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。


# 暴力递归求解
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not p:
#             return not s
#         first_match = bool(s) and p[0] in {s[0], '.'}
#         if len(p) >= 2 and p[1] == '*':
#             return (self.isMatch(s, p[:2])) or first_match and self.isMatch(s[:1], p)
#         else:
#             return first_match and self.isMatch(s[1:], p[1:])
#


# 动态规划

# 1、p[j]是字母
# (a、)、p[j]==s[i]  只要匹配  p[:j - 1] 和 s[:i - 1]
# (b、)、p[j]!=s[i]  不成立

# 2、p[j]是'.'
# (a、)、只要匹配  p[:j - 1] 和 s[:i - 1]

# 3、p[j]是'*'
# (a、)、p[j-1]==s[i]或者p[j - 1]=='.'  只要匹配  p[:j] 和 s[:i - 1] 例如：s = aaab  p = a*.*  或者 s = aaab p = a*b*
# (b、)、p[j-1]!=s[i],p[:j - 2]==s[:i] 例如 s = aaab  p = a*b**

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]  # 初始化二维数组
        # dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]




if __name__ == '__main__':
    clazz = Solution()
    clazz.isMatch("abc", "abc")
