class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = collections.defaultdict(int)
        counts[0] = 1
        counter = 0
        summ = 0
        for num in nums:
            summ += num
            diff = summ - k
            if diff in counts:
                counter += counts[diff]
            counts[summ] += 1
        return counter
        
    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        [1,-2,1,-1,2]
            i    j     
        [1,-1,0,-1,1]
        
        1: 2
        -1: 2
        0: 1
        
      
         k = 2
        
        TLE
        """
        counter = 0
        for i in range(0, len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                if summ == k: counter += 1
        return counter