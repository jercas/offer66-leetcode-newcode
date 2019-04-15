# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:43:36 2019

@author: jercas
"""
"""
    leetcode-26: 删除排序数组中的重复项 EASY
    '数组' '双指针'
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
class Solution:
    def removeDuplicates1(self, nums: 'List[int]') -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        result = list(set(nums))
        result.sort()

        for i, v in enumerate(result):
            nums[i] = result[i]
        return len(result)
    
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        for n in nums:
            if i<1 or n != nums[i-1]:
                nums[i] = n
                i += 1
        return i
    
if __name__ == "__main__":
    Q1, Q2 = [1,1,2], [0,0,1,1,1,2,2,3,3,4]
    A11, A12 = 2,5
    A21, A22 = [1, 2], [0,1,2,3,4]
    
    solution = Solution()
    if A11 == solution.removeDuplicates1(Q1):
        print('equal')
        for i in range(A11):
            Q1[i] == A21[i]
            print('match')
    if A12 == solution.removeDuplicates1(Q2):
        print('equal')
        for i in range(A12):
            Q2[i] == A22[i]
            print('match')
    if A11 == solution.removeDuplicates2(Q1):
        print('equal')
        for i in range(A11):
            Q1[i] == A21[i]
            print('match')
    if A12 == solution.removeDuplicates2(Q2):
        print('equal')
        for i in range(A12):
            Q2[i] == A22[i]
            print('match')
    print("AC")