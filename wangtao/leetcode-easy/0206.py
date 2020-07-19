#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 15:24


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur, nxt = None, head, head
        while cur:
            nxt = nxt.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverse(self, head):

        dummy = ListNode(-1)
        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt
        return dummy.next


if __name__ == '__main__':
    pass
