#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2019-12-24 19:47


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = start = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while slow != start:
                    slow = slow.next
                    start = start.next
                return start
        return None
    """

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        visited = set()

        node = head

        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None


if __name__ == '__main__':
    pass
