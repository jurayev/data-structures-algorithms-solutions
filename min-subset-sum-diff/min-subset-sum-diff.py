def can_partition(nums):
    """
    {1, 2, 3, 9}, {} {}
           ^
     {1,2,3,9} {}
     {1,2,3} {9}
     {1,2} {3,9}


    Time O(2^n)
    Space O(2^n)
    """
    best = {"diff": float("inf")}
    backtrack(nums, 0, 0, 0, best)
    return best["diff"]


def backtrack(nums, start, sum1, sum2, best):
    if start >= len(nums):
        best["diff"] = min(best["diff"], abs(sum1 - sum2))
        return

    backtrack(nums, start + 1, sum1 + nums[start], sum2, best)
    backtrack(nums, start + 1, sum1, sum2 + nums[start], best)


def can_partition_dp(nums):
    """
    {1, 2, 3, 9}, S=16//2=8
     ^
                0 1 2 3 4 5 6 7 8
    {1}         0 1 0 0 0 0 0 0 0
    {1,2}       0 1 2 3 0 0 0 0 0
    {1,2,3}     0 1 2 3 4 5 6 0 0
    {1,2,3,9}   0 1 2 3 4 5 6 0 0

                0 1 2 3 4 5 6 7 8
    {1}         1 1 0 0 0 0 0 0 0
    {1,1}       1 1 1 0 0 0 0 0 0
    {1,1,2}     1 1 1 1 1 0 0 0 0
    {1,1,2,5}   1 1 1 1 1 1 1 1 1
    {1,1,2,5,7} 1 1 1 1 1 1 1 1 1

    Time O(N*S), N is the total numbers, S is the sum
    Space O(N*S)
    """
    total_sum = sum(nums)
    part_sum = total_sum // 2
    n = len(nums)
    dp = [[0 for _ in range(part_sum + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for j in range(1, part_sum + 1):
        dp[0][j] = int(j == nums[0])

    for i in range(1, n):
        for j in range(1, part_sum + 1):
            if j >= nums[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    first_subset_sum = 0
    for i in range(part_sum + 1):
        first_subset_sum = i if dp[-1][i] else first_subset_sum

    second_subset_sum = total_sum - first_subset_sum
    return abs(first_subset_sum - second_subset_sum)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
