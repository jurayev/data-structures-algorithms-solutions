from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
           0    1      2     3
        [[1,2],[2,4],[3,2],[4,1]]

           ^
        0 1 2 3 4 5 6
          0 0 0
            1 1 1 1 1
              2 2 2
                3 3

        max ts = 6



        """
        if not tasks:
            return []

        order = []  # [0]
        available = []  # [[2,4]]
        to_process = []  # [,,]
        # 0 1 2 3 4 5 6 7
        #           ^

        for i, task in enumerate(tasks):
            heappush(to_process, (task[0], task[1], i))

        ts = to_process[0][0]
        while to_process or available:
            while to_process and to_process[0][0] <= ts:
                start_ts, time, index = heappop(to_process)
                heappush(available, (time, index))

            if available:
                time, index = heappop(available)
                ts += time
                order.append(index)
            else:
                ts = to_process[0][0]
        return order