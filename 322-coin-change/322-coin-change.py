class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [1,2,5] amount = 11
         j
        [0,1,2,3,4,5,6,7,8,9,10,11]
        [0,1,1,2,2,1,6,7,8,9,10,11]
           i
 
        State [j]
        Value function -> min_coins[i] min coins to get this amount
        Initial states: -> min_coins[0..n-1] = 0
        Transition function -> min_coins[i] = min(min_coins[i], min_coins[i - coin_value] + 1)
        Order -> 0 ... n-1
        Answer -> min_coins[n-1]
        
        Time O(N*M)
        Space O(N)
        """
        n = amount + 1
        m = len(coins)
        min_coins = [float(inf) for i in range(n)]
        min_coins[0] = 0
        for i in range(0, n):
            for j in range(m):
                if coins[j] <= i:
                    min_coins[i] = min(min_coins[i], min_coins[i - coins[j]] + 1)     
        return min_coins[n-1] if min_coins[n-1] < float(inf) else -1