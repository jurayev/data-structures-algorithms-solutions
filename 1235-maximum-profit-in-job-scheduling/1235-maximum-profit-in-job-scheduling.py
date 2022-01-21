from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        """          0  1. 2. 3
        startTime = [1, 2, 3, 3], 
                              
        jobs      = [1,3,5] [2,4,1] [3,5,4] [3,6,7]
        
        dp =        [12,12,7,7]
        Time Complexity O(N log N)
        Space Complexity (N+M+K)
        """
        
        # sort by starting time
        jobs = [[startTime[i], endTime[i], profits[i]] for i in range(len(startTime))]
        jobs.sort(key=lambda x: (x[0], x[1], x[2]))
        start_time = sorted(startTime)
        n = len(start_time)
        dp = [0 for i in range(0, n)]
        
        # bin search on end times to find overlappings
        
        dp[n-1] = jobs[-1][2]
        
        for i in range(n-2, -1, -1):
            start, end, profit = jobs[i]
            next_idx = bisect_left(start_time, end)

            curr = 0
            if next_idx >= n:
                curr = profit
            else:
                curr = dp[next_idx] + profit   
            dp[i] = max(curr, dp[i+1])

        return dp[0]