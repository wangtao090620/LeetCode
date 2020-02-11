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

    print(d.popleft())
