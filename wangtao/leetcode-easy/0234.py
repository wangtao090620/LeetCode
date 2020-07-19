#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 16:07

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


""""
快慢指针

快指针走完的时候，慢指针在一半的位置
"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow)

        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse(self, head):
        pre, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == '__main__':
    pass
