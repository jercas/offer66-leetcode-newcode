# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:36:48 2019

@author: jercas
"""
"""基础排序算法：插入排序"""
def insert_sort(data):
	n = len(data)
	"""
	for i in range(1, n):
		tmp = data[i]
		prev = i - 1
		while prev >= 0:
			if data[prev] > tmp:
				data[prev + 1] = data[prev]
				data[prev] = tmp
			prev -= 1
	"""
	for i in range(1, n):
		while i>0 and data[i-1] > data[i]:
			data[i], data[i-1] = data[i-1], data[i]
			i -= 1
	return data

if __name__ == '__main__':
	list1 = [3, 4, 2, 8, 9, 5, 1]
	list2 = [1, 2, 3, 2, 5, 6]
	print("排序前序列 -> ", list1, list2)
	print("排序后序列 -> ", insert_sort(list1), insert_sort(list2))