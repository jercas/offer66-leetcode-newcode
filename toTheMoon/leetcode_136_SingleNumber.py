# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:14:10 2019

@author: jercas
"""
"""
	leetcode-136: 只出现一次的数字 EASY
	'位运算' '哈希表'
	给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
	说明：
	你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
"""
	Thinking:
		1. 首先想到暴力双循环，以判断位来判断是否重复来找出结果，但时间复杂度 O(n^2)，超时
		2. 再次想到运用py中set去重，随后遍历set并利用数组的count函数求解重复次数为1的值，显然不仅超时还利用了额外空间
		3. 利用异或操作：
				(1) 交换律：a ^ b ^ c <=> a ^ c ^ b
				(2) 任何数于0异或为任何数 0 ^ n => n
				(3) 相同的数异或为0: n ^ n => 0
						var a = [2,3,2,4,4]
						2 ^ 3 ^ 2 ^ 4 ^ 4 等价于  2 ^ 2 ^ 4 ^ 4 ^ 3  =>  0 ^ 0 ^3 => 3
			线性时间复杂度，且不使用额外空间
"""
class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		时间复杂度: O(s)，一次遍历线性时间内得到结果，92ms beaten 93.56%
		空间复杂度: O(1)，未使用额外空间，13.5MB beaten 34.70%
		"""
		res = 0
		for num in nums:
			res = res ^ num
		return res


if __name__ == "__main__":
	Q = [[2, 2, 1], [4, 1, 2, 1, 2]]
	A = [1, 4]
	solution = Solution()
	for i in range(2):
		if solution.singleNumber(Q[i]) == A[i]:
			print("The single number of {0} is {1}.".format(Q[i], A[i]))
	print('AC')