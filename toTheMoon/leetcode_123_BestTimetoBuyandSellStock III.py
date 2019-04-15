# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:02:09 2019

@author: jercas
"""
"""
    leetcode-123: 买卖股票的最佳时机 III HARD
    '动态规划' '数组'
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
import sys
import numpy as np
class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        for price in prices:
            first_buy = max(first_buy, -price)  # 第一次买入手上的钱
            first_sell = max(first_sell, price+first_buy)  # 第一次卖出手上的钱
            second_buy = max(second_buy, first_sell-price)  # 第二次买入手上的钱
            second_sell = max(second_sell, price+second_buy)  # 第二次卖出手上的钱
            #print(first_buy, first_sell, second_buy, second_sell)
        return second_sell
    
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        left, right = np.zeros(len(prices)), np.zeros(len(prices))
        min_price, max_price = prices[0], prices[-1]
        
        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i]-min_price)
            min_price = min(min_price, prices[i])
            
        for j in range(len(prices)-2, -1, -1):
            right[j] = max(right[j+1], max_price-prices[j])
            max_price = max(max_price, prices[j])
        #print(left, right)
        res = [left[k]+right[k] for k in range(len(prices))]
        return max(res)

    
    
if __name__ == "__main__":
    Q1,Q2,Q3 = [3,3,5,0,0,3,1,4], [1,2,3,4,5], [7,6,4,3,1]
    A1,A2,A3 = 6, 4, 0 
    solution = Solution()
    if A1 == solution.maxProfit1(Q1) and A2 == solution.maxProfit1(Q2) and A3 == solution.maxProfit1(Q3):
        if A1 == solution.maxProfit2(Q1) and A2 == solution.maxProfit2(Q2) and A3 == solution.maxProfit2(Q3):
            print("AC")
        