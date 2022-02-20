class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        
        "aaacecaa"
        "aacecaaa"
        
        aaacecaa # aacecaaa
        Sol 1. 
            1. Take all substring
            2. Try to find the longest leftmost palindrome in it (start, end indexes)
            3. if start index < 0 -> just prepend everything after end index
            4. if start index >= 0 -> prepend everything after start index
            
        Sol 2. KMP
            1. Make pattern of the original string
            2. compare reverse string with original string (original string is considered as a substring here)
            
        Sol 2. Optimized KMP
            1. Make pattern of the original string + reverse string
            2. the last position in patter would indicate the longest prefix suffix
            3. take last position as len of prefix-suffix and take a substring from reversed till this position.
        """
        rev_s = s[::-1]
        search_string = s + "#" + rev_s
        n = len(search_string)
        pattern = [0] * n
        i, j = 0, 1
        while j < n:
            if search_string[i] == search_string[j]:
                pattern[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = pattern[i-1]
            else:
                j += 1
        end_index = len(s) - pattern[-1]
        return rev_s[:end_index] + s

    def shortestPalindrome2(self, s: str) -> str:
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