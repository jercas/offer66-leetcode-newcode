# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:47:02 2019

@author: jercas
"""
"""
    leetcode-1: 两数之和 EASY
    '数组' '哈希表'
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
    

if __name__ == "__main__":
    Q1,Q2 = [2, 7, 11, 15], 9
    A = [0, 1]
    solution = Solution()
    if solution.twoSum(Q1, Q2) == A:
        print('AC')