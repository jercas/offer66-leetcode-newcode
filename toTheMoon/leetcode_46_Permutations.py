# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:07:10 2019

@author: jercas
"""
"""
    leetcode-46: 全排列 MEDIUM
    '回溯算法'
    给定一个没有重复数字的序列，返回其所有可能的全排列。
""" 
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0] * len(nums)
        res = []
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
                        
        dfs([])
        return res


if __name__ == "__main__":
    Q = [1, 2, 3]
    A = [[1,2,3],
         [1,3,2],
         [2,1,3],
         [2,3,1],
         [3,1,2],
         [3,2,1]]
    solution = Solution()
    if solution.permute(Q) == A:
            print("AC")