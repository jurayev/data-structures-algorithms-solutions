class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        i - customer
        j - bank

        [[1,5],
        [7,3],
        [3,5]]
        """
        best = 0
        for account in accounts:
            best = max(best, sum(account))

        return best
