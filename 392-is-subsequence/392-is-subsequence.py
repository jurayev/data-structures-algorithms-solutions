class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s = "abcr", t = "ahcbgddcr"
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