from heapq import heappush, heappop, heappushpop

"""
[3, 1, 5, 12, 2, 11]
                 ^ 
[11, 5, 12]

O(n log k)
"""


def find_k_largest_numbers(nums, k):
    result = []
    for num in nums:
        if len(result) >= k:
            heappushpop(result, num)
        else:
            heappush(result, num)
    return result


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
