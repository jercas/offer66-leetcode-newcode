# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:56:43 2019

@author: jercas
"""
"""
	leetcode-74: 搜索二维矩阵 MEDIUM
	'数组' '动态规划'
	编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
	每行中的整数从左到右递增, 每列中的整数从上到下递增
	每行的第一个整数大于前一行的最后一个整数。
"""
class Solution(object):
	def searchMatrix1(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix or not matrix[0]:
			return False
		rows, cols = len(matrix), len(matrix[0])
		row, col = 0, cols - 1
		while row < rows and col >= 0:
			if matrix[row][col] == target:
				return True
			elif matrix[row][col] > target:
				col -= 1
			else:
				row += 1
		return False

	def searchMatrix2(self, matrix, target):
		if not matrix or not matrix[0]:
			return False
		rows, cols = len(matrix), len(matrix[0])
		for i in range(rows):
			if target in matrix[i]:
				return True
		return False


if __name__ == "__main__":
	Q1, Q2 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], [7, 5, 15, 1, 16, 0]
	A = [True, False, True, True, False, False]
	solution = Solution()
	for i in range(6):
		if solution.searchMatrix1(Q1, Q2[i]) == A[i] and solution.searchMatrix2(Q1, Q2[i]) == A[i]:
			print("AC")
	print(solution.searchMatrix1([[]], 16), solution.searchMatrix1([], 16))