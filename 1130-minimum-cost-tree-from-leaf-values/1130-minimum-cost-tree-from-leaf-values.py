class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        
           [6,2,4]
            l
                r
              k
        [12,24]   [24, 8]
        
        [36]      [32]
        
        
        [6,2,4,1]
         l     r
             k
        [12,24, 6] [8]
            
          24       
      6      8
         2      4       1
        """
        @lru_cache(None)
        def cost(left, right):
            if left+1 >= right:
                return 0
            min_cost = float(inf)
            for k in range(left+1, right): # 1
                leaf_costs = max(arr[left:k]) * max(arr[k:right]) # 6, 4
                non_leaf_costs = cost(left, k) + cost(k, right)   # 0, 1 | 1, 2
                min_cost = min(min_cost, leaf_costs + non_leaf_costs)
            return min_cost
        
        return cost(0, len(arr))
                