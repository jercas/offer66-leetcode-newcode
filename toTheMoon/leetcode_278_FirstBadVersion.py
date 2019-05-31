# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:58:42 2019

@author: jercas
"""
"""
	leetcode-34: 在排序数组中查找元素的第一个和最后一个位置 MEDIUM
	'二分查找'
	你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
	假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
	Tips:
		你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
		
	i.e., 给定 n = 5，并且 version = 4 是第一个错误的版本。
		调用 isBadVersion(3) -> false
		调用 isBadVersion(5) -> true
		调用 isBadVersion(4) -> true
		所以，4 是第一个错误的版本。 
"""
"""
	Thinking:
		1. 变形问法的二分查找问题，相当于No.34里找多个target中的起始位置
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
	def firstBadVersion1(self, n):
		"""
		:type n: int
		:rtype: int
		时间复杂度：O(logn)，二分查找，12ms beaten 99.36%
		空间复杂度：O(1)，未使用额外空间，11.6 MB beaten 30.29%
		"""
		l = 0
		r = n
		while l < r:
			if r - l == 1:
				return r
			m = (l+r) // 2
			if self.isBadVersion(m):
				r = m
			else:
				l = m


	def firstBadVersion2(self, n):
		l = 0
		r = n
		while l < r:
			m = (l + r) // 2
			if self.isBadVersion(m):
				r = m
			else:
				l = m + 1
		return l


	def firstBadVersion3(self, n):
		l = 1
		r = n
		while l <= r:
			m = (l + r) // 2
			if self.isBadVersion(m) and self.isBadVersion(m - 1) == False:
				return m
			elif self.isBadVersion(m) == False:
				l = m + 1
			elif self.isBadVersion(m) == True:
				r = m - 1

	def isBadVersion(self, n):
		print('')