class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        
        0 ^ 0 = 0
        1 ^ 1 = 0
        1 ^ 0 = 1
        0 ^ 1 = 1
        
        x = 001001
            000001
            001000
        x >>= 1
        
        Time O(N) - N bits count in the number
        Space O(1)
        """
        if not n: return 1
        leftover = n
        
        complement = n
        bitmask = 1
        while leftover > 0:
            leftover >>=1
            complement ^= bitmask
            bitmask <<= 1
            
        return complement