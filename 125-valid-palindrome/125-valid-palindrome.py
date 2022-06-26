class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx, right_idx = 0, len(s)-1
        
        while left_idx < right_idx:
            left_char = s[left_idx]
            right_char = s[right_idx]
            
            if not left_char.isalnum():
                left_idx += 1
            elif not right_char.isalnum():
                right_idx -= 1
            elif left_char.lower() == right_char.lower():
                left_idx += 1
                right_idx -= 1
            else:
                return False
            
        return True