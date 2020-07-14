#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-05 08:44

from collections import deque

if __name__ == '__main__':
    d = deque()
    d.append(1)
    d.append(2)
    d.append(3)

    print(d)

    print(d.pop())

    l = [2, 3, 4, 10, 9]

    l.append(12)

    print(l.pop(0))

    sum = 0

    sum += l.pop()

    # l.extend([3])
    # print(l)

    print(l[2:-1])

    print(l[0:2])

    a = set()

    a.add(3)

    print(3 in a)

    print(4 % 3)

    print([1 + 1] * 1 + [1] * 4)

    print(l[::-1])

