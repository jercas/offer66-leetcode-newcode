# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:06:20 2019

@author: jercas
"""
"""
	leetcode-4: 寻找两个有序数组的中位数 HARD
	'数组' '二分查找' '分治算法'
	给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
	请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
	你可以假设 nums1 和 nums2 不会同时为空。
"""
"""
	Thinking:
			1.时间复杂度限制 O(log(m+n))，一时间没想到好的解决方法
			2.偷鸡方法：直接合并俩数组，组内排序后根据长度为 奇/odd or 偶/even，获取中位数 n//2 or ((n-1)//2 + (n+1)//2) / 2.0
												时间复杂度：O(m+n)，新数组组内排序，164ms beaten 24.66%
												空间复杂度：O(m+n)，使用了新空间排序合并数组，21.4MB beaten 5.12%。
			3.二分查找：首先梳理中位数概念，对num1和num2合并后的中位数，一定是[nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]
					关键在于获取num1和num2各自的边界值，假设num1的边界值为m1，则可得num2的边界值为 m2=(l1+l2+1)/2 - m1 (因为m1+m2一定是l1+l2的一半)
																							 即 len(left_part) = len(right_part)
			4.此时问题就简化为找到合适的m1,将该问题转化为了一个二分查找问题，那么如何定位m1？由中位数的特性必有 num2[left2] > num1[left1]
																							 即 max(left_part) < min(right_part)
			5.当得出m1,m2位置后，只需根据合并数组长度为奇为偶分别处理即可。
"""
class Solution(object):
	def findMedianSortedArrays1(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		时间复杂度：O(m+n)，新数组组内排序，164ms beaten 24.66%
		空间复杂度：O(m+n)，使用了新空间排序合并数组，21.4MB beaten 5.12%。
		"""
		# merge two lists then sort the merged list
		nums = nums1 + nums2
		nums.sort()
		n = len(nums)

		# l1 + l2 -> even
		if n % 2 == 0:
			return (nums[(n-1)//2] + nums[(n+1)//2]) / 2.0
		# l1 + l2 -> odd
		else:
			return nums[n//2]


	def findMedianSortedArrays2(self, nums1, nums2):
		"""
				:type nums1: List[int]
				:type nums2: List[int]
				:rtype: float
				时间复杂度：O(log(min(m, n)))，只在短数组中其左侧分隔m1 - 二分查找，112ms beaten 99.81%
				空间复杂度：O(1)，未使用额外空间，11.9MB beaten 30.41%。
				"""
		l1, l2 = len(nums1), len(nums2)
		if l1 > l2:
			return self.findMedianSortedArrays2(nums2, nums1)
		half = (l1 + l2 + 1) // 2
		left = 0
		right = l1

		while left < right:
			m1 = left + (right - left) // 2
			m2 = half - m1
			if nums1[m1] < nums2[m2 - 1]:
				left = m1 + 1
			else:
				right = m1

		m1 = left
		m2 = half - m1
		c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"),
		         nums2[m2 - 1] if m2 > 0 else float("-inf"))

		# l1 + l2 -> odd
		if (l1 + l2) % 2 == 1:
			return c1

		# l1 + l2 -> even
		c2 = min(nums1[m1] if m1 < l1 else float("inf"),
		         nums2[m2] if m2 < l2 else float("inf"))
		return (c1 + c2) / 2.0


if __name__ == "__main__":
	Q1, Q2 = [[1, 3], [1, 2]], [[2], [3, 4]]
	A = [2.0, 2.5]
	solution = Solution()
	for i in range(2):
		if solution.findMedianSortedArrays1(Q1[i], Q2[i]) == A[i] and solution.findMedianSortedArrays2(Q1[i], Q2[i]) == A[i]:
			print("The median of list - {0} and list - {1} is {2}".format(Q1[i], Q2[i], A[i]))
			print("AC")