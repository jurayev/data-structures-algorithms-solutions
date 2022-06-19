class Leaderboard:
    """
    1: 0
    2: 3
    3: 6
        (score, id)
    top2 = [(5,1), (6,3)]
    
    
    
    """

    def __init__(self):
        self.scores = Counter()
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        scores = list(self.scores.values())
        heap = [scores[i] for i in range(0, K)]
        heapify(heap)
        for i in range(K, len(scores)):
            smallest = heappop(heap)
            heappush(heap, max(scores[i], smallest))
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)