from heapq import *


class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        heap = []
        for battery in batteries:
            heappush(heap, -battery)
        summ = sum(batteries)
        while heap and -heap[0] > summ // n:
            summ -= -heappop(heap)
            n -= 1
        return summ // n