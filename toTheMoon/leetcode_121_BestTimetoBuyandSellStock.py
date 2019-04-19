# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:14:58 2019

@author: jercas
"""
"""
	leetcode-121: 买卖股票的最佳时机 EASY 
	'动态规划' '数组'
	给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
	如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
	注意你不能在买入股票前卖出股票。
"""
import sys
class Solution:
	def maxProfit1(self, prices: 'List[int]') -> int:
		n = len(prices)
		if n <= 0:
			return 0

		profit = 0
		minPrice = prices[0]
		for i in range(1, n):
			profit = max(profit, prices[i] - minPrice)
			if prices[i] < minPrice:
				minPrice = prices[i]
		return profit

	def maxProfit2(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		minPrice = sys.maxsize
		profit = 0
		for price in prices:
			profit = max(profit, price - minPrice)
			minPrice = min(minPrice, price)
		return profit


if __name__ == "__main__":
	Q = [[7,1,5,3,6,4], [7,6,4,3,1]]
	A = [5, 0]
	solution = Solution()
	for i in range(2):
		if solution.maxProfit1(Q[i]) == A[i] and solution.maxProfit2(Q[i]) == A[i]:
			print("{0} ==> Max Profit:{1}".format(Q[i],A[i]))
			print("AC")