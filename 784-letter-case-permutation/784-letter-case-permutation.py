class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Time complexity O(N!) - factorial time need to generate all permutations
        Space complexity O(N!)
        
        Approach:
            Using BFS generate new permutations by append one more char to all previous generated permutations
        """
        permutations = []
        if not s:
            return permutations

        q = deque([""])
        while q:
            curr_string = q.popleft()
            n = len(curr_string)
            if n == len(s):
                permutations.append(curr_string)
                continue

            q.append(curr_string + s[n])
            if s[n].isalpha():
                q.append(curr_string + s[n].swapcase())
        return permutations