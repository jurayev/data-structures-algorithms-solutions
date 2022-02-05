class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
        
        