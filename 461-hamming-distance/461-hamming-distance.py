class Solution:
    def hammingDistance(self, start: int, end: int) -> int:
        """
        0100  XOR
        1110
        
        1010
        0001

        1 ^ 0 -> 1
        1 ^ 1 -> 0
        0 ^ 1 -> 1
        """
        distance = 0
        xored = start ^ end
        for i in range(0, 32):
            distance += xored & (1 << i) != 0
            
        return distance