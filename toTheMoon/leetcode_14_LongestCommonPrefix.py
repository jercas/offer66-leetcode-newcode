# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:30:41 2019

@author: jercas
"""
"""
	leetcode-14: 最长公共前缀 EASY
	'字符串'
	编写一个函数来查找字符串数组中的最长公共前缀。
	如果不存在公共前缀，返回空字符串 ""。
"""
"""
	Thinking:
		0.Python特性-字符串排序解法：Python中字符串按照ascII码排序，如sorted(['abb','aba','abac']) -> ['aba','abac','abb'] -> min:aba, max:abb;
								在此基础上，只需要比较最大和最小的字符串的公共前缀即可。
		1.Python特性-zip+set处理：首先zip(*)做解压处理，将strs中各个str拆分为按位置的单个字符组成的tuple，再利用set去重的效果使得如果该字符为
								公共前缀的部分，则该tuple长度必为1，当大于1时说明前缀到此不一致
"""
class Solution(object):
	def longestCommonPrefix1(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		时间复杂度：O(s)，s为公共前缀长度，24ms beaten 99.90%
		空间复杂度：O(1)，未使用任何额外空间，11.8MB beaten 31.06%
		"""
		if not strs:
			return ""
		s1, s2 = min(strs), max(strs)
		for i in range(len(s1)):
			# 当遍历到不相等前缀时，返回截止此位置前的公共前缀
			if s1[i] != s2[i]:
				return s2[:i]
		# 当整体为公共前缀时， 即较短的s1整体为s2的组成部分前缀，直接返回s1
		return s1


	def longestCommonPrefix2(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		时间复杂度：O(s)，s为公共前缀长度，24ms beaten 99.90%
		空间复杂度：O(1)，使用额外数组来保存zip切分后的单个字符数组，12MB beaten 15.72%
		"""
		if not strs:
			return ""
		# 经过zip(*) -> [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
		# 经过map()分别映射到set()去重 -> [{'f'}, {'l'}, {'i', 'o'}, {'g', 'w'}]
		ss = list(map(set, zip(*strs)))
		res = ""
		for i, x in enumerate(ss):
			x = list(x)
			# 长度大于1，说明此位置的字符不一致，即前缀到此不一样
			if len(x) > 1:
				break
			# 前缀相同，记为公共前缀
			res += x[0]
		return res


	def longestCommonPrefix3(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		时间复杂度：O(s)，s为公共前缀长度，28ms beaten 99.52%
		空间复杂度：O(1)，使用额外数组来保存单个字符数组，11.9MB beaten 29.28%
		"""
		if not strs:
			return ''
		length = [len(s) for s in strs]
		res = ''
		for i in range(min(length)):
			# 分别取出strs中每个str的各个位置字符s组成数组
			cur = [s[i] for s in strs]
			# 同理判断长度，为1时说明未含有重复，为公共前缀
			if len(set(cur)) == 1:
				res += cur[0]
			# 有不用前缀字符时，直接跳出，或返回任意字符串的公共前缀
			else:
				return strs[0][:i]
				# break
		return res


if __name__ == "__main__":
	Q = [["flower","flow","flight"], ["dog","racecar","car"], ["aca","cba"]]
	A = ['fl', '', '']
	solution = Solution()
	for i in range(3):
		if solution.longestCommonPrefix1(Q[i]) == A[i] and solution.longestCommonPrefix2(Q[i]) == A[i] \
				and solution.longestCommonPrefix3(Q[i]) == A[i]:
			print("The longest common prefix of {0} is '{1}'".format(Q[i], A[i]))
	print("AC")