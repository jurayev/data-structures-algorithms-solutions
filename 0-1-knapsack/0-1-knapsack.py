def solve_knapsack_recursive_brute_force(profits, weights, capacity):
    """
    profit = 0 # 4 # 3 #
    weight = 0 # 2 #
    max = 9
    Items: { Apple, Orange, Banana, Melon }
    Weights: { 2, 3, 1, 4 }
                        ^
    Profits: { 4, 5, 3, 7 }

    Time O(2^n)
    Space O(2^n)
    """
    max_profit = [0]
    solve(profits, weights, capacity, max_profit, 0, 0, 0)
    return max_profit[0]


def solve(profits, weights, capacity, max_profit, weight, profit, start):
    if weight > capacity:
        return
    for i in range(start, len(profits)):
        solve(profits, weights, capacity, max_profit, weight + weights[i], profit + profits[i], i + 1)

    max_profit[0] = max(max_profit[0], profit)


def solve_knapsack_2d_array(profits, weights, capacity):
    """
    capacity
              0 1 2 3 4 5
            0 0 0 0 0 0 0
            1 0 1 1 1 1 1
            2 0 1 2 3 3 3
            3 0 1 2 3 4 5
            5 0 1 2 3 4 5

            0 1 2 3 4 5
            0 1 2 3 4 5

    profits -> [1, 2, 3, 4],
    weights -> [1, 2, 3, 5]

    Time O(c*w)
    Space O(c*w)
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, capacity + 1):
            w = weights[r - 1]
            if w > c:
                dp[r][c] = dp[r - 1][c]
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r - 1][c - w] + profits[r - 1])

    return dp[-1][-1]


def solve_knapsack_1d_array(profits, weights, capacity):
    """
    capacity
            0 1 2 3 4 5
            0 1 2 3 4 5

    profits -> [1, 2, 3, 4]
    weights -> [1, 2, 3, 5]
                         ^
    Time O(c*w)
    Space O(c)
    """
    n = len(weights)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(n):
        for c in range(capacity, -1, -1):
            w = weights[i]
            if w > c:
                break
            dp[c] = max(dp[c], dp[c - w] + profits[i])

    return dp[-1]


def main():
    print(solve_knapsack_1d_array([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_1d_array([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_1d_array([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
