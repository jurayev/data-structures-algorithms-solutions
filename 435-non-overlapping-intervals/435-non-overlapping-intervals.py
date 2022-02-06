class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,2],[1,5],[2,3],[3,4]
        
        [1,2],[2,3],[3,4]
        
        """
        
        events = sorted(intervals, key=lambda x: x[1])
        
        processed_events = []
        skipped_events = 0
        for start, end in events:
            if processed_events and processed_events[-1][1] > start:
                skipped_events += 1
            else:
                processed_events.append([start, end])
                
        return skipped_events
            
            