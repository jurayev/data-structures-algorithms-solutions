class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        
        aacecaaa   -> aaacecaaa
        aaacecaa
        
        aaacecaa   -> aacecaaacecaa
        ^ 
        aacecaaa
             ^
        bacecaaa   -> aaacecabacecaaa
        ^
        
        abcd       -> dcbabcd
        dcba
        ^
       
        accd       -> dccaccd
        dcca
        
        baa        -> aabaa
        aab
        aa         -> 
       ^
        bcaabbb    -> aacbcaabbb
        bbbaacb                 ^
              ^
        Sol 1. 
            1. Take all substring
            2. Try to find the longest leftmost palindrome in it (start, end indexes)
            3. if start index < 0 -> just prepend everything after end index
            4. if start index >= 0 -> prepend everything after start index
        """
        r = s[::-1]
        n = len(s)
        for start_idx in range(n):
            substring = r[start_idx:]
            if s.startswith(substring):
                return r[:start_idx] + s
        return ""