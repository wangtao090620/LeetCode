#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-24 15:45


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = [0 for _ in range(len(num1) + len(num2))]

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # 乘积在res对应的索引位置
                p1, p2 = i + j, i + j + 1
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                # 累加到res上面，之前可能进一位
                sums = mul + res[p2]

                res[p2] = sums % 10  # 个位
                res[p1] += sums // 10  # 取出十位

        cur = 0
        # 跳过前缀为0的数
        while cur < len(res) and res[cur] == 0:
            cur += 1
        # 去除前导0
        res_str = ''
        # res的每一位拼接在一起就是最终答案
        for i in range(cur, len(res)):
            res_str += str(res[i])
        if res_str == '':
            return '0'
        return res_str


if __name__ == '__main__':
    print(Solution().multiply("123", "45"))
