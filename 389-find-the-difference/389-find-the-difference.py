class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Time O(M+N)
        Space O(1)
        """
        single_number = 0
        for letter in s + t:
            single_number ^= ord(letter)
        return chr(single_number)
        
        
    def findTheDifferenceCounter(self, s: str, t: str) -> str:
        """
        Time O(N+M)
        Space O(N+M)
        """
        s_counts = collections.Counter(s)
        t_counts = collections.Counter(t)
        
        for letter, count in t_counts.items():
            if s_counts[letter] != count:
                return letter
            
        return ""