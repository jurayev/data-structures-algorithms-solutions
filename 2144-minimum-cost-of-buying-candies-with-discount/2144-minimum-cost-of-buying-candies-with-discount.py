from heapq import heappush, heappop

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        [5]
        """
        heap = []
        for c in cost:
            heappush(heap, -c)
        total = 0
        while len(heap) > 2:
            cost1 = -heappop(heap)
            cost2 = -heappop(heap)
            free = heappop(heap)
            total += cost1 + cost2
        
        return total + sum([-cost1 for cost1 in heap])