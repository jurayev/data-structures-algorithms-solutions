import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.positions = defaultdict(set)         # {1:{0} , 2:1, 3:2}
        self.values = []            #. [1,2,3,1]
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        O(1)
        """
        index = len(self.values)
        self.values.append(val)
        if val in self.positions:
            self.positions[val].add(index)
            return False

        self.positions[val].add(index)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        O(1)
        """
        if val not in self.positions:
            return False
        
        index_to_swap = self.positions[val].pop() # 2 -> 1
        last_index = len(self.values)-1
        last_value = self.values.pop()
        if index_to_swap < last_index:
            self.values[index_to_swap] = last_value
            self.positions[last_value].remove(last_index)
            self.positions[last_value].add(index_to_swap)
            
       
        if len(self.positions[val]) == 0:
            self.positions.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        [1,2,3,4,5]
        O(1)
        """
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()