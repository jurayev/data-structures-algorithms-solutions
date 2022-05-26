class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        makes: [1,5,7,10]
                      ^
        coding: [3,9,12]
                     ^
        
        """
        
        word1_idx = []
        word2_idx = []
        
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word1_idx.append(idx)
            elif word == word2:
                word2_idx.append(idx)
                
        
        idx1, idx2 = 0, 0
        min_dist = float("inf")
        while idx1 < len(word1_idx) or idx2 < len(word2_idx):
            num1 = word1_idx[idx1] if idx1 < len(word1_idx) else float("inf")
            num2 = word2_idx[idx2] if idx2 < len(word2_idx) else float("inf")
            
            min_dist = min(min_dist, abs(num1-num2))
            if num1 < num2:
                idx1 += 1
            else:
                idx2 += 1
        
        return min_dist