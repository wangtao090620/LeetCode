#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 18:53

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

"""
from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or len(s) == 0:
            return False

        dp = [False for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i + 1] in wordDict and (j == 0 or dp[j - 1]):
                    dp[i] = True
                    break
        return dp[len(s) - 1]


if __name__ == '__main__':
    s = "applepenapple"

    wordDict = ["apple", "pen"]

    print(Solution().wordBreak(s, wordDict))
