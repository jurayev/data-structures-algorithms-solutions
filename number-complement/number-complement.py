class Solution:
    def findComplement(self, num: int) -> int:
        """
        101
         01
        
        TC O(1)
        SC O(1)
        """
        bit = 1
        rem = num
        while rem:
            num ^= bit
            bit = bit << 1
            rem = rem >> 1
        return num