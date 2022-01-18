class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        BottomUp approach
        Time Complexity O(N*M)
        Space Complexity O(N*M)
        """
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        
        
    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        """
        text1 = "abcde", text2 = "ace"
            "ace"
        ""   000
        "a"  111
        "b"  111
        "c"  122
        "e"  123
        "e"  123
        
        dp[i-1][j-1] + 1 or dp[i-1][j]
        """
        @functools.lru_cache(maxsize=None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            
            return max(dp(i-1, j), dp(i, j-1))
            
        return dp(len(text1)-1, len(text2)-1)