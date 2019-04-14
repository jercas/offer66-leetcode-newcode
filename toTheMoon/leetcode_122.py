# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:51:17 2019

@author: jercas
"""
"""
    leetcode-122: 买卖股票的最佳时机 II EASY
    '贪心算法' '数组'
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if len(prices) <= 0:
            return 0
        
        maxP = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxP = maxP + (prices[i] - prices[i-1])
        return maxP  
    
    
if __name__ == "__main__":
    Q1,Q2,Q3 = [7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]
    A1,A2,A3 = 7, 4, 0
    solution = Solution()
    if solution.maxProfit(Q1) == A1 and solution.maxProfit(Q2) == A2 and solution.maxProfit(Q3) == A3:
        print("{0} ==> Max Profit:{1}".format(Q1,A1))
        print("{0} ==> Max Profit:{1}".format(Q2,A2))
        print("{0} ==> Max Profit:{1}".format(Q3,A3))
        print('AC')