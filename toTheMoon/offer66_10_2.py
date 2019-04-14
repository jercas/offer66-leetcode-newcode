# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:47:32 2019

@author: jercas
"""
"""
    offer66-10.2
    ‘动态规划’
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
    （先后次序不同算不同的结果）
"""
class Solution:
    def jumpFloor(self, n):
        fib = [1 ,1]
        if n <= 1:
            return fib[n]
        for i in range(2, n+1):
            t = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = t
        return fib[1]
    
    
if __name__ == "__main__":
    Q = 5
    A = 8
    solution = Solution()
    if A == solution.jumpFloor(Q):
        print("AC")