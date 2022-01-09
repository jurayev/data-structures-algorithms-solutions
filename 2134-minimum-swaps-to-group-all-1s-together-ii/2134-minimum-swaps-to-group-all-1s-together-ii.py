class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Approach:
            Count total number of ones.
            Set the window size = total ones
            Slide until start pointer reaches the end of the array
            Difference betweeen ones in total and in window is the answers
        Examples:
            [0,1,0,1,1,0,0]
            [0,1,1,1,0,0,1,1,0]
            [1,1,0,0,1]
            [1]
            [0]
            [0,1,0,0,0,0,1,1,0]
            [1,0,0,0,0,1]
            [1,1,1]
            [0,0,0]
            [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0] => 7
                     ^                             ^      
             0 1 2 3 4 5 6 7 8
            [0,1,0,0,1,0,0,0,1]
               ^             ^   ^
                
            total = 16
            ones_in_window = 8
            
        Complexities:
            Time O(N)
            Space O(1)
        """
        N = len(nums)
        total_ones = sum(nums)
        start, end = 0, 0
        in_window_ones = 0
        # set the window size
        while end < total_ones:
            in_window_ones += nums[end]
            end += 1
            
        end %= N
        
        best = total_ones - in_window_ones
        # moving the window in circular manner until start reaches the end of nums
        while start < N:
            in_window_ones -= nums[start]
            in_window_ones += nums[end]
            best = min(best, total_ones - in_window_ones)
            start += 1
            end += 1
            end %= N
            
        return best