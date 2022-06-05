class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))
        
        booked = 0
        for time, freq in self.calendar:
            booked += freq
            if booked == 2:
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                return False
        return True


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class Tree:
    def __init__(self,):
        self.root = None
        
    def insert(self, root, start, end):
        if not root:
            self.root = Node(start, end)
            return True
        
        if root.start >= end:
            if root.left:
                return self.insert(root.left, start, end)
            else:
                root.left = Node(start, end)
                return True
        elif root.end <= start:
            if root.right:
                return self.insert(root.right, start, end)
            else:
                root.right = Node(start, end)
                return True
        else:
            return False
        
class _MyCalendar:
    """[20,25]
    
           [10,20]
           
                    [25, 30]
    
                [20,25]
    """
    def __init__(self):
        self.tree = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.tree.insert(self.tree.root, start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)