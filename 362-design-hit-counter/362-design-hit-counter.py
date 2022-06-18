class HitCounter:

    def __init__(self, interval=300):
        self.interval = interval
        self.hits = Counter()
        self.timestamps = deque([])
        self.total_hits = 0
        

    def hit(self, timestamp: int) -> None:
        self.cleanup(timestamp)
        if not self.timestamps or self.timestamps[-1] != timestamp:
            self.timestamps.append(timestamp)
            
        self.hits[timestamp] += 1
        self.total_hits += 1
        

    def getHits(self, timestamp: int) -> int:
        self.cleanup(timestamp)
        return self.total_hits
    
    def cleanup(self, timestamp):
        
        while self.timestamps and self.timestamps[0] <= timestamp - self.interval:
            removed_timestamp = self.timestamps.popleft()
            self.total_hits -= self.hits[removed_timestamp]
            del self.hits[removed_timestamp]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)