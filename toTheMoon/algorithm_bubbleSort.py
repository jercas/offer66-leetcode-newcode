# -*- coding: utf-8 -*-
def bubble_sort(data):
    n = len(data) - 1
    for i in range(n):
        for j in range(n - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
 
 
if __name__ == '__main__':
    array = [3, 4, 2, 8, 9, 5, 1, 8]
    print("排序前序列 -> ", array)
    print("排序后序列 -> ", bubble_sort(array))
