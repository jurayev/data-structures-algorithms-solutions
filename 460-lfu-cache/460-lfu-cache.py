class LRUCache:
    def __init__(self):
        self.cache = collections.OrderedDict()
        
    def put(self, key: int, value) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
    
    def evict(self) -> int:
        return self.cache.popitem(last=False)[0]
    
    def remove(self, key):
        return self.cache.pop(key, None)
        
    def is_empty(self,) -> bool:
        return len(self.cache) == 0
    
class LFUCache:
    """
    Time Complexity: O(1). Amortized for all operations
    Space Compelxity O(C * 3), C - is capacity, we store 3x our capacity to maintain LFU + LRU properties
    
    Test-Cases:
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
        
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[0],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
        
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[4],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
        
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[1],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
        
        ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
        [[0],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
        
        ["LFUCache","put","put","put", "get", "get", "get", "put", "get", "put", "get", "get", "put"]
        [[1],[1,1],[2,2],[3,3], [1], [3], [3], [4,4], [4], [1,1], [1], [1], [2,2]]
        
        ["LFUCache","put","put","put", "get", "get", "get", "put", "get", "put", "get", "get", "put"]
        [[3],[1,1],[2,2],[3,3], [1], [3], [3], [4,4], [4], [1,1], [1], [1], [2,2]]
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_counter = 1
        self.counters = collections.defaultdict(LRUCache)
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # remove key from curr counter
        value = self.remove(key)
        self.increment(key, value)
        return value
    
    def put(self, key: int, value: int) -> None:
        min_counter = self.min_counter
        
        # check if the new key
        if key not in self.cache:
            self.cache[key] = 1
            self.min_counter = 1
            self.counters[1].put(key, value)
        else:
            self.move(key, value)
        # handle capacity overflow
        if len(self.cache) > self.capacity:
            lru = self.counters[min_counter]
            key = lru.evict()
            if lru.is_empty():
                del self.counters[min_counter]
            self.cache.pop(key, None)

    def move(self, key, value):
        # remove key from current counter, removing from LRU
        self.remove(key)
        self.increment(key, value)
        
    def increment(self, key, value):
        self.cache[key] += 1
        counter = self.cache[key]
        # add new key to the counter
        lru = self.counters[counter]
        lru.put(key, value)
    
    def remove(self, key) -> int:
        # remove key from current counter, removing from LRU
        counter = self.cache[key]
        lru = self.counters[counter]
        value = lru.remove(key)
        if lru.is_empty():
            del self.counters[counter]
            self.min_counter = self.min_counter if self.min_counter != counter else counter + 1
        return value
                
        
"""
counters = {c1: LRu
            c2: LRU
            c3: LRU}
            
cache = {key1: c2,
         key2: c2,
         key3: c3}


["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2],        [1], [3, 3], [2],   [3], [4, 4], [1], [3], [4]]

counters = {c1: 2<->1
            c2: 2<->1
            c4: 1<->}
            
cache = {key1: c2,
         key3: c1,}
"""

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)