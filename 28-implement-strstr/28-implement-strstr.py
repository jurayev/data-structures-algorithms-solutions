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
        n, m = len(str1), len(str2)
        for start in range(n):
            end = start + m
            if str1[start:end] == str2:
                return start
            
        return -1 if str2 else 0
            
            