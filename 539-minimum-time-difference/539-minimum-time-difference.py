class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        1h -> 60 min -> 3600 sec
        24 h -> 86400 sec
        24 h -> 1440 min
        
        
        [123, 123, 124]
        
        [1, 800, 1439]
        """
        
        # covert to minutes
        # sort all timestamps
        # substruct two adjacents ts keeping the min
        # check the corner case ts[0] - ts[-1] 
        # 1 - 1439
        hour_to_minutes = 60
        day_to_minutes = 24 * hour_to_minutes
        ts = []
        for time in timePoints:
            in_minutes = 0
            hours, minutes = int(time[:2]), int(time[3:])
            in_minutes += minutes + hours * hour_to_minutes
            ts.append(in_minutes)
            
        ts.sort()
        min_time_diff = float("inf")
        for i in range(len(ts)-1):
            ts1, ts2 = ts[i], ts[i+1]
            min_time_diff = min(min_time_diff, ts2 - ts1)
            
        ts1, ts2 = ts[0], ts[-1]
        min_time_diff = min(min_time_diff, ts1 + day_to_minutes - ts2)
        return min_time_diff
        
        
        
        
        