def search_bitonic_array(arr, key):
    """
    TIME COMPLEXITY O(LOGN) + O(LOGN) + O(LOGN)
    SPACE COMPLEXITY O(1)
    """
    max_idx = search_max_idx(arr)

    left_idx = search(arr, 0, max_idx, key)
    right_idx = search(arr, max_idx, len(arr) - 1, key)
    return max(left_idx, right_idx)


def search_max_idx(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


def search(arr, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if arr[start] <= arr[mid]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
