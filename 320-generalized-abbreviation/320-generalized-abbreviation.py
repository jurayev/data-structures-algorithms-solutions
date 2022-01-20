from collections import deque

class Solution:
    def generateAbbreviationDSF(self, word: str) -> List[str]:
        result = []
        self.dfs(word, 0, "", result)
        return result
    
    def dfs(self, word, i, string, result):
        if len(string) >= len(word):
            abbreviated = self.create_string(string)
            result.append(abbreviated)
            return
        
        self.dfs(word, i+1, string+"_", result)
        self.dfs(word, i+1, string+word[i], result)
    
    def generateAbbreviations(self, word: str) -> List[str]:
        """
        Approach:
            Using BFS try to generate all possible subsets.
            For every new word skip adding next char, and add next char.
            use underscore to denote char skip.
            At the last, count continious underscores and convert to number
            
        Time O(2^N)
        Space O(2^N)
        
        Example:
        "BAT"
        ^
        ""
        "_" B
        __ _A B_ BA
        ___ __T _A_ _AT B__ B_T BA_ BAT   
        """
        result = []
        q = deque([("", 0)])

        while q:
            string, index = q.popleft()
            if len(string) >= len(word):
                result.append(self.create_string(string))
                continue

            q.append((string+"_", index+1))
            q.append((string+word[index], index+1))
        return result

    def create_string(self, string):
        str_result = []
        count = 0
        for char in string+" ":
            if char == "_":
                count += 1
                continue
            if count:
                str_result.append(str(count))
                count = 0
            str_result.append(char.strip())

        return "".join(str_result) 