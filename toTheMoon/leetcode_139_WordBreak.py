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
		
	Hint:
		（1）设dp[i]表示字符串s[0:i]是否可以被拆分，False 不能，True能。
		（2）现在要想求dp[i]的值，很显然只要判断dp[i - k]的值和子串s[i - k: i]是否存在wordDict中，
			其中k为wordDict中一个单词的长度，所以在这一块，可以遍历所有的单词来求。
		（3）可以先求出wordDict中每个长度，并且给它排序，方便后面的计算。
"""


class Solution(object):
	def wordBreak1(self, s, wordDict):
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

	def wordBreak2(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		words = set(wordDict)
		lengths = sorted({len(w) for w in words})

		dp = [False] * (len(s) + 1)
		dp[0] = True

		for i in range(1, len(s) + 1):
			for k in lengths:
				if not dp[i] and i - k >= 0:
					dp[i] = (dp[i - k] and s[i - k: i] in words)
					#print(i, dp[i])
		#print(dp)
		return dp[-1]


if __name__ == "__main__":
	s = ["leetcode", "applepenapple", "catsandog", "cars"]
	wordDict = [["leet", "code"], ["apple", "pen"], ["cats", "dog", "sand", "and", "cat"], ["car", "ca", "rs"]]
	A = [True, True, False, True]
	solution = Solution()
	for i in range(4):
		if A[i] == solution.wordBreak2(s[i], wordDict[i]):
			print(s[i],"+", wordDict[i], "-->", A[i])
			print('AC')