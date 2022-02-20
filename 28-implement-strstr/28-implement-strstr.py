class Solution:
    def strStr(self, str1: str, str2: str) -> int:
        """
        helpplplo
                ^ 
              plo;
                ^
              
        
        Time -> O(n*m)
        
        Time -> O(n)
        
        ""
        "a"
        "a"
        ""
        "hello"
        "hhello"
        "hello"
        "helloo"
        "hello"
        "hello"
        "hello"
        "eh"
        "hello"
        "lo"
        "hello"
        "loo"
        "hello"
        "ll"
        "hello"
        "ell"
        "aaaaa"
        "bba"
        ""
        ""
        "mississi"
        "issip"

        """
#         TLE for large test case
#         n, m = len(str1), len(str2)
#         if m > n:
#             return -1
#         if not m:
#             return 0
#         for i in range(n):
#             if i + m > n:
#                 break
#             for j in range(m):
#                 if str1[i+j] != str2[j]:
#                     break
#                 if j == m-1:
#                     return i
            
        
#         return -1
        # index = str1.find(str2)
        # return index
#         n, m = len(str1), len(str2)
#         for start in range(n):
#             end = start + m
#             if str1[start:end] == str2:
#                 return start
            
#         return -1 if str2 else 0
        str2_hash = hash(str2)
        n, m = len(str1), len(str2)
        
        for start in range(n):
            substring = str1[start : start + m]
            if hash(substring) == str2_hash:
                return start
        return -1 if str2 else 0
        #return self.KMP(str1, str2)
            
    def KMP(self, str1, str2):
        """
        KMP Time O(N+M) | Space O(M)

        s2 "abcdvrbcdvbv"
            000001234500
            j
        s1  ababcdvabcdvrv
            i
        """
        n = len(str1)
        m = len(str2)
        pattern = self.get_pattern(str2)
        index = self.get_substring_index(str1, str2, pattern)
        return index
        
    def get_pattern(self, string):
        n = len(string)
        pattern = [0 for _ in range(n)]
        
        start, end = 0, 1
        while end < n:
            if string[start] == string[end]:
                # prefix == suffix # save start index + 1 as a next position to be matched
                pattern[end] = start + 1
                start += 1
                end += 1
            elif start > 0:
                # take start - 1, to consider only string before start
                # ababmabad
                # 001201230
                #    s    e
                start = pattern[start - 1]
            else:
                end += 1
        return pattern         
    
    def get_substring_index(self, string, substring, pattern):
        n, m = len(string), len(substring)
        i, j = 0, 0
        while i < n and j < m:
            if string[i] == substring[j]:
                i += 1
                j += 1
            elif j > 0:
                # take j - 1, to consider only string before j
                j = pattern[j - 1]
            else:
                i += 1
                
        return i - j if j >= m else -1
        
        
            
            