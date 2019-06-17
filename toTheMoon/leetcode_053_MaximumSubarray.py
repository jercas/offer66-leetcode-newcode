# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:49:37 2019

@author: jercas
"""
"""
    leetcode-53: 最大子序和 EASY
    '数组' '动态规划' '分治算法'
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），
    返回其最大和。
"""
"""
    Thinking:
        1.动态规划法：定义最大子序和 与 当前累积和，遍历列表当前数为正值时累加，否则清空累积和设置为当前值，每次按是否大于最大子序和进行更新。
        2.分治算法： 遍历数组，当前值i-1>0时，将以累积和替代自身 -> 即将i-1和i值相加替代i位置，遍历一轮后，数组中最大值即为最大子序和。
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
        # 动态规划, 在自身位置以累积和替代，原数组上操作（对i，当i-1为正值时，nums[i]+nums[i-1]累积和必然上升，
        #                                           此时以该累积和替换nums[i]，套用动态规划思想 -- 记下历史记录）
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
    
    def maxSubArray2(self, nums: 'List[int]') -> int:
        if len(nums) <=0 :
            return 0
        # 动态规划，以变量记录累积和变化 和 最大值
        maxV = nums[0]
        benefited = 0
        for num in nums:
            benefited = max(num, num + benefited) # 记录累积和，当i + i-1 累积和超过 i 本身时，为正向累积和-》记录下来（-1+4=3>-1 正向累积记录， -2+4=2<4 负向累积不记录）
            maxV = max(maxV, benefited)           # 新累积和 超过 当前最大值时， 替换
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
