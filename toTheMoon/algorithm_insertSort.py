# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:36:48 2019

@author: jercas
"""
"""基础排序算法：插入排序"""
def insert_sort(list):
	n = len(list)
	for i in range(1, n):
		key = list[i]
		prev = i - 1
		while prev >= 0:
			if list[prev] > key:
				list[prev + 1] = list[prev]
				list[prev] = key
			prev -= 1
	return list


list = [3, 4, 2, 8, 9, 5, 1]
print("排序前序列 -> ", list)
print("排序后序列 -> ", insert_sort(list))