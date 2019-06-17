# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:43:42 2019

@author: jercas
"""
"""
	leetcode-17: 电话号码的字母组合 MEDIUM
	'字符串' '回溯算法'
	给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
	给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
	Tips：
		尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
"""
	Thinking:
		1. 回溯是一种通过穷举所有可能情况来找到所有解的算法。
		如果一个候选解最后被发现并不是可行解，回溯算法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解。
		给出如下回溯函数 backtrack(combination, next_digits) ，它将一个目前已经产生的组合 combination 和接下来准备要输入的数字 next_digits 作为参数。
		如果没有更多的数字需要被输入，那意味着当前的组合已经产生好了。 
		如果还有数字需要被输入： 遍历下一个数字所对应的所有映射的字母。 
		将当前的字母添加到组合最后，也就是 combination = combination + letter。 
		重复这个过程，输入剩下的数字： backtrack(combination + letter, next_digits[1:])。
		
		2. 非递归暴力三循环
"""
class Solution(object):
	num2char = {'2': ['a', 'b', 'c'],
	            '3': ['d', 'e', 'f'],
	            '4': ['g', 'h', 'i'],
	            '5': ['j', 'k', 'l'],
	            '6': ['m', 'n', 'o'],
	            '7': ['p', 'q', 'r', 's'],
	            '8': ['t', 'u', 'v'],
	            '9': ['w', 'x', 'y', 'z']}
	def letterCombinations1(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		时间复杂度：O(3^n * 4^m)，回溯算法，20ms beaten 92.24%
		空间复杂度：O(3^n * 4^m)，数组保存返回结果，11.7MB beaten 30.54%
		"""
		def backtrack(combination, next_digits):
			# if there is no more digits to check
			if len(next_digits) == 0:
				# the combination is done
				res.append(combination)

			# if there are still digits to check
			else:
				# iterate over all letters which map the next available digit
				for letter in self.num2char[next_digits[0]]:
					# append the current letter to the combination and proceed to the next digits
					backtrack(combination + letter, next_digits[1:])

		res = []
		if digits:
			backtrack("", digits)
		return res


	def letterCombinations2(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		时间复杂度：O(3^n)，回溯算法，20ms beaten 92.24%
		空间复杂度：O(3^n * 4^m)，数组保存返回结果，11.7MB beaten 33.46%
		"""
		if not digits:
			return []
		res = [""]
		for num in digits:
			next_res = []
			for alp in self.num2char[num]:
				for tmp in res:
					next_res.append(tmp + alp)
			res = next_res
		return res


if __name__ == '__main__':
	Q = '23'
	A1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
	A2 = ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
	solution = Solution()
	if solution.letterCombinations1(Q) == A1 and solution.letterCombinations2(Q) == A2:
		print("Input: {0}; Output: {1}".format(Q, A1))
	print('AC')