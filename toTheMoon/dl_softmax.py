# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:51:28 2019

@author: jercas
"""
import numpy as np
import math
def softmax1(inMatrix):
    m,n = np.shape(inMatrix)
    outMatrix = np.mat(np.zeros((m,n)))
    soft_sum = 0
    
    for idx in range(0,n):
        outMatrix[0,idx] = math.exp(inMatrix[0,idx])
        soft_sum += outMatrix[0,idx]
    for idx in range(0,n):
        outMatrix[0,idx] = outMatrix[0,idx] / soft_sum
    return outMatrix


def softmax2(x, axis=1):
    row_max = x.max(axis=axis)  # 计算每行的最大值
    row_max=row_max.reshape(-1, 1)
    x = x - row_max  # 每行元素都需要减去对应的最大值，否则求exp(x)会溢出，导致inf情况
 
    x_exp = np.exp(x)  # 计算e的指数次幂
    x_sum = np.sum(x_exp, axis=axis, keepdims=True) 
    s = x_exp / x_sum
    return s

a = np.array([[1, 2, 1, 2, 1, 1, 3]])
print(softmax1(a))
print('\n')
print(softmax2(a))