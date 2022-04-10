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
        #return match(0, 0)
        
        return self.match_pattern(text, pattern, 0, 0)
    @lru_cache(None)
    def match_pattern(self, string, pattern, s_idx, p_idx) -> bool:
        if p_idx == len(pattern):
            return s_idx == len(string)
        
        if s_idx == len(string) and pattern[p_idx] == "*":
            return self.match_pattern(string, pattern, s_idx, p_idx+1)
        if s_idx == len(string):
            return False
        
        if pattern[p_idx] in ["?", string[s_idx]]:
            matched = self.match_pattern(string, pattern, s_idx+1, p_idx+1)
            if matched:
                return True
        if pattern[p_idx] == "*":
            # skip
            matched = self.match_pattern(string, pattern, s_idx, p_idx+1)
            if matched:
                return True
            # take one
            matched = self.match_pattern(string, pattern, s_idx+1, p_idx)
            if matched:
                return True

        return False
