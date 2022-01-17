class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution
        
        [1,2,3]
           ^
        2^n subsets
        
        []
        
        [1]
            [1,2]
                  [1,2,3]
            [1,3]
        [2]
           [2,3]
        [3]
        
        TC O(2*n), SP O(2*n)
        
        """
        
        subsets = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset[:])
                new_subsets[-1].append(num)
            subsets.extend(new_subsets)
            
        return subsets
        
        
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """ recursion
        
        [1,2,3]
           ^
        2^n subsets
        
        []
        
        [1]
            [1,2]
                  [1,2,3]
            [1,3]
        [2]
           [2,3]
        [3]
           
        
        TC O(2*n), SP O(2*n)
        """
        subsets = []
        self.generate(subsets, [], nums, 0)
        
        return subsets
    
    def generate(self, subsets, subset, nums, start):
        subsets.append(subset[:])

        for i in range(start, len(nums)):            
            subset.append(nums[i])
            self.generate(subsets, subset, nums, i+1)
            subset.pop()
            
    
    
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """ Bitwise solution
        
            TC O(2*n), SP O(2*n)
        """
        result = []
        n = len(nums)
        for i in range(0, n+1 << 1):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
            
        return result
                    
        