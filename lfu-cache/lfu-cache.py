class LRUCache:
    def __init__(self):
        self.cache = collections.OrderedDict()
        self.placeholder = "*"
        
    def put(self, key: int) -> None:
        self.cache[key] = self.placeholder
        self.cache.move_to_end(key)
    
    def evict(self) -> int:
        return self.cache.popitem(last=False)[0]
    
    def pop(self, key):
        self.cache.pop(key)
        
    def is_empty(self,) -> bool:
        return len(self.cache) == 0

class ListNode:
    def __init__(self, val=0, _prev=None, _next=None):
        self.val = val
        self.prev = _prev
        self.next = _next

class LinkedList:
    def __init__(self,):
        self.head = ListNode()
        
    def append(self,) -> ListNode:
        return self.get_next(self.head)
    
    def get_next(self, node) -> ListNode:
        if node.next and node.val+1 == node.next.val:
            return node.next
        node.next = ListNode(node.val+1, node, node.next)
        if node.next.next:
            node.next.next.prev = node.next
        return node.next
    
    def pop(self, ) -> ListNode:
        node = self.head.next
        self.remove(node)
        return node
    
    def remove(self, node):
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        if _next:
            _next.prev = _prev
    
    def peek(self, ) -> int:
        return self.head.next.val if self.head.next else -1
    
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
        self.counter_llist = LinkedList()                 # storing counters in list order -> [1 <-> 2 <-> 3 <-> 4]
        self.counters = collections.defaultdict(LRUCache) # storing counter: [keys] -> {1: [1,2,3], 2: [5, 6]}
        self.cache = {}                                   # storing key: [value, counter_node] -> {1: [1, ListNode(1), 2: [2, ListNode(2), 3: [4, ListNode(1)]}
        self.max_len = capacity
    
    def increment_counter(self, key) -> None:
        # increment counter and add value and counter to cache
        value, curr_counter_node = self.cache[key]
        counter = curr_counter_node.val
        next_counter_node = self.counter_llist.get_next(curr_counter_node)
        self.cache[key] = [value, next_counter_node]
        # add a key to incoremented counter (counter+1)
        self.counters[counter+1].put(key)
        
        # remove key from current counter
        self.counters[counter].pop(key)
        if self.counters[counter].is_empty():
            # no more keys belong to the counter, remove it from linked list and from counters map
            self.counter_llist.remove(curr_counter_node)
            del self.counters[counter]
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # increment counter and add value and counter to cache
        self.increment_counter(key)
        value, _ =  self.cache[key]
        return value

    def put(self, key: int, value: int) -> None:
        if self.max_len < 1: return # check for corner case
        
        if key in self.cache:
            # update value in cache and increment counter
            _, curr_counter_node = self.cache[key]
            self.cache[key] = [value, curr_counter_node]
            self.increment_counter(key)
            return 
        
        # check capacity overflow and evict LFU key
        if len(self.cache)+1 > self.max_len:
            candidate_counter = self.counter_llist.peek()
            evicted_key = self.counters[candidate_counter].evict()

            self.cache.pop(evicted_key)
            if self.counters[candidate_counter].is_empty():
                # removing LFU counter
                self.counter_llist.pop()
                del self.counters[candidate_counter]
        # add new key
        counter = 1
        counter_node = self.counter_llist.append()
        self.cache[key] = (value, counter_node)
        self.counters[counter].put(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)