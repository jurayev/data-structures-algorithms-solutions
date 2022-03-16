class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        days = [1,4,6,7,8,20], costs = [2,7,15]
        
        
        
        Ideas:
        1. Brute Force:
            take cost for 1 day and try to count how many dollars to travel from days[0] to days[n-1]
        using 1 day-pass -> 20*2 = 40
        using 1 and 2 day-pass -> ?
        using 1 and 3 day-pass -> ?
            
            Complexity: 
                Time O(3^N)
                Space O(3^N)
        2. Optimized DP:
            try all possible combinations of 1,2,7 day-passes, try to minimize the total cost, caching results at the same time
            
            1. Subproblems -> min_cost(day_i, cost_i)
            2. recurrence
                    1. min_cost(day_i, cost_i), min_cost(day_i+1, cost_i+1), min_cost(day_i+n-1, cost_i+m-1)
                    2. min_cost(day_i, cost_i) = min(min_cost(day_i+1, cost_i) for cost_i in range(0, 3)
            2. base cases:
                    if day_i >= len(days):
                        return cost
                    
            4. answer -> min_cost(0, 0)
            
            Complexity: 
                Time O(N^3)
                Space O(N^3)
        [1,4,6,7,8,20]
         i
           i
        
        """
        #total_days = [day for day in range(days[0], days[-1]+1)]
        @lru_cache(None)
        def min_cost(day_i):
            if day_i >= len(days):
                return 0
            
            cost = float("inf")
            current_day = days[day_i]
            index = bisect.bisect_left(days, current_day+1)
            cost = min(cost, min_cost(index) + costs[0])
            
            index = bisect.bisect_left(days, current_day+7)
            cost = min(cost, min_cost(index) + costs[1])
            
            index = bisect.bisect_left(days, current_day+30)
            cost = min(cost, min_cost(index) + costs[2])
            return cost
        
        return min_cost(0)
        
        
        
        