class Solution:
    def strStr1(self, str1: str, str2: str) -> int:
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
        n, m = len(str1), len(str2)
        for start in range(n):
            end = start + m
            if str1[start:end] == str2:
                return start
            
        return -1 if str2 else 0
            
    def strStr(self, str1, str2):
        """
        KMP Time O(N+M) | Space O(M)
             i   j
        "abcdabcdv"
         000012340
         
         abcdabcdv
                  j
         abcdabcrabcdabcdv
                          i
        """
        n = len(str1)
        m = len(str2)
        # build suffix prefix array
        
        psa = [-1 for i in range(m)]
        i, j = 0, 1
        while j < m:
            if str2[i] == str2[j]:
                psa[j] = i
                i += 1
                j += 1
            elif i > 0:
                i = psa[i-1] + 1
            else:
                j += 1
        
        i, j = 0, 0

        while i < n and j < m:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif j > 0:
                j = psa[j-1] + 1
            else:
                i += 1
        
        return i - m if j >= m else -1
                
            
            