# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:54:53 2019

@author: jercas
"""
"""
    leetcode-217: 存在重复元素 EASY
    '数组' '哈希表'
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

    PS： 不同于287寻找重复数，217中会出现负数，不可以用值匹配下标调换顺序的算法去解决，出现越界情况
"""
class Solution:
    def containsDuplicate1(self, nums):
        if len(set(nums)) < len(nums):
            return True
        return False
    
    def containsDuplicate2(self, nums):
        if len(nums) <2:
            return False
        
        hashT = {}
        for ind, val in enumerate(nums):
            if val in hashT:
                return True
            hashT[val] = ind
        return False
        
        
if __name__ == "__main__":
    Q1, Q2 = [1,2,3,1], [1,2,3,4]
    A1, A2 = True, False
    solution = Solution()
    
    if A1 == solution.containsDuplicate1(Q1) and A2 == solution.containsDuplicate2(Q2):
        print(Q1,'==>',A1)
        print(Q2,'==>',A2)
        print("AC")