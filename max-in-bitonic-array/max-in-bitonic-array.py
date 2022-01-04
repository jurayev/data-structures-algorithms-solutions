def find_max_in_bitonic_array(arr):
    n = len(arr)
    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2
        mid_left = arr[mid - 1] if mid - 1 >= 0 else float("-inf")
        mid_val = arr[mid]
        mid_right = arr[mid + 1] if mid + 1 < n else float("-inf")
        if mid_left <= mid_val >= mid_right:
            return mid_val
        if mid_left < mid_val:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
