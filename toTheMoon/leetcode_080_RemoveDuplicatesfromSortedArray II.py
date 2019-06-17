# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:57:04 2019

@author: jercas
"""
"""
    leetcode-80: 删除排序数组中的重复项 II MEDIUM
    '数组' '双指针'
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i

if __name__ == "__main__":
    Q1, Q2 = [1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3]
    A11, A12 = 5, 7
    A21, A22 = [1, 1, 2, 2, 3], [0,0,1,1,1,1,2,3,3]
    solution = Solution()
    if A11 == solution.removeDuplicates(Q1):
        print('equal')
        for i in range(A11):
            Q1[i] == A21[i]
            print('match')
    if A12 == solution.removeDuplicates(Q2):
        print('equal')
        for i in range(A12):
            Q2[i] == A22[i]
            print('match')
    print("AC")