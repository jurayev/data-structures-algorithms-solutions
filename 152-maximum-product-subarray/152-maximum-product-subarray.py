class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [2,3,-2,4]
        [-2,0,-1]
        [ 2, 3, -2, 4, -2]
        [ 2, 3, 0, 4, -2,-4]
        [2,-1,1,1]
        [-2]
        
        [-1,-2,-9,-6]
         -1 2, -18,96
          98-98 54 -6
        [1,-2,-9,-6]
         1 -2 18,-96
         -96-98  54  -6
         
         [1,-2, 1, -9,6]
         Better O(N)
         
         Brute force O(N^2)
         
        """
        if not nums:
            return -1
        best = float("-inf")
        n = len(nums)
        product = 1
        for i in range(0, n):
            product = product * nums[i]
            best = max(best, product)
            if nums[i] == 0:
                product = 1
        
        product = 1
        for i in range(n-1, -1, -1):
            product = product * nums[i]
            best = max(best, product)
            if nums[i] == 0:
                product = 1

        return best