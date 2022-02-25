class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        [[5,4],[6,4],[6,7],[2,3]]
        
        [2,5,4,5,5,6,7,1,8,3]
         1 2 2 3 3 4 5 1 6 7
                         i
        [1,3,5,6,7,8]
        Optimize with memo O(N^2)
        
        Total Time O(N^2) TLE
        """
        s_envelopes = sorted(envelopes, key=lambda env: (env[0], -env[1]))
        included_envelopes = []
        for _, height in s_envelopes:
            insert_index = bisect.bisect_left(included_envelopes, height)
            #print(included_envelopes, insert_index, height)
            if insert_index >= len(included_envelopes):
                included_envelopes.append(height)
            else:
                included_envelopes[insert_index] = height
        return len(included_envelopes)
        
    
    def dp(self, envelopes):
        """
        [[5,4],[6,4],[6,7],[2,3]]
        
        [[2,3], [5,4], [6,7] [6,4]]  -> LIS
           ^      ^             ^
           1      2      2      3   -> bottom up
           3      2      1      1   -> top down
                                i
                  j
        [2,5,6,6,6,7,8,8,9]
         1 2 3 3 3 4 5 5 6
        subproblem -> env(i) 
        
        Sorting O(NlogN)
        Try all envelopes O(2^n)
        
        Optimize with memo O(N^2)
        
        Total Time O(N^2) TLE
        """
        if not envelopes: return 0
        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = [1] * n
        max_envelope = 1
        for i in range(1, n):
            larger_w, larger_h = sorted_envelopes[i]
            for j in range(0, i):
                smaller_w, smaller_h = sorted_envelopes[j]
                if smaller_h < larger_h:
                    dp[i] = max(dp[i], dp[j]+1)
            max_envelope = max(max_envelope, dp[i])
        return max_envelope
        