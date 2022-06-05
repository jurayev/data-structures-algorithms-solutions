class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, 0))
            
        events.sort()
        
        balance = 0
        for time, event in events:
            if event == 1:
                if balance > 0:
                    return False
                balance += 1
            else:
                balance -= 1
                
        return True