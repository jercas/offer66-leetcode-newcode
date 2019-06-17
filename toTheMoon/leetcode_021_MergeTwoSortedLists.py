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
"""
	Thinking:
		1.迭代法：不要求空间复杂度情况下，使用额外空链表进行排序，因为均为有序链表故双指针分别对比判断大小，链入排序链表即可，当有一方为空时，另一方整体链入
		排序链表中（均为有序链表，则剩下来的链表定为最后末尾的大数数列），返回排序链表即可，
		2.递归法：不使用额外空间，在原链表基础上进行链接排序。
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists1(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		时间复杂度: O(m+n)，遍历一次即可，32ms beaten 94.53%
		空间复杂度: O(m+n), 采用额外链表合并排序，11.8MB beaten 32.12%
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

	def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		时间复杂度: O(m+n)，遍历一次即可，20ms beaten 99.76%
		空间复杂度: O(m+n), 采用额外链表合并排序，11.8MB beaten 32.12%
		"""
		if not l1: return l2
		if not l2: return l1
		if l1.val < l2.val:
			l1.next = self.mergeTwoLists2(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists2(l1, l2.next)
			return l2