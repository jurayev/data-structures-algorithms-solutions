class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
         0  1  2  3 4 5 6 7
        [4,-3,-2,-7,8,2,-3,-1]  1 ... 10^5 100001
         1  2  3 4 0 0 7 8
                     ^
        duplicates -> [2, 3]
        missing    -> [5, 6]
        
        Approach:
            Map the numbers with indexes and mark seen with negatice sign
        Time O(N)
        Space O(1)
        """
        
        duplicates = []
        
        for num in nums:
            origin_num = abs(num)
            
            if nums[origin_num-1] < 0:
                duplicates.append(origin_num)
            else:
                nums[origin_num-1] *= -1
                
        return duplicates
        
        