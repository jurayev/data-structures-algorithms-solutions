class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        
        return self.isSubsequence(s, t[1:])
    
    def isSubsequence1(self, s: str, t: str) -> bool:
        """
        s = "abck", t = "ahcbgddcr"
                ^
                                  ^
        "aaaaaa"
             ^
        "bbaaaa"
              ^
        """
        idx = 0
        for char in s:
            while idx < len(t) and char != t[idx]:
                idx += 1
            
            if idx >= len(t):
                return False
            idx += 1
        return True