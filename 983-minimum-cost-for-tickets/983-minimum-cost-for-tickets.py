class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        days = [1,4,6,7,8,11], costs = [2,7,15], durations = [1,7,30]
        
        [0,1,2,3,4,5,6,7,8,9,10,11]
        [0,2,2,2,4,4,6,7,9,9, 9, 11]
         i-1
         i-7
         i-30
        """
        max_days = days[-1]+1
        min_costs = [0] * max_days
        durations = [1, 7, 30]
        
        for day in range(1, max_days):
            min_costs[day] = float("inf")
            for cost, duration in zip(costs, durations):
                if day in days:
                    day_pass = max(day-duration, 0)
                    min_costs[day] = min(min_costs[day], min_costs[day_pass] + cost)
                else:
                    min_costs[day] = min_costs[day-1]
        return min_costs[max_days-1]
        
    def mincostTicketsRecursion(self, days: List[int], costs: List[int]) -> int:
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
                Time O(N)
                Space O(N)
        [1,4,6,7,8,20]
         i
           i
        
        """
        durations = [1, 7, 30]
        day_set = set(days)
        
        @lru_cache(None)
        def min_cost(day):
            # DP + linear search for 365 day
            # Time O(W), Space O(W), W is one calendar year
            if day > 365:
                return 0
            if day not in day_set:
                return min_cost(day+1)
            minimum_cost = float("inf")
            for cost, duration in zip(costs, durations):
                minimum_cost = min(minimum_cost, min_cost(day+duration) + cost)
                
            return minimum_cost
            
        @lru_cache(None)
        def min_cost_bin_search(day_i):
            # DP + bin search the next day to travel
            # Time O(NlogN), Space O(N)
            if day_i >= len(days):
                return 0
            
            minimum_cost = float("inf")
            current_day = days[day_i]
            for cost, duration in zip(costs, durations):
                next_day_i = bisect.bisect_left(days, current_day+duration)
                minimum_cost = min(minimum_cost, min_cost_bin_search(next_day_i) + cost)

            return minimum_cost
        
        return min_cost(0)
        
        
        
        