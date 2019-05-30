# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:19:32 2019

@author: jercas
"""
"""
	leetcode-34: 在排序数组中查找元素的第一个和最后一个位置 MEDIUM
	'数组' '二分查找'
	给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
	Tips:
		你的算法时间复杂度必须是 O(log n) 级别。
		如果数组中不存在目标值，返回 [-1, -1]。
"""
"""
	Thinking:
		1. 二分查找，搜索问题且为有序数组，首先考虑二分查找，根据题意，需要先找到一个target然后找其左右是否存在另一个相同target,以此类推找到
		target区间确定起始位置。
		2. 采用两种二分思路：
				（0）注意两种二分方式，判断条件的不同
				（1）先找边界
					若target存在，直接将m定位到起始位置的target，while结束后，l和r指针均会指向起始位置target，随后只需向右迭代找到target接受位置即可；
					若target不存在，l和r两种情况，一是数组中所有值均小于target -- l r会指向 -1 位置，而是均大于targer -- l r会指向 0 位置，随后在下个判断中因l值不等于target均跳出，直接返回[-1,-1]
				（2）先找值 -- 传统方法
					传统二分法，直接定位到某个target的位置m，随后两边遍历找target起始终结边界
"""


class Solution(object):
	def searchRange1(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		时间复杂度：O(log2n)，二分查找变体，80ms beaten 99.79%
		空间复杂度：O(1)，未使用额外空间，13MB beaten 38.34%
		"""
		res = [-1, -1]
		n = len(nums)
		if not nums:
			return res

		l = 0
		r = n

		while l < r:
			m = (l + r) // 2
			if nums[m] < target:
				l = m + 1
			else:
				r = m
		if l < n and nums[l] == target:
			res[0] = l
			while l < len(nums) and nums[l] == target:
				l += 1
			res[1] = l - 1
		return res


	def searchRange2(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		时间复杂度：O(log2n)，二分查找变体，88ms beaten 99.37%
		空间复杂度：O(1)，未使用额外空间，12.9MB beaten 41.11%
		"""
		res = [-1, -1]
		n = len(nums) - 1
		if not nums:
			return res

		l = 0
		r = n
		m = 0

		while l <= r:
			m = (l + r) // 2
			if nums[m] == target:
				break
			elif nums[m] < target:
				l = m + 1
			else:
				r = m - 1

		if nums[m] == target:
			i, j = m, m
			while i > 0 and nums[i - 1] == target:
				i -= 1
			while j < n and nums[j + 1] == target:
				j += 1
			res = [i, j]
		return res


if __name__ == '__main__':
	Q1 = [[5,7,7,8,8,10], [5,7,7,8,8,10]]
	Q2 = [8, 6]
	A  = [[3, 4], [-1, -1]]
	solution = Solution()
	for i in range(2):
		if solution.searchRange1(Q1[i], Q2[i]) == A[i] and solution.searchRange2(Q1[i], Q2[i]) == A[i]:
			print("The start and end position of {0} in {1} is {2}".format(Q2[i], Q1[i], A[i]))
	print('ac')