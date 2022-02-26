class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        
        transitions: dist(i, j) = min(dist(i, j), dist(i+1, j), dist(i, j)) + 1
        base case: i >= n or j >= m -> 0
        
        "horse" "ros"
           i
                   j
                   
        0x
        xx
        abcd
      ""23210
      ""12210
       a01210   2x4  
       b10110
        00000
        
          b c
        0 1 2
       a1 1 2
       b2 1 2
        
        Time O(N*N), where N is the max of (len1, len2)
        Space O(N*N), where N is the max of (len1, len2)
        """ 
        n, m = len(word1), len(word2)
        dp = [[0 for i in range(m+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        return dp[n][m]
    
    def minDistanceRec(self, word1, word2):
        """
        Time O(N*M)
        Space O(N*M)
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
                