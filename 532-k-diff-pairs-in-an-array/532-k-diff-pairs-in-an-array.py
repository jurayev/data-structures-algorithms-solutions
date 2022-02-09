class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        seen = set()
        
        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))
            if num + k in seen:
                pairs.add((num, num + k))
                
            seen.add(num)
        return len(pairs)
        
    def findPairs1(self, nums: List[int], k: int) -> int:
        """
        Time O(N log N)
        Space O(N)

        Dry Run
        [3,1,4,1,5] k = 2
        
        [1,1,1,3,3,4,5]
        
        (1,3) (3,5)
        (1,1) (3,3)
        """
        
        pairs = set()
        seen = set()
        sorted_nums = sorted(nums)
        
        for num in sorted_nums:
            if num - k in seen:
                pairs.add((num-k, num))
                
            seen.add(num)
        return len(pairs)