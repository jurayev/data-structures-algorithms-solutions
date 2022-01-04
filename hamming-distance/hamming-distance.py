class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        ans -> 6
        
        101011100
        000000101
        101011001
        
        0001
        0100
        0101
        
        1 ^ 1 = 0
        0 ^ 0 = 0
        
        1 ^ 0 = 1
        0 ^ 1 = 1 
        
        
        1 & 1 = 1
        0 & 0 = 0
        
        1 & 0 = 0
        0 & 1 = 0 
        
        
        1 | 1 = 1
        0 | 0 = 0
        
        1 | 0 = 1
        0 | 1 = 1 
        
        XOR two numbers, count 1 bits
        """
        
        xored = x^y
        
        one_bits = 0
        
        for i in range(0, 32):
            one_bits += (xored & (1 << i) != 0)
            
        return one_bits