class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Time O(N)
        Space O(N)
        
        """
        hour_to_minutes = 60
        day_to_minutes = 24 * hour_to_minutes
        buckets = [0] * (day_to_minutes + 1)
        for time in timePoints:
            in_minutes = 0
            hours, minutes = int(time[:2]), int(time[3:])
            in_minutes += minutes + hours * hour_to_minutes
            buckets[in_minutes] += 1
            
        ts = []
        for time, count in enumerate(buckets):
            times = [time] * count
            ts = ts + times
        
        min_time_diff = ts[0] + day_to_minutes - ts[-1]
        for i in range(len(ts)-1):
            ts1, ts2 = ts[i], ts[i+1]
            min_time_diff = min(min_time_diff, ts2 - ts1)
            
        return min_time_diff
    
    def findMinDifference1(self, timePoints: List[str]) -> int:
        """
        Time O(N log N)
        Space O(N)
        
        1h -> 60 min -> 3600 sec
        24 h -> 86400 sec
        24 h -> 1440 min
        
        
        [123, 123, 124]
        
        [1, 800, 1439]
        """
        
        # covert to minutes
        # sort all timestamps
        # substruct two adjacents ts keeping the min
        # check the corner case 1440 + ts[0] - ts[-1] 
        # 
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
        
        
        
        
        