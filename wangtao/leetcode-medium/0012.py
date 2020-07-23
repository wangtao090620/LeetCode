#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 10:17


class Solution:
    def intToRoman(self, num: int) -> str:

        mapping = [
            ('M', 1000), ('CM', 900), ('D', 500),
            ('CD', 400), ('C', 100), ('XC', 90),
            ('L', 50), ('XL', 40), ('X', 10),
            ('IX', 9), ('V', 5), ('IV', 4),
            ('I', 1)

        ]
        res = []

        for c, value in mapping:

            if num == 0: break
            count, num = divmod(num, value)

            res.append(c * count)
        return "".join(res)


if __name__ == '__main__':
    print(Solution().intToRoman(1994))
