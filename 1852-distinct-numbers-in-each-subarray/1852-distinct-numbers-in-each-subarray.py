class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        distinct = Counter()
        
        for i in range(k):
            distinct[nums[i]] += 1
        output = [len(distinct)] 
        """
        [1,1,1,1,2,3,4,2]
           ^     ^
             
        {1: 0
         2: 2
         3: 1
         4: 1
         
         }
        
        """
        for end_idx in range(k, len(nums)):
            start_idx = end_idx - k
            distinct[nums[start_idx]] -= 1
            if distinct[nums[start_idx]] == 0:
                del distinct[nums[start_idx]]

            distinct[nums[end_idx]] += 1
            
            output.append(len(distinct))
        
        
        return output
        