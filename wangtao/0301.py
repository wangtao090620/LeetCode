#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-07 18:16


"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

"""
from typing import List

"""
思路：
这个想法很简单，使用输入字符串s，我们通过删除一个(或来生成所有可能的状态)，检查它们是否有效，

如果在当前级别上找到有效的状态，则将它们放入最终结果列表，然后完成操作，否则，添加将他们排入队列，并继续进行下一个阶段。


思路：

我们都知道如何使用堆栈检查括号中的字符串是否有效。或更简单的使用计数器。
计数器为“（”时将增加，为“）时将减少。每当计数器为负数时，前缀中的'）'多于'（'。

为了使前缀有效，我们需要删除“）”。问题是：哪一个？答案是前缀中的任何一个。但是，如果删除任何一个，我们将生成重复的结果，例如：s =（）），

我们可以删除s [1]或s [2]，但结果是相同的（）。因此，我们限制自己删除一系列连续的）中的第一个。

删除后，前缀有效。然后，我们递归调用该函数以解决字符串的其余部分。但是，我们需要保留其他信息：最后的移走位置。

如果我们没有这个位置，我们将通过在两个步骤中以不同的顺序删除两个'）'来生成重复项。
为此，我们将继续跟踪最后一个移除位置，并在此之后仅移除'）'。

现在有人问。那'（'呢？如果s ='（（）（（）'），我们需要删除'（'呢？
怎么办？答案是：从右到左做同样的事情。
但是，一个更聪明的主意是：反转字符串并重用代码！

"""


class Solution:
    # def removeInvalidParentheses(self, s: str) -> List[str]:
    #
    #     visited = {s}
    #
    #     return self.dfs(s, visited)
    #
    # def dfs(self, s, visited):
    #     mi = self.calc(s)
    #     if mi == 0:
    #         return [s]
    #     res = []
    #     for i in range(len(s)):
    #
    #         if s[i] in ('(', ')'):
    #             tmp = s[:i] + s[i + 1:]
    #             if tmp not in visited and self.calc(tmp) < mi:
    #                 visited.add(tmp)
    #                 res.extend(self.dfs(tmp, visited))
    #     return res
    #
    # def calc(self, s):
    #     a = b = 0
    #     for c in s:
    #         a += {'(': 1, ')': -1}.get(c, 0)
    #         b += a < 0
    #         a = max(a, 0)
    #     return a + b

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.remove(s, result, 0, 0, ('(', ')'))
        return result

    def remove(self, s, result, last_i, last_j, par):
        count = 0
        for i in range(last_i, len(s)):
            count += (s[i] == par[0]) - (s[i] == par[1])
            if count >= 0:
                continue
            for j in range(last_j, i + 1):  # ) 多了 删除 )4
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], result, i, j, par)
            return
        reversed_s = s[::-1]
        if par[0] == '(':
            self.remove(reversed_s, result, 0, 0, (')', '('))
        else:
            result.append(reversed_s)


if __name__ == '__main__':
    print(Solution().removeInvalidParentheses("(()(()"))

    # print({"dfasdfsdf"})
