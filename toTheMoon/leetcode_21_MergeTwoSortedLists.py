# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:37:55 2019

@author: jercas
"""
"""
	leetcode-21: 合并两个有序链表 EASY
	'链表'
	将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
	
	Hint:
		输入：1->2->4, 1->3->4
		输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		node = ListNode(None)
		res = node
		while l1 != None and l2 != None:
			if l1.val > l2.val:
				node.next = l2
				l2 = l2.next
			else:
				node.next = l1
				l1 = l1.next
			node = node.next
		if l1 == None:
			node.next = l2
		elif l2 == None:
			node.next = l1
		return res.next

