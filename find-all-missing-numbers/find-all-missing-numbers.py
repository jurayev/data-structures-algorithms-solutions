def find_missing_numbers(nums):
  missingNumbers = []
  """
   0  1  2  3
  [1, 2, 2, 4]
            ^
  [3, 3, 1, 2]
  [1, 2, 3, 3]
   0  1  2  3  4. 5  6  7
  [1, 2, 3, 1, 5, 3, 2, 8]
                     ^
  """
  n = len(nums)
  for i in range(n):
    j = nums[i] - 1
    while nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
      j = nums[i] - 1

  print(nums)
  for i in range(n):
    print(nums[i], i+1)
    if nums[i] != i+1:
      missingNumbers.append(i+1)
  return missingNumbers
