# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Easy
# O(n) time, O(1) space

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left = right 
        
        return max_profit