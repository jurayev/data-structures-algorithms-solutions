class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf") # 7, 1
        profit = 0 # 4
        
        for price in prices:
            sell = price - buy
            profit = max(profit, sell)
            buy = min(buy, price)
            
        return profit