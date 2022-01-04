def search_min_diff_element(arr, key):
    n = len(arr)
    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return arr[mid]
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    start_val = arr[start] if start < n else float("inf")
    end_val = arr[end] if end >= 0 else float("inf")
    if abs(start_val - key) < abs(end_val - key):
        return start_val
    return end_val


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([1, 3, 8, 10, 15], 13))
    print(search_min_diff_element([4, 6, 10], 17))
    print(search_min_diff_element([3, 6, 10], 2))


main()
