class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
           12     5     7       1       1
        [(0,1), (3,2), (5,1), (8,4), (10,2)]
                                ^
                                        ^
        
        12
        10 2, 1h
        
        
        stack = [1,1,5]
        
        10
        [0,4,2]
        [2,1,3]
         5 6 2
         
         [5,2,6]
        """
        
        times = []
        
        for idx in range(len(position)):
            car_pos, car_speed = position[idx], speed[idx]
            time = (target - car_pos) / car_speed
            times.append((car_pos, time))
            
        times.sort()
        fleet = []
        
        for pos, time in times:
            
            while fleet and fleet[-1] <= time:
                fleet.pop()
            
            fleet.append(time)
            
        return len(fleet)