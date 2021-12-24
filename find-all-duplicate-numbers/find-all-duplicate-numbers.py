def find_all_duplicates(nums):
  duplicateNumbers = []
  n = len(nums)
  for i in range(n):
    j = nums[i] - 1
    while nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
      j = nums[i] - 1

  for i in range(n):
    if i+1 != nums[i]:
      duplicateNumbers.append(nums[i])

  return duplicateNumbers
