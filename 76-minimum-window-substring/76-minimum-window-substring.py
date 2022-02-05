class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "ADOBECODEBANC", t = "ABC"   t count = 3
                       ^                   
                         ^
                                  010
        s count = 0
        
        Time O(N+M)
        Space O(M)
        """
        
        counts = collections.Counter(t) 
        counter = len(t)
        min_size = float("inf")
        min_start, min_end = 0, -1
        start, end = 0, 0
        
        while end < len(s):
            end_char = s[end]
            if end_char in counts:
                counts[end_char] -= 1
                if counts[end_char] >= 0:
                    counter -= 1
                
            while counter == 0:
                if end - start + 1 < min_size:
                    min_start, min_end = start, end
                    min_size = end - start + 1
                start_char = s[start]
                if start_char in counts:
                    counts[start_char] += 1
                    if counts[start_char] > 0:
                        counter += 1
                    
                start += 1
                
            end += 1
        return s[min_start:min_end+1]