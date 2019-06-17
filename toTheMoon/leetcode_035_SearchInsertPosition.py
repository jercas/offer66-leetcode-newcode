# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:46:52 2019

@author: jercas
"""
"""
	leetcode-35: 搜索插入位置 EASY
	'数组' '二分查找'
	给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
	你可以假设数组中无重复元素。
"""
"""
	Thinking:
		1. 二分查找，搜索指定target+搜索不到后根据lr指针位置判断的结合题
"""


class Solution(object):
	def searchInsert1(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		时间复杂度：O(logn)，二分查找，40ms beaten 99.15%
		空间复杂度：O(1)，未使用额外空间，12.1MB beaten 41.21%
		"""
		l = 0
		r = len(nums)

		while l < r:
			m = (l + r) // 2
			if nums[m] == target:
				return m
			elif nums[m] < target:
				l = m + 1
			elif nums[m] > target:
				r = m
		return l


	def searchInsert2(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		时间复杂度：O(logn)，二分查找，40ms beaten 99.15%
		空间复杂度：O(1)，未使用额外空间，12.1MB beaten 41.21%
		"""
		l = 0
		r = len(nums) - 1

		while l < r:
			m = (l + r) // 2
			if nums[m] == target:
				return m
			elif nums[m] < target:
				l = m + 1
			elif nums[m] > target:
				r = m

		if nums[l] < target:
			return l + 1
		else:
			if l == 0:
				return 0
			else:
				return l


if __name__ == '__main__':
	Q1 = [[1,3,5,6], [1,3,5,6], [1,3,5,6], [1,3,5,6], [1], [1], [1], [1,3]]
	Q2 = [5, 2, 7, 0, 1, 0, 2, 3]
	A  = [2, 1, 4, 0, 0, 0, 1, 1]
	solution = Solution()
	for i in range(len(A)):
		if solution.searchInsert1(Q1[i], Q2[i]) == A[i] and solution.searchInsert2(Q1[i], Q2[i]) == A[i]:
			print('The insert position of {1} in {0} is {2}'.format(Q1[i], Q2[i], A[i]))
	print('ac')