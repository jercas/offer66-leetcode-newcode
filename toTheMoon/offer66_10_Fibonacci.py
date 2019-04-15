# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:40:14 2019

@author: jercas
"""
"""
    offer66-10
    ‘动态规划’
    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项
    （从0开始，第0项为0）
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        fib = [a ,b]
        if n <= 1:
            return fib[n]
        for i in range(2, n+1):
            fib.append(a + b)
            a = fib[-2]
            b = fib[-1]
        return fib[-1]
    
if __name__ == "__main__":
    Q = [1,2,3,4,5]
    A = [1,1,2,3,5]
    solution = Solution()
    for i in range(len(Q)):
        if A[i] == solution.Fibonacci(Q[i]):
            print(Q[i],"==>",solution.Fibonacci(Q[i]))
    print("AC")