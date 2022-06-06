class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        
        AABABBA k=1
          ^
             ^
        len = 4
        count = 3
        A:2
        B:3
        """
        max_count = 0
        best_len = 0
        counts = Counter()
        
        for idx in range(len(s)):
            char = s[idx]
            counts[char] += 1
            max_count = max(counts[char], max_count)
            
            if best_len < max_count + k:
                best_len += 1
            else:
                counts[s[idx-best_len]] -= 1
                
        return best_len