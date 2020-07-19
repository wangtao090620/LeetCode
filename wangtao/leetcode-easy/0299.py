#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-19 15:04
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        d1 = dict(Counter(list(secret)))
        d2 = dict(Counter(list(guess)))
        print(d1)
        print(d2)


        for i in d1:
            if i in d2:
                cows += min(d1[i], d2[i])
        cows = cows - bulls
        return str(bulls) + 'A' + str(cows) + 'B'


if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    print(Solution().getHint(secret, guess))
