class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        [1,100,1,1,1,100,1,1,100,1]
         6,100,5,5,4,102,3,2,100,1
        
        """
        cache = {}
        step1 = self.recurse(cost, 0, cache)
        step2 = self.recurse(cost, 1, cache)
        return min(step1, step2)
    
    def recurse(self, cost, i, cache):
        if i >= len(cost):
            return 0
        if i in cache:
            return cache[i]
        step1 = self.recurse(cost, i+1, cache)
        step2 = self.recurse(cost, i+2, cache)
        cache[i] = min(step1, step2) + cost[i]
        return min(step1, step2) + cost[i]
    
    def minCostClimbingStairsBottomUp(self, cost: List[int]) -> int:
        """
        [1,100,1,1,1,100,1,1,100,1]
         1,100,2,2,3,102,4,5,104,6
        
        """
        
        curr_cost = cost[:]
        
        for i in range(2, len(cost)):
            curr_cost[i] += min(curr_cost[i-1], curr_cost[i-2])
            
        return min(curr_cost[-1], curr_cost[-2])
    
    