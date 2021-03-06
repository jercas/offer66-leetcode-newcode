# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:31:08 2019

@author: jercas
"""
"""基础排序算法：选择排序"""
def select_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            if data[j] <= data[i]:
                data[j], data[i] = data[i], data[j] 
    return data

if __name__ == '__main__':
    array = [3, 4, 2, 8, 9, 5, 1, 8]
    print("排序前序列 -> ", array)
    print("排序后序列 -> ", select_sort(array))