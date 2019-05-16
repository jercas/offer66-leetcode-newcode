# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:15:35 2019

@author: jercas
"""
"""
	leetcode-14: 最长公共前缀 MEDIUM
	'数组' '双指针'
	给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
	假定每组输入只存在唯一答案。
"""
"""
	Thinking:
		0: 类同No.15 ThreeSum, 对输入数组的遍历方式一样，只需变换逻辑判断由 ==0 -》 closest to target即可
			且要求输出的最相近的值，而非三个数的数组，也不需要考虑No.15中重复数组情况的问题。
"""


class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		时间复杂度：O(n)，一次遍历得出结果，76ms beaten 96.65%
		空间复杂度：O(1)，未使用额外空间， 11.6MB beaten 40.86%
		"""
		# 排序简化逻辑
		nums.sort()
		n = len(nums)
		res = 0
		min_diff = float('inf')
		for i in range(n - 2):
			# 定位时，因为已经排序完毕，若出现两个相同数的情况，其结果也必定一致，直接跳出该次循环
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			l, r = i + 1, n - 1

			while l < r:
				cur = nums[l] + nums[r] + nums[i]
				diff = cur - target

				if abs(diff) < min_diff:
					min_diff = min(abs(diff), min_diff)
					res = cur
				# 找到最近距离（0），直接返回结果
				if diff == 0:
					return res
				# 排序后数组，若距离较小，移动l提升diff
				elif diff < 0:
					l += 1
				# 同时，距离过大，移动r减小diff
				else:
					r -= 1
		# 找到相对最近距离，返回结果
		return res


if __name__ == "__main__":
	Q, T = [-1,2,1,-4], 1
	A = 2
	solution = Solution()
	if solution.threeSumClosest(Q, T) == A:
			print("The cloest three sum result of {0} to {1} is {2}".format(Q, T, A))
	print("AC")