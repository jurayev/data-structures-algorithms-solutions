def find_single_numbers(nums):
    x1x2 = 0
    for num in nums:
        x1x2 ^= num

    rightmost_bit = 1

    for i in range(0, 32):
        if x1x2 & (1 << i) != 0:
            rightmost_bit = i
            break

    res1 = 0
    res2 = 0
    for num in nums:
        if num & (1 << rightmost_bit) != 0:
            res1 ^= num
        else:
            res2 ^= num
    return [res1, res2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 2, 3, 5, 11])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
