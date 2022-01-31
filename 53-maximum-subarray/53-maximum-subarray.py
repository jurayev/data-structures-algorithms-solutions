class Solution:
    def maxSubArray(self, nums):
        prev_sum = 0
        max_sum = float("-inf")

        for curr_number in nums:
            prev_sum = max(curr_number, prev_sum + curr_number)
            max_sum = max(max_sum, prev_sum)
        return max_sum	
        
        