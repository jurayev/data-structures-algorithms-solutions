class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        ["0:start:0","1:start:2","1:end:5","0:end:6"]
        
        ["0:start:0, "0:end:6"]
        """
        times = [0 for i in range(n)]
        
        stack = []
        for record in logs:
            log = Log(record)
            if log.is_start:
                stack.append(log)
            else:
                last_log = stack.pop()
                exec_time = (log.time - last_log.time + 1)
                times[last_log.id] += exec_time
                if stack:
                    func_id = stack[-1].id
                    times[func_id] -= exec_time
                
        return times
        

class Log:
    def __init__(self, log):
        _id, start_end, time = log.split(":")
        self.id = int(_id)
        self.is_start = start_end == "start"
        self.time = int(time)
        