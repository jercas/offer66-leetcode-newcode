# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:45:24 2019

@author: jercas
"""
"""
	leetcode-88: 合并两个有序数组 EASY
	'数组' '双指针'
	给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

    Hint:
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
"""


class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i , j, length = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums2[j] > nums1[i]:
                nums1[length] = nums2[j]
                length -=1
                j -=1
            else:
                nums1[length] = nums1[i]
                length -=1
                i -=1
        while j >= 0:
            nums1[length] = nums2[j]
            length -=1
            j -= 1
            

if __name__ == "__main__":
    Q1, Q2 = [[1,2,3,0,0,0], [2,5,6]], [3, 3]
    A = [1,2,2,3,5,6]
    solution = Solution()
    solution.merge(Q1[0], Q2[0], Q1[1], Q2[1])
    if Q1[0] == A:
            print("merge sorted list [1, 2, 3] and [2, 5, 6] --> {0}".format(A))
            print("AC")