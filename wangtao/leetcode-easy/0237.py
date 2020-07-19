#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 16:53


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
将要删除的节点的值替换为它后面节点的值，然后删除该节点的下一个节点
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    pass
