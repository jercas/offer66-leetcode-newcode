# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:37:49 2019

@author: jercas
"""
"""
    leetcode-115: 不同的子序列 HARD
    '动态规划' '字符串'
    给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
    一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
    （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
                  ___ 0
                 |true
        i < j ? -     ____ 1                ____ sum(i-1, j)
                 |___|j==0                 |false
                     |____ S[i] == T[j] ? -
                                           |____ sum(i-1, j) + sum(i-1,j-1)
""" 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dictTimes = {}
        dictChars = {}
        
        for i in range(len(t)):
            if t[i] in dictChars:
                dictChars[t[i]].append(t[:i])
            else:
                dictChars[t[i]] = [t[:i]]
        for i in range(1, len(t)+1):
            dictTimes[t[:i]] = 0
        dictTimes[''] = 1
        
        for char in s:
            if char in dictChars:
                for c in dictChars[char][::-1]:
                    if dictTimes[c] > 0:
                        dictTimes[c+char] += dictTimes[c]
        print(dictChars, '\n',dictTimes)
        return dictTimes[t]
    
    
if __name__ == "__main__":
    S = ["rabbbit", "babgbag"]
    T = ["rabbit", "bag"]
    A = [3, 5]
    solution = Solution()
    for i in range(len(S)):
        if solution.numDistinct(S[i], T[i]) == A[i]:
            print("AC")