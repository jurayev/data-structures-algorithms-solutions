class ATM:

    def __init__(self):
        self.banknotes_nominations = {0: 20,
                                     1: 50,
                                     2: 100,
                                     3: 200,
                                     4: 500}
        self.bank = [0, 0, 0, 0, 0]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, count in enumerate(banknotesCount):
            self.bank[idx] += count * self.banknotes_nominations[idx]

    def withdraw(self, amount: int) -> List[int]:
        counts = [0, 0, 0, 0, 0]
        for idx in range(len(self.bank)-1, -1, -1):
            nomination = self.banknotes_nominations[idx]
            count = min(self.bank[idx]//nomination, amount//nomination)
            amount -= nomination*count
            counts[idx] += count
        if amount == 0:
            for idx, count in enumerate(counts):
                self.bank[idx] -= self.banknotes_nominations[idx]*count
            return counts
        return [-1]
        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)