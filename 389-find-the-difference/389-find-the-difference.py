class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = collections.Counter(s)
        t_counts = collections.Counter(t)
        
        for letter, count in t_counts.items():
            if s_counts[letter] != count:
                return letter
            
        return ""