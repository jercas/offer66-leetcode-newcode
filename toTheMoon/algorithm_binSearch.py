# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:31:08 2019

@author: jercas
"""
"""基础查找算法：二分查找"""
def bin_search(data_list, val):    
    low = 0                         # 最小数下标    
    high = len(data_list) - 1       # 最大数下标    
    while low <= high:        
        mid = (low + high) // 2     # 中间数下标        
        if data_list[mid] == val:   # 如果中间数下标等于val, 返回            
            return mid        
        elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标            
            high = mid - 1        
        else:                       # 如果val在中间数右边, 移动low下标            
            low = mid + 1    
    return # val不存在, 返回None

if __name__ == '__main__':
    print(bin_search(list(range(1, 10)), 3))