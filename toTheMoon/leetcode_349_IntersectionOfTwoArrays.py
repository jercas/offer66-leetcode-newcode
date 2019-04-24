# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:26:34 2019

@author: jercas
"""
"""
	leetcode-349: 两个数组的交集 EASY
	'数组' '排序' '哈希表' '双指针' '二分查找'
	给定两个数组，编写一个函数来计算它们的交集。
	
	Hint:
		输出结果中的每个元素一定是唯一的。
		我们可以不考虑输出结果的顺序。
"""
class Solution(object):
	def intersection1(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		res = list()
		hashMap = dict()
		for i in range(len(nums1)):
			if nums1[i] not in hashMap:
				hashMap[nums1[i]] = i
		for j in range(len(nums2)):
			if nums2[j] in hashMap and nums2[j] not in res:
				res.append(nums2[j])
		return res

	def intersection2(self, nums1, nums2):
		return list(set(nums1) & set(nums2))

if __name__ == "__main__":
	Q1, Q2 = [[1, 2, 2, 1], [4, 9, 5]], [[2, 2], [9, 4, 9, 8, 4]]
	A = [[2], [9, 4]]
	solution = Solution()
	for i in range(2):
		if solution.intersection1(Q1[i], Q2[i]) == A[i] and solution.intersection2(Q1[i], Q2[i]):
			print("{0} and {1} -> intersection = {2}".format(Q1[i], Q2[i], A[i]))
			print('AC')