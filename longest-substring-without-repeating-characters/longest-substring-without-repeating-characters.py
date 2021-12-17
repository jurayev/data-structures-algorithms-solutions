class Solution:

                    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TC: O(N)
        SC: O(N)
        Examples:
            best = 3
            seen = {a, c, b}

            "abcabcbb"
                 e
               s


            "pwwkew"
                   ^
               ^
        """
        
        best = 0
        seen = set()
        
        start, end = 0, 0
        
        while end < len(s):
            end_char = s[end]
            while end_char in seen:
                start_char = s[start]
                seen.remove(start_char)
                start += 1
            seen.add(end_char)
            
            best = max(best, end - start + 1)
            end += 1
            
        return best