# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:58:42 2019

@author: jercas
"""
"""
	leetcode-374: 猜数字大小 EASY
	'二分查找'
	我们正在玩一个猜数字游戏。 游戏规则如下：
	我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
	每次你猜错了，我会告诉你这个数字是大了还是小了。
	你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
	Tips:
		-1 : 我的数字比较小
		 1 : 我的数字比较大
		 0 : 恭喜！你猜对了！   
"""
"""
	Thinking:
		1. 标准二分查找，顺带练习了下变体的写法
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber1(self, n):
		"""
		:type n: int
		:rtype: int
		时间复杂度：O(log2n)，标准二分查找， 16ms beaten 98.66%
		空间复杂度：O(1)，未使用额外空间，11.6MB beaten 45.82%
		"""
		l = 1
		r = n
		while l < r:
			m = (l + r) // 2
			res = self.guess(m)
			if res == 1:
				l = m + 1
			else:
				r = m
		return l


	def guessNumber2(self, n):
		"""
		:type n: int
		:rtype: int
		时间复杂度：O(log2n)，标准二分查找，20ms beaten 93.74%
		空间复杂度：O(1)，未使用额外空间，11.6MB beaten 45.82%
		"""
		l = 1
		r = n
		while l <= r:
			m = (l + r) // 2
			res = self.guess(m)
			if res == 0:
				return m
			elif res == -1:
				r = m - 1
			elif res == 1:
				l = m + 1


	def guess(self, n):
		print('')