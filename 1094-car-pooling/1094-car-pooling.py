class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        2
        
        [[2,1,5],[3,3,7]] capacity = 5
        
        1234567
        22222
          33333
        2255533
        
        1234 56 7
        2255 33 0
          3    -3
        """
        
        locations = [0] * 1001
        n = len(locations)
        for pas, start, end in trips:
            locations[start] += pas
            locations[end] -= pas
        max_capacity = locations[0]
        for i in range(1, n):
            locations[i] += locations[i-1]
            max_capacity = max(max_capacity, locations[i])

        return max_capacity <= capacity
            