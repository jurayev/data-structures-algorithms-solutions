import collections
from heapq import *


def sort_character_by_frequency(string):
    """
    "Programming"

    g: 2
    g_idx: 3
    r: 2
    r_idx: 1
    """
    freq = collections.Counter()
    indexes = {}
    n = len(string)
    for i in range(n - 1, -1, -1):
        freq[string[i]] += 1
        indexes[string[i]] = i
    heap = []
    for char, count in freq.items():
        heappush(heap, (-count, indexes[char], char * count))

    res = []
    while heap:
        res.append(heappop(heap)[2])
    return "".join(res)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
