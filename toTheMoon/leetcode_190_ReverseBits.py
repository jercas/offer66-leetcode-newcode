# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:29:21 2019

@author: jercas
"""
"""
	leetcode-190: 颠倒二进制位 EASY
	'位运算'
	颠倒给定的 32 位无符号整数的二进制位。
"""
class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		bit = bin(n)[2:]
		bit = (32 - len(bit)) * '0' + bit
		return int(bit[::-1], 2)


if __name__ == "__main__":
	Q = [0b00000010100101000001111010011100, 0b11111111111111111111111111111101]
	A = [964176192, 3221225471]
	solution = Solution()
	for i in range(2):
		if A[i] == solution.reverseBits(Q[i]):
			print(Q[i], "-->", A[i])
			print('AC')