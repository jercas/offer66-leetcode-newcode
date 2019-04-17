# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:05:00 2019

@author: jercas
"""
"""
	leetcode-198: 打家劫舍 EASY
	'动态规划'
	你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
	如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
	给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""
class Solution:
	def rob1(self, nums: 'List[int]') -> int:
		if len(nums) == 0:
			return 0
		if len(nums) <= 2:
			return max(nums)

		dp = [0 for _ in range(0, 2)]
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])

		for i in range(2, len(nums)):
			dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
		return dp[(len(nums) - 1) % 2]


	def rob2(self, nums: 'List[int]') -> int:
		if len(nums) == 0:
			return 0
		if len(nums) <= 2:
			return max(nums)

		dp = [nums[0], max(nums[0], nums[1])]
		for num in nums[2:]:
			tmp = max(dp[0] + num, dp[1])
			dp[0] = dp[1]
			dp[1] = tmp
		return dp[1]


if __name__ == "__main__":
	Q = [[1, 2, 3, 1], [2,7,9,3,1]]
	A = [4, 12]
	solution = Solution()
	for i in range(2):
		if A[i] == solution.rob1(Q[i]) and A[i] == solution.rob2(Q[i]):
			print('\n', Q[i], "-->", A[i])
			print('AC')