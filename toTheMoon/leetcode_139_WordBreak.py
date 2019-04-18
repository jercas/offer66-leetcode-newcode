# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:32:31 2019

@author: jercas
"""
"""
	leetcode-139: 单词拆分 MEDIUM
	'动态规划'
	给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
	说明：
		拆分时可以重复使用字典中的单词。
		你可以假设字典中没有重复的单词。
"""


class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if len(s) == 0 or not wordDict:
			return False

		max_stride = max([len(x) for x in wordDict])
		res = [0] * (len(s) + 1)
		res[0] = 1
		for i in range(1, len(s) + 1):
			for j in range(i - max_stride, i):
				if res[j] == 1 and s[j:i] in wordDict:
					res[i] = 1
		if res[-1] == 1:
			return True
		else:
			return False


if __name__ == "__main__":
	s = ["leetcode", "applepenapple", "catsandog"]
	wordDict = [["leet", "code"], ["apple", "pen"], ["cats", "dog", "sand", "and", "cat"]]
	A = [True, True, False]
	solution = Solution()
	for i in range(3):
		if A[i] == solution.wordBreak(s[i], wordDict[i]):
			print('\n', s[i],"+", wordDict[i], "-->", A[i])
			print('AC')