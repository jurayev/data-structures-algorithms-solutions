def find_target_subsets(nums, s):
    """       r
              0 1 2 3 4  j
    {1}       0 1 0 0 0
    {1,1}     0 1 2 0 0
    {1,1,2}   0 1 2 3 4
    {1,1,2,3} 0 1 2 3 4

    """
    s2 = (s + sum(nums)) // 2
    n = len(nums)

    dp = [[0 for _ in range(s2 + 1)] for _ in range(n)]

    dp[0][nums[0]] = nums[0]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, s2 + 1):
            if nums[i] <= j:
                dp[i][j] += dp[i - 1][j - nums[i]]
            dp[i][j] += dp[i - 1][j]

    return dp[-1][-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
