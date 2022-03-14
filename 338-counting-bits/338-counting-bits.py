class Solution:
    def countBits(self, n: int) -> List[int]:
        counters = []
        for i in range(n+1):
            counters.append(self.count_bits(i))
        return counters 
            
    def count_bits(self, number):
        """
        
        101
        
        001 -> 001
        010 -> 000
        100 -> 100
        """
        count = 0
        for i in range(0, 32):
            count += number & (1 << i) != 0
            
        return count