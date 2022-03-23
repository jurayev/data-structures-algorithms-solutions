class Solution:
    def largestDivisibleSubset1(self, nums: List[int]) -> List[int]:
        """
        Approach 1:
        sort the input
        two for loops
        take any two pairs and try to divide
        take the longest subset + current value
        
        [1,2,3,4,9]
               i
        
        1: {1}
        2: {1,2}
        3: {1,3}
        4: {1,2,4}
        9: {1,3}
        """
        asc_nums = sorted(nums)
        subsets = defaultdict(set)
        size = len(nums)
        for num1 in asc_nums:
            candidate_subsets = [subsets[num2] for num2 in asc_nums if num1 % num2 == 0]
            max_subset = max(candidate_subsets, key=len) | {num1}
            subsets[num1] = max_subset
            
        return max(subsets.values(), key=len)
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        asc_nums = sorted(nums)
        size = len(nums)
        dp = [set() for _ in range(size)]
        max_subset = set()
        
        for i in range(size):
            first_num = asc_nums[i]
            for j in range(i):
                second_num = asc_nums[j]
                if first_num % second_num == 0:
                    dp[i] = max([dp[i], dp[j]], key=len)
                    
            dp[i] = dp[i] | {first_num}
            max_subset = max([max_subset, dp[i]], key=len)
                
        return max_subset