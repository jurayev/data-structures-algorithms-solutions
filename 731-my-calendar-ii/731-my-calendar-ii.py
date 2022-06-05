class MyCalendarTwo:
    """
    [(s,5)(s,10),(s,10),(e,15),(e,20),(e,40),(s,50),(e,60),]
    
    """
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))
        
        booked = 0
        for time, freq in self.calendar:
            booked += freq
            if booked == 3:
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)