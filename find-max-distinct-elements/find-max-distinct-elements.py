from heapq import *
from collections import Counter


def find_maximum_distinct_elements(nums, k):
    """
    [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5] k = 2

    1: 1
    2: 1
    3: 4
    4: 2
    5: 3

    [3, 5, 12, 11, 12]  k = 2
    """
    min_heap = []
    freq = Counter(nums)
    for num, count in freq.items():
        heappush(min_heap, count)
    distinct_count = 0
    while min_heap and k:
        count = heappop(min_heap)
        if count == 1:
            distinct_count += 1
        else:
            heappush(min_heap, count - 1)
            k -= 1
    return distinct_count - k


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
