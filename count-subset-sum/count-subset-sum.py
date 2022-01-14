def count_subsets(nums, sum):
    """       r
              0 1 2 3 4  j
    {1}       0 1 0 0 0
    {1,1}     0 1 2 0 0
    {1,1,2}   0 1 2 3 4
    {1,1,2,3} 0 1 2 3 4

    """
    n = len(nums)

    dp = [[0 for _ in range(sum + 1)] for _ in range(n)]

    dp[0][nums[0]] = nums[0]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, sum + 1):
            if nums[i] <= j:
                dp[i][j] += dp[i - 1][j - nums[i]]
            dp[i][j] += dp[i - 1][j]

    return dp[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
