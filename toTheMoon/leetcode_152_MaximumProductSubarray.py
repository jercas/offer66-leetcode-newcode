# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:56:43 2019

@author: jercas
"""
"""
	leetcode-152: 乘积最大子序列 MEDIUM
	'数组' '动态规划'
	给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
	返回最大乘积
"""
import sys
class Solution:
	def maxProduct1(self, nums: 'List[int]') -> int:
		rev = nums[::-1]
		for i in range(1, len(nums)):
			nums[i] *= nums[i - 1] or 1
			rev[i] *= rev[i - 1] or 1
		print(nums, "+", rev)
		return max(max(nums), max(rev))

	def maxProduct2(self, nums: 'List[int]') -> int:
		ans = -sys.maxsize
		imax, imin = 1, 1
		for i in range(len(nums)):
			if nums[i] < 0:
				tmp  = imax
				imax = imin
				imin = tmp
			imax = max(imax*nums[i], nums[i])
			imin = min(imin*nums[i], nums[i])
			print(nums[i], '-->', 'imax', imax, 'imin', imin)
			ans  = max(ans, imax)
		return ans


if __name__ == "__main__":
	Q = [[2,3,-2,4], [-2, 0, -1], [2, -5, -2, -4, 3]]
	A = [6, 0, 24]
	solution = Solution()
	for i in range(3):
		if A[i] == solution.maxProduct2(Q[i]) and A[i] == solution.maxProduct1(Q[i]):
			Q = [[2, 3, -2, 4], [-2, 0, -1], [2, -5, -2, -4, 3]]
			print(Q[i], "-->", A[i])
			print('AC\n')