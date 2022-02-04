class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        Approach 2:
            Calculate set bits at every position in every num -> k
            Calculate number of unset bits at every position in every num -> (n - k)
            Calcualte the distance for every k -> k*(n -k) 
        
        Analysis:
            Time Complexity: O(n)
            Space Complexity (n)
        """
        set_bit_counts = collections.Counter()
        
        for num in nums:
            
            for i in range(0,32):
                set_bit_counts[i] += (num & (1 << i) != 0)
        
        dist, n = 0, len(nums)
        for count in set_bit_counts.values():
            dist += count * (n - count) 
        return dist
    
    def totalHammingDistance1(self, input_nums: List[int]) -> int:
        counts = collections.Counter(input_nums)
        nums = list(counts.keys())
        total_distance = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                total_distance += self.get_distance(nums[i], nums[j]) * counts[nums[i]] * counts[nums[j]]
                
        return total_distance
    
    def get_distance(self, start, end):
        """
        0100  XOR
        1110
        
        1010
        0001

        1 ^ 0 -> 1
        1 ^ 1 -> 0
        0 ^ 1 -> 1
        """
        distance = 0
        xored = start ^ end
        for i in range(0, 32):
            distance += xored & (1 << i) != 0
            
        return distance
        
        