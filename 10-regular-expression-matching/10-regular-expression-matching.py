class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ 
        recurrence:
        x. match -> move i, j
        x. "." move forwards i, j
        -. "d*" move forwards i as long as d is match, then move j once
        x. "d*" move forwards j, backtrack move i if char1 == char2
        x. ".*" move forwards i, backtrack move j
        x. "*" -> i, j+1
        
        base cases:
            1. i > n: false
            2. j > m: false
            3. i == n and j == m: true
            
        answer: match(0, 0)
        """
        @lru_cache(None)
        def match(i, j):
            if j >= len(p):
                return i == len(s)
            wildcard_match = j+1 < len(p) and p[j+1] == "*"
            match_curr_char = i < len(s) and p[j] in [".", s[i]]
            #   abc        abc     abc  abc
            #   .*abc      a.*c    aa*  ab.*.*
            if wildcard_match:
                return match(i, j+2) or match_curr_char and match(i+1, j)

            return match_curr_char and match(i+1, j+1)
        
        return match(0, 0)