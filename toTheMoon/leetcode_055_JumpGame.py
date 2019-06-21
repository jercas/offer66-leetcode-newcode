# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:54:22 2019

@author: jercas
"""
"""
	leetcode-55: 跳跃游戏 MEDIUM
	'贪心算法' '动态规划' '数组'
	给定一个非负整数数组，你最初位于数组的第一个位置。
	数组中的每个元素代表你在该位置可以跳跃的最大长度。
	判断你是否能够到达最后一个位置。  
"""
"""
	Thinking:
		1. 贪心算法：自底向上,从右向左迭代，对于每个节点我们检查
		是否存在一步跳跃可以到达 GOOD 的位置（currPosition + nums[currPosition] >= leftmostGoodIndex）。
		如果可以到达，当前位置也标记为 GOOD ，
		同时，这个位置将成为新的最左边的 GOOD 位置，一直重复到数组的开头，如果第一个坐标标记为 GOOD 意味着可以从第一个位置跳到最后的位置。
"""
class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		时间复杂度O(n)：84ms beaten 99.33%
		空间复杂度O(n): 13.2MB beaten 48.48%
		"""
		length = len(nums)
		if length == 0:
			return False

		lastPos = length - 1
		for i in range(lastPos, -1, -1):
			if nums[i] + i >= lastPos:
				lastPos = i
		return lastPos == 0


if __name__ == '__main__':
	Q = [[2,3,1,1,4], [3,2,1,0,4]]
	A = [True, False]
	solution = Solution()
	for i in range(2):
		if solution.canJump(Q[i]) == A[i]:
			print("In list {0}, can jump to the end? -- {1}".format(Q[i], A[i]))
	print('AC')