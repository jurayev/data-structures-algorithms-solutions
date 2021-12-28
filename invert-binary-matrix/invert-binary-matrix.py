def flip_and_invert_image(matrix):
  """
  0 ^ 1 = 1
  1 ^ 1 = 0
  """
  for row in matrix:
    reverse(row)
    for i in range(len(row)):
      row[i] = row[i] ^ 1
  return matrix

def reverse(arr):
  left, right = 0, len(arr)-1
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

def main():
  print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
  print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()