# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:49:37 2019

@author: jercas
"""
"""
    leetcode-53: 最大子序和 EASY
    '数组' '动态规划' '动态规划'
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），
    返回其最大和。
""" 
class Solution:
    def maxSubArray1(self, nums: 'List[int]') -> int:
        if len(nums) <=0 :
            return 0
        # 分治算法
        res = nums[0]
        sumValue = 0
        for num in nums:
            if sumValue > 0:
                sumValue += num
            else:
                sumValue = num
            res = max(res, sumValue)
        return res
    
    def maxSubArray3(self, nums: 'List[int]') -> int:
        if len(nums) <=0 :
            return 0
        # 动态规划, 在自身位置以累积和替代
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
    
    def maxSubArray2(self, nums: 'List[int]') -> int:
        if len(nums) <=0 :
            return 0
        # 动态规划
        maxV = nums[0]
        benefited = 0
        for num in nums:
            benefited = max(num, num + benefited)
            maxV = max(maxV, benefited)
        return maxV
    
    
if __name__ == "__main__":
    Q = [-2,1,-3,4,-1,2,1,-5,4]
    A = 6
    solution = Solution()
    solutions = [solution.maxSubArray1(Q), solution.maxSubArray2(Q),
                 solution.maxSubArray3(Q)]
    for i in range(3):
        if solutions[i] == A:
            print("AC")
