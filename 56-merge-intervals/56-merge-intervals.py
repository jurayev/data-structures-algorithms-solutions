class Event:
    def __init__(self, time, event_type):
        self.time = time
        self.type = event_type
        
    def __lt__(self, other):
        if self.time == other.time:
            return self.type < other.type
        return self.time < other.time
        
class Type:
    START = 0
    END = 1

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sweep Line Algo
        Time O(N log N)
        Space O(N)
        
        Test-cases:
            [[1,3],[2,6],[8,10],[15,18]]
            [[1,4],[4,5]]
            [[1,3],[2,6],[6,10],[9,18]]
            [[1,4],[0,0]]
            [[2,3],[4,5],[6,7],[8,9],[1,10]]
            [[1,1]]
            
        Dry run:
            [1,3], [2,6] [8,10] [15, 18]
            balance = 0
            start = 0

            [(1,s), (2,s), (3,e), (6, e), (8, s), (10,e), (15,s), (18, e)]
              ^
        """
        
        events = []
        for interval in intervals:
            events.append(Event(interval[0], Type.START))
            events.append(Event(interval[1], Type.END))
        
        events.sort()
        merged_events = []
        start = 0
        balance = 0

        for event in events:
            if balance == 0:
                start = event.time
            if event.type == Type.START:
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                merged_events.append([start, event.time])
            
            
        return merged_events
    
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,2,8,15]
                ^
        
        [3,6,10,18]
              ^
         
         [1,6] [8,10] []
        
        1. Solve by merging overlapping intervals
        2. Solve using scan line: 
            put all start and end separately
            sort both events
        Time O(N log N)
        Space O(N)
        """
        
        start_events = sorted([event[0] for event in intervals])
        end_events = sorted([event[1] for event in intervals])
        
        merged_events = []
        
        start_idx, end_idx = 0, 0
        
        while start_idx < len(start_events):
            start = start_events[start_idx]
            end = end_events[end_idx]
            if not merged_events:
                merged_events.append([start, end])
            elif start <= end:
                end_idx += 1
                end = end_events[end_idx]
                merged_events[-1][1] = end
            else:
                end_idx += 1
                end = end_events[end_idx]
                merged_events.append([start, end])
            start_idx += 1
            
        return merged_events
        
        