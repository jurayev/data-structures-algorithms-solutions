class Solution:
    def countBits(self, n: int) -> List[int]:
        counters = []
        for i in range(n+1):
            counters.append(self.pop_count(i))
        return counters 
    
    def pop_count(self, number):
        count = 0
        while number:
            number &= number - 1
            count += 1
        return count
    
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