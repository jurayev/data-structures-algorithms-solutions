class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        
        abcacbda
        ^     ^
        
        """
        size = len(s)
        palindrome = ""
        for i in range(size):
            odd_p = self.find_palindrome(s, size, i, i)
            even_p = self.find_palindrome(s, size, i, i+1)
            palindrome = max([palindrome, odd_p, even_p], key=len)
        
        return palindrome
    
    def find_palindrome(self, s, size, start, end):
        while start >= 0 and end < size and s[start] == s[end]:
            start -= 1
            end += 1
        
        return s[start+1:end]