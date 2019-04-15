# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:00:22 2019

@author: jercas
"""
"""
    leetcode-509: 斐波那契数列 EASY
    '动态规划' '数组'
    斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，
    后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
"""
class Solution:
    def fib(self, N: int) -> int:
        fib = [0, 1]
        if N < 2:
            return fib[N]
        else:
            for i in range(2, N+1):
                tmp = fib[0] + fib[1]
                fib[0] = fib[1]
                fib[1] = tmp
        return fib[1]
    
    
if __name__ == "__main__":
    Q1,Q2 = 2, 5
    A1, A2 = 1, 5
    solution = Solution()
    if solution.fib(Q1) == A1 and solution.fib(Q2) == A2:
        print('AC')