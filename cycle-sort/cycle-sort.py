def cyclic_sort(nums):
    """
     0  1  2  3  4  5
    [1, 2, 3, 4, 5]
                 ^

    [1, 2, 3, 4, 5, 6]
                 ^
    """

    for i in range(0, len(nums)):
        while nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    return nums
