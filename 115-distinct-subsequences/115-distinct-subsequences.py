class Solution:
    def numDistinct(self, text: str, pattern: str) -> int:
        """
        recurrence:
            1. match char in both text and pattern
            2. delete char in text
        
        base case:
            1. j >= len(patter): return 1
            2. i >= len(text): return 0
            
        
        "rabbbit"
            i
        "rabbit"
           j
            
        "abc"
        "c"
        "abc"
        "am"
        "m"
        "p"
        """
        
        @lru_cache(None)
        def count_matches(i, j):
            if j >= len(pattern):
                return 1
            if i >= len(text):
                return 0
            counter = 0
            if text[i] == pattern[j]: 
                counter += count_matches(i+1, j+1)
            return counter + count_matches(i+1, j)
        
        return count_matches(0, 0)