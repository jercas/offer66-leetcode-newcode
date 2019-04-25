# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:02:55 2019

@author: jercas
"""
"""
    leetcode-70: 爬楼梯 EASY
    ‘动态规划’
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。
"""
class Solution:
    def climbStairs1(self, n: int) -> int:
        ways = [1, 1]
        if n < 2:
            return ways[n]
        else:
            for i in range(2, n+1):
                tmp = ways[0] + ways[1]
                ways[0] = ways[1]
                ways[1] = tmp
            return ways[1]

    def climbStairs2(self, n: int) -> int:
        ways = [1, 1]
        for i in range(1, n):
            ways.append(ways[i] + ways[i-1])
        """
        for i in range(2, n+1):
            ways.append(ways[-2] + ways[-1])
        """
        return ways[-1]
        

if __name__ == "__main__":
    Q = [2, 4]
    A = [2, 5]
    solution = Solution()
    for i in range(2):
        if solution.climbStairs1(Q[i]) == A[i] and solution.climbStairs2(Q[i]) == A[i]:
            print('AC')