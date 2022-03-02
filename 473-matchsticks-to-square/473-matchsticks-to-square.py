class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        [1,1,2,2,2] total = 8, k = 4, subset = 2
        
        
        subproblems:
                Can I make 4 subsets with equal sum out of the given numbers?
                
                Find all subsets, starting from 0 .... n-1
                if can make 4 subsets and use all numbers -> answer true
                else answer is false
                
                find_subsets(k, i, sum) = find_subsets(k-1...0, i...n-1, sum...0)
        
        base cases:
            if k == 0:
                return True
            if sum == 0:
                return find(subsets)
            if sum < 0:
                return False
        answer ->   if can make 4 subsets and use all numbers -> answer true
                    else answer is false
        """
        @lru_cache(None)
        def find_subsets(mask, k, curr_sum):
            #nonlocal mask
            if k == 0:
                return True
            if curr_sum == 0:
                return find_subsets(mask, k-1, subset_sum)
            if curr_sum < 0:
                return False
            # if mask in cache:
            #     return cache[mask]
            
            for j in range(0, len(matchsticks)):
                if mask & (1 << j) != 0: continue
                #mask = mask ^ (1 << j)
                
                if find_subsets(mask ^ (1 << j), k, curr_sum - matchsticks[j]):
                    return True

                #mask = mask ^ (1 << j)
            
            # cache[mask] = False
            return False
        
        total_sum = sum(matchsticks)
        subsets_count = 4
        if total_sum % subsets_count != 0:
            return False
        subset_sum = total_sum // subsets_count
        return find_subsets(0, subsets_count-1, subset_sum)