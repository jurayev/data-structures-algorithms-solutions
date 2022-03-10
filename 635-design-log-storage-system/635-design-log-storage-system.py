from bisect import insort, bisect_left, bisect_right
class LogSystem:

    def __init__(self):
        self.logs = []
        self.mappings = {"Year": 4, 
                         "Month": 7,
                        "Day": 10,
                        "Hour": 13,
                        "Minute": 16,
                        "Second": 19}

    def put(self, ts_id: int, timestamp: str) -> None:
        insort(self.logs, (timestamp, ts_id))
        # insort(self.ss_logs, (timestamp[:19], ts_id))
        # insort(self.ms_logs, (timestamp[:16], ts_id))
        # insort(self.hh_logs, (timestamp[:13], ts_id))
        # insort(self.dd_logs, (timestamp[:10], ts_id))
        # insort(self.mm_logs, (timestamp[:7], ts_id))
        # insort(self.yy_logs, (timestamp[:4], ts_id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        size = self.mappings[granularity]
        
        leftmost_idx = bisect_left(self.logs, start[:size], key = lambda x: x[0][:size])
        rightmost_idx = bisect_right(self.logs, end[:size], key = lambda x: x[0][:size])
        range_ids = []
        # print(self.logs)
        # print(leftmost_idx, rightmost_idx)
        for i in range(leftmost_idx, rightmost_idx):
            ts, ts_id = self.logs[i]
            range_ids.append(ts_id)
        return range_ids

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)