from heapq import heappush, heappop, heapify
class Item:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        
    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def maxSlidingWindow(self, nums, k):
        maxes = []
        deq = collections.deque([], maxlen=k)

        for idx, num in enumerate(nums):
            while deq and deq[0].index <= idx - k:
                deq.popleft()
            while deq and deq[-1].value <= num:
                deq.pop()

            deq.append(Item(num, idx))
            if idx - k + 1 >= 0:
                maxes.append(deq[0].value)
        return maxes

    def maxSlidingWindowHeap(self, nums: List[int], k: int) -> List[int]:
        start = 0
        window = []
        for end in range(0, k):
            heappush(window, Item(-nums[end], end))
        if not window:
            return []
        maxes = [-window[0].value]

        for end in range(k, len(nums)):
            heappush(window, Item(-nums[end], end))
            while window and window[0].index <= end - k:
                heappop(window)
            maxes.append(-window[0].value)
            
        return maxes
