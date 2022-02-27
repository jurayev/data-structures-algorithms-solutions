class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        
        [1,5,2]
         l
         r
        
        
        subproblems:
                burst leftmost or rightmost, trying all subarrays
        
        recurrence / state:
                points = max(play(l+1, r) + nums[l], play(l, r-1) + nums[r])
                
        base cases:
                if l >= r: return 0
                
        answer:
            points = play(0, n-1))
            total_points - points <= points
            
        Time O(N^2)
        Space O(N^2)
        
        [1,5,2]
             l
             r
             
              1-3         [1,5,2]   2 - 4
                    /                   \
           5-2    [5,2] 2 - 5    1-5   [1,5] 5-1
                 /    \             /      \
       2-0    [2]     [5] 5-0    [5]       [1]
              / \    /    \
            []   []        []
        
        """
        @lru_cache(None)
        def play(l, r):
            if l > r:
                return 0
            return max(nums[l] - play(l+1, r), nums[r] - play(l, r-1))
        
        points = play(0, len(nums)-1)
        total_points = sum(nums)
        print(total_points, points)
        return points >= 0