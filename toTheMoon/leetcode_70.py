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
    def climbStairs(self, n: int) -> int:
        ways = [1, 1]
        if n < 2:
            return ways[n]
        else:
            for i in range(2, n+1):
                tmp = ways[0] + ways[1]
                ways[0] = ways[1]
                ways[1] = tmp
            return ways[1]
        

if __name__ == "__main__":
    Q1,Q2 = 2, 4
    A1, A2 = 2, 5
    solution = Solution()
    if solution.climbStairs(Q1) == A1 and solution.climbStairs(Q2) == A2:
        print('AC')