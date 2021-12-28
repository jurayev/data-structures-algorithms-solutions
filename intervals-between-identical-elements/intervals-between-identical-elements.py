class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        Approach:
            1. Calculate prefix sum for the same values
            2. Calculate suffix sum for the same values
            3. Sum up the prefix and the suffix value for i 
        Examples:
            [0,0,0,0,0,0,0]

            seen =
            {
            2: [0, 4]
            1: [1, 3]
            3: [2,5,6]
            }
             0 1 2 3 4 5 6 7
            [2,1,3,1,2,3,3,3]
                 ^
             0 1 2 3 4 5 6
            [0,0,0,2,4,3,5,7]
            [4,2,7,0,0,1,0]



            [4,2,7,2,4,4,5]

             0 1 2 3
            [2,2,2,2]
            [6,3,3,6]

        Complexity:
            Time O(N)
            Space O(N)
        """
        
        seen = {}
        n = len(arr)
        # prefix sum
        dist = [0 for i in range(n)]
        for i in range(n):
            num = arr[i]
            if num in seen:
                last_idx, prev_count = seen[num]
                dist[i] += dist[last_idx] + (abs(i - last_idx) * prev_count)
                seen[num] = [i, prev_count+1]
            else:
                seen[num] = [i, 1]
        # suffix sum
        seen = {}
        dist_rev = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            num = arr[i]
            if num in seen:
                last_idx, prev_count = seen[num]
                dist_rev[i] += dist_rev[last_idx] + (abs(i - last_idx) * prev_count)
                seen[num] = [i, prev_count+1]
            else:
                seen[num] = [i, 1]
        # sum up prefix[i] and suffix[i]
        return [d1+d2 for d1, d2 in zip(dist, dist_rev)]