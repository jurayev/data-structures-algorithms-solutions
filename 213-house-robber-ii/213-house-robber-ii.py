class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [4,3,2]
        
        [1,2,3,1]
         1 2 4 3
           i   i
        
        [1,5,3,1]
         1 5 5 1
         i   i
         
         [1,5,3,1]
          1 5 3 6
            i   i
            
        [200,3,140,20,10]
         200 3 340 340
         200 3 140 140 150
                i      i
                
        state: -> amount[i]
        state value: -> amount[i] -> max amount robbed till i
        initial states -> amount[0] = nums[0] and amount[1] = nums[1]; amount[1] = nums[1] and amount[2] = nums[2];
        state transition -> amount[i] = max(amounts[i] + amounts[i-2], amounts[i-1])
        calculation order -> 0 .... n-2; 1....n-1;
        answers -> amounts[n-2]; amounts[n-1]
        
        Time O(2N) -> O(N)
        Space O(N) -> O(1)
        
[2,3,2]
[1,2,3,1]
[1,2,3]
[1,5,3,1]
[200,3,140,20,10]
[200,3,140,20,400]
[200,3,140,20,400,200,3,140,20,400,200,3,140,20,400,200,3,140,20,400,200,3,140,20,200,3,140,20,400]
[1]
[1,2]
[5,2,1]
[1,3,1,3,100]
        """
        n = len(nums)
        if n < 4:
            return max(nums)
        amounts = [0 for i in range(n)]
        amounts[0] = nums[0]
        amounts[1] = max(nums[0], nums[1])
        
        for i in range(2, n-1):
            amounts[i] = max(nums[i] + amounts[i-2], amounts[i-1])
        #print(amounts)
        best = amounts[n-2]
        amounts = [0 for i in range(n)]
        amounts[1] = nums[1]
        amounts[2] = max(nums[1], nums[2])
        for i in range(3, n):
            amounts[i] = max(nums[i] + amounts[i-2], amounts[i-1])
        #print(amounts)
        return max(best, amounts[n-1])
        