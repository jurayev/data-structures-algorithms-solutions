class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,2],[2,3],[3,4],[1,3]
        
        [(1,s), (1,s), (2,e), (2, s), (3, e), (3, e), (3, s), (4,e)]
        
        """
        events = []
        for start, end in intervals:
            events.append((start, 0))
            events.append((end, 1))
        events.sort(key=lambda x: (x[1], x[0]))
        
        processed_events = []
        skipped_events = 0
        balance = 0
        start = 0
        for time, e_type in events:
            if balance > 0 and e_type == 0:
                skipped_events += 1
            balance += 1 if e_type.START else -1
        return skipped_events
        
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
            
            