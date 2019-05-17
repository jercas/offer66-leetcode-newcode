# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:37:21 2019

@author: jercas
"""
"""
	leetcode-15: 三数之和 MEDIUM
	'数组' '双指针'
	给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
	注意：答案中不可以包含重复的三元组。
"""
"""
	Thinking:
		1: 首先直接考虑暴力三循环， O(n^3)直接超时没啥好说的；
		2：考虑借鉴TwoSum中的哈希表将时间复杂度优化到 O(n^2)，先固定两个数，套用哈希表寻找第三个数。
		3：使用双指针，只固定一个数，寻找另外两数a+b=-c，即将三数相加转化为两数相加等于第三个数
			先对数组排序以处理重复结果情况，遍历时遇到重复数字直接跳过。
"""
class Solution(object):
	def threeSum1(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		时间复杂度：O(n^3)，超时
		空间复杂度：O(1)，未使用额外空间
		"""
		nums.sort()
		n = len(nums)
		res = []
		for i in range(n - 2):
			for j in range(i + 1, n - 1):
				for k in range(j + 1, n):
					if nums[i] + nums[j] + nums[k] == 0:
						res.append([nums[i], nums[j], nums[k]])
		res = list(set([tuple(t) for t in res]))
		res = [list(v) for v in res]
		return res


	def threeSum2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		时间复杂度：O(n^2)，超时
		空间复杂度：O(n)，使用哈希表空间换时间
		"""
		nums.sort()
		n = len(nums)
		res = []
		for i in range(n - 2):
			hashmap = {}
			for j in range(i + 1, n - 1):
				another = 0 - nums[i] - nums[j]
				if another in hashmap:
					r = [nums[i], nums[j], nums[hashmap[another]]]
					res.append(r)
				hashmap[nums[j]] = j
		return res


	def threeSum3(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		时间复杂度：O(n)，一次遍历得出结果，524ms beaten 92.02%
		空间复杂度：O(1)，未使用额外空间， 14.8MB beaten 83.17%
		"""
		nums.sort()
		n = len(nums)
		res = []
		for i in range(n - 2):
			# 数组已经排序，如果定位数字自身已经大于0，且其后的都大于0，则在此范围内任何组合均大于0，直接跳出循环
			if nums[i] > 0:
				break
			# 定位时，因为已经排序完毕，若出现两个相同数的情况，其结果也必定一致，直接跳出该次循环
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			# 定位一个数，对另外两个数采用双向查找
			l, r = i + 1, n - 1
			while l < r:
				cur = nums[l] + nums[r] + nums[i]
				if cur == 0:
					res.append([nums[i], nums[l], nums[r]])
					l += 1
					r -= 1
					while l < r and nums[l] == nums[l - 1]:
						l += 1
					while l < r and nums[r] == nums[r + 1]:
						r -= 1
				elif cur < 0:
					l += 1
				else:
					r -= 1
		return res


if __name__ == "__main__":
	Q = [-1, 0, 1, 2, -1, -4]
	A = [[-1, -1, 2], [-1, 0, 1]]
	solution = Solution()
	if solution.threeSum1(Q) == A and solution.threeSum3(Q) == A:
			print("In {0}, the sum of {1} -> 0".format(Q, A))
	print("AC")