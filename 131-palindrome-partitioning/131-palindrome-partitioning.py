class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        |aab
            a|ab
                a|a|b -> add
                    
        a|ab
        a
         a
          b
        """
        answer = []
        def backtrack(start_idx, candidates):
            if start_idx >= len(s):
                answer.append(list(candidates))
                return
            
            for end_idx in range(start_idx, len(s)):
                if s[start_idx: end_idx+1] == s[start_idx: end_idx+1][::-1]:
                    candidates.append(s[start_idx: end_idx+1])
                    backtrack(end_idx+1, candidates)
                    candidates.pop()
                    
                    
        backtrack(0, [])
        return answer