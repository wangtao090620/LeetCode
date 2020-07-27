#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-26 14:35

"""
难点就在找旋转点
1->2->3->4->5->NULL, k = 2

1->2->3->NULL

4->5->NULL

---> 4->5->1->2->3->NULL

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        p2 = dummy
        num = 0
        while p1.next:
            num += 1
            p1 = p1.next
        k = num - k % num
        while k > 0:
            p2 = p2.next
            k -= 1
        p1.next = dummy.next
        dummy.next = p2.next
        p2.next = None

        return dummy.next


if __name__ == '__main__':
    pass
