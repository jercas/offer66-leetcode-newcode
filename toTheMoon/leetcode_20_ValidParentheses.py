# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:54:41 2019

@author: jercas
"""
"""
	leetcode_20 : 有效的括号 EASY
	'栈' '字符串'
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
	有效字符串需满足：
		左括号必须用相同类型的右括号闭合。
		左括号必须以正确的顺序闭合。
		注意空字符串可被认为是有效字符串。
"""
"""
	Thinking:
		0. 字符串匹配问题，直接套用‘栈’解决
"""
class Solution(object):
	def isValid(self, s):
		"""
		:type s: s
		:rtype: bool
		"""
		stack = []
		mapping = {')':'(', ']':'[', '}':'{'}
		for char in s:
			# 右括号时进行判断
			if char in mapping:
				# 取出栈顶左括号
				top = stack.pop() if stack else '#'
				# 当栈顶左括号和当前右括号不匹配时，无效
				if mapping[char] != top:
					return False
			# 左括号入栈
			else:
				stack.append(char)
		# 有效情况下，最后为空栈
		return not stack


if __name__ == '__main__':
	Q = ['()', '()[]{}', '(]', '([)]', '([{}])']
	A = [True, True, False, False, True]
	solution = Solution()
	for i in range(5):
		if solution.isValid(Q[i]) == A[i]:
			print('The string {0} is a {1} valid parentheses'.format(Q[i], A[i]))
	print('AC')