def binary_search(arr, key):
    """
    target = 1
    [1, 2, 3, 4, 5, 6, 7]

    target = 4
    [10, 6, 4, 3, 1]

    """
    ord_reversed = bool(arr and arr[0] > arr[-1])
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            if ord_reversed:
                right = mid
            else:
                left = mid + 1
        else:
            if ord_reversed:
                left = mid + 1
            else:
                right = mid
    return left if arr[left] == key else -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10, 6, 4, 3, 2, 1], 5))
    print(binary_search([10, 6, 4, 3, 2, 1], 0))
    print(binary_search([10, 6, 4, 3, 2, 1], 11))


main()
