class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        """
        recurrence:
        
        1. ? matches single char -> match(i+1, j+1)
        2. s[i] == s[j] -> match(i+1, j+1)
        3. * matches zero chars -> match(i, j+1)
        3. * matches any sequence onwards -> match(i+1, j)
        
        base case:
            1. j >= len(p): return i == len(s)
            
        aa
         i
        *a
         j
         
        aab
           i
        a*
          j
        
        cb
        ?a
        cb
        ?*
        
        aa
        *

        "aa"
"a"
"aa"
"*"
"aab"
"a*"
"aab"
"a*a"
"cb"
"?a"
"cb"
"?*****"
"cb"
"????*"
"cb"
"*????"

"aab"
    i
"a*a"
  j
        """
        @lru_cache(None)
        def match(i, j):
            if j >= len(pattern):
                return i == len(text)
            if i >= len(text):
                return pattern[j] == "*" and match(i, j+1)
            if pattern[j] == "*":
                return match(i, j+1) or match(i+1, j)
            match_one_char = i < len(text) and pattern[j] in ["?", text[i]]
            return match_one_char and match(i+1, j+1)
        return match(0, 0)