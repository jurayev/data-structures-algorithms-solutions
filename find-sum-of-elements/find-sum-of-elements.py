from heapq import *

def find_sum_of_elements(nums, k1, k2):
    """
     0  1  2   3. 4.   5
    [1, 3, 5, 11, 12, 15]. k1 = 3, k2=6

    [1,3,5]
    [15]
    [1, 3, 12, 5, 15, 11]
    """
    heap = nums[:]
    heapify(heap)
    output = 0
    for i in range(0, k2 - 1):
        val = heappop(heap)
        if i >= k1:
            output += val

    return output


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
