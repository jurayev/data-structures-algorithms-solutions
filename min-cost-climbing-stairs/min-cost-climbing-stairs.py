class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        [1,100,1,1,1,100,1,1,100,1]
         1,100,2,2,3,102,4,5,104,6
        
        """
        
        curr_cost = cost[:]
        
        for i in range(2, len(cost)):
            curr_cost[i] += min(curr_cost[i-1], curr_cost[i-2])
            
        return min(curr_cost[-1], curr_cost[-2])