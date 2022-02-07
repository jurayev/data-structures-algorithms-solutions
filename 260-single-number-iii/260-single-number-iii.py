class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        2,2,1,1,3,5
        
        3 0011 ^
          0101
          0110
        
        Approach:
            Xor all numbers, all duplicates turned to 0, 
            two single numbers make some other number with bits set that are different in original numbers
            find the any set bit and split all numbers based on this bitmask.
            Group 1 ends up having duplicates and single number
            Group 2 ends up having duplicates and single number
        """ 
        xored = 0
        for num in nums:
            xored ^= num
        ith_bitmask = 1
        for i in range(0, 32):
            if xored & (1 << i) != 0:
                ith_bitmask = i
                break
                
        xored_group_one = 0
        xored_group_two = 0
        for num in nums:
            if num & (1 << ith_bitmask) != 0:
                xored_group_one ^= num
            else:
                xored_group_two ^= num
        return [xored_group_one, xored_group_two]