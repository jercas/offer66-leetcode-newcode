# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:36:22 2019

@author: jercas
"""
"""
	leetcode-78: 子集 MEDIUM
	'数组' '回溯'
	给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
	
	Hint：
		解集不能包含重复的子集。
"""
class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 0:
			return [[]]

		res = self.subsets(nums[:-1])
		res += [a + [nums[-1]] for a in res]
		#print(ans, '\n')
		return res


if __name__ == "__main__":
	Q = [1, 2, 3]
	A = [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
	solution = Solution()
	ans = solution.subsets(Q)
	for i in A:
		if i in ans:
			print(i)
	print('AC')