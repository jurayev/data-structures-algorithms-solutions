class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [[0,30],[5,10],[15,20]]
        
        """
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, 0))
            
        events.sort()
        
        balance = 0
        max_balance = 0
        for time, event in events:
            if event == 1:
                balance += 1
            else:
                balance -= 1
            max_balance = max(max_balance, balance)
                
        return max_balance