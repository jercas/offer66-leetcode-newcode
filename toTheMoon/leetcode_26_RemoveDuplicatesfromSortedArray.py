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
"""
	Thinking:
		0. 偷鸡解法：使用Py中set不含重复元素的特点，对输入数组进行去重，因set后原有序数组会乱序，故需要重新排序，然后覆盖原数组即可
				但使用了额外空间，不符合题意，不可行
		1. 双指针维护不重复有序子集：以指针i来维护其前面的所有元素均是不重复的有序子数组；遍历数组判断条件为：当i元素 != i-1元素时，说明未重复，
				此时将i位置的元素值，赋给i下标更新不重复有序子数组，对于重复元素跳过不处理，遍历一遍后，直接返回i为移除重复元素的新长度，对原数组
				其[0:i+1]切片，即为处理后新的不重复有序数组。
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
            nums[i] = v
        return len(result)
    
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间复杂度：O(n) 遍历一次原数组, 76ms beaten 99.91%
        空间复杂度：O(1) 未使用额外空间，在原数组上操作，13.5MB beaten 30.58%
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