# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:53:41 2019

@author: jercas
"""
"""
	leetcode-347: 前K个高频元素 MEDIUM
	'堆' '哈希表'
	给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
"""


class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		hashT = {}
		for num in nums:
			if num in hashT:
				hashT[num] += 1
			else:
				hashT[num] = 1
		res = [x[0] for x in sorted(hashT.items(), reverse=True, key=lambda hashT:hashT[1])]
		return res[:k]


if __name__ == "__main__":
	Q1, Q2 = [[1,1,1,2,2,3], [1]], [2, 1]
	A = [[1, 2], [1]]
	solution = Solution()
	for i in range(2):
		if A[i] == solution.topKFrequent(Q1[i], Q2[i]):
			print(Q1[i], "+ K =", Q2[i], "-->", A[i])
			print('AC')