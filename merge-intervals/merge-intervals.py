class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: 
            1. Sort the intervals by start time
            2. Add every interval to the new array
            3. If curr interval ovelaps with the last one, merge them
                - two intervals overlaps if start_i <= end_j and start_j <= end_i
            4. Repeat step 2
        
        Time Complexity O(nlogn) + O(N) ~ O(nlogn)
        Space Complexity O(N) - for new sorted arr
        """
        
        s_intervals = sorted(intervals)
        
        merged_intervals = []
        
        for start, end in s_intervals:
            prev_start, prev_end = merged_intervals[-1] if merged_intervals else (float(-inf), float(-inf))
            
            if merged_intervals and prev_start <= end and start <= prev_end:
                new_start = min(start, prev_start)
                new_end = max(end, prev_end)
                merged_intervals[-1][0] = new_start
                merged_intervals[-1][1] = new_end
            else:
                merged_intervals.append([start, end])
        return merged_intervals