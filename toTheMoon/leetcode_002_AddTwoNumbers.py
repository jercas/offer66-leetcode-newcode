# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:46:54 2019

@author: jercas
"""
"""
	leetcode-2: 两数相加 Medium
	'链表' '双指针'
	给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
	如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
	您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
		输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
		输出：7 -> 0 -> 8
		原因：342 + 465 = 807
"""
"""
	Thinking:
			1.首先想到了跟leetcode no.1 two sum的区别，two sum空间结构是数组，而本题是链表，在遍历方式上有区别；且two sum属于变化的查找问题，
		利用target-sum1查找出sum2即可，该过程利用hash最快，二分也可考虑，而本题则是一个链表操作+细节考虑的问题，对进位的操作和对长短位加数的
		处理都要注意。
			2.单位相加，首先要考虑到进位问题 -- 必须要有变量记录本位的运算是否产生进位，已经前一次相加是否产生了进位，若产生需要加入。
			3.俩链表遍历，要考虑 两位数+一位数 一位数+空 空+空等等的长短位相加问题。
			4.最高位的进位，在遍历结束后一定要考虑最高位的运算是否产生了进位，如产生要生成一个新的最高位节点进位为1，ListNode(1)。
			5.细枝末节的问题，(1)直接//整除，获取carry是否进位，而不需要x+y+c-10这么蠢; (2)同理结果直接 %10 创建新节点，而不需要x+y+c-10这么蠢。
		综上需要考虑的测试用例，10+210、None+10、99+1、23+5、None+None
"""

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		时间复杂度：O(max(m,n))，m和n分别表示l1和l2的长度， 80ms beaten 73.95%
		空间复杂度：O(max(m,n))，额外链表空间长度最多为max(m,n)+1，11.8MB beaten 29.46%。
		"""
		# 允许使用额外空间
		head = ListNode(0)
		# 保存首节点位置，方便返回结果
		res = head
		# 初始化进位
		carry = 0
		while l1 != None or l2 != None:
			# 获取本位的值，如果某一数长度将其记为0
			x = l1.val if l1 else 0
			y = l2.val if l2 else 0
			# 计算结果，注意附加上进位carry
			count = carry + x + y
			# 进位结果，整除获取
			carry = count // 10
			# 保存结果，创建新节点
			head.next = ListNode(count % 10)
			# 移动各指针
			head = head.next
			# 对俩加数链表判空，针对高位加低位数的情况
			if l1 != None:
				l1 = l1.next
			if l2 != None:
				l2 = l2.next
		# 遍历完俩加数指针，如果最高位出现进位结果，需要额外添加
		if carry > 0:
			head.next = ListNode(1)
		return res.next