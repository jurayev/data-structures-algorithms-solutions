class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        abbaca
           ^
        ["c", "a"]
        
        azxxzy
        
        ["a", "y"]
        
        azxzxxzxy
        
        [a, z, y]
        
        azxzxxzxza
        []
        Time O(N)
        Space O(N)
        """
        
        stack = []
        
        for letter in s:
            added = 0
            while stack and stack[-1] == letter:
                stack.pop()
                added += 1
            if not added:  
                stack.append(letter)
            
        return "".join(stack)