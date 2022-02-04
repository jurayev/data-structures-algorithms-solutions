class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Solution 1: Time O(N), Space O(N)
            count the frequencies of all nums, the the number with freqency 1 is the answer
            
        Solution 2: Time O(N), Space O(1)
        
            Using bitwise operations.
            Use property of XOR operation
            
            x ^ 0 = x
            x ^ x = 0
        
        """
        
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        return xor_sum