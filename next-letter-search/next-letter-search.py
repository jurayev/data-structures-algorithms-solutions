def search_next_letter(letters, key):
  # ['a', 'c', 'f', 'h'], key = 'h'
  if not letters:
    return 'a'
  n = len(letters)

  left, right = 0 , n-1

  while left < right:
    mid = left + (right-left) // 2
    if key > letters[mid]:
      left = mid+1
    else:
      right = mid

  return letters[left] if letters[left] > key else letters[(left+1)%n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'a'))
  print(search_next_letter(['b', 'c', 'f', 'h'], 'a'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))


main()