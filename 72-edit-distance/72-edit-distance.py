class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        
        transitions: dist(i, j) = min(dist(i, j), dist(i+1, j), dist(i, j)) + 1
        base case: i >= n or j >= m -> 0
        
        "horse" "ros"
           i
                   j
        """ 
        n, m = len(word1), len(word2)
        
        @lru_cache(None)
        def dist(i, j):
            if i >= n and j >= m:
                return 0
            if i >= n or j >= m:
                return max(n-i, m-j)
            if word1[i] == word2[j]:
                return dist(i+1, j+1)

            min_dist = min(dist(i+1, j+1), dist(i+1, j), dist(i, j+1)) + 1
            return min_dist
        
        return dist(0, 0)
                