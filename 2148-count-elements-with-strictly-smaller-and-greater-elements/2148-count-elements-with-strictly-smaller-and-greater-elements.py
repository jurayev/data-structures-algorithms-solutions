class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_el = min(nums)
        max_el = max(nums)
        
        count = 0
        for num in nums:
            count += bool(min_el < num < max_el)
        
        return count
    
    
    def countElements1(self, nums: List[int]) -> int:
        
        nums_count = collections.Counter(nums)
        sorted_nums = sorted(set(nums))
        
        n = len(sorted_nums)
        count = 0
        for i in range(1, n-1):
            if sorted_nums[i-1] < sorted_nums[i] < sorted_nums[i+1]:
                count += nums_count[sorted_nums[i]]
                
        return count
        
        
        