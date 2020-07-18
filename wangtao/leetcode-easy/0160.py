#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-17 23:32

"""
链表判断是否相等 ==
循环a1、b1 如果遍历完则将另一个链表赋值前一个

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a1, b1 = headA, headB
        while a1 != b1:
            a1 = a1.next if a1 else headB
            b1 = b1.next if b1 else headA
        return a1

if __name__ == '__main__':
    pass
