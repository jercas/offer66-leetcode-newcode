# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:31:08 2019

@author: jercas
"""
"""
基础排序算法：快速排序
最优情况：待排序列升序有序O(n)，即，1  2  3  4  5  6  7，基准选择第一个数，调整次数最少，注意只是调试次数减少，比较次数没变少。
最差情况：待排序序列降序有序O(n2)，即，7  6  5  4  3  2  1，这种情况就退化为冒泡排序。
"""
def quick_sort1(data):
    """快速排序"""    
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[0]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort1(left) + [mid] + quick_sort1(right)
    else:        
        return data


def quick_sort2(data, left, right):
    """快速排序"""
    # 如果start和end碰头了，说明要我排的这个子数列就剩下一个数了，就不用排序了
    if not left < right:
        return

    mid = data[left]  # 拿出第一个数当作基准数mid
    low = left  # low来标记左侧从基准数始找比mid大的数的位置
    high = right  # high来标记右侧end向左找比mid小的数的位置


    # 循环，只要low和high没有碰头就一直进行,当low和high相等说明碰头了
    while low < high:
        # 从high开始向左，找到第一个比mid小或者等于mid的数，标记位置,（如果high的数比mid大，我们就左移high）
        # 并且要确定找到之前，如果low和high碰头了，也不找了
        while low < high and data[high] > mid:
            high -= 1
        # 跳出while后，high所在的下标就是找到的右侧比mid小的数
        # 把找到的数放到左侧的空位 low 标记了这个空位
        data[low] = data[high]
        # 从low开始向右，找到第一个比mid大的数，标记位置,（如果low的数小于等于mid，我们就右移low）
        # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and data[low] <= mid:
            low += 1
        # 跳出while循环后low所在的下标就是左侧比mid大的数所在位置
        # 我们把找到的数放在右侧空位上，high标记了这个空位
        data[high] = data[low]

        # 以上我们完成了一次 从右侧找到一个小数移到左侧，从左侧找到一个大数移动到右侧

    # 当这个while跳出来之后相当于low和high碰头了，我们把mid所在位置放在这个空位
    data[low] = mid
    # 这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大
    # 然后我们对mid左侧所有数进行上述的排序
    quick_sort2(data, left, low - 1)
    # 我们mid右侧所有数进行上述排序
    quick_sort2(data, low + 1, right)

 
if __name__ == '__main__':
    array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    q1, q2 = array.copy(), array.copy()
    print("排序前序列 -> ", array)
    print("排序后序列 -> ", quick_sort1(q1), '\n', quick_sort2(q2, 0, len(array)-1), q2)