class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        trans = 4
        profits = [[0 for i in range(trans+1)] for i in range(n)]
        for k in range(1, trans+1):
            profits[0][k] = -prices[0] if k % 2 == 1 else 0
        for i in range(1, n):
            for k in range(1, trans+1):
                if k % 2 == 1:
                    # buy
                    profits[i][k] = max(profits[i-1][k], -prices[i] + profits[i-1][k-1])
                else:
                    # sell
                    profits[i][k] = max(profits[i-1][k], prices[i] + profits[i-1][k-1])
                    
        return profits[n-1][k]
    
    def maxProfit1(self, prices: List[int]) -> int:
        """
         0 1 2 3 4 5 6 7
        [3,3,5,0,0,3,1,4] k = 2 ans = 6
           i j
                 i     j
                 i j
                     i
                       j
          0 1  2  3 4
          0 0  0  0 0
        3 0 -3 0 -3 0
        4 0 -3 1 -3 1
        5 0 -5 2 -5 2
          0 0  0  0 0
         
         4 3 2 1 0
         b s b s
         compute suffixes
         for i in range(n)
         dp(i, k) = max(dp(i, k), dp(i+1, k), dp(i+1, k-1))
         
         base cases:
            if i >= len:
                return 0
            if k == 0:
                return 0
                
        Time O(N)
        Space O(N)
        """
        @lru_cache
        def get_max_profit(i, k):
            if i >= len(prices):
                return 0
            if k == 0:
                return 0
            
            # buy or sell, 4 transactions
            can_buy = k % 2 == 0
            # hold
            profit = get_max_profit(i+1, k)
            if can_buy:
                # buy
                profit = max(profit, -prices[i] + get_max_profit(i+1, k-1))
            else:
                # sell
                profit = max(profit, prices[i] + get_max_profit(i+1, k-1))
            return profit
        
        return get_max_profit(0, 4)
            
            