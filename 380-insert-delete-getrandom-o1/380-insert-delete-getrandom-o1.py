class RandomizedSet:
    """
    Brute force:
    insert -> O(1)
    remove -> O(N) 
    getRandom -> O(1)

    Optimized:
    insert -> O(1)
    remove -> O(1) 
    getRandom -> O(1)

    store the value in hash map and array
    insert -> push to the hash map val:index and to the array
    remove -> get the index from hash map, remove from hash map, swap the last value with current, pop the last value from arr
    getrandom -> randint index and return the value
    """
    def __init__(self,):
        self.values_map = {}
        self.values = []

    def insert(self, value: int) -> bool:
        if value in self.values_map:
            return False
        index = len(self.values)
        self.values.append(value)
        self.values_map[value] = index
        return True

    def remove(self, value: int) -> bool:
        if value not in self.values_map:
            return False
        index = self.values_map.pop(value)

        last_value = self.values.pop()        
        if index < len(self.values):
            self.values[index] = last_value
            self.values_map[last_value] = index

        return True

    def getRandom(self,) -> int:
        if not self.values:
            return -1
        index = random.randint(0, len(self.values)-1)
        return self.values[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()