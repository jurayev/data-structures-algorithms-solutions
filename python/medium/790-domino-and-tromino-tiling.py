class Solution:
    def numTilings(self, n: int) -> int:
        """

        1: 1

        2: 2

        3: 5 , 3 dominos, 2 tromino


        4: 11

        5: 24

        6: 53

        7: 106 + 11

        TC O(N)
        SC O(N)

        """

        dp = [0 for _ in range(max(n + 1, 4))]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]
        return dp[n] % (10 ** 9 + 7)