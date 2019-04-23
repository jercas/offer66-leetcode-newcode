# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 9:50:00 2019

@author: jercas
"""
"""
	leetcode-704: 二分查找 EASY
	'数组' '二分查找'
	给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
	写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""
class Solution(object):
	def BinarySearch(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		l = 0
		r = len(nums) - 1
		while l <= r:
			mid = (l + r) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1
		return -1


if __name__ == "__main__":
	Q1, Q2 = [[-1,0,3,5,9,12], [-1,0,3,5,9,12]], [9, 2]
	A = [4, -1]
	solution = Solution()
	for i in range(2):
		if solution.BinarySearch(Q1[i], Q2[i]) == A[i]:
			print("target:{1} in array {0} -> location = {2}".format(Q1[i], Q2[i], A[i]))
			print('AC')