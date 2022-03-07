class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
         0 1 2 3 4 5 6 7
        [3,3,5,0,0,3,1,4] k = 2 ans = 6
           i j
                 i     j
                 i j
                     i
                       j
           buy  sell
        1. 3     5
        2. 3     5
        
            0  1   2 3 4 5 6 7
         b  3  3   3 0 0 3 1 4
         s  0  0   2 0 0 3 3 3
         
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
            
            