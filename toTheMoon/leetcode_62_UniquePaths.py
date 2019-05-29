# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:19:03 2019

@author: jercas
"""
"""
	leetcode-62: 不同路径 MEDIUM
	一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
	机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
	问总共有多少条不同的路径？
	Tips: m 和 n 的值均不超过 100。
"""
"""
	Thinking:
		1: 动态规划法：标准的动态规划题目，首先找状态转移公式：
		dp存储当前点位共有多少种走法，(i,j)格子的走法共为其左边和上方相邻格子的走法之和 --> dp[i][j]=dp[i][j-1] + dp[i-1][j]。
		2：排列组合法：到达目的地一定且一共会走m+n-2步，则从m+n-2步中挑出m-1步向下走即可 --> C(m+n-2, min(m-1, n-1))
		3: 递归法：原理上行得通，编译器可行但提交leetcode超时.
"""
class Solution(object):
	def uniquePaths1(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		时间复杂度：O(m*n)，遍历整个二维数组，12ms beaten 99.79%
		空间复杂度：O(m*n)，创建状态数组dp大小等同于二维路径数组，11.7MB beaten 41.04%
		"""
		if not m or not n:
			return 0

		# 创建状态数组dp，并以全1初始化，因为第一行和第一列的走法一定唯一，即0行dp[0][~]和0列d[~][0]值为1.
		dp = [[1] * m for _ in range(n)]
		# 遍历数组，更新状态/步数数组dp
		for i in range(1, n):
			for j in range(1, m):
				dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
		return dp[-1][-1]


	def uniquePaths2(self, m, n):
		"""
			:type m: int
			:type n: int
			:rtype: int
			时间复杂度：O(m*n)，遍历整个二维数组，12ms beaten 99.79%
			空间复杂度：O(1)，未使用额外空间，11.5MB beaten 45.55%
		"""
		# N = m+n-2
		# M = m-1 if m<n else n-1
		# 计算C(N, M)==C(m+n-2, min(m-1, n-1)) 排列组合

		if not m or not n:
			return 0
		k = min(m-1, n-1)
		return self.combination(m + n - 2, k)


	def combination(self, n, m):
		"""
		计算组合C(n, m)
		"""
		return self.factorial(n) // self.factorial(m) // self.factorial(n - m)


	def factorial(self, n):
		"""
		计算阶乘
		"""
		c = 1
		for i in range(1, n + 1):
			c = c * i
		return c


	def uniquePaths3(self, m, n):
		"""
			:type m: int
			:type n: int
			:rtype: int
			时间复杂度：O(m*n)，
			空间复杂度：O(m*n)，
		"""
		if m==1 or n==1:
			return 1
		return self.uniquePaths3(m, n-1) + self.uniquePaths3(m-1, n)


if __name__ == "__main__":
	Q = [[3, 2], [7, 3]]
	A = [3, 28]
	solution = Solution()
	for i in range(2):
		if solution.uniquePaths1(Q[i][0], Q[i][1]) == A[i] and solution.uniquePaths2(Q[i][0], Q[i][1]) == A[i] and solution.uniquePaths3(Q[i][0], Q[i][1]) == A[i]:
			print('The paths through the matrix {0} is {1}'.format(Q[i], A[i]))
	print('AC')