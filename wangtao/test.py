#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-05 08:44

from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def test(self, head: ListNode):
        pre, cur, nxt = None, head, head

        while cur:
            nxt = nxt.next
            cur.next = pre
            cur = nxt
            pre = cur
        return pre


if __name__ == '__main__':
    s = 'www.baidu.com'

    print(".".join(s.split('.')[::-1]))
