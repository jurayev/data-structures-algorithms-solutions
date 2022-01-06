class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Time Complexity O(N)
        Space Complecity O(M), where M is the number of distinct letters
        """
        
        on_stack = set()
        last_seen = {s[idx]: idx for idx in range(len(s))}
        stack = []
        
        for idx, char in enumerate(s):
            if char in on_stack: continue
            while stack and stack[-1] > char and last_seen[stack[-1]] > idx:
                val = stack.pop()
                on_stack.remove(val)
            stack.append(char)
            on_stack.add(char)
                
        return "".join(stack)