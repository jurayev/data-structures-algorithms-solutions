from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """DFS approach"""
        result = []
        self.dfs(result, [], n, 0, 0)
        return result
        
    def dfs(self, result, brackets, n, opening, closing):
        if opening < closing: # base case 1 # unbalanced permutation
            return
        if opening > n or closing > n: # base case 2 # unbalanced permutation
            return
        if len(brackets) == n*2: # base case 3 # making sure the balance
            result.append("".join(brackets))
            return
        brackets.append("(")
        self.dfs(result, brackets, n, opening+1, closing)
        brackets.pop()
        
        brackets.append(")")
        self.dfs(result, brackets, n, opening, closing+1)
        brackets.pop()
        
    def generateParenthesisTopDown(self, n: int) -> List[str]:
        """
        n = 2

        ()(), (())
        ^

        Approach: Using BFS start with single brackets, trying all possible
                  permutations. Keep track of opening and closing variables
                  for balancing purposes.
        Time Complexity: O(2^N2) Generating all possible subsets of N brackets times 2
        Space Complexity O(2^N2)
        """
        result = []
        
        q = deque([(["("], 1, 0)])
        while q:
            brackets, opening, closing = q.popleft()
            if opening > n or closing > n: # unbalanced permutation
                continue
            if len(brackets) == n*2: # making sure the balance
                result.append("".join(brackets))
                continue
            q.append((brackets + ["("], opening+1, closing))
            if opening > closing: # making sure the balance
                q.append((brackets + [")"], opening, closing+1))
        return result