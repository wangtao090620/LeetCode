#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-21 14:10

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    pass
