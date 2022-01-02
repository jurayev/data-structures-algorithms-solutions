class Solution:
    def checkString(self, s: str) -> bool:
        """
        Question from Weekly Contest 274
        """
        a_idx = -1
        b_idx = len(s)
        
        for idx, char in enumerate(s):
            if char == 'a':
                a_idx = max(a_idx, idx)
            else:
                b_idx = min(b_idx, idx)
        
        return a_idx < b_idx