# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:33:26 2019

@author: jercas
"""
"""
	leetcode-27: 移除元素 EASY
	'数组' '双指针'
	给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
	Tips:不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
		 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
"""
	Thinking:
		0. 考虑类似于No.26移除数组中重复元素的题，设置正确数组下标计数i的方法；
		1. 正向遍历，遇targer即删除，一直出错，后来发现是Py中pop()函数的问题；
		2. 利用for正循环时，因为正向遍历的话如果后面那个数字和前面已删除的数字相同，pop删除后后面的元素全部顺序前移，后面数字的索引会变成之前
		已删除数字的索引，但是正在遍历的索引已经检查过这个索引了，会过掉，所以倒序遍历倒着就不会有覆盖现象了；
		i.e., [2,3,3,2]，i=1的时候num[1]=3，这个被删了以后，下一次应该迭代i=2，但是列表已变成[2,3,2]，i=2对应的num[2]=2，中间那个3就删不掉了，而且迭代到i=3的时候会越界。
		3. 或者使用while循环也可以避免此问题。
"""


class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		时间复杂度：O(n)，一次循环遍历，20ms beaten 98.21%
		空间复杂度：O(1)，未使用额外空间， 11.6MB beaten 45.67%
		"""
		#逆序循环
		#for i in range(len(nums)-1, -1, -1):
		#for i in reversed(range(len(nums))):
		i = 0
		while i < len(nums):
			if nums[i] == val:
				nums.pop(i)
			else:
				i += 1
		return len(nums)


if __name__ == '__main__':
	Q11 = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2]]
	Q1 = [[3,2,2,3], [0,1,2,2,3,0,4,2]]
	Q2 = [3, 2]
	A2 = [2, 5]
	solution = Solution()
	for i in range(2):
		if solution.removeElement(Q1[i], Q2[i]) == A2[i]:
			print('After remove the target value {0}, the array {1} turn to {2} with length of {3}'.format(
				Q2[i], Q11[i], Q1[i], A2[i]))
	print('ac')