# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:31:08 2019

@author: jercas
"""
"""基础排序算法：选择排序"""
def select_sort(list):
	n = len(list)
	for i in range(n):
		min = i
		for j in range(i+1, n):
			if list[j] < list[min]:
				min = j
		tmp = list[min]
		list[min] = list[i]
		list[i] = tmp
	return list


list = [3, 4, 2, 8, 9, 5, 1]
print("排序前序列 -> ", list)
print("排序后序列 -> ", select_sort(list))