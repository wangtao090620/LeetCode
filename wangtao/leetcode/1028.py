#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-06-18 19:17


# def recoverFromPreorder(self, S: str) -> TreeNode:
#     if not S: return None
#
#     from collections import defaultdict
#     depth_node = defaultdict(list)  # 记录访问过的深度为depth的节点列表
#     start = 0
#     while start < len(S):
#         # 获取当前值的深度
#         end = start
#         while end < len(S) and S[end] == '-': end += 1
#         depth = end - start
#
#         # 获取当前值
#         start = end
#         while end < len(S) and S[end] != '-': end += 1
#         node = TreeNode(int(S[start:end]))
#
#         # 将当前节点放在对应的深度列表中
#         depth_node[depth].append(node)
#         # 将当前节点挂载父节点上面
#         # 为什么这里可以这样做？因为在访问每个节点之前，肯定已经访问过它的父节点了，而且是最近刚访问过，因此可以用这种方式挂载
#         if depth > 0:
#             # 优先挂载父节点的左边
#             if depth_node[depth - 1][-1].left:
#                 depth_node[depth - 1][-1].right = node
#             else:
#                 depth_node[depth - 1][-1].left = node
#
#         start = end
#     return depth_node[0][0]

if __name__ == '__main__':
    pass



