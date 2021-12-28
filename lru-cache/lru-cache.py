from collections import OrderedDict

class ListNode():
    def __init__(self, key=0, val=0, _prev=None, _next=None):
        self.key = key
        self.val = val
        self.prev = _prev
        self.next = _next

class DoublyLinkedList():
    
    def __init__(self,):
        self.sentinel = ListNode() # used to reduce the overhead with initial state when 
        self.head = self.sentinel   
        self.tail = self.sentinel    
        self.len = 0                
    
    def append(self, key, val) -> ListNode:
        self.tail.next = ListNode(key, val, _prev=self.tail)
        self.tail = self.tail.next
        self.len += 1
        return self.tail
    
    def print(self, node):
        print(None, end="")
        while node:
            print(" <-> ", node.val, end="")
            node = node.next
        print(" <-> ", None, end="")
        print()
    
    def move_to_end(self, node: ListNode) -> None:
        if not node.next:
            return
        prev = node.prev
        _next = node.next
        
        # move to end
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = self.tail.next
        
        # link prev with next
        prev.next = _next
        _next.prev = prev
        
    def evict(self, ) -> int:
        if self.len < 1:
            return -1
        evicted_key = self.head.next.key
        # remove head node, actual head is a sentinel node, so head.next gets removed
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        if self.len == 1: # remove tail pointer
            self.tail = self.tail.prev
            self.tail.next = None
        self.len -= 1
        return evicted_key
    
class LRUCache:
    """
    This is the Doubly LinkedList with HashMap implementation
    
    Examples:
            
        ["LRUCache","put","put","put", "get", "get", "get", "put", "get", "put", "get", "get", "put"]
        [[1],[1,1],[2,2],[3,3], [1], [3], [3], [4,4], [4], [1,1], [1], [1], [2,2]]

    Time Complexity:
        get -> O(1)
        put -> O(1)
    Space Complexity:
        O(N) where N is the capacity size
    """
    def __init__(self, capacity: int):
        self.cache = {}                # for storing nodes
        self.list = DoublyLinkedList() # keep track of eviction and ordering of nodes
        self.max_len = capacity

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self.list.move_to_end(node)
        return -1 if not node else node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.list.move_to_end(node)
            return
        node = self.list.append(key, value)
        self.cache[key] = node
        if self.list.len > self.max_len:
            evicted_key = self.list.evict()
            self.cache.pop(evicted_key)
        assert(len(self.cache) == self.list.len)

class LRUCacheOrderedDict:
    """
    This is the OrderedDict built-in datastructure implementation

    Time Complexity:
        get -> O(1)
        put -> O(1)
    Space Complexity:
        O(N) where N is the capacity size
    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.len = 0
        self.max_len = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if value:
            self.cache.move_to_end(key)
        return -1 if not value else value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        self.cache[key] = value
        self.len += 1
        # check if eviction is required
        if self.len > self.max_len:
            self.cache.popitem(last=False) # remove a pair from the start of List
            self.len -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)