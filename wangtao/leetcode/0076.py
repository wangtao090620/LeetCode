#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-12 08:51

# 思路：滑动窗口问题
# 只要保证窗口字符串含有 t 中的字符的个数大于等于t里相应元素的个数


from collections import Counter
from collections import defaultdict


class Solution:
    # def minWindow(self, s, t):
    #     need, missing = Counter(t), len(t)
    #     start, end = 0, 0
    #     i = 0
    #     for j, char in enumerate(s, 1):
    #         if need[char] > 0:
    #             missing -= 1
    #         need[char] -= 1
    #
    #         if missing == 0:
    #             while i < j and need[s[i]] < 0:
    #                 need[s[i]] += 1
    #                 i += 1
    #             need[s[i]] += 1
    #             missing += 1
    #             if end == 0 or j - i < end - start:
    #                 start, end = i, j
    #             i += 1
    #     return s[start:end]

    def minWindow(self, s, t):
        need = Counter(t)
        start, end, res = 0, 0, ""
        counter, min_len = len(t), float("inf")  # 正无穷，float("-inf"):负无穷
        while end < len(s):
            if need[s[end]] > 0:
                counter -= 1
            need[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if need[s[start]] == 0:
                    counter += 1
                need[s[start]] += 1
                start += 1
        return res


if __name__ == '__main__':
    s = "ABAACBAB"
    t = "ABC"
    a = Solution().minWindow(s, t)
    print(a)

    print(float("inf") < 2)
