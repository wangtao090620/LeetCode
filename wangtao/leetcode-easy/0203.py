#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 11:23


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(0)

        pre, cur, node.next = node, head, head

        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return node.next


if __name__ == '__main__':
    pass
