# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:40:12 2019

@author: jercas
"""
"""
	leetcode-43: 字符串相乘 MEDIUM
	'数学' '字符串'
	给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
	
	说明：
		num1 和 num2 的长度小于110。
		num1 和 num2 只包含数字 0-9。
		num1 和 num2 均不以零开头，除非是数字 0 本身。
		不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		num1 = int(num1)
		num2 = int(num2)
		return str(num1 * num2)


if __name__ == "__main__":
	Q = [['2', '3'], ['123', '456']]
	A = ['6', '56088']
	solution = Solution()
	for i in range(2):
		if A[i] == solution.multiply(Q[i][0], Q[i][1]):
			print('{0} * {1} == {2}'.format(Q[i][0], Q[i][1], A[i]))
			print('AC')