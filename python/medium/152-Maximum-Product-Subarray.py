class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [0,-1,-2,4,3,-2,0,4,-2] => even => odds
                 ^
        [0,-1,-2,4,12,-2,0,4,-2]   no zeros, only pluses
        [0,-1,2,8,24,-48,0,-8,-2] no zeros, only minuses left -> right

        [0,-48,48,-24,-6,-2,0,-8,-2] no zeros, only minuses left <- right

        keep track of the max, including zero if any

        1. zero found    -> skip zeros
        2. minus found   -> skip minus
        3. minus found   -> include minus


        """
        best = current = nums[0]
        # first go -> no zeros, only pluses product

        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            if num > 0 and current:
                current = max(current, current * num, num)
            else:
                current = num
            best = max(best, current)

        # second go -> no zeros, only minuses product, left -> right
        current = nums[0]
        best = max(best, current)

        for i in range(1, n):
            num = nums[i]
            if num and current:
                current *= num
            else:
                current = num
            best = max(best, current)
        # third go -> no zeros, only minuses product, left <- right
        current = nums[-1]
        best = max(best, current)
        for i in range(n - 2, -1, -1):
            num = nums[i]
            if num and current:
                current *= num
            else:
                current = num
            best = max(best, current)
        return best