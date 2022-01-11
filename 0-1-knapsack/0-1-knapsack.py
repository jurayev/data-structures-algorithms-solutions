def solve_knapsack_brute_force(profits, weights, capacity):
    """
      profit = 0 # 4 # 3 #
      weight = 0 # 2 #
      max = 9
      Items: { Apple, Orange, Banana, Melon }
      Weights: { 2, 3, 1, 4 }
                          ^
      Profits: { 4, 5, 3, 7 }

    Time Complexity: O(2^N)
    Space Complexity O(2^N)
    """
    max_profit = [0]
    solve_brute_force(profits, weights, capacity, max_profit, 0, 0, 0)
    return max_profit[0]


def solve_brute_force(profits, weights, capacity, max_profit, weight, profit, start):
    if weight > capacity:
        return
    for i in range(start, len(profits)):
        solve_brute_force(profits, weights, capacity, max_profit, weight + weights[i], profit + profits[i], i + 1)

    max_profit[0] = max(max_profit[0], profit)
