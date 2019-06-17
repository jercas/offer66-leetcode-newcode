# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:30:41 2019

@author: jercas
"""
"""
	leetcode-11: 盛最多水的容器 MEDIUM
	'数学' '双指针'
	给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
	找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
	说明：你不能倾斜容器，且 n 的值至少为 2。
"""
"""
	Thinking:
		0.双指针遍历：对该问题如果出现相同的容器高，则一定是有更大底长的容量更大，考虑使用双指针首尾分别进行移动，获取当前容量，并动态保存最大的容量；
				   又考虑木桶短板效应，最大容量为较短一侧筒壁高*底，每次判断是否更新最大容量后，因为更高的筒壁优先级更高，故向中间移动较短筒壁一侧；
				   当两侧指针相遇时，遍历完毕退出循环返回最大容量值，类同二分查找的循环条件。
"""


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		时间复杂度：O(n)，双指针双向遍历一次，132ms beaten 99.62%
		空间复杂度：O(1)，未使用任何额外空间，13MB beaten 39.75%
		"""
		maxV = 0
		l = 0
		r = len(height) - 1

		while l < r:
			maxV = max(maxV, min(height[l], height[r]) * (r - l))
			if height[l] < height[r]:
				l += 1
			else:
				r -= 1
		return maxV


if __name__ == "__main__":
	Q = [1,8,6,2,5,4,8,3,7]
	A = 49
	solution = Solution()
	if solution.maxArea(Q) == A:
		print("The most water of the container {0} is {1}".format(Q, A))
	print("AC")