class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Time O(N LOG 4) -> 1 heappop + 3 heappush
        Space O(N LOG 4)
        """
        seen = set()

        factors = [2, 3, 5]

        ugly_count = 1
        min_heap = [1]

        while ugly_count < n:
            curr_value = heappop(min_heap)
            ugly_count += 1
            for factor in factors:
                ugly = factor * curr_value
                if ugly not in seen:
                    heappush(min_heap, factor * curr_value)
                seen.add(ugly)
        
        return heappop(min_heap)
