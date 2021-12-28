class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        """
        1811
          10
           0
        
        81
        18
        
        1801
        1081
        1801
        
        99
        
        199
        991
        """
        return num == 0 or num % 10 != 0
        