def find_range(arr, key):
    left_idx = get_leftmost_idx(arr, key)
    right_idx = get_rightmost_idx(arr, key)
    return [left_idx, right_idx]


def get_leftmost_idx(arr, key):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if key > arr[mid]:
            left = mid + 1
        else:
            right = mid

    return left if arr[left] == key else -1


def get_rightmost_idx(arr, key):
    """
    Input: [4, 6, 6, 6, 9, 9], key = 6

    Output: [1, 3]

    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1 if arr[left - 1] == key else -1


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
