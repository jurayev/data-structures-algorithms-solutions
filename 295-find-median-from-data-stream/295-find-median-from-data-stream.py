from heapq import heappush, heappop, heappushpop
from sortedcontainers import SortedList

class MedianFinder1:
    """ 
    Time O(N log N)
    Space O(N)
    
    Test-case:
            ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
    [[],[1],[2],[],[3],[],[-3],[],[-3],[],[-3],[],[0],[],[-1],[],[-10],[],[4],[],[-1],[]]
    """ 
    def __init__(self):
        self.elements = SortedList() # B-tree, most operations O(log N)
                                

    def addNum(self, num):  # O(log N)
        self.elements.add(num)
            
    def findMedian(self): # O(1) because mid element is always a root element of B-tree
        mid_idx = len(self.elements) // 2
        if len(self.elements) % 2 == 0:
            return (self.elements[mid_idx-1] + self.elements[mid_idx]) / 2

        return self.elements[mid_idx]
    
class MedianFinder:
    """
    Time O(N log N)
    Space O(N)
    """ 
    def __init__(self):
        self.max_elements = [] # min heap # [2,3]  -> 
        self.min_elements = [] # max heap # [-1,-2] ->
                                

    def addNum(self, num):  # O(log N)
        if len(self.max_elements) == len(self.min_elements):
            heappush(self.min_elements, -num)
            max_value = -heappop(self.min_elements)
            heappush(self.max_elements, max_value)
        else:
            heappush(self.max_elements, num)
            min_value = -heappop(self.max_elements)
            heappush(self.min_elements, min_value)
            
    def findMedian(self): # O(1)
        if len(self.max_elements) == len(self.min_elements):
            return (self.max_elements[0] + (-self.min_elements[0])) / 2
        return self.max_elements[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()