# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:24:56 2019

@author: jercas
"""
"""
	leetcode-7: 整数翻转 EASY
	'数学'
	给出一个 "32 位" 的 "有符号" 整数，你需要将这个整数中每位上的数字进行反转。
	
	Hint:
		假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
class Solution:
	def reverse(self, x: int) -> int:
		if x == 0:
			return 0

		minus = False
		if x < 0:
			minus = True
			x = abs(x)
		rev = int(str(x)[::-1])

		if minus:
			rev = -rev
		if pow(-2, 31) < rev < pow(2, 31) - 1:
			return rev
		return 0


if __name__ == "__main__":
	Q = [123, -123, 120, 1534236469]
	A = [321, -321, 21, 0]
	solution = Solution()
	for i in range(4):
		if A[i] == solution.reverse(Q[i]):
			print(Q[i], "-->", A[i])
			print('AC')