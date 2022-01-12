from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        """
    [3, 1, 5, 12, 2, 11]  K = 4

    [3, 1, 5, 12, 2, 11]
    [11,12,13,6]
    """
        self.k = k
        self.top_k = []

        for i in range(k):
            heappush(self.top_k, nums[i])

        for j in range(i + 1, len(nums)):
            el = max(heappop(self.top_k), nums[j])
            heappush(self.top_k, el)

    def add(self, num):
        el = max(heappop(self.top_k), num)
        heappush(self.top_k, el)
        return self.top_k[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
