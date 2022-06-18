class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.max_numbers = maxNumbers
        self.numbers = [True for _ in range(maxNumbers)]

    def get(self) -> int:
        for i in range(self.max_numbers):
            if self.numbers[i]:
                self.numbers[i] = False
                return i
        return -1

    def check(self, number: int) -> bool:
        return self.numbers[number]

    def release(self, number: int) -> None:
        self.numbers[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)