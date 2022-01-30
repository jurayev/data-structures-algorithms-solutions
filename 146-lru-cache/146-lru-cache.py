class ListNode:
    def __init__(self, key=0, value=0, prev_node=None, next_node=None):
        self.key = key
        self.value = value
        self.prev = prev_node
        self.next = next_node

        
class LinkedList:

    def __init__(self,):
        dummy = ListNode()
        self.head = dummy
        self.tail = dummy

    def evict(self,):
        #    head  <->  1 <-> 2
        evicted_node = self.head.next
        self.head.next = evicted_node.next
        if evicted_node.next:
            evicted_node.next.prev = self.head
        return evicted_node.key

    def move_to_end(self, node):
        #    prev  <->   next
        #    head  <->  1 <-> 2 <-> 3
        if node == self.tail:
            return
        next_node = node.next
        prev_node = node.prev
        if next_node and prev_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        self.tail.next = None
        node = self.head
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = LinkedList()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.list.move_to_end(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = ListNode(key, value)
        node = self.cache[key]
        node.value = value
        self.list.move_to_end(node)
        
        if self.capacity < len(self.cache):
            key = self.list.evict()
            del self.cache[key]
            
"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],       [1,1],[2,2],  [1],[3,3],  [2], [4,4],[1],  [3],[4]]

list -> <-> 2 <-> 1 <-> 3
{1:1,
 2: 2,
 3: 3}

"""


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)