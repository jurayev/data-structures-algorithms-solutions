class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        """
        [10,6,5,8]
         
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [-1, -1, -1,-1, 5, 6,-1, 8, -1, 10]
        
        """
        buckets = [0] * 1000002
        
        for num in nums:
            buckets[num] += 1
        
        lonely_nums = []
        for num in nums:
            if buckets[num] == 1 and not buckets[num-1] and not buckets[num+1]:
                lonely_nums.append(num)
                
        return lonely_nums
        