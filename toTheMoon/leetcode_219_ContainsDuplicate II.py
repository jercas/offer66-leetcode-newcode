# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:22:48 2019

@author: jercas
"""
"""
    leetcode-219: 存在重复元素 II EASY
    '数组' '哈希表'
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
    使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) < 2:
            return False
        
        hashT = {}
        for ind, val in enumerate(nums):
            if val in hashT:
                if abs(ind - hashT[val]) <= k:
                    return True
            hashT[val] = ind  
        return False
    
if __name__ == "__main__":
    Q11, Q12, Q13 = [1,2,3,1], [1,0,1,1], [1,2,3,1,2,3]
    Q21, Q22, Q23 = 3,1,2
    A1, A2, A3 = True, True, False
    solution = Solution()
    
    if A1 == solution.containsNearbyDuplicate(Q11, Q21) and A2 == solution.containsNearbyDuplicate(Q12, Q22) and A3 == solution.containsNearbyDuplicate(Q13, Q23):
        print(Q11,Q21,'==>',A1)
        print(Q12,Q22,'==>',A2)
        print(Q13,Q23,'==>',A3)
        print("AC")