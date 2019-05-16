# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:47:52 2019

@author: jercas
"""
"""
	offer66-4
	'二维数组中的查找'
	在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
	每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution:
	# array 二维列表
	def Find(self, target, array):
		# write code here
		if len(array[0]) == 0:
			return False

		n = len(array)
		row, col = 0, n - 1
		while row < n and col >= 0:
			if array[row][col] == target:
				return True
			elif array[row][col] > target:
				col -= 1
			else:
				row += 1
		return False


if __name__ == "__main__":
	Q1, Q2 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], [7, 5, 15, 1, 16, 0]
	A = [True, False, True, True, False, False]
	solution = Solution()
	for i in range(6):
		if solution.Find(Q2[i], Q1) == A[i]:
			print("AC")
	print(solution.Find(16, [[]]))
