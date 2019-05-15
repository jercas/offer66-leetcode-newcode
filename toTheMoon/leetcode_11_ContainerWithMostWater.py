# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:30:41 2019

@author: jercas
"""
"""
	leetcode-11: 盛最多水的容器 MEDIUM
	'数学' '双指针'
	给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
	说明：你不能倾斜容器，且 n 的值至少为 2。
"""
"""
	Thinking:
		0.排除临界条件，(1)所有负数都不会为回文；(2)个位数不会为回文;(3)如翻转要考虑翻转溢出问题 2^31-1。
		1.简单处理方法，直接将输入数转为字符串判断翻转后是否相同，以及翻转后是否溢出即可。
		2.不转字符串方法，为了避免整个翻转会导致的溢出问题，只翻转一半，判断前后段是否相同，相同即为回文，如1221-》12 & 12；
						至于如何取出后半段，可以让输入数每次'取10模' -- 1221 % 10 = 1, 而输入数剔除取出数的移动，则可以'整除'10 -- 1221 // 10 = 122
						最后将取出的后半段分别乘10^n即可，1*10 + 2 = 12 == 12 -> True
						而如何判断已经取到了输入数的一半，跳出循环，则可考虑当原始数 小于/等于 提出数时，就相当于已经将后半段都提出来了，可以开始比较
"""


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		maxV = 0
		l = 0
		r = len(height) - 1

		while l < r:
			if height[l] < height[r]:
				maxV = max(maxV, height[l] * (r - l))
				l += 1
			else:
				maxV = max(maxV, height[r] * (r - l))
				r -= 1
			print(maxV)
		return maxV