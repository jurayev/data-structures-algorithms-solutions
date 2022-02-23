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
        pre_pre_amount = nums[0]
        pre_amount = max(nums[0], nums[1])
        
        for i in range(2, n-1):
            amount = max(nums[i] + pre_pre_amount, pre_amount)
            pre_pre_amount = pre_amount
            pre_amount = amount

        best_after_first_run = pre_amount

        pre_pre_amount = nums[1]
        pre_amount = max(nums[1], nums[2])
        for i in range(3, n):
            amount = max(nums[i] + pre_pre_amount, pre_amount)
            pre_pre_amount = pre_amount
            pre_amount = amount
        
        return max(best_after_first_run, pre_amount)
        