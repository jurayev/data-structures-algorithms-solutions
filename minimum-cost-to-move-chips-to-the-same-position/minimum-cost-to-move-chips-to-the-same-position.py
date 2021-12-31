class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        TC O(n)
        SC O(1)
        
        Examples:
        [1,2,3]
         odds = 2
         evens = 1
         
        [2,2,2,3,3,4,4,6,6,6,10,13]
         odds = 3
         evens = 9
        
        Approach: Count odds and evens, the smaller gives us the min cost
        """
        cost_odds = 0
        cost_evens = 0
        for pos in position:
            cost_odds += pos & 1 == 1
            cost_evens += pos & 1 == 0
         
        return min(cost_odds, cost_evens)