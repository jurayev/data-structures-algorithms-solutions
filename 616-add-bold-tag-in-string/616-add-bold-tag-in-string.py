class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        """  012345678
        s = "aaabbccam"
              s
                e
          
        bold_ranges = [[0,2],[1,3],[4,5]]
                       [0,5]
        
        Time O(N^2)
        Space O(N+M), M is the number of bold tags
        """
        
        words_set = set(words)
        n = len(s)
        intervals = []
        for start_idx in range(0, n):
            for end_idx in range(start_idx+1, n+1):
                word = s[start_idx:end_idx]
                if word in words_set:
                    intervals.append([start_idx, end_idx])          
        merged = self.merge(intervals)
        output = list(s)
        shifted_pos = 0
        start_tag = "<b>"
        end_tag = "</b>"
        """
        <b>aaabbc</b>c
        
        [[0,5]]
        """
        for start, end in merged:
            output.insert(start+shifted_pos, start_tag)
            shifted_pos += 1
            output.insert(end+shifted_pos, end_tag)
            shifted_pos += 1
            
        return "".join(output)
    
    def merge(self, intervals):
        """
        [[0,2],[1,3],[4,5]]
                      ^
        [[0,5]]
        """
        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
                
        return merged