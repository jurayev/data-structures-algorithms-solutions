class Event:
    def __init__(self, time, event_type):
        self.time = time
        self.type = event_type
        
class Type:
    START = 0
    END = 1
    
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1, 3
        
        2,2
        
        [1]
        """
        new_start, new_end = newInterval
        events = [Event(new_start, Type.START), Event(new_end, Type.END)]
        for start_time, end_time in intervals:
            events.append(Event(start_time, Type.START))
            events.append(Event(end_time, Type.END))
            
        events.sort(key=lambda e: (e.time, e.type))
        balance = 0
        start_time = 0
        merged_events = []
        # Scan line
        for event in events:
            if balance == 0:
                start_time = event.time
            balance += 1 if event.type == Type.START else -1
            if balance == 0:
                merged_events.append([start_time, event.time])
        return merged_events
    
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Solution using scan line algo:
            Time O(N)
            Space O(N)
         
         [1,2] [3,10], [12,16]
         
         [1, 2, 6] 
                ^
         [3, 5, 9]
                ^
          [1,5] [6, 9]
        """
        
        start_events = []
        end_events = []
        for start, end in intervals + [[float(inf), float(inf)]]:
            if start > newInterval[0]:
                start_events.append(newInterval[0])
                newInterval[0] = float(inf)
            if end > newInterval[1]:
                end_events.append(newInterval[1])
                newInterval[1] = float(inf)
            if start < float(inf):
                start_events.append(start)
                end_events.append(end)

        merged_events = []
        start_idx, end_idx = 0, 0
        while start_idx < len(start_events):
            start_event = start_events[start_idx]
            end_event = end_events[end_idx]
            start_idx += 1
            if not merged_events:
                merged_events.append([start_event, end_event])
                continue
            end_idx += 1
            end_event = end_events[end_idx]
            if start_event <= end_events[end_idx-1]:
                merged_events[-1][1] = end_event
            else:
                merged_events.append([start_event, end_event])

        return merged_events
            
        