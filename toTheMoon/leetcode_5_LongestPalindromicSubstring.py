# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:50:20 2019

@author: jercas
"""
"""
	leetcode-198: 打家劫舍 EASY
	'字符串' '动态规划'
	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		maxl, start = 0, 0
		for i in range(n):
			if i - maxl >= 1 and s[i-maxl-1:i+1] == s[i-maxl-1:i+1][::-1]:
				start = i - maxl - 1
				maxl += 2
				continue
			if i - maxl >= 0 and s[i-maxl:i+1] == s[i-maxl:i+1][::-1]:
				start = i - maxl
				maxl += 1
		return s[start: start + maxl]


if __name__ == "__main__":
	Q = ["babad", "cbbd"]
	A = ["bab", "bb"]
	solution = Solution()
	for i in range(2):
		if A[i] == solution.longestPalindrome(Q[i]):
			print('\n', Q[i], "-->", A[i])
			print('AC')