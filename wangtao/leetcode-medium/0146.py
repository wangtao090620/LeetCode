#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-27 11:33


"""

init get put

双链表

关键写写出add和remove

"""
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]

    def remove(self, node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    def add(self, node):
        pre = self.tail.pre
        pre.next = node
        self.tail.pre = node
        node.pre = pre
        node.next = self.tail




if __name__ == '__main__':
    pass
