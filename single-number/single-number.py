def find_single_number(arr):
  res = 1
  for num in arr:
    res ^= num
  return res ^ 1

def main():
    arr = [1, 4, 2, 4, 3, 2, 3]
    print(find_single_number(arr))

main()
