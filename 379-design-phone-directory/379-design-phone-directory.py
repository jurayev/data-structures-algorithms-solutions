class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.free = deque([i for i in range(maxNumbers)])
        self.numbers = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        if not self.free:
            return -1
        reserved = self.free.popleft()
        self.numbers.remove(reserved)
        return reserved

    def check(self, number: int) -> bool:
        return number in self.numbers

    def release(self, number: int) -> None:
        if not self.check(number):
            self.numbers.add(number)
            self.free.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)