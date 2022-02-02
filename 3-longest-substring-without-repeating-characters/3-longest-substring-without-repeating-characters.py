class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abcabcbb
               i
               j
        {}
        """
        seen = set()
        best = 0
        i = 0
        for j in range(0, len(s)):
            end_char = s[j]
            while end_char in seen:
                start_char = s[i]
                seen.remove(start_char)
                i += 1
            seen.add(end_char)
            best = max(best, len(seen))
            
        return best
        