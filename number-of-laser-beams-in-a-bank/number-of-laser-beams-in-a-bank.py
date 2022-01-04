class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Question from Weekly Contest 274
        
        ["011001",
         "000000",
         "010100",
         "001000"]
        
        """
        counts = []
        for row in bank:
            count = row.count("1")
            if count:
                counts.append(count)
                
        total = 0
        for i in range(0, len(counts)-1):
            total += counts[i] * counts[i+1]
            
        return total