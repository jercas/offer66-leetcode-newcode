# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:30:48 2019

@author: jercas
"""
"""
    leetcode-287: 寻找重复数 MEDIUM
    '数组' '双指针' '二分查找' '按顺序大小位置重排序'
    给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
    可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数
"""
class Solution:
    def findDuplicate1(self, nums):
        for i in range(len(nums)):
            while(nums[i] != i):
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i] = nums[tmp]
                    nums[tmp] = tmp
                    
    def findDuplicate2(self, nums):             
        if len(nums) <2:
            return False
        
        hashT = {}
        for ind, val in enumerate(nums):
            if val in hashT:
                return val
            hashT[val] = ind
        return -1

if __name__ == "__main__":
    Q = [1,3,4,2,2]
    A = 2
    solution = Solution()
    if A == solution.findDuplicate1(Q.copy()) and A == solution.findDuplicate2(Q.copy()):
        print(Q,'==>',A)
        print("AC")