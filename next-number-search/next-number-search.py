def search_ceiling_of_a_number(arr, key):
  # [1, 3, 8, 10, 15], key = 2
  n = len(arr)
  left, right = 0, n-1

  while left < right:
    mid = left + (right-left) // 2
    if arr[mid] == key:
      return mid

    if key < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1

  return left if arr[left] >= key else -1


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()