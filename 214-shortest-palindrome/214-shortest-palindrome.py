class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        
        aacecaaa   -> aaacecaaa
        aaacecaa
        
        aaacecaa   -> aacecaaacecaa
           j 
        aacecaaa
                ^
        aacecaaa$aaacecaa
        
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
        n, m = len(s), len(s)
        rev_str = s[::-1]
        # buidling pattern for original string
        pattern = [0] * n
        start, end = 0, 1
        while end < n:
            if s[start] == s[end]:
                pattern[end] = start + 1
                start += 1
                end += 1
            elif start > 0:
                start = pattern[start-1]
            else:
                end += 1
                
        # find longest common prefix in original string that equals to suffix in reverse string
        
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == rev_str[j]:
                i += 1
                j += 1
            elif i > 0:
                i = pattern[i-1]
            else:
                j += 1
        end = j - i
        return rev_str[:end] + s
        
    def shortestPalindrome1(self, s: str) -> str:
        r = s[::-1]
        n = len(s)
        for start_idx in range(n):
            substring = r[start_idx:]
            if s.startswith(substring):
                return r[:start_idx] + s
        return ""