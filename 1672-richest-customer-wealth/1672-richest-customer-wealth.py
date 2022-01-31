class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        best = 0
        for account in accounts:
            best = max(best, sum(account))

        return best
