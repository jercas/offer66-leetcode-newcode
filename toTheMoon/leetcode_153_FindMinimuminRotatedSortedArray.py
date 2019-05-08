# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:22:37 2019

@author: jercas
"""
"""
    leetcode_153: 寻找旋转排序数组中的最小值 MEDIUM
    '数组' '二分查找'
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
"""
class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        #return min(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


if __name__ == "__main__":
    Q = [[3,4,5,1,2], [4,5,6,7,0,1,2]]
    A = [1, 0]
    solution = Solution()
    for i in range(2):
        if solution.findMin(Q[i]) == A[i]:
            print("the minimum of {0} is -> {1}".format(Q[i], A[i]))
            print("AC")