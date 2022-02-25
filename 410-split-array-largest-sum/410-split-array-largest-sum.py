class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        
        
        1. use prefix sum to give an instant answer to sum(i, j) -> O(1)
        2. subproblems: find one way to split the array into m subarrays
        3. recurrence: 1. split(i, m) = min(split(i+1, m-1), split(i...n, m...0))
                       2. sum(i, j) = max(sum(i, j) * m)
        4. Recursion + memo/ Tabulation (for loops)
        5. answer: split(0, m)
        
        [7,2,5,10,8], m = 2
         i
        [7] [2,5,10,8] m = 1
             j
              l       m = 0
        [7,2][5,10,8]
        [7,2,5][10,8]
        [7,2,5,10][8]
        """
        summ = 0     # 0  1   2   3.  4  
        pre_sum = [] # 7, 9, 14, 24, 32  # O(N)
        for num in nums:
            summ += num
            pre_sum.append(summ)
            
        def get_sum(i, j):
            # assume in the range is always correct
            # O(1) Time
            if i == 0:
                return pre_sum[j]
            return pre_sum[j] - pre_sum[i-1]
        
        @lru_cache(None)
        def split(i, k):
            if k == 1: # m == 1
                return get_sum(i, len(nums)-1)
            
            min_largest_sum = float(inf)
            for j in range(i+1, len(nums)):
                curr_summ = get_sum(i, j-1) # 7, 9, 14, 24, 32
                rest_summ = split(j, k-1)

                min_largest_sum = min(max(curr_summ, rest_summ), min_largest_sum)
                if curr_summ >= min_largest_sum: break
            return min_largest_sum

        return split(0, m)