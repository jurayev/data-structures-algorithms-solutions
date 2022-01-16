class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        Q3 from Weekly contest 276
        Submission time: 0:51:37
        Time spent: 26 mins

        Approach:
            Go questions backward, saving the prev best results
        
        Complexity:
            Time: O(N)
            Space O(N)
        Examples:
           0      1     2    3     4    5   6   7   8
        [[1,1],[2,2],[3,3],[4,4],[5,5]]
           1     2      3     4     5
           4     7            5
        
        """
        n = len(questions)
        points = [questions[i][0] for i in range(n)]
        
        for idx in range(n-2, -1, -1):
            point, skip = questions[idx]
                
            next_idx = idx+skip+1
            # if next available question solved/exists, add to the current results
            if next_idx < n:
                points[idx] += points[next_idx]
            # choose to take or skip the current question
            points[idx] = max(points[idx], points[idx+1])
         
        return points[0]