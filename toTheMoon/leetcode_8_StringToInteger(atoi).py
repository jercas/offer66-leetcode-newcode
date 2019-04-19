# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:44:33 2019

@author: jercas
"""
"""
	leetcode-8: 字符串转换整数 (atoi - ascii to integer) MEDIUM
	'数学' '字符串'
	请你来实现一个 atoi 函数，使其能将字符串转换成整数。
	首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
	当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
	该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

	Hint:
		假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
		在任何情况下，若函数不能进行有效的转换时，请返回 0。
	PS:
		假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""
class Solution:
	def Atoi(self, s: str) -> int:
		s = s.strip()
		res = 0
		i = 0
		n = len(s)
		sign = 1
		max_num = 2 ** 31 - 1
		min_num = -2 ** 31

		if i < n:
			if s[i] == "-":
				sign = -1
				i += 1
			elif s[i] == "+":
				i += 1

		while i < n and s[i].isdigit():
			# print(res)
			res = 10 * res + int(s[i])
			i += 1

		res = res * sign
		res = min(res, pow(2, 31) - 1)
		res = max(res, pow(-2, 31))
		return res


if __name__ == "__main__":
	Q = ['42', "   -42", "words and 987", "4193 with words", "-91283472332"]
	A = [42, -42, 0, 4193, -2147483648]
	solution = Solution()
	for i in range(5):
		if A[i] == solution.Atoi(Q[i]):
			print(Q[i], "-->", A[i])
			print('AC')