class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Complexity:
            Time O(n log n)
            Space O(n)
        """
        result = sticks[:]
        total = 0
        heapq.heapify(result)
        while len(result) > 1:
            num1 = heapq.heappop(result)
            num2 = heapq.heappop(result)
            total += num1 + num2
            heapq.heappush(result, num1+num2)
        return total
        