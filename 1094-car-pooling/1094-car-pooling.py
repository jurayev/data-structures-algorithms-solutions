class Solution:
    """
    23:55
    00:30
    
    
    [[2,1,5], [3,3,7]], capacity = 4  => false
      
      
      [[5,1,7]]
      0 1 2 3 4 5 6 7
        ^       ^
            ^       ^
            
     0  2 2 5 5 5  3 3 
     0  2 2 5 5 5  3 3 0
     
     0 1 2 3  4 5 6 7
       ^   ^
           ^        ^
     0 2 0 1  0 0 0 -3
     
     sol 1. prefix sums from ranges => max would give the right answer - TC O(N*trips num)
     sol 2. merge overlapping intervals 0 => max passanger - TC O(nlogn)
     sol 3. prefix sums from ranges in constant time => max would give the right answer - TC O(2*(trips num) + N asmax range)
    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_km = 0
        max_km = trips[-1][2]+1 if trips else 0
        
        for passanger, start, end in trips:
            max_km = max(max_km, end+1)
            
        passangers_in_trip = [0 for _ in range(min_km, max_km)]
        for passanger, start, end in trips:
            passangers_in_trip[start] += passanger
            passangers_in_trip[end] -= passanger
        
        max_capacity = 0
        for i in range(1, max_km):
            passangers_in_trip[i] += passangers_in_trip[i-1]
            max_capacity = max(max_capacity, passangers_in_trip[i-1])
            
        return max_capacity <= capacity