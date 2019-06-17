# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:30:27 2019

@author: jercas
"""
"""
	leetcode-9: 回文数 EASY
	'数学'
	判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
	Hint:
		考虑不将输入转为字符串来处理
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
	def isPalindrome1(self, x):
		"""
		:type x: int
		:rtype: bool
		时间复杂度：O(1)，56ms beaten 100%
		空间复杂度：O(n)，但使用了变量来保存翻转后的输入数，11.7MB beaten 27.30%
		"""
		# 剔除边界变量，负数和个位数
		if x < 0 or ( x % 10 == 0 and x != 0 ):
			return False
		# 判断翻转溢出和翻转后的回文情况
		if int(str(x)) == int(str(x)[::-1]) and int(str(x)[::-1]) < pow(2, 31) - 1:
			return True


	def isPalindrome2(self, x):
		"""
		:type x: int
		:rtype: bool
		时间复杂度：O(1)，56ms beaten 100%
		空间复杂度：O(n)，但使用了变量来保存翻转后的输入数，11.7MB beaten 32.08%
		"""
		# 剔除边界变量，负数和个位数
		if x < 0 or (x % 10 == 0 and x != 0):
			return False

		reverted = 0
		while x > reverted :
			reverted = reverted*10 + x%10
			x = x // 10
		# 当输入数为奇数时，需要再通过次整除10取出中间数
		# 如12321，循环结束时 x=12 而 reverted = 123, 需要将reverted // 10 = 12，再行判断
		return x == reverted or x == reverted // 10


if __name__ == "__main__":
	Q = [121, -121, 10, 0]
	A = [True, False, False, True]
	solution = Solution()
	for i in range(4):
		if solution.isPalindrome1(Q[i]) == A[i] and solution.isPalindrome2(Q[i]) == A[i]:
			print("Num {0} is a {1} palindrome".format(Q[i], A[i]))
	print("AC")