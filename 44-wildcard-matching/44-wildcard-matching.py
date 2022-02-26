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
        
        Time O(N*M)
        Space O(N*M)

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
        """
        @lru_cache(None)
        def match(i, j):
            if j >= len(pattern):
                return i == len(text)

            if pattern[j] == "*":
                # match(i, j+1) -> match zero chars in text
                # match(i+1, j) -> match one char in text
                return match(i, j+1) or i < len(text) and match(i+1, j)
            # match(i+1, j+1) -> both matched
            match_one_char = i < len(text) and pattern[j] in ["?", text[i]]
            return match_one_char and match(i+1, j+1)
        return match(0, 0)