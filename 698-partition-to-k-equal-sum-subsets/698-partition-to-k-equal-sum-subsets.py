class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        [4,3,2,3,5,2,1], k = 4 total = 20 each = 5
        
        
        Approach 1: Not working
            save the nums in map counter
            apply two sum technique to find the sesond number in the map
            decrease a counter if 2nd num found
            
            answer : check map if there is any counter > 0 -> false else true
            
        Approach:
            Use DP and try all combinations via backtracking
            
            subproblems:
                find a subset equals to the sum
                not possible to reuse the values from other subsets
                skip used value already (used set of indexes)
                    
                sum(i, sum) - include into current subset
                
                used_indexes = []
                for j in range(i, n):
                    can = sum(j, sum-nums[j])
                
                
            base cases:
                if sum == 0:
                return true
                
            answer: sum(used_indexes) == len(nums)
        """
        total_sum = sum(nums)
        nums.sort(reverse=True)
        if total_sum % k != 0:
            return False
        subset_sum = total_sum // k
        mask = 0
        memo = {}
        
        def can_summ(i, subsets, curr_sum):
            nonlocal mask
            if subsets == k:
                return True
            if curr_sum > subset_sum:
                return False
            if curr_sum == subset_sum:
                memo[mask] = can_summ(0, subsets+1,  0)
                return memo[mask]
                
            if mask in memo:
                return memo[mask]
            for j in range(i, len(nums)):
                # test if j-th bit is set
                if mask & (1 << j) != 0: continue
                # set j-th bit
                mask ^= (1 << j)
                if can_summ(j+1, subsets, curr_sum + nums[j]):
                    return True
                # unset j-th bit
                mask ^= (1 << j)
                
            memo[mask] = False
            return False
        
        return can_summ(0, 1, 0)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        