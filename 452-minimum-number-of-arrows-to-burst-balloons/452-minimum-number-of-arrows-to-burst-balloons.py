class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Approach:
            Sort and merge overlapping intervals

        Time complexity O(nlogn)
        Space complexity O(n)

        Test-Cases
        [[10,16],[2,8],[1,6],[7,12]]
        
        [[1,6], [2,5], [6,12], [6,16]]
                                 ^
        [[10,16],[2,8],[1,6],[7,12]]
        [[1,6], [2,8], [6,12], [6,16]]
        [[1,6], [2,8], [6,12], [7,16]]
        [[1,6], [2,5], [6,12], [6,16]]
        [[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]]
        [[1,44],[3,5],[4,45]]
        [[1,55]]
        [[1,44],[10,11],[10,45]]
        """
        s_points = sorted(points, key=lambda x: (x[0], x[1])) 
        
        bursted = []
        
        for start, end in s_points:
            if bursted and start <= bursted[-1][1]:
                bursted[-1][0] = min(bursted[-1][0], start)
                bursted[-1][1] = min(bursted[-1][1], end)
            else:
                bursted.append([start, end])

        return len(bursted)