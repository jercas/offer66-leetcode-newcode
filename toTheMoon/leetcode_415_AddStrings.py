# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:43:51 2019

@author: jercas
"""
"""
	leetcode-415: 字符串相加 EASY
	'数学' '字符串'
	给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
	
	注意：
		num1 和num2 的长度都小于 5100.
		num1 和num2 都只包含数字 0-9.
		num1 和num2 都不包含任何前导零。
		你不能使用任何內建BigInteger库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		num1 = int(num1)
		num2 = int(num2)
		return str(num1 + num2)


if __name__ == "__main__":
	Q = [['2', '3'], ['123', '456']]
	A = ['5', '579']
	solution = Solution()
	for i in range(2):
		if A[i] == solution.addStrings(Q[i][0], Q[i][1]):
			print('{0} + {1} == {2}'.format(Q[i][0], Q[i][1], A[i]))
			print('AC')
