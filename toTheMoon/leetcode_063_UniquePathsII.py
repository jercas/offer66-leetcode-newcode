# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:36:33 2019

@author: jercas
"""
"""
	leetcode-63: 不同路径 II MEDIUM
	'数组' '动态规划'
	一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
	机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
	现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
	Tips: 网格中的障碍物和空位置分别用 1 和 0 来表示。
		  m 和 n 的值均不超过 100。
"""
"""
	Thinking：
		1.动态规划法：同理考虑在No.62的基础上的变体，状态转移公式同62题，但需要加些额外判断：
			(0) 若[0][0]即为1，说明起点就是堵死的，直接返回0即可；
			(1) 在第一行[0][~]和第一列[~][0]中，当为0时，状态转移为dp[0][~] = dp[0][~-1]将前面/上面位置替换本位置，切记不可相加，否则在[[0]]的情况下，shape=(1,1)会计算两遍，返回2的错误值！
											当为1时，死路置为0，以便不影响下面的状态转移计算；
											以上都是在No.62中 dp = [[1]*m for _ in range(n)]上因为多了障碍后的复杂初始化变化，
			(2) 在其他正常位置的，状态转移同Np.62，遇1死路置为0，遇0通路状态转移obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
			(3) 最后返回终点值dp[-1][-1]即可
"""
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		时间复杂度：O(m*n)，遍历阵大小m*n，32ms beaten 100.100%
		空间复杂度：O(1)，未使用额外空间，输入矩阵直接作为dp数组，11.7MB beaten 46.30%
		"""
		# (1)
		if obstacleGrid[0][0] == 1:
			return 0
		obstacleGrid[0][0] = 1

		for i in range(len(obstacleGrid)):
			for j in range(len(obstacleGrid[0])):
				if i == 0 and j == 0:
					continue

				if obstacleGrid[i][j] == 1:
					obstacleGrid[i][j] = 0

				else:
					# (2)
					if i == 0:
						obstacleGrid[i][j] = obstacleGrid[i][j - 1]
					elif j == 0:
						obstacleGrid[i][j] = obstacleGrid[i - 1][j]
					# (3)
					else:
						obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
		# (4)
		return obstacleGrid[-1][-1]


if __name__ == '__main__':
	Q = [
		[0,0,0],
		[0,1,0],
		[0,0,0]
	]
	A = 2
	solution = Solution()
	if solution.uniquePathsWithObstacles(Q) == A:
		print('The paths through the matrix {0} is {1}'.format(Q, A))
	print('ac')