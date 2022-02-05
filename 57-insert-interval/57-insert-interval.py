class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
            
        