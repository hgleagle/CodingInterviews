#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
File: test6_printLinklistTailtoHead.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:
输入一个链表，从尾到头打印链表每个节点的值。
"""
from __future__ import print_function


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.reverse_list = []

    def printListFromTailToHead(self, listNode):
        """ 从尾部到头部的列表值序列，例如[1,2,3]

        递归或者栈实现

        Returns: None

        """
        if listNode is None:
            return
        else:
            self.printListFromTailToHead(listNode.next)
        self.reverse_list.append(listNode.val)


if __name__ == "__main__":
    prev = None
    head = None
    for i in range(10):
        node = ListNode(i)
        if head is None:
            head = node
        if prev:
            prev.next = node
        prev = node
    sol = Solution()
    sol.printListFromTailToHead(head)
    print(sol.reverse_list)
