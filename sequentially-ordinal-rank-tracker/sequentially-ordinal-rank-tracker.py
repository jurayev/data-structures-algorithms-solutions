from sortedcontainers import SortedList
from functools import cmp_to_key

class SORTracker:
    """
    time complexity:
        insert - O(logn)
        get     - O(logn)
    space complexity:
         O(n)
         
    ranking = [["branford", 3], ["bradford", 2], ]
    ranking[i] -> get the element from sorted BST
    
    """
    def __init__(self):
        self.calls_count = 0 # 0 #1 #
        self.locations = SortedList()  # [[3, "branford"], [2, "alps"]], # [[3, "branford"], [2,"alps"], [2, "bradford"]]

    def add(self, name: str, score: int) -> None:
        self.locations.add((-score, name))

    def get(self) -> str:
        location = self.locations[self.calls_count] # branford # alps
        self.calls_count += 1
        return location[1]
    
    


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()