class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Complexity:
            Time O(N)
            Space O(N)
        
        Approach:
            Keep merging the intervals and account for any interval where new interval can be inserted.
            Corner case when no insert postion is found, just append new_interval to the end
        Examples: 
            [[1,2],[3,5],[6,7],[8,10],[12,16]]      [0,0]
                ^


            i,j  i1, j1

            if j >= i1 and i <= j1

            i = min(i, i1)
            j = max(j, j1)


            [[1,2], [3,10], [12,16]]  []
        """
        new_interval = newInterval[:]
        
        merged_inter = []
        
        for idx, interval in enumerate(intervals):
            
            curr_start, curr_end = interval
            if not merged_inter:
                merged_inter.append(interval)
            
            curr_start, curr_end = merged_inter[-1]
            next_start, next_end = interval

            if curr_end >= next_start and curr_start <= next_end:
                merged_inter[-1][0] = min(curr_start, next_start)
                merged_inter[-1][1] = max(curr_end, next_end)
            else:
                merged_inter.append(interval)
                
            if new_interval:
                curr_start, curr_end = merged_inter[-1]
                next_start, next_end = new_interval
                
                if curr_end >= next_start and curr_start <= next_end:
                    merged_inter[-1][0] = min(curr_start, next_start)
                    merged_inter[-1][1] = max(curr_end, next_end)
                    new_interval = []
                elif next_end < curr_start:
                    last = merged_inter.pop()
                    merged_inter.append([next_start, next_end])
                    merged_inter.append(last)
                    new_interval = []
                    
        if new_interval:
            merged_inter.append(new_interval)
            
        return merged_inter
            