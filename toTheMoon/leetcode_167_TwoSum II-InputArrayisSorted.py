# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:32:35 2019

@author: jercas
"""
"""
    leetcode-167: 两数之和 II - 输入有序数组 EASY
    '数组' '双指针' '二分查找' '哈希表'
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    
    Hint:
        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
""" 
class Solution(object):
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for ind, val in enumerate(numbers):
            another_num = target - val
            if another_num in d:
                return [d[another_num]+1, ind+1]
            d[val]=ind
            
            
    def twoSum2(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
    
    
if __name__ == "__main__":
    Q1 = [[2, 7, 11, 15], [5, 25, 75]]
    Q2 = [9, 100]
    A = [[1, 2], [2, 3]]
    solution = Solution()
    for i in range(2):
        if solution.twoSum1(Q1[i], Q2[i]) == A[i] and solution.twoSum2(Q1[i], Q2[i]) == A[i]:
            print("{0} -> sum to {1} where two sum located in {2}{3}".format(
                    Q1[i], Q2[i], A[i][0], A[i][1]))
            print("AC")

