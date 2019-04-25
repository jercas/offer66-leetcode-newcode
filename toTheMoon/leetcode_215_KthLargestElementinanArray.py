# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:53:41 2019

@author: jercas
"""
"""
	leetcode-215: 数组中的第K个最大元素 MEDIUM
	'堆' '分治算法'
	在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""


class Solution(object):
	def findKthLargest1(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		nums.sort()
		return nums[-k]

	def findKthLargest2(self, nums, k):
		for i in range(0, k):
			maxV = i
			for j in range(i+1, len(nums)):
				if nums[j] > nums[maxV]:
					maxV = j
			tmp = nums[maxV]
			nums[maxV] = nums[i]
			nums[i] = tmp
		return nums[k-1]


if __name__ == "__main__":
	Q1, Q2 = [[3,2,1,5,6,4], [3,2,3,1,2,4,5,5,6]], [2, 4]
	A = [5, 4]
	solution = Solution()
	for i in range(2):
		if A[i] == solution.findKthLargest1(Q1[i], Q2[i]) and A[i] == solution.findKthLargest2(Q1[i], Q2[i]):
			print(Q1[i], "+ K =", Q2[i], "-->", A[i])
			print('AC')