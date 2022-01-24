class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # case 1
        all_capitals = word.upper()
        if word == all_capitals:
            return True
        
        # case 2
        all_lower = word.lower()
        if word == all_lower:
            return True
        
        # case 3
        capitalized = word.capitalize()
        if capitalized == word:
            return True
        
        return False