# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:47:00 2019

@author: jercas
"""
"""
    leetcode-33: 搜索旋转排序数组 MEDIUM
    '数组' '二分查找'
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
""" 
class Solution:
    def search1(self, nums: 'List[int]', target: int) -> int:
        #双向暴力搜索
        n = len(nums)
        if n == 0:
            return -1
        for i in range(n):
            if target == nums[i]:
                return i
            elif target == nums[n-i-1]:
                return n-i-1
        return -1
        
        
    def search2(self, nums: 'List[int]', target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pos = l
        
        res = self.BinarySearch(target, nums[:pos])
        if res == -1:
            res = self.BinarySearch(target, nums[pos:])
            if res != -1:
                res += pos
        return res

    
    def BinarySearch(self, t, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == t:
                return m
            elif nums[m] < t:
                l = m + 1
            else:
                r = m - 1
        return -1


if __name__ == "__main__":
    Q1, Q2 = [4,5,6,7,0,1,2], [0, 3]
    A = [4, -1]
    solution = Solution()
    for i in range(2):
        if solution.search1(Q1, Q2[i]) == A[i] and solution.search2(Q1, Q2[i]) == A[i]:
            print("target {0} in list {1} -> pos: {2}".format(Q2[i], Q1, A[i]))
            print("AC")