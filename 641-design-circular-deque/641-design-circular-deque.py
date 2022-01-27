class MyCircularDeque:
    """
    max_size = 4
    deque = [1,0,3,2]
               f  
           b
           
    All operations O(1)
    """
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.deque = [-1 for _ in range(k)]
        self.front = 1
        self.back = -1
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1

        self.front = (self.front - 1 + self.max_size) % self.max_size
        self.deque[self.front] = value
        if self.size == 1:
            self.back = self.front
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1

        self.back = (self.back + 1) % self.max_size
        self.deque[self.back] = value
        if self.size == 1:
            self.front = self.back
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        # if self.isEmpty():
        #     self.back = -1
        #     self.front = 1
        #     return True

        self.front = (self.front + 1) % self.max_size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        # if self.isEmpty():
        #     self.back = -1
        #     self.front = 1
        #     return True
        self.back = (self.back - 1 + self.max_size) % self.max_size
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.back]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
	    return self.size == self.max_size

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()