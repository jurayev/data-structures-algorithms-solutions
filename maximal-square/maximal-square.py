class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Approach 1. Try to selec every possible square with all 1s in it
                    Time O(2^NM) - exponential time to exhaust all possible subsets
                    Space O(1)
        
        Apprach 2. Use dynamic programmin by reusing prev calculated results
                   Start with square == 1, then square == 2, square == n ....
                   reuse prev results
        
        [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]]
        
        [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","4","4"],
         ["1","0","1","4","9"]]
         
         
        [["1","1","1","1","0"],
         ["1","4","4","4","1"],
         ["1","4","9","9","1"],
         ["1","4","9","16","9"]]
         min_square = min()
         dp[i][j] += sqrt(dp[i][j-1]) + sqrt(dp[i-1][j]) + dp[i-1][j-1]
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[int(matrix[r][c]) for c in range(0, m)] for r in range(0, n)]
        
        max_square = 0
        for i in range(0, min(2, n)):
            for j in range(0, min(2, m)):
                max_square = max(max_square, dp[i][j])
                
        for i in range(1, n):
            for j in range(1, m):
                if not dp[i][j]: continue
                min_square = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                dp[i][j] += min_square + int(math.sqrt(min_square)) * 2
                max_square = max(max_square, dp[i][j])
        return max_square