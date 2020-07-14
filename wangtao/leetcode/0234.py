#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-28 10:12

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # 快指正到尾部，慢指针正好在链表一半的位置
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None

        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True


if __name__ == '__main__':
    pass
